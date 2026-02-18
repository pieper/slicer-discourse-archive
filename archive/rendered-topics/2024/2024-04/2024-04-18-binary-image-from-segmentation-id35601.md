# Binary image from segmentation

**Topic ID**: 35601
**Date**: 2024-04-18
**URL**: https://discourse.slicer.org/t/binary-image-from-segmentation/35601

---

## Post #1 by @ahmad_alminnawi (2024-04-18 13:59 UTC)

<p>Hi all,</p>
<p>I have a segmentation and I want to select some slices (planes) that I want to convert to 2D binary images (lets say the xy plane at z=0) for example.</p>
<p>I found the question asked <a href="https://discourse.slicer.org/t/export-binary-mask-of-the-segmentation-as-jpeg-png/28256">here</a> where the advice was to Export as LabelMap and save it as nrrd file but when I do so, i don’t see anything basically the labelMap is empty or it looks empty to me.</p>
<p>in a similar topic <a href="https://discourse.slicer.org/t/cannot-save-binary-mask-of-annottated-images-from-segmentation-module/8829/2">here</a> the question "how to visualize the labelMap if we save it as a nrrd file was not answered</p>
<p>I would prefer using python to automate it but i wouldn’t mind using the GUI as well</p>
<p>can someone help with this issue please?</p>

---

## Post #2 by @muratmaga (2024-04-18 15:00 UTC)

<aside class="quote no-group" data-username="ahmad_alminnawi" data-post="1" data-topic="35601">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ahmad_alminnawi/48/66700_2.png" class="avatar"> ahmad_alminnawi:</div>
<blockquote>
<p>I have a segmentation and I want to select some slices (planes) that I want to convert to 2D binary images (lets say the xy plane at z=0) for example.</p>
</blockquote>
</aside>
<p>As mentioned in the thread you linked, Slicer doesn’t allow exporting 2D slices. The most you can do is to use tiff format instead of NRRD. in that case, this will be a multi-frame TIFF (that is a single file, with all the slices inside).</p>
<p>If you are going to do this selectively (i.e., only export a few selected Slicer), you can possibly use the Screencapture module to save what’s visible in the 2D viewers as PNG or JPG. But then you will lose geometry information.</p>
<aside class="quote no-group" data-username="ahmad_alminnawi" data-post="1" data-topic="35601">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ahmad_alminnawi/48/66700_2.png" class="avatar"> ahmad_alminnawi:</div>
<blockquote>
<p>I found the question asked <a href="https://discourse.slicer.org/t/export-binary-mask-of-the-segmentation-as-jpeg-png/28256">here </a> where the advice was to Export as LabelMap and save it as nrrd file but when I do so, i don’t see anything basically the labelMap is empty or it looks empty to me.</p>
</blockquote>
</aside>
<p>Unless your segmentations/labelmaps fill a large portion of the volume, most of the resultant file will be empty (0s).</p>

---
