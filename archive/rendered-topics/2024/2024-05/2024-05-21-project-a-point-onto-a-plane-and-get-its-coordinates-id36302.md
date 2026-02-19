---
topic_id: 36302
title: "Project A Point Onto A Plane And Get Its Coordinates"
date: 2024-05-21
url: https://discourse.slicer.org/t/36302
---

# Project a point onto a plane and get its coordinates

**Topic ID**: 36302
**Date**: 2024-05-21
**URL**: https://discourse.slicer.org/t/project-a-point-onto-a-plane-and-get-its-coordinates/36302

---

## Post #1 by @Olivia (2024-05-21 15:17 UTC)

<p>Hello esteemed developers, I’m new to this software and am a student of dentistry. I’m measuring the precision of the implant placement, This program has been a great help to me! But I’ve run into some problems.Can you guys edit a piece of code to help me out?<br>
In general, the problem I face is this:<br>
I plan two line segments that are perpendicular to each other, while they can define a plane and form a Cartesian coordinate system. In addition, I marked a point to be measured that would lie outside the plane. But in order to get its position, I need to get its coordinates in the above mentioned right-angled coordinate system. In other words, I think I need to get the projected position of that point in the plane and get its coordinates in the plane’s Cartesian coordinate system.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e698f2600c35f23fb61d16df4b5221591668063.png" alt="image" data-base62-sha1="fKKGeFzYetLMzzDStl50JayVByX" width="274" height="299"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9fd979aeeed7317f800423f3bbaeb84861684ab.png" alt="image" data-base62-sha1="xnYziPlcJ9opINhdJ9svEjRXqDV" width="291" height="249"><br>
As shown in the figure, I need to get the distance of F6 in the plane formed by the two lines from to the line where the two line segments are located (i.e., the coordinates of F6 projected onto that Cartesian coordinate system)<br>
I know it’s going to be a bit complicated and I’d appreciate any help you guys can offer.<br>
Thanks again to the members of the development team for their dedication!<br>
Sincerely, Olivia</p>

---

## Post #2 by @chir.set (2024-05-21 15:51 UTC)

<p>At first glance, if you subtract the coordinates of the intersection of the lines from F_6-1, the result should mean the projection of F_6-1 on that plane. It would be “in the plane’s Cartesian coordinate system” as you say, not a RAS coordinate. But I’m not 100% sure, other insights would be interesting to read.</p>

---

## Post #3 by @chir.set (2024-05-21 18:51 UTC)

<p>This code snippet may better answer your question. But you should use a plane markups node named ‘P’ instead of 2 lines intersecting at right angle. A fiducial node named ‘F’ with a single point is needed.</p>
<p>It outputs the projection relative to the origin of the plane, and the projection in world coordinates.</p>
<p>Maybe there’s a simpler way, or a right way if it’s incorrect, I’ll be eager to learn it.</p>
<pre><code class="lang-auto">p = getNode("P")
f = getNode("F")

normal = [0.0] * 3
binormal = [0.0] * 3
tangent = [0.0] * 3
planeOrigin = p.GetOriginWorld()

# Using a plane avoids much calculation.
p.GetAxesWorld(normal, binormal, tangent)

t = vtk.vtkTransform()
m = t.GetMatrix()
for r in range(3):
    m.SetElement(r, 0, normal[r])
    m.SetElement(r, 1, binormal[r])
    m.SetElement(r, 2, tangent[r])
    m.SetElement(r, 3, planeOrigin[r])
    
t.Inverse()

# Go to origin with the inverse matrix.
f.ApplyTransform(t)

point = [0.0] * 3
f.GetNthControlPointPositionWorld(0, point)

# Project on the plane at origin.
point = [point[0], point[1], 0.0]
f.SetNthControlPointPositionWorld(0, point)
print(point, "Relative to the plane's origin.")

# Go back to the plane.
t.Inverse()
f.ApplyTransform(t)
f.GetNthControlPointPositionWorld(0, point)
print(point, "World coordinates")
</code></pre>

---

## Post #4 by @mikebind (2024-05-21 19:03 UTC)

