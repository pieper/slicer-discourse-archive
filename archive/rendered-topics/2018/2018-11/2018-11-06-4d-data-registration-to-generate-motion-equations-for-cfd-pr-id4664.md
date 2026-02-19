---
topic_id: 4664
title: "4D Data Registration To Generate Motion Equations For Cfd Pr"
date: 2018-11-06
url: https://discourse.slicer.org/t/4664
---

# 4D Data Registration To Generate Motion Equations for CFD Programs

**Topic ID**: 4664
**Date**: 2018-11-06
**URL**: https://discourse.slicer.org/t/4d-data-registration-to-generate-motion-equations-for-cfd-programs/4664

---

## Post #1 by @aginn (2018-11-06 22:14 UTC)

<p>Hello everyone,</p>
<p>I need to model the deformation of a 4D MRI dataset for use within CFD software. I will need equations that track node position over time.</p>
<p>Can 3D slicer’s registration capabilities achieve this?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2018-11-06 23:24 UTC)

<p><a href="https://github.com/moselhy/SlicerSequenceRegistration">Sequence registration extension</a> can compute displacement for every voxel for every time point.</p>

---

## Post #3 by @aginn (2018-11-07 15:34 UTC)

<p>I was able to find the “Sequence Registration” extension on the slicer app store (I am using a Mac). However, I could not find the “Elastix” app, which is required for proper function.</p>
<p>Has this app changed or been renamed?</p>
<p>Thank you!</p>

---

## Post #4 by @lassoan (2018-11-07 23:20 UTC)

<p>You need to install SlicerElastix extension. On Mac, you may need to <a href="http://elastix.isi.uu.nl/download.php">download Elastix application</a> and set its path in Slicer in “General registration (Elastix)” extension.</p>

---
