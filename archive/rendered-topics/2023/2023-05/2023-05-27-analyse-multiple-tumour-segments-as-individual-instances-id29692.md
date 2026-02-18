# Analyse multiple tumour segments as individual instances

**Topic ID**: 29692
**Date**: 2023-05-27
**URL**: https://discourse.slicer.org/t/analyse-multiple-tumour-segments-as-individual-instances/29692

---

## Post #1 by @nasibov_98 (2023-05-27 21:14 UTC)

<p>Hi, I have labeled the multiple tumours present in an MRI image as “Tumour”. Tumour pixels all have the label value of 2.</p>
<p>Here are the multiple tumour segmentations.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afd5e1dbc2b6ad7f57e4a1614217cd5dd18b5590.png" data-download-href="/uploads/short-url/p5vNtljB2WnBKOy4vx9TwaOa8qk.png?dl=1" title="statistics displayed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd5e1dbc2b6ad7f57e4a1614217cd5dd18b5590_2_690x333.png" alt="statistics displayed" data-base62-sha1="p5vNtljB2WnBKOy4vx9TwaOa8qk" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd5e1dbc2b6ad7f57e4a1614217cd5dd18b5590_2_690x333.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd5e1dbc2b6ad7f57e4a1614217cd5dd18b5590_2_1035x499.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd5e1dbc2b6ad7f57e4a1614217cd5dd18b5590_2_1380x666.png 2x" data-dominant-color="62605A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">statistics displayed</span><span class="informations">1380×666 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c91d3e66d76b9d418a533bf4beffbcbebe596de4.png" alt="Volume and segments" data-base62-sha1="sH8COq7sMY7J6jLOgb3E5pqoIlu" width="438" height="376"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a410503e042bc10a48357d2c91bba3538b9d52c.png" alt="3D reconstruction of tumour segments" data-base62-sha1="hrvyqhBjhZqxb55JngtoRyjZ03G" width="422" height="340"></p>
<p><strong>I would like the “segment statistics” module to report on each tumour separately.</strong> Is there a quick method of "splitting " these tumours up into separate instances? On 2D images of cells, I have used “regionprops” in python, which  finds groups of pixels and considers them a unique entity, is there something similar for 3D segmentations???</p>
<p>I have many images with multiple tumours, it would take too long for me to segment them all with separate values.</p>
<p>Operating system:Mac OS<br>
Slicer version: 5.2.2</p>

---

## Post #2 by @pieper (2023-05-27 22:10 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#islands">the Islands</a> tool with the “Split islands to segments” option.</p>

---

## Post #3 by @nasibov_98 (2023-05-28 11:15 UTC)

<p>Thank you! That was a lot simpler than I expected.</p>
<p>Cheers</p>

---
