# Ac-pc based registration

**Topic ID**: 2733
**Date**: 2018-04-30
**URL**: https://discourse.slicer.org/t/ac-pc-based-registration/2733

---

## Post #1 by @Vinny (2018-04-30 10:16 UTC)

<p>Hello 3d Slicer forum,</p>
<p>I’d like to register two different images based on aligning the ac-pc lines.  What is the best way to do this?  Usually, I would do a nonlinear normalization of the moving image (atlas) to the fixed image, followed by a rigid affine transformation.  However, the acpc lines do not necessarily align once this methodology is performed.  I was thinking that the next step would then be to align the acpc lines through aligning the acpc landmarks?  Is this a correct strategy?</p>
<p>Thanks for your help,</p>
<p>Vinny</p>

---

## Post #2 by @Vinny (2018-05-01 01:54 UTC)

<p>I used the Landmark registration module and from what I see, both ACPC lines can be aligned either through affine or thinplate (nonlinear) registration using a fixed and moving image.  There are still differences in other areas.</p>

---

## Post #3 by @lassoan (2018-05-01 04:15 UTC)

<p>What is the goal of the alignment? If you need ACPC line alignment then you can use 4 landmarks and rigid transform.</p>
<p>If you need complete alignment of all structures in the images then you can use image-based registration using “General registration (BRAINS)” or “General registration (Elastix)” module (the latter requires installation of SlicerElastix extension).</p>

---

## Post #4 by @Vinny (2018-05-01 10:38 UTC)

<p>The goal of the alignment is to bring atlas structures in MNI space into patient ac-pc space, particularly basal ganglia structures since I am dealing with DBS patients.  A complete alignment of all structures is ideal.  I’ve tried the General Registration (BRAINS) module and got good alignment between the T1 mni atlas and T1 patient acpc image for one patient using a nonrigid followed by affine transformation (moving image = T1 mni; fixed = patient T1 acpc); however, alignment was not good for another patient.  I was thinking that maybe forcing an ACPC alignment between the images may lead to consistently good alignment across different patients.  I was hoping that it wouldn’t have to be a trial-and-error registration for each patient.</p>
<p>is there a way to manually adjust the moving image in 3d Slicer such as in ITK-SNAP?  <a href="https://www.youtube.com/watch?v=RT_M_EPzdyY" rel="nofollow noopener">https://www.youtube.com/watch?v=RT_M_EPzdyY</a></p>

---

## Post #5 by @lassoan (2018-05-02 22:34 UTC)

<p>Slicer has way better methods for image alignment! You have the option of manual translation/rotation using sliders or 3D widgets, but all these processes are iterative, take a long time, especially if you need to rotate as well. A much faster, better, non-iterative method is landmark-based registration. There are several modules for this, but the two that stand out are:</p>
<ol>
<li>
<p><a href="https://github.com/pieper/LandmarkRegistration/">Landmark registration module</a> (in Slicer core). It is mainly developer for fine-tuning alignment of images.</p>
</li>
<li>
<p>Fiducial registration wizard (in SlicerIGT extension). It is more general purpose (not just for image to image but also for model to image, navigation system to image, etc.). See U-12 <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorial</a> for guidance about how to use it.</p>
</li>
</ol>
<p>Both modules support rigid and deformable alignments.</p>

---

## Post #6 by @Vinny (2018-05-03 10:18 UTC)

<p>Great thanks Andras!  I was not aware of the Fiducial registration wizard.</p>

---
