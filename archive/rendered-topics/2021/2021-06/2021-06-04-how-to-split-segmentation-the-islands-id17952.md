---
topic_id: 17952
title: "How To Split Segmentation The Islands"
date: 2021-06-04
url: https://discourse.slicer.org/t/17952
---

# How to split segmentation the islands?

**Topic ID**: 17952
**Date**: 2021-06-04
**URL**: https://discourse.slicer.org/t/how-to-split-segmentation-the-islands/17952

---

## Post #1 by @Saima (2021-06-04 08:16 UTC)

<aside class="quote no-group" data-username="giovform" data-post="17" data-topic="8348">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"><a href="https://discourse.slicer.org/t/scissors-segment-editor-effects-from-a-script/8348/17">Scissors segment editor effects from a script</a></div>
<blockquote>
<p><code>segmentEditorNode.SetMasterVolumeIntensityMask(True)</code></p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I need to get the volume convert to labelmap import to segmentationnode and then split it into islands.</p>
<p>I am using the script below but its not working it crashes. could you please help.</p>
<p>Thank you</p>
<p>labelVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
slicer.vtkSlicerVolumesLogic().CreateLabelVolumeFromVolume(slicer.mrmlScene, labelVolumeNode, inputVolume)<br>
<span class="hashtag-raw">#convert</span> volume to labelmap</p>
<h1><a name="p-60576-create-segmentation-1" class="anchor" href="#p-60576-create-segmentation-1" aria-label="Heading link"></a>Create segmentation</h1>
<pre><code>segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(inputVolume)

# Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(inputVolume)

#import volume to labelmap     
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelVolumeNode, segmentationNode) 
segmentEditorWidget.setCurrentSegmentID(segmentationNode.GetSegmentation().GetNthSegmentID(0))
segmentEditorNode.SetMasterVolumeIntensityMask(True)
# check the volume scalar range and based on that use the island filter to split the segment
# get scalar range of a volume
img = inputVolume.GetImageData()
rng = img.GetScalarRange()
r2 = rng[1]
print(r2)
if r2==1:
    #do the island thing for the volume as only one segment will be crreated and we need to split the segment into islands
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    operationName = 'SPLIT_ISLANDS_TO_SEGMENTS'
    minsize = 500
    effect.setParameter("Operation", operationName)
    effect.setParameter("MinimumSize",minsize)
    effect.self().onApply()
</code></pre>

---

## Post #2 by @Saima (2021-06-08 05:19 UTC)

<aside class="quote no-group" data-username="Saima" data-post="1" data-topic="17952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Volume)</p>
</blockquote>
</aside>
<p>I found the problem. The split island filter is not working properly. Its not creating islands it ignores 113 island 0 created. why is this happening although it should split the segment.</p>
<p>Thank you</p>

---

## Post #3 by @Saima (2021-06-08 05:52 UTC)

<p>I have reduced the minimumsize it works but from the script it crashes. is there any problem with the script below.</p>
<p>Thank you</p>
<p>labelVolumeNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
slicer.vtkSlicerVolumesLogic().CreateLabelVolumeFromVolume(slicer.mrmlScene, labelVolumeNode, inputVolume)<br>
<span class="hashtag-raw">#convert</span> volume to labelmap</p>
<h1><a name="p-60747-create-segmentation-1" class="anchor" href="#p-60747-create-segmentation-1" aria-label="Heading link"></a>Create segmentation</h1>
<pre><code>segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(inputVolume)

# Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(inputVolume)

#import volume to labelmap     
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelVolumeNode, segmentationNode) 
segmentationNode.CreateClosedSurfaceRepresentation()
segmentEditorWidget.setCurrentSegmentID(segmentationNode.GetSegmentation().GetNthSegmentID(0))
#segmentEditorNode.SetMasterVolumeIntensityMask(True)
# check the volume scalar range and based on that use the island filter to split the segment
# get scalar range of a volume
img = inputVolume.GetImageData()
rng = img.GetScalarRange()
r2 = rng[1]
print(r2)

if int(r2)==1:
    #do the island thing for the volume as only one segment will be crreated and we need to split the segment into islands
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    operationName = 'SPLIT_ISLANDS_TO_SEGMENTS'
    minsize = 45
    effect.setParameter("Operation", operationName)
    effect.setParameter("MinimumSize",minsize)
    effect.self().onApply()
</code></pre>

---

## Post #4 by @lassoan (2021-06-08 20:21 UTC)

<p>The application probably does not actually crash, but it slows down extremely due to the large number of created segments. If you don’t filter out the noise and set the minimum size to be 0 then you can get a separate segment for each single-voxel speckle that you have in the image. You can end up with hundreds of thousands of segments, which will make everything extremely slow.</p>

---

## Post #5 by @Valentina_Nepi (2021-12-11 22:58 UTC)

<p>sorry for the intrusion <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"> I would like to reproduce this islands generation directly in pyradiomics without passing for 3d slicer. how can I do this? adn mainly, is it possible?</p>

---

## Post #6 by @lassoan (2021-12-14 14:27 UTC)

<p>There should be connected component filters in SimpleITK or ITK-Python that you can use in any Python environment to split a label image to disconnected islands. You can ask on the <a href="https://discourse.itk.org/">ITK forum</a> for details.</p>

---
