---
topic_id: 42009
title: "How To Save The Image After Add Dicom Attribute"
date: 2025-03-07
url: https://discourse.slicer.org/t/42009
---

# How to save the image after add DICOM attribute

**Topic ID**: 42009
**Date**: 2025-03-07
**URL**: https://discourse.slicer.org/t/how-to-save-the-image-after-add-dicom-attribute/42009

---

## Post #1 by @akmal871026 (2025-03-07 08:01 UTC)

<p>Dear all,</p>
<p>I was add some DICOM attribute in my image as picture attached.</p>
<p>Do you know how to save it in image.</p>
<p>Because when I try export image, then I open again, all the DICOM attribute was lost.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0579b6ce773ce4a22f99d5a5059ecd1fdbd2bbfd.png" data-download-href="/uploads/short-url/Mr9PAKSoIKA3LxX0BBuJZTFT5z.png?dl=1" title="Screenshot 2025-03-07 155557" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0579b6ce773ce4a22f99d5a5059ecd1fdbd2bbfd_2_288x500.png" alt="Screenshot 2025-03-07 155557" data-base62-sha1="Mr9PAKSoIKA3LxX0BBuJZTFT5z" width="288" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0579b6ce773ce4a22f99d5a5059ecd1fdbd2bbfd_2_288x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0579b6ce773ce4a22f99d5a5059ecd1fdbd2bbfd_2_432x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0579b6ce773ce4a22f99d5a5059ecd1fdbd2bbfd_2_576x1000.png 2x" data-dominant-color="E1EAF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-07 155557</span><span class="informations">585×1015 45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2025-03-07 15:45 UTC)

<p>The attributes shown in the data module are save/restored in the mrml scene (Slicer’s document format).  To modify the dicom you can see this documentation:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database</a></p>

---
