---
topic_id: 27511
title: "Using Monailabel For Vertebrae Segmentation"
date: 2023-01-28
url: https://discourse.slicer.org/t/27511
---

# Using MONAILabel for vertebrae segmentation

**Topic ID**: 27511
**Date**: 2023-01-28
**URL**: https://discourse.slicer.org/t/using-monailabel-for-vertebrae-segmentation/27511

---

## Post #1 by @DeepaKrishnaswamy (2023-01-28 00:58 UTC)

<p>Hi,</p>
<p>I’m trying to perform inference using the pretrained model from the 3 stage vertebrae segmentation pipeline from MONAI Label, but have been running into a few issues on a Windows machine with Slicer version 5.2.1:</p>
<ol>
<li>
<p>I’ve been able to start the server and run the first step localization_spine without runtime errors, but unfortunately it produces empty segments. I’ve tried this using a nifti file from both Verse2019 and Verse2020, which are the datasets the 3 stage pipeline were originally trained on. I’ve tried other models such as the segmentation_spleen and the segmentation_full_ct from here:<a href="https://drive.google.com/drive/folders/17eJan-8_oNCnZyJk8B9zLQpwaOjtDuKi?usp=share_link" class="inline-onebox" rel="noopener nofollow ugc">radiology_full_ct-upgraded-HYBRID - Google Drive</a>, and those have produced mostly accurate output labels.</p>
</li>
<li>
<p>I also tried running the entire vertebrae_pipeline, but this resulted in the following error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53a3161001501797b5cf90acffd81d392ec905f4.png" data-download-href="/uploads/short-url/bVT2vZnMzXP7VNiVSXcXdjucWhe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53a3161001501797b5cf90acffd81d392ec905f4.png" alt="image" data-base62-sha1="bVT2vZnMzXP7VNiVSXcXdjucWhe" width="690" height="80" data-dominant-color="1A1A1A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">963×113 4.71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ol>
<p>Has anyone encountered similar issues? Thanks!</p>
<p>Deepa</p>

---

## Post #2 by @mau_igna_06 (2023-01-28 13:03 UTC)

<aside class="quote no-group" data-username="DeepaKrishnaswamy" data-post="1" data-topic="27511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepakrishnaswamy/48/8913_2.png" class="avatar"> DeepaKrishnaswamy:</div>
<blockquote>
<p>Has anyone encountered similar issues?</p>
</blockquote>
</aside>
<p>Hi. Yes. I couldn’t make it work either</p>

---

## Post #3 by @diazandr3s (2023-01-30 19:36 UTC)

<p>Hi <a class="mention" href="/u/deepakrishnaswamy">@DeepaKrishnaswamy</a>,</p>
<p>Thanks for providing the details of your experience using MONAI Label here and on the issue here: <a href="https://github.com/Project-MONAI/MONAILabel/issues/1268#issuecomment-1409022013" class="inline-onebox" rel="noopener nofollow ugc">vertebrae_pipeline produces an error during inference · Issue #1268 · Project-MONAI/MONAILabel · GitHub</a></p>
<p>It is good that you managed to run the vertebra model on the Medical Segmentation Decathlon dataset.</p>
<p>The vertebra segmentation model was trained only on a portion of the VerSe dataset (~60 volumes). I’ve also had similar issues with that dataset and I think it was because some files were corrupted or had wrong NIfTI headers.</p>
<p>If you have a GPU, you could also try the whole-body CT segmentation model available here: <a href="https://drive.google.com/drive/folders/17eJan-8_oNCnZyJk8B9zLQpwaOjtDuKi?usp=share_link" class="inline-onebox" rel="noopener nofollow ugc">radiology_full_ct-upgraded-HYBRID - Google Drive</a></p>
<p>That model also segments all vertebras.</p>
<p>Thanks again!</p>

---

## Post #4 by @diazandr3s (2023-01-30 19:42 UTC)

<p>Hi <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>,</p>
<p>Is it the same error you faced last time?<br>
As far as I remember the issue you faced was related to not having computing resources. Did you manage to run these models on a bigger GPU/CPU?<br>
If you’re facing a different issue, please don’t hesitate to post the logs directly on the MONAI Label repository: <a href="https://github.com/Project-MONAI/MONAILabel/issues" class="inline-onebox" rel="noopener nofollow ugc">Issues · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Thanks!</p>

---
