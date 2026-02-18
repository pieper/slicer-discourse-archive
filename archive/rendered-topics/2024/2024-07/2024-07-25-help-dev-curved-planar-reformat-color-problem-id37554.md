# Help dev)"curved planar reformat" color problem

**Topic ID**: 37554
**Date**: 2024-07-25
**URL**: https://discourse.slicer.org/t/help-dev-curved-planar-reformat-color-problem/37554

---

## Post #1 by @Seokjun_Hwang (2024-07-25 08:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a032856b290199edb0774082c2c27588375025a.png" data-download-href="/uploads/short-url/3I7b7ej7FM7lHEnkRiCbOopLIYa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a032856b290199edb0774082c2c27588375025a_2_680x500.png" alt="image" data-base62-sha1="3I7b7ej7FM7lHEnkRiCbOopLIYa" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a032856b290199edb0774082c2c27588375025a_2_680x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a032856b290199edb0774082c2c27588375025a_2_1020x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a032856b290199edb0774082c2c27588375025a.png 2x" data-dominant-color="8B8A88"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1203×884 52.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2797d01ea272bbbc6dd58b1a14f1061a4039a7d2.png" alt="image" data-base62-sha1="5EfSvnl8mL5vbGD6fJmWqrhXRDQ" width="568" height="132"></p>
<p>Hellow…!</p>
<p>I am seeking assistance with an issue encountered while using the Curved Planar Reformat module with sandbox extensions.</p>
<p><strong>Problem:</strong> I used the straightening function to straighten the aorta into a straight line. However, the overall color of the volume and the cross-section are not filled uniformly with one color (white); instead, they alternate with black. This is causing issues with mask preprocessing when transferring and saving the data in Python.</p>
<p><strong>Implementation Steps:</strong></p>
<ol>
<li>First, I loaded the aorta 3D data in nii.gz format as two node types: volume and segmentation.</li>
<li>Using the curve line, I applied the straightening mode and created a new straightened volume.</li>
<li>Upon checking, I noticed the color issue as described.</li>
</ol>
<p>I cannot use any edits. Additionally, there is an issue with displaying it in the 3D viewer.</p>
<p>How can I change the color to white? Or how can I resolve this issue?</p>
<p>Thank you.</p>

---
