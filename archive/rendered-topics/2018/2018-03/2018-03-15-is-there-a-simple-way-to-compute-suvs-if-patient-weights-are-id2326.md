# Is there a simple way to compute SUVs if patient weights are kept separate from the DICOM files?

**Topic ID**: 2326
**Date**: 2018-03-15
**URL**: https://discourse.slicer.org/t/is-there-a-simple-way-to-compute-suvs-if-patient-weights-are-kept-separate-from-the-dicom-files/2326

---

## Post #1 by @drusmanbashir (2018-03-15 14:17 UTC)

<p>Hi,<br>
My dataset has been anonymised rather rigorously and weights stripped. I have them separately and wish to enter them manually case-by-case. I have tried several plugins e.g., SUV factor calculator, PET image maker, but they all ask for DICOM files and do not let me input patient weight data. Is there a way around this ?</p>
<p>Thanks<br>
Usman.</p>

---

## Post #2 by @pieper (2018-03-15 14:48 UTC)

<p>The easiest might be just to write a script with pydicom or command line tools to add the info back into the dicom files.</p>
<p>One option would be to fork and modify the dicom patcher with some custom code.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/58c8311c55c0d73e1311247b2a5a2d25253b6a3e/Modules/Scripted/DICOMPatcher/DICOMPatcher.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/58c8311c55c0d73e1311247b2a5a2d25253b6a3e/Modules/Scripted/DICOMPatcher/DICOMPatcher.py" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/58c8311c55c0d73e1311247b2a5a2d25253b6a3e/Modules/Scripted/DICOMPatcher/DICOMPatcher.py</a></h4>
<pre><code class="lang-py">import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# DICOMPatcher
#

class DICOMPatcher(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "DICOM Patcher"
    self.parent.categories = ["Utilities"]
    self.parent.dependencies = ["DICOM"]
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/58c8311c55c0d73e1311247b2a5a2d25253b6a3e/Modules/Scripted/DICOMPatcher/DICOMPatcher.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @fedorov (2018-03-15 16:58 UTC)

<p>It might be easier to batch-fix the dataset by using the <a href="http://support.dcmtk.org/docs/dcmodify.html"><code>dcmodify</code> tool of DCMTK</a>. Here’s the command to modify the value in a single file in place (or with <code>-i</code> if <code>PatientWeight</code> tag was removed completely):</p>
<pre><code class="lang-auto">$ dcmodify -nb -m PatientWeight=200 pet001.dcm
</code></pre>

---

## Post #4 by @drusmanbashir (2018-03-16 12:28 UTC)

<p>Thanks for the help. Unfortunately, even after fixing the weights with a script, Slicer was crashing in the SUV factor calculator CLI while running its PETDicom plugin(although Osirix SUV converter is  able to convert SUVs if i manually enter the weights, hence confused why SUV factor calculator should crash). Ended up writing a script that takes in .nrrd volumes of uncorrected values and replaces them with SUVs using weights and relevant DICOM tags input separately.</p>

---

## Post #5 by @fedorov (2018-03-16 13:23 UTC)

<p>Can you share a sample dataset?</p>
<p>Cc: <a class="mention" href="/u/chribaue">@chribaue</a></p>

---

## Post #6 by @fedorov (2018-03-16 17:07 UTC)

<p>I also submitted an issue to address this in the implementation: <a href="https://github.com/QIICR/Slicer-SUVFactorCalculator/issues/3">https://github.com/QIICR/Slicer-SUVFactorCalculator/issues/3</a></p>

---

## Post #7 by @drusmanbashir (2018-03-16 19:12 UTC)

<p>Hi,<br>
That problem is solved. It was either due to the patient weights not being as ‘DS’ format (I chose ‘FL’ float in defining the dicom tag) or because there were some non-DICOM files in the folder. I believe  SUV factor calculator expects the folder to contain only DICOM</p>

---
