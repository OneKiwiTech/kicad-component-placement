# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class ComponentPlacementDialog
###########################################################################

class ComponentPlacementDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Component Placement", pos = wx.DefaultPosition, size = wx.Size( 400,350 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		boxMain = wx.BoxSizer( wx.VERTICAL )

		radioOriginChoices = [ u"Drill Origin", u"Gird Origin" ]
		self.radioOrigin = wx.RadioBox( self, wx.ID_ANY, u"Origin", wx.DefaultPosition, wx.DefaultSize, radioOriginChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioOrigin.SetSelection( 0 )
		boxMain.Add( self.radioOrigin, 0, wx.ALL|wx.EXPAND, 5 )

		radioUnitChoices = [ u"millimeters", u"mils", u"inches" ]
		self.radioUnit = wx.RadioBox( self, wx.ID_ANY, u"Unit", wx.DefaultPosition, wx.DefaultSize, radioUnitChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioUnit.SetSelection( 0 )
		boxMain.Add( self.radioUnit, 0, wx.ALL|wx.EXPAND, 5 )

		boxDnp = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"DNP field name" ), wx.VERTICAL )

		self.textDnp = wx.StaticText( boxDnp.GetStaticBox(), wx.ID_ANY, u"Components with this field not empty will be ignored", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textDnp.Wrap( -1 )

		boxDnp.Add( self.textDnp, 0, wx.ALL, 5 )

		comboDnpChoices = []
		self.comboDnp = wx.ComboBox( boxDnp.GetStaticBox(), wx.ID_ANY, u"-None-", wx.DefaultPosition, wx.DefaultSize, comboDnpChoices, 0 )
		boxDnp.Add( self.comboDnp, 0, wx.ALL|wx.EXPAND, 5 )


		boxMain.Add( boxDnp, 0, wx.ALL|wx.EXPAND, 5 )

		self.buttonGenerate = wx.Button( self, wx.ID_ANY, u"Generate Position File", wx.DefaultPosition, wx.DefaultSize, 0 )
		boxMain.Add( self.buttonGenerate, 0, wx.ALL, 5 )

		self.textStatus = wx.StaticText( self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textStatus.Wrap( -1 )

		boxMain.Add( self.textStatus, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.textAbout = wx.StaticText( self, wx.ID_ANY, u"About", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textAbout.Wrap( -1 )

		bSizer2.Add( self.textAbout, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.hyperLink = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"OneKiwi", u"https://github.com/OneKiwiTech", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		bSizer2.Add( self.hyperLink, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		boxMain.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( boxMain )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnInitDialog )
		self.radioOrigin.Bind( wx.EVT_RADIOBOX, self.OnOriginChange )
		self.radioUnit.Bind( wx.EVT_RADIOBOX, self.OnUnitChange )
		self.comboDnp.Bind( wx.EVT_COMBOBOX, self.OnDnpChange )
		self.buttonGenerate.Bind( wx.EVT_BUTTON, self.OnGenerateClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnInitDialog( self, event ):
		event.Skip()

	def OnOriginChange( self, event ):
		event.Skip()

	def OnUnitChange( self, event ):
		event.Skip()

	def OnDnpChange( self, event ):
		event.Skip()

	def OnGenerateClick( self, event ):
		event.Skip()


