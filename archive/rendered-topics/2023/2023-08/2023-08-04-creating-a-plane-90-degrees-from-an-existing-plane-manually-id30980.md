---
topic_id: 30980
title: "Creating A Plane 90 Degrees From An Existing Plane Manually"
date: 2023-08-04
url: https://discourse.slicer.org/t/30980
---

# Creating a plane 90 degrees from an existing plane manually or automatically

**Topic ID**: 30980
**Date**: 2023-08-04
**URL**: https://discourse.slicer.org/t/creating-a-plane-90-degrees-from-an-existing-plane-manually-or-automatically/30980

---

## Post #1 by @Dbradl6 (2023-08-04 17:55 UTC)

<p>Hi! I am looking to use 3DSlicer to analyze several CT scans and need to create two planes to base my measurement on. The first is going to be a Frankfort plan based on 3 markups and the second will be a coronal plane 90 degrees vertically from the created Frankfort plane. What would be the best way to do this? I know there is a script function to measure the angle between two planes. In theory, I could place the new plane and then adjust it until it is 90 degrees but that seems time-consuming to do for 100+ images.</p>
<p>Ultimately I want to create a program that will allow me to place a few control points and measurement points and generate the two planes as well as the distance between a series of points and the planes. This is just the first step. I’ve looked into the extension SlicerMorph to help automatic this process but any additional tips would be greatly appreciated since this is my first time using 3D Slicer as a replacement for mimics/dolphin.</p>
<p>TLDR: How can I create two planes 90 degrees from each other based and then place a series of points and get the distance from them in the plane in the fastest, non-manual way possible?</p>

---

## Post #2 by @chir.set (2023-08-04 20:30 UTC)

<p>I suppose you are referring to markups planes.</p>
<p>You may automate the <em>plane creation steps</em> by placing 3 fiducial points per the requirements of the Frankfurt plane. The script below will create orthogonal planes using the 3 fiducial points.</p>
<pre><code class="lang-auto">def createPlanes(f, angle):
    p1 = [0.0, 0.0, 0.0]
    p2 = [0.0, 0.0, 0.0]
    p3 = [0.0, 0.0, 0.0]
    f.GetNthControlPointPositionWorld(0, p1)
    f.GetNthControlPointPositionWorld(1, p2)
    f.GetNthControlPointPositionWorld(2, p3)
    
    plane1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsPlaneNode")
    plane1.CreateDefaultDisplayNodes()
    plane1.SetPlaneType(slicer.vtkMRMLMarkupsPlaneNode.PlaneType3Points)
    plane1.AddControlPointWorld(p1)
    plane1.AddControlPointWorld(p2)
    plane1.AddControlPointWorld(p3)
    
    plane1Normal = plane1.GetNormalWorld()
    plane1Binormal = [0.0, 0.0, 0.0]
    plane1Tangent = [0.0, 0.0, 0.0]
    # Get axes relative to plane1Normal. 
    vtk.vtkMath().Perpendiculars(plane1Normal, plane1Binormal, plane1Tangent, angle)
    
    plane2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsPlaneNode")
    plane2.CreateDefaultDisplayNodes()
    plane2.AddControlPointWorld(p1)
    # Set this plane's normal : to plane1Binormal or plane1Tangent.
    plane2.SetNormalWorld(plane1Binormal)
    
# Place 3 fiducial points to define your plane.
# Replace F by the name of your fiducial markups node
f = slicer.util.getNode("F")
# Using a 0° rotation around plane1Normal. Tune as needed.
createPlanes(f, 0)
</code></pre>
<p>This should probably be of help to further proceed with your other requirements. As I understand, a big problem would be to know the angle of rotation around plane1Normal.</p>

---

## Post #3 by @chir.set (2023-08-05 16:05 UTC)

<p>Hi <a class="mention" href="/u/dbradl6">@Dbradl6</a> ,</p>
<p>You may have a look at <a href="https://github.com/chir-set/RcHacks7.git" rel="noopener nofollow ugc">this</a> page to have more insight in your automation scripts. You may pay attention to 12-ResliceToAxis file in particular. This file aims at reslicing in particular. Slices are planes too, it may be easier to place points on slices than on markups planes.</p>

---

## Post #4 by @Dbradl6 (2023-08-12 16:11 UTC)

<p>Hi thank you for responding. I agree the biggest issue is going to be getting the angle of rotation. I noticed in your script you have this portion: "# Using a 0° rotation around plane1Normal. Tune as needed.<br>
createPlanes(f, 0) " Could I just create an additional plane and change the angle here from 0 to 90?</p>

---

## Post #5 by @Dbradl6 (2023-08-12 17:11 UTC)

<p>Also this might seem very basic but how exactly would I run this? When I pasted it into the python console I got an error. I also tried creating the node F with the three control points first and I still got an error. This was the error I got:</p>
<p>Traceback (most recent call last):<br>
File “”, line 30, in <br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 1499, in getNode<br>
raise MRMLNodeNotFoundException(“could not find nodes in the scene by name or id ‘%s’” % (pattern if (isinstance(pattern, str)) else “”))<br>
slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘F’</p>

---

## Post #6 by @chir.set (2023-08-12 17:38 UTC)

