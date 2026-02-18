# I cannot DICOM image export with a segment

**Topic ID**: 11788
**Date**: 2020-05-29
**URL**: https://discourse.slicer.org/t/i-cannot-dicom-image-export-with-a-segment/11788

---

## Post #1 by @11139 (2020-05-29 18:54 UTC)

<p>I want to draw contour with dicom image sequence and export them together as DICOM images.<br>
I tried to export them but only exported original DICOM image sequence(the image sequence didn’t have any segment（contours）.<br>
Please tell me how to export DICOM image sequence with segment.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/520034574e65cf424eaa7c74169df35cdd26ec3b.jpeg" data-download-href="/uploads/short-url/bHpACmjuJjv8NNM4vMFRM3ES2Cf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/520034574e65cf424eaa7c74169df35cdd26ec3b_2_690x369.jpeg" alt="image" data-base62-sha1="bHpACmjuJjv8NNM4vMFRM3ES2Cf" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/520034574e65cf424eaa7c74169df35cdd26ec3b_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/520034574e65cf424eaa7c74169df35cdd26ec3b_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/520034574e65cf424eaa7c74169df35cdd26ec3b_2_1380x738.jpeg 2x" data-dominant-color="9B9B9C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1029 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2020-05-29 23:42 UTC)

<p>I’ve just tested this with Slicer 4.11.0-2020-05-27 (revision 29081 / abc9bd3) win-amd64 and it worked perfectly.</p>
<p>Make sure SlicerRT is installed correctly. You can try to reinstall it (make sure you wait until the “Restart” button appears and click that).</p>

---

## Post #4 by @11139 (2020-05-30 04:09 UTC)

<p>Thank you for replying my question!<br>
I uninstalled slicerRT, clicked restart, reinstalled it, and clicked restart.<br>
However I couldn’t select RT as export type…</p>
<p>I tried such as, two times.</p>
<p>Are there else solutions?</p>

---

## Post #5 by @lassoan (2020-05-30 04:21 UTC)

<p>Could you share your scene file (saved as a .mrb file)? If you used any data that you would not like to share then you can recreate a scene using any of the Slicer sample data sets.</p>

---

## Post #7 by @lassoan (2020-05-31 00:50 UTC)

<p>If you can reproduce the problem using public sample data sets then that’s great. Just save the scene that you have prepared into a .mrb file, upload it somewhere, and post the link here. It would also help if you could upload the application log of the session where you attempted an export (available in menu: Help / Report a bug).</p>

---
