# PET lymph node automated segmentation 

**Topic ID**: 34329
**Date**: 2024-02-14
**URL**: https://discourse.slicer.org/t/pet-lymph-node-automated-segmentation/34329

---

## Post #1 by @kjmkjw (2024-02-14 16:23 UTC)

<p>Hi,</p>
<p>I’m new to 3D Slicer.</p>
<p>I am hoping to segment metabolically active lymph nodes using the SUV threshold.<br>
If I use Threshold tool on Segment Editor, and set the Threshold range and Apply, it would segment everything above that threshold like brain, kidney etc.</p>
<p>If I use PET Tumour Segmentation tool, it either include or exclude pixels outside of threshold range.</p>
<p>Is there a way, I could segment area within the threshold range within the anatomical compartment I want?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2024-02-14 18:15 UTC)

<p>Usually you can use thresholding to get an initial segmentation and then use Keep Selected Island in the Islands tool to keep just the part you want.  You may need to use the Scissors or other tool if you have adjacent (touching) areas to exclude.</p>

---
