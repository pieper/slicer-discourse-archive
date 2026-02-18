# Segmentation using thresholding using Python

**Topic ID**: 7833
**Date**: 2019-07-31
**URL**: https://discourse.slicer.org/t/segmentation-using-thresholding-using-python/7833

---

## Post #1 by @jazlynn21100 (2019-07-31 18:40 UTC)

<p>Hey there,<br>
I’m back with more silly questions<br>
using the examples of using segment editor have been really helpful, the issue I have been running into, however, is using an image that is not the sample image.</p>
<p>Just dragging in an image and avoiding anything that uses ‘masterVolumeNode’ was my original plan, but I am unable to apply the threshold on the image of interest if I do it that way.Same with pulling in the image and setting it as the master volume manually on segment editor. So I did some digging to try and find out how to load in my own image the correct way and found this:</p>
<p>masterVolumeNode = slicer.util.loadVolume('C:/Users/m222222/Dropbox/BRAIN_MASK.nii.gz’, returnNode=True)</p>
<p>(the path is similar to my actual path)<br>
and it doesn’t complain at me, but it also doesn’t open the file, and when I tried to run things anyways, after<br>
‘segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)’<br>
I got an error that I needed a VTK object, and after<br>
‘segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)’<br>
it also said that I needed a VTK object</p>
<p>if I run it without those 2 lines, it complains at the end on ‘effect.self().onApply()’ and says…</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorEffects/SegmentEditorEffects/SegmentEditorThresholdEffect.py”, line 351, in onApply<br>
modifierLabelmap.GetImageToWorldMatrix(originalImageToWorldMatrix)<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetImageToWorldMatrix’</p>
<p>To be honest, I really don’t know what I’m doing on the coding front, so even simple things like loading images are rough, which is why I’m here.</p>
<p>I’m just confused and would like to know the correct way to load a master volume so the sample works with a novel image.</p>
<p>Thank you,<br>
Jazlynn</p>

---

## Post #2 by @lassoan (2019-08-01 04:25 UTC)

<p><a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="nofollow noopener">This</a> example should work as is, just replace this line:</p>
<pre><code>masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()
</code></pre>
<p>by this, if you use recent 4.11 version of Slicer:</p>
<pre><code>masterVolumeNode = slicer.util.loadVolume('C:/Users/m222222/Dropbox/BRAIN_MASK.nii.gz')
</code></pre>
<p>by this, if you use 4.10 version:</p>
<pre><code>[success, masterVolumeNode] = slicer.util.loadVolume('C:/Users/m222222/Dropbox/BRAIN_MASK.nii.gz', returnNode=True)</code></pre>

---

## Post #3 by @jazlynn21100 (2019-08-01 17:31 UTC)

<p>that makes a lot of sense, thank you</p>

---

## Post #4 by @jazlynn21100 (2019-08-01 18:40 UTC)

<p>I replaced the first line with</p>
<p>[success, masterVolumeNode] = slicer.util.loadVolume(“C:/Users/m214492/Dropbox/CNV Modeling/Brain for Gustavo/BRAIN_MASK.nii.gz”, returnNode=True)</p>
<p>because it gave a syntax error the ran with one quote, and everything seemed to work until I got to that apply line</p>
<p>effect.self().onApply()</p>
<p>Where the callback was:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorEffects/SegmentEditorEffects/SegmentEditorThresholdEffect.py”, line 351, in onApply<br>
modifierLabelmap.GetImageToWorldMatrix(originalImageToWorldMatrix)<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetImageToWorldMatrix’</p>
<p>I’m really not sure why or what it going on internally in slicer when this happens, but it runs with the sample</p>
<p>sorry for all of the questions</p>
<p>best,<br>
Jazlynn</p>

---

## Post #5 by @jazlynn21100 (2019-08-01 18:44 UTC)

<p>I think it may have something to do with the fact that in the sample, slicer actually opens the file, and you can see it in your 3 colored windows, but when I set my master volume, the file doesn’t come up visibly in slicer. I’m not sure if that could be the issue or not.</p>

---

## Post #6 by @lassoan (2019-08-01 18:50 UTC)

<p>Does the example that I linked above works? If yes then try to follow that example more closely, make modifications step-by-step, and see which change causes the problem.</p>

---

## Post #7 by @jazlynn21100 (2019-08-01 20:23 UTC)

<p>The sample that is provided works without an issue, and slicer doesn’t throw up an error until the thresholding line (after going through the code step by step)</p>
<p>effect.self().onApply()</p>
<p>So there must be an issue earlier although there was no complaint from slicer. I believe that is has to do with loading the master image; when I set the master image to be my novel image, the image is not shown in the colored ‘slices’ windows. However, when the sample image is loaded, it appears in the colored ‘slices’ windows.</p>
<p>The exact code I have been running is:<br>
The master volume is a mask, saved as a nifty file.</p>
<p>[success, masterVolumeNode] = slicer.util.loadVolume(“C:/Users/m22222/Dropbox/BRAIN_MASK.nii.gz”, returnNode=True)</p>
<p>segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
segmentationNode.CreateDefaultDisplayNodes() # only needed for display<br>
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)<br>
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(“skin”)</p>
<p>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentEditorNode”)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</p>
<p>segmentEditorWidget.setActiveEffectByName(“Threshold”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“MinimumThreshold”,“1”)<br>
effect.setParameter(“MaximumThreshold”,“1”)<br>
effect.self().onApply()</p>
<p>segmentEditorWidget = None<br>
slicer.mrmlScene.RemoveNode(segmentEditorNode)</p>
<p>segmentationNode.CreateClosedSurfaceRepresentation()</p>

