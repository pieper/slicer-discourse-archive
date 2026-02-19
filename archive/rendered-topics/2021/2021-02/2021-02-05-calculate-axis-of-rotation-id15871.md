---
topic_id: 15871
title: "Calculate Axis Of Rotation"
date: 2021-02-05
url: https://discourse.slicer.org/t/15871
---

# Calculate axis of rotation

**Topic ID**: 15871
**Date**: 2021-02-05
**URL**: https://discourse.slicer.org/t/calculate-axis-of-rotation/15871

---

## Post #1 by @Selva (2021-02-05 21:21 UTC)

<p>Hi</p>
<p>Could I ask if there someone has a code to calculate the axis of rotation please.</p>
<p>I have two STL files, bones, which has moved from time point 1 to time point 2.</p>
<p>I want to calculate the displacement. So I calculate the transformation matrix by rigid registration. I would like to find out the axis of rotation, between the two.</p>
<p>Many thanks</p>

---

## Post #2 by @mau_igna_06 (2021-02-05 23:25 UTC)

<p>I think you are looking for the Euler axis. Here is a formula to calculate it given a transformation matrix A:</p><aside class="onebox wikipedia">
  <header class="source">
      <a href="https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions#Rotation_matrix_%E2%86%94_Euler_axis/angle" target="_blank" rel="noopener nofollow ugc">en.wikipedia.org</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:109/113;"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/5/51/Euler_AxisAngle.png/220px-Euler_AxisAngle.png" class="thumbnail" width="109" height="113"></div>

<h3><a href="https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions#Rotation_matrix_%E2%86%94_Euler_axis/angle" target="_blank" rel="noopener nofollow ugc">Rotation formalisms in three dimensions</a></h3>

<p>In geometry, various formalisms exist to express a rotation in three dimensions as a mathematical transformation. In physics, this concept is applied to classical mechanics where rotational (or angular) kinematics is the science of quantitative description of a purely rotational motion. The orientation of an object at a given instant is described with the same tools, as it is defined as an imaginary rotation from a reference placement in space, rather than an actually observed rotation from a pre...</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Selva (2021-02-05 23:32 UTC)

<p>Thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a></p>
<p>I am a medical doctor, so no experience in coding</p>
<p>I am after “axis of rotation” (yes I am calculating Euler angles for rotation)</p>
<p>Is there a code that I can get it</p>
<p>Thanks</p>

---

## Post #4 by @mau_igna_06 (2021-02-06 15:54 UTC)

<p>(the euler angle with euler axis formula is different than yaw, pitch, row angles formula. I think you need the euler axis)</p>
<p>Having into account that you have no programming experience I suggest you open Transforms module and look for the transform matrix you just created. You only need its elements to use the formula. In the formula where it says A13 (for example) it means you need to use the element in first row and third column of matrix A (the matrix you just created). You can calculate each ecuation typing the values and operations in the python interactor. To calculate arccos you can write the line <code>import math</code>, press enter then write  <code>math.acos(X)</code> where X is a number and press enter.<br>
Divisions are done with <code>/</code> character and multiplications are done with <code>*</code> character.<br>
So you can write <code>12/4</code> and the python interactor will print <code>3</code> as the result.<br>
The axis of rotation you want is a vector which components are e1, e2 and e3<br>
To calculate <code>sin</code> you can use <code>math.sin(X)</code> for example in the python interactor you can write <code>math.sin(X)</code> and press enter and it will print <code>0.8414709848078965</code> that is the result.<br>
Here you have example code of how to make basic arithmetic operations in the python interactor (or you can just use a calculator):<br>
<a href="https://www.tutorialspoint.com/python/arithmetic_operators_example.htm" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.tutorialspoint.com/python/arithmetic_operators_example.htm</a></p>

---

## Post #5 by @lassoan (2021-02-07 05:04 UTC)

<aside class="quote no-group" data-username="Selva" data-post="1" data-topic="15871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/13edae/48.png" class="avatar"> Selva:</div>
<blockquote>
<p>Could I ask if there someone has a code to calculate the axis of rotation please.</p>
</blockquote>
</aside>
<p>What do you mean by this exactly? Are you interested in rotation angles? Or, would you like to get the direction of the axis that can orient one model to match the orientation of the other model by a single rotation?</p>
<p>What is the clinical problem you would like to solve/question you want to answer?</p>

