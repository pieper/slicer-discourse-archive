---
topic_id: 33251
title: "Make Custom Application Changing Ui Ux Design"
date: 2023-12-06
url: https://discourse.slicer.org/t/33251
---

# Make custom application - changing UI/UX design

**Topic ID**: 33251
**Date**: 2023-12-06
**URL**: https://discourse.slicer.org/t/make-custom-application-changing-ui-ux-design/33251

---

## Post #1 by @park (2023-12-06 14:24 UTC)

<p>Hi</p>
<p>I’m working on creating a custom app based on Slicer. The functional aspects are completed, and I’m currently in the process of updating the UI/UX for user convenience.</p>
<p>While exploring the options for updating the UI design, I found that styling changes can be made using the Slicer sandbox’s QSS sheets. However, it seems there are limitations to achieving the level of design I have in mind.</p>
<p>I’m currently thinking of a design change similar to the NousNav project. Additionally, I’d like to apply elements designed in Figma to Slicer if possible.</p>
<p>What can I do to achieve this? Also, is it possible to obtain an example code, similar to NousNav? I appreciate any advice you can provide.</p>

---

## Post #2 by @pieper (2023-12-06 14:51 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> has done a <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/SlicerThemesExtension/">lot of work</a> on this and as I understand it there are some places where getting the Qt infrastructure to behave consistently can be a challenge, often due to older code that may have had workaround for older Qt or to to achieve a particular effect.  In general it should be possible to fix or replace any component.  Maybe if you have a specific example you are trying to achieve then people would have suggestions.</p>

---

## Post #3 by @Sam_Horvath (2023-12-06 20:21 UTC)

<p>So, the NousNav work was done heavily with style sheets (<a href="https://gist.github.com/sjh26/984d2c753502ea4fdace1e2203b2c68c">style sheet</a>), removing ui elements with slicer.util functions, and adding some custom elements (most notably the tab bar at the top)</p>
<p>Custom icons were included in the module resources and used from there.  You can also register icons with the Qt resource system to be able to address them from QSS.</p>
<p>Code snippet of setting up tool/tab bars and such from the NousNav setup code</p>
<pre data-code-wrap="python"><code class="lang-python"># Create primary toolbar
    slicer.util.mainWindow().addToolBarBreak()
    self.primaryToolBar = qt.QToolBar("PrimaryToolBar")
    self.primaryToolBar.setObjectName("PrimaryToolBar")
    self.primaryToolBar.movable = False
    slicer.util.mainWindow().addToolBar(self.primaryToolBar)

    # create secondary toolbar
    slicer.util.mainWindow().addToolBarBreak()
    self.secondaryToolBar = qt.QToolBar("SecondaryToolBar")
    self.secondaryToolBar.setObjectName("SecondaryToolBar")
    self.secondaryToolBar.movable = False
    slicer.util.mainWindow().addToolBar(self.secondaryToolBar)

    # Centering widget for primary toolbar
    self.primaryTabWidget = slicer.util.loadUI(self.resourcePath('UI/CenteredWidget.ui'))
    self.primaryTabWidget.setObjectName("PrimaryCenteredWidget")
    self.primaryTabWidgetUI = slicer.util.childWidgetVariables(self.primaryTabWidget)

    # Tabs for primary toolbar
    self.primaryTabBar = qt.QTabBar()
    self.primaryTabBar.setObjectName("PrimaryTabBar")
    self.primaryTabWidgetUI.CenterArea.layout().addWidget(self.primaryTabBar)

    # Assemble primary bar
    nousNavLabel = qt.QLabel('NousNav')
    nousNavLabel.setObjectName("NousNavLabel")
    self.primaryToolBar.addWidget(nousNavLabel)
    self.primaryToolBar.addWidget(self.primaryTabWidget)

    # Settings dialog
    gearIcon = qt.QIcon(self.resourcePath('Icons/Gears.png'))
    self.settingsAction = self.primaryToolBar.addAction(gearIcon, "")
    self.settingsDialog = slicer.util.loadUI(self.resourcePath('UI/Settings.ui'))
    self.settingsUI = slicer.util.childWidgetVariables(self.settingsDialog)
    self.settingsUI.CustomUICheckBox.toggled.connect(self.setCustomUIVisible)
    self.settingsUI.ValidateCheckBox.checked = self.validateStepsDefault
    self.settingsUI.ValidateCheckBox.toggled.connect(self.setValidateSteps)
    self.settingsUI.CustomStyleCheckBox.toggled.connect(self.toggleStyle)
    self.settingsAction.triggered.connect(self.raiseSettings)
</code></pre>

---
