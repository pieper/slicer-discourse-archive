---
topic_id: 27737
title: "How To Find The Upper Direction Of Mesh Data Idea Task Refer"
date: 2023-02-10
url: https://discourse.slicer.org/t/27737
---

# How to find the upper-direction of mesh data ( idea , task, reference anything )

**Topic ID**: 27737
**Date**: 2023-02-10
**URL**: https://discourse.slicer.org/t/how-to-find-the-upper-direction-of-mesh-data-idea-task-reference-anything/27737

---

## Post #1 by @dsa934 (2023-02-10 06:51 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>I have several mesh data files (.ply), and the orientation of objects in these files is always random.</p>
<p>like this :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/757ac353c96ed48389f043def4cfef74819c12f0.png" data-download-href="/uploads/short-url/gLgSIwDqbQcXz283vSALVblGbGU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/757ac353c96ed48389f043def4cfef74819c12f0_2_690x368.png" alt="image" data-base62-sha1="gLgSIwDqbQcXz283vSALVblGbGU" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/757ac353c96ed48389f043def4cfef74819c12f0_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/757ac353c96ed48389f043def4cfef74819c12f0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/757ac353c96ed48389f043def4cfef74819c12f0.png 2x" data-dominant-color="F4F6F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">939×502 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>With the goal of having all meshes have the same ‘upper-direction’, I tried the following ideas.</p>
<ol>
<li>
<p>calculate mesh’s center point</p>
</li>
<li>
<p>get ‘inner-mesh’ from kD-tree</p>
</li>
<li>
<p>Find the point normals of the ‘inner-mesh’ and sum them all.</p>
</li>
</ol>
<pre><code class="lang-auto">
# make functions that find inner mesh 

# set mesh's center point

mesh_center_pos =[0,0,0]
node_in_scene = slicer.mrmlScene.GetNodesByClass('vtkMRMLModelNode')

for value in node_in_scene:
 node_name = value.GetName()

crown_node = getNode(node_name)
mesh = crown_node.GetMesh()


# make kdtree for mesh data
points = mesh.GetPoints()
k_Dtree = vtk.vtkKdTree()
k_Dtree.SetNumberOfRegionsOrMore(4)
k_Dtree.BuildLocatorFromPoints(points)


# cal mesh's center point 
for value in range(mesh.GetNumberOfPoints()):
 mesh_center_pos[0] += mesh.GetPoint(value)[0] 
 mesh_center_pos[1] += mesh.GetPoint(value)[1] 
 mesh_center_pos[2] += mesh.GetPoint(value)[2] 

mesh_center_pos[0] /= mesh.GetNumberOfPoints()
mesh_center_pos[1] /= mesh.GetNumberOfPoints()
mesh_center_pos[2] /= mesh.GetNumberOfPoints()

# current pos = [28.750410911221405, -4.0782514881915715, 26.817471450103564]
slicer.modules.markups.logic().AddControlPoint(mesh_center_pos[0], mesh_center_pos[1] , mesh_center_pos[2])

inner_mesh_id = vtk.vtkIdList()

k_Dtree.FindClosestNPoints( 3000, mesh_center_pos, inner_mesh_id)

inner_mesh_pos = [] 

# get nearest position's id 
for value in range(inner_mesh_id.GetNumberOfIds()):

 inner_mesh_pos.append( inner_mesh_id.GetId(value))

# draw nearest position via makrupsFiducialNode
for value in inner_mesh_pos:
 closet_pos = mesh.GetPoint(value)
 slicer.modules.markups.logic().AddControlPoint(closet_pos[0], closet_pos[1] , closet_pos[2])

</code></pre>
<p>However, the kD_tree.FindClosestNPoints() function has a problem because it requires directly specifying the number of points close to the reference point.</p>
<p>Therefore, I want to unify the case where the direction of the mesh data object is random. Is there a way to find the uppder-direction of the ojbect mesh?</p>

---

## Post #2 by @lassoan (2023-02-15 03:57 UTC)

<p>If the shape is always similar to your sketches then the “up” vector is the vector that connects the <em>center of the oriented bounding box</em> to the <em>center of gravity</em>. You can get both these center positions from Segment Statistics module.</p>

---