---

## Post #6 by @Selva (2021-02-07 05:13 UTC)

<p>Thanks</p>
<p>Yes, I am able to calculate the rotation angles in a given coordinate system</p>
<p>Instantaneous centre of rotation and instantaneous axis of rotation?- axis fixed to a body undergoing planar movement that has zero velocity at a particular instant of time.</p>
<p>Clincal problem- I have wrist bones that I am studying, rotating as the wrist moves.I have 2 models (same bone) , one at time point 1 and second at time point 2.  So I am able to calculate rotation angles using transforms module.</p>
<p>But I would like to calculate the "Instantaneous axis of rotation- from time point 1 to point 2) I believe it is the axis around which the bone rotates. Hope this makes sense</p>

---

## Post #7 by @lassoan (2021-02-07 14:32 UTC)

<p>If you have a single relative transform then copy-paste <a href="https://docs.mdanalysis.org/1.0.0/_modules/MDAnalysis/lib/transformations.html#rotation_from_matrix">this <code>rotation_from_matrix</code> function</a> to the Python console, and then to get rotation axis from a transform node you can run this:</p>
<pre><code class="lang-python">transformNode = getNode('Transform')  # replace 'Transform' with the actual name of your transform node
import numpy as np
import math
transformMatrix = arrayFromTransformMatrix(transformNode)
angle, axisDirection, axisPosition = rotation_from_matrix(transformMatrix)

# Display rotation axis
rotationAxisMarkupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode", "RotationAxis")
rotationAxisMarkupsNode.AddControlPoint(vtk.vtkVector3d(axisPosition[:3]-50*axisDirection))
rotationAxisMarkupsNode.AddControlPoint(vtk.vtkVector3d(axisPosition[:3]+50*axisDirection))
</code></pre>
<p>Getting rotation axis from a single relative transform is probably not very robust or accurate. It would be better to compute an “average” axis from multiple transforms, similarly how Pivot calibration module in SlicerIGT extension does it (see a recent discussion about the algorithm that the module uses <a href="https://discourse.slicer.org/t/what-is-the-algorithm-and-theory-of-spin-calibration/15434/2">here</a>).</p>

---

## Post #8 by @Selva (2021-02-07 21:47 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a><br>
I get an error message NameError: name ‘rotation_from_matrix’ is not defined<br>
Thanks</p>

---

## Post #9 by @lassoan (2021-02-07 21:50 UTC)

<p>Copy-paste <a href="https://docs.mdanalysis.org/1.0.0/_modules/MDAnalysis/lib/transformations.html#rotation_from_matrix">this <code>rotation_from_matrix</code> function</a> to the Python console before running the code snippet above.</p>

---

## Post #10 by @Selva (2021-02-08 11:31 UTC)

