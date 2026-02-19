---
topic_id: 36725
title: "Model Alignment To World Coordinate System"
date: 2024-06-12
url: https://discourse.slicer.org/t/36725
---

# Model alignment to world coordinate system

**Topic ID**: 36725
**Date**: 2024-06-12
**URL**: https://discourse.slicer.org/t/model-alignment-to-world-coordinate-system/36725

---

## Post #1 by @Julian_KC (2024-06-12 14:19 UTC)

<p>Hello,</p>
<p>I’m a paleontologist working with surface model bones, and I need all my models to follow a certain alignment for analysis purposes.</p>
<p>I’m wondering if it’s possible to align a certain markup line to the world axis or to align certain points to the origin of the world?</p>
<p>Thank you so much in advance for your answer!</p>
<p>Julian KC</p>

---

## Post #2 by @muratmaga (2024-06-12 15:57 UTC)

<aside class="quote no-group" data-username="Julian_KC" data-post="1" data-topic="36725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julian_kc/48/18359_2.png" class="avatar"> Julian_KC:</div>
<blockquote>
<p>need all my models to follow a certain alignment for analysis purposes.</p>
</blockquote>
</aside>
<p>This is doable in many ways, couple easy options are:</p>
<ol>
<li>
<p>Create a transform from set of points on a reference and target (ie., fiducial registration).</p>
</li>
<li>
<p>You can do it manually by using the interaction widget of the Transforms module.</p>
</li>
</ol>
<aside class="quote no-group" data-username="Julian_KC" data-post="1" data-topic="36725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julian_kc/48/18359_2.png" class="avatar"> Julian_KC:</div>
<blockquote>
<p>I’m wondering if it’s possible to align a certain markup line to the world axis or to align certain points to the origin of the world?</p>
</blockquote>
</aside>
<p>Do you want to do this interactively (using GUI) or from a python script? For GUI you can use the manual options I described above… Programmatically there might be some examples in Python script repository.</p>
<p>If you can give some examples (screenshots of what you are trying to do), it would be easier to give more concrete answers.</p>

---

## Post #3 by @Julian_KC (2024-06-13 13:58 UTC)

<p>Thank you very much for your prompt response.</p>
<ol>
<li>
<p>I apologize for not being clear earlier. I cannot manually align my models as it isn’t accurate enough for my needs.</p>
</li>
<li>
<p>I don’t mind whether it’s done with or without a GUI. I’m currently learning Python, so it would be great to use it for this task and enhance my skills.</p>
</li>
</ol>
<p>You can see exactly what I want to achieve in the first image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b202b1e342d879c662a1955be08b9d51f09268.jpeg" data-download-href="/uploads/short-url/sDqSyh9l4EqJtTJdF2OFN7W2l2E.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8b202b1e342d879c662a1955be08b9d51f09268_2_690x359.jpeg" alt="image" data-base62-sha1="sDqSyh9l4EqJtTJdF2OFN7W2l2E" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8b202b1e342d879c662a1955be08b9d51f09268_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8b202b1e342d879c662a1955be08b9d51f09268_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8b202b1e342d879c662a1955be08b9d51f09268_2_1380x718.jpeg 2x" data-dominant-color="C9C9CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1474×768 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li>First, set the red point as the origin of the world coordinates (0,0,0).</li>
<li>Then, set the green line as the Z-axis of the world coordinates.</li>
</ol>
<p>The second image shows exactly what I want, but it’s done using another software (Geomagic Wrap). I would prefer to use only open-source software for my study, but it should give you an idea.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29f0b7143a747417e655ed18800dea9da0940045.jpeg" data-download-href="/uploads/short-url/5Z1iYJU23pCfkLAf8LSrw1q1k45.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29f0b7143a747417e655ed18800dea9da0940045_2_533x500.jpeg" alt="image" data-base62-sha1="5Z1iYJU23pCfkLAf8LSrw1q1k45" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29f0b7143a747417e655ed18800dea9da0940045_2_533x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29f0b7143a747417e655ed18800dea9da0940045.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29f0b7143a747417e655ed18800dea9da0940045.jpeg 2x" data-dominant-color="BBC7C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">666×624 60.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can see two circles; I want to achieve that in Slicer too. I think I can manage that on my own, but if I can’t, I’ll discuss it in another post… haha.</p>
<p>I hope I was clear enough. Thanks a lot in advance for your help!</p>

---

## Post #4 by @muratmaga (2024-06-13 14:49 UTC)

