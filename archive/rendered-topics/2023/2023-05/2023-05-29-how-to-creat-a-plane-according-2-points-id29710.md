---
topic_id: 29710
title: "How To Creat A Plane According 2 Points"
date: 2023-05-29
url: https://discourse.slicer.org/t/29710
---

# How to creat a plane according 2 points

**Topic ID**: 29710
**Date**: 2023-05-29
**URL**: https://discourse.slicer.org/t/how-to-creat-a-plane-according-2-points/29710

---

## Post #1 by @slicer365 (2023-05-29 14:36 UTC)

<p>Dear friends</p>
<p>I know there are many ways in slicer to creat a plane</p>
<p>Then how to use two points to create a plane that passes through the middle point of these two points and is perpendicular to the line formed by the two points?</p>
<p>any way or script will be useful!</p>
<p>thankyou!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82f5a4989294cd80121c374f8366aebf97dd2cb9.jpeg" data-download-href="/uploads/short-url/iGwmf46zkEjm1bq2cf3kc9CBVfr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82f5a4989294cd80121c374f8366aebf97dd2cb9_2_517x243.jpeg" alt="image" data-base62-sha1="iGwmf46zkEjm1bq2cf3kc9CBVfr" width="517" height="243" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82f5a4989294cd80121c374f8366aebf97dd2cb9_2_517x243.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82f5a4989294cd80121c374f8366aebf97dd2cb9_2_775x364.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82f5a4989294cd80121c374f8366aebf97dd2cb9_2_1034x486.jpeg 2x" data-dominant-color="CAC6D5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1887×888 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @chir.set (2023-05-29 15:47 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="1" data-topic="29710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>any way or script will be useful!</p>
</blockquote>
</aside>
<p>It should be doable with vtkMath::Perpendiculars() with a direction vector relative to the middle point.</p>
<p>Calculate</p>
<ul>
<li>the middle point,</li>
<li>a direction vector with either point relative to the middle point,</li>
<li>the perpendiculars at the middle point using the direction vector.</li>
</ul>
<p>By adding the perpendiculars to the middle point, you have the 3 points of a plane.</p>

---

## Post #3 by @slicer365 (2023-05-29 16:25 UTC)

<p>I would really appreciate it if you could help me write this slicer script</p>

---

## Post #4 by @chir.set (2023-05-29 17:16 UTC)

