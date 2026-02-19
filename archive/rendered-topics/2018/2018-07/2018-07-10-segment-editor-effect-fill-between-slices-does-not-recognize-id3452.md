---
topic_id: 3452
title: "Segment Editor Effect Fill Between Slices Does Not Recognize"
date: 2018-07-10
url: https://discourse.slicer.org/t/3452
---

# Segment Editor Effect: Fill Between Slices does not recognize existing contour

**Topic ID**: 3452
**Date**: 2018-07-10
**URL**: https://discourse.slicer.org/t/segment-editor-effect-fill-between-slices-does-not-recognize-existing-contour/3452

---

## Post #1 by @MRXCAT_CMR (2018-07-10 21:01 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.1 (r26813) built myself</p>
<p><strong>Background:</strong><br>
I have started some work on automatic segmentation using the Segment Editor framework. Now I have an automatically generated contour for the spinal canal. The contour is present in some slices (about every 3rd), and is not present in others. Now I thought about including some methodology from “Fill between slices” module. The first attempt before automating is testing manually by clicking through the GUI.</p>
<p><strong>Approach - step by step</strong></p>
<ol>
<li>Select contour called “Spinal canal” and open “Fill between slices” module</li>
<li>Click “Initialize”</li>
<li>Check the result by using the slider - the results contour is empty</li>
<li>Then I selected the “Paint” module for some testing, draw a small region in an empty slice of “Spinal canal” contour.</li>
<li>Now try “Initialize” again in the “Fill between slices” module, and wow, the result looks good.</li>
</ol>
<p><strong>Problem analysis</strong><br>
Obviously, there’s something wrong which makes my automatically segmented structure not being recognized by the “Fill between slices” module. But what?</p>
<p>I analyzed the source and had a look at the file <code>AbstractScriptedSegmentEditorAutoCompleteEffect.py</code>, and the <code>preview</code> method, there around line 342, which looks like this:</p>
<pre><code>previewNode.SetName(segmentationNode.GetName()+" preview")

mergedImage = vtkSegmentationCore.vtkOrientedImageData()
segmentationNode.GenerateMergedLabelmapForAllSegments(mergedImage,
  vtkSegmentationCore.vtkSegmentation.EXTENT_UNION_OF_EFFECTIVE_SEGMENTS, self.mergedLabelmapGeometryImage, self.selectedSegmentIds)
</code></pre>
<p>There was a difference in <code>mergedImage</code> variable:<br>
a) In the situation when I used my contour only, <code>mergedImage</code> is empty<br>
b) If I apply some paint operation, <code>mergedImage</code> contains all the masks (the painted + the automatically segmented)</p>
<p><strong>Questions/Problem solving</strong>:</p>
<ul>
<li>What may be wrong/missing in my auto-segmentation, so that “Fill between slices” won’t recognize my masks?</li>
<li>To find out more, I tried to debug the “Paint” module. I was not successful. Where in the code can I find the “Paint” module methods?</li>
</ul>

---

## Post #2 by @lassoan (2018-07-11 00:21 UTC)

<p>What do you mean by <em>Select contour called “Spinal canal”</em>? You create a segmentation node and create a segment in it (“Spinal canal”)? Does the segment show up correctly in slice views?</p>
<aside class="quote no-group" data-username="MRXCAT_CMR" data-post="1" data-topic="3452">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> MRXCAT_CMR:</div>
<blockquote>
<p>“Initialize” again in the “Fill between slices” module, and wow, the result looks good.</p>
</blockquote>
</aside>
<p>Do you mean that slices are filled around the new region only, or throughout the whole image?</p>
<aside class="quote no-group" data-username="MRXCAT_CMR" data-post="1" data-topic="3452">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> MRXCAT_CMR:</div>
<blockquote>
<p>What may be wrong/missing in my auto-segmentation, so that “Fill between slices” won’t recognize my masks?</p>
</blockquote>
</aside>
<p>Fill between slices only considers visible segments, so make sure you have a display node and the segment is visible. Also, interpolation only happens around slices that have at least one completely empty slice on both sides.</p>
<aside class="quote no-group" data-username="MRXCAT_CMR" data-post="1" data-topic="3452">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> MRXCAT_CMR:</div>
<blockquote>
<p>To find out more, I tried to debug the “Paint” module. I was not successful. Where in the code can I find the “Paint” module methods</p>
</blockquote>
</aside>
<p>Paint effect is implemented in C++, source code is available on <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorPaintEffect.cxx">GitHub/Slicer</a>.</p>

