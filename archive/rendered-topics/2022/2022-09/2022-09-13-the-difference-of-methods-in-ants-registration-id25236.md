---
topic_id: 25236
title: "The Difference Of Methods In Ants Registration"
date: 2022-09-13
url: https://discourse.slicer.org/t/25236
---

# The difference of methods in ANTs Registration

**Topic ID**: 25236
**Date**: 2022-09-13
**URL**: https://discourse.slicer.org/t/the-difference-of-methods-in-ants-registration/25236

---

## Post #1 by @Chuan (2022-09-13 12:24 UTC)

<p>Hi,<br>
I use 3D slicer5.0.3 and in ANTs there are three different methods(stages) which are QuickSyN, Rigid, Rigid plus Affine.<br>
Now I have many CT images of different subjects head. And I want to registrate the different CT images to the same reference before I extract the landmark location information.<br>
I compared these three methods that for Rigid and Rigid+Affine, the new volume after registration looks similar. But for QuickSyN, it is different. And I am not sure whether the QuickSyN will change the shape and the CT value of the original CT. Just looks very different and the max CT value is also changed.<br>
I would like to ask and also double check whether the method of QuickSyN will change the shape of CT images. Because I would like to keep the shape and if it is true, I probably will choose from Rigid and Rigid+Affine.</p>
<p>Best,<br>
Chuan</p>

---

## Post #2 by @ebrahim (2022-09-13 14:10 UTC)

<p>I guess you are looking at the SlicerANTs extension, right? QuickSyN appears to be a SlicerANTs setting that carries out multiple steps of ANTs registration: Rigid, then Affine, then SyN. Learn about the meanings of these <a href="https://antspy.readthedocs.io/en/latest/registration.html" rel="noopener nofollow ugc">here</a>.</p>
<blockquote>
<p>And I am not sure whether the QuickSyN will change the shape and the CT value of the original CT.</p>
</blockquote>
<p>Registration will not change CT value; it doesn’t know about your imaging modality and will not touch the voxel values.</p>
<p>The question about changing “shape” depends on what you mean by shape, i.e. what you’re interested in preserving. <a href="https://pubmed.ncbi.nlm.nih.gov/17659998/" rel="noopener nofollow ugc">SyN</a> is a type of deformable (“non-parametric”) registration using velocity fields, so probably doesn’t preserve shape by any geometric definition of the word, but it should preserve topology. Affine will not necessarily preserve distances, but the transform will be uniform across the image (looks the same in each local region; affine just means linear with a possible translation) and it should preserve angles (typically an affine transform need not preserve angles, but the way ANTs seems to use the word it should). Rigid preserves both angles and distances.</p>

---

## Post #3 by @Chuan (2022-09-13 14:12 UTC)

<p>Thanks! That is exactly what I want!</p>

---

## Post #4 by @muratmaga (2022-09-14 05:23 UTC)

<aside class="quote no-group" data-username="Chuan" data-post="1" data-topic="25236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>the new volume after registration looks similar.</p>
</blockquote>
</aside>
<p>To be clear, that new volume is your original volume after the resultant deformation field calculated by ANTs applied to it, regardless whether the registration is Rigid+affine only or SyN. The intensity values are likely to be different from the original CT, due to necessary interpolation to warp the image in all cases. Just because max value remained the same doesn’t mean that the individual voxel intensities are not modified. The effect of the affine registration might be low, if the reference and target is already in the same orientation, and of approximate size.</p>
<aside class="quote no-group" data-username="Chuan" data-post="1" data-topic="25236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>And I want to registrate the different CT images to the same reference before I extract the landmark location information.</p>
</blockquote>
</aside>
<p>If your targets and reference are similar in shape, affine might be sufficient. For more precise local deformation, you need to use SyN.</p>

---

## Post #5 by @ebrahim (2022-09-14 06:01 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="25236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>The intensity values are likely to be different from the original CT, due to necessary interpolation to warp the image in all cases.</p>
</blockquote>
</aside>
<p>Oops that’s right; my answer should be corrected. Interpolation changes voxel values.</p>

