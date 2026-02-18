# How to generate a .seg.nrrd file out of multiple STLs with Python?

**Topic ID**: 34607
**Date**: 2024-02-28
**URL**: https://discourse.slicer.org/t/how-to-generate-a-seg-nrrd-file-out-of-multiple-stls-with-python/34607

---

## Post #1 by @Dzemal (2024-02-28 23:20 UTC)

<p>Hi together,<br>
I’m trying to write a code snippet in Python for a pipeline that should generate a .seg.nrrd file by using the actual DICOM and the segmented STLs. In Slicer, I have performed this by using the module ‘Segmentations’ → Import models (one by one) → Right-click on the created segmentation node and export it as a .seg.nrrd file. Are there any existing python modules or functions, which can perform exactly this operation?</p>
<p>Thanks for any clue!</p>

---

## Post #2 by @muratmaga (2024-02-28 23:33 UTC)

<p>You can perhaps take a look at SlicerMorph’s ImportSurfaceToSegment module:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImportSurfaceToSegment/ImportSurfaceToSegment.py">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImportSurfaceToSegment/ImportSurfaceToSegment.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImportSurfaceToSegment/ImportSurfaceToSegment.py" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/master/ImportSurfaceToSegment/ImportSurfaceToSegment.py</a></h4>


      <pre><code class="lang-py">import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# ImportSurfaceToSegment
#

class ImportSurfaceToSegment(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "ImportSurfaceToSegment" # TODO make this more human readable by adding spaces
    self.parent.categories = ["SlicerMorph.SlicerMorph Utilities"]
    self.parent.dependencies = []
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ImportSurfaceToSegment/ImportSurfaceToSegment.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Dzemal (2024-02-29 04:48 UTC)

<p>Thank you for the fast reply, I will take a closer look and write back if it has solved my problem.</p>

---

## Post #4 by @Dzemal (2024-02-29 05:51 UTC)

<p>I’ve tested the module in slicer and it does exactly what I need, but I can just load one STL at once. Is there a way to load mutliple STLs and create a segmentation tree out of this STLs instead of a single segmenation node? In other words, I have the right and left femur as well as the left and right tibia and fibula saved in separated  STL files. Now I need one segmentation (-tree) which I can export as a .seg.nrrd file.</p>

---

## Post #5 by @muratmaga (2024-02-29 16:30 UTC)

<p>You can copy/paste segments from different segmentations. Our module doesn’t do that, but you can look into the script library for examples. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---

## Post #6 by @Dzemal (2024-03-01 05:06 UTC)

<p>Thanks again, the script repository might be helpful. I’ll give it a try and keep you updated.</p>

---