<p>This should work when pasted in the Python console.</p>
<p>Add a fiducial node named ‘F’ with 2 points, and a plane named ‘P’ before.</p>
<pre><code class="lang-auto">def findMiddleCrossSectionPlane(p1, p2):
    middlePoint = ((p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0, (p1[2] + p2[2]) / 2.0)
    directionVector = [0.0, 0.0, 0.0]
    vtk.vtkMath().Subtract(p2, middlePoint, directionVector)
    
    perpendicular1 = [0.0, 0.0, 0.0]
    perpendicular2 = [0.0, 0.0, 0.0]
    vtk.vtkMath().Perpendiculars(directionVector, perpendicular1, perpendicular2, 0.0)
    
    planePoint1 = [0.0, 0.0, 0.0]
    planePoint2 = [0.0, 0.0, 0.0]
    vtk.vtkMath().Add(middlePoint, perpendicular1, planePoint1)
    vtk.vtkMath().Add(middlePoint, perpendicular2, planePoint2)
    
    return (middlePoint, planePoint1, planePoint2)
    

# Add a fiducial node named 'F', and a plane named 'P'
f = slicer.util.getNode("F")
p1 = [0.0, 0.0, 0.0]
p2 = [0.0, 0.0, 0.0]
f.GetNthControlPointPositionWorld(0, p1)
f.GetNthControlPointPositionWorld(1, p2)

planePoints = findMiddleCrossSectionPlane(p1, p2)

# Just for visualisation.
plane = slicer.util.getNode("P")
plane.SetPlaneType(slicer.vtkMRMLMarkupsPlaneNode.PlaneType3Points)
plane.SetNthControlPointPositionWorld(0, planePoints[0])
plane.SetNthControlPointPositionWorld(1, planePoints[1])
plane.SetNthControlPointPositionWorld(2, planePoints[2])
</code></pre>

---

## Post #5 by @slicer365 (2023-05-29 22:38 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="4" data-topic="29710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p><code>plane.SetNthControlPointPositionWorld(2, planePoints[2])</code></p>
</blockquote>
</aside>
<p>thankyou very much! it works well!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/938be53b7ffb4b3bc993528823105ed71bfd0e22.jpeg" data-download-href="/uploads/short-url/l3fUACneSBdFMQ8zz7vSLvlengC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/938be53b7ffb4b3bc993528823105ed71bfd0e22_2_689x401.jpeg" alt="image" data-base62-sha1="l3fUACneSBdFMQ8zz7vSLvlengC" width="689" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/938be53b7ffb4b3bc993528823105ed71bfd0e22_2_689x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/938be53b7ffb4b3bc993528823105ed71bfd0e22_2_1033x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/938be53b7ffb4b3bc993528823105ed71bfd0e22.jpeg 2x" data-dominant-color="DFDDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1279×744 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @slicer365 (2023-07-25 11:13 UTC)

<p>Sorry to disturbe you,Mr！</p>
<p>In the last version slicer，the script does not work.</p>
<p>It shows the errors.</p>
<p>Would you like to help solve the problem?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efac06cfbb1cb644c2351016860db8d561934ce3.png" data-download-href="/uploads/short-url/yceGcMezcspWGylJM2Oq3Tsqy2f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efac06cfbb1cb644c2351016860db8d561934ce3.png" alt="image" data-base62-sha1="yceGcMezcspWGylJM2Oq3Tsqy2f" width="690" height="300" data-dominant-color="FDFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1011×440 12.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @chir.set (2023-07-25 15:48 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="6" data-topic="29710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>In the last version slicer，the script does not work.</p>
</blockquote>
</aside>
<p>Hi, I checked with 5.3.0-2023-07-23 r31895 / 98f1a5a on Linux and the script does work.</p>
<p>The error messages mean that the plane P is found but does not have any control point. I could reproduce the errors by adding a plane without any control point to the scene. Use one that you can see and interact with normally.</p>

---

## Post #8 by @lili-yu22 (2025-02-18 13:39 UTC)

<p>can you give me a script about creating a plane through point N and perpendicular to P1,thank you very much.</p>

---

## Post #9 by @cpinter (2025-02-18 14:37 UTC)

<p>The plane node has a mode where you can define the plane with a point and a normal, see <code>PlaneTypePointNormal</code><br>
<a href="https://apidocs.slicer.org/main/classvtkMRMLMarkupsPlaneNode.html#af83a7dac83b04668a4f2bae10245a7baa5bce04cda74677cd6404657aa0868783" class="onebox" target="_blank" rel="noopener">https://apidocs.slicer.org/main/classvtkMRMLMarkupsPlaneNode.html#af83a7dac83b04668a4f2bae10245a7baa5bce04cda74677cd6404657aa0868783</a></p>

---

## Post #10 by @lili-yu22 (2025-02-19 00:19 UTC)

<p>I’m really sorry, but I can’t understand that code and I’m not sure which part of the text I should copy. Could you please provide me with the specific text that I can copy directly? Thank you so much!</p>

---

## Post #11 by @cpinter (2025-02-19 09:55 UTC)

<p>I asked Copilot this question:<br>
“Write me a brief code snippet that creates a vtkMRMLMarkupsPlaneNode from a point and a normal vector using the PlaneTypePointNormal mode.”</p>
<p>It gave me the answer in a few seconds. It looks correct:</p>
<pre><code class="lang-auto">import slicer
import numpy as np

# Define the point and normal vector
point = np.array([10.0, 20.0, 30.0])
normal = np.array([0.0, 0.0, 1.0])

# Create a new vtkMRMLMarkupsPlaneNode
planeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsPlaneNode')
planeNode.SetName('PlaneNode')

# Set the plane type to PlaneTypePointNormal
planeNode.SetPlaneType(slicer.vtkMRMLMarkupsPlaneNode.PlaneTypePointNormal)

# Set the point and normal vector
planeNode.SetOrigin(point)
planeNode.SetNormal(normal)
</code></pre>

---

## Post #12 by @lili-yu22 (2025-02-20 07:39 UTC)

<p>thank you very much <img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=12" title=":rose:" class="emoji" alt=":rose:" loading="lazy" width="20" height="20"></p>

---
