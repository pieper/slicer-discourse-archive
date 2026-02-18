# Fix broken volume - face is behind the back of the head

**Topic ID**: 30069
**Date**: 2023-06-16
**URL**: https://discourse.slicer.org/t/fix-broken-volume-face-is-behind-the-back-of-the-head/30069

---

## Post #1 by @newbie1 (2023-06-16 13:02 UTC)

<p>Hello everyone, im new to 3D Slicer and trying to do some segmentations and measurements but i keep having this problem where the volume its unorganized (the head in trying to measure is split in half and the face is behind the hindhead, leaving on the outside the inside of the head).</p>
<p>Any support on how to solve this would be very aprecciated.</p>
<p>(please excuse my english)</p>

---

## Post #2 by @lassoan (2023-06-16 13:20 UTC)

<p>I’m not sure if you refer to the MRI wrap-around artifact (a body part appears on the other side of the image), which occurs when the field of view is set to smaller than the imaged body part. See for example in the MRHead sample data set:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e807c6005eae682e130cdabce6bf38300473e3e4.jpeg" alt="image" data-base62-sha1="x6DqvXzlM2UX4cCQPHONLpDsiNe" width="593" height="500"></p>
<p>See some more information here: <a href="https://radiopaedia.org/articles/aliasing-on-mri" class="inline-onebox">Aliasing on MRI | Radiology Reference Article | Radiopaedia.org</a></p>
<p>The best would be to acquire the images properly (the MR imaging technician paying more attention to avoid this artifact).</p>
<p>If that’s not feasible then you can fix it retrospectively:</p>
<ul>
<li>use Segment Editor to segment the part of the face that appears in incorrect location</li>
<li>export inside and outside the masked region to two different volumes</li>
<li>use <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">Stitch Volumes module</a> (provided by Sandbox extension) to stitch the two volumes together</li>
</ul>

---

## Post #3 by @newbie1 (2023-06-16 15:46 UTC)

<p>Thanks for your help.</p>
<p>Unfortunately i dont think the fix inside the software is going to work in this case as it is so wrap around that the face has flatenned in contact with the nape.</p>
<p>Thanks again for your help.</p>

---

## Post #4 by @pieper (2023-06-16 16:26 UTC)

<p>It sounds like an issue with the data files being corrupted or. not correctly read.  Post a screenshot and we can probably make suggestions.</p>

---

## Post #5 by @newbie1 (2023-06-16 19:22 UTC)

<p>hello, it looks like this</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76562ab54d6408cd5cca1a6631945ece352e86e1.jpeg" data-download-href="/uploads/short-url/gSQX5GEwDhaVW8W4u2IjeufCbE5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76562ab54d6408cd5cca1a6631945ece352e86e1_2_690x475.jpeg" alt="image" data-base62-sha1="gSQX5GEwDhaVW8W4u2IjeufCbE5" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76562ab54d6408cd5cca1a6631945ece352e86e1_2_690x475.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76562ab54d6408cd5cca1a6631945ece352e86e1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76562ab54d6408cd5cca1a6631945ece352e86e1.jpeg 2x" data-dominant-color="222222"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">932×642 53.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/999d760d799ffb75c2045cb9e320bc63adef8d5e.jpeg" data-download-href="/uploads/short-url/lUWpxqx2xQyK1L2Q2H6AZusmFBQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/999d760d799ffb75c2045cb9e320bc63adef8d5e_2_503x500.jpeg" alt="image" data-base62-sha1="lUWpxqx2xQyK1L2Q2H6AZusmFBQ" width="503" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/999d760d799ffb75c2045cb9e320bc63adef8d5e_2_503x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/999d760d799ffb75c2045cb9e320bc63adef8d5e_2_754x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/999d760d799ffb75c2045cb9e320bc63adef8d5e.jpeg 2x" data-dominant-color="938EA7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">832×826 73.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>or like this</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1700a772894daf82923208027427db9a51337902.png" data-download-href="/uploads/short-url/3hunL2qnWdApPeUGJdpceEPkX4e.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1700a772894daf82923208027427db9a51337902_2_690x316.png" alt="image" data-base62-sha1="3hunL2qnWdApPeUGJdpceEPkX4e" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1700a772894daf82923208027427db9a51337902_2_690x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1700a772894daf82923208027427db9a51337902.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1700a772894daf82923208027427db9a51337902.png 2x" data-dominant-color="202020"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">984×451 60 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>any ideas on how to fix it( if possible) are very much aprecciated</p>

---

## Post #6 by @lassoan (2023-06-16 19:42 UTC)

<p>Have you loaded the image using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#read-dicom-files-into-the-scene">DICOM module</a>?</p>

---
