# Wanted to use vtkImageData type data input, in place of vtkMRMLScalarVolumeNode/vtkMRMLSegmentationNode type input in lungCt analyzer code

**Topic ID**: 27017
**Date**: 2023-01-03
**URL**: https://discourse.slicer.org/t/wanted-to-use-vtkimagedata-type-data-input-in-place-of-vtkmrmlscalarvolumenode-vtkmrmlsegmentationnode-type-input-in-lungct-analyzer-code/27017

---

## Post #1 by @Rajesh_Ds (2023-01-03 16:01 UTC)

<p>recently I was going through the code</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/LungCTAnalyzer/LungCTAnalyzer.py">
  <header class="source">

      <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/LungCTAnalyzer/LungCTAnalyzer.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/LungCTAnalyzer/LungCTAnalyzer.py" target="_blank" rel="noopener nofollow ugc">rbumm/SlicerLungCTAnalyzer/blob/master/LungCTAnalyzer/LungCTAnalyzer.py</a></h4>


      <pre><code class="lang-py">import os
import unittest
import logging
import vtk, qt, ctk, slicer
import sys, subprocess
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin
from SegmentStatisticsPlugins import *

#
# LungCTAnalyzer
#

class LungCTAnalyzer(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
</code></pre>



  This file has been truncated. <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/LungCTAnalyzer/LungCTAnalyzer.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and i wanted to know how will i use vtkImageData type data input,  in place of vtkMRMLScalarVolumeNode/vtkMRMLSegmentationNode type input in lungCt analyzer code while inputting input CT volume  and segmentation volume. Please help</p>

---
