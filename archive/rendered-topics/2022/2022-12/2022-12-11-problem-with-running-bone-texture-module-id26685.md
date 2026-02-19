---
topic_id: 26685
title: "Problem With Running Bone Texture Module"
date: 2022-12-11
url: https://discourse.slicer.org/t/26685
---

# Problem with Running Bone Texture Module

**Topic ID**: 26685
**Date**: 2022-12-11
**URL**: https://discourse.slicer.org/t/problem-with-running-bone-texture-module/26685

---

## Post #1 by @berke (2022-12-11 15:03 UTC)

<p>Hi everyone,<br>
I cropped a volume from a 0.075 mm voxel size CBCT scan and saved it as a .nrrd file. Then i opened the Bone Texture module and set the parameters according to the recommendation in the tutorial file.<br>
I clicked on both compute buttons but it’s not working. I don’t know what did i miss actually. Since there is no comprehensive tutorial videos about this module, i wanted to write this post.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0ca20f6bcb419348f3b63186a5fa784d8dd29d0.jpeg" data-download-href="/uploads/short-url/w4A0L8pO4UZwoBJZXT1I5nofdSw.jpeg?dl=1" title="Ekran Resmi 2022-12-11 ÖS 4.45.08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ca20f6bcb419348f3b63186a5fa784d8dd29d0_2_690x431.jpeg" alt="Ekran Resmi 2022-12-11 ÖS 4.45.08" data-base62-sha1="w4A0L8pO4UZwoBJZXT1I5nofdSw" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ca20f6bcb419348f3b63186a5fa784d8dd29d0_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ca20f6bcb419348f3b63186a5fa784d8dd29d0_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ca20f6bcb419348f3b63186a5fa784d8dd29d0_2_1380x862.jpeg 2x" data-dominant-color="9293A1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Resmi 2022-12-11 ÖS 4.45.08</span><span class="informations">1920×1200 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-12-11 16:17 UTC)

<p>Perhaps one of the developers of this extension will comment but if you don’t hear you can file and issue <a href="https://github.com/Kitware/BoneTextureExtension">on their repository</a>.  Also you may check the error log or python console.  I would guess it’s something to do with the small pixel spacing.</p>

---
