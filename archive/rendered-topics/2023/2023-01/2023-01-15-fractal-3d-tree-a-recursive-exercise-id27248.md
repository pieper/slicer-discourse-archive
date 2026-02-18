# Fractal 3D Tree (a Recursive Exercise)

**Topic ID**: 27248
**Date**: 2023-01-15
**URL**: https://discourse.slicer.org/t/fractal-3d-tree-a-recursive-exercise/27248

---

## Post #1 by @jumbojing (2023-01-15 10:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fa275ae0d6d17918716058b33d8ffb443d75f88.png" data-download-href="/uploads/short-url/fVz4brK4R7HJnim3thAC8FpFDrW.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fa275ae0d6d17918716058b33d8ffb443d75f88_2_473x500.png" alt="图片" data-base62-sha1="fVz4brK4R7HJnim3thAC8FpFDrW" width="473" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fa275ae0d6d17918716058b33d8ffb443d75f88_2_473x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fa275ae0d6d17918716058b33d8ffb443d75f88.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fa275ae0d6d17918716058b33d8ffb443d75f88.png 2x" data-dominant-color="9D9DAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">514×543 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/225c60d6a028a705dbbff674f9c3c82202bef90e.png" data-download-href="/uploads/short-url/4TY9wc2Y8UHIEIf6jArISwKvthk.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/225c60d6a028a705dbbff674f9c3c82202bef90e_2_568x500.png" alt="图片" data-base62-sha1="4TY9wc2Y8UHIEIf6jArISwKvthk" width="568" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/225c60d6a028a705dbbff674f9c3c82202bef90e_2_568x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/225c60d6a028a705dbbff674f9c3c82202bef90e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/225c60d6a028a705dbbff674f9c3c82202bef90e.png 2x" data-dominant-color="9897A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">592×521 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70a248a3da307d73420c11e660b5aa058f306921.png" data-download-href="/uploads/short-url/g4papSeFwf6l55wvRWzhP5CXI1b.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70a248a3da307d73420c11e660b5aa058f306921_2_528x500.png" alt="图片" data-base62-sha1="g4papSeFwf6l55wvRWzhP5CXI1b" width="528" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70a248a3da307d73420c11e660b5aa058f306921_2_528x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70a248a3da307d73420c11e660b5aa058f306921.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70a248a3da307d73420c11e660b5aa058f306921.png 2x" data-dominant-color="9392A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">638×604 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Just kidding…</p>

---

## Post #2 by @RafaelPalomar (2023-01-16 06:36 UTC)

<p>This type synthetic data could be useful for algorithm testing. Just out of curiosity, how did you generate it? Did you use 3D Slicer for the generation?</p>

---

## Post #3 by @jumbojing (2023-01-16 16:22 UTC)

<p>用python代码, 点到点产生棱柱, 继而以棱柱末端的点(这里是三棱柱-三个点)为起点, 以一定方向和距离再做棱柱, 如此递归…做了6层(3**6), 末端的棱柱中点插入mark点, , ,</p>
<p>完成6层递归(产生将近1000个圆柱和728个markups点), 要花费20多分钟…</p>
<blockquote>
<p>Use python code in Slicer : generate a cylinder(<code>vtkcylindersource</code>) from point to point at first, and then use those points at the end of the cylinder (here is a triangular prism - three points) as starting points, and then make other cylinders in a certain direction and distance, so recursive Six layers (3 * * 6) are made, and the midpoints of the cylinders at the end is inserted into the <code>MarkupsFiducial</code>.</p>
</blockquote>
<blockquote>
<p>It takes more than 20 minutes to complete 6 layers of recursion (generating nearly 1000 cylinders and 728 markups points)…</p>
</blockquote>

---
