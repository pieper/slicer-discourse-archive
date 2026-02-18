# Registration of MRI Scans

**Topic ID**: 12536
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/registration-of-mri-scans/12536

---

## Post #1 by @bernland (2020-07-14 15:59 UTC)

<p>As you can see on the below screenshots, there is an offset between two abdominal MRIs (anywhere between 0 and 6 mm). What would be the best way to register the volumes in Silcer?</p>
<p>Any help is greatly appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/890e62430029bf87ee438dd511cb93acab5950ca.png" data-download-href="/uploads/short-url/jyseiIrwewC6G9gpEXmk7uAUoNc.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/890e62430029bf87ee438dd511cb93acab5950ca_2_690x373.png" alt="1" data-base62-sha1="jyseiIrwewC6G9gpEXmk7uAUoNc" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/890e62430029bf87ee438dd511cb93acab5950ca_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/890e62430029bf87ee438dd511cb93acab5950ca_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/890e62430029bf87ee438dd511cb93acab5950ca_2_1380x746.png 2x" data-dominant-color="686867"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1040 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-07-14 19:26 UTC)

<p>You can use Landmark registration module to correct slight misalignments between volumes.</p>

---
