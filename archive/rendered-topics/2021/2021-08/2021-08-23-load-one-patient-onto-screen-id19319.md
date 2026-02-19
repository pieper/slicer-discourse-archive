---
topic_id: 19319
title: "Load One Patient Onto Screen"
date: 2021-08-23
url: https://discourse.slicer.org/t/19319
---

# Load one patient onto screen

**Topic ID**: 19319
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/load-one-patient-onto-screen/19319

---

## Post #1 by @alyssan (2021-08-23 14:58 UTC)

<p>Hello, I have a folder of dicom files but would like to automatically load on patient onto the screen every time.</p>
<p>I have loaded my dicom files into the DICOM database using this code:</p>
<pre><code class="lang-python">dicomDataDir = "c:/my/folder/with/dicom-files"  # input folder with DICOM files
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>
<p>How do I automatically access one patient and load it, do I have to use the patient uid and how do i find this?</p>

---

## Post #2 by @lassoan (2021-08-23 16:09 UTC)

<p>If you just want to load the first patient then replace the last two lines by</p>
<pre><code class="lang-python">loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUIDs[0]))
</code></pre>

---

## Post #3 by @alyssan (2021-08-24 13:36 UTC)

<p>Thank you this seems to be working I appreciate your help.<br>
I have a script set up but it was using sample data.</p>
<p><span class="hashtag">#Load</span> Data<br>
import SampleData<br>
sampleDataLogic = SampleData.SampleDataLogic()<br>
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()<br>
n = getNode(‘MRBrainTumor1’)</p>
<p>The masterVolumeNode variable is important and called in future code, how would I set this using my new data from dicom folder?</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2021-08-24 13:59 UTC)

<p>In the example above, <code>loadedNodeIDs</code> contain the IDs of the loaded nodes. For example, you can get the first node object (for example, it can be a volume node) by calling:</p>
<pre><code class="lang-python">n = slicer.mrmlScene.GetNodeByID(loadedNodeIDs[0])
</code></pre>

---

## Post #5 by @alyssan (2021-08-24 15:44 UTC)

<p>Okay, I have tried it out.</p>
<p>masterVolumeNode = slicer.mrmlScene.GetNodeByID(loadedNodeIDs[0])</p>
<p>I am using this for segmentation and get the error “Master Volume Node is not set as either background or foreground”</p>
<p>Any ideas on how to fix this?</p>

---

## Post #6 by @rbumm (2021-08-24 16:27 UTC)

<aside class="quote no-group" data-username="alyssan" data-post="5" data-topic="19319">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3da27b/48.png" class="avatar"> alyssan:</div>
<blockquote>
<p>I am using this for segmentation</p>
</blockquote>
</aside>
<p>What exactly is it you want to do? Please give more details …</p>

---

## Post #7 by @alyssan (2021-08-25 16:41 UTC)

<p>I am following an example like this one:</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9">
  <header class="source">

      <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9</a></h4>

  <h5>ExtractSkin.py</h5>
  <pre><code class="Python">import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRHead()

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin")
</code></pre>
    This file has been truncated. <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I was asking how to define masterVolumeNode from loaded data from folder on my computer.</p>
<p>When I implemented:</p>
<p>masterVolumeNode = slicer.mrmlScene.GetNodeByID(loadedNodeIDs[0])</p>
<p>It said that masterVolume Node is not set as either the background or foreground</p>

---
