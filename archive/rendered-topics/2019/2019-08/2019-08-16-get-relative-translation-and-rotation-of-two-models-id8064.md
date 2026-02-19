---
topic_id: 8064
title: "Get Relative Translation And Rotation Of Two Models"
date: 2019-08-16
url: https://discourse.slicer.org/t/8064
---

# Get relative translation and rotation of two models

**Topic ID**: 8064
**Date**: 2019-08-16
**URL**: https://discourse.slicer.org/t/get-relative-translation-and-rotation-of-two-models/8064

---

## Post #1 by @Jainey (2019-08-16 17:59 UTC)

<p>I would like to know the rotation and translation of two segmented models, in numerical values. Could you please suggest the best way to do that.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2019-08-17 20:15 UTC)

<p>You can align segments using Segment Registration extension then see the transformation matrix values in Transforms module.</p>

---

## Post #3 by @Jainey (2019-08-18 19:46 UTC)

<p>Thank you Professor <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
It only gives translation along the xyz axes. Is it because the displacement here is based on the centre of mass/ centroid? If I want the rotation of a the rigid body/ bone- what should I do. In the transforms matrix rotation is indicated as 0 in all 3 axes. Do i have to define an axis of rotation please? Thanks</p>
<p>Tom</p>

---

## Post #4 by @lassoan (2019-08-18 21:18 UTC)

<p>The sliders are only for changing the transforms, they don’t necessarily represent the current state.</p>
<p>The transformation is specified by a 4x4 homogeneous transformation matrix (top-left 3x3 matrix defines orientation and scaling, top-right 3x1 vector defines translation).</p>

---

## Post #5 by @Jainey (2019-08-19 15:27 UTC)

<p>Apologies Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
I did not understand I am afraid- I am trying to see the change of position in terms of translation and rotation of two segments. Could you please let me know the numerical values given in the transform correspond to the translation of segment 2, compared to segment 1. If not, what should I do to calculate that, please? Also, how can I calculate rotation, please? Apologies for taking your time- I am a medical person with no software background. Thanks a lot.</p>

---

## Post #6 by @Jainey (2019-08-21 14:45 UTC)

<p>Hi All</p>
<p>Sorry about all this amateur questions and new post. But could someone explain me how to get the displacement of one segment to another in terms of rotations please. I did segment registration and got a the linear transform, but I don’t know how to calculate Euler s angles of rotation of my segment out of this numbers. Thanks a lot</p>

---

## Post #7 by @lassoan (2019-08-21 15:40 UTC)

<p>You can get Euler angles orientation matrix using this code snippet:</p>
<pre><code class="lang-python">transformNode = getNode('LinearTransform_3')
transformMatrix = vtk.vtkMatrix4x4()
transformNode.GetMatrixTransformToParent(transformMatrix)
transform = vtk.vtkTransform()
transform.SetMatrix(transformMatrix)
orientation = transform.GetOrientation()
print(orientation)
</code></pre>
<p>Note that the same orientation can be encoded using many different combinations of rotations, even Euler angles have many variants.</p>
<p>If you need to use a particular convention then you can implement the angle computations from the corresponding mathematical formulae directly you can access orientation matrix element in the <code>transformMatrix</code> object in the example above.</p>

---

## Post #8 by @Jainey (2019-08-21 15:56 UTC)

<p>I can’t thank you enough Professor <a class="mention" href="/u/lassoan">@lassoan</a><br>
I will try this- I don’t get all the mathematical side of it, but my project is to segment bones and calculate the translation and rotation with time points. so I m planning to take the translation values , off the transform module top right  and rotation in Euler angles with this. hope my steps are correct. Thanks again.</p>

---

## Post #9 by @Selva (2021-03-10 01:59 UTC)

<p>Hi Prof <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I have tried to use this code for my calculations of Euler angles.<br>
When I apply to my linear transformation of known roll yaw and pitch, the values I get is only 2 values correct. What could be the possible.</p>
<p>Thanks</p>

---

## Post #10 by @lassoan (2021-03-11 04:24 UTC)

<p>The same orientation can be encoded using many different combinations of rotations, even Euler angles have many variants. The code snippet above uses ZXY rotation order - see complete conversion between matrix and Euler angles representation in this post:</p>
<aside class="quote quote-modified" data-post="2" data-topic="15873">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/reformat-module-values-not-resetting/15873/2">Reformat module Values not resetting</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    The sliders are used only for relative rotations. See more details here: <a href="https://discourse.slicer.org/t/is-the-rotation-of-the-3d-slicers-transform-module-euler-or-quaternion/11944/2" class="inline-onebox">Is the rotation of the 3D Slicer's Transform module Euler or Quaternion? - #2 by lassoan</a> 
We should reset them to 0 more often to make sure users don’t mistake it for Euler angles or something similar. 
Euler angles (and similar representations that rely on successive rotations along multiple axes) are not well suited for representing arbitrary orientations, as it suffers from gimbal lock and there are multiple parametrizat…
  </blockquote>
