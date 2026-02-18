# Adding reference grid in 3D view

**Topic ID**: 29707
**Date**: 2023-05-29
**URL**: https://discourse.slicer.org/t/adding-reference-grid-in-3d-view/29707

---

## Post #1 by @q2577040659 (2023-05-29 10:00 UTC)

<p>I want to add a grid like the one in the picture to the 3D view.<br>
The grid can be scaled as the view is scaled.<br>
But the grid cannot be rotated or moved.<br>
Please tell me what to do,  Thank.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cb45be50c5c561f692f7c542d67c6b30391913e.png" alt="85478906a7e3916cce1c1580bbc347d" data-base62-sha1="45VMLbSX1MnQMcoXODINUuj0vZc" width="548" height="306"></p>

---

## Post #2 by @lassoan (2023-05-30 02:36 UTC)

<p>We provide a reference grid for transformvisualization. You can specify the grid size in mm and so it is properly scaled and it is shown in both slice and 3D views. However, I think it does not do exactly what you describe because in 3D we display a 3D grid not a 2D grid:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28b4887b3937ee8ddaeb33090785d2c3dacfce1e.jpeg" data-download-href="/uploads/short-url/5O5T8kTYRUOeZ8szEscYmDD9VqC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28b4887b3937ee8ddaeb33090785d2c3dacfce1e_2_690x415.jpeg" alt="image" data-base62-sha1="5O5T8kTYRUOeZ8szEscYmDD9VqC" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28b4887b3937ee8ddaeb33090785d2c3dacfce1e_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28b4887b3937ee8ddaeb33090785d2c3dacfce1e_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28b4887b3937ee8ddaeb33090785d2c3dacfce1e_2_1380x830.jpeg 2x" data-dominant-color="3D3B3B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1157 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you have C++ programming experience it would not be hard to copy the reference grid display from the 2D transform displayable manager](<a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Transforms/MRMLDM/vtkMRMLTransformsDisplayableManager2D.cxx" class="inline-onebox">Slicer/vtkMRMLTransformsDisplayableManager2D.cxx at main · Slicer/Slicer · GitHub</a>), in 3D it could be implemented similarly to how the ruler is displayed (it gets scaling from the main renderer, but it displays the 2D line always in the camera plane):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccb4b8c4e2e0a6dbb35b724c40cd83e421766ebf.jpeg" data-download-href="/uploads/short-url/tcUB6NSvKYJSYYOrN7ExpLCQtQj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccb4b8c4e2e0a6dbb35b724c40cd83e421766ebf_2_566x499.jpeg" alt="image" data-base62-sha1="tcUB6NSvKYJSYYOrN7ExpLCQtQj" width="566" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccb4b8c4e2e0a6dbb35b724c40cd83e421766ebf_2_566x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccb4b8c4e2e0a6dbb35b724c40cd83e421766ebf_2_849x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccb4b8c4e2e0a6dbb35b724c40cd83e421766ebf_2_1132x998.jpeg 2x" data-dominant-color="3D3732"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1372×1211 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>That said, using reference grid for measurement has many shortcomings compared to direct measurements (using markups line, curve, etc.), such as:</p>
<ul>
<li>approximate visual alignment with grid lines is less accurate and more error-prone (you may make a mistake when counting grid points or when you write down the results)</li>
<li>no evidence of the measurement is preserved, therefore if you need to later review the results you don’t know if inaccuracy is due to incorrectly identifying landmark points, inaccurately aligning grid lines, or incorrectly counting grid points</li>
</ul>
<p>Therefore, I would recommend to use markups for measurements instead of spending time with implementing a less reliable measurement solution. If you have questions on how to do your measurements using markups then let us know.</p>

---

## Post #3 by @q2577040659 (2023-05-30 02:43 UTC)

<p>That’s taken care of, thank you.</p>

---

## Post #4 by @lassoan (2023-05-30 19:32 UTC)

<p>What did you end up doing?</p>

---
