---
topic_id: 29080
title: "Addsegment Error"
date: 2023-04-24
url: https://discourse.slicer.org/t/29080
---

# AddSegment error

**Topic ID**: 29080
**Date**: 2023-04-24
**URL**: https://discourse.slicer.org/t/addsegment-error/29080

---

## Post #1 by @pearsonm (2023-04-24 05:28 UTC)

<p>Using a local build of 5.3.0-2023-03-04 r31618 / b0b9be5 on Ubuntu 23.02 I get an error when I run the create segmentation node snippet from  <a href="https://discourse.slicer.org/t/programmatically-create-a-segmentationnode-and-labelmapnode-from-polygon-coordinates/8448/4">Programmatically Create a SegmentationNode and LabelMapNode from Polygon Coordinates</a>:</p>
<p>The last line<br>
<code>segmentationNode.GetSegmentation().AddSegment(segment)</code><br>
results in the error: [VTK] AddSegment: Unable to create master representation!</p>
<p>How do you create the master representation?</p>

---

## Post #2 by @lassoan (2023-04-24 11:12 UTC)

<p>It is quite an old release example. Maybe now you need to set the master representation to planar contours. Or maybe you just haven’t installed SlicerRT extension.</p>
<p>Anyway, you can find a complete implementation for n this module that imports parallel contours from an OsiriX segmentation file that should work well:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py" target="_blank" rel="noopener">PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py</a></h4>


      <pre><code class="lang-py">import os
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

#
# ImportOsirixROI
#

class ImportOsirixROI(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Import OsiriX ROI"
    self.parent.categories = ["Utilities"]
</code></pre>



  This file has been truncated. <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Why do you need to create a segment from parallel contours? Are you implementing an importer for a new file format?</p>

---

## Post #3 by @pearsonm (2023-04-24 11:44 UTC)

<p>I was using it as an example of creating a segmentation from datapoints.</p>
<p>I am creating a module to process nuclear medicine dynamic images and one of the steps involves drawing a rectangular ROI to do count statistics. I currently use the scissors rectangle tool for the ROI but it would be better if the ROI could be adjusted after creation.</p>
<p>I want to make a box ROI in Markups and then convert it to a binary labelmap so I can run Mask Volume. The code snippet looked like it would help make the labelmap.</p>

---
