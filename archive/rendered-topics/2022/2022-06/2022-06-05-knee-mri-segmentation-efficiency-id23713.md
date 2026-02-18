# Knee MRI Segmentation: Efficiency

**Topic ID**: 23713
**Date**: 2022-06-05
**URL**: https://discourse.slicer.org/t/knee-mri-segmentation-efficiency/23713

---

## Post #1 by @Abdulla_Al_Shibli (2022-06-05 14:41 UTC)

<p>Hi,</p>
<p>I am currently segmenting the bones (Femur, Tibia, Patella, etc.), ligaments, and tendons of a knee MRI. Pasted is a screenshot of what it looks like. I’m currently just painting and using the fill between slices function. However, as a new user, I am sure there are more efficient/accurate methods of getting this done. Anyone have any ideas?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bff476b4e80961a5b7a36447f9fb70d9873f32ac.jpeg" data-download-href="/uploads/short-url/ro6Xodu9as7uq5lUxFwklLKtc8Q.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff476b4e80961a5b7a36447f9fb70d9873f32ac_2_690x420.jpeg" alt="image" data-base62-sha1="ro6Xodu9as7uq5lUxFwklLKtc8Q" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff476b4e80961a5b7a36447f9fb70d9873f32ac_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff476b4e80961a5b7a36447f9fb70d9873f32ac_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff476b4e80961a5b7a36447f9fb70d9873f32ac_2_1380x840.jpeg 2x" data-dominant-color="3D3D49"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1169 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>On a sidenote, the fill between slices function sometimes includes some parts of an intensity different than the body part I am trying to segment. How can I cut these parts off multiple slices at once?</p>
<p>Any response is appreciated, thanks.</p>

---

## Post #2 by @pieper (2022-06-05 14:44 UTC)

<p>GrowFromSeeds should work well on that task.</p>
<p>For the fill, you could explore using a threshold, but relying on the signal intensity is probably not going to work well.</p>

---