---

## Post #8 by @lassoan (2019-08-01 21:14 UTC)

<p>What is the output of <code>print(master VolumeNode)</code>?</p>

---

## Post #9 by @jazlynn21100 (2019-08-01 21:26 UTC)

<p>The output is just ‘none’</p>

---

## Post #10 by @lassoan (2019-08-02 01:59 UTC)

<p>It means the image loading has failed. The application log may contain more details (menu: Help / Report a bug). Is the file path correct? Can you load the image by using “Add data”?</p>

---

## Post #11 by @jazlynn21100 (2019-08-02 17:21 UTC)

<p>When I use the ‘add data’ option I get</p>
<p>[INFO][VTK] 02.08.2019 10:18:59 [vtkMRMLVolumeArchetypeStorageNode (0x7f9436777de0)] (/Volumes/Dashboards/Stable/Slicer-4102/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: /Users/m214492/Dropbox/CNV Modeling/Brain for Gustavo/BRAIN_MASK.nii.gz. Dimensions: 270x320x76. Number of components: 1. Pixel type: float.<br>
[DEBUG][Qt] 02.08.2019 10:18:59 [] (unknown:0) - “Volume” Reader has successfully read the file “/Users/m214492/Dropbox/CNV Modeling/Brain for Gustavo/BRAIN_MASK.nii.gz” “[0.29s]”</p>
<p>in the application log</p>
<p>When I enter it using the CLI I get</p>
<p>[DEBUG][Qt] 02.08.2019 10:18:00 [] (unknown:0) - Python console user input: [success, masterVolumeNode] = slicer.util.loadVolume(“C:/Users/m214492/Dropbox/CNV Modeling/Brain for Gustavo/BRAIN_MASK.nii.gz”, returnNode=True)</p>

---

## Post #12 by @lassoan (2019-08-02 17:26 UTC)

<p>Path looks different:<br>
<code>/Users/m214492/Dropbox/CNV Modeling/Brain for Gustavo/BRAIN_MASK.nii.gz</code><br>
is not the same as<br>
<code>C:/Users/m214492/Dropbox/CNV Modeling/Brain for Gustavo/BRAIN_MASK.nii.gz</code></p>
<p>Drive name (such as <code>C:</code>) is only used on Windows machines.</p>

---

## Post #13 by @jazlynn21100 (2019-08-02 17:28 UTC)

<p>Oh my goodness you have just saved my life, thank you so much</p>

---

## Post #14 by @lassoan (2019-08-02 21:20 UTC)

<p>A post was split to a new topic: <a href="/t/change-segment-color-and-opacity/7855">Change segment color and opacity</a></p>

---

## Post #15 by @xavier_bouquin (2022-03-15 13:14 UTC)

<p>Hello<br>
I am new to 3DS Slicer.<br>
I would like to automate 3D mesh generation with 3DSlicer from dcm serie and save it  as obj file.<br>
the idea is to open obj files in hololens afterwards.</p>
<p>I can open my dcm files like this.</p>
<pre><code class="lang-python">dicomDataDir = "C:/Users/xbouq/Downloads/Anonymized/dcm"
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>
<p>But after i dont understand	how make a link  with segmentatioNodes</p>
<pre><code class="lang-python">segmentationNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment('skin')

segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentEditorNode')
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

segmentEditorWidget.setActiveEffectByName('Threshold')
effect = segmentEditorWidget.activeEffect()
effect.setParameter('MinimumThreshold','135') // for bones
effect.setParameter('MaximumThreshold','294')
effect.self().onApply()
</code></pre>
<p>Can you help me ?<br>
maybe there is a plugin for 3DSlicer?</p>

---

## Post #16 by @lassoan (2022-03-18 14:36 UTC)

<p>You can get the volume node object from <code>loadedNodeIDs</code> by using <code>masterVolumeNode = slicer.mrmlScene.GetNodeByID(nodeID)</code>.</p>
<p>If you import a complete DICOM study then the loaded nodes include scout scans, dose report, etc., so you may want to filter out images that have only one or few slices.</p>

---

## Post #17 by @xavier_bouquin (2022-04-26 15:22 UTC)

<p>Thank’s very lot Andras<br>
But now i have another problem.</p>
<pre><code class="lang-auto">dicomDataDir = "C:/Users/xbouq/Downloads/Anonymized/dcm"
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))



segmentationNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
masterVolumeNode = segmentationNode.GetNodeReference(segmentationNode.GetReferenceImageGeometryReferenceRole())

segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment('skin')

segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentEditorNode')
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)


addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("Segmentation")
segmentEditorNode.SetSelectedSegmentID(addedSegmentID)
    
segmentEditorWidget.setActiveEffectByName('Threshold')
effect = segmentEditorWidget.activeEffect()
effect.setParameter('MinimumThreshold',"135")
effect.setParameter('MaximumThreshold',"294")
effect.self().onApply()
</code></pre>
<p>When execution arrival at this line i have this error, Something escape me…</p>
<pre><code class="lang-auto">SegmentEditorThresholdEffect.py", line 590, in onApply

```    modifierLabelmap.GetImageToWorldMatrix(originalImageToWorldMatrix)
AttributeError: 'NoneType' object has no attribute 'GetImageToWorldMatrix'


layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.resetFocalPoint()  

outputFolder = "C:/Users/xbouq/Downloads/Anonymized/dcm"
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles(outputFolder, segmentationNode, None, "OBJ", True, 1.0, False)
</code></pre>

---

## Post #18 by @lassoan (2022-04-26 17:48 UTC)

<aside class="quote no-group" data-username="xavier_bouquin" data-post="17" data-topic="7833">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xavier_bouquin/48/14620_2.png" class="avatar"> xavier_bouquin:</div>
<blockquote>
<pre><code class="lang-auto">masterVolumeNode = segmentationNode.GetNodeReference(segmentationNode.GetReferenceImageGeometryReferenceRole())
</code></pre>
</blockquote>
</aside>
<p>This would get you the node that was used to set the segmentation geometry (which is usually the master volume). But you have just created a new segmentation node. You have not set its geometry, so this GetNode… method will return None.</p>
<p>Instead, you can set the master volume (a volume that you loaded from DICOM) into the segmentation node by calling <code>segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</code>.</p>

---

## Post #19 by @xavier_bouquin (2022-04-27 09:29 UTC)

<aside class="quote no-group" data-username="xavier_bouquin" data-post="17" data-topic="7833">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xavier_bouquin/48/14620_2.png" class="avatar"> xavier_bouquin:</div>
<blockquote>
<p><code>masterV</code></p>
</blockquote>
</aside>
<p>Hi Andras<br>
How to replace this init of masterVolumeNode<br>
sampleDataLogic = SampleData.SampleDataLogic()<br>
masterVolumeNode = sampleDataLogic.downloadMRHead()</p>
<p>with this loading system<br>
dicomDataDir = “C:/Users/xbouq/Downloads/Anonymized/dcm”<br>
loadedNodeIDs = <span class="chcklst-box fa fa-square-o fa-fw"></span>  # this list will contain the list of all loaded node IDs</p>
<p>from DICOMLib import DICOMUtils<br>
with DICOMUtils.TemporaryDICOMDatabase() as db:<br>
DICOMUtils.importDicom(dicomDataDir, db)<br>
patientUIDs = db.patients()<br>
for patientUID in patientUIDs:<br>
loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))</p>
<p>masterVolumeNode =</p>
<p>Do you know if there are freelancers to develop with 3dSlicer.<br>
Our idea is to do a proof of concept, where we will copy Dicom files to a directory and with an online command we could select filters to generate 3d files to visualize them in the end in hololens.<br>
But we don’t have any expertise with 3Dslicer which is sacred software and with Python either.</p>
<p>I manage to generate OBJ files with the software but I can’t automate the process and I may not find the time to learn to program with 3Dslicer. There are too many concepts that I don’t know <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #20 by @lassoan (2022-04-27 15:02 UTC)

<p>It would be something like this:</p>
<pre><code class="lang-auto">i = 0  # first loaded image series (it multiple image series are loaded then you may want to iterate through all of them)
masterVolumeNode = slicer.mrmlScene.GetNodeByID(loadedNodeIDs[i])
</code></pre>
<aside class="quote no-group" data-username="xavier_bouquin" data-post="19" data-topic="7833">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xavier_bouquin/48/14620_2.png" class="avatar"> xavier_bouquin:</div>
<blockquote>
<p>Our idea is to do a proof of concept, where we will copy Dicom files to a directory and with an online command we could select filters to generate 3d files to visualize them in the end in hololens.<br>
But we don’t have any expertise with 3Dslicer which is sacred software and with Python either.</p>
</blockquote>
</aside>
<p>Simple thresholding often does not provide sufficiently good quality results. I would recommend to use <code>Grow from seeds</code> or <code>Local threshold</code> effects in Segment Editor, or use MONAILabel extension to train a neural network for automatic segmentation. As a proof of concept, you can segment a couple of images manually using Segment Editor module and later you can automate it.</p>
<aside class="quote no-group" data-username="xavier_bouquin" data-post="19" data-topic="7833">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xavier_bouquin/48/14620_2.png" class="avatar"> xavier_bouquin:</div>
<blockquote>
<p>Do you know if there are freelancers to develop with 3dSlicer.</p>
</blockquote>
</aside>
<p>I would recommend to contact <a href="https://www.slicer.org/commercial-use.html#commercial-partners">Slicer Commercial Partners</a>.</p>

---