<p>this post and specific answer seems relevant to your inquiry:</p>
<aside class="quote quote-modified" data-post="16" data-topic="19446">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/creating-a-new-coordinate-system/19446/16">Creating a new coordinate system</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can define a coordinate system using a markups plane node: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fd6fd42bfe7e90bf0b890105aa4424e79e42ae5.jpeg" data-download-href="/uploads/short-url/boikCzGpiFFwX5LNcAuEO8jNLBb.jpeg?dl=1" title="image">[image]</a> 
The advantage of using this instead of a transform that you can conveniently place the node using 3 points and then further adjust its position and orientation using interaction handles. 
Once you have defined the plane, you can get the the transform between this coordinate system and the RAS coordinate system like this: 
planeToWorld = vtk.vtkMatrix4x4()
getNode('P').GetObjectToWorldMatrix(planeToWorld)

If you concatenat…
  </blockquote>
</aside>


---

## Post #5 by @Julian_KC (2024-06-13 15:10 UTC)

<p>Thanks for your answer,</p>
<p>I already saw that but I didn’t understood how to use it and apply it to my models,<br>
Sorry to ask that but can you be a little bit more specific ?</p>

---

## Post #6 by @Julian_KC (2024-06-14 08:55 UTC)

<p>I tried this code :</p>
<p>import slicer<br>
import numpy as np</p>
<h1><a name="p-112682-fonction-to-create-a-translate-transform-1" class="anchor" href="#p-112682-fonction-to-create-a-translate-transform-1" aria-label="Heading link"></a>Fonction to Create a translate transform</h1>
<p>def create_translation_transform(x, y, z):<br>
transform = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTransformNode”)<br>
matrix = vtk.vtkMatrix4x4()<br>
matrix.SetElement(0, 3, -x)<br>
matrix.SetElement(1, 3, -y)<br>
matrix.SetElement(2, 3, -z)<br>
transform.SetMatrixTransformToParent(matrix)<br>
return transform</p>
<h1><a name="p-112682-fonction-to-align-with-z-axis-2" class="anchor" href="#p-112682-fonction-to-align-with-z-axis-2" aria-label="Heading link"></a>Fonction to Align with Z axis</h1>
<p>def create_rotation_transform(angle, axis):<br>
transform = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTransformNode”)<br>
matrix = vtk.vtkMatrix4x4()<br>
axis = np.array(axis) / np.linalg.norm(axis)<br>
c, s = np.cos(angle), np.sin(angle)<br>
C = 1 - c<br>
x, y, z = axis<br>
matrix.SetElement(0, 0, x<em>x</em>C + c)<br>
matrix.SetElement(0, 1, x<em>y</em>C - z<em>s)<br>
matrix.SetElement(0, 2, x</em>z<em>C + y</em>s)<br>
matrix.SetElement(1, 0, y<em>x</em>C + z<em>s)<br>
matrix.SetElement(1, 1, y</em>y<em>C + c)<br>
matrix.SetElement(1, 2, y</em>z<em>C - x</em>s)<br>
matrix.SetElement(2, 0, z<em>x</em>C - y<em>s)<br>
matrix.SetElement(2, 1, z</em>y<em>C + x</em>s)<br>
matrix.SetElement(2, 2, z<em>z</em>C + c)<br>
transform.SetMatrixTransformToParent(matrix)<br>
return transform</p>
<h1><a name="p-112682-define-point-to-align-with-origin-000-3" class="anchor" href="#p-112682-define-point-to-align-with-origin-000-3" aria-label="Heading link"></a>Define point to align with origin (0.0.0)</h1>
<p>point_origin = [13.311, -14.499, -1.052]  # Remplacer par les coordonnées réelles du point</p>
<h1><a name="p-112682-define-point-of-the-line-to-align-with-z-axis-4" class="anchor" href="#p-112682-define-point-of-the-line-to-align-with-z-axis-4" aria-label="Heading link"></a>Define point of the line to align with z axis</h1>
<p>point1 = [16.183, 0.719, 11.181]  # Remplacer par les coordonnées réelles du point 1<br>
point2 = [13.277, -14.627, -1.061]  # Remplacer par les coordonnées réelles du point 2</p>
<h1><a name="p-112682-compute-line-direction-5" class="anchor" href="#p-112682-compute-line-direction-5" aria-label="Heading link"></a>Compute line direction</h1>
<p>line_direction = np.array(point2) - np.array(point1)<br>
line_direction = line_direction / np.linalg.norm(line_direction)</p>
<h1><a name="p-112682-compute-the-angle-of-the-line-6" class="anchor" href="#p-112682-compute-the-angle-of-the-line-6" aria-label="Heading link"></a>Compute the angle of the line</h1>
<p>axis_z = np.array([0, 0, 1])<br>
angle = np.arccos(np.dot(line_direction, axis_z))</p>
<h1><a name="p-112682-create-and-apply-the-fonction-of-translate-transforme-7" class="anchor" href="#p-112682-create-and-apply-the-fonction-of-translate-transforme-7" aria-label="Heading link"></a>Create and apply the fonction of translate transforme</h1>
<p>translation_transform = create_translation_transform(*point_origin)<br>
slicer.util.getNode(‘YourNodeName’).SetAndObserveTransformNodeID(translation_transform.GetID())</p>
<h1><a name="p-112682-create-and-apply-rotate-transform-8" class="anchor" href="#p-112682-create-and-apply-rotate-transform-8" aria-label="Heading link"></a>Create and apply rotate transform</h1>
<p>rotation_transform = create_rotation_transform(angle, np.cross(line_direction, axis_z))<br>
slicer.util.getNode(‘YourNodeName’).SetAndObserveTransformNodeID(rotation_transform.GetID())</p>
<p>slicer.app.processEvents()</p>
<p>And this is note exactly the result I want :</p>
<p>Before<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5d26c3818bd0f9983aee5e1a024d8b6dfe3e1fc.jpeg" data-download-href="/uploads/short-url/pWtfxYgHqSwzm7MMelSulwfgf8w.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5d26c3818bd0f9983aee5e1a024d8b6dfe3e1fc_2_690x497.jpeg" alt="image" data-base62-sha1="pWtfxYgHqSwzm7MMelSulwfgf8w" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5d26c3818bd0f9983aee5e1a024d8b6dfe3e1fc_2_690x497.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5d26c3818bd0f9983aee5e1a024d8b6dfe3e1fc_2_1035x745.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5d26c3818bd0f9983aee5e1a024d8b6dfe3e1fc.jpeg 2x" data-dominant-color="9C9EB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1169×843 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a9b5b2c2c35935ac1b1d308f39f8b109673980f.jpeg" data-download-href="/uploads/short-url/3NngjRFA8Da2tX07z0jpFooNu3B.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a9b5b2c2c35935ac1b1d308f39f8b109673980f_2_690x428.jpeg" alt="image" data-base62-sha1="3NngjRFA8Da2tX07z0jpFooNu3B" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a9b5b2c2c35935ac1b1d308f39f8b109673980f_2_690x428.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a9b5b2c2c35935ac1b1d308f39f8b109673980f_2_1035x642.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a9b5b2c2c35935ac1b1d308f39f8b109673980f.jpeg 2x" data-dominant-color="9D9FB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1080×671 88.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But it seems a bit better, but the bounding box and the markups not follow …</p>

