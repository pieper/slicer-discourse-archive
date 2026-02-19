---
topic_id: 32388
title: "How Can I Avoid Holes In The Output When Converting A Model"
date: 2023-10-23
url: https://discourse.slicer.org/t/32388
---

# How can I avoid holes in the output when converting a model to segmentation?

**Topic ID**: 32388
**Date**: 2023-10-23
**URL**: https://discourse.slicer.org/t/how-can-i-avoid-holes-in-the-output-when-converting-a-model-to-segmentation/32388

---

## Post #1 by @Yu.Mingzhong_Michael (2023-10-23 18:23 UTC)

<p>Hi,<br>
I am using Slicer 5.0.2 to convert a model file (.ply) to segmentation mask image, with the following functions : 1. convert model to segmentation node; 2. export visible segmentation to binary label map.</p>
<p>But when I view the volume rending image of the binary label map, I find that there several holes in the surface. I want to know how to get a segmentation mask image  without the annoying holes, and why the holes are generated?</p>
<p>Thanks!</p>
<hr>
<p>Operating system:Windows<br>
Slicer version:5.0.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2023-10-23 18:35 UTC)

<p>My first guess is that you are not sampling the surface models with high enough resolution to capture the shape of your model well.  Try a higher sampling grid.  If you’re not sure how we can explain.</p>
<p>To give better answers you could post some screenshots so we know what you are describing.</p>

---

## Post #3 by @Yu.Mingzhong_Michael (2023-10-24 03:29 UTC)

<p>maybe low resolution of the model is the reason of the holes generated,<br>
this is the original model<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a95a80b2ed9dd881763b52b2f2d2696868d7bb9.png" data-download-href="/uploads/short-url/jLYwKSvdGhsczqW00aKX2WReRSN.png?dl=1" title="original_model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a95a80b2ed9dd881763b52b2f2d2696868d7bb9_2_595x500.png" alt="original_model" data-base62-sha1="jLYwKSvdGhsczqW00aKX2WReRSN" width="595" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a95a80b2ed9dd881763b52b2f2d2696868d7bb9_2_595x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a95a80b2ed9dd881763b52b2f2d2696868d7bb9_2_892x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a95a80b2ed9dd881763b52b2f2d2696868d7bb9.png 2x" data-dominant-color="9FA1B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">original_model</span><span class="informations">1092×917 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
and the labelmap (volume rendering) after conversion is<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04b77e1ef479e5704a3743143bd6bad6be15f091.png" data-download-href="/uploads/short-url/FJ2xXsZHDknVSJ3ejx3Y2dNc7D.png?dl=1" title="binary_labelmap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04b77e1ef479e5704a3743143bd6bad6be15f091_2_583x500.png" alt="binary_labelmap" data-base62-sha1="FJ2xXsZHDknVSJ3ejx3Y2dNc7D" width="583" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04b77e1ef479e5704a3743143bd6bad6be15f091_2_583x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04b77e1ef479e5704a3743143bd6bad6be15f091_2_874x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04b77e1ef479e5704a3743143bd6bad6be15f091.png 2x" data-dominant-color="7E899C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">binary_labelmap</span><span class="informations">1117×957 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
several holes can be seen on it.<br>
I tried to upload the the original model file (.ply), but not authorized to do so.</p>
<p>I’m wondering, if any chance that something in the program is not good enough converting the segmentation node to binary labelmap.</p>
<p>thanks for your help.</p>

---

## Post #4 by @Yu.Mingzhong_Michael (2023-10-24 03:36 UTC)

<p>would you please give me some ideas on how to sampling the surface model with higher sampling grid. I tried to look for some parameter settings on it in Slicer, but found nothing.</p>

---

## Post #5 by @lassoan (2023-10-24 13:13 UTC)

<p>See these <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file">step-by-step instructions for importing a model into a segmentation</a> with as high accuracy as you need.</p>

---

## Post #6 by @Yu.Mingzhong_Michael (2023-10-26 01:22 UTC)

<p>Thanks a lot! I finally get binary labelmap without holes with the instructions. But the labelmap image file saved becomes so large, from original 400K to nearly 21M.</p>

---

## Post #7 by @lassoan (2023-10-26 01:32 UTC)

<p>This is normal. Labelmap representation of an object can be infinitely larger than its closed surface representation. The size of the labelmap representation depends on the chosen resolution.</p>
<p>If you only need to segment anatomical structures then you usually don’t need to go below the original CT image resolution, which is not that big (usually less than 512 x 512 x 512 voxels). However, if you also want to represent CAD models with high accuracy in the segmentation then you may need to increase the resolution a lot. Therefore, it can make sense to design your workflow so that you finish all your anatomical segmentations, export to model (closed surface), and combine that with CAD models (e.g., using “Combine Models” module in Sandbox extension).</p>
<p>If you export the segmentation to a model again then you can reduce the file size dramatically (e.g., by 99%) with barely visible change in appearance, by using the <code>Surface Toolbox</code> module’s <code>Decimate</code> option.</p>

---
