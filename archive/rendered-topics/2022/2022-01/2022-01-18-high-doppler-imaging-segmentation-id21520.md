---
topic_id: 21520
title: "High Doppler Imaging Segmentation"
date: 2022-01-18
url: https://discourse.slicer.org/t/21520
---

# High Doppler imaging segmentation 

**Topic ID**: 21520
**Date**: 2022-01-18
**URL**: https://discourse.slicer.org/t/high-doppler-imaging-segmentation/21520

---

## Post #1 by @Effand (2022-01-18 18:33 UTC)

<p>Hey All, I would like to kindly ask you all for some support for vessel segmentation on ultrasound images. I am a Medical researcher in radiology, currently working on Micro- Doppler ultrasound images which is a novel modality. I have no experience of working with 3D Slicer and my technical expertise in imaging modalities is quite limited, thus could you help with finding the right tools and where to start from since it is vast major. you can find below an image from my data which is 2D image with only one plane to have a clear idea about it.</p>
<p>Thank you all in advance and hope I will get some useful info back from you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e6b151ae1670437aa1a720471bd8afd917f9460.jpeg" data-download-href="/uploads/short-url/dtgiVyjj1tDWKQ4s79QB0dSuRWM.jpeg?dl=1" title="thumbnail_IMG_1140" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e6b151ae1670437aa1a720471bd8afd917f9460_2_666x500.jpeg" alt="thumbnail_IMG_1140" data-base62-sha1="dtgiVyjj1tDWKQ4s79QB0dSuRWM" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e6b151ae1670437aa1a720471bd8afd917f9460_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e6b151ae1670437aa1a720471bd8afd917f9460_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e6b151ae1670437aa1a720471bd8afd917f9460.jpeg 2x" data-dominant-color="85695D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thumbnail_IMG_1140</span><span class="informations">1280×960 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/228fbeb0c3bb63d512d37d70693bef0b890e8dc1.jpeg" data-download-href="/uploads/short-url/4VKcLPhzXWrOvWkfi84AGsD1iBr.jpeg?dl=1" title="IMG_1140" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/228fbeb0c3bb63d512d37d70693bef0b890e8dc1_2_666x500.jpeg" alt="IMG_1140" data-base62-sha1="4VKcLPhzXWrOvWkfi84AGsD1iBr" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/228fbeb0c3bb63d512d37d70693bef0b890e8dc1_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/228fbeb0c3bb63d512d37d70693bef0b890e8dc1_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/228fbeb0c3bb63d512d37d70693bef0b890e8dc1_2_1332x1000.jpeg 2x" data-dominant-color="896658"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_1140</span><span class="informations">1920×1440 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-01-19 03:05 UTC)

<p>Recent Slicer Preview Releases may load the acquisition as a volume sequence, but for now having all the frames in a single volume should work, too.</p>
<p>The images seem to be just a single scalar value mapped with a red-to-yellow colormap, so before processing it would be better to convert back to grayscale (for example, using “Vector to Scalar volume” module).</p>
<p>After this, probably you would want to segment the vessels manually using the Segment Editor. If you want more automated segmentation then you might experiment with various effects in the Segment Editor, but there are only few tools that are applicable to 2D image sequences. Instead, you may segment a few dozens of sequences and use them to train a neural network that will be able to segment vessels fully automatically.</p>

---
