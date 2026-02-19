---
topic_id: 34335
title: "Issue With Volume Cropping"
date: 2024-02-14
url: https://discourse.slicer.org/t/34335
---

# Issue with Volume Cropping

**Topic ID**: 34335
**Date**: 2024-02-14
**URL**: https://discourse.slicer.org/t/issue-with-volume-cropping/34335

---

## Post #1 by @joseph00 (2024-02-14 23:07 UTC)

<p>Hello everyone,</p>
<p>I am encountering an issue with the volume cropping functionality in 3D Slicer and would greatly appreciate any assistance or guidance you could provide.</p>
<p>When attempting to perform a volume crop Volume module, I am encountering errors that prevent the operation from completing successfully.<br>
I followed these steps for volume cropping:</p>
<ol>
<li>Select image</li>
<li>Create a ROI for cropping</li>
<li>Create a new volume as output.<br>
But, when I click “apply”, the selected image is not cropped.</li>
</ol>
<p>Specifically, I am receiving these errors on Error Log:</p>
<ol>
<li></li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db344df505bc646072a724c1a06f919001ade7f9.png" data-download-href="/uploads/short-url/vhaCVP1isSWVWSpmbcKgdT7ojzz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db344df505bc646072a724c1a06f919001ade7f9_2_244x500.png" alt="image" data-base62-sha1="vhaCVP1isSWVWSpmbcKgdT7ojzz" width="244" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db344df505bc646072a724c1a06f919001ade7f9_2_244x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db344df505bc646072a724c1a06f919001ade7f9_2_366x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db344df505bc646072a724c1a06f919001ade7f9.png 2x" data-dominant-color="EEF0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">449×919 64.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>“Could not create an instance of “InverseDisplacementFieldTransform_double_3_3”<br>
The usual cause of this error is not registering the transform with TransformFactory<br>
Currently registered Transforms:<br>
“AffineTransform_double_2_2”<br>
“AffineTransform_double_3_3”<br>
“AffineTransform_double_4_4”<br>
“AffineTransform_float_2_2”<br>
“AffineTransform_float_3_3”<br>
“AffineTransform_float_4_4”<br>
“AzimuthElevationToCartesianTransform_double_3_3”<br>
“AzimuthElevationToCartesianTransform_float_3_3”<br>
“BSplineDeformableTransform_double_2_2”<br>
“BSplineDeformableTransform_double_3_3”<br>
“BSplineDeformableTransform_float_2_2”<br>
“BSplineDeformableTransform_float_3_3”<br>
“BSplineSmoothingOnUpdateDisplacementFieldTransform_double_2_2”<br>
“BSplineSmoothingOnUpdateDisplacementFieldTransform_double_3_3”<br>
“BSplineSmoothingOnUpdateDisplacementFieldTransform_float_2_2”<br>
“BSplineSmoothingOnUpdateDisplacementFieldTransform_float_3_3”<br>
“BSplineTransform_double_2_2”<br>
“BSplineTransform_double_3_3”<br>
“BSplineTransform_float_2_2”<br>
“BSplineTransform_float_3_3”<br>
“CenteredAffineTransform_double_2_2”<br>
“CenteredAffineTransform_double_3_3”<br>
“CenteredAffineTransform_float_2_2”<br>
“CenteredAffineTransform_float_3_3”<br>
“CenteredEuler3DTransform_double_3_3”<br>
“CenteredEuler3DTransform_float_3_3”<br>
“CenteredRigid2DTransform_double_2_2”<br>
“CenteredRigid2DTransform_float_2_2”<br>
“CenteredSimilarity2DTransform_double_2_2”<br>
“CenteredSimilarity2DTransform_float_2_2”<br>
“ComposeScaleSkewVersor3DTransform_double_3_3”<br>
“ComposeScaleSkewVersor3DTransform_float_3_3”<br>
“CompositeTransform_double_2_2”<br>
“CompositeTransform_double_3_3”<br>
“CompositeTransform_double_4_4”<br>
“CompositeTransform_float_2_2”<br>
“CompositeTransform_float_3_3”<br>
“CompositeTransform_float_4_4”<br>
“ConstantVelocityFieldTransform_double_2_2”<br>
“ConstantVelocityFieldTransform_double_3_3”<br>
“ConstantVelocityFieldTransform_float_2_2”<br>
“ConstantVelocityFieldTransform_float_3_3”<br>
“DisplacementFieldTransform_double_2_2”<br>
“DisplacementFieldTransform_double_3_3”<br>
“DisplacementFieldTransform_float_2_2”<br>
“DisplacementFieldTransform_float_3_3”<br>
“Euler2DTransform_double_2_2”<br>
“Euler2DTransform_float_2_2”<br>
“Euler3DTransform_double_3_3”<br>
“Euler3DTransform_float_3_3”<br>
“FixedCenterOfRotationAffineTransform_double_3_3”<br>
“FixedCenterOfRotationAffineTransform_float_3_3”<br>
“GaussianExponentialDiffeomorphicTransform_double_2_2”<br>
“GaussianExponentialDiffeomorphicTransform_double_3_3”<br>
“GaussianExponentialDiffeomorphicTransform_float_2_2”<br>
“GaussianExponentialDiffeomorphicTransform_float_3_3”<br>
“GaussianSmoothingOnUpdateDisplacementFieldTransform_double_2_2”<br>
“GaussianSmoothingOnUpdateDisplacementFieldTransform_double_3_3”<br>
“GaussianSmoothingOnUpdateDisplacementFieldTransform_float_2_2”<br>
“GaussianSmoothingOnUpdateDisplacementFieldTransform_float_3_3”<br>
“GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_double_2_2”<br>
“GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_double_3_3”<br>
“GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_float_2_2”<br>
“GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_float_3_3”<br>
“IdentityTransform_double_2_2”<br>
“IdentityTransform_double_3_3”<br>
“IdentityTransform_double_4_4”<br>
“IdentityTransform_float_2_2”<br>
“IdentityTransform_float_3_3”<br>
“IdentityTransform_float_4_4”<br>
“QuaternionRigidTransform_double_3_3”<br>
“QuaternionRigidTransform_float_3_3”<br>
“Rigid2DTransform_double_2_2”<br>
“Rigid2DTransform_float_2_2”<br>
“Rigid3DPerspectiveTransform_double_3_2”<br>
“Rigid3DPerspectiveTransform_float_3_2”<br>
“Rigid3DTransform_double_3_3”<br>
“Rigid3DTransform_float_3_3”<br>
“ScalableAffineTransform_double_3_3”<br>
“ScalableAffineTransform_float_3_3”<br>
“ScaleLogarithmicTransform_double_3_3”<br>
“ScaleLogarithmicTransform_float_3_3”<br>
“ScaleSkewVersor3DTransform_double_3_3”<br>
“ScaleSkewVersor3DTransform_float_3_3”<br>
“ScaleTransform_double_2_2”<br>
“ScaleTransform_double_3_3”<br>
“ScaleTransform_double_4_4”<br>
“ScaleTransform_float_2_2”<br>
“ScaleTransform_float_3_3”<br>
“ScaleTransform_float_4_4”<br>
“ScaleVersor3DTransform_double_3_3”<br>
“ScaleVersor3DTransform_float_3_3”<br>
“Similarity2DTransform_double_2_2”<br>
“Similarity2DTransform_float_2_2”<br>
“Similarity3DTransform_double_3_3”<br>
“Similarity3DTransform_float_3_3”<br>
“ThinPlateSplineKernelTransform_double_3_3”<br>
“ThinPlateSplineKernelTransform_float_3_3”<br>
“TimeVaryingBSplineVelocityFieldTransform_double_2_2”<br>
“TimeVaryingBSplineVelocityFieldTransform_double_3_3”<br>
“TimeVaryingBSplineVelocityFieldTransform_float_2_2”<br>
“TimeVaryingBSplineVelocityFieldTransform_float_3_3”<br>
“TimeVaryingVelocityFieldTransform_double_2_2”<br>
“TimeVaryingVelocityFieldTransform_double_3_3”<br>
“TimeVaryingVelocityFieldTransform_float_2_2”<br>
“TimeVaryingVelocityFieldTransform_float_3_3”<br>
“TranslationTransform_double_2_2”<br>
“TranslationTransform_double_3_3”<br>
“TranslationTransform_double_4_4”<br>
“TranslationTransform_float_2_2”<br>
“TranslationTransform_float_3_3”<br>
“TranslationTransform_float_4_4”<br>
“VelocityFieldTransform_double_2_2”<br>
“VelocityFieldTransform_double_3_3”<br>
“VelocityFieldTransform_float_2_2”<br>
“VelocityFieldTransform_float_3_3”<br>
“VersorRigid3DTransform_double_3_3”<br>
“VersorRigid3DTransform_float_3_3”<br>
“VersorTransform_double_3_3”<br>
“VersorTransform_float_3_3”<br>
Resample Scalar/Vector/DWI Volume completed with errors”</li>
</ol>
<p>I have attempted to troubleshoot the issue by reinstalling the software, but unfortunately, the problem persists.</p>
<p>If anyone in the community has experienced a similar issue or has any insights into resolving this problem, I would be extremely grateful for your assistance. Additionally, if there are any specific troubleshooting steps or configurations I should try, please do not hesitate to let me know.</p>
<p>Thank you very much for your time and assistance.<br>
P.S. I’m using 5.6.1 stable release, but I’ve tried also 5.7.0 release (I’m ubuntu user).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df04eaef55c3df0ce5646806946c8a654d33fc4c.jpeg" data-download-href="/uploads/short-url/vOV0KnnhuZSQwpzmYhD7mpT4B6k.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df04eaef55c3df0ce5646806946c8a654d33fc4c_2_690x388.jpeg" alt="image" data-base62-sha1="vOV0KnnhuZSQwpzmYhD7mpT4B6k" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df04eaef55c3df0ce5646806946c8a654d33fc4c_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df04eaef55c3df0ce5646806946c8a654d33fc4c_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df04eaef55c3df0ce5646806946c8a654d33fc4c_2_1380x776.jpeg 2x" data-dominant-color="99989D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-02-15 02:19 UTC)

<p>CropVolume works for me with 5.6.1 with the CTACardio from SampleData.  Maybe try that data and also check that you have enough disk space.</p>

---

## Post #3 by @joseph00 (2024-02-15 06:44 UTC)

<p>Thanks for your reply.</p>
<p>The crop function seems to work fine with example images (MRI image or CT image for example), but it’s failing with some of the CT scans I have.</p>
<p>Any idea why this might be happening?</p>

---

## Post #4 by @muratmaga (2024-02-15 07:09 UTC)

<p>Since this is specific to your data, the only way we can help you is if you can share the data so that we can replicate the issue and understand why it is happening.</p>
<p>Do you have any anonymized data that you can share?</p>

---
