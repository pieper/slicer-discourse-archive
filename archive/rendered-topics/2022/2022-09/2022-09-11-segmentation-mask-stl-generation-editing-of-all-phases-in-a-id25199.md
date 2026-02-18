# Segmentation Mask/STL generation/Editing of all phases in a 4D Cardiac MRI dataset

**Topic ID**: 25199
**Date**: 2022-09-11
**URL**: https://discourse.slicer.org/t/segmentation-mask-stl-generation-editing-of-all-phases-in-a-4d-cardiac-mri-dataset/25199

---

## Post #1 by @Yue-Hin_Loke (2022-09-11 01:28 UTC)

<p>Hi there,</p>
<p>I have used the Segment Registration Module to create a moving mask (whole heart and/or atrium + ventricle) of the 4D Cardiac MRI dataset. I was able to follow most of the discussion from here: <a href="https://discourse.slicer.org/t/load-multiple-cardiac-phases-for-segmentation-virtual-reality/5214/2" class="inline-onebox">Load multiple cardiac phases for segmentation/virtual reality - #2 by lassoan</a> and the video (<a href="https://www.youtube.com/watch?v=qVgXdXEEVFU" class="inline-onebox" rel="noopener nofollow ugc">Create an animated 4D surface model by segmenting a single 3D frame - YouTube</a>)</p>
<p>Ultimately I end up generating a segmented mask that and a transform output that mostly follows to what I want, with some areas that I would like to further tweak and edit.</p>
<p>I had several questions:</p>
<p><span class="hashtag">#1</span>) What is the best/efficient way of going from here to create STLs for each timepoint (i.e. t1… t30), such that I can open up a moving STL on another software like Paraview?<br>
<span class="hashtag">#2</span>) If there is something off in the transformed segmentation during one of the cardiac phases, what is the best way to edit this?<br>
<span class="hashtag">#3</span>) How do I edit the transformed output?</p>
<p>Can provide more specific details if needed. Thank you!</p>

---

## Post #2 by @Yue-Hin_Loke (2022-09-12 18:55 UTC)

<p>Somewhat answering my own question, I was able to use the Python code to export the transformed segmentations into .ply from the repository (see below).</p>
<p>I still have questions related to whether I can adjust the warping manually (ideally without resegmenting at that particular phase, as I still want to maintain coordinates across the segementation. thanks!</p>
<pre><code class="lang-python"># Inputs
transformSequenceNode = getNode("OutputTransforms")
segmentationNode = getNode("Segmentation")
segmentIndex = 0
outputFilePrefix = r"c:/tmp/20220312/seg"

# Ensure the segmentation contains closed surface representation
segmentationNode.CreateClosedSurfaceRepresentation()
# Create temporary node that will be warped
segmentModelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')

for itemIndex in range(transformSequenceNode.GetNumberOfDataNodes()):
  # Get a copy of the segment that will be transformed
  segment = segmentationNode.GetSegmentation().GetNthSegment(segmentIndex)
  slicer.modules.segmentations.logic().ExportSegmentToRepresentationNode(segment, segmentModelNode)
  # Apply the transform
  transform = transformSequenceNode.GetNthDataNode(itemIndex).GetTransformToParent()
  segmentModelNode.ApplyTransform(transform)
  # Write to file
  outputFileName = f"{outputFilePrefix}_{itemIndex:03}.ply"
  print(outputFileName)
  slicer.util.saveNode(segmentModelNode, outputFileName)

# Delete temporary node
slicer.mrmlScene.RemoveNode(segmentModelNode)
</code></pre>

---

## Post #3 by @lassoan (2022-09-16 22:04 UTC)

<aside class="quote no-group" data-username="Yue-Hin_Loke" data-post="2" data-topic="25199">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yue-hin_loke/48/16602_2.png" class="avatar"> Yue-Hin_Loke:</div>
<blockquote>
<p>whether I can adjust the warping manually</p>
</blockquote>
</aside>
<p>You can use landmark registration (for example, in Fiducial Registration Wizard module of SlicerIGT extension) to slightly shift/warp certain regions of a data set (segmentation, image, model, …), as shown in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="GfDDQykH1iY" data-video-title="Soft tissue deformation simulation" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=GfDDQykH1iY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/GfDDQykH1iY/maxresdefault.jpg" title="Soft tissue deformation simulation" width="" height="">
  </a>
</div>


---

## Post #4 by @Yue-Hin_Loke (2022-09-23 01:32 UTC)

<p>Thanks! The landmark registration appears to warp all the time points in the transform sequence (i.e. I just want to adjust time point 3 - 8, but after applying this it warps everything every after and everything before time point 8). Any way to use landmark registration to only adjust the mesh at several time points and not the rest?</p>
<p>Another potential solution, I sort of was able to improve this address my issue by “concatenating” two separate sequence registrations together - one transform that goes from timepoint 1-&gt;8, the other from 8-&gt;25, then hardening the transform at time point 8 and export the two of them separately; there is some slight differences between the mesh during the transition and ideally I’d like keep the same mesh for everything (hence my desire to only manually adjust the warping above). Any advice?</p>

---
