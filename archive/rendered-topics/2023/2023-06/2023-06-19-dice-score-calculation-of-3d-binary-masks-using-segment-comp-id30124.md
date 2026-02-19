---
topic_id: 30124
title: "Dice Score Calculation Of 3D Binary Masks Using Segment Comp"
date: 2023-06-19
url: https://discourse.slicer.org/t/30124
---

# Dice score calculation of 3D binary masks using Segment Comparison module

**Topic ID**: 30124
**Date**: 2023-06-19
**URL**: https://discourse.slicer.org/t/dice-score-calculation-of-3d-binary-masks-using-segment-comparison-module/30124

---

## Post #1 by @thanuja (2023-06-19 15:44 UTC)

<p>Hi All,</p>
<p>Could you please point out where can I find the source code for Segment Comparison module (Slicer version 5.2.2). I’m getting different values of dice score for 3D binary nifti masks when using 3D Slicer and the Monai framework. This is the monai function I’m using:</p>
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
<p>Please note that I have tried both mean and sum for reduction method and still getting different values from Slicer and Monai .</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2023-06-20 12:58 UTC)

<p>This is the source code of the module:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerRt/SlicerRT/tree/master/SegmentComparison">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/SlicerRT/tree/master/SegmentComparison" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerRt/SlicerRT/tree/master/SegmentComparison" target="_blank" rel="noopener">SlicerRT/SegmentComparison at master · SlicerRt/SlicerRT</a></h3>

  <p><a href="https://github.com/SlicerRt/SlicerRT/tree/master/SegmentComparison" target="_blank" rel="noopener">master/SegmentComparison</a></p>

  <p><span class="label1">Open-source toolkit for radiation therapy research, an extension of 3D Slicer. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), struc...</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The difference may be due to the resizing that a MONAI transform does, that’s where I’d look first.</p>

---

## Post #3 by @thanuja (2023-06-20 17:05 UTC)

<p>Thank you for sharing the code. I’m getting same dice score value as monai for below python code as well:</p>
<pre><code class="lang-auto"># Calculate dice score of masks
def calculate_dice_score(predicted, ground_truth):
    area_sum = np.sum(predicted == 1) + np.sum(ground_truth == 1)
    if area_sum &gt; 0:
        return np.sum(predicted[ground_truth == 1]) * 2.0 / area_sum
    else:
        return 1.0 # Will return 1.0 if both predicted and ground truth masks are empty
</code></pre>
<p>Will check the slicer code. Thanks again.</p>

---

## Post #4 by @thanuja (2023-08-29 19:59 UTC)

<p>I’m getting the same value with Segment Comaprison module as with manual calculation. Sorry for the trouble. Thank you!</p>

---