---

## Post #3 by @MRXCAT_CMR (2018-07-12 08:53 UTC)

<p>Thank you for the quick reply!</p>
<aside class="quote no-group" data-username="&quot;lassoan" data-post="2" data-topic="3452">
<div class="title">
<div class="quote-controls"></div>
 "lassoan:</div>
<blockquote>
<p>What do you mean by <em>Select contour called “Spinal canal”</em>? You create a segmentation node and create a segment in it (“Spinal canal”)? Does the segment show up correctly in slice views?</p>
</blockquote>
</aside>
<p>Yes, exactly. I have a segmentation node, and in it a few segments. One of them and the only selected and visible is <em>“Spinal canal”</em>. It shows up correctly in slice views.</p>
<aside class="quote no-group quote-modified" data-username="&quot;lassoan" data-post="2" data-topic="3452">
<div class="title">
<div class="quote-controls"></div>
 "lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="MRXCAT_CMR" data-post="1" data-topic="3452">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> MRXCAT_CMR:</div>
<blockquote>
<p>“Initialize” again in the “Fill between slices” module, and wow, the result looks good.</p>
</blockquote>
</aside>
<p>Do you mean that slices are filled around the new region only, or throughout the whole image?</p>
</blockquote>
</aside>
<p>Slices are filled in all the regions between “Spinal canal” segmented slices, i.e. the whole image. This means also in the slices that were not drawn by Paint, but by my owm method.<br>
In effect, I place one point in one slice by Paint and it works the same for all slices (and as intended). But it does not work at all without putting the point via Paint.</p>
<aside class="quote no-group quote-modified" data-username="&quot;lassoan" data-post="2" data-topic="3452">
<div class="title">
<div class="quote-controls"></div>
 "lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="MRXCAT_CMR" data-post="1" data-topic="3452">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> MRXCAT_CMR:</div>
<blockquote>
<p>What may be wrong/missing in my auto-segmentation, so that “Fill between slices” won’t recognize my masks?</p>
</blockquote>
</aside>
<p>Fill between slices only considers visible segments, so make sure you have a display node and the segment is visible. Also, interpolation only happens around slices that have at least one completely empty slice on both sides.</p>
</blockquote>
</aside>
<p>The segment is visible (and selected). Slices in-between are empty.</p>
<p>About the display node, I am a bit unsure, whether I have one or not. But I think I have one. I can run<br>
<code>segmentationNode.GetDisplayNode()</code><br>
and get a <code>vtkMRMLSegmentationDisplayNode</code> as output. Does it mean I do have a display node?</p>
<aside class="quote no-group quote-modified" data-username="&quot;lassoan" data-post="2" data-topic="3452">
<div class="title">
<div class="quote-controls"></div>
 "lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="MRXCAT_CMR" data-post="1" data-topic="3452">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a698b9/48.png" class="avatar"> MRXCAT_CMR:</div>
<blockquote>
<p>To find out more, I tried to debug the “Paint” module. I was not successful. Where in the code can I find the “Paint” module methods</p>
</blockquote>
</aside>
<p>Paint effect is implemented in C++, source code is available on <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorPaintEffect.cxx" rel="noopener nofollow ugc">GitHub/Slicer</a>.</p>
</blockquote>
</aside>
<p>Thanks, so I know where to look and I’ll check it out to see if I can get some hints.</p>

---

## Post #4 by @lassoan (2018-07-12 12:55 UTC)

