# Displacement field and deformable registration: Unexpected folded “mirror” images outside the fixed volume

**Topic ID**: 5081
**Date**: 2018-12-14
**URL**: https://discourse.slicer.org/t/displacement-field-and-deformable-registration-unexpected-folded-mirror-images-outside-the-fixed-volume/5081

---

## Post #1 by @stephan (2018-12-14 20:11 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.10.0<br>
Expected behavior: Displacement field deforms moving volume only within the limits of the displacement field (i.e. within the limits of the fixed image). Regions outside of the displacement field should not affect the registration.<br>
Actual behavior:</p>
<p>I have a problem with displacement fields (deformable registration) in Slicer: Using SlicerElastix, I register a (pig) cardiac CT [moving volume] to a (comparably small) <em>ex vivo</em> MRI of the explanted heart [fixed volume]. Due to post mortem tissue deformation, the deformation is rather large but Elastix handles this extremely well. The output from SlicerElastix is a displacement field, which I then apply to the moving volume. Registration results within the FOV of the fixed volume are nice. This workflow has worked without any problem in two cases in the past, but this time I noticed strange results:</p>
<p>When I look beyond the extent of the fixed volume, there is strange folding and mirroring happening. (See screenshot. Moving volume in blue, fixed volume in yellow, displacement field visualized in the 3d view)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59d63ba61162e92f7a7d341db2e0e4f4bfe02f4e.png" data-download-href="/uploads/short-url/cOJubSyIRGSywj96Zs1Ib3eYUW2.png?dl=1" title="screenshot1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59d63ba61162e92f7a7d341db2e0e4f4bfe02f4e_2_690x420.png" alt="screenshot1" data-base62-sha1="cOJubSyIRGSywj96Zs1Ib3eYUW2" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59d63ba61162e92f7a7d341db2e0e4f4bfe02f4e_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59d63ba61162e92f7a7d341db2e0e4f4bfe02f4e_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59d63ba61162e92f7a7d341db2e0e4f4bfe02f4e_2_1380x840.png 2x" data-dominant-color="454846"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot1</span><span class="informations">1920×1170 962 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This would not matter if this folding would not mess up the transformation of segmentations. I do have surface models (isodose volumes from SlicerRT) as well as a segmentation, both mapping to the moving volume CT and both located in a region which should actually be registered into the fixed volume. However, both structures become grossly deformed and do not display correctly due to the folding happening outside of the fixed volume.</p>
<p>To illustrate this effect, I have created an affine (non-deformable) registration which approximates the deformable one. This is how the isodose lines, the segmentation, and the moving volume (blue) look under this affine transform:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5deee9570d011a47fb90b42f32aa1fcc0f137321.jpeg" data-download-href="/uploads/short-url/doYgKPlTtOAmH4L8D4MybTvEcdX.jpeg?dl=1" title="screenshot2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5deee9570d011a47fb90b42f32aa1fcc0f137321_2_690x420.jpeg" alt="screenshot2" data-base62-sha1="doYgKPlTtOAmH4L8D4MybTvEcdX" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5deee9570d011a47fb90b42f32aa1fcc0f137321_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5deee9570d011a47fb90b42f32aa1fcc0f137321_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5deee9570d011a47fb90b42f32aa1fcc0f137321_2_1380x840.jpeg 2x" data-dominant-color="4B605E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot2</span><span class="informations">1920×1170 703 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, once I apply the displacement field instead of the affine transformation, the isodose volumes / isodose lines and the segmentation become wildly distorted and do not display at all in some views. Note how the green slice goes through the white segmentation as can be seen from the slice intersection in the other slice viewers. Nonetheless, no white segmentation is displayed in the green slice viewer. Note also how the white segmentation (in the yellow and red viewers) is duplicated / mirrored in regions outside the actual fixed volume, leading to an wildly stretched appearance in the 3d view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee527b1037d50be4e73a44bb42cd7060a1264e91.jpeg" data-download-href="/uploads/short-url/y0ilPq2AFCFuvjS3e2wHYDRApi1.jpeg?dl=1" title="screenshot3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee527b1037d50be4e73a44bb42cd7060a1264e91_2_690x420.jpeg" alt="screenshot3" data-base62-sha1="y0ilPq2AFCFuvjS3e2wHYDRApi1" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee527b1037d50be4e73a44bb42cd7060a1264e91_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee527b1037d50be4e73a44bb42cd7060a1264e91_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee527b1037d50be4e73a44bb42cd7060a1264e91_2_1380x840.jpeg 2x" data-dominant-color="3F5C5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot3</span><span class="informations">1920×1170 826 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I wondered if it has something to do with the size difference between the fixed and the moving volume and with the displacement field being undefined in certain places. I have already tried to either crop the moving volume to the size of the fixed volume or to overcrop the fixed volume so that it is the same size as the moving one. The result have been the same (folding, mirroring, chaos).</p>
<p>What am I missing?<br>
Any hints are greatly appreciated.</p>
<p>Thank you very much</p>
<p>Stephan</p>

---

## Post #2 by @lassoan (2018-12-14 20:22 UTC)

<aside class="quote no-group" data-username="stephan" data-post="1" data-topic="5081">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>Displacement field deforms moving volume only within the limits of the displacement field (i.e. within the limits of the fixed image). Regions outside of the displacement field should not affect the registration.</p>
</blockquote>
</aside>
<p>It is very important to estimate displacement field outside the limits of the fixed image, because transforming points and surfaces require inversion of the resampling transform (that is use for transforming images). If you don’t have a smooth boundary but displacement field would abruptly change from some large value to small value then the inverse computation would fail.</p>
<p>If you have very large displacements (especially rotations) then you may perform rigid registration first and harden the results (this does not cause any change to the image voxels, just changes position and orientation of the voxel grid). After this initial alignment, you should have no problem with performing deformable registration.</p>
<p>Note that it is very rare to have flips or large rotations between registered volumes and it may indicate problems in previous steps of your workflow. So, if you regularly encounter such cases then probably it is better to fix your imaging or pre-processing workflow.</p>

---

## Post #3 by @stephan (2018-12-14 21:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="5081">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you have very large displacements (especially rotations) then you may perform rigid registration first and harden the results (this does not cause any change to the image voxels, just changes position and orientation of the voxel grid). After this initial alignment, you should have no problem with performing deformable registration.</p>
</blockquote>
</aside>
<p>That was it. I realized that in the two previous cases (which worked well) I had hardened any linear transform on the moving volume before starting Elastix, while this time I simply used those linear transforms to initialize Elastix. This way, the large translation and rotation* ended up being a part of the displacement field this time.<br>
I did not know that displacement fields are so sensitive to large displacements, so thank you for pointing this out.<br>
And thank you for the very quick reply, as always.</p>
<p>Stephan</p>
<hr>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="5081">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that it is very rare to have flips or large rotations between registered volumes and it may indicate problems in previous steps of your workflow.</p>
</blockquote>
</aside>
<p>Because you mentioned this: The large amount of translation and rotation stem from the fact that the moving and fixed volume were acquired under very different circumstances, one being a CT of a living animal and the other being an MRI of the heart in a jar… So it is challenging to register them, indeed.</p>

---
