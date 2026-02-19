---
topic_id: 40035
title: "Image Calculator"
date: 2024-11-05
url: https://discourse.slicer.org/t/40035
---

# Image calculator

**Topic ID**: 40035
**Date**: 2024-11-05
**URL**: https://discourse.slicer.org/t/image-calculator/40035

---

## Post #1 by @ashkanpakzad (2024-11-05 11:46 UTC)

<p>Hi all,</p>
<p>My first post, thanks for all the good work. I’m keen to get involved.</p>
<p>I was wondering if anyone has developed in Slicer something like ImageJ/FIJI’s ‘image calculator’?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af44e8779061d8e5ddad9d1067ce183c3f41b56d.jpeg" data-download-href="/uploads/short-url/p0vbUNX0n7qrJcMEBvNepJoeDO5.jpeg?dl=1" title="images" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af44e8779061d8e5ddad9d1067ce183c3f41b56d.jpeg" alt="images" data-base62-sha1="p0vbUNX0n7qrJcMEBvNepJoeDO5" width="270" height="258"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">images</span><span class="informations">270×258 10.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Which would allow the user to manipulate images by mathematical operators with a scalar or image? (I appreciate image and image operations are not necessarily trivial e.g. different array sizes and orientations etc.)</p>
<p>I suppose users with know-how would just do this programmatically.</p>
<p>I’m only so far aware of a module that allows to multiply 2 images together “Multiply Scalar Volumes”.</p>
<p>If it dosen’t exist, I would make a mock up. is it something that the community would consider useful?</p>
<p>Cheers,<br>
Ashkan</p>

---

## Post #2 by @pieper (2024-11-05 13:12 UTC)

<p>There are several modules like this in Slicer.  Let us know if there’s a specific operation you can’t find.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86734c5382bbb6357ed155a8f66a9ed7c0fae680.jpeg" data-download-href="/uploads/short-url/jbp0nMehl22hpa6YVibzxr7bjnG.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86734c5382bbb6357ed155a8f66a9ed7c0fae680_2_690x277.jpeg" alt="image" data-base62-sha1="jbp0nMehl22hpa6YVibzxr7bjnG" width="690" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86734c5382bbb6357ed155a8f66a9ed7c0fae680_2_690x277.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86734c5382bbb6357ed155a8f66a9ed7c0fae680_2_1035x415.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86734c5382bbb6357ed155a8f66a9ed7c0fae680_2_1380x554.jpeg 2x" data-dominant-color="AEB0B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1676×674 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>SimpleFilters exposes a huge list of operations.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b84695f28b3074c134cd9655456fd655f54edb5.png" data-download-href="/uploads/short-url/mbLHiXNLnV7ZSCIaeXTxuLFpgax.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b84695f28b3074c134cd9655456fd655f54edb5_2_410x500.png" alt="image" data-base62-sha1="mbLHiXNLnV7ZSCIaeXTxuLFpgax" width="410" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b84695f28b3074c134cd9655456fd655f54edb5_2_410x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b84695f28b3074c134cd9655456fd655f54edb5_2_615x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b84695f28b3074c134cd9655456fd655f54edb5_2_820x1000.png 2x" data-dominant-color="E0E2E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">960×1168 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @ashkanpakzad (2024-11-05 23:16 UTC)

<p>This is great thank you and I can see exposes SimpleITK filters for image and image operations. However, it dosent seem to allow image and scalar operations e.g. <code>Image * 10</code>.</p>
<p>Though it appears possible by the <a href="https://simpleitk.org/doxygen/v2_4/html/classitk_1_1simple_1_1MultiplyImageFilter.html" rel="noopener nofollow ugc">documentation</a> <code>Execute (const Image &amp;image1, double constant)</code></p>

---

## Post #4 by @muratmaga (2024-11-05 23:45 UTC)

<p>Most people use python for that:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-noise-to-image" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-noise-to-image</a></p>

---
