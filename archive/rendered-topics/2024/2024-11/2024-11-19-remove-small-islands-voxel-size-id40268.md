# Remove small islands voxel size

**Topic ID**: 40268
**Date**: 2024-11-19
**URL**: https://discourse.slicer.org/t/remove-small-islands-voxel-size/40268

---

## Post #1 by @FraP (2024-11-19 16:30 UTC)

<p>I am using the “Remove Small Islands” function with a voxel size of 10 after segmenting with the threshold function.<br>
The information of the volume I’m working with is the following:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e32f7f921880c37fb3dffa5bb3b3a260030cd804.png" data-download-href="/uploads/short-url/wpM9krvm6UDwnSYCCdmganpbvjm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e32f7f921880c37fb3dffa5bb3b3a260030cd804.png" alt="image" data-base62-sha1="wpM9krvm6UDwnSYCCdmganpbvjm" width="482" height="191"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">482×191 4.01 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you confirm if I understand correctly that the voxel size is 0.0004546 mm³?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @muratmaga (2024-11-19 17:30 UTC)

<p>No, that is not correct. Based on the information above, your voxel size is anisotropic. it is 0.00045x0.00045x0.005 (in other words about 0.45 micron in XY and 5 micron in Z axes).</p>

---

## Post #3 by @FraP (2024-11-20 08:05 UTC)

<p>Thank you for the answer.</p>
<p>How this applies to the voxel size for “Remove Small Islands” from a segment?<br>
Does a voxel size of 10 correspond to dimensions of 4.5 × 4.5 × 50 microns?</p>
<p>When I apply it to my segments, this doesn’t seem to be the case. Graphically, it appears to remove only very small islands, around 4.5 microns³.<br>
Do segments always have isotropic voxels?</p>

---

## Post #4 by @cpinter (2024-11-20 09:25 UTC)

<aside class="quote no-group" data-username="FraP" data-post="3" data-topic="40268">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/e68b1a/48.png" class="avatar"> FraP:</div>
<blockquote>
<p>Does a voxel size of 10 correspond to dimensions of 4.5 × 4.5 × 50 microns?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="FraP" data-post="3" data-topic="40268">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/e68b1a/48.png" class="avatar"> FraP:</div>
<blockquote>
<p>When I apply it to my segments, this doesn’t seem to be the case. Graphically, it appears to remove only very small islands, around 4.5 microns³.</p>
</blockquote>
</aside>
<p>This is very hard to confirm visually. If you have any doubts, paint a blob of 10 voxels then one of 9 and see if it’s correct. By the way this part of the code has not changed for about 7 years. Let us know if you do find an issue. (I just tried it and it works as expected)</p>
<aside class="quote no-group" data-username="FraP" data-post="3" data-topic="40268">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/e68b1a/48.png" class="avatar"> FraP:</div>
<blockquote>
<p>Do segments always have isotropic voxels?</p>
</blockquote>
</aside>
<p>No. A segmentation assumes the geometry of its source volume unless you change it manually.</p>

---
