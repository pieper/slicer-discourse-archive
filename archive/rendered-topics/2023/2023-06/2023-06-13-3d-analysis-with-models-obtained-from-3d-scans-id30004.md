---
topic_id: 30004
title: "3D Analysis With Models Obtained From 3D Scans"
date: 2023-06-13
url: https://discourse.slicer.org/t/30004
---

# 3D analysis with models obtained from 3D scans

**Topic ID**: 30004
**Date**: 2023-06-13
**URL**: https://discourse.slicer.org/t/3d-analysis-with-models-obtained-from-3d-scans/30004

---

## Post #1 by @IsabelW96 (2023-06-13 08:38 UTC)

<p>Hello everyone,</p>
<p>Currently I am conducting research on the positioning accuracy of surgical guides on 3D printed bone models. I take a 3D scan of the bone models with the attached surgical guide, and I want to analyze this entire setup in comparison to a reference model.</p>
<p>I am fairly new to 3D Slicer, and I am working only with loaded STL files, which are the models.</p>
<p>The steps I want to perform are as follows:</p>
<ol>
<li>Set up a coordinate system on the reference model.</li>
<li>Align the test model with the reference model.</li>
<li>Compare the translation and rotation of the surgical guide on the test model with those on the reference model.</li>
</ol>
<p>Does anyone have any tips on the appropriate modules I can use?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @lassoan (2023-06-16 14:33 UTC)

<p>You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#model-registration">align the models using registration</a> and compute basic translation/rotation properties using <a href="https://github.com/PerkLab/SlicerSandbox#characterize-transform-matrix">Characterize transform matrix</a> module (provided by Sandbox extension).</p>

---
