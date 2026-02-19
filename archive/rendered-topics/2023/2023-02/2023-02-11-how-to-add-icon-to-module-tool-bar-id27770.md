---
topic_id: 27770
title: "How To Add Icon To Module Tool Bar"
date: 2023-02-11
url: https://discourse.slicer.org/t/27770
---

# How to add icon to Module Tool Bar

**Topic ID**: 27770
**Date**: 2023-02-11
**URL**: https://discourse.slicer.org/t/how-to-add-icon-to-module-tool-bar/27770

---

## Post #1 by @Mauricio_Cespedes (2023-02-11 13:57 UTC)

<p>Hi,</p>
<p>I’m building some simple Slicer extension with Python and one of the things I want to implement in one of the modules is to add a widget to the ModuleToolBar. I’m currently doing this through this function:</p>
<pre><code class="lang-auto">def modifyWindowUI(self):
        mainToolBar = slicer.util.findChild(slicer.util.mainWindow(), 'ModuleToolBar')
        add_widget = True
        for element in mainToolBar.actions():
            if element.text == "vCastSender":
                add_widget = False
        if add_widget:        
            moduleIcon = qt.QIcon(self.resourcePath('Icons/BrainZoneClassifier.png'))
            self.StyleAction = mainToolBar.addAction(moduleIcon, "vCastSender")
            self.StyleAction.triggered.connect(self.toggleStyle)
</code></pre>
<p>And then I called this function in the setup function for the module:</p>
<pre><code class="lang-auto">    def setup(self):
        """
        Called when the user opens the module the first time and the widget is initialized.
        """
        ScriptedLoadableModuleWidget.setup(self)
        # Custom toolbar for applying style
        self.modifyWindowUI()

        self._loadUI()
        self.logic = BrainZoneClassifierLogic()

        # Connections
        self._setupConnections()
</code></pre>
<p>So this is working fine but I’ve seen that the behaviour is that, after launching slicer, the icon is included in the toolbar until I select the module (in the modules dropdown). Is there a way to setup the module when Slicer is launched? Or is there any approach to have my module icon in the toolbar after Slicer is initialized (without the need of changing to the module tab)?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2023-02-11 17:12 UTC)

<p>You can use the <a href="https://github.com/Slicer/Slicer/search?p=2&amp;q=startupCompleted"><code>startupCompleted()</code></a> signal to trigger things like this.</p>

---

## Post #3 by @Mauricio_Cespedes (2023-02-13 15:38 UTC)

<p>Amazing! Thanks so much!</p>

---
