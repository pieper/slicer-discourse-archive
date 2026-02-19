---
topic_id: 20472
title: "Add A Menu To Slicecontroller"
date: 2021-11-03
url: https://discourse.slicer.org/t/20472
---

# Add a menu to sliceController

**Topic ID**: 20472
**Date**: 2021-11-03
**URL**: https://discourse.slicer.org/t/add-a-menu-to-slicecontroller/20472

---

## Post #1 by @mau_igna_06 (2021-11-03 13:11 UTC)

<p>Hi. This is my code to add a menu to the Red Slice controller:</p>
<pre><code class="lang-auto">toolButton = qt.QToolButton()

toolButton = qt.QToolButton()
toolButton.setText('T')
slicer.app.layoutManager().sliceWidget("Red").sliceController().barLayout().insertWidget(0,toolButton)

myMenu = qt.QMenu(toolButton)
toolButton.setMenu(myMenu)

pushButton = qt.QPushButton('mybutton')
widgetAction = qt.QWidgetAction(myMenu)
widgetAction.setDefaultWidget(pushButton)

myMenu.addAction(widgetAction)
myMenu.addAction("testAction")
</code></pre>
<p>It doesn’t work. The actions do not show when you click the toolButton. Could you help?</p>

---

## Post #2 by @jamesobutler (2021-11-03 18:22 UTC)

<p>The default popup mode is <code>DelayedPopup</code> for a QToolButton. I believe you have missed this as showing the action does work with your code when long pressing on the toolbutton.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bd3ab968845851303ff415989a245ee19988394.png" alt="image" data-base62-sha1="d6kWYEKhz8gzZ2cykaAz5neLeNS" width="157" height="90"></p>
<pre data-code-wrap="python"><code class="lang-python"># Create ToolButton and add to sliceController
toolButton = qt.QToolButton()
slicer.app.layoutManager().sliceWidget("Red").sliceController().barLayout().insertWidget(0,toolButton)
# Create QMenu and add QActions to it
myMenu = qt.QMenu(toolButton)
myActionT = qt.QAction("T")
myActionTest = qt.QAction("Test")
myMenu.addAction(myActionT)
myMenu.addAction(myActionTest)
# Add Menu to ToolButton
toolButton.setMenu(myMenu)
# Want to define one of the menu items so it is triggered on toolbutton press? set it as default action
toolButton.setDefaultAction(myActionT)

# Default to show menu is DelayedPopup method which requires long press
# Long press is to differentiate it from pressing ToolButton (the default QAction)

# Want a different method to show menu?
# Other options include arrow next to button to open menu
toolButton.setPopupMode(qt.QToolButton.MenuButtonPopup)
# Open the menu by clicking the toolbutton rather than triggering the default QAction
toolButton.setPopupMode(qt.QToolButton.InstantPopup)
</code></pre>

---
