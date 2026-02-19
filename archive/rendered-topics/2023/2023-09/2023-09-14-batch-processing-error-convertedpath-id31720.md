---
topic_id: 31720
title: "Batch Processing Error Convertedpath"
date: 2023-09-14
url: https://discourse.slicer.org/t/31720
---

# Batch Processing Error - convertedPath

**Topic ID**: 31720
**Date**: 2023-09-14
**URL**: https://discourse.slicer.org/t/batch-processing-error-convertedpath/31720

---

## Post #1 by @trussel1 (2023-09-14 15:52 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.40</p>
<p>I have a general understanding of 3D Slicer and have been using for a few years now. I now have a project with a large data set and want to start using Python to segment data using batch processing.</p>
<p>I have referenced the Script repository along with other recommend material previously mentioned in other posts but I am getting an error stating that “NameError: name ‘convertedPath’ is not defined”. Can someone help me troubleshoot this ?</p>
<p><em>Snippet of Code</em> :</p>
<pre><code class="lang-auto">import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from DICOMLib import DICOMUtils
import logging

db = slicer.dicomDatabase
patients = db.patients()
patientCount = 0
for patient in patients:
  patientCount += 1
  print(f"Patient {patient} ({patientCount} of {len(patients)})")
  for study in db.studiesForPatient(patient):
    print(f"Study {study}")
    for series in db.seriesForStudy(study):
      print(f"Series {series}")
      temporaryDir = qt.QTemporaryDir()
      for instanceUID in db.instancesForSeries(series):
        qt.QFile.copy(db.fileForInstance(instanceUID), f"{temporaryDir.path()}/{instanceUID}.dcm")
      patientID = slicer.dicomDatabase.instanceValue(instanceUID, '0010,0020')
      outputPath = os.path.join(convertedPath, patientID, study, series, "BatchResult")
      if not os.path.exists(outputPath):
        os.makedirs(outputPath)
      # do an operation here that processes the series into the outputPath

masterVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")


# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
</code></pre>
<p>Best,<br>
Ty</p>

---

## Post #2 by @pieper (2023-09-14 18:33 UTC)

<aside class="quote no-group" data-username="trussel1" data-post="1" data-topic="31720">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/trussel1/48/67529_2.png" class="avatar"> trussel1:</div>
<blockquote>
<p>“NameError: name ‘convertedPath’ is not defined”. Can someone help me troubleshoot this ?</p>
</blockquote>
</aside>
<p>The example script is just a skeleton.  You’ll need to have something like <code>convertedPath = "/tmp/output"</code> as a place to store the converted data.</p>

---
