# Rotation around y axe

**Topic ID**: 9062
**Date**: 2019-11-07
**URL**: https://discourse.slicer.org/t/rotation-around-y-axe/9062

---

## Post #1 by @alexk (2019-11-07 15:02 UTC)

<p>Hi, I’m using SlicerVirtualReality with HTC Vive Pro.<br>
I wish to rotate my scene and an object around its axis “y” to have a circular view of my object.<br>
I can not do it using the controllers.<br>
Is it possible ? Can you help me ?<br>
Alex</p>

---

## Post #2 by @aiden.zhu (2019-11-07 15:35 UTC)

<p>Hi Alex,<br>
If you play with python code, it’s easy to do it.</p>
<pre><code>  slicer.util.setSliceViewerLayers(background = imgNode)
  transform = [ ]
  rot_angle = 45
  transform = vtk.vtkTransform()
  transform.RotateWXYZ(0, rot_angle,  0, 1)  
  transformNode = slicer.mrmlScene.AddNode(slicer.vtkMRMLTransformNode())
  transformNode.ApplyTransform(transform)
  imgNode.SetAndObserveTransformNodeID(transformNode.GetID())
</code></pre>
<p>Hope it helps.</p>

---

## Post #3 by @lassoan (2019-11-07 16:03 UTC)

<aside class="quote no-group" data-username="alexk" data-post="1" data-topic="9062">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/91b2a8/48.png" class="avatar"> alexk:</div>
<blockquote>
<p>I can not do it using the controllers</p>
</blockquote>
</aside>
<p>Do you mean it is inconvenient to rotate the scene around using <a href="https://github.com/KitwareMedical/SlicerVirtualReality#how-to-use-controllers">two-handed gestures</a>, or you don’t know how to rotate the scene?</p>

---

## Post #4 by @alexk (2019-11-07 16:33 UTC)

<p>Yes, it is inconvenient using two handed gestures.</p>
<p>I tried to make several movements with controllers but I can only rotate around the Z axis (the object turns as needles).</p>
<p>I would like to rotate it around the y axis (horizontal movement)</p>

---

## Post #5 by @lassoan (2019-11-07 17:32 UTC)

<p>Have you tried both these methods?</p>
<ul>
<li>rotating the scene (using two-handed gestures; making the object non-selectable in Data module to ensure that you don’t accidentally grab the object)</li>
<li>rotating the object (grab the object by reaching inside with one hand, rotating it, then taking over to the other hand to rotate it further)</li>
</ul>
<p>You can also rotate the object to a view that you would like to see in virtual reality and click “Set virtual reality view to match reference view” button on the toolbar.</p>

---

## Post #6 by @alexk (2019-11-08 09:36 UTC)

<p>Thanks for your answer.</p>
<p>Yes, i have already tried these methods.</p>
<p>I wish to be able to see my scene of face then rotation to see it in right profile but also to be able to see it from below. The goal is to have a rotation in traveling.<br>
The actual manipulation that I make only allows me to turn the scene like clockwise.</p>

---

## Post #7 by @lassoan (2019-11-08 12:53 UTC)

<p>Sorry, for me it is still not clear what would you like to achieve. Can you send a video of your virtual reality view so that we can see what you do now, and annotate a few still frames so that we can understand what would you like to do differently?</p>

---

## Post #8 by @alexk (2019-11-10 12:03 UTC)

<p>Hello, I just want to do a horizontal or vertical rotation like this in Slicer Virtual Reality using the controllers.</p>
<p>Alex</p>
<p>Le ven. 8 nov. 2019 à 14:03, Andras Lasso via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> a écrit :</p>
<p>(Attachment Rotation.mov is missing)</p>

---

## Post #9 by @lassoan (2019-11-10 12:48 UTC)

<p>The attachment did not come through. Please try to upload via the web interface of discourse.</p>
<p>In virtual reality view, you can rotate the object or rotate the world (move around the object). Rotating the object around its own center is easier to implement: you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Examples">apply a linear transform</a> and set the desired rotation matrix in it.</p>

---

## Post #10 by @alexk (2019-11-12 21:27 UTC)

<p>Thank you very much. I tried to make a rotation of object but it is not around its axis but of the center of the rest of the skull.</p>
<p>Here is a video of what I get and what I want for virtual reality :    <a href="https://filedn.com/lMEY7FuuJRLkh9f4Jtgk5ez/Test%20zygomatic%20bone.mov" rel="nofollow noopener">https://filedn.com/lMEY7FuuJRLkh9f4Jtgk5ez/Test%20zygomatic%20bone.mov</a>.</p>
<p>How to do ?</p>
<p>Alex</p>
<p>Le dim. 10 nov. 2019 à 13:58, Andras Lasso via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> a écrit :</p>

---

## Post #11 by @lassoan (2019-11-14 14:45 UTC)

<p>You can construct a transformation matrix that rotates around an arbitrary point by multiplying 3 transforms: translate center of rotation to origin, rotate, translate origin to center of rotation.</p>

---

## Post #12 by @alexk (2019-11-19 13:52 UTC)

<p>Thanks for your answer. I do not know how to create an arbitrary point of rotation and then do the 3 proposed transformations. Is there a tutorial to do this type of transformation?</p>
<p>Alex</p>
<p>Le jeu. 14 nov. 2019 à 15:55, Andras Lasso via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> a écrit :</p>

---

## Post #13 by @alexk (2019-11-27 22:58 UTC)

<p>Hello mr Lasso, I have not managed to find a solution to change the point of rotation in arbitrary position and make the transformations. Can you tell if there is a tutorial available.</p>
<p>I thank you in advance</p>

---

## Post #14 by @lassoan (2019-11-27 23:23 UTC)

<p>See for example these pages:</p>
<ul>
<li><a href="https://www.euclideanspace.com/maths/geometry/affine/aroundPoint/">https://www.euclideanspace.com/maths/geometry/affine/aroundPoint/</a></li>
<li><a href="https://math.stackexchange.com/questions/2093314/rotation-matrix-of-rotation-around-a-point-other-than-the-origin">https://math.stackexchange.com/questions/2093314/rotation-matrix-of-rotation-around-a-point-other-than-the-origin</a></li>
</ul>

---

## Post #15 by @lassoan (2019-12-05 15:09 UTC)

<p>I’ve now added an example script in the script repository for rotating about arbitrary centerpoint - see details here: <a href="https://discourse.slicer.org/t/transform-and-rotation/9398/3" class="inline-onebox">Transform and rotation</a></p>

---
