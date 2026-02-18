# Landmark registration and combining intenstities of fixed and moving volume

**Topic ID**: 7106
**Date**: 2019-06-10
**URL**: https://discourse.slicer.org/t/landmark-registration-and-combining-intenstities-of-fixed-and-moving-volume/7106

---

## Post #1 by @mahagop (2019-06-10 12:48 UTC)

<p>I am trying to combine two image volumes using landmark points. I created four fiducial points. I was successful in visualizing the landmark points and positioning them accurately. I applied “adding” option to combine the intensities in the resultant transformed image. However I am unable to add the intensities from both fixed and moving image volumes. Is there a way to combine the intensities. I tried to do in dicom converter option but it displays only intensity from one image volume. I am stuck up in this last step. Does any one have a solution for it.</p>

---

## Post #2 by @pieper (2019-06-10 13:16 UTC)

<p>Hi -</p>
<p>Maybe you are looking for this: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/AddScalarVolumes" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/AddScalarVolumes</a></p>

---

## Post #3 by @mahagop (2019-06-10 16:50 UTC)

<p>Thanks for reply. Yes, I am looking for such kind of volume addition. I want to add two volumes as it is without any interpolation. The volumes consists of radiation dose information. The challenge which I faced is, after landmark registration the moving volume is transformed and is in different orientation (change in X, Y and Z  and angle)  w.r.t fixed volume. The moving volume gets aligned with fixed volume w.r.t the fiducial points. I want to add both moving and fixed volume exactly in this position.  However the moving volume adds to fixed volume only with its initial position. i.e. the fiducial points matching doesn’t exist during adding scalar volumes. Is there any solution for this?<br>
Thanks</p>

---

## Post #4 by @lassoan (2019-06-10 18:39 UTC)

<p>SlicerRT extension is developed specifically for RT dose accumulation. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT#Tutorials" rel="nofollow noopener">SlicerRT tutorials</a> for step-by-step instructions (probably “World congress 2015” tutorial is the most relevant for you).</p>

---

## Post #5 by @mahagop (2019-06-11 08:29 UTC)

<p>Thanks for the input. The tutorials was informative. Slicer RT is very much useful for routine RT based procedure in which planning is usually based on CT images. I am looking for image registration in Gamma Knife treatment which is little different from regular RT. But I have to mention that the new Gamma Knife Modality such as ICON has RT kind of work flow. For older version GK Models such as in B, 4C and Perfexion treatment workflow is different. Planning is solely based on MRI imaging modality.</p>

---

## Post #6 by @mahagop (2019-06-18 04:23 UTC)

<p>Hi,<br>
Anyone could suggest adding fixed scalar volume intensity with moving scalar volume intensity after transformation (in Landmark Registration) without using slicerRT module.<br>
Thanks</p>

---

## Post #7 by @pieper (2019-06-18 13:32 UTC)

<p>Hi <a class="mention" href="/u/mahagop">@mahagop</a> - Maybe you are missing a step, you can harden the transform (from the right-click menu in the Transform hierarchy of the Data module) and then use Filtering-&gt;Add Scalar Volumes.</p>

---

## Post #8 by @mahagop (2019-06-19 11:32 UTC)

<p>Hi Steve,<br>
Thanks for mentioning the vital step. Finally I got the solution by using this step. It works now great.<br>
Thanks once again.</p>

---
