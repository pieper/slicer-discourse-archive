---
topic_id: 48171
title: "Radiomics ECHO 2D"
date: 2026-09-15
url: https://discourse.slicer.org/t/48171
last_bumped: 2026-09-16T18:39:26.853Z
---

# Radiomics ECHO 2D

**Topic ID**: 48171
**Date**: 2026-09-15
**URL**: https://discourse.slicer.org/t/radiomics-echo-2d/48171

---

## Post #1 by @Bouthaina_Besbes (2026-09-15 14:06 UTC)

<p>Hello everybody,</p>
<p>I m trying to extract radiomics features from echo images. And I can’t seem to understand how.</p>
<p>I can segment the images, but when I use de radiomics slicer extension, I can’t apply it to my ROI.</p>
<p>I don’t know if the software is not designed to be applyed on 2D images</p>

---

## Post #2 by @Deep_Learning (2026-09-16 12:51 UTC)

<p>Def should work.  I’m not sure that you can apply it to rois but to what 3Dslicer calls segmentations which are masks.  That is what pyradiomics uses.  If that is true, you could draw/paint segmentations or convert the ROIs to masks.</p>

---

## Post #3 by @lassoan (2026-09-16 18:39 UTC)

<p>Ultrasound images are usually saved as screenshots in DICOM (capturing the color RGB screen of the ultrasound machine). These images may be usable for computing radiomics features, but probably you need to first convert the color image to grayscale using “Vector to scalar volume” module.</p>

---
