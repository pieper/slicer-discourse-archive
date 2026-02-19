---
topic_id: 33132
title: "Create New Qslicerwidget"
date: 2023-11-30
url: https://discourse.slicer.org/t/33132
---

# Create new qSlicerWidget

**Topic ID**: 33132
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/create-new-qslicerwidget/33132

---

## Post #1 by @Victor_Manuel_Montan (2023-11-30 04:38 UTC)

<p>I am developing a new qSlicerWidget that should be shown when a button that is part of a qMRMLWidget is clicked. When the new qSlicerWidget is created empty, it is possible to see the new window without any elements inside.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d867ab7e0dd75c89ac7f7d9771f7e5fd7cc7bcf.jpeg" data-download-href="/uploads/short-url/dlmwzU5lHOuRgp2mOn23qBuqncr.jpeg?dl=1" title="Captura de pantalla 2023-11-29 a la(s) 9.00.33 a.m." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d867ab7e0dd75c89ac7f7d9771f7e5fd7cc7bcf_2_690x418.jpeg" alt="Captura de pantalla 2023-11-29 a la(s) 9.00.33 a.m." data-base62-sha1="dlmwzU5lHOuRgp2mOn23qBuqncr" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d867ab7e0dd75c89ac7f7d9771f7e5fd7cc7bcf_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d867ab7e0dd75c89ac7f7d9771f7e5fd7cc7bcf_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d867ab7e0dd75c89ac7f7d9771f7e5fd7cc7bcf_2_1380x836.jpeg 2x" data-dominant-color="353439"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-11-29 a la(s) 9.00.33 a.m.</span><span class="informations">1920×1165 86.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I try to load a UI created from qtStudio in a UI file that contains a widget. The class is in a new file as shown below:</p>
<pre data-code-wrap="python"><code class="lang-python">import slicer
import os

class TutorialGUI(slicer.qSlicerWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        print(self)
        dir_path = os.path.dirname(__file__)
        
        self.Widget = slicer.util.loadUI(dir_path+'/../Resources/UI/TutorialGUI.ui')
        self.layout.addWidget(self.Widget)

    def showEvent(self, event):
        # Do something when the window is shown
        print("The window is shown!")
</code></pre>
<p>in python console shows following error message:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/Users/victormontanoserrano/Documents/3DSlicer/NewGui/NewGUI/NewGUI.py", line 141, in __init__
    self.window = TutorialGUI()
  File "/Users/victormontanoserrano/Documents/3DSlicer/NewGui/NewGUI/Lib/TutorialGUI.py", line 11, in __init__
    self.layout.addWidget(self.Widget)
AttributeError: 'builtin_qt_slot' object has no attribute 'addWidget'
[Qt] qSlicerPythonCppAPI::instantiateClass  - [ "NewGUIWidget" ] - Failed to instantiate scripted pythonqt class "NewGUIWidget" 0x7fcbb551fba0
</code></pre>

---

## Post #2 by @lassoan (2023-11-30 04:46 UTC)

<p>The error message tells that <code>self.layout</code> is a slot. Probably you wanted to write <code>self.layout()</code> instead.</p>

---

## Post #3 by @Victor_Manuel_Montan (2023-12-01 19:08 UTC)

<p>Thanks for the comment. I made the change but it was not the solution.</p>
<p>I solved the problem in the following way.</p>
<pre data-code-wrap="python"><code class="lang-python">import qt
import slicer
import os

class TutorialGUI(slicer.qSlicerWidget):
    def __init__(self, parent=None):
        super().__init__()

        # Load a UI file
        dir_path = os.path.dirname(__file__)
        self.uiWidget = slicer.util.loadUI(dir_path+'/../Resources/UI/TutorialMaker.ui')
        
        # Create a new accessible qt layout component
        self.newlayout = qt.QVBoxLayout()
        
        # Add Widget from IU file to new layout
        self.newlayout.addWidget(self.uiWidget)

        # Set self layout with UI components 
        self.setLayout(self.newlayout)
</code></pre>

---
