# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class ComponentPlacementDialog
###########################################################################

class ComponentPlacementDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Component Placement", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		radioOriginChoices = [ u"Gird Origin", u"Drill Origin", u"Page Origin" ]
		self.radioOrigin = wx.RadioBox( self, wx.ID_ANY, u"Origin", wx.DefaultPosition, wx.DefaultSize, radioOriginChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioOrigin.SetSelection( 0 )
		bSizer10.Add( self.radioOrigin, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"DNP field name" ), wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.radioDefault = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Default (from KiCad v7)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.radioDefault, 0, wx.ALL, 5 )

		self.radioOther = wx.RadioButton( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Other", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.radioOther, 0, wx.ALL, 5 )


		sbSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )

		self.textDnp = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Components with this field not empty will be ignored", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textDnp.Wrap( -1 )

		sbSizer5.Add( self.textDnp, 0, wx.ALL, 5 )

		choiceDnpChoices = []
		self.choiceDnp = wx.Choice( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDnpChoices, 0 )
		self.choiceDnp.SetSelection( 0 )
		sbSizer5.Add( self.choiceDnp, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Add custom fields:" ), wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		self.m_scrolledWindow1.SetMinSize( wx.Size( -1,200 ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.gridCustom = wx.grid.Grid( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridCustom.CreateGrid( 0, 2 )
		self.gridCustom.EnableEditing( True )
		self.gridCustom.EnableGridLines( True )
		self.gridCustom.EnableDragGridSize( False )
		self.gridCustom.SetMargins( 0, 0 )

		# Columns
		self.gridCustom.AutoSizeColumns()
		self.gridCustom.EnableDragColMove( False )
		self.gridCustom.EnableDragColSize( True )
		self.gridCustom.SetColLabelValue( 0, u"Add" )
		self.gridCustom.SetColLabelValue( 1, u"Name" )
		self.gridCustom.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridCustom.EnableDragRowSize( False )
		self.gridCustom.SetRowLabelSize( wx.grid.GRID_AUTOSIZE )
		self.gridCustom.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridCustom.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_TOP )
		bSizer5.Add( self.gridCustom, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer5 )
		self.m_scrolledWindow1.Layout()
		bSizer5.Fit( self.m_scrolledWindow1 )
		sbSizer3.Add( self.m_scrolledWindow1, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer10.Add( sbSizer3, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonGenerate = wx.Button( self, wx.ID_ANY, u"Generate Position File", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonGenerate, 0, wx.ALL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonClear = wx.Button( self, wx.ID_ANY, u"Clear Logs", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonClear, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 0, wx.EXPAND, 5 )


		bSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )

		self.staticline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.staticline, 0, wx.EXPAND |wx.ALL, 5 )

		self.textLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.textLog, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.gridCustom.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.OnGridCustom )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnGridCustom( self, event ):
		event.Skip()


