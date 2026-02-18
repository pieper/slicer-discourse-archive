# Converting RTStruct to Dicom SEG for Pyradiomics

**Topic ID**: 41689
**Date**: 2025-02-13
**URL**: https://discourse.slicer.org/t/converting-rtstruct-to-dicom-seg-for-pyradiomics/41689

---

## Post #1 by @jackjcoop (2025-02-13 20:12 UTC)

<p>Hi all!</p>
<p>I am new here, and have been recently struggling with the following.</p>
<p>I have a dataset from TCIA I am hoping to analyze containing a CT series and associated segmentations in RTStruct format. Although, I can extract radiomic features through the GUI, I am hoping to use script this in python specifically and use pyradiomics-labs to process the dicom imagery.</p>
<p>Using dcmrtstruct2nii, I have been able to extract .nii masks of all the features from the RTStruct, and similarly using SimpleITK, have convered it to a .nrrd format. However, this is where I am stuck trying to convert either of these masks to a Dicom SEG object.</p>
<p>It may be simpler at this point to convert my dicom series to .nrrd potentially.</p>
<p>Thanks for the help!</p>

---

## Post #2 by @jackjcoop (2025-02-13 20:35 UTC)

<p>It seems it may actually be easier to just convert my dicom serise to nrrd for now.</p>

---

## Post #3 by @cpinter (2025-02-17 09:47 UTC)

<aside class="quote no-group" data-username="jackjcoop" data-post="1" data-topic="41689">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jackjcoop/48/79445_2.png" class="avatar"> jackjcoop:</div>
<blockquote>
<p>dcmrtstruct2nii</p>
</blockquote>
</aside>
<p>I don’t know how dcmrtstruct2nii works, but in SlicerRT we have a quite sophisticated algorithm that can convert the antiquated contour set to an interpolated surface and then labelmap. If you’re interested after all let me know. All you need are the SlicerRT and DCMQI extensions.</p>

---

## Post #4 by @jackjcoop (2025-02-20 03:46 UTC)

<p>SlicerRT is excellent, I was using it in the GUI.</p>
<p>Is there an available API or a way to script it to work over multiple files without user intervention?</p>
<p>dcmrtstruct2nii seemed to work well for the meantime. It took ~5h to convert about 400 RtStruct files with ~20 masks within each. Not sure if this is fast or slow haha.</p>

---

## Post #5 by @cpinter (2025-02-20 09:56 UTC)

<p>We have a script in the repo that batch-converts RTSS to nrrd. It is not a long way from here to DICOM SEG.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py" target="_blank" rel="noopener">BatchProcessing/BatchStructureSetConversion.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py" rel="noopener"><code>master</code></a>
</div>


      <pre><code class="lang-py">from __future__ import absolute_import, division, print_function # Makes moving python2 to python3 much easier and ensures that nasty bugs involving integer division don't creep in
import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import argparse
import sys
import logging
from DICOMLib import DICOMUtils

slicer.exit_when_finished = True

# ------------------------------------------------------------------------------
# BatchStructureSetConversion
#   Convert structures in structure set to labelmaps and save them to disk
#
class BatchStructureSetConversion(ScriptedLoadableModule):
    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        parent.title = "Batch Structure Set Conversion"
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I hope it still works, this one is not regularly tested. Let me know if anything comes up!</p>

---
