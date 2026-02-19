---
topic_id: 10837
title: "Loading Dicom Directory Into Scene And Obtaining Master Volu"
date: 2020-03-25
url: https://discourse.slicer.org/t/10837
---

# Loading dicom directory into scene and obtaining master volume node

**Topic ID**: 10837
**Date**: 2020-03-25
**URL**: https://discourse.slicer.org/t/loading-dicom-directory-into-scene-and-obtaining-master-volume-node/10837

---

## Post #1 by @Queen_Rei (2020-03-25 17:53 UTC)

<p>Heya once again~</p>
<p><strong>I am trying to get three things working.</strong></p>
<ol>
<li>Load a dicom directory and have it render in the scene. Right now I have it working with a specific patient id, but I wanted to know if there is a better way of doing this. Ideally, in a manner which loads it without needing to input a patient id.</li>
<li>Obtain the master volume node of this dicom directory, so that it segments and displays the segmentation in the scene.</li>
<li>Be able to set the color of the segmentation to one of the preset colors. I have it set to bone, but it still appears as green.</li>
</ol>
<p>Any and all resources and advice would be much appreciated~</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23bd1b8a851920860f8d4bee0643d0dbe26da9c3.png" alt="dicom2" data-base62-sha1="569S6fcKG3elbHMQwUn7lVSz1ED" width="672" height="476"></p>

---

## Post #2 by @pieper (2020-03-25 18:10 UTC)

<p>1 and 2) Here’s what I do (when I know the seriesInstanceUID)</p>
<pre><code class="lang-auto">    seriesNodeIDs = DICOMUtils.loadSeriesByUID([seriesInstanceUID,])
    seriesVolumeNode = slicer.util.getNode(seriesNodeIDs[0])
    storageNode = seriesVolumeNode.CreateDefaultStorageNode()
    slicer.mrmlScene.AddNode(storageNode)
    seriesVolumeNode.SetAndObserveStorageNodeID(storageNode.GetID())
    storageNode.SetFileName(slicer.dicomDatabase.fileForInstance(sopInstanceUID))
</code></pre>
<ol start="2">
<li>This uses the series volume as master</li>
</ol>
<pre><code class="lang-auto">segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# To show segment editor widget (useful for debugging): segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)

segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(seriesVolumeNode)
</code></pre>
<ol start="3">
<li>this add a segment with a custom color</li>
</ol>
<pre><code class="lang-auto">lesionSegment = slicer.vtkSegment()
lesionSegment.SetName("Lesion Seeds")
lesionSegment.SetColor([0.0,1.0,0.0])
segmentationNode.GetSegmentation().AddSegment(lesionSegment,"lesionSeeds")
</code></pre>

---

## Post #3 by @lassoan (2020-03-25 18:54 UTC)

<p>This example shows how to import and load all DICOM series in a file folder into the scene:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder</a></p>

---

## Post #4 by @Queen_Rei (2020-03-25 23:02 UTC)

<p>Wow, thank you so much! I am new to the forum and I have to say you all are so responsive and helpful.</p>
<p>I did the following below:</p>
<pre><code>seriesInstanceUID = '2.16.840.1.114151.3.1.20566.9261759.7592.1584719071.211'
    sopInstanceUID = '2.16.840.1.114151.3.1.20566.9261759.7592.1584719071.212'

    seriesNodeIDs = DICOMUtils.loadSeriesByUID([seriesInstanceUID,])
    seriesVolumeNode = slicer.util.getNode(seriesNodeIDs[0])
    storageNode = seriesVolumeNode.CreateDefaultStorageNode()
    slicer.mrmlScene.AddNode(storageNode)
    seriesVolumeNode.SetAndObserveStorageNodeID(storageNode.GetID())
    storageNode.SetFileName(slicer.dicomDatabase.fileForInstance(sopInstanceUID))
</code></pre>
<p>And I get an error</p>
<pre><code>  File "Z:/LoadSegMod/Dicom/SegmentDicom/SegmentDicom.py", line 166, in LoadSegment
    seriesVolumeNode = slicer.util.getNode(seriesNodeIDs[0])
