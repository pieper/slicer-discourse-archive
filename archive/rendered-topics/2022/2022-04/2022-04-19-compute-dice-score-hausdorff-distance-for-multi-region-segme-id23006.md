---
topic_id: 23006
title: "Compute Dice Score Hausdorff Distance For Multi Region Segme"
date: 2022-04-19
url: https://discourse.slicer.org/t/23006
---

# Compute Dice score, Hausdorff distance for Multi-Region segmentation

**Topic ID**: 23006
**Date**: 2022-04-19
**URL**: https://discourse.slicer.org/t/compute-dice-score-hausdorff-distance-for-multi-region-segmentation/23006

---

## Post #1 by @Js165 (2022-04-19 00:41 UTC)

<p>Hi,<br>
I have NIFTI files of sizes (512 x 512 x 150) of auto-segmentation and manual segmentation. <strong>Each file/slice contains the segmentation of multiple regions (seven regions).</strong> I want to compute the dice score, Hausdorff distance, Jaccard index, and average surface distance.<br>
Could you please suggest the easiest method for that purpose? I don’t want to convert NIFTI to PNGs/JPEGs. I tried the <a href="http://plastimatch.org/plastimatch.html#plastimatch-dice" rel="noopener nofollow ugc">plastimatch dice</a>. It seems that it doesn’t work for multi-region segmentation. Please find the command and relevant output of plastimatch. Please suggest if I am missing anything or if there is a better approach.</p>
<p>plastimatch dice --all manual_GT.nii Auto_seg.nii<br>
CENTER_OF_MASS<br>
ref	       15.9689	      -56.3064	      -32.7915<br>
cmp	       16.4171	      -56.3639	       -35.121<br>
TP:        194139<br>
TN:      40941820<br>
FN:         10594<br>
FP:         10055<br>
DICE:      0.949504<br>
SE:      0.948255<br>
SP:      0.999754<br>
Hausdorff distance = 12.750913<br>
Avg average Hausdorff distance = 0.131478<br>
Max average Hausdorff distance = 0.160547<br>
Percent (0.95) Hausdorff distance = 0.634766<br>
Hausdorff distance (boundary) = 27.516542<br>
Avg average Hausdorff distance (boundary) = 1.705389<br>
Max average Hausdorff distance (boundary) = 1.814141<br>
Percent (0.95) Hausdorff distance (boundary) = 5.156286</p>

---

## Post #2 by @cpinter (2022-04-19 08:59 UTC)

<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison">Segment Comparison</a> module in the SlicerRT extension allows you to compute Dice and Hausdorff on segmentations containing multiple labels. You’ll need to first convert the labelmap volumes to segmentation nodes (in Segmentations module Import/Export section, or in the Data module by right-clicking the labelmap volume).</p>

---

## Post #3 by @Js165 (2022-04-19 13:56 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Thanks a lot! It worked. I love Slicer! Btw, some features can be improved and can be made more interactive by incorporating some sort of automation. For example, the “Segment Comparison” tool should have the Box/tick option for all segments rather than the drop-down menu.</p>

---

## Post #4 by @thanuja (2023-06-16 19:52 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Could you please point out where can I find the source code for Segment Comparison module (Version 5.2.2). I’m getting different values of dice score for 3D binary nifti masks when using 3D Slicer and Monai framework. This is the monai function I’m using:</p>
<pre><code class="lang-auto">def calculate_dice_score(predicted, ground_truth):
      dice_metric = monai.metrics.DiceMetric(include_background=False, reduction="mean")
      # Convert the predicted and ground truth masks to PyTorch tensors
      predicted_tensor = torch.from_numpy(predicted)
      ground_truth_tensor = torch.from_numpy(ground_truth)
      # Reshape tensors to have batch size and number of channels
      predicted_tensor = predicted_tensor.unsqueeze(0).unsqueeze(0)
      ground_truth_tensor = ground_truth_tensor.unsqueeze(0).unsqueeze(0)
      # Calculate the Dice score
      dice_score = dice_metric(y_pred =predicted_tensor, y = ground_truth_tensor)
      return dice_score.item()
</code></pre>
<p>Thanks!</p>

---

## Post #5 by @cpinter (2023-06-19 12:53 UTC)

<p>Please create a new topic for this and I’ll answer there. If we keep reusing year-old topic nobidy will be able to find anything here. Thanks!</p>

---

## Post #6 by @thanuja (2023-06-19 15:45 UTC)

<p>Noted. Thank you! Created a new topic: <a href="https://discourse.slicer.org/t/dice-score-calculation-of-3d-binary-masks-using-segment-comparison-module/30124">Dice score calculation of 3D binary masks using Segment Comparison module</a></p>

---

## Post #7 by @Young_Wang (2023-12-13 21:53 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> thank you. However I have trouble locating Dice and Hausdorff from SlicerRT extension. I’m using Slicer 5.6. Could you please point me where they are.</p>

---

## Post #8 by @cpinter (2023-12-14 10:17 UTC)

<p>It’s in the Segment Comparison module. What operating system do you use? There have been issues on Mac lately with some extensions.</p>

---

## Post #9 by @Young_Wang (2023-12-14 16:58 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> , thanks for getting back to me. I use 14.2 (23C64) on an Apple M1 Pro. I couldn’t find this Segment Comparison module on Slicer 5.6 and Slicer 5.6.1. But I was able to find it on Slicer 5.2 after I revert it back.</p>

---

## Post #10 by @cpinter (2024-05-10 11:49 UTC)

<p>3 posts were merged into an existing topic: <a href="/t/hausdorff-distance-interval/35998/3">Hausdorff Distance Interval</a></p>

---