<aside class="quote no-group" data-username="Dbradl6" data-post="4" data-topic="30980">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ecd19e/48.png" class="avatar"> Dbradl6:</div>
<blockquote>
<p>change the angle</p>
</blockquote>
</aside>
<p>You can specify an arbitrary angle of rotation to ::Perpendiculars(). However, it’s in radians; you may yet mean 90 radians <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="Dbradl6" data-post="4" data-topic="30980">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ecd19e/48.png" class="avatar"> Dbradl6:</div>
<blockquote>
<p>Could I just create an additional plane</p>
</blockquote>
</aside>
<p>I suppose you mean a third plane orthogonal to the 2 others. The simplest way is to append these lines to the <em>function</em> :</p>
<pre><code class="lang-auto">plane3 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsPlaneNode")
plane3.CreateDefaultDisplayNodes()
plane3.AddControlPointWorld(p1)
# Set this plane's normal : to plane1Tangent.
plane3.SetNormalWorld(plane1Tangent)
</code></pre>

---

## Post #7 by @chir.set (2023-08-12 17:41 UTC)

<aside class="quote no-group" data-username="Dbradl6" data-post="5" data-topic="30980">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ecd19e/48.png" class="avatar"> Dbradl6:</div>
<blockquote>
<p>could not find nodes in the scene by name or id ‘F’</p>
</blockquote>
</aside>
<p>As it says, your scene does not have a node of whatever class having ‘F’ as <em>name</em> or <em>id</em>.</p>
<p>If, for example, you have been playing with a fiducial node named ‘F’, then deleted it and created another one, the default name will be ‘F_1’. Adapt the script thus.</p>

---

## Post #8 by @Dbradl6 (2023-08-12 18:03 UTC)

<p>Ok thank you so much I got it to work perfectly!! One last thing… I realized that I need to shift the second plane horizontally up to a different control point while not changing the angle. I’ll attach a picture. The additional control point/where I want the plane to be moved up to is marked “Sella”. What would be the best way to do that?</p>
<p>Could I just add the fourth point in the initial point-creating process or should I create a third plane using the new point?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23e374ffe332e9620b054765ee79f3d02ff07ac6.png" data-download-href="/uploads/short-url/57u2e0Vd1F7D8SCWT8d9G1C5jCK.png?dl=1" title="Screen Shot 2023-08-12 at 12.59.09 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23e374ffe332e9620b054765ee79f3d02ff07ac6_2_690x454.png" alt="Screen Shot 2023-08-12 at 12.59.09 PM" data-base62-sha1="57u2e0Vd1F7D8SCWT8d9G1C5jCK" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23e374ffe332e9620b054765ee79f3d02ff07ac6_2_690x454.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23e374ffe332e9620b054765ee79f3d02ff07ac6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23e374ffe332e9620b054765ee79f3d02ff07ac6.png 2x" data-dominant-color="8C95B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-08-12 at 12.59.09 PM</span><span class="informations">979×645 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @chir.set (2023-08-12 18:45 UTC)

<aside class="quote no-group quote-modified" data-username="Dbradl6" data-post="8" data-topic="30980">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ecd19e/48.png" class="avatar"> Dbradl6:</div>
<blockquote>
<p>Could I just add… …</p>
</blockquote>
</aside>
<p>You may manually set the center of the second plane to sella’s coordinate in the Markups module’s widget.</p>
<p>Or use an updated script :</p>
<pre><code class="lang-auto">def createPlanes(f, plane2Center = None, angle = None):
    p1 = [0.0, 0.0, 0.0]
    p2 = [0.0, 0.0, 0.0]
    p3 = [0.0, 0.0, 0.0]
    f.GetNthControlPointPositionWorld(0, p1)
    f.GetNthControlPointPositionWorld(1, p2)
    f.GetNthControlPointPositionWorld(2, p3)
    
    rotationOfPerpendiculars = 0.0
    if angle is not None:
        rotationOfPerpendiculars = angle
        
    plane2Coordinates = p1
    if plane2Center is not None:
        plane2Coordinates = plane2Center
    
    plane1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsPlaneNode")
    plane1.CreateDefaultDisplayNodes()
    plane1.SetPlaneType(slicer.vtkMRMLMarkupsPlaneNode.PlaneType3Points)
    plane1.AddControlPointWorld(p1)
    plane1.AddControlPointWorld(p2)
    plane1.AddControlPointWorld(p3)
    
    plane1Normal = plane1.GetNormalWorld()
    plane1Binormal = [0.0, 0.0, 0.0]
    plane1Tangent = [0.0, 0.0, 0.0]
    # Get axes relative to plane1Normal. 
    vtk.vtkMath().Perpendiculars(plane1Normal, plane1Binormal, plane1Tangent, rotationOfPerpendiculars)
    
    plane2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsPlaneNode")
    plane2.CreateDefaultDisplayNodes()
    plane2.AddControlPointWorld(plane2Coordinates)
    # Set this plane's normal : to plane1Binormal or plane1Tangent.
    plane2.SetNormalWorld(plane1Binormal)
    
# Place 3 fiducial points to define your plane.
# Replace F by the name of your fiducial markups node
f = slicer.util.getNode("F")
p4 = [0.0, 0.0, 0.0] # sella
f.GetNthControlPointPositionWorld(3, p4)
# Using a 0° rotation around plane1Normal. Tune as needed.
createPlanes(f, p4, 0.0)
</code></pre>
<p>You now get the picture to further modify the script for your specific needs.</p>

---
