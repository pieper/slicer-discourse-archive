---
topic_id: 35921
title: "Issue With Contour Display In 3D Slicer"
date: 2024-05-05
url: https://discourse.slicer.org/t/35921
---

# Issue with Contour Display in 3D Slicer

**Topic ID**: 35921
**Date**: 2024-05-05
**URL**: https://discourse.slicer.org/t/issue-with-contour-display-in-3d-slicer/35921

---

## Post #1 by @wjd (2024-05-05 00:31 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87c5faa2ced035a78eb43b57b046d0642e16dc98.png" data-download-href="/uploads/short-url/jn6CQT6UtbzQqv0XGCrHslFk0jK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87c5faa2ced035a78eb43b57b046d0642e16dc98_2_690x221.png" alt="image" data-base62-sha1="jn6CQT6UtbzQqv0XGCrHslFk0jK" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87c5faa2ced035a78eb43b57b046d0642e16dc98_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87c5faa2ced035a78eb43b57b046d0642e16dc98_2_1035x331.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87c5faa2ced035a78eb43b57b046d0642e16dc98_2_1380x442.png 2x" data-dominant-color="393B3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1397×449 68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi everyone,</p>
<p>I recently encountered an issue when trying to open CT images and their corresponding RT structures, exported from MIM software version 7.0.10, in 3D Slicer version 5.6.1 with extension of Slicer RT (version: dbbdffd 2023-12-12).</p>
<p>The problem I’m facing is that when I load these files into 3D Slicer, zigzag lines appear for the ring contour around the body and skin. Additionally, the contour becomes opaque at certain slices. The image above is the body contour ring become opaque at certain slices. I’m puzzled by this behavior and wondering if anyone has encountered a similar issue or knows what might be causing it.</p>
<p>Any insights or suggestions on how to resolve this would be greatly appreciated. Thank you!</p>

---

## Post #2 by @cpinter (2024-05-05 14:53 UTC)

<p>Can you please check the planar contour representation?</p>
<p>The Representations section in the Segmentations module should look like this (make sure you select the correct segmentation on the top):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92dc87e65960fcb9f9a7eb2bdce25a8e941e723f.png" alt="image" data-base62-sha1="kXcc8VyaON1SqBgJm0tmBz0ismH" width="377" height="129"></p>
<p>Center the 3D view to make the segmentation show up (or find the reason why it does not show in 3D)/</p>
<p>Show the planar contour representation:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b581731dcd4c3947535f47bad44a3d4bc181614.png" alt="image" data-base62-sha1="jSH6iIdetHgs1zKjr5AgGV9mEpC" width="562" height="310"></p>
<p>You should see something like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a23fc96eea0c17a67e154bbb04076acae551723.png" alt="image" data-base62-sha1="cRq4yjpxoEVm9ZTrPncUgYWhEor" width="611" height="459"></p>
<p>If something is not right, please send us screenshots.</p>

---

## Post #3 by @wjd (2024-05-05 15:32 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13dd392590215dce1a9d2f3172d7b0e43a688cbf.png" data-download-href="/uploads/short-url/2PJ2vLrjkSFIhKlCC0Cu1bxqWjt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13dd392590215dce1a9d2f3172d7b0e43a688cbf_2_690x350.png" alt="image" data-base62-sha1="2PJ2vLrjkSFIhKlCC0Cu1bxqWjt" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13dd392590215dce1a9d2f3172d7b0e43a688cbf_2_690x350.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13dd392590215dce1a9d2f3172d7b0e43a688cbf_2_1035x525.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13dd392590215dce1a9d2f3172d7b0e43a688cbf_2_1380x700.png 2x" data-dominant-color="373534"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×974 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for your reply.</p>
<p>I made adjustments to ensure the 3D view displays correctly. The image above depicts the skin segmentation. However, zigzag lines are present, which deviate from the intended segmentation—a perfect ring surrounding the skin on the CT image. Additionally, while there should be a perfect ring visible, the entire section appears shaded instead.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cacce1716d8b998d2d0db129d6df0bddd0beca13.png" data-download-href="/uploads/short-url/sW3p25XjZRGNC4Tn8kO7dHvHYd5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/cacce1716d8b998d2d0db129d6df0bddd0beca13_2_690x347.png" alt="image" data-base62-sha1="sW3p25XjZRGNC4Tn8kO7dHvHYd5" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/cacce1716d8b998d2d0db129d6df0bddd0beca13_2_690x347.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/cacce1716d8b998d2d0db129d6df0bddd0beca13_2_1035x520.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/cacce1716d8b998d2d0db129d6df0bddd0beca13_2_1380x694.png 2x" data-dominant-color="363534"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×967 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The axial plane shown in the figure above is the actual segmentation.  I’ve noticed that the segmentation becomes shaded at certain slices when I navigate through slices (same problems existed on 3 planes) in 3D slicer.</p>
<p>I’m puzzled as to why this zigzag line and distortion are occurring. Any further insights or suggestions would be greatly appreciated.</p>

---

## Post #4 by @cpinter (2024-05-06 08:20 UTC)

<p>I was trying to help figure out the root cause of the issue. If the lines appear correctly, then the original representation in the file is right, and the problem is in the conversion. It would be useful to know this.</p>

---
