# Creating New Views using Cameras

**Topic ID**: 27959
**Date**: 2023-02-22
**URL**: https://discourse.slicer.org/t/creating-new-views-using-cameras/27959

---

## Post #1 by @brennachampion (2023-02-22 00:04 UTC)

<p>I am trying to create a second view using the “Cameras” module following the instructions given here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/cameras.html" class="inline-onebox" rel="noopener nofollow ugc">Cameras — 3D Slicer documentation</a><br>
But it doesn’t show “create new view” when I click the view pull-down menu. is there a reason for this? I am in the tabbed 3D layout as specified in the module instructions. Any guidance would be great. Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbe0d3e48ca808108c53149390f5d2f15bf7ea5e.png" data-download-href="/uploads/short-url/zWdxfeCbvwt69fk58De3STSQNfo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbe0d3e48ca808108c53149390f5d2f15bf7ea5e_2_690x380.png" alt="image" data-base62-sha1="zWdxfeCbvwt69fk58De3STSQNfo" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbe0d3e48ca808108c53149390f5d2f15bf7ea5e_2_690x380.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbe0d3e48ca808108c53149390f5d2f15bf7ea5e_2_1035x570.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbe0d3e48ca808108c53149390f5d2f15bf7ea5e_2_1380x760.png 2x" data-dominant-color="AFB3D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1785×985 59.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @schcat (2024-06-01 02:02 UTC)

<p>I also encountered this, it seems can’t added by GUI.<br>
You can add vtkMRMLViewNode by using python script or revising scene.mrml file.</p>

---

## Post #3 by @lassoan (2024-06-01 11:52 UTC)

<p>To simulate tool-mounted cameras (“first-person-shooter” style) or endoscopy procedures, I would recommend to use <code>Viewpoint</code> module in SlicerIGT repository or “Endoscopy” module in Slicer core.</p>

---
