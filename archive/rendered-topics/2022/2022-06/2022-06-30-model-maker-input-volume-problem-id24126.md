---
topic_id: 24126
title: "Model Maker Input Volume Problem"
date: 2022-06-30
url: https://discourse.slicer.org/t/24126
---

# Model maker input volume problem

**Topic ID**: 24126
**Date**: 2022-06-30
**URL**: https://discourse.slicer.org/t/model-maker-input-volume-problem/24126

---

## Post #1 by @canseda (2022-06-30 23:28 UTC)

<p>Problem report for Slicer 5.0.2 macosx-amd64: Hi, I’ve started use Slicer. Unfortunately, whenever I try to perform ‘model maker’ stage, after segmentation, the system gives error ‘cannot open input volume file…’. I watched all tutorial videos, I followed the steps exactly the same. I tried with my dicom files, also I tried with sample datas, there is nothing to change.<br>
What should I do, please help me?</p>

---

## Post #2 by @canseda (2022-06-30 23:28 UTC)

<p>hello everyone,<br>
trying to generate 3d models but I couldn’t make it. I keep seeing the same error message ‘No input data assigned to “Input Volume”’. Please, someone help me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
![Ekran Resmi 2022-06-30 15.39.30|690x416](upload://7V<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/186e5f2b87eb4c6e3f74c8ac993a7b3f98b5863a.jpeg" data-download-href="/uploads/short-url/3u7VDJyjJx7vXI596vkDmCh82O6.jpeg?dl=1" title="Ekran Resmi 2022-06-30 15.39.20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/186e5f2b87eb4c6e3f74c8ac993a7b3f98b5863a_2_690x414.jpeg" alt="Ekran Resmi 2022-06-30 15.39.20" data-base62-sha1="3u7VDJyjJx7vXI596vkDmCh82O6" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/186e5f2b87eb4c6e3f74c8ac993a7b3f98b5863a_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/186e5f2b87eb4c6e3f74c8ac993a7b3f98b5863a_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/186e5f2b87eb4c6e3f74c8ac993a7b3f98b5863a_2_1380x828.jpeg 2x" data-dominant-color="8A8B93"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Resmi 2022-06-30 15.39.20</span><span class="informations">1920×1152 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
VGiTUMoeMAaU9qctI4zLnXsaD.jpeg)<br>
Thank you…</p>

---

## Post #3 by @lassoan (2022-06-30 23:55 UTC)

<p>Model maker is a very old volume, which is indeed used in old tutorials. In current Slicer versions, once you segmented the structure of interest using Segment Editor, you can go to Data module and right-click on the segmentation to export it to a model.</p>

---
