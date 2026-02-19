---
topic_id: 21154
title: "Pyradiomics Glcm Calculation"
date: 2021-12-20
url: https://discourse.slicer.org/t/21154
---

# Pyradiomics (GLCM) calculation

**Topic ID**: 21154
**Date**: 2021-12-20
**URL**: https://discourse.slicer.org/t/pyradiomics-glcm-calculation/21154

---

## Post #1 by @tenzin_kunkyab (2021-12-20 19:29 UTC)

<p>Hi developers,</p>
<p>I am working on implementing a past study on radiomics. The extract from the published report includes the definition of the GLCM radiomic features as follows in their matlab software:</p>
<p>“Neighbouring voxels were paired in four spatial directions within the 2D axial image planes [(-1, 0), (-1, -1), (0, -1), (1, -1)]. All second-order texture measures were computed based on GLCMs calculated using each of these four directions, and were averaged over all directions.”</p>
<p>I am using pyRadiomics, is there a setting somewhere where I can implement this particular GLCM technique? I used symmetrical GLCM in the past but I am not sure if it resembles this particular way of calculating GLCM.</p>
<p>best<br>
Tenzin</p>

---

## Post #2 by @JoostJM (2022-01-11 11:29 UTC)

<p>Ensure force2D is set to true (default false) and symmetricalGLCM is set to true (default).</p>
<p>Be aware that other preprocessing steps (especially pixel size resampling and discretization methods) can heavily influence the resultant feature values.</p>

---

## Post #3 by @tenzin_kunkyab (2022-01-14 19:34 UTC)

<p>Great! Thank you so much! thats all I need!</p>

---