<p>What it sounds like you want can be achieved with some basic linear algebra, but you will need to be a bit more precise.  For example, three points determine a plane; in general, if you place a 4th point without constraints it is very unlikely to lie on the same plane as the other three points, so then it needs to be determined exactly what plane you are referring to for your 2D cartesian coordinate system.  Likewise, two intersecting lines are unlikely to be exactly perpendicular, so if you want to force them to be perpendicular then you need to specify what points are moved and how to enforce that. Lastly, you need to decide which way is positive on each axis and what units you are using.</p>
<p>One simple way to achieve your goals would be to have 3 points placed in a specified order, let’s call them points A, B, and C.  The vector from B to A could be your positive y-axis, and positive x-axis could be the vector perpendicular from BA which points at C.  The origin of your coordinate system could be where those two vectors intersect, call that point O.  Then, to get in-plane coordinates for any arbitrary point P, we need to project the vector OP into the plane defined by ABC.  This is obtained by subtracting the component of OP which is in the direction of the normal vector to the plane, which will leave the component of OP which is parallel to the plane.</p>
<p><a class="mention" href="/u/chir.set">@chir.set</a> 's suggestion to use a markups plane node is a good one, and will simplify a couple of these steps, but you would still need specify the axis directions for your plane (which you could do interactively by manipulating the markups plane, or derive via linear algebra from your point placements).</p>

---

## Post #5 by @Olivia (2024-05-22 13:43 UTC)

<p>I think this could work, but I still have some uncertainties. Since I’m really not very good at math and code, I haven’t heard of a “plane-marked node” before, how does that point define a plane? Is that the center origin of the plane that is automatically generated after I create the plane?</p>

---

## Post #6 by @Olivia (2024-05-22 13:52 UTC)

<p>I guess the good news is that the two mutually perpendicular line segments above are defined in a pre-existing plane, which I think probably basically guarantees the accuracy of the entire coordinate system establishment.<br>
Going through the vectors with some simple trigonometric functions does sound like it would solve the problem, but I’m worried that wouldn’t be a smart way to go about it, since I have a lot of similar data to measure and that would be a lot of work.<br>
I think I’ll go with <a class="mention" href="/u/chir.set">@chir.set</a> method, but I believe I need to learn more about planar labeled nodes.</p>

---

## Post #7 by @chir.set (2024-05-22 14:53 UTC)

<p>It’s the regular markups plane node. By default, its normal adapts to the closest object in a view. You images show that you deal with a cylinder, so it’s very easy to place the plane on top of the cylinder.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78ce5016a5ffa56c2ceff05cd4570cdabba4370a.png" data-download-href="/uploads/short-url/heHjOSm3TWANar6tt3mrS16Q2Xo.png?dl=1" title="PlaneOnCylinder" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78ce5016a5ffa56c2ceff05cd4570cdabba4370a_2_410x499.png" alt="PlaneOnCylinder" data-base62-sha1="heHjOSm3TWANar6tt3mrS16Q2Xo" width="410" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78ce5016a5ffa56c2ceff05cd4570cdabba4370a_2_410x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78ce5016a5ffa56c2ceff05cd4570cdabba4370a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78ce5016a5ffa56c2ceff05cd4570cdabba4370a.png 2x" data-dominant-color="51382E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PlaneOnCylinder</span><span class="informations">571×696 25.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Olivia (2024-05-22 15:26 UTC)

<p>It’s very happy news that this can work! I’m sure this will be an efficient way to help me make bulk measurements. You have really helped me solve a big problem. I’m glad this will allow me to work more smoothly on the 3D Slicer platform. Again, hats off to you and the other developers!</p>

---

## Post #9 by @mikebind (2024-05-22 15:44 UTC)

<p>If all you need is a distance within that plane, this will work fine.  If you need (x,y) coordinates of the projected point within the plane, then you need to specify an axis direction for the plane as well as placing the single point. If you need to do that, it should be straightforward to do, just respond here and we can sort it out.</p>

---

## Post #10 by @Olivia (2024-05-22 15:52 UTC)

