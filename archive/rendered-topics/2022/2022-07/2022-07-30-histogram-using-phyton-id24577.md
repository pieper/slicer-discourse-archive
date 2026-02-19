---
topic_id: 24577
title: "Histogram Using Phyton"
date: 2022-07-30
url: https://discourse.slicer.org/t/24577
---

# Histogram using Phyton 

**Topic ID**: 24577
**Date**: 2022-07-30
**URL**: https://discourse.slicer.org/t/histogram-using-phyton/24577

---

## Post #1 by @Jessica (2022-07-30 14:26 UTC)

<p>Hello, I have zero experience in 3D slicer or coding<br>
I am actually MD<br>
I am working on project and was able to segment the pituitary from Segment editor then calculate the volume using Statistics<br>
Need to get a grayscale histogram for the segment portion aka the pituitary<br>
Can someone please help to guide me from scratch ?</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2022-07-30 19:12 UTC)

<p>Fortunately there is a an example for what you need.  Paste it in slicer and you should get the image below.  You can customize to work with your data and for that you will need to learn some python.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a547e311cc510604c63dadc12608ae860be0708c.jpeg" data-download-href="/uploads/short-url/nA8NAotUB3urlwXc9ilkJWeXvxa.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a547e311cc510604c63dadc12608ae860be0708c_2_690x439.jpeg" alt="image" data-base62-sha1="nA8NAotUB3urlwXc9ilkJWeXvxa" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a547e311cc510604c63dadc12608ae860be0708c_2_690x439.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a547e311cc510604c63dadc12608ae860be0708c_2_1035x658.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a547e311cc510604c63dadc12608ae860be0708c.jpeg 2x" data-dominant-color="797984"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1096×698 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
