# Threshold range lower value script vs GUI

**Topic ID**: 38563
**Date**: 2024-09-26
**URL**: https://discourse.slicer.org/t/threshold-range-lower-value-script-vs-gui/38563

---

## Post #1 by @G_Tom (2024-09-26 21:25 UTC)

<p>hi, I am using a python script to threshold an image after first testing in the GUI.<br>
I am noticing that the threshold behaves differently ( different results) between the script and when doing threshold in the GUI.<br>
The pain reason I think is that the Lower bound of the threshold in the GUI seems to be updated automatically. How can I recreate this in a script ?</p>
<blockquote>
<pre><code>segmentationNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
segmentationNode.SetName('Segmentation_Image')
segmentationNode.CreateDefaultDisplayNodes() # only needed for display    
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(inputVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("Segment_BBs")

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)

segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setSourceVolumeNode(inputVolumeNode)

# Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("AutoThresholdMethod", "Maximum entropy")
effect.setParameter("AutoThresholdMode", "SET_LOWER_MAX")
effect.self().onApply()
</code></pre>
</blockquote>
<p>Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6f4712ae683dd313197a8c712891effe86d1bec.png" data-download-href="/uploads/short-url/wX7x2tMBjUkzwKDcEv4KDTE8lyY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6f4712ae683dd313197a8c712891effe86d1bec_2_352x500.png" alt="image" data-base62-sha1="wX7x2tMBjUkzwKDcEv4KDTE8lyY" width="352" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6f4712ae683dd313197a8c712891effe86d1bec_2_352x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6f4712ae683dd313197a8c712891effe86d1bec.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6f4712ae683dd313197a8c712891effe86d1bec.png 2x" data-dominant-color="363839"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">509×721 29.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Result in GUI:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20c16485aac15726270747a0e7d8e37674ea672e.png" data-download-href="/uploads/short-url/4FLCuQn48OXV5ELIJuRYTtSazLg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20c16485aac15726270747a0e7d8e37674ea672e_2_690x470.png" alt="image" data-base62-sha1="4FLCuQn48OXV5ELIJuRYTtSazLg" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20c16485aac15726270747a0e7d8e37674ea672e_2_690x470.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20c16485aac15726270747a0e7d8e37674ea672e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20c16485aac15726270747a0e7d8e37674ea672e.png 2x" data-dominant-color="3A3D45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">986×672 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Result from scrip:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20b668f7d8e34965becfdffd77b07468f2fb4cf3.jpeg" data-download-href="/uploads/short-url/4Fo5CP7zLccjW27h4YMMlKX0aLV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20b668f7d8e34965becfdffd77b07468f2fb4cf3_2_690x467.jpeg" alt="image" data-base62-sha1="4Fo5CP7zLccjW27h4YMMlKX0aLV" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20b668f7d8e34965becfdffd77b07468f2fb4cf3_2_690x467.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20b668f7d8e34965becfdffd77b07468f2fb4cf3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20b668f7d8e34965becfdffd77b07468f2fb4cf3.jpeg 2x" data-dominant-color="383944"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">991×671 96.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>GT</p>

---
