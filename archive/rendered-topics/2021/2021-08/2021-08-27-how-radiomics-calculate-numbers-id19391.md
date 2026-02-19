---
topic_id: 19391
title: "How Radiomics Calculate Numbers"
date: 2021-08-27
url: https://discourse.slicer.org/t/19391
---

# How radiomics calculate numbers

**Topic ID**: 19391
**Date**: 2021-08-27
**URL**: https://discourse.slicer.org/t/how-radiomics-calculate-numbers/19391

---

## Post #1 by @hotsen (2021-08-27 21:52 UTC)

<p>Hi all,</p>
<p>I got some basic questions about radiomics. Say I have input image A and a lablemap B as input region, I got first-order features like mean, min, max using Radiomics. I assume Radiomics first generate an array using the input image and labelmap, then got all the feature numbers from that array. Is it possible to output this array? I want to change the array by set up a threshold, for example change all numbers less than 0.5 to 0 in the array, then I can generate a new lablemap from this array. Next, I can get features using this new lablemap. Is this doable or I am in a totally wrong direction?</p>
<p>Thank you!</p>

---

## Post #2 by @JoostJM (2022-01-21 10:20 UTC)

<p>What you are describing is already implemented. Using option ‘resegmentRange’ you can set the range of values you consider to be valid. Voxels outside that range are removed from the segmentation prior to feature calculation. See the customization section on <a href="http://pyradiomics.readthedocs.io">pyradiomics.readthedocs.io</a> for more details.</p>
<p>By the way, it is not possible to extract the array of values half-way during the extraction process, but it is possible to get them outside of PyRadiomics.</p>
<p>If you have loaded them as SimpleITK.Image objects <code>im</code> and <code>ma</code>:</p>
<pre><code class="lang-auto">import SimpleITK as sitk
im_arr = sitk.GetArrayFromImage(im)
ma_arr = sitk.GetArrayFromImage(ma) == label
segemented_voxels = im_arr[ma_arr]
</code></pre>

---
