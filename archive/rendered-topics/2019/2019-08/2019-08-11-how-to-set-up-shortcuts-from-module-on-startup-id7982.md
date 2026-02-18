# How to set up shortcuts from module on startup?

**Topic ID**: 7982
**Date**: 2019-08-11
**URL**: https://discourse.slicer.org/t/how-to-set-up-shortcuts-from-module-on-startup/7982

---

## Post #1 by @Amine (2019-08-11 23:41 UTC)

<p>Hi, to register keyboard shortcuts from a scripted module i have been putting the code in the setup method of my widget class, however there is a need to run each module to register its shortcuts, where should shortcut registration be placed in a module so it can run as soon as slicer starts?<br>
I tried setting it as a separate method in widget class then call it but then i get "Failed to obtain reference to ‘qSlicerMainWindow’ " error</p>
<pre><code>def Register_Shortcuts():
    def funct():
        print("OKAY")
    shortcuts = [
        ('x', funct),
        ('b', funct)]
    for (shortcutKey, callback) in shortcuts:
        shortcut = qt.QShortcut(slicer.util.mainWindow())
        shortcut.setKey(qt.QKeySequence(shortcutKey))
        shortcut.connect('activated()', callback)
Register_Shortcuts()</code></pre>

---

## Post #2 by @pieper (2019-08-12 12:15 UTC)

<p>Hi -</p>
<p>A couple options - if it’s just for the user you can put the code <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/slicerqt.py#L103-L127" rel="nofollow noopener">in ~/.slicerrc.py</a>.  Or if you want this to be part of the module you can use <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L43" rel="nofollow noopener">the startupComplete() signal from the application</a> to trigger the code.</p>

---

## Post #3 by @Amine (2019-08-12 15:45 UTC)

<p>Thanks a lot.<br>
Indeed slicerrc needs to be edited which is not ideal for module sharing.<br>
startupComplete() signal is exactly what i was looking for. Thanks a lot for your help.</p>
<p>Note to interested people: i had to put in the <strong>init</strong> method of the main module class to be run at slicer’s startup</p>

---

## Post #4 by @ungi (2019-08-12 21:32 UTC)

<p>If there is a risk of shortcuts conflicting between modules, and you only want to use specific shortcuts in your module, you could have a look at this example (search for “shortcut” in the code). It installs shortcuts when you enter the module, but uninstalls them when you switch to a different module.<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerIGT/UsAnnotationExport/blob/master/SlicerExtension/UsAnnotationExport/SingleSliceSegmentation/SingleSliceSegmentation.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/UsAnnotationExport/blob/master/SlicerExtension/UsAnnotationExport/SingleSliceSegmentation/SingleSliceSegmentation.py" target="_blank" rel="nofollow noopener">SlicerIGT/UsAnnotationExport/blob/master/SlicerExtension/UsAnnotationExport/SingleSliceSegmentation/SingleSliceSegmentation.py</a></h4>
<pre><code class="lang-py">from __future__ import print_function
import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

import numpy as np


#
# SingleSliceSegmentation
#

class SingleSliceSegmentation(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
</code></pre>

  This file has been truncated. <a href="https://github.com/SlicerIGT/UsAnnotationExport/blob/master/SlicerExtension/UsAnnotationExport/SingleSliceSegmentation/SingleSliceSegmentation.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #5 by @Amine (2019-08-13 20:42 UTC)

<p>Thanks for the precision, that will definitely come in handy,<br>
i don’t see how enter and exit methods (lines 317 and 375) get called? do slicer recognize their names and runs them automatically like the setup method?</p>

---

## Post #6 by @pieper (2019-08-13 20:53 UTC)

<aside class="quote no-group" data-username="Amine" data-post="5" data-topic="7982">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>i don’t see how enter and exit methods (lines 317 and 375) get called? do slicer recognize their names and runs them automatically like the setup method?</p>
</blockquote>
</aside>
<p>yes, it does automatically call them</p>

---

## Post #7 by @Amine (2019-08-13 21:04 UTC)

<p>Quite useful, Thanks for your help!</p>

---

## Post #8 by @dalv.silvermann (2022-08-07 19:19 UTC)

<p>Dear Tamas,<br>
Could you please reload the link?</p>

---

## Post #9 by @ungi (2022-08-07 19:50 UTC)

<p>It’s better to take examples from the official script repository: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#keyboard-shortcuts-and-mouse-gestures" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>But here it is:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/aigt/blob/30bbb67ecbfdd6bc27a954803cbd211829814478/SlicerExtension/LiveUltrasoundAi/SingleSliceSegmentation/SingleSliceSegmentation.py#L75">
  <header class="source">

      <a href="https://github.com/SlicerIGT/aigt/blob/30bbb67ecbfdd6bc27a954803cbd211829814478/SlicerExtension/LiveUltrasoundAi/SingleSliceSegmentation/SingleSliceSegmentation.py#L75" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/aigt/blob/30bbb67ecbfdd6bc27a954803cbd211829814478/SlicerExtension/LiveUltrasoundAi/SingleSliceSegmentation/SingleSliceSegmentation.py#L75" target="_blank" rel="noopener nofollow ugc">SlicerIGT/aigt/blob/30bbb67ecbfdd6bc27a954803cbd211829814478/SlicerExtension/LiveUltrasoundAi/SingleSliceSegmentation/SingleSliceSegmentation.py#L75</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="65" style="counter-reset: li-counter 64 ;">
          <li>  ScriptedLoadableModuleWidget.__init__(self, parent)</li>
          <li>
          <li>  self.logic = SingleSliceSegmentationLogic()</li>
          <li>
          <li>  # Members</li>
          <li>
          <li>  self.parameterSetNode = None</li>
          <li>  self.editor = None</li>
          <li>  self.ui = None</li>
          <li>  </li>
          <li class="selected">  # Shortcuts</li>
          <li>
          <li>  self.shortcutS = qt.QShortcut(slicer.util.mainWindow())</li>
          <li>  self.shortcutS.setKey(qt.QKeySequence('s'))</li>
          <li>  self.shortcutD = qt.QShortcut(slicer.util.mainWindow())</li>
          <li>  self.shortcutD.setKey(qt.QKeySequence('d'))</li>
          <li>  self.shortcutC = qt.QShortcut(slicer.util.mainWindow())</li>
          <li>  self.shortcutC.setKey(qt.QKeySequence('c'))</li>
          <li>
          <li>def setup(self):</li>
          <li>  ScriptedLoadableModuleWidget.setup(self)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