<p>Thanks, <a class="mention" href="/u/lassoan">@lassoan</a><br>
Really appreciate your advice, Not sure what I am doing wrong</p>
<p>I get this</p>
<blockquote>
<blockquote>
<blockquote>
<p>def rotation_from_matrix(matrix):<br>
…     “”“Return rotation angle and axis from rotation matrix.<br>
…<br>
…     &gt;&gt;&gt; angle = (random.random() - 0.5) * (2*math.pi)<br>
…     &gt;&gt;&gt; direc = np.random.random(3) - 0.5<br>
…     &gt;&gt;&gt; point = np.random.random(3) - 0.5<br>
…     &gt;&gt;&gt; R0 = rotation_matrix(angle, direc, point)<br>
…     &gt;&gt;&gt; angle, direc, point = rotation_from_matrix(R0)<br>
…     &gt;&gt;&gt; R1 = rotation_matrix(angle, direc, point)<br>
…     &gt;&gt;&gt; is_same_transform(R0, R1)<br>
…     True<br>
…<br>
…     “””<br>
…     R = np.array(matrix, dtype=np.float64, copy=False)<br>
…     R33 = R[:3, :3]<br>
…     # direction: unit eigenvector of R33 corresponding to eigenvalue of 1<br>
…     l, W = np.linalg.eig(R33.T)<br>
…     i = np.where(abs(np.real(l) - 1.0) &lt; 1e-8)[0]<br>
…     if not len(i):<br>
…         raise ValueError(“no unit eigenvector corresponding to eigenvalue 1”)<br>
…     direction = np.real(W[:, i[-1]]).squeeze()<br>
…     # point: unit eigenvector of R33 corresponding to eigenvalue of 1<br>
…     l, Q = np.linalg.eig(R)<br>
…     i = np.where(abs(np.real(l) - 1.0) &lt; 1e-8)[0]<br>
…     if not len(i):<br>
…         raise ValueError(“no unit eigenvector corresponding to eigenvalue 1”)<br>
…     point = np.real(Q[:, i[-1]]).squeeze()<br>
…     point /= point[3]<br>
…     # rotation angle depending on direction<br>
…     cosa = (np.trace(R33) - 1.0) / 2.0<br>
…     if abs(direction[2]) &gt; 1e-8:<br>
…         sina = (R[1, 0] + (cosa - 1.0) * direction[0] * direction[1]) / direction[2]<br>
…     elif abs(direction[1]) &gt; 1e-8:<br>
…         sina = (R[0, 2] + (cosa - 1.0) * direction[0] * direction[2]) / direction[1]<br>
…     else:<br>
…         sina = (R[2, 1] + (cosa - 1.0) * direction[1] * direction[2]) / direction[0]<br>
…     angle = math.atan2(sina, cosa)<br>
…     return angle, direction, point<br>
…</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>transformNode = getNode(‘LinearTransform_3’)<br>
import numpy as np<br>
import math<br>
transformMatrix = arrayFromTransformMatrix(transformNode)<br>
angle, axisDirection, axisPosition = rotation_from_matrix(transformMatrix)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘rotation_from_matrix’ is not defined</p>
</blockquote>
</blockquote>
</blockquote>
</blockquote>
</blockquote>
</blockquote>

---

## Post #11 by @lassoan (2021-02-08 19:24 UTC)

<p>Copy-paste the <code>rotation_from_matrix</code> function implementation to the Python console first (that you included in the top of your previous post). After you copy-paste and hit Enter key once or twice, you should see the command prompt (<code>&gt;&gt;&gt;</code>) again and no error message. That means that the function is now available.</p>
<p>You can then copy-paste the rest of the code to the Python console.</p>

---

## Post #12 by @Selva (2021-02-09 04:12 UTC)

<p>Thanks a lot.</p>
<p>It worked fine, I trialled with two models (create model module)  with known rotation. Thank you very much. It draws the AoR on the 3D viewer.</p>
<p>I have two questions.</p>
<ol>
<li>
<p>How to get a numerical value for this axis. (With the code, in the console, it types 0 or 1 only, I do not get a value)</p>
</li>
<li>
<p>I have pasted an image of my transform (resulted by model registration). _this is after registering bone position 1 to position two using ICP. When I apply the same code for this transformation matrix- Linear transform 5 in this case- All models disappear. (I have positioned my models centred on the coordinate system o, o, o)</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67b2ccc62d6449b6ce8cfad169da9e9b9c4e1435.png" data-download-href="/uploads/short-url/eNmfTSHopT63WYWghFdl3jAJauh.png?dl=1" title="Screenshot 2021-02-09 at 14.42.11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67b2ccc62d6449b6ce8cfad169da9e9b9c4e1435_2_690x463.png" alt="Screenshot 2021-02-09 at 14.42.11" data-base62-sha1="eNmfTSHopT63WYWghFdl3jAJauh" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67b2ccc62d6449b6ce8cfad169da9e9b9c4e1435_2_690x463.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67b2ccc62d6449b6ce8cfad169da9e9b9c4e1435_2_1035x694.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67b2ccc62d6449b6ce8cfad169da9e9b9c4e1435_2_1380x926.png 2x" data-dominant-color="E8E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-02-09 at 14.42.11</span><span class="informations">1588×1066 66.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2021-02-10 04:03 UTC)

