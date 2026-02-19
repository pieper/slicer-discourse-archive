---
topic_id: 2698
title: "Atlas Based Subcortical Nuclei Transformation"
date: 2018-04-26
url: https://discourse.slicer.org/t/2698
---

# Atlas-based subcortical nuclei transformation

**Topic ID**: 2698
**Date**: 2018-04-26
**URL**: https://discourse.slicer.org/t/atlas-based-subcortical-nuclei-transformation/2698

---

## Post #1 by @Vinny (2018-04-26 12:36 UTC)

<p>Hello 3d Slicer forum,</p>
<p>I used General Registration (BRAINS) (affine followed by nonrigid B-spline) to align the MNI T1 atlas with a patient’s ac-pc aligned space; the results looked good  There are various subcortical nuclei as separate nifti files that are stored in MNI space that I would like to bring into the patient’s ac-pc space.  The approach I took was to pass the nuclei sequentially through first the calculated affine transformation node followed by the B-spline transformation node, hardening the transformation after each node.  Hardening after the affine node went fine and the nuclei were established in good proximity to their known anatomical location.  However, after hardening the B-Spline node, the nuclei appear in a different location and/or disappear from view.  Is there any reason for this?</p>
<p>3d Slicer version 4.8.1<br>
Windows 10</p>
<p>Thanks for your help!</p>

---

## Post #2 by @Vinny (2018-04-27 00:58 UTC)

<p>For the separate subcortical nuclei nifti files (in MNI space), I resampled them using the calculated non-rigid transform.  This appeared to solve the problem and then I can carry harden the transform in the affine node.  My question now is related to the interpolation method for the resampling…how to decide which to use?  Linear vs BSpline interpolation?  From an anatomical fidelity perspective, it seems that for my dataset, linear interpolation is best.  But is this considered correct given that I’m using a B-Spline transform for the resampling?</p>

---

## Post #3 by @lassoan (2018-04-27 04:01 UTC)

<p>If you need the output to be aligned with another volume’s geometry then resampling using a reference volume is the way to go.</p>
<p>Interpolator: Linear is fast and may be good enough if voxel size small. Windowed sinc provides the closest estimation of the theoretically optimal low-pass filter. B-spline may reach same image quality as windowed sinc, but it is much faster. Nearest neighbor (no interpolation) is only for labelmaps.</p>

---

## Post #4 by @Vinny (2018-04-27 10:15 UTC)

<p>Great, thanks Andras!   Also, for the General Registration (BRAINS) module, I’ve coregistered the MNI T1 to the patient’s T1.  Is resampling done as part of the transformation?   If so, do you know if the Linear interpolation is being used as the default?</p>
<p>Thanks!</p>

---

## Post #5 by @lassoan (2018-04-30 12:47 UTC)

<p>Yes, if you harden a non-linear transform using Transforms module then linear interpolation is used.</p>

---
