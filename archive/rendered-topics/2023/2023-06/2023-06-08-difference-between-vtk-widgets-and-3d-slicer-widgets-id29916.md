# Difference between VTK widgets and 3D Slicer widgets

**Topic ID**: 29916
**Date**: 2023-06-08
**URL**: https://discourse.slicer.org/t/difference-between-vtk-widgets-and-3d-slicer-widgets/29916

---

## Post #1 by @mazurkin.daniel (2023-06-08 11:03 UTC)

<p>Hello, what’s the difference between VTK widgets and 3D Slicer widgets in terms of rendering? When trying to compile to wasm, the vtk widget is successfully displayed, when trying to get the widget from the 3D Slicer, WebGL gives errors with shaders. I try get LineWidget from VTK (success in web assembly) and 3D Slicer (not success in web assembly). Thanks in advance for your reply.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fcd15b9ae00db8a529b4d0bad2ec09c3719f546.png" data-download-href="/uploads/short-url/dFuKCDT7uNTE2e1dm0DW0M9kj0a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fcd15b9ae00db8a529b4d0bad2ec09c3719f546_2_690x354.png" alt="image" data-base62-sha1="dFuKCDT7uNTE2e1dm0DW0M9kj0a" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fcd15b9ae00db8a529b4d0bad2ec09c3719f546_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fcd15b9ae00db8a529b4d0bad2ec09c3719f546_2_1035x531.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fcd15b9ae00db8a529b4d0bad2ec09c3719f546_2_1380x708.png 2x" data-dominant-color="C9C6B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×987 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e578b99362a7726367ae354ab0c91377e0ba2430.jpeg" data-download-href="/uploads/short-url/wJZZxK7dhMe1v2P8rj4c5Lmh1oA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e578b99362a7726367ae354ab0c91377e0ba2430_2_690x351.jpeg" alt="image" data-base62-sha1="wJZZxK7dhMe1v2P8rj4c5Lmh1oA" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e578b99362a7726367ae354ab0c91377e0ba2430_2_690x351.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e578b99362a7726367ae354ab0c91377e0ba2430_2_1035x526.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e578b99362a7726367ae354ab0c91377e0ba2430_2_1380x702.jpeg 2x" data-dominant-color="7976A3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×979 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-06-16 14:56 UTC)

<p>The main difference is that Slicer widgets represent MRML nodes, while VTK widgets represent VTK objects.</p>

---
