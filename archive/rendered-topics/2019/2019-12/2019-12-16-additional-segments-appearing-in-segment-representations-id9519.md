# Additional segments appearing in segment representations

**Topic ID**: 9519
**Date**: 2019-12-16
**URL**: https://discourse.slicer.org/t/additional-segments-appearing-in-segment-representations/9519

---

## Post #1 by @dominicrushforth (2019-12-16 18:17 UTC)

<p>I think I have found a bug where segments are not displaying properly.</p>
<p>In one scenario I have a segment that includes both the left kidney and the spleen. I then separate this into two seperate segments. Both of these segments display as expected. However if I create a new segment and copy of one of the split segments into it using the command ‘DeepCopy’ the new segment now displays both of the split segments at once…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46900308c60c9a48a509909e12b66ff882f5ce74.png" data-download-href="/uploads/short-url/a4dXWLZ4yFiHZpc5gAPlezN7tv6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46900308c60c9a48a509909e12b66ff882f5ce74_2_625x500.png" alt="image" data-base62-sha1="a4dXWLZ4yFiHZpc5gAPlezN7tv6" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46900308c60c9a48a509909e12b66ff882f5ce74_2_625x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46900308c60c9a48a509909e12b66ff882f5ce74_2_937x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46900308c60c9a48a509909e12b66ff882f5ce74_2_1250x1000.png 2x" data-dominant-color="87868C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×1024 320 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In this image only the segment ‘left kidney - temporary copy’ should be visible. It is displayed correctly in the 3D representation but not in the 2D slices. In the image the segment name can be seen in the data probe but if the mouse pointer is moved over the 2D representation of the spleen no segment name/information can be seen.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6993494f20c09eb1c005f87a1556c7bc4e12de33.jpeg" data-download-href="/uploads/short-url/f3XH1DTlaY9s7GLu7DIY1iqde7h.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6993494f20c09eb1c005f87a1556c7bc4e12de33_2_625x500.jpeg" alt="image" data-base62-sha1="f3XH1DTlaY9s7GLu7DIY1iqde7h" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6993494f20c09eb1c005f87a1556c7bc4e12de33_2_625x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6993494f20c09eb1c005f87a1556c7bc4e12de33_2_937x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6993494f20c09eb1c005f87a1556c7bc4e12de33_2_1250x1000.jpeg 2x" data-dominant-color="87878C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×1024 329 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In this second image the segments were loaded from an RTStruct file and converted into a binary labelmap. When a copy of one of the segments is again created using DeepCopy, multiple ‘ghost’ segments can be seen (the number is dependent on the segment copied) even though only the ‘Left Kidney 1 - temporary copy’ segment should be visible. It is notable in this image that the although the spleen and right kidney are both ‘ghosts’, they have very different appearences.</p>
<p>Testing has confirmened that the ghost segments appear when the ‘DeepCopy’ line is run. I am using r28683.</p>
<p>I started trying to make a workaround by using ‘DeepCopyMetadata’ and creating new representations for the copied segments but haven’t got it working yet. Presumably it shouldn’t really be necessary.</p>

---

## Post #2 by @Sunderlandkyl (2019-12-16 18:21 UTC)

<p>Thanks for reporting this issue!<br>
I’m working on a fix, and will let you know when it’s integrated.</p>

---

## Post #3 by @Sunderlandkyl (2019-12-18 14:20 UTC)

<p><a class="mention" href="/u/dominicrushforth">@dominicrushforth</a> This issue should be fixed in the latest nightly.</p>

---

## Post #4 by @dominicrushforth (2019-12-18 15:47 UTC)

<p>Thanks. It’s seriously impressive how you guys fix things so quickly.</p>

---
