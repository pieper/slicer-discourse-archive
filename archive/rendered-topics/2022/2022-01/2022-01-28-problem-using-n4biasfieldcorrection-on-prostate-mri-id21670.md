# Problem using N4BiasFieldCorrection on prostate MRI

**Topic ID**: 21670
**Date**: 2022-01-28
**URL**: https://discourse.slicer.org/t/problem-using-n4biasfieldcorrection-on-prostate-mri/21670

---

## Post #1 by @skssh (2022-01-28 02:55 UTC)

<p>I’m using N4BiasFieldCorrectionImageFilter from SimpleITK to adjust inhomogeneity between MR images. While the algorithm performs well on most MR images, it doesn’t perform well on some outliers. Here is an example of the outliers:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e39461a1f059e9907100a3f3d8233865655921c.png" alt="LH_before" data-base62-sha1="4jn21Rb43rQLqVEPqwPxkzZZITi" width="174" height="155"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dff9de11a490843d4e59c735c5fc61ad31bfcc64.png" alt="before2" data-base62-sha1="vXnOuOkJjcqlc7UcFRXMsDBSfmk" width="174" height="155"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df725cde44a8c3d10b7aeab883e053abc241aabc.png" alt="before3" data-base62-sha1="vSHuOuMPkSu51cN0yza5AriC1Yw" width="174" height="155"></p>
<p>The first row are slices from an MRI before N4 correction. The second are after N4 correction.</p>
<p>And here is another example of normal prostate MRI:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/340a54c4e4477a6639eb64c7435d7cc05ea15e0b.png" alt="normal_before" data-base62-sha1="7qmXH1APv84pCmHqQJOSR7ig93J" width="174" height="155"><br>
The first image is one slice from an MRI before N4 correction. The second is after N4 correction.</p>
<p>The code I use is:</p>
<pre><code>img = sitk.ReadImage(filename)
ori_type = img.GetPixelIDValue()
corrector = sitk.N4BiasFieldCorrectionImageFilter()
mask_image = sitk.OtsuThreshold(img, 0, 1, 200)
new_img = sitk.Cast(img, sitk.sitkFloat32)
new_img = corrector.Execute(new_img, mask_image)
new_img = sitk.Cast(new_img, ori_type)
</code></pre>
<p>How should I deal with the outliers?</p>

---

## Post #2 by @pieper (2022-01-28 13:40 UTC)

<p>Probably better to post this question to the ITK forum.</p>

---

## Post #3 by @lassoan (2022-01-28 23:41 UTC)

<p>About prostate MRI bias field correction using N4ITK (from my PhD thesis from a decade ago) - maybe it helps:</p>
<blockquote>
<p>The N4ITK method has just a few user-defined parameters. The bias full width at half maximum characterizes the Gaussian that models the bias field. The noise parameter specifies the Wiener filter that is used for the field estimation. Number of fitting levels, convergence threshold, and maximum number of iterations define the numerical optimization parameters. The shrink factor defines the degree of sub-sampling that is performed on the input image before the bias estimation to decrease the computation time.</p>
</blockquote>
<blockquote>
<p>The N4ITK method was used for image intensity inhomogeneity correction of the input images. The most important parameter of the method is the bias full width at half maximum (BWHM), which defines the Gaussian that estimates the bias field. Testing on clinical images showed that low values (&lt;0.3) tend to keep some inhomogeneity in the image, while too high values (&gt;0.7) tend to remove valuable signal contents from the image, therefore 0.5, the center of the correct operation range was used for all the images</p>
</blockquote>

---