</aside>


---

## Post #11 by @Selva (2021-03-11 07:43 UTC)

<p>Thank you Professor <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #12 by @matsuba8 (2022-01-27 19:55 UTC)

<p>Hello Andras,</p>
<p>I’m wondering what the Z, X, and Y axes are in terms of LR, PA, and IS axes?<br>
Thank you,</p>
<p>Michele</p>

---

## Post #13 by @lassoan (2022-01-27 21:48 UTC)

<p>Slicer’s coordinate system axis directions are right, anterior, superior.</p>

---

## Post #14 by @matsuba8 (2022-01-27 23:49 UTC)

<p>Yes, but you mentioned in your earlier post that the code snippet is uses the ZXY rotation order, and I was wondering which axes these correspond to, in the slicer axes?</p>
<p>Thank you,</p>
<p>Michele</p>

---

## Post #15 by @lassoan (2022-01-28 00:57 UTC)

<p>I meant first, second, third coordinate system axis by X, Y, Z . Therefore, X=R, Y=A, Z=S.</p>

---

## Post #16 by @matsuba8 (2022-01-28 00:58 UTC)

<p>Oh my apologies. Thank you very much!!</p>
<p>Michele</p>

---

## Post #17 by @jegberink (2022-11-15 10:50 UTC)

<p>Sorry to revive this, but how would you put this into the XYZ order</p>

---

## Post #18 by @lassoan (2022-11-15 11:56 UTC)

<p>Could you describe a bit more detail ecset you want to achieve?</p>

---

## Post #19 by @jegberink (2022-11-15 14:14 UTC)

<p>So currently i have 3 models of a femur. A preoperative, postoperative and planning. I made a coordinate system that i made from three points of this femur. I allign the coordinate system with the World coordinate system and allign all my femoral shafts as shown here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8be4073b0e1154579d10126ee0bb4daafd8fde36.png" data-download-href="/uploads/short-url/jXwUPChuyIM4JuNdiZVOQOHnsp0.png?dl=1" title="final coordinatesystem, everything alligned" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8be4073b0e1154579d10126ee0bb4daafd8fde36_2_690x456.png" alt="final coordinatesystem, everything alligned" data-base62-sha1="jXwUPChuyIM4JuNdiZVOQOHnsp0" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8be4073b0e1154579d10126ee0bb4daafd8fde36_2_690x456.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8be4073b0e1154579d10126ee0bb4daafd8fde36.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8be4073b0e1154579d10126ee0bb4daafd8fde36.png 2x" data-dominant-color="6F718C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">final coordinatesystem, everything alligned</span><span class="informations">839×555 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>All transformations have been hardened and i measure from the point ive set. Through alpaca i allign the proximal parts to see how they’ve moved.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f63838d0ef47ef03515ad00a02256a003a5a445.png" data-download-href="/uploads/short-url/4tG0yRwd5qNaBKVAbxsfMsM190F.png?dl=1" title="post to pre second" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f63838d0ef47ef03515ad00a02256a003a5a445_2_342x500.png" alt="post to pre second" data-base62-sha1="4tG0yRwd5qNaBKVAbxsfMsM190F" width="342" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f63838d0ef47ef03515ad00a02256a003a5a445_2_342x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f63838d0ef47ef03515ad00a02256a003a5a445.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f63838d0ef47ef03515ad00a02256a003a5a445.png 2x" data-dominant-color="646892"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">post to pre second</span><span class="informations">429×626 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
t and use this transformation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cea03c189f542eab5fea0893f888bdc38bd5896.png" data-download-href="/uploads/short-url/k6AdDCCmSiTuNGSrYElPcNRsb2u.png?dl=1" title="post to planning 22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cea03c189f542eab5fea0893f888bdc38bd5896_2_158x500.png" alt="post to planning 22" data-base62-sha1="k6AdDCCmSiTuNGSrYElPcNRsb2u" width="158" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cea03c189f542eab5fea0893f888bdc38bd5896_2_158x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cea03c189f542eab5fea0893f888bdc38bd5896.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cea03c189f542eab5fea0893f888bdc38bd5896.png 2x" data-dominant-color="8871BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">post to planning 22</span><span class="informations">218×688 50 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I return the euler angles from the matrices with the script as described above. This gives the euler angles in a ZXY order, i would like it to be in a XYZ order if possible.</p>
<p>Thank you so much for your help.</p>