<p>I do need its coordinates in the coordinate system made up of the specified axes, and in the test I just did, I manually tried to align the original axes of the plane as closely as possible to the axes I needed, which introduces a relatively acceptable error. But if this is indeed a simple problem, then I would be more than willing to accept your help and thank you for assisting me.</p>

---

## Post #11 by @mikebind (2024-05-22 18:56 UTC)

<pre><code class="lang-auto">P = getNode('P') # your markupsPlaneNode
xLine = getNode('NameOfYourXAxisLineHere')

import numpy as np
# Get Desired X-axis direction from your line markup which runs along the x axis
point0 = np.zeros(3) # pre-allocate
point1 = np.zeros(3) # pre-allocate
xLine.GetNthControlPointPositionWorld(0, point0) # fill in point0
xLine.GetNthControlPointPositionWorld(1, point1) # fill in point1
xDirectionVectorRaw = point1 - point0 # switch order of subtraction if x-axis is reversed
# Normalize direction vector to have length 1 
xDirectionVectorUnitLength = xDirectionVectorRaw/np.linalg.norm(xDirectionVectorRaw)

# Allocate vectors to hold existing axes
x = np.zeros(3)
y = np.zeros(3)
z = np.zeros(3)
P.GetAxes(x,y,z) # get existing axes of plane

# Calculate the desired Y axis from desired X axis and plane normal (Z axis)
newY = np.cross(z, xDirectionVectorUnitLength)

# Adjust the plane to align with the desired axes
P.SetAxes(xDirectionVectorUnitLength, newY, z)
# Note, you will get an error here if the original xLine
# was not truly in the same plane as the planeNode
</code></pre>
<p>If you haven’t already, you will also want to make sure the plane origin point coincides with the intersection of your axes lines, because the coordinates you get out are going to be relative to wherever the plane origin point is rather than relative to the axes line intersection.  You can set the plane origin point like <code>P.SetCenter(originPoint)</code> and you gather the origin point using <code>GetNthControlPointPositionWorld()</code> the same way as for point0 and point1 above; you just need to know the name of the markups node which has the point you need, and what control point number the origin point is (numbering starts at 0, so if there is only one control point, then you just want the 0th one).</p>
<p>Let us know if you run into any problems.</p>

---

## Post #12 by @Olivia (2024-05-23 02:52 UTC)

<p>Thank you very much! This really works and helps me solve problems more easily and with precision. Once again, I salute you and the development team of 3D Slicer! The ease of use of the software and your professional and timely support will be a great motivation for me to continue using it!</p>

---

## Post #13 by @lassoan (2024-05-24 11:13 UTC)

<p>Glad to hear this! Can you write a bit about the clinical application, i.e., what do you need to measure. Since there are thousands of Slicer users on this forum, there is a good chance that there are others who are working on the exact same clinical problem and you could help each other further. For example, we have been working on very similar measurements for various cardiac device placement measurements and simulations and we have (and will have more) complete modules to share and collaborate in developing.</p>

---

## Post #14 by @Olivia (2024-05-26 08:48 UTC)

<p>Overall, what I’m doing is measuring implant placement accuracy. We will align the pre-implant plan with the post-implant DICOM and measure the desired data. You can see roughly the data to be measured in this picture.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e13f268a11d132f3b22881ae6a05e6bc6b795c5.png" alt="image" data-base62-sha1="6zCHnDb6lSMHKQaqVMm6N1aN421" width="536" height="443"><br>
But the reason I’m posting this is because I’m measuring the buccolingual and proximo-distal mesial deviation in the crown and root planes of the implant.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e698f2600c35f23fb61d16df4b5221591668063.png" alt="image" data-base62-sha1="fKKGeFzYetLMzzDStl50JayVByX" width="274" height="299"><br>
As shown in the diagram (which is the coronal plane of the implant), F_6-1 is the actual postoperative implant center (DICOM has been hidden), and the intersection point shown in the diagram is the preoperatively planned implant center. The code you have provided allows me to directly measure the buccolingual and proximal-distal mesial distances of F_6-1 from the ideal center point in the same plane.It made my measurements much easier.</p>

---
