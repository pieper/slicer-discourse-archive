# Model LineWidth

**Topic ID**: 23330
**Date**: 2022-05-08
**URL**: https://discourse.slicer.org/t/model-linewidth/23330

---

## Post #1 by @Adam_Kalina (2022-05-08 02:05 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.10,4.11, 4.13<br>
Expected behavior: Models → Display → Slice display → Line Width should change size of line intersection with slice<br>
Actual behavior: works in 3D, in slice it stays the same - 1px = hard to see</p>
<p>Line created using</p>
<pre data-code-wrap="python"><code class="lang-python">line = vtk.vtkLineSource()
line.SetPoint1([0,0,0])
line.SetPoint2([30,30,30])
modelNode = slicer.modules.models.logic().AddModel(line.GetOutputPort())
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3b6ce086da93bddbf54fdb48eb2774b3fd8ab15.png" data-download-href="/uploads/short-url/nmhu55EeWZBtc4YpKQtp831cYhT.png?dl=1" title="obrazek" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3b6ce086da93bddbf54fdb48eb2774b3fd8ab15_2_690x488.png" alt="obrazek" data-base62-sha1="nmhu55EeWZBtc4YpKQtp831cYhT" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3b6ce086da93bddbf54fdb48eb2774b3fd8ab15_2_690x488.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3b6ce086da93bddbf54fdb48eb2774b3fd8ab15_2_1035x732.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3b6ce086da93bddbf54fdb48eb2774b3fd8ab15_2_1380x976.png 2x" data-dominant-color="929297"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">obrazek</span><span class="informations">1671×1183 77.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-05-08 04:19 UTC)

<p>The slice display → line width setting currently only sets line width. It does not affect point size.</p>
<p>Usually we set 2D intersection size by specifying a physical size for the line via a tube filter:</p>
<pre><code class="lang-python">line = vtk.vtkLineSource()
line.SetPoint1([0,0,0])
line.SetPoint2([30,30,30])
tube = vtk.vtkTubeFilter()
tube.SetInputConnection(line.GetOutputPort())
tube.SetNumberOfSides(4)
tube.SetRadius(1.5)
modelNode = slicer.modules.models.logic().AddModel(tube.GetOutputPort())
modelNode.GetDisplayNode().SetVisibility2D(True)
modelNode.GetDisplayNode().SetSliceIntersectionThickness(10)
</code></pre>
<p>Nevertheless, I can see that it could be intuitive to set intersection point size along with line size, so I’ve pushed a <a href="https://github.com/Slicer/Slicer/commit/adf8985966ad4ebcf5ef49fcc2ca8f15a95dceda">change</a> to make Slicer apply the slice intersection thickness to both points and lines. The update will be available in the Slicer Preview Release from Monday.</p>

---
