# Feature extraction from anisotropic 3D VOIs: should we apply Force2D potion?

**Topic ID**: 21285
**Date**: 2021-12-31
**URL**: https://discourse.slicer.org/t/feature-extraction-from-anisotropic-3d-vois-should-we-apply-force2d-potion/21285

---

## Post #1 by @Eugene (2021-12-31 06:25 UTC)

<p>Greetings expert team. Much obliged for your great invention and maintanance of pyradiomics!</p>
<p>I’m currently working on some MRI T2WI data, consecutively delineating 2D ROIs in each slice on the coronal plane. I noticed that my MRI data have different slice thickness, including 3mm and 5mm. Relative literature suggests that resampling should be done in such scenario, but as I refer to the exampleMR_NoResampling.yaml settings in the pyradiomics folder, I learn that force2D is recommended to handle the anisotropic data, which means I should use this setting:</p>
<p>force2D: true<br>
force2Ddimension: 0</p>
<p>Am I correct?<br>
Thank you in advantage for a request.</p>

---

## Post #2 by @Valentina_Nepi (2022-01-01 20:49 UTC)

<p>If you are working roi in the coronal plane you should use ‘force2Ddimension: 1’</p>

---

## Post #3 by @Eugene (2022-01-02 03:52 UTC)

<p>Thank you for your kind reply. I’m not so sure about the force2Ddimension setting. To my understanding, value 0 identifies the out-of-plane dimension -  ‘z’ dimension, resulting in features being extracted from the working-plane(xy plane). You can refer to this post: <a href="https://groups.google.com/g/pyradiomics/c/cUD7bW4Tw-Q" rel="noopener nofollow ugc">Forced2D extraction dimensions (google.com)</a>.</p>

---

## Post #4 by @Valentina_Nepi (2022-01-02 07:18 UTC)

<p>Interesting post! So, let’s wait some confirms now</p>

---

## Post #5 by @JoostJM (2022-01-11 11:46 UTC)

<p>Correct. However, the x, y and z planes are relative to the image axis, not the real-world axis. Therefore, it is possible that even though the MRI is coronal, the z dimension is the one you want tot set as the force2D dimension. Easiest way of checking this is to run a small extraction and take a look at the diagnostic features. These should include the spacing, e.g. (1, 1, 3), where ‘3’ will identify the slice thickness.<br>
To make everything more confusing, this means you should set the dimension to 0.<br>
This is because the spacing is the reflection of the SimpleITK image object, which lists spacing as xyz, while the force2Ddimension applies the the numpy array view, which is in zyx.</p>

---

## Post #6 by @Eugene (2022-01-12 02:03 UTC)

<p>Thank you for your kind reply! Hopefully this post will help more people with the same question that I have.</p>

---
