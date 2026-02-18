# Registration error using MMI with an ROI moving mask

**Topic ID**: 4886
**Date**: 2018-11-27
**URL**: https://discourse.slicer.org/t/registration-error-using-mmi-with-an-roi-moving-mask/4886

---

## Post #1 by @Eloise (2018-11-27 11:55 UTC)

<p>Hi,</p>
<p>I am using the BRAINS registration module to register two MRI exams using an affine transform. I want to provide an ROI Masking image for the moving image, but I get the following error when using the MMI metric :</p>
<p>too many samples map outside moving image buffer, the images do not sufficiently overlap!</p>
<p>This is very surprising since the two MRI exams are already globally aligned (I just want to be more precise on some organs using the mask). And the registration runs when I use any other metric, but with unsatisfying results.</p>
<p>For test, I put the same MRI exam as both the fixed and moving images for the registration. When I put the mask as the ROI fixed masking image, it runs, but I get the same error when I put it as the ROI moving masking image!</p>
<p>Is there any bug or specificity for masking input moving with MMI ? Thanks for your help!</p>
<p>Eloïse</p>

---

## Post #2 by @lassoan (2018-11-28 07:36 UTC)

<p>If you use a small ROI mask then you need to increase sampling percentage accordingly. See details here: <a href="https://discourse.itk.org/t/how-to-fix-the-problem-of-too-many-samples-map-outside-moving-image-buffer/850" rel="nofollow noopener">https://discourse.itk.org/t/how-to-fix-the-problem-of-too-many-samples-map-outside-moving-image-buffer/850</a></p>

---

## Post #3 by @Eloise (2018-11-28 12:09 UTC)

<p>Hi,<br>
Thanks for your response! I try to set the sampling percentage to 1 to consider all voxels but it makes no difference. Any other idea ?<br>
I don’t understand why this problem only appears when considering an ROI mask for the moving image, with mutual information?</p>

---

## Post #4 by @lassoan (2018-11-28 13:55 UTC)

<p>How much is the volume of the masked region comopared to the volume of the entire image region?</p>
<p>You may try much higher, 30-100% ratio. If you still have problems, write to the ITK forum topic that I linked above.</p>

---

## Post #5 by @Eloise (2018-11-29 09:16 UTC)

<p>I’m sorry I meant 100% for the sampling percentage (it corresponds to a value of 1 in the BRAINS registration module).<br>
The masked region corresponds to a dilated organ, it represents 5% of the entire MRI Volume.<br>
What I don’t understand is that it works in one way when the mask is used for the fixed image, but if a switch the moving and fixed images to do the inverse registration, then the mask is used for the moving image, and it does not work anymore.</p>

---

## Post #6 by @lassoan (2018-11-29 16:23 UTC)

<p>Probably you can alleviate the error by cropping the image using Crop Volume module (so that the mask takes much more than 5% of the total volume).</p>
<p>For more information, you can read <a href="https://discourse.itk.org/t/fixed-mask-not-working-as-expected/1238" rel="nofollow noopener">this discussion</a>. You can also create a new topic for your question on the <a href="https://discourse.itk.org/" rel="nofollow noopener">ITK forum</a> (if you do that, please post the link here so those who interested can follow the discussion there).</p>

---

## Post #7 by @lassoan (2018-12-01 15:45 UTC)

<p>You may also try to use Elastix - via <a href="https://github.com/lassoan/SlicerElastix/" rel="nofollow noopener">SlicerElastix extension</a>. It tends to be much more robust than BRAINS. You may not even need masking, just approximately crop volumes to the same region before registration.</p>

---
