---
topic_id: 48001
title: "Spect Ct Reconstruction "
date: 2026-08-27
url: https://discourse.slicer.org/t/48001
last_bumped: 2026-08-30T15:47:13.581Z
---

# Spect Ct Reconstruction 

**Topic ID**: 48001
**Date**: 2026-08-27
**URL**: https://discourse.slicer.org/t/spect-ct-reconstruction/48001

---

## Post #1 by @JuanIgnacioElutchanz (2026-08-27 19:23 UTC)

<p>Hello everyone, I need some help in terms of spect reconstruction in 3dSlicer.                       I’m student of Nuclear Medicine in Uruguay, I’m currently working on a research project to present at the Uruguayan Congress of Nuclear Medicine.</p>
<p>In our daily work at the hospital, we noticed a pattern in certain types of pulmonary patients. When we performed SPECT CT followed by fusion with attenuation correction, we observed artifactual enhancement. One of the suspected reasons for this is our equipment, which includes a low-dose, 16-slice CT scanner.</p>
<p>My idea is to reprocess these scans, but replacing our Spect CT scans with DICOM data from CT scans performed at other centres with dedicated scanners that have a higher number of slices. I haven’t had any problems loading and viewing the DICOMs in 3D Slicer, but when I try to reconstruct them with attenuation correction, the program freezes on the processing bar and I can’t get the results.</p>
<p>I need help from someone who has done similar work or understands why the program might not be performing the fusion.</p>

---

## Post #2 by @drnoorfatima (2026-08-28 02:17 UTC)

<p>Hey, email me here <a href="mailto:noorfatimacheema249@gmail.com">noorfatimacheema249@gmail.com</a></p>

---

## Post #3 by @pieper (2026-08-29 16:04 UTC)

<p>I’m not sure about the spect part, but if Slicer is freezing it would be good to narrow that down and get it fixed.</p>
<p>First thing to try is a smaller dataset or a bigger machine with more RAM.  If that doesn’t work the best thing is to test with public data and come up with specific reproducible steps to replicate the issue.</p>

---

## Post #4 by @JuanIgnacioElutchanz (2026-08-30 15:47 UTC)

<p>Hi Steve, that’s my other suspicion. Tomorrow I’ll try it on one of the hospital’s processing PCs, which have more processing power than the current one. I’ll keep you updated. Thanks and regards</p>

---
