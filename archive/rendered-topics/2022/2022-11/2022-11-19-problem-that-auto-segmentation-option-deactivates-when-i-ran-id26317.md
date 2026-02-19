---
topic_id: 26317
title: "Problem That Auto Segmentation Option Deactivates When I Ran"
date: 2022-11-19
url: https://discourse.slicer.org/t/26317
---

# Problem that 'Auto Segmentation' option deactivates when I ran monaibundle apps based on MONAI Label server of 3D-Slicer

**Topic ID**: 26317
**Date**: 2022-11-19
**URL**: https://discourse.slicer.org/t/problem-that-auto-segmentation-option-deactivates-when-i-ran-monaibundle-apps-based-on-monai-label-server-of-3d-slicer/26317

---

## Post #1 by @platanus (2022-11-19 02:55 UTC)

<p>Dear 3D-Slicer developers</p>
<p>I’m running ‘[brats_mri_segmentation_v0.3.3] (<a href="https://github.com/Project-MONAI/model-zoo/releases" class="inline-onebox" rel="noopener nofollow ugc">Releases · Project-MONAI/model-zoo · GitHub</a>)’ using monaibundle apps in 3D-Slicer.</p>
<p>I captured work scene of monaibundle apps based on MONAI Label server that I ran in 3D-Slicer.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/883d69e1b2bc29da3aa43c88588f694ac7ef1bdc.mp4">
  </div><p></p>
<p>As above video,  I pressed 'refresh(green) button next to MONAI Label server. so I checked Master volume information that include nii.gz.</p>
<p>And then when I pressed ‘Next Sample’ button, I can’t see ‘Model’ name and ‘Run’ button of ‘Auto Segmentation’ option. It seems to deactivate in MONAI Label module, when I ran MONAI Label server with ‘brats_mri_segmentation_v0.3.3’ using monaibundle apps.</p>
<p>Please, let me know how to activate Auto Segmentation option when it ran MONAI Label using ‘brats_mri_segmentation_v0.3.3’ through monaibundle apps.</p>
<blockquote>
<p>Blockquote</p>
</blockquote>

---

## Post #3 by @platanus (2022-11-21 07:52 UTC)

<p>I solved problem that doesn’t show Auto Segmenation option in 3D-Slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58b4dd3e0cc59797df1fb887b85f2b974a077844.png" data-download-href="/uploads/short-url/cEJw4cfeM5L1aE8FPIkzeKciomw.png?dl=1" title="auto_segmentation_success" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b4dd3e0cc59797df1fb887b85f2b974a077844_2_690x280.png" alt="auto_segmentation_success" data-base62-sha1="cEJw4cfeM5L1aE8FPIkzeKciomw" width="690" height="280" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b4dd3e0cc59797df1fb887b85f2b974a077844_2_690x280.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b4dd3e0cc59797df1fb887b85f2b974a077844_2_1035x420.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b4dd3e0cc59797df1fb887b85f2b974a077844_2_1380x560.png 2x" data-dominant-color="88888E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">auto_segmentation_success</span><span class="informations">2561×1041 279 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @platanus (2022-11-21 07:55 UTC)

<p>But, I want to solve problem that segmentation detection can’t be when I press ‘run’ button next to ‘model’ name in ‘Auto Segmenation’ option.</p>
<p>I edited “in_channels” : 4 into “in_channels” : 1 in inference.json and train.json, it dosn’t run ‘Auto Segmentation’.</p>
<p>Please, let me know how to edit json file code to solve this problem.</p>

---

## Post #5 by @Bor_Antolic (2023-01-22 20:10 UTC)

<p>Can you explain once again how you solved this problem? I do not understand.</p>

---
