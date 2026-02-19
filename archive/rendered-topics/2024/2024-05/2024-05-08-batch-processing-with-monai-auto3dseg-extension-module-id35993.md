---
topic_id: 35993
title: "Batch Processing With Monai Auto3Dseg Extension Module"
date: 2024-05-08
url: https://discourse.slicer.org/t/35993
---

# Batch processing with MONAI Auto3DSeg extension module

**Topic ID**: 35993
**Date**: 2024-05-08
**URL**: https://discourse.slicer.org/t/batch-processing-with-monai-auto3dseg-extension-module/35993

---

## Post #1 by @Osson4 (2024-05-08 14:45 UTC)

<p>I am working on a set of around 60 CTs and I would like to process the volumes with the same model (brain and hemorrage) from the new monai Auto3dSeg extension module.<br>
While I can process them one by one within the GUI, by selecting every volume and generating a new segmentation each time (which is pretty tedious), I wanted a way to batch process a series of volumes like with other slicer modules.<br>
I tried to implement this in the python interactor in Slicer, but I am not a coding expert and I can’t seem to work it out.<br>
there’s probably an easy solution involving the modules’ attributes but I can’t find it.<br>
thanks to whomever might help me!</p>
<p>input: loaded volumes<br>
output: segmentation model inferences from Monai auto3Dseg module</p>

---

## Post #2 by @LeidyMoraV (2024-05-08 18:32 UTC)

<p>I’m don’t really know much about MONAI but there is a batch processing in another module named ALPACA, maybe you can look it up and try to use something similar to that.</p>

---
