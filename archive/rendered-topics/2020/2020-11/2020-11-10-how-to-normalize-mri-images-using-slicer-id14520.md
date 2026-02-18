# How to normalize MRI images using Slicer?

**Topic ID**: 14520
**Date**: 2020-11-10
**URL**: https://discourse.slicer.org/t/how-to-normalize-mri-images-using-slicer/14520

---

## Post #1 by @Eshani (2020-11-10 16:02 UTC)

<p>Hi! I am using the Slicer 4.10.2 version to segment only the eyeball in my MRI images. So, I want to know the simplest way of  preprocessing/normalizing of brain MRI images as I don’t have any knowledge regarding python codes.</p>

---

## Post #2 by @lassoan (2020-11-10 19:18 UTC)

<p>Probably you don’t need much pre-processing/normalizing to segment the eyeball. I would expect that by using <a href="https://discourse.slicer.org/t/new-segment-editor-effect-local-threshold/9233">“Local threshold” effect</a> you can segment the eyeball with a few clicks (set a threshold range then Ctrl-click in the eyeball).</p>

---

## Post #3 by @Eshani (2020-11-11 12:50 UTC)

<p>Thank you very much!</p>

---
