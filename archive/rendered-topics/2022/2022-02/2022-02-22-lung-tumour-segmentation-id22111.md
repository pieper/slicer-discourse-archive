---
topic_id: 22111
title: "Lung Tumour Segmentation"
date: 2022-02-22
url: https://discourse.slicer.org/t/22111
---

# Lung tumour segmentation

**Topic ID**: 22111
**Date**: 2022-02-22
**URL**: https://discourse.slicer.org/t/lung-tumour-segmentation/22111

---

## Post #1 by @ni5h (2022-02-22 12:09 UTC)

<p>Hi, for complex lung tumours, other than grow from seeds and fill between slices etc, is there an extension that can annotate a lung tumours? I have found completing this via GfS as not very accurate - imaging dataset is routine but I was hoping there is an extension whereby it would assist in segmenting the tumour only</p>

---

## Post #2 by @rbumm (2022-02-22 17:54 UTC)

<p>Hi, there is no specialized extension for advanced lung tumor segmentation yet.<br>
Try the “Surface Cut” Segment Editor effect and settings like this (Slicer 4.13):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dabab0c20505462fa30c4740fa04b45f8d6a8df1.png" data-download-href="/uploads/short-url/vcY4p1cFNKQBjC7Vjh9GCiyD9M5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dabab0c20505462fa30c4740fa04b45f8d6a8df1_2_485x500.png" alt="image" data-base62-sha1="vcY4p1cFNKQBjC7Vjh9GCiyD9M5" width="485" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dabab0c20505462fa30c4740fa04b45f8d6a8df1_2_485x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dabab0c20505462fa30c4740fa04b45f8d6a8df1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dabab0c20505462fa30c4740fa04b45f8d6a8df1.png 2x" data-dominant-color="EFF0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">600×618 46.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You would place your markups around the complex tumor <em>in the healthy lung tissue and along the chest wall, if the tumor is adjacent</em>, press “Apply” and get a reasonable/good result (can´t show the segmentation result for privacy reasons).</p>

---

## Post #3 by @ni5h (2022-02-22 19:48 UTC)

<p>Thank you for your suggestion, however, for complex tumours where the tumour can be impeding into the aorta and adjacent areas, the process is particularly slow. I have tried nvidia ai assisted ct lung covid 19 to see if this offers a solution but it does not work, even the lung ct segmenter cuptures the lung well but not the tumour, maybe I can work out if I can integrate lung ct segmenter and see if i can find a way to threshold the tumour after this. I will try. Thanks</p>

---

## Post #4 by @rbumm (2022-02-22 20:04 UTC)

<p>I am planning to integrate lung lesion segmentation into the Lung CT Segmenter later this year.  If you identify a good workflow please let me know.</p>

---

## Post #5 by @lassoan (2022-02-23 00:57 UTC)

<p><a class="mention" href="/u/ni5h">@ni5h</a> If you can share an anonymized data set (upload somewhere and post the link) then we can help developing a quick and accurate segmentation workflow for it.</p>

---