<p>If your segment shows up then it means you have a display node.</p>
<p>Do you select a master volume node before you create your automatic segmentation?</p>
<p>How do you create the automatic segmentation? By adding a custom segment editor effect and running it from the Segment editor?</p>

---

## Post #5 by @MRXCAT_CMR (2018-07-12 20:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="3452" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If your segment shows up then it means you have a display node.</p>
<p>Do you select a master volume node before you create your automatic segmentation?</p>
<p>How do you create the automatic segmentation? By adding a custom segment editor effect and running it from the Segment editor?</p>
</blockquote>
</aside>
<p>Yes. I do select a master volume node, corresponding my loaded data, via</p>
<p><code>segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</code></p>
<p>as in <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" rel="noopener nofollow ugc">SegmentGrowCutSimple.py</a></p>
<p>My automatic segmentation method is a separate segment editor effect added to the list of effects (like Paint, Fill between slices or Grow from seeds etc.). It is derived from the <a href="https://github.com/Slicer/Slicer/blob/master/Extensions/Testing/ScriptedSegmentEditorEffectExtensionTemplate/ScriptedSegmentEditorEffectModuleTemplate/SegmentEditorScriptedSegmentEditorEffectModuleTemplateLib/SegmentEditorEffect.py" rel="noopener nofollow ugc">SegmentEditorEffect.py</a> example, and modified quite a bit.</p>
<p>It uses numpy and vtk a lot, and convenience functions in <code>slicer.util</code> to convert to segments and back.</p>

---

## Post #6 by @lassoan (2018-07-13 03:02 UTC)

<p>Does it work correctly if you save the segmentation node to file and then load that file?<br>
If yes, then send me the file and I’ll have a look.</p>

---

## Post #7 by @MRXCAT_CMR (2018-07-16 10:35 UTC)

<aside class="quote" data-post="6" data-topic="3452">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segment-editor-effect-fill-between-slices-does-not-recognize-existing-contour/3452/6">Segment Editor Effect: Fill Between Slices does not recognize existing contour</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Does it work correctly if you save the segmentation node to file and then load that file? 
If yes, then send me the file and I’ll have a look.
  </blockquote>
</aside>

<p>Yes, indeed, it works correctly once I load the segmentation from file. I’ve saved the segmentation and I’ll send you the file. Thanks a lot!</p>

---

## Post #8 by @lassoan (2018-07-17 04:23 UTC)

<p>If everything works if you save and reload the file then maybe you miss a Modified() event. For example, after you’ve finished changing voxels in numpy, you must call <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L760-L769">arrayFromVOlumeModified()</a> to signal VTK that the changes are ready to be processed.</p>

---

## Post #9 by @MRXCAT_CMR (2018-07-17 13:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="3452" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If everything works if you save and reload the file then maybe you miss a Modified() event. For example, after you’ve finished changing voxels in numpy, you must call <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L760-L769" rel="noopener nofollow ugc">arrayFromVOlumeModified()</a> to signal VTK that the changes are ready to be processed.</p>
</blockquote>
</aside>
<p>My code for updating the <em>“Spinal Canal”</em> mask reads:</p>
<pre><code>seg2export = vtk.vtkStringArray()
seg2export.InsertNextValue('Spinal Canal')
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segNode, seg2export, labelmapVolumeNode)
slicer.util.updateVolumeFromArray(labelmapVolumeNode, spinalCanalMask)
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, segNode, seg2export)
</code></pre>
<p>and within <code>slicer.util.updateVolumeFromArray()</code> the <code>volumeNode.Modified()</code> method is called. There is no modification of the <code>spinalCanalMask</code> beyond these lines of code.</p>
<p>Do you see any problem with this approach in terms of signalling to VTK using <code>Modified()</code>, or any other error?</p>

---

## Post #10 by @lassoan (2018-07-17 15:24 UTC)

<p>Could you send the link to your complete extension? It does not matter if it is not fully stable or cleaned but, just as it is now.</p>

---
