---
topic_id: 1584
title: "Resampling Or Modify Mesh Properties Of A Model To Get Light"
date: 2017-12-04
url: https://discourse.slicer.org/t/1584
---

# Resampling or modify mesh properties of a model to get light .stl files

**Topic ID**: 1584
**Date**: 2017-12-04
**URL**: https://discourse.slicer.org/t/resampling-or-modify-mesh-properties-of-a-model-to-get-light-stl-files/1584

---

## Post #1 by @terajnol (2017-12-04 11:06 UTC)

<p>Hi everyone,</p>
<p>I am trying to obtain a 3D model of a vertebra from DICOM images, and to display it in other applications, such as a 3D pdf. So far, my solution is to export a stl file from Slicer and then to translate it to u3D with MeshLab for example.<br>
Thanks to the tutorial and the Segment Editor module, I could manage to get a nice 3D model rendering and to export it as .stl file (by cropping, thresholding and a bit of filtering and then exporting my segmentation as a model).</p>
<p>However, my stl file is still heavy and I couldn’t find a way to resample my model, or to modify the mesh properties. Am I missing a module or an option within Segment Editor ?</p>
<p>Thank you for your help,</p>

---

## Post #2 by @lassoan (2017-12-04 12:41 UTC)

<p>You can use “Surface Toolbox” module’s “decimate” option to reduce mesh size without changing visual appearance of the model.</p>

---

## Post #3 by @terajnol (2017-12-05 13:14 UTC)

<p>Ok perfect, that was exactly what I was looking for.<br>
Thanks !</p>

---
