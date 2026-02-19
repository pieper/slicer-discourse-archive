---
topic_id: 21468
title: "Extract Multiple Labels From One Image Without Reloading Ima"
date: 2022-01-14
url: https://discourse.slicer.org/t/21468
---

# Extract multiple labels from one image without reloading image and mask data? 

**Topic ID**: 21468
**Date**: 2022-01-14
**URL**: https://discourse.slicer.org/t/extract-multiple-labels-from-one-image-without-reloading-image-and-mask-data/21468

---

## Post #1 by @Sebastian_Nagel (2022-01-14 19:51 UTC)

<p>Dear Community,</p>
<p>we performed a CT segmentation for which we placed multiple labels into one dataset.</p>
<p>Now when we start extracting the features using either the command line or a Jupyter notebook, the image and mask data need to be loaded for each label, even if they are from the same image data. Is there a way to speed up the extraction in the way that the extractor loads the image and mask once and then goes through all the labels? Loading image and mask into a variable and the parsing it to the extractor speeded up things a little…</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @JoostJM (2022-01-18 12:41 UTC)

<p>If you do this from a jupyter notebook you can load the image and mask as SimpleITK image objects, which you can pass instead of the path to the corresponding files. Then the image and mask are loaded only once. All other processing steps are repeated for each computation, as they are ROI dependent (e.g. the resampling only resamples the ROI and a limited region around it for computational and memory efficiency).</p>

---

## Post #3 by @JoostJM (2022-01-18 12:44 UTC)

<p>On the commandline there is no option to prevent reloading the image, but you can enable parallel processing to speed things up a bit (<code>--jobs</code>). This parallelizes the process on the case level (e.g. each thread processes a single case, multiple threads can run in parallel). Especially handy in case of large datasets.</p>

---

## Post #4 by @Sebastian_Nagel (2022-01-19 20:40 UTC)

<p>Dear Joost, thank you very much for the responses!</p>
<p>We will try both options, but the latter one is really attractive since we do not have to change much in our setup.</p>

---
