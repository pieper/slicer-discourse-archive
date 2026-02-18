# Problem with importing files

**Topic ID**: 16103
**Date**: 2021-02-20
**URL**: https://discourse.slicer.org/t/problem-with-importing-files/16103

---

## Post #1 by @Shrb_Show (2021-02-20 03:22 UTC)

<p>Hi,<br>
I am a beginner and I am trying to do the segmentation of femur. While using the software I am facing couple of problems.</p>
<ol>
<li>
<p>Whenever I try to import a new data I am getting distorted slices<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3656845903875b2e1043ba7196c534c9caa5d2d.jpeg" data-download-href="/uploads/short-url/njt5H3sVRv3m5metXDOU47GQV0F.jpeg?dl=1" title="Screenshot 2021-02-20 105744" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3656845903875b2e1043ba7196c534c9caa5d2d_2_690x438.jpeg" alt="Screenshot 2021-02-20 105744" data-base62-sha1="njt5H3sVRv3m5metXDOU47GQV0F" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3656845903875b2e1043ba7196c534c9caa5d2d_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3656845903875b2e1043ba7196c534c9caa5d2d_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3656845903875b2e1043ba7196c534c9caa5d2d_2_1380x876.jpeg 2x" data-dominant-color="42434E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-02-20 105744</span><span class="informations">1427×907 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Whenever I try to import a saved file, all the slices are either missing or distorted.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3b788b3f59207d1d8696a4b77ba486b32f1c137.png" data-download-href="/uploads/short-url/nmj2Wq6fI2rTaeuNyqGLSRZuOhh.png?dl=1" title="Screenshot 2021-02-20 110850" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3b788b3f59207d1d8696a4b77ba486b32f1c137_2_690x436.png" alt="Screenshot 2021-02-20 110850" data-base62-sha1="nmj2Wq6fI2rTaeuNyqGLSRZuOhh" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3b788b3f59207d1d8696a4b77ba486b32f1c137_2_690x436.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3b788b3f59207d1d8696a4b77ba486b32f1c137_2_1035x654.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3b788b3f59207d1d8696a4b77ba486b32f1c137_2_1380x872.png 2x" data-dominant-color="3F3C44"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-02-20 110850</span><span class="informations">1417×896 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>Please help.</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2021-02-20 04:15 UTC)

<p>Please try loading the data with DICOM module in latest Slicer Preview Release and if you still have issues then follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#something-is-displayed-but-it-is-not-what-i-expected">these instructions</a>.</p>

---

## Post #3 by @Shrb_Show (2021-05-12 01:12 UTC)

<p>Tried that didnt work.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2021-05-12 01:16 UTC)

<p>No problem, if you follow the instructions above then it is guaranteed that your data will load correctly (follow the instructions all the way through - including sending us an anonymized data set if previous steps do not lead to success).</p>

---
