# Radiomic analysis thesis questions

**Topic ID**: 18366
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/radiomic-analysis-thesis-questions/18366

---

## Post #1 by @retidani18 (2021-06-28 06:00 UTC)

<p>Hi!</p>
<p>I am new here. I am doing my medical physics masters and my thesis heavily involves 3D Slicer. In short a lung sample was imaged using a special x-ray technique. Than the cells in this sample was dyed. I can use this dyed cell slices (only 7 slices across the sample) to segment different types of cells. Than I want to use one part of this segmentation (the other part is for testing) to do radiomic analysis with it.</p>
<p>The segmentation might take a long time because I think I cannot make it automatic. So I segment every 10th-5th (there is about 900) slice and than I’ll use 'Fill between Slices". Do you think it is a suitable solution?</p>
<p>After that I will do some pre-processing and than radiomic analysis. After dimension reduction I would like to train an AI. To test the performance of the AI I want to use the segmented cells I did not use for the radiomic part. Can I/Should I do this whole thing (dimension reduction and AI training) in 3D Slicer.</p>
<p>I appreciate every advises and suggestions.</p>
<p>Thank you in advance!</p>

---

## Post #2 by @lassoan (2021-07-17 23:11 UTC)

<p>What you describe sound reasonable. You can do radiomics feature extraction, AI training, inference, etc. in any Python environment (including Slicer’s). Slicer is very good for implementing interactive steps, such segmentation or review of input or resulting images. Doing everything in Slicer may be convenient because then you only need to set up a single working environment. Let us know if you have any specific questions or run into issues.</p>

---
