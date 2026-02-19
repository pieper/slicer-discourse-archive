---
topic_id: 29532
title: "How To Make Markupsnode Follow Mouse Cursor"
date: 2023-05-18
url: https://discourse.slicer.org/t/29532
---

# How to make markupsnode follow mouse cursor

**Topic ID**: 29532
**Date**: 2023-05-18
**URL**: https://discourse.slicer.org/t/how-to-make-markupsnode-follow-mouse-cursor/29532

---

## Post #1 by @dsa934 (2023-05-18 15:27 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e67a278d6deb99a1b56d1941ec87d94df9abf08e.png" data-download-href="/uploads/short-url/wSTx2UIJzxdOb6K2oRh6XpgFJXU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e67a278d6deb99a1b56d1941ec87d94df9abf08e_2_690x351.png" alt="image" data-base62-sha1="wSTx2UIJzxdOb6K2oRh6XpgFJXU" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e67a278d6deb99a1b56d1941ec87d94df9abf08e_2_690x351.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e67a278d6deb99a1b56d1941ec87d94df9abf08e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e67a278d6deb99a1b56d1941ec87d94df9abf08e.png 2x" data-dominant-color="626684"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">984×501 19.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fc04c3a4670238d2c78c800ce9013046d92aca2.png" alt="image" data-base62-sha1="fWAZHQZ7OmfJEJhuROktxHjgtO2" width="471" height="130"><br>
When you click on the markup node above in Slicer’s GUI interface, the markup node will follow the mouse cursor until it generates a mouse click event in the 3D view. How can I implement this in code?</p>

---

## Post #2 by @lassoan (2023-05-18 18:37 UTC)

<p>What you describe is already the current behavior. What do you mean by how can you implement it? Do you want to reimplement the feature in another application?</p>

---

## Post #3 by @dsa934 (2023-05-18 23:55 UTC)

<p>I think slicers have loose cell, point picker functions.</p>
<p>What I mean is, when I create a markupNode on the mesh, visually it looks like the markupNode is attached to the mesh, but when I actually create a 3d point cloud and check it, I can see that the distance between the mesh and the markupnode is not zero.</p>
<p>So I’m trying to add an algorithm that makes this distance difference zero by utilizing OBBtree, vtkPointPicker, vtkCellPicker, etc.</p>
<p>Therefore, when rendering on the 3D view by selecting one of the Markupnodes through the GUI, we are trying to add a condition that prevents rendering if the mesh and markupsnode are separated.</p>

---

## Post #4 by @lassoan (2023-05-19 02:05 UTC)

<p>When you place a markup point on a visible surface, it is placed exactly on the surface.</p>
<p>You talk about point clouds. Maybe you expect the point to snap to a mesh point? We don’t do that because a mesh can have huge cells, so the point would be placed very inaccurately. In general, if you have a mesh then use it as a mesh; treating it as a point cloud would be a huge downgrade (you would discard very valuable information).</p>
<p>If you can provide a script and instructions that reproduces some unexpected behavior then we can investigate.</p>

---

## Post #5 by @dsa934 (2023-05-19 16:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fd9582cf8d963598ae2d3488733a1eb2bedab12.png" data-download-href="/uploads/short-url/6Pi6aa7qItjEJs6OqxJxosLCT1U.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fd9582cf8d963598ae2d3488733a1eb2bedab12_2_278x500.png" alt="image" data-base62-sha1="6Pi6aa7qItjEJs6OqxJxosLCT1U" width="278" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fd9582cf8d963598ae2d3488733a1eb2bedab12_2_278x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fd9582cf8d963598ae2d3488733a1eb2bedab12_2_417x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fd9582cf8d963598ae2d3488733a1eb2bedab12.png 2x" data-dominant-color="363839"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">501×900 22.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you take a control point on the Mesh (Stanford Bunny) through ClosedCurveNode, there is a line connected by a curve between the control points.</p>
<p>For ClosedCurveNode, if you proceed with the ‘Resampling’ process through the options shown in the picture above, another control point is interpolated on the curve between the control points.</p>
<p>Are the options specified in the picture above resampling while ensuring that even the curves between the control points are attached to the mesh?</p>
<p>The point cloud mentioned above is what I said wrong. During the ClosedCurveNode Resampling process, there seems to be a phenomenon in which the newly created control point is not attached to the mesh. Is there an option to set this inside the slicer?</p>
<p>I am picking with the IntersectWithLine function through the OBBTree for the mesh, and I am wondering if there is another method other than the above method.</p>

---
