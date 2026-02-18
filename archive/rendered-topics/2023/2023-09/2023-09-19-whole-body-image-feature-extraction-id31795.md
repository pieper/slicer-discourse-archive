# Whole-body image feature extraction

**Topic ID**: 31795
**Date**: 2023-09-19
**URL**: https://discourse.slicer.org/t/whole-body-image-feature-extraction/31795

---

## Post #1 by @Jimmy (2023-09-19 20:03 UTC)

<p>Hi,</p>
<p>I am extracting radiomics features from whole-body PET/CT using Pyradiomics. My ROI is whole-body fat.</p>
<p>Problem is, it got stuck at some point and would not give any output even after running overnight. But when I seperate the whole-body fat to two separate part, upper/lower, it can be finished.</p>
<p>My question is, is it due to the configuration dose not allow running too many slices at a time, such as whole-body images? If separate the whole-body structure into two parts is the only solution, is there anyway to combine the output into a result as a whole structure afterwards?</p>
<p>Thanks in adavance for any of your input,<br>
Jimmy</p>

---

## Post #2 by @mladenze (2023-09-19 23:06 UTC)

<p>Even though this is possible for some of the radiomic features, in general, combining the radiomics would not be possible. Higher order features are based on spatial dependency of voxels. When you split the ROI in two parts, you break this spatial relationship.</p>
<p>Have you tried monitoring your RAM utilization during runtime? Consider increasing available RAM if this is your bottleneck.</p>

---

## Post #4 by @Jimmy (2023-09-19 23:16 UTC)

<p>Thank you so much for your comments. Actually, I was thinking the same that split the ROI will make it unavailable to combine again.</p>
<p>Yes, I have checked the RAM (32G) has ~50% usage and CPU is at ~15% during running. Is there any configuration in the package that limit the total images to be processed? Otherwise, I can not think up anything to fix it.</p>
<p>Thanks for your input again,</p>

---

## Post #5 by @mladenze (2023-09-19 23:31 UTC)

<p>You can also consider this setting in PyRadiomics configuration file:<br>
<em>Force2D = True</em><br>
This will result in per-slice radiomics computation, with averaging at the end. Resulting features will be more stable, but you will loose some of the 3D information.</p>

---

## Post #6 by @Jimmy (2023-09-19 23:36 UTC)

<p>Thanks a lot for the suggestion. I will try it.</p>
<p>Is there any configuration that set limit to RAM/CPU usage or maximum processing slices for each ROI? It stuck as a whole but can get through after split, which still make me wondering.</p>

---

## Post #7 by @mladenze (2023-09-19 23:49 UTC)

<p>I do not think that there is a setting for max number of slices, but you can set max number of voxels processed in a single batch, <em>voxelBatch &gt; X</em>, where X is an integer &gt; 0.</p>
<p>I also think it would be a good test to restrict your computation to a single feature class and see if that works first, say:</p>
<pre><code class="lang-auto">featureClass:
    firstorder:
</code></pre>
<p>This may give you some insight if this fails with higher order features only.</p>

---

## Post #8 by @Jimmy (2023-09-20 00:00 UTC)

<p>Thanks again for your input.</p>
<p>I was also wondering this is possibly due to the high amount of voxels/data it has to process and store temporarily, which exceeds some sort of limitations before the final result is generated.</p>
<p>Is the <em>voxelBatch &gt; X</em>, X is the minimum, or maximum? Should I set it higher in my case?<br>
Thanks</p>

---

## Post #9 by @mladenze (2023-09-20 00:16 UTC)

<p>It is a maximum. So try setting it to some larger number that is smaller than your largest ROI’s number of voxels divided by 2. The actual parameter setting would be something like this…</p>
<pre><code class="lang-auto">voxelSetting:
    voxelBatch: 500
</code></pre>
<p>where I have chosen 500 to be the max number of voxels in a batch.</p>

---
