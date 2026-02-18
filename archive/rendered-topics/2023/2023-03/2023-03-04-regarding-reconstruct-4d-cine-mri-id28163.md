# Regarding Reconstruct 4D cine MRI

**Topic ID**: 28163
**Date**: 2023-03-04
**URL**: https://discourse.slicer.org/t/regarding-reconstruct-4d-cine-mri/28163

---

## Post #1 by @ICUH (2023-03-04 03:36 UTC)

<p>Hi.<br>
I have 2D Cine MRI images with 25 frames for 2ch/4ch/multiple SAX slices.<br>
I was trying to generate 4D cine from those images using Reconstruct 4D Cine MRI from Slicer Heart plug in.<br>
Each set of images are loaded as 25 frames Volume sequence and have multiple of those volume sequence for each sax and 2ch/4ch.<br>
When I tried to run the reconstruct (apply) it initially fail due to “Failed to get frame indices automatically Trigger Time DICOM tag is not found in the input sequence. Specify them manually in Advanced section.”<br>
So I set it up as manual, turn off auto detect and run it again but I get his error in python script.<br>
“int __cdecl ctkVTKAbstractView::resumeRender(void) Cannot resume rendering, pause render count is already 0!”<br>
I have zero idea why is that happening. Doesn’t look like it’s referencing any thing in the script either.<br>
I could manually modify dicom header to frame information but I need to know dicom header address as well.</p>
<p>If anyone came across this problem and had a solution let me know.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2023-03-04 04:16 UTC)

<p>If your series does not contain trigger time then specify the frame indices manually. There is no need to modify DICOM headers. You can find <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/Reconstruct4DCineMRI.md#reconstruct-volume-with-custom-frame-grouping">more information and example in the module documentation</a>.</p>
<aside class="quote no-group" data-username="ICUH" data-post="1" data-topic="28163">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/icuh/48/18628_2.png" class="avatar"> ICUH:</div>
<blockquote>
<p>int __cdecl ctkVTKAbstractView::resumeRender(void) Cannot resume rendering, pause render count is already 0!</p>
</blockquote>
</aside>
<p>This is a false alarm, you can ignore this warning.</p>

---
