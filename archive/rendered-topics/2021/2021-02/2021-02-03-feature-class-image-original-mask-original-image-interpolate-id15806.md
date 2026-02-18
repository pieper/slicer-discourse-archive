# Feature class (Image original, Mask original, Image interpolated, Mask interpolated)

**Topic ID**: 15806
**Date**: 2021-02-03
**URL**: https://discourse.slicer.org/t/feature-class-image-original-mask-original-image-interpolated-mask-interpolated/15806

---

## Post #1 by @Yasuhiro_TAKEDA (2021-02-03 08:34 UTC)

<p>Hi</p>
<p>I have a question about feature class in diagnostic, such as Image original, Mask original, Image interpolated, and Mask interpolated.<br>
What do they mean exactly?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bbcad50fbcf3ee0d499c28f1845b81c75391bff.png" data-download-href="/uploads/short-url/8wspnJIPRKwwTre2wYJBUX4Rvwb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bbcad50fbcf3ee0d499c28f1845b81c75391bff_2_562x500.png" alt="image" data-base62-sha1="8wspnJIPRKwwTre2wYJBUX4Rvwb" width="562" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bbcad50fbcf3ee0d499c28f1845b81c75391bff_2_562x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bbcad50fbcf3ee0d499c28f1845b81c75391bff_2_843x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bbcad50fbcf3ee0d499c28f1845b81c75391bff_2_1124x1000.png 2x" data-dominant-color="CCE0EC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2134×1896 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As in the figure above, the values of spacing, size, max, and min in Image and Mask original seem to be reasonable. However, why are they almost the same between Image and Mask interpolated?<br>
I thought spacing in Image-interpolated (1.0, 1.0, 1.0) is OK, but size (40,41,37) doesn’t make sense. Isn’t it supposed to be larger, like (170,170,60)??</p>
<p>My parameter settings are as follows:<br>
imageType:</p>
<p>Original: {}</p>
<p>featureClass:<br>
shape:<br>
firstorder:<br>
glcm:<br>
glrlm:<br>
glszm:<br>
gldm:<br>
ngtdm:</p>
<p>setting:<br>
normalize: true<br>
removeOutliers: 3<br>
interpolator: ‘sitkLinear’<br>
resampledPixelSpacing: [1, 1, 1]<br>
binCount: 64<br>
label: 1</p>
<p>Thank you,</p>
<p>TAKEDA</p>

---

## Post #2 by @JoostJM (2021-03-09 12:28 UTC)

<p>These are exactly what they claim to be, i.e. diagnostic features. They provide insight into what happens to the image and the ROI during pre-processing in PyRadiomics.<br>
These can help you understand what happens when the extracted feature values don’t make sense (e.g. extreme values when, due to interpolation, your ROI only consists of very few voxels, even when your original mask contained many).</p>

---

## Post #3 by @JoostJM (2021-03-09 12:30 UTC)

<p>Also be ware, that during interpolation the image is also (partially) cropped onto the boundingbox of the ROI, which is computationally much more efficient. It would be illogical to resample an entire CT with 512x512x100s of slices when the ROI is just a small nodule in the lung covering maybe 20x20x20 voxels.</p>

---

## Post #4 by @Yasuhiro_TAKEDA (2021-03-30 02:56 UTC)

<p>Thank you for your reply!</p>

---