TypeError: 'bool' object has no attribute '__getitem__'
</code></pre>
<p>Seems as if the issue is with the seriesNodeIDs[0]</p>

---

## Post #5 by @pieper (2020-03-25 23:21 UTC)

<p>For something like this it’s usually easiest just to add print statements to check all the return values and then check through the source code to see if you can figure out what’s going on.</p>
<p>If that doesn’t work you can also <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools">use debuggers</a>.</p>
<p>Good luck!</p>

---

## Post #6 by @lassoan (2020-03-26 00:25 UTC)

<aside class="quote no-group" data-username="Queen_Rei" data-post="4" data-topic="10837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/queen_rei/48/6348_2.png" class="avatar"> Queen_Rei:</div>
<blockquote>
<p>I get an error</p>
<pre><code class="lang-auto">  File "Z:/LoadSegMod/Dicom/SegmentDicom/SegmentDicom.py", line 166, in LoadSegment
    seriesVolumeNode = slicer.util.getNode(seriesNodeIDs[0])
TypeError: 'bool' object has no attribute '__getitem__'
</code></pre>
</blockquote>
</aside>
<p>The code snippet in the “Nightly” sccript repository page requires latest Slicer Preview Release. Yours may be a couple of weeks old (or even older).</p>

---

## Post #7 by @Queen_Rei (2020-03-26 16:37 UTC)

<p>Ohh my! I am using the latest official version rather than the latest preview release.<br>
Do you know of any documentation on loading from a seriesUID using the version I am currently on?</p>
<p>Version: 4.10.2</p>

---

## Post #8 by @lassoan (2020-03-26 18:59 UTC)

<p>DICOM loading has been completely reworked in Slicer Preview Releases (Slicer-4.11). We plan to release Slicer-4.11 as the new stable release within a couple of weeks, so I would not recommend to implement any DICOM processing script for Slicer-4.10.</p>

---

## Post #9 by @Queen_Rei (2020-03-26 20:32 UTC)

<p>Thanks for the advice. I have installed the latest preview version, but I have run into issues.</p>
<pre><code># Import and load dicom from directory
dicomDataDir = "Z:/Dicom2Text/LumbarCTforMagicLeap"
loadedNodeIDs = []

from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
for patientUID in patientUIDs:
  loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>
<p>When I run this code there are two things that arise:</p>
<ol>
<li>I need to get the master volume node from this info. And when I try using slicer.util.getNode(loadedNodeIDs[0]) then it crashes the app.</li>
<li>Running this code sometimes gives me an error stating:<br>
OSError: No patient found with DICOM database UID 1</li>
</ol>

---

## Post #10 by @Queen_Rei (2020-03-26 20:40 UTC)

<p>Also when I try the code below I get have an empty seriesNodeIDs = []</p>
<pre><code>    seriesInstanceUID = '2.16.840.1.114151.3.1.20566.9261759.7592.1584719071.211'
    sopInstanceUID = '2.16.840.1.114151.3.1.20566.9261759.7592.1584719071.212'

    seriesNodeIDs = DICOMUtils.loadSeriesByUID([seriesInstanceUID,])
    self.delayDisplay(seriesNodeIDs)
    seriesVolumeNode = slicer.util.getNode(seriesNodeIDs[0])
    storageNode = seriesVolumeNode.CreateDefaultStorageNode()
    slicer.mrmlScene.AddNode(storageNode)
    seriesVolumeNode.SetAndObserveStorageNodeID(storageNode.GetID())
    storageNode.SetFileName(slicer.dicomDatabase.fileForInstance(sopInstanceUID))</code></pre>

---

## Post #11 by @lassoan (2020-03-26 21:22 UTC)

<p>I’ve just tried it in Slicer-4.11.0-2020-03-23 (revision 28875 / e5c1f6e) win-amd64 and it worked well:</p>
<pre><code class="lang-python">&gt;&gt;&gt; from DICOMLib import DICOMUtils
&gt;&gt;&gt; DICOMUtils.loadSeriesByUID(['1.3.6.1.4.1.14519.5.2.1.8421.4009.100453996512067231032804863467'])
Loading with imageIOName: GDCM
['vtkMRMLScalarVolumeNode1']
</code></pre>

---