---

## Post #20 by @lassoan (2022-11-15 14:44 UTC)

<p>Each column of the transformation matrix contain direction of one coordinate system axis. Therefore, you can use the same <code>vtkTransform.GetOrientation()</code> method and just reorder the columns of the input transformation matrix. It is probably a good idea to keep the transformation matrix right-handed by swapping columns even numner of times; or swapping columns odd number of times and inverting the direction of one axis.</p>
<p>Note that Euler angles is generally considered to be a poor representation of orientation. Problems include gimbal lock and that the angles don’t have an intuitive meaning when more than one angle is significantly different than 0 (because the second and third rotations are performed around already rotated axes). If you want to characterize misalignment, I would recommend measuring angle between axes in anterior-posterior and lateral projections - similarly how you would measure angles in two planar X-ray projection images. To compute these angles you would not need to arbitrarily choose an ordering of rotation axes.</p>

---

## Post #21 by @jegberink (2022-11-15 15:05 UTC)

<p>I am unfortunately not well acquanted with euler angles. This might be a quite uninformed question.</p>
<p>So i get the euler rotations in ZXY order above. Translation i get from the 4x4 matrix.<br>
For instance as above: i perform a model registration through ALPACA, it gives me a matrix. From this matrix i get the ZXY of euler angles. Now when i put these angles in the ZXY order into a new transformation (with the translational component of the 4x4 matrix) to see if i would again get the same allignment, this does not occur. I know this is a flaw in my understanding of Euler angles, however i cannot seem to find a answer to this.</p>
<p>Im very gratefull for the time you’ve taken to answer my questions.</p>

---

## Post #22 by @lassoan (2022-11-15 16:57 UTC)

<aside class="quote no-group" data-username="jegberink" data-post="21" data-topic="8064">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jegberink/48/16031_2.png" class="avatar"> jegberink:</div>
<blockquote>
<p>From this matrix i get the ZXY of euler angles. Now when i put these angles in the ZXY order into a new transformation (with the translational component of the 4x4 matrix) to see if i would again get the same allignment, this does not occur. I know this is a flaw in my understanding of Euler angles, however i cannot seem to find a answer to this.</p>
</blockquote>
</aside>
<p>Conversion from orientation matrix to Euler angles is not well defined (the same orientation may be represented with various combination of rotations). However, conversion from Euler angles to orientation matrix should always provide the same matrix as the one that the Euler angles are computed from.</p>
<p>You need to play a bit with the order of rotation axes, but the vtkTransform class can be used for both conversions. For example:</p>
<pre data-code-wrap="python"><code class="lang-python">print("=============================")
import random
random.random()
rx = random.random() * 180 - 90
ry = random.random() * 180 - 90
rz = random.random() * 180 - 90
transform = vtk.vtkTransform()
transform.RotateZ(rz)
transform.RotateX(rx)
transform.RotateY(ry)
print(f"Euler angles (original): {rx}, {ry}, {rz}")
print(f"Matrix (original): {transform.GetMatrix()}")

print("--------------")
[rx2, ry2, rz2] = transform.GetOrientation()
transform2 = vtk.vtkTransform()
transform2.RotateZ(rz2)
transform2.RotateX(rx2)
transform2.RotateY(ry2)
print(f"Euler angles (computed from matrix): {rx2}, {ry2}, {rz2}")
print(f"Matrix (from computed Euler angles): {transform2.GetMatrix()}")
</code></pre>
<p>Output:</p>
<pre><code class="lang-auto">=============================
Euler angles (original): 31.012387417137504, -0.18095415482437716, 65.38408784135231
Matrix (original): vtkMatrix4x4 (000001BBE31DC5C0)
  Debug: Off
  Modified Time: 243130
  Reference Count: 2
  Registered Events: (none)
  Elements:
    0.418011 -0.779167 0.467082 0 
    0.908438 0.356992 -0.217478 0 
    0.00270679 0.515223 0.857052 0 
    0 0 0 1 
--------------
Euler angles (computed from matrix): 31.012387417137504, -0.18095415482437716, 65.38408784135231
Matrix (from computed Euler angles): vtkMatrix4x4 (000001BBE31DBC60)
  Debug: Off
  Modified Time: 243145
  Reference Count: 2
  Registered Events: (none)
  Elements:
    0.418011 -0.779167 0.467082 0 
    0.908438 0.356992 -0.217478 0 
    0.00270679 0.515223 0.857052 0 
    0 0 0 1 
</code></pre>

---
