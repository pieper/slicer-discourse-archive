# Is there a way to export in 3mf file format?

**Topic ID**: 46130
**Date**: 2026-02-12
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-export-in-3mf-file-format/46130

---

## Post #1 by @HelloAll (2026-02-12 07:05 UTC)

<p>Hi.  I’m new to 3D Slicer.  Is there a way to export files in 3mf format to make printing different segments with different colors easier?</p>

---

## Post #2 by @pieper (2026-02-12 15:00 UTC)

<aside class="quote no-group" data-username="HelloAll" data-post="1" data-topic="46130">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/59ef9b/48.png" class="avatar"> HelloAll:</div>
<blockquote>
<p>3mf format to make printing</p>
</blockquote>
</aside>
<p>Not that I’m aware of, but it probably would not be hard for someone to add.</p>

---

## Post #3 by @lassoan (2026-02-14 05:28 UTC)

<p>You can ask any modern AI chatbot to write the Python script for you that writes a model node in Slicer to a 3mf file. The prompt can be something like this: <code>Generate Python code that writes a 3mf file from a model node in Slicer</code>.</p>
<p>To make this file format conveniently available in the scene save or node export options then you can ask the AI chatbot to create a “scripted file writer plugin” using <a href="https://github.com/Slicer/Slicer/blob/main/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py">this file</a> as an example. If the file writer works well and you share it with us then we can add it to an extension, such as the <code>Sandbox</code> so that anyone can install it by a few clicks.</p>

---

## Post #4 by @lassoan (2026-02-14 06:48 UTC)

<p>I went ahead and implemented this. If you install the Sandbox extension tomorrow or later then you will be able to save model nodes in .3mf format.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/blob/master/ExportModelTo3mf/ExportModelTo3mf.py">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ExportModelTo3mf/ExportModelTo3mf.py" target="_blank" rel="noopener">github.com/PerkLab/SlicerSandbox</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ExportModelTo3mf/ExportModelTo3mf.py" target="_blank" rel="noopener">ExportModelTo3mf/ExportModelTo3mf.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ExportModelTo3mf/ExportModelTo3mf.py" rel="noopener"><code>master</code></a>
</div>


      <pre><code class="lang-py">import logging
import os
import vtk
import qt
import ctk
import slicer
from slicer.ScriptedLoadableModule import *


class ExportModelTo3mf(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Export Model to 3MF"
        self.parent.categories = ["Surface Models"]
        self.parent.dependencies = []
        self.parent.contributors = ["Andras Lasso (PerkLab)"]
</code></pre>



  This file has been truncated. <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ExportModelTo3mf/ExportModelTo3mf.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
