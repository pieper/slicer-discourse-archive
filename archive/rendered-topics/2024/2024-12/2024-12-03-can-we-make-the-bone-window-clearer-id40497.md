---
topic_id: 40497
title: "Can We Make The Bone Window Clearer"
date: 2024-12-03
url: https://discourse.slicer.org/t/40497
---

# Can we make the bone window clearer？

**Topic ID**: 40497
**Date**: 2024-12-03
**URL**: https://discourse.slicer.org/t/can-we-make-the-bone-window-clearer/40497

---

## Post #1 by @sunwei921119 (2024-12-03 15:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5006db869be3d0c3b3a3756e05bd1e417f6eb8eb.jpeg" data-download-href="/uploads/short-url/bpWTaqMgPutxgfQWNPBtvUH79RV.jpeg?dl=1" title="mmexport1733239764421" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5006db869be3d0c3b3a3756e05bd1e417f6eb8eb_2_689x489.jpeg" alt="mmexport1733239764421" data-base62-sha1="bpWTaqMgPutxgfQWNPBtvUH79RV" width="689" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5006db869be3d0c3b3a3756e05bd1e417f6eb8eb_2_689x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5006db869be3d0c3b3a3756e05bd1e417f6eb8eb_2_1033x733.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5006db869be3d0c3b3a3756e05bd1e417f6eb8eb.jpeg 2x" data-dominant-color="3D3D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mmexport1733239764421</span><span class="informations">1283×910 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94b3f4ae17f9dc2aa3399d3815d17fd2f6a51fa4.jpeg" data-download-href="/uploads/short-url/ldudAg4aRbovLP66vuvRMkljYJm.jpeg?dl=1" title="mmexport1733239760590" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94b3f4ae17f9dc2aa3399d3815d17fd2f6a51fa4_2_689x489.jpeg" alt="mmexport1733239760590" data-base62-sha1="ldudAg4aRbovLP66vuvRMkljYJm" width="689" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94b3f4ae17f9dc2aa3399d3815d17fd2f6a51fa4_2_689x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94b3f4ae17f9dc2aa3399d3815d17fd2f6a51fa4_2_1033x733.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94b3f4ae17f9dc2aa3399d3815d17fd2f6a51fa4.jpeg 2x" data-dominant-color="232323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mmexport1733239760590</span><span class="informations">1283×910 61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Radiology has a thin-layer bone algorithm that can make bones clearer based on the original CT scan. Excuse me, does 3D Slicer have this kind of functional plugin?</p>

---

## Post #2 by @cpinter (2024-12-03 15:34 UTC)

<p>You can manually adjust the Window/Level settings in the Volumes module to any values you want.</p>

---

## Post #3 by @sunwei921119 (2024-12-03 15:39 UTC)

<p>I know that. What I need is to handle the bone window, increase contrast and sharpening values to make it clearer.</p>

---

## Post #4 by @cpinter (2024-12-03 15:41 UTC)

<p>Then it seems I don’t understand the question sorry. Maybe someone else will. Or if you could share more details about what you want exactly, that could help. Thanks</p>

---

## Post #5 by @mohammed_alshakhas (2024-12-03 16:56 UTC)

<p>there are sharpening filter i use in other software , i wish we have something similar in 3d slicer</p>

---

## Post #6 by @pieper (2024-12-03 17:27 UTC)

<p>There are plenty of image sharpening filters in Slicer (try Filters-&gt;Denoising or the options in SimpleFilters) but probably the bone reconstruction filters used during the CT backprojection would have the most impact since they work at the level of the raw data.</p>

---

## Post #7 by @lassoan (2024-12-03 18:15 UTC)

<p>General-purpose sharpening filters have limited capabilities. Is there a specific region or bone you want are interested in? For example, in the past we investigated special processing methods to improve visibility of orbital bones.</p>

---

## Post #8 by @mohammed_alshakhas (2024-12-04 05:13 UTC)

<p>I’m heavily focused on TMJ , the outline the cortical outline and decorticated are is extremely important to me . I found using ct bone window to be game changer but it’s not very sharp .</p>
<p>The default and automatic windows are clear but miss important details . So I was thinking of looking for sharpening filters on bone window</p>

---

## Post #9 by @sunwei921119 (2024-12-05 15:26 UTC)

<p>Thank you for your reply. I am interested in bone sharpening and hope to develop better plugins</p>

---

## Post #10 by @sunwei921119 (2024-12-05 15:27 UTC)

<p>Thank you very much. I’ll give it a try</p>

---

## Post #11 by @mohammed_alshakhas (2024-12-07 14:57 UTC)

<p>this view would be great if  sharpening is applied</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/726b2bd9c6cde452a15c31e5ef6852b23648c2f2.jpeg" data-download-href="/uploads/short-url/gkc2NecQUWDCPYjco5K4tsHJarU.jpeg?dl=1" title="Screenshot 2024-12-07 at 17.53.47" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/726b2bd9c6cde452a15c31e5ef6852b23648c2f2_2_690x304.jpeg" alt="Screenshot 2024-12-07 at 17.53.47" data-base62-sha1="gkc2NecQUWDCPYjco5K4tsHJarU" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/726b2bd9c6cde452a15c31e5ef6852b23648c2f2_2_690x304.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/726b2bd9c6cde452a15c31e5ef6852b23648c2f2_2_1035x456.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/726b2bd9c6cde452a15c31e5ef6852b23648c2f2_2_1380x608.jpeg 2x" data-dominant-color="41403E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-12-07 at 17.53.47</span><span class="informations">1920×848 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
