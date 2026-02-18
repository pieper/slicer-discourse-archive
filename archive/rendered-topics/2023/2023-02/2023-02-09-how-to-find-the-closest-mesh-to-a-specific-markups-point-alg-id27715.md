# How to find the closest mesh to a specific markups point (algorithm , idea )

**Topic ID**: 27715
**Date**: 2023-02-09
**URL**: https://discourse.slicer.org/t/how-to-find-the-closest-mesh-to-a-specific-markups-point-algorithm-idea/27715

---

## Post #1 by @dsa934 (2023-02-09 04:25 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>hi Slicer users</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93322a162c74d175824394fa25daa2617e64104c.png" data-download-href="/uploads/short-url/l09FdPHkG0szAPnUUj9C0v3fv88.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93322a162c74d175824394fa25daa2617e64104c_2_690x438.png" alt="image" data-base62-sha1="l09FdPHkG0szAPnUUj9C0v3fv88" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93322a162c74d175824394fa25daa2617e64104c_2_690x438.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93322a162c74d175824394fa25daa2617e64104c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93322a162c74d175824394fa25daa2617e64104c.png 2x" data-dominant-color="F2F1F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">884×562 43.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I want to get only the position value of the inner mesh closest to the center point of this mesh. Can anyone recommend an idea or algorithm?</p>

---

## Post #2 by @RafaelPalomar (2023-02-09 05:12 UTC)

<p>Assuming that the center point will always be closer to the inner mesh than to the outer mesh (or if your mesh has been splitted/segmented beforehand), you could build a KD-Tee (<a href="https://vtk.org/doc/nightly/html/classvtkKdTree.html" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkKdTree Class Reference</a>) and query the tree for the closest point (<a href="https://vtk.org/doc/nightly/html/classvtkKdTree.html#af5cabd7f0482765792d376ca70b25dd8" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkKdTree Class Reference</a>). A C++ example of this can be found here (<a href="https://kitware.github.io/vtk-examples/site/Cxx/DataStructures/KdTree/" rel="noopener nofollow ugc">https://kitware.github.io/vtk-examples/site/Cxx/DataStructures/KdTree/</a>). This example is easily translatable to python and can be used within Slicer.</p>

---

## Post #4 by @dsa934 (2023-02-09 07:38 UTC)

<p>Hi again <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a></p>
<p>I implemented what you said in Python, but as a result, it seems that only one mesh point closest to the center point is obtained.</p>
<p>Is there any way to get all points of the inner mesh?</p>
<pre><code class="lang-auto"># set kD-tree via mesh 
mesh_center_pos =[0,0,0]
node_in_scene = slicer.mrmlScene.GetNodesByClass('vtkMRMLModelNode')

for value in node_in_scene:

 node_name = value.GetName()

crown_node = getNode(node_name)
mesh = crown_node.GetMesh()

# make kdtree for mesh data
points = mesh.GetPoints()
k_Dtree = vtk.vtkKdTree()
k_Dtree.BuildLocatorFromPoints(points)

# cal mesh's center point 
for value in range(mesh.GetNumberOfPoints()):
 mesh_center_pos[0] += mesh.GetPoint(value)[0] 
 mesh_center_pos[1] += mesh.GetPoint(value)[1] 
 mesh_center_pos[2] += mesh.GetPoint(value)[2] 

mesh_center_pos[0] /= mesh.GetNumberOfPoints()
mesh_center_pos[1] /= mesh.GetNumberOfPoints()
mesh_center_pos[2] /= mesh.GetNumberOfPoints()

# check mesh's center point
slicer.modules.markups.logic().AddControlPoint(mesh_center_pos[0], mesh_center_pos[1] , mesh_center_pos[2])

p_distance = vtk.reference(0.5)
inner_mesh_pos = k_Dtree.FindClosestPoint( mesh_center_pos, p_distance)

closet_pos = mesh.GetPoint(inner_mesh_pos)
# check closet point from mesh's center point
slicer.modules.markups.logic().AddControlPoint(closet_pos[0], closet_pos[1] , closet_pos[2])

</code></pre>

---

## Post #5 by @RafaelPalomar (2023-02-09 11:32 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="4" data-topic="27715">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>Is there any way to get all points of the inner mesh?</p>
</blockquote>
</aside>
<p>You could use vtkKDTree to query for <em>N closest points</em> (<a href="https://vtk.org/doc/nightly/html/classvtkKdTree.html#af5cabd7f0482765792d376ca70b25dd8" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkKdTree Class Reference</a>) or even find <em>points within a radius</em> (<a href="https://vtk.org/doc/nightly/html/classvtkKdTree.html#a7dc6bd5104cb90f333f0985e6f142446" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkKdTree Class Reference</a>)</p>
<p>If you want to discriminate what you call “inner mesh” and “outer mesh”, you probably need to be more specific about what criteria these points should meet to be considered inner or outer; with arbitrary geometries, I would think distance alone won’t be sufficient.</p>

---
