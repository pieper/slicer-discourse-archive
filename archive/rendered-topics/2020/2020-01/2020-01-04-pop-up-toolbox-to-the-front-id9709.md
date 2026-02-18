# Pop-up ToolBox to the front

**Topic ID**: 9709
**Date**: 2020-01-04
**URL**: https://discourse.slicer.org/t/pop-up-toolbox-to-the-front/9709

---

## Post #1 by @apparrilla (2020-01-04 16:57 UTC)

<p>I want to make a pop-up toolbox to show/hide it with a button in main window</p>
<blockquote>
<p>self.ToolBoxCheck = qt.QCheckBox(‘Show ToolBox’)<br>
self.ToolBoxCheck.connect(‘clicked(bool)’, self.ShowToolBox)<br>
Layout.addRow(self.ToolBoxCheck)<br>
self.ToolBox_widget = slicer.util.loadUI(“E:/MyExtension/Resources/UI/ToolBox.ui”)<br>
self.Button_widget = self.ToolBox_widget .findChild(qt.QPushButton, ‘Button1’)</p>
</blockquote>
<p>CheckBox works perfect launching widget window but I don´t know how to make it always on top.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-01-04 17:32 UTC)

<p>While it might be possible to keep a widget always on top, the proper solution would be to place it in the application window’s layout: a docking window (as it is done in <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/NodeInfo/NodeInfo.py">NodeInfo module</a>) or add a custom toolbar (as it is done in <a href="https://github.com/SlicerRt/Sequences/blob/master/SequenceBrowser/qSlicerSequenceBrowserModule.cxx">Sequences module</a>). You can make both docking widgets and toolbars float over the GUI or dock any side of the application window.</p>

---

## Post #3 by @apparrilla (2020-01-04 19:20 UTC)

<p>Ok. I have a DockWidget working as you propose in NodeInfo module example and it´s really cool.<br>
I have turn my ToolBar to a DockWidget in Qt Designer.  How can i use it?<br>
It throw me this error:</p>
<blockquote>
<p>.setFeatures(qt.QDockWidget.DockWidgetClosable + qt.QDockWidget.DockWidgetMovable + qt.QDockWidget.DockWidgetFloatable)<br>
AttributeError: QFrame has no attribute named ‘setFeatures’</p>
</blockquote>

---

## Post #4 by @lassoan (2020-01-05 03:47 UTC)

<p>The easiest way to change the base class of the top-level widget in Qt Designer is to create a new widget and copy-paste its content (see <a href="https://forum.qt.io/topic/20723/how-to-change-my-gui-base-class-qwidget-qmainwindow/14">here</a>). You may also be able to change the class by changing the .ui file in a text editor.</p>

---

## Post #5 by @apparrilla (2020-01-05 15:10 UTC)

<p>Ok. I go around it and it´s working. I send my config in case someone had same need.</p>
<p>CheckButton to show/hide ToolBox:</p>
<blockquote>
<p>self.ToolBoxCheck = qt.QCheckBox(‘Show ToolBox’)<br>
self.ToolBoxCheck.connect(‘clicked(bool)’, self.ShowToolBox)<br>
Layout.addRow(self.ToolBoxCheck)</p>
</blockquote>
<blockquote>
<p>def ShowToolBox(self, pressed):<br>
if pressed:<br>
self.ToolBox_widget.show()<br>
else:<br>
self.ToolBox_widget.hide()</p>
</blockquote>
<p>Add ToolBox Widget to Layout:</p>
<blockquote>
<p>self.ToolBox_widget = slicer.util.loadUI(“E:/MyExtension/Resources/UI/ToolBox.ui”)<br>
self.Button_widget = self.ToolBox_widget.findChild(qt.QPushButton, ‘Button1’)<br>
mainWindow = slicer.util.mainWindow()<br>
mainWindow.addDockWidget(qt.Qt.RightDockWidgetArea, self.ToolBox_widget)</p>
</blockquote>
<p>QtWidget has this structure:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e4837154462c4426325c4320ca9f61710d221f6.png" data-download-href="/uploads/short-url/kiGwj3UlXVOnoJj2zT06E3BY5Ey.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e4837154462c4426325c4320ca9f61710d221f6.png" alt="image" data-base62-sha1="kiGwj3UlXVOnoJj2zT06E3BY5Ey" width="490" height="375" data-dominant-color="29394A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">723×552 9.32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks very much <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #6 by @lassoan (2020-01-05 15:19 UTC)

<p>It’s great that you could make this work for you. Just one more recommendation: instead of using findChild for each button, you can automatically get all of them at once by calling <a href="https://github.com/Slicer/Slicer/blob/b6bf2d30c99f731644182f750a4abd8e3c8204ca/Base/Python/slicer/util.py#L299"><code>slicer.util. childWidgetVariables</code></a>.</p>

---
