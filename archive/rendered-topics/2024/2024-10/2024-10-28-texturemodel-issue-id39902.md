---
topic_id: 39902
title: "Texturemodel Issue"
date: 2024-10-28
url: https://discourse.slicer.org/t/39902
---

# TextureModel Issue

**Topic ID**: 39902
**Date**: 2024-10-28
**URL**: https://discourse.slicer.org/t/texturemodel-issue/39902

---

## Post #1 by @Jack95 (2024-10-28 20:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eaa16ee0a056623ae8d967c24270815611a1b4b.png" data-download-href="/uploads/short-url/6EOnulFJgw6jS0ULREyJ8bJpFHl.png?dl=1" title="texture model pane" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eaa16ee0a056623ae8d967c24270815611a1b4b_2_690x319.png" alt="texture model pane" data-base62-sha1="6EOnulFJgw6jS0ULREyJ8bJpFHl" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eaa16ee0a056623ae8d967c24270815611a1b4b_2_690x319.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eaa16ee0a056623ae8d967c24270815611a1b4b_2_1035x478.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eaa16ee0a056623ae8d967c24270815611a1b4b_2_1380x638.png 2x" data-dominant-color="ADB0D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">texture model pane</span><span class="informations">1714×793 96.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello all,</p>
<p>I am running into an issue trying to apply textures to my 3D models (mainly to assist in landmarking). Previously (a few months ago) I had no problem applying these same textures in 3D slicer using the TextureModel function from SlicerIGT. However, and perhaps this is just a usage error, when I load my data into Slicer the panel seemingly does not provide me any options. My model is loaded in (.obj format) and my texture loaded as a volume (.png and .jpg have been tried). Am I missing something obvious?</p>
<p>Thanks!<br>
Jack</p>

---

## Post #2 by @Jack95 (2024-10-28 20:59 UTC)

<p>Solved after the new update (10/28/2024)</p>

---

## Post #3 by @muratmaga (2024-10-28 21:31 UTC)

<p>If you have the slicermorph extension installed, you can probably skip TextureModel function, if your models are in OBJ format. When you drag and drop your model into Slicer, instead of default data type Model, choose Textured OBJ Model.</p>

---