---

## Post #6 by @Chuan (2022-09-14 09:05 UTC)

<p>Hi, thank you a lot! Now I am clear that the CT value will change.<br>
The targets and reference are similar in shape because all of them are head but they are different in size.<br>
Yesterday I employed the Rigid method on all targets because I dont want to change the size. But for some cases, the result is not good. So I used ‘IGT Fiducial registration Wizard’ to rigidly registrate my targets. For example, I used three anotamy points (which represents the same point for different individual) to build my rigid transfor matrix.<br>
But I am confused that for those cases with different sizes, how did the target position itself? And also whether the 3D slicer rendering model can represent the actual size in the real world?</p>

---

## Post #7 by @Chuan (2022-09-14 09:17 UTC)

<p>To make my question clear, for the newborn and 9month baby head, the size are different, and the red points are marked points for   Fiducial registration Wizard.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b84a85e6427f186b362b04b33511935e391d7024.png" alt="image" data-base62-sha1="qijwcLnSFQFeE09vkJPenoVUEAY" width="353" height="186"></p>
<ol>
<li>List item</li>
</ol>

---

## Post #8 by @muratmaga (2022-09-14 15:53 UTC)

<aside class="quote no-group" data-username="Chuan" data-post="7" data-topic="25236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>To make my question clear, for the newborn and 9month baby head, the size are different, and the red points are marked points for Fiducial registration Wizard.</p>
</blockquote>
</aside>
<p>I am still not clear on what you are trying to do with the image registration. There are typically two ways you can use the registration.</p>
<ol>
<li>There are a set of canonical landmarks in some sort of reference sample, and you deform your new target to this reference, and then use the inverse of the transformation (using a metric like SyN that does provide invertible transforms) to transfer the canonical landmarks back to the new subject.</li>
<li>You can register a number of new samples into an existing reference sample, and then do the statistics on the resultant warp fields (e.g., compare whether warp fields are statistically significant across groups, or visualize the expansion/contraction of individual voxels etc).</li>
</ol>
<p>Whether you will use affine or deformable registration (or the total warp field, which is combining these two) depends on the questions you are asking.</p>
<p>Newborn to 9 months old is a very difficult registration problem due to closure of the fontanelles, matching the size of the skull will not be sufficient, as the shape of the skull is changing allometrically (in an non-uniform) way. The choice of your registration parameters (similarity metric and the geometric transformation model) will affect the output, and you have no real basis to prefer one over the other, if you do not have constrains or an objective measure to assess the outcome (e.g., which method gives you the landmark estimates closest to your expert landmarks).</p>
<p>Below, the second row are outputs of antsRegistration  using the same pair of images in the top row (new born to 6 months of age) using different similarity and transformation models. <strong>A</strong> uses a large deformation model based on mean squared metric and velocity fields, <strong>B</strong> is the SyNCC (SyN with cross-correlation). Both of them does a good job of reducing the global size difference due to growth, but the local deformations are very different. Without having an objective method of choosing one over the other, you are sort of stuck.</p>
<p>Landmarks are usually the way to constrain this (or use them to choose one outcome over the other), but sounds like you are trying to use the image registration to transfer the landmarks perhaps?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8815f13f17095d71d3860e15e5026f9be9f36a8c.jpeg" data-download-href="/uploads/short-url/jpRWJnEE29iP6q08FwQYWZ2L73K.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8815f13f17095d71d3860e15e5026f9be9f36a8c_2_488x500.jpeg" alt="image" data-base62-sha1="jpRWJnEE29iP6q08FwQYWZ2L73K" width="488" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8815f13f17095d71d3860e15e5026f9be9f36a8c_2_488x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8815f13f17095d71d3860e15e5026f9be9f36a8c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8815f13f17095d71d3860e15e5026f9be9f36a8c.jpeg 2x" data-dominant-color="81818E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">570×583 84.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
