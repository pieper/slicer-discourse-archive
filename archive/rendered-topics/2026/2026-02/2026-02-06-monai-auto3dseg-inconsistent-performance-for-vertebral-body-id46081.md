---
topic_id: 46081
title: "Monai Auto3Dseg Inconsistent Performance For Vertebral Body"
date: 2026-02-06
url: https://discourse.slicer.org/t/46081
---

# MONAI Auto3DSeg – inconsistent performance for vertebral body segmentation

**Topic ID**: 46081
**Date**: 2026-02-06
**URL**: https://discourse.slicer.org/t/monai-auto3dseg-inconsistent-performance-for-vertebral-body-segmentation/46081

---

## Post #1 by @jchao (2026-02-06 21:23 UTC)

<p>Hi everyone,</p>
<p>I’m currently working with Prof. Ron Alkalay on a spine CT segmentation project using <strong>MONAI Auto3DSeg</strong> and would appreciate any advice from the community.</p>
<p>My task is to segment <strong>only vertebral bodies</strong>. I reformulated it as a <strong>binary segmentation task (VB vs. non-VB)</strong>, which initially improved the validation Dice to &gt;70%.</p>
<p>However, when I ran a second round of training, the performance dropped noticeably and did not recover, even though the training process itself ran normally.</p>
<p>Between the two runs, I changed the following parameters:</p>
<ul>
<li>
<p><strong>Resample resolution</strong><br>
From: (0.3125, 0.3125, 0.5)<br>
To:  (0.3125, 0.3125, 1.0)</p>
</li>
<li>
<p><strong>ROI size</strong><br>
From: (128, 128, 64)<br>
To:  (128, 128, 96)</p>
</li>
</ul>
<p>Other than these changes, the setup and data split were kept the same.</p>
<p>In both experiments, I used <strong>Auto3DSeg’s Quick training mode</strong>.</p>
<h4><a name="p-131814-dataset-details-1" class="anchor" href="#p-131814-dataset-details-1" aria-label="Heading link"></a>Dataset details</h4>
<ul>
<li>
<p><code>imagesTr</code>: ~60 GB, 257 CT volumes (<code>.nii.gz</code>)</p>
</li>
<li>
<p><code>labelsTr_bin</code>: ~385 MB, 257 binary segmentation masks (<code>.nii.gz</code>)</p>
</li>
</ul>
<p>Some additional details:</p>
<ul>
<li>
<p>Tool: MONAI Auto3DSeg - segresnet_0</p>
</li>
<li>
<p>Task: Vertebral body vs. background (binary)</p>
</li>
<li>
<p>Modality: CT</p>
</li>
<li>
<p>Tried adjusting: ROI size, AMP, batch/auto-scaling</p>
</li>
</ul>
<p>I’m trying to understand whether this performance drop is likely related to the coarser through-plane resolution, the larger ROI depth, Quick mode limitations, or some interaction with Auto3DSeg’s preprocessing and model selection.</p>
<p>If anyone has experience using Auto3DSeg for similar anatomical segmentation tasks, I would really appreciate any guidance on what to sanity-check first, or best practices for tuning these parameters.</p>
<p>I’m happy to share configs or logs if helpful.</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @pieper (2026-02-08 16:31 UTC)

<p>I have tried Auto3DSeg for training but not extensively.  The results were good, but not noticeably better than nnU-Net, so I’ve standardized on nnU-Net for a the last few years and have generally found that it behaves predictably as more data is added for training.  I don’t use any resampling or cropping, only segmentations and native resolution CT data.</p>
<p>The details change for each dataset, but the basic format for me is still as demonstrated <a href="https://github.com/pieper/nnmouse">in this nnmouse repo</a>.</p>
<p>The format of the input directories is a little different between Auto3DSeg and nnU-Net, but they are close enough that you can accomplish the renaming just with symbolic links, so you don’t need to duplicate the data.</p>
<p>Was there a particular reason you wanted to use Auto3DSeg instead of nnU-Net?</p>

---
