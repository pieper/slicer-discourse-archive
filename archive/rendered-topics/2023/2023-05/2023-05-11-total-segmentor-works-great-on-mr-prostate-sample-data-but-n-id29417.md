---
topic_id: 29417
title: "Total Segmentor Works Great On Mr Prostate Sample Data But N"
date: 2023-05-11
url: https://discourse.slicer.org/t/29417
---

# Total segmentor works great on MR Prostate sample data but not CT abdomen. Why

**Topic ID**: 29417
**Date**: 2023-05-11
**URL**: https://discourse.slicer.org/t/total-segmentor-works-great-on-mr-prostate-sample-data-but-not-ct-abdomen-why/29417

---

## Post #1 by @metarom (2023-05-11 21:25 UTC)

<p>I have been trying to run total segmentation extension for hours on my MacBook Air M2. I use fast-mode and so far the only dataset that has worked would be the MR Prostate sample data. Could it be too hard of a processing work as the prostate dataset is a lot smaller that abdomen? Ive tried the Liver sample data swell, same error. This is the error (NB returned non-zero exit status 120.):</p>
<p>Failed to compute results.</p>
<p>Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/5l/0634852x57xbl97b00t1237h0000gn/T/Slicer-dennisjohnsen/__SlicerTemp__2023-05-11_16+54+53.747/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/5l/0634852x57xbl97b00t1237h0000gn/T/Slicer-dennisjohnsen/__SlicerTemp__2023-05-11_16+54+53.747/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>

---

## Post #2 by @lassoan (2023-05-11 21:44 UTC)

<p>Most likely your computer cannot handle  this task. MRI images can be a magnitude smaller than CT images. You can try to downsample your CT using “Crop volume” module and see if you have better luck on the smaller image.</p>
<p>What version of Pytorch do you have (you can find it in Pytorch Utils module)?<br>
How much RAM and free disk space does your computer have?</p>

---

## Post #3 by @metarom (2023-05-11 21:55 UTC)

<p>Thank you for replying!</p>
<p>I have a MacBook Air M2 with 8 gb of RAM and 120gb free space (SSD).<br>
I run Slicer 5.2, and the PyTorch version 7df4613.</p>
<p>I also tried running a fresh install of 3d slicer and total segmentation on a Windows virtual machine with  and got the same error.</p>

---

## Post #4 by @lassoan (2023-05-12 03:01 UTC)

<p>8GB RAM is really small. MacOS may swap out memory to the disk (you have enough disk space, so that’s good), but maybe some steps just require more memory.</p>
<p>PyTorch version should be something like 1.x or 2.x. I don’t know what this 7df4613 may come from. Could you take a screenshot of your Pytorch Utils module?</p>
<p>You can try installing the latest Slicer Preview Release. You may also try to force installing pytorch 2.0 by uninstalling pytorch and then installing it by typing this in Slicer’s Python interpreter: <code>pip_install('torch&gt;=2')</code></p>

---
