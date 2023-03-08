import os
import csv
import sys
import logging
import pcbnew

def get_field_data(board):
    fields = ["<none>"]
    for footprint in board.GetFootprints():
        ref = footprint.GetReference()
        props = footprint.GetProperties()
        for key in props.keys():
            if key not in fields:
                fields.append(key)
    fields.remove("Sheetname")
    fields.remove("Sheetfile")
    fields.remove("ki_description")
    fields.remove("ki_keywords")
    return fields


def create_file(board, dnp, unit, offset):
    pathname = str(board.GetFileName())
    base = os.path.basename(pathname)
    name = os.path.splitext(base)[0]
    name_smt = "pos_" + name + ".csv"
    
    csv_file = os.path.join(os.path.dirname(pathname), "", name_smt)

    try:
        # check if File exist
        if os.path.exists(csv_file):
            os.remove(csv_file)
        f = open(csv_file, 'w', encoding="utf-8")
    except IOError:
        e = "Can't open output file for writing: "
        print( __file__, ":", e, sys.stderr )
        f = sys.stdout

    # drill origin
    origin = board.GetDesignSettings().GetAuxOrigin()
    if offset == "Gird Origin":
        # grid origin
        origin = board.GetDesignSettings().GetGridOrigin()

    measurementX = "PosX(mm)"
    measurementY = "PosY(mm)"
    measurement = pcbnew.IU_PER_MM
    if unit == "mils":
        measurementX = "PosX(mil)"
        measurementY = "PosY(mil)"
        measurement = pcbnew.IU_PER_MILS
    elif unit == "inches":
        measurementX = "PosX(in)"
        measurementY = "PosY(in)"
        measurement = pcbnew.IU_PER_MILS*1000.0
    
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
        measurementX, # unit: mm
        measurementY, # unit: mm
        'SMD', # Yes or No
    ])

    item = 0
    footprints = board.GetFootprints()
    footprints.sort(key=lambda x: x.GetReference())
    for footprint in footprints:
        props = footprint.GetProperties()
        if props.get(dnp) == None or props.get(dnp) == "":
            #logging.debug('%s' % footprint.GetValue())
            #logging.debug('\t%s' % props.get(dnp))
            item += 1
            posX = round((footprint.GetPosition().Get()[0] - origin.Get()[0])/measurement, 4)
            posY = round((origin.Get()[1] - footprint.GetPosition().Get()[1])/measurement, 4)
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
                posX,
                posY,
                smd,
            ])
        
    f.close()
    return csv_file


"""
import pcbnew
board = pcbnew.GetBoard()
ref = board.FindFootprintByReference('C9')
ref = board.FindFootprintByReference('C10')
#props = ref.GetProperties()
#ref.GetPropertiesNative().keys()
#ref.GetPropertiesNative().values()
#ref.GetPropertiesNative().items()
#ref.GetPropertiesNative().items()[0][0]
props = ref.GetPropertiesNative().items()
prop = props[0]
key = prop[0]
value = prop[1]
"""