<aside class="quote no-group" data-username="Selva" data-post="12" data-topic="15871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/13edae/48.png" class="avatar"> Selva:</div>
<blockquote>
<p>When I apply the same code for this transformation matrix- Linear transform 5 in this case- All models disappear. (I have positioned my models centred on the coordinate system o, o, o)</p>
</blockquote>
</aside>
<p>I think, this is expected for real-life motion, where you cannot ensure that the rotation happens exactly along a single axis. In general, an orientation difference cannot be described by rotation along a single axis, but you need to rotate along two axes (or around a point). If you have several (preferably dozens) of different poses then from those you can compute an average instantaneous axis of rotation, even if there are slight additional rotations (similarly how <a href="https://discourse.slicer.org/t/what-is-the-algorithm-and-theory-of-spin-calibration/15434/3">Pivot calibration module</a> computes the rotation axis in SlicerIGT extension), but I’m not sure if this can be applied to just two poses.</p>
<p><a class="mention" href="/u/mholden8">@mholden8</a> Do you have any recommendation?</p>

---

## Post #14 by @Selva (2021-02-12 22:01 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I elicited the same behaviour with the created models. Whenever I introduce few mm translation to a model, this happens.</p>
<p>I think that is the reason with the bones. If I strictly take two STL files (of the same bone), which only is slightly displaced between time points (10-15 degrees of rotation in all three planes and 1-3 mm translation ) I believe, I still give a ‘theoretical’ instantaneous axis of rotation.</p>
<p>What are your thoughts? Thanks</p>

---

## Post #15 by @lassoan (2021-02-13 00:56 UTC)

<p>The function that I’ve found and linked above can only compute the instantaneous axis of rotation if it exists (if the transformation can be reproduced by rotation along a single axis). If you also have a translation component then this computation fails. There are infinite number of solutions for decomposing a linear transformation to rotation along a single axis and some additional rotations and/or translations and you need to figure out that in what sense you would like an optimal solution. I would suggest to find papers in your field that compute the rotation axis and try to implement the method that they describe (or if it is not clear how exactly they do it then contact them and ask for the implementation). If you have an exact computation formula or implementation in any language then we can help with porting it to Python/Slicer. You may also contract an R&amp;D company, such as Kitware, or a computational geometry expert to work this out for you.</p>

---

## Post #16 by @Selva (2021-02-13 23:07 UTC)

<p>Thanks for advice <a class="mention" href="/u/lassoan">@lassoan</a><br>
I will define the calculation a bit more from previous work<br>
(Also will update slicer support so that if we can have this functionality, it will be useful for the users, As any bone that moves in human body is likely to have a translational component, even its few mm)</p>

---

## Post #17 by @Selva (2021-02-24 06:38 UTC)

<p>Thanks for kind support <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Found this, after some research</p>
<p>"Similarly we can also calculate backwards and find the intantanous axis of rotation at some distance<br>
−<br>
⃗<br>
r<br>
from any point if we know the linear velocity of the point and the angular velocity. This is given by:</p>
<p>[\begin{equation} \label{eq:2} -\vec{r}= \frac{\vec{\omega} \times \vec{v}_P }{ \vec{\omega}\cdot\vec{\omega} } \end{equation}]<br>
Thus if know the position of a point<br>
⃗<br>
r<br>
P<br>
, its linear velocity<br>
⃗<br>
v<br>
P<br>
we can find closest point<br>
⃗<br>
r<br>
C<br>
on the rotation axis as:</p>
<p>[\vec{r}_C = \vec{r}_P - \vec{r} = \vec{r}_P + \frac{\vec{\omega}\times\vec{v}_P}{\vec{\omega}\cdot\vec{\omega} }]</p>
<p>Script</p>
<pre><code class="lang-auto">   AnyKinRotational Rotational ={
     AngVelOnOff = On;
     AnyRefFrame&amp; Ref1= .ReferenceFrame;
   }; 

   AnyKinLinear Linear ={
     Ref=-1;
     AnyRefFrame&amp; Ref1= .ReferenceFrame;
   };
   
   /// Direction of the instantaneous axis of rotation
   AnyVec3 e_iaor = Rotational.Vel/vnorm(Rotational.Vel)

   /// The point on the rotation axis closest to ReferenceFrame origin
   AnyVec3 r_iaor = Linear.Pos + cross(Rotational.Vel, Linear.Vel)/(vnorm(Rotational.Vel)^2);
</code></pre>
<p>Unfortunately I cant use the same software, as it only runs on Windows<br>
Is there any possibility that slicer could enable this function, Thanks</p>

---

## Post #18 by @lassoan (2021-02-25 06:45 UTC)

<p>I cannot decipher neither the formulae nor the code. Can you provide a link to the source of this code snippet?</p>

---
