---
topic_id: 18616
title: "Loss Of Contours After Applying Rotation"
date: 2021-07-10
url: https://discourse.slicer.org/t/18616
---

# Loss of contours after Applying Rotation

**Topic ID**: 18616
**Date**: 2021-07-10
**URL**: https://discourse.slicer.org/t/loss-of-contours-after-applying-rotation/18616

---

## Post #1 by @MichaelCHL (2021-07-10 13:53 UTC)

<p>Hi all, I’ve applied transformation (rotation about the red target in my phantom) to both the CT scans and the contours (RT strucutures), hardened it and export it to DICOM</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/578afd672a6667c115bb307dbfb6bad9b7a0cdb6.png" data-download-href="/uploads/short-url/curk6GLy1Ut1L0fcxRTHLvAvFyK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/578afd672a6667c115bb307dbfb6bad9b7a0cdb6_2_690x410.png" alt="image" data-base62-sha1="curk6GLy1Ut1L0fcxRTHLvAvFyK" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/578afd672a6667c115bb307dbfb6bad9b7a0cdb6_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/578afd672a6667c115bb307dbfb6bad9b7a0cdb6_2_1035x615.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/578afd672a6667c115bb307dbfb6bad9b7a0cdb6_2_1380x820.png 2x" data-dominant-color="808A87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1437×855 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After the rotation, some of the contours are missing, but the CT scans are not affected.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/432d288a4e5a0ec45c2ec82d6d9fda39219137e7.png" data-download-href="/uploads/short-url/9AgJZIfk5rxIczzOxR5HvnVQyBp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/432d288a4e5a0ec45c2ec82d6d9fda39219137e7_2_690x413.png" alt="image" data-base62-sha1="9AgJZIfk5rxIczzOxR5HvnVQyBp" width="690" height="413" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/432d288a4e5a0ec45c2ec82d6d9fda39219137e7_2_690x413.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/432d288a4e5a0ec45c2ec82d6d9fda39219137e7_2_1035x619.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/432d288a4e5a0ec45c2ec82d6d9fda39219137e7_2_1380x826.png 2x" data-dominant-color="808A87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1439×862 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anybody have clues about what the problem is?</p>
<p>Many thanks!<br>
Michael</p>

---

## Post #2 by @lassoan (2021-07-12 04:20 UTC)

<p>Can you share the scene that is saved as .mrb file, before you hardened the transform? Use an anonymized data set or - even better - a publicly available sample data set.</p>

---

## Post #3 by @MichaelCHL (2021-07-12 15:32 UTC)

<p>Hi Andras, thanks for the reply.</p>
<p>I am now using Eclipse to register the contours to the rotated CT scans so this problem has been solved.</p>

---
