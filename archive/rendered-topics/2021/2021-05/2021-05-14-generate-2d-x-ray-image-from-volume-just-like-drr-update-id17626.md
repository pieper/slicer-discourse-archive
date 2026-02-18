# Generate 2D X-ray image from volume, just like DRR...update?

**Topic ID**: 17626
**Date**: 2021-05-14
**URL**: https://discourse.slicer.org/t/generate-2d-x-ray-image-from-volume-just-like-drr-update/17626

---

## Post #1 by @jumbojing (2021-05-14 21:07 UTC)

<p>生成X线片就像DRR, 有没有更好的办法呢?<br>
我查了相关的讨论,更喜欢volume rendering的渲染方式,怎么通过python实现呢?</p>
<blockquote>
<p>jumbojing<br>
1m<br>
Generating X-rays is like DRR, is there a better way?<br>
I checked the related discussions, and I prefer the rendering method of volume rendering, how to achieve it through python?</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8ae9a294531a4804b85192d70dbe46d1c287e61.jpeg" data-download-href="/uploads/short-url/sDjzO93AgJ0eu1ZTUfURUOCQMDL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8ae9a294531a4804b85192d70dbe46d1c287e61_2_635x500.jpeg" alt="image" data-base62-sha1="sDjzO93AgJ0eu1ZTUfURUOCQMDL" width="635" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8ae9a294531a4804b85192d70dbe46d1c287e61_2_635x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8ae9a294531a4804b85192d70dbe46d1c287e61_2_952x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8ae9a294531a4804b85192d70dbe46d1c287e61_2_1270x1000.jpeg 2x" data-dominant-color="646462"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1662×1308 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2021-05-16 00:42 UTC)

<p>You can use the X-ray volume rendering preset. All necessary Python code snippets are listed in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">Slicer Script Repository</a>.</p>

---
