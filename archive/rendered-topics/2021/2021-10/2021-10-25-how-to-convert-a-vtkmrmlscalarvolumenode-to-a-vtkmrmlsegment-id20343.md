---
topic_id: 20343
title: "How To Convert A Vtkmrmlscalarvolumenode To A Vtkmrmlsegment"
date: 2021-10-25
url: https://discourse.slicer.org/t/20343
---

# How to convert a vtkMRMLScalarVolumeNode to a vtkMRMLSegmentationNode

**Topic ID**: 20343
**Date**: 2021-10-25
**URL**: https://discourse.slicer.org/t/how-to-convert-a-vtkmrmlscalarvolumenode-to-a-vtkmrmlsegmentationnode/20343

---

## Post #1 by @kkkkkkk123 (2021-10-25 17:31 UTC)

<p>Hi all,<br>
I’m trying to convert a vtkMRMLScalarVolumeNode to a new vtkMRMLSegmentationNode (in Python) and I don’t seem to get it figured out… The scalar volume is basically just a binary image but I want it to be rendered as a segmentation (contour) and not a volume.<br>
Does anyone know how I can achieve this? Thanks in advance!</p>

---

## Post #2 by @mikebind (2021-10-25 18:50 UTC)

<p>You can programmatically use the segment editor tools to generate a segment from your binary image using a threshold (check out the segmentations section of the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations" rel="noopener nofollow ugc">script repository</a>), though there is probably a simpler way given that you basically already have a thresholded image. If it helps, it looks like you can load your volume as a segmentation (see instructions here <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file" class="inline-onebox" rel="noopener nofollow ugc">Segmentations — 3D Slicer documentation</a>).  That’s not exactly the same as converting an already loaded volume, but maybe it will work for you.</p>

---

## Post #3 by @cpinter (2021-10-26 08:42 UTC)

<p>There are convenience tools to do this conversion. Thresholding as suggested above is an error-prone workaround, so I suggest using the built-in function called <code>ImportLabelmapToSegmentationNode</code>, see <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#adf111c9bcd3ceb28d49028f6fc6a2506" class="inline-onebox">Slicer: vtkSlicerSegmentationsModuleLogic Class Reference</a></p>

---

## Post #4 by @kkkkkkk123 (2021-10-26 08:48 UTC)

<p>Thank you, it was indeed the preferred method! <img src="https://emoji.discourse-cdn.com/twitter/grinning_face_with_smiling_eyes.png?v=10" title=":grinning_face_with_smiling_eyes:" class="emoji" alt=":grinning_face_with_smiling_eyes:"></p>

---

## Post #5 by @helenawill95 (2022-01-21 12:32 UTC)

<p>I may have missed something, I see that the input to the function is a label map, is there anyway to input a volume Node instead i.e. convert the volume node to a segmentation then labelmap.</p>

---

## Post #6 by @cpinter (2022-01-21 13:19 UTC)

<aside class="quote no-group" data-username="helenawill95" data-post="5" data-topic="20343">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/helenawill95/48/2650_2.png" class="avatar"> helenawill95:</div>
<blockquote>
<p>convert the volume node to a segmentation then labelmap</p>
</blockquote>
</aside>
<p>When you say “convert the volume node to a segmentation” do you mean segmenting an anatomical image like a CT or MRI? For that you need to use the Segment Editor module.</p>

---

## Post #7 by @helenawill95 (2022-01-21 14:28 UTC)

<p>I have a binary 3D mask of a structure that I load as a volume node instead of a segmentation node, I then just want to convert it to a segmentation node later on in a post-processing step.</p>

---

## Post #8 by @mikebind (2022-01-21 20:06 UTC)

<p>If your scalar volume is already a binary labelmap (just imported as a scalar volume instead), then the easiest method is to convert your scalar volume to a labelmap using the Volumes module, in the “Volume Information” section:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecad23fc2cd2765b2a1763e42ac51b4655ce01ce.png" alt="image" data-base62-sha1="xLJDmRjLcy9mH0myrJ4drJ3jgOW" width="584" height="75"></p>
<p>and then import the labelmap as a segmentation using the “Segmentations” module in the “Export/Import models and labelmaps” section:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51e176de0131840ff76405003d196654cfa00aee.png" alt="image" data-base62-sha1="bGlJgRTirbrrzeEoiL2GoLqwiAK" width="578" height="214"></p>
<p>or programmatically using <code>ImportLabelmapToSegmentationNode</code> as suggested above.</p>

---
