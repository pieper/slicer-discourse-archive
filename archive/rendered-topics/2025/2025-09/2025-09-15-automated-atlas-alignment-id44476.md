# Automated Atlas Alignment

**Topic ID**: 44476
**Date**: 2025-09-15
**URL**: https://discourse.slicer.org/t/automated-atlas-alignment/44476

---

## Post #1 by @diseaseprogression (2025-09-15 05:05 UTC)

<p>Hi everyone, I am trying to use the OpenAnatomy Atlas extension on Slicer with various MRI scans but am struggling with aligning the atlas with the scans. For some scans, it is automatically aligned, but for others they need to be manually aligned with the transformations which is labor intensive and slightly inaccurate. Is there anyway to automate the alignment of the atlas with the scans? I attached a picture of an unaligned atlas and scan we are trying to align for reference.</p>
<p>Additionally, if there is no way to automate the alignment would there be a way to verify or complete the final part of alignment after manual transformations?</p>
<p>Thank you in advance for your help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/531a549f7b921f9ad38b1d2b70fe31c21bd9f71a.jpeg" data-download-href="/uploads/short-url/bRa2FkbazcSsBlGwTbNDPYJr9Oy.jpeg?dl=1" title="Screenshot 2025-08-24 at 1.26.55 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531a549f7b921f9ad38b1d2b70fe31c21bd9f71a_2_690x316.jpeg" alt="Screenshot 2025-08-24 at 1.26.55 PM" data-base62-sha1="bRa2FkbazcSsBlGwTbNDPYJr9Oy" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531a549f7b921f9ad38b1d2b70fe31c21bd9f71a_2_690x316.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531a549f7b921f9ad38b1d2b70fe31c21bd9f71a_2_1035x474.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531a549f7b921f9ad38b1d2b70fe31c21bd9f71a_2_1380x632.jpeg 2x" data-dominant-color="9B999C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-08-24 at 1.26.55 PM</span><span class="informations">1920×880 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-09-15 05:06 UTC)

<p>Everything should be well aligned. Most likely it is an RAS/LPS coordinate system mismatch. If you describe where you got the files from and how you loaded them into Slicer then we can advise how to avoid the issue.</p>

---
