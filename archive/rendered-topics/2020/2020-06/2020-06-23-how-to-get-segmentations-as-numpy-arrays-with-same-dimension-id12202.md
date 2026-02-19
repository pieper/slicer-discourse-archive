---
topic_id: 12202
title: "How To Get Segmentations As Numpy Arrays With Same Dimension"
date: 2020-06-23
url: https://discourse.slicer.org/t/12202
---

# How to get segmentations as numpy arrays with same dimensions?

**Topic ID**: 12202
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/how-to-get-segmentations-as-numpy-arrays-with-same-dimensions/12202

---

## Post #1 by @SummerZ2020 (2020-06-23 06:57 UTC)

<p>hello, lassoan. I encountered the same problem when save the segmentation result to file. I right clicked the segmentation in the “Subject hierarchy”, and then choose “export visible segments to binary labelmap”, and got the labelmap which name is “Segmentation-bone-label”. And then I got the segmentation mask array using python. But the size of each image in segmentation mask is only 224<em>332, and the original image in volume is 512</em>512. I got the segmentation mask which size is same as original image before. And I donot know why this time the size is only bounding box. Here is the python code I used:</p>
<blockquote>
<blockquote>
<blockquote>
<p>bone=array(“Segmentation-bone-label”)<br>
bone.shape<br>
(114, 224, 322)<br>
volume = array(“5 ARTERIAL PHASE”)<br>
volume.shape<br>
(114, 512, 512)</p>
</blockquote>
</blockquote>
</blockquote>
<p>Looking forward to your reply, thank you so much.</p>

---

## Post #2 by @lassoan (2020-06-23 21:40 UTC)

<p>The simplest is to use the latest Slicer version, which does not crop the segmentation to the minimum necessary size. If you already created your segmentation in Slicer-4.10 then you need to specify a Reference volume as described above.</p>

---

## Post #4 by @SummerZ2020 (2020-06-24 01:36 UTC)

<p>The version is 4.11(2020-6-15). And where can i find the advanced export section in 4.11 to add reference volume. In the screenshot below, you can see the segmentation size is not 512*512, and the Slicer version is 4.11.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89cead611f9eb57d62200b2ac267bca632f49de5.png" data-download-href="/uploads/short-url/jF6dtRqr8CMOoNdxUN5axI319bL.png?dl=1" title="export" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89cead611f9eb57d62200b2ac267bca632f49de5_2_386x500.png" alt="export" data-base62-sha1="jF6dtRqr8CMOoNdxUN5axI319bL" width="386" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89cead611f9eb57d62200b2ac267bca632f49de5_2_386x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89cead611f9eb57d62200b2ac267bca632f49de5_2_579x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89cead611f9eb57d62200b2ac267bca632f49de5_2_772x1000.png 2x" data-dominant-color="F4F8F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">export</span><span class="informations">816×1055 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2020-06-24 15:35 UTC)

<p>How did you create <code>Segmentation_1-bone-label</code> and <code>Segmentation_2-bone-label</code>?<br>
If they were created from two different segmentations (of two different volumes), could you check the dimensions of these volumes (in Volumes module, Volume Information section)?</p>

---

## Post #6 by @JanWitowski (2020-06-25 06:40 UTC)

<p>In addition to <a class="mention" href="/u/lassoan">@lassoan</a> replies, you can change the segmentation geometry to match volume geometry with <code>SetReferenceImageGeometryParameterFromVolumeNode()</code>. This allowed me in the past to batch process mismatched examples, e.g.</p>
<pre><code>loadedVolumeNode = slicer.util.loadVolume(ct_path)
loadedSegmentationNode = slicer.util.loadSegmentation(seg_path)
loadedSegmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(loadedVolumeNode)
slicer.util.saveNode(loadedSegmentationNode, seg_path)
slicer.mrmlScene.RemoveNode(loadedVolumeNode)
slicer.mrmlScene.RemoveNode(loadedSegmentationNode)</code></pre>

---

## Post #7 by @SummerZ2020 (2020-06-25 14:09 UTC)

<p>yes, they are from differnent volumes.Here is how can I create the labelmap in the scrrenshot 1-2. and the third screenshot showes the volume dimension. And I tried to get the  dimension of the labelmap, the result is shown below.</p>
<blockquote>
<blockquote>
<blockquote>
<p>bone = array(“Segmentation_5-bone-label”)<br>
bone.shape<br>
(118, 276, 382)<br>
volume = array(“4 Tx Abdomen 5mm”)<br>
volume.shape<br>
(118, 512, 512)</p>
</blockquote>
</blockquote>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce7a4b281f5fa80a0b0e9dd2e856dadd5546f16b.jpeg" data-download-href="/uploads/short-url/tsAn2OPZd2EN7GBqmdV9XZTvYuv.jpeg?dl=1" title="binary" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce7a4b281f5fa80a0b0e9dd2e856dadd5546f16b_2_690x367.jpeg" alt="binary" data-base62-sha1="tsAn2OPZd2EN7GBqmdV9XZTvYuv" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce7a4b281f5fa80a0b0e9dd2e856dadd5546f16b_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce7a4b281f5fa80a0b0e9dd2e856dadd5546f16b_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce7a4b281f5fa80a0b0e9dd2e856dadd5546f16b_2_1380x734.jpeg 2x" data-dominant-color="A5A7AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">binary</span><span class="informations">1920×1023 272 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @SummerZ2020 (2020-06-25 14:37 UTC)

<p>I found if I save the segmentation to nrrd file first, and then load it and volume again. and then the labelmap created from the segmentation is bounding box size. If I save the segmentation directly after segmentation, the labelmap size is same as the volume(512*512).</p>

---

## Post #9 by @SummerZ2020 (2020-06-25 14:57 UTC)

<aside class="quote no-group" data-username="JanWitowski" data-post="6" data-topic="12202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/janwitowski/48/4512_2.png" class="avatar"> JanWitowski:</div>
<blockquote>
<p><code>loadedSegmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(loadedVolumeNode)</code></p>
</blockquote>
</aside>
<p>Your solution works greatly. Thanks a lot. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"><br>
BTW, do you know how to get the node name (like loadSegmentationNode and loadedVolumeNode in your code) if I load the volume and segmentation from GUI. thanks again.</p>

---
