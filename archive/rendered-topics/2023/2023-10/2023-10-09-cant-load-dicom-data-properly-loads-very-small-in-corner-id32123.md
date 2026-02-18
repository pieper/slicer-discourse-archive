# Cant load dicom data properly, loads very small in corner

**Topic ID**: 32123
**Date**: 2023-10-09
**URL**: https://discourse.slicer.org/t/cant-load-dicom-data-properly-loads-very-small-in-corner/32123

---

## Post #1 by @studyskin (2023-10-09 18:03 UTC)

<p>hi, i am trying to import this dicom data but it loads only in the corner of the viewer and very small, i have included a screenshot but it is hard to see<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b5b6fd3912dad47e2567b9e6ad2b6133f6424c9.png" data-download-href="/uploads/short-url/3U0NeRF5yN4eCgOi3t8Jz41ovy1.png?dl=1" title="Screenshot 2023-10-09 183712" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b5b6fd3912dad47e2567b9e6ad2b6133f6424c9_2_690x366.png" alt="Screenshot 2023-10-09 183712" data-base62-sha1="3U0NeRF5yN4eCgOi3t8Jz41ovy1" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b5b6fd3912dad47e2567b9e6ad2b6133f6424c9_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b5b6fd3912dad47e2567b9e6ad2b6133f6424c9_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b5b6fd3912dad47e2567b9e6ad2b6133f6424c9_2_1380x732.png 2x" data-dominant-color="6F6F77"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-09 183712</span><span class="informations">1920×1021 60.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
here is the <a href="https://drive.google.com/drive/folders/12Ee7r19AXiC7RusUBK79gMtlrKCyAhqo?usp=sharing" rel="noopener nofollow ugc">data</a><br>
thank you so much to anyone who can help! i have tried YouTube videos but i cant find anyone else with this issue</p>

---

## Post #2 by @muratmaga (2023-10-09 20:54 UTC)

<p>I managed to get the data in by simply drag and dropping the one of the dicom images and loading it as a volume. This is not the proper way of loading DICOMs, it should really work with DICOM module, and given that even after patching it doesnt suggest,  this DICOM sequence is ill-prepared, and not standards compliant. For example, I am getting this error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64fff4a5f69d253a750c06cce518c31d7bc86381.png" data-download-href="/uploads/short-url/epu81QhrwjqE5WAFNUAU63ssXvj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64fff4a5f69d253a750c06cce518c31d7bc86381.png" alt="image" data-base62-sha1="epu81QhrwjqE5WAFNUAU63ssXvj" width="690" height="253" data-dominant-color="F1F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1159×426 17.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For example, I don’t think this skull is couple meters long, which is what the data reports.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19926371aa51226712ace92310758959fddeb149.jpeg" data-download-href="/uploads/short-url/3EdzuYNGTm0p9NVAgNfLNCzBBzP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19926371aa51226712ace92310758959fddeb149_2_690x305.jpeg" alt="image" data-base62-sha1="3EdzuYNGTm0p9NVAgNfLNCzBBzP" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19926371aa51226712ace92310758959fddeb149_2_690x305.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19926371aa51226712ace92310758959fddeb149_2_1035x457.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19926371aa51226712ace92310758959fddeb149_2_1380x610.jpeg 2x" data-dominant-color="898691"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×849 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2023-10-10 10:34 UTC)

<p>It sounds like the “image position patient” and “image orientation tags” are not set correctly. You can have a look at these values by right-clicking in the DICOM browser and choose to view metadata. If you are not sure why the values are incorrect then you can share the data set and we’ll have a look.</p>

---