---

## Post #7 by @muratmaga (2024-06-14 17:21 UTC)

<p>You need to apply the same transform to the markups as well.</p>
<p>Also, if you want to recenter the bounding box to its new position, make sure the hit the center the FOV icon in 3D viewer.</p>

---

## Post #8 by @chir.set (2024-06-14 17:24 UTC)

<aside class="quote no-group" data-username="Julian_KC" data-post="3" data-topic="36725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julian_kc/48/18359_2.png" class="avatar"> Julian_KC:</div>
<blockquote>
<p>in the first image</p>
</blockquote>
</aside>
<p>If I rightly understood your requirement, this code snippet may help. You’ll need to add a Plane node anywhere in your scene. The Line guides everything else.</p>
<pre><code class="lang-auto">
model = getNode("Model")
line = getNode("L")
# The plane is a wonderful node: it provides its orthogonal axes that we can immediately use. Calculating these axes can become irritating.
plane = getNode("P")

p1Line = [0.0] * 3
p2Line = [0.0] * 3
line.GetNthControlPointPositionWorld(0, p1Line)
line.GetNthControlPointPositionWorld(1, p2Line)

normal = [0.0] * 3
binormal = [0.0] * 3
tangent = [0.0] * 3
# Change the subtraction order if needed.
vtk.vtkMath().Subtract(p2Line, p1Line, normal)
vtk.vtkMath().Normalize(normal)

plane.SetNormalWorld(normal)
plane.SetNthControlPointPositionWorld(0, p2Line)

plane.GetAxesWorld(normal, binormal, tangent)

transform = vtk.vtkTransform()
matrix = transform.GetMatrix()
for r in range(3):
    matrix.SetElement(r, 0, normal[r])
    matrix.SetElement(r, 1, binormal[r])
    matrix.SetElement(r, 2, tangent[r])
    matrix.SetElement(r, 3, p2Line[r])

# Allows alignment of the plane's axes to world axes, and placement at origin.
matrix.Invert()

model.ApplyTransform(transform)
plane.ApplyTransform(transform)
line.ApplyTransform(transform)
</code></pre>

---
