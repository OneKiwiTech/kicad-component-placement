import pcbnew
import os
import csv
from typing import List
from ..kicad.board import get_layer_names

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.board:pcbnew.BOARD = board
        self.offset = 1
        self.default = 1
        self.dnp = ''

    def get_field_data(self):
        fields = ['<none>']
        for footprint in self.board.GetFootprints():
            ref = footprint.GetReference()
            props = {}
            # kicad v7
            if hasattr(footprint, "GetProperties"):
                props = footprint.GetProperties()
             # kicad v8
            if hasattr(footprint, "GetFieldsText"):
                props = footprint.GetFieldsText()
            for key in props.keys():
                if key not in fields:
                    fields.append(key)
        if 'Sheetname' in fields:
            fields.remove('Sheetname')
        if 'Sheetfile' in fields:
            fields.remove('Sheetfile')
        if 'ki_description' in fields:
            fields.remove('ki_description')
        if 'ki_keywords' in fields:
            fields.remove('ki_keywords')
        if 'dnp' in fields:
            fields.remove('dnp')
        return fields
    
    def create_file(self):
        pathname = str(self.board.GetFileName())
        dir = os.path.dirname(pathname)
        base = os.path.basename(pathname)
        name = os.path.splitext(base)[0]
        name_smt = "pos_" + name + ".csv"
        
        csv_file = os.path.join(dir, "", name_smt)
        
        try:
            # check if File exist
            if os.path.exists(csv_file):
                os.remove(csv_file)
            f = open(csv_file, 'w', encoding="utf-8")
        except IOError:
            e = "Can't open output file for writing: "
            print( __file__, ":", e, sys.stderr )
            f = sys.stdout
          
        # page origin
        origin = pcbnew.wxPoint(0, 0)
        # grid origin
        if self.offset == 1:
            origin = self.board.GetDesignSettings().GetGridOrigin()
        # drill origin
        if self.offset == 2:
            origin = self.board.GetDesignSettings().GetAuxOrigin()

        ummX = "PosX(mm)"
        ummY = "PosY(mm)"
        umilX = "PosX(mil)"
        umilY = "PosY(mil)"
        IU_PER_MM = 1000000
        IU_PER_MILS = 25400
        
        # Create a new csv writer object to use as the output formatter
        out = csv.writer( f, lineterminator='\n', delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL )

        # Write CSV
        out.writerow([
            'Item', # number
            'References',  # E.g. U1, R1
            'Value',  # E.g. 10k, 0.1uF
            'Package',  # E.g. SMD, 0805, SOT-23-5
            'Layer',  # Top or Bottom
            'Orientation', # 0, 90, 180, 270
            ummX, # unit: mm
            ummY, # unit: mm
            umilX, # unit: mil
            umilY, # unit: mil
            'SMD', # Yes or No
        ])

        item = 0
        footprints = self.board.GetFootprints()
        footprints.sort(key=lambda x: x.GetReference())
        if self.default == 1:
            for footprint in footprints:
                category = ''
                if hasattr(footprint, "GetProperties"):
                    category = footprint.GetProperties().get('Category')
                else:
                    try:
                        category = footprint.GetFieldText('Category')
                    except:
                        category = ''

                # kicad v7
                if hasattr(footprint, "GetPropertiesNative"):
                    fields = {str(item) for item in footprint.GetPropertiesNative().keys()}
                # kicad v8
                else:
                    fields = {str(item) for item in footprint.GetFieldsText().keys()}
                    
                if 'dnp' not in fields and category != 'PCB':
                    item += 1
                    mmX = round((footprint.GetPosition().Get()[0] - origin.Get()[0])/IU_PER_MM, 4)
                    mmY = round((origin.Get()[1] - footprint.GetPosition().Get()[1])/IU_PER_MM, 4)
                    milX = round((footprint.GetPosition().Get()[0] - origin.Get()[0])/IU_PER_MILS, 4)
                    milY = round((origin.Get()[1] - footprint.GetPosition().Get()[1])/IU_PER_MILS, 4)
                    layer = "Top"
                    smd = "No"
                    if footprint.GetTypeName() == "SMD":
                        smd = "Yes"
                    if footprint.IsFlipped():
                        layer = "Bottom"
                    out.writerow([
                        item,
                        footprint.GetReference(),
                        footprint.GetValue(),
                        footprint.GetFPID().GetUniStringLibItemName(),
                        layer,
                        footprint.GetOrientationDegrees(),
                        mmX,
                        mmY,
                        milX,
                        milY,
                        smd,
                    ])
        else:
            for footprint in footprints:
                props = {}
                # kicad v7
                if hasattr(footprint, "GetProperties"):
                    props = footprint.GetProperties()
                # kicad v8
                else:
                    props = footprint.GetFieldsText()
                if props.get(self.dnp) == None or props.get(self.dnp) == "":
                    #logging.debug('%s' % footprint.GetValue())
                    #logging.debug('\t%s' % props.get(dnp))
                    item += 1
                    mmX = round((footprint.GetPosition().Get()[0] - origin.Get()[0])/IU_PER_MM, 4)
                    mmY = round((origin.Get()[1] - footprint.GetPosition().Get()[1])/IU_PER_MM, 4)
                    milX = round((footprint.GetPosition().Get()[0] - origin.Get()[0])/IU_PER_MILS, 4)
                    milY = round((origin.Get()[1] - footprint.GetPosition().Get()[1])/IU_PER_MILS, 4)
                    layer = "Top"
                    smd = "No"
                    if footprint.GetTypeName() == "SMD":
                        smd = "Yes"
                    if footprint.IsFlipped():
                        layer = "Bottom"
                    out.writerow([
                        item,
                        footprint.GetReference(),
                        footprint.GetValue(),
                        footprint.GetFPID().GetUniStringLibItemName(),
                        layer,
                        footprint.GetOrientationDegrees(),
                        mmX,
                        mmY,
                        milX,
                        milY,
                        smd,
                    ])
            
        f.close()
        return csv_file
    
    def create_file_custom(self, customs):
        pathname = str(self.board.GetFileName())
        dir = os.path.dirname(pathname)
        base = os.path.basename(pathname)
        name = os.path.splitext(base)[0]
        name_smt = "pos_" + name + ".csv"
        
        csv_file = os.path.join(dir, "", name_smt)
        
        try:
            # check if File exist
            if os.path.exists(csv_file):
                os.remove(csv_file)
            f = open(csv_file, 'w', encoding="utf-8")
        except IOError:
            e = "Can't open output file for writing: "
            print( __file__, ":", e, sys.stderr )
            f = sys.stdout
          
        # page origin
        origin = pcbnew.wxPoint(0, 0)
        # grid origin
        if self.offset == 1:
            origin = self.board.GetDesignSettings().GetGridOrigin()
        # drill origin
        if self.offset == 2:
            origin = self.board.GetDesignSettings().GetAuxOrigin()

        #ummX = "PosX(mm)"
        #ummY = "PosY(mm)"
        #umilX = "PosX(mil)"
        #umilY = "PosY(mil)"
        IU_PER_MM = 1000000
        IU_PER_MILS = 25400
        
        # Create a new csv writer object to use as the output formatter
        out = csv.writer( f, lineterminator='\n', delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL )

        headers = ['Item', 'References', 'Value', 'Package', 'Layer', 'Orientation', 
            'PosX(mm)', 'PosY(mm)', 'PosX(mil)', 'PosY(mil)', 'SMD']
        
        if self.dnp in customs:
            customs.remove(self.dnp)
        headers.extend(customs)
        print(customs)

        # Write CSV
        out.writerow(headers)

        item = 0
        footprints = self.board.GetFootprints()
        footprints.sort(key=lambda x: x.GetReference())
        for footprint in footprints:
            # kicad v7
            if hasattr(footprint, "GetPropertiesNative"):
                fields = {str(item) for item in footprint.GetPropertiesNative().keys()}
            # kicad v8
            else:
                fields = {str(item) for item in footprint.GetFieldsText().keys()}
            if 'dnp' not in fields:
                item += 1
                mmX = round((footprint.GetPosition().Get()[0] - origin.Get()[0])/IU_PER_MM, 4)
                mmY = round((origin.Get()[1] - footprint.GetPosition().Get()[1])/IU_PER_MM, 4)
                milX = round((footprint.GetPosition().Get()[0] - origin.Get()[0])/IU_PER_MILS, 4)
                milY = round((origin.Get()[1] - footprint.GetPosition().Get()[1])/IU_PER_MILS, 4)
                layer = "Top"
                smd = "No"
                if footprint.GetTypeName() == "SMD":
                    smd = "Yes"
                if footprint.IsFlipped():
                    layer = "Bottom"
                values = [item, footprint.GetReference(), footprint.GetValue(), footprint.GetFPID().GetUniStringLibItemName(),
                    layer, footprint.GetOrientationDegrees(), mmX, mmY, milX, milY, smd]
                for x in customs:
                    data = ''
                    if hasattr(footprint, "GetProperties"):
                        data = footprint.GetProperties().get(x)
                    else:
                        try:
                            data = footprint.GetFieldText(x)
                        except:
                            data = ''
                    values.append(data)
                out.writerow(values)
            
        f.close()
        return csv_file
