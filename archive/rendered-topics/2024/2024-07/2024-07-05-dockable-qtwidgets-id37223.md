# Dockable qtWidgets

**Topic ID**: 37223
**Date**: 2024-07-05
**URL**: https://discourse.slicer.org/t/dockable-qtwidgets/37223

---

## Post #1 by @JASON (2024-07-05 21:51 UTC)

<p>Hello,<br>
Is it possible to allow floating qtWidget UI to dock into the 3D Slicer interface?<br>
I notice that every item in the Slicer interface can be dragged &amp; dropped into panels around the viewport.<br>
Is it possible for me to use the same base same class as the ‘<strong>Error Log</strong>’ or ‘<strong>Python Console</strong>’ window, which both dock and display ‘<em>undock</em>’ and ‘<em>close</em>’ buttons when docked?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9bd68272198bce55ab431cdbaf670d2b01822b5.gif" alt="Dockable" data-base62-sha1="v4dpD3pzaxZu5tejcTsS65pnoQ5" width="357" height="500" class="animated"></p>
<pre><code class="lang-auto">window = qt.QWidget()
window.setWindowTitle('Hello World')
window.show()
</code></pre>

---

## Post #2 by @JASON (2024-07-05 21:55 UTC)

<p>Nevermind, ChatGPT help me solve it:</p>
<pre><code class="lang-auto">from __main__ import qt, slicer

# Create a dockable widget
dockWidget = qt.QDockWidget()
dockWidget.setWindowTitle("Hello Dock")
dockWidget.setFeatures(qt.QDockWidget.DockWidgetClosable | qt.QDockWidget.DockWidgetFloatable | qt.QDockWidget.DockWidgetMovable)

# Create a simple widget to put inside the dockable widget
mainWidget = qt.QWidget(dockWidget)
layout = qt.QVBoxLayout(mainWidget)
button = qt.QPushButton("Click me", mainWidget)
layout.addWidget(button)
mainWidget.setLayout(layout)

dockWidget.setWidget(mainWidget)

# Add the dockable widget to the main window
slicer.util.mainWindow().addDockWidget(qt.Qt.LeftDockWidgetArea, dockWidget)
</code></pre>

---

## Post #3 by @cpinter (2024-07-08 11:06 UTC)

<p>Thanks for posting the solution!</p>

---
