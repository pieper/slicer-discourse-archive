---
topic_id: 41832
title: "Blood Oxygenation Level Dependent Bold Imaging Utility In Re"
date: 2025-02-22
url: https://discourse.slicer.org/t/41832
---

# Blood Oxygenation Level-Dependent (BOLD) Imaging Utility in Renal Evaluation

**Topic ID**: 41832
**Date**: 2025-02-22
**URL**: https://discourse.slicer.org/t/blood-oxygenation-level-dependent-bold-imaging-utility-in-renal-evaluation/41832

---

## Post #1 by @chrisvasquezfuentes (2025-02-22 21:07 UTC)

<p>Hello, I hope you’re doing well. I was wondering if you could provide guidance on extracting the BOLD value from the acquired signal. I would greatly appreciate your assistance.</p>
<p>Is there a tool that allows me to extract and plot the pixel values within a specific Region of Interest (ROI) or segmentation?</p>

---

## Post #2 by @pieper (2025-02-22 22:13 UTC)

<p>Yes, you can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">SegmentStatistics</a> for that.</p>

---

## Post #3 by @chrisvasquezfuentes (2025-02-23 13:31 UTC)

<p>I’m trying to identify the spatial distribution of pixel values within my segmentation. Specifically, I’d like to visualize where the pixels with values closest to the mean or maximum are located, within my 1160-pixel segmentation</p>

---

## Post #4 by @pieper (2025-02-23 15:56 UTC)

<p>You can that manually by getting the overall mean, max, etc for the segment and then re-thresholding within the segment to create new segments that will show the pixels of interest.  You might want to use a python script for reproducibility.</p>

---

## Post #5 by @chrisvasquezfuentes (2025-04-30 22:52 UTC)

<p>Sure, thanks for you answer. First, I select the pixel value width in the image I want, using the T2* image, the T1 map, and R2*. I generally use the circle or the line to calculate the pixels, but I always modify it visually to isolate only the renal cortex and then the renal medulla.</p>
<p>I would like to know if someone on the web could determine if the values provided by the program are the real ones. For example, if I were to calculate the diffusion restriction values in the renal cortex, it would be different (from the point of view of the number of pixels it would take in the ROI) than if I measured it directly on the workstation console, since I could only do it in a single slice. I would like to know if it is accurate, and if it were affirmative, could I also consider the T2* and R2* values as reliable?</p>

---
