---
topic_id: 19446
title: "Creating A New Coordinate System"
date: 2021-08-31
url: https://discourse.slicer.org/t/19446
---

# Creating a new coordinate system

**Topic ID**: 19446
**Date**: 2021-08-31
**URL**: https://discourse.slicer.org/t/creating-a-new-coordinate-system/19446

---

## Post #1 by @matsuba8 (2021-08-31 18:27 UTC)

<p>Hello all,</p>
<p>I am trying to create a local coordinate system within the global coordinate system in order to compute the displacement of a bone block between two different scans. The reason why the global coordinate system does not suffice is because I would like the rotational displacement of the bone block to be in terms of the orientation of the reference bone block rather than the global space.</p>
<p>Could someone please provide some guidance on how to create a local coordinate system?</p>
<p>Thank you very much in advance,</p>
<p>Michele</p>

---

## Post #2 by @Fluvio_Lobo (2021-09-01 03:41 UTC)

<p><a class="mention" href="/u/matsuba8">@matsuba8</a>,</p>
<p>I am not sure about creating a ‘local’ coordinate system, but here are two things that have worked for me in the recent past;</p>
<ol>
<li>
<p><strong>Center all of your models to the origin of the scene itself.</strong> You can do this through the Python interactor by calculating the centroid of your model, then the distance between the centroid and the origin, and then translating the model to the origin. If you do this, then your rotation will be about the centroid of the model, as you would hope. If you have a secondary model that can be placed at an arbitrary distance from the origin, now you know that arc-length of its rotation. This may take a bit of programming, but it has helped me in a few workflows I am developing <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=10" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>
</li>
<li>
<p><strong>You can rotate nodes in slicer about ‘points’ or ‘lines’ using the Python interactor <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-line" rel="noopener nofollow ugc">also</a></strong>. Maybe you only need one of your objects to rotate about a long bone, where the length of the bone is defined as axis of rotation…?</p>
</li>
</ol>
<p>Perhaps you can expand a little on your intended goal and current problem. What are these ‘bone blocks’? Are you trying to recreate the rotation of a joint from bones segmented from different scans?</p>
<p>Let me know!</p>

---

## Post #3 by @matsuba8 (2021-09-01 16:12 UTC)

<p>Hi Fluvio,</p>
<p>Thank you very much for your reply!</p>
<ol>
<li>I’ve used the same method as you for translating the centroid to the origin, but I didn’t know there was a way to use the arc-length to calculate the rotation! This is good to know. I am quite an inexperienced coder (and by that I mean 0 experience, haha), but this seems very useful!</li>
<li>I have not tried this method, but it may not be ideal, as it is crucial in my project that the three axes are orthogonal to one another.</li>
</ol>
<p>To explain my project further, I have attached images below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd664e5195bcb90731c10172ad13564af70b0e15.jpeg" data-download-href="/uploads/short-url/r1vqKa9a5cpvnyo4rOYcFTYxNKl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd664e5195bcb90731c10172ad13564af70b0e15_2_345x215.jpeg" alt="image" data-base62-sha1="r1vqKa9a5cpvnyo4rOYcFTYxNKl" width="345" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd664e5195bcb90731c10172ad13564af70b0e15_2_345x215.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd664e5195bcb90731c10172ad13564af70b0e15_2_517x322.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd664e5195bcb90731c10172ad13564af70b0e15_2_690x430.jpeg 2x" data-dominant-color="A2A2A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1380×862 98.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e7eebe7a439e0d6cd3e40f939237f8eeea07171.jpeg" data-download-href="/uploads/short-url/8URwW44HduIzWUaqOG0lBMO0TvP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e7eebe7a439e0d6cd3e40f939237f8eeea07171_2_345x215.jpeg" alt="image" data-base62-sha1="8URwW44HduIzWUaqOG0lBMO0TvP" width="345" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e7eebe7a439e0d6cd3e40f939237f8eeea07171_2_345x215.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e7eebe7a439e0d6cd3e40f939237f8eeea07171_2_517x322.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3e7eebe7a439e0d6cd3e40f939237f8eeea07171_2_690x430.jpeg 2x" data-dominant-color="A2A2A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1380×862 98.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The model seen in the 3D view is the bone block of interest, and the blue model is the neutral condition while the red model is the condition (models are overlaid on top of each other). While they  appear to be registered, they are not, as the difference in rotation we are looking for is expected to be ≤ 1˚. In the images attached, the centroids of both the neutral and the condition bone block have been moved to the origin.<br>
Our objective is to find the amount of translation and rotation of the condition bone block relative to the neutral bone block.<br>
In method <span class="hashtag">#1</span> which you have explained in your reply, did you move the centroids of both models to the origin? or just the reference model?<br>
Further, it would be awesome if you could provide me with some guidance as to where I could learn the coding for using the arc length to calculate the rotation.</p>
<p>Thank you!</p>
<p>Michele</p>
<p>P.S. Please note that the red axes in both images were added to a screenshot rather than created in 3d slicer. The top image represents the global coordinate system, and the second image is what I was hoping for the local coordinate system to look like.</p>

---

## Post #4 by @Fluvio_Lobo (2021-09-01 17:34 UTC)

<p><a class="mention" href="/u/matsuba8">@matsuba8</a>,</p>
<p>Glad I could help!<br>
I am also happy you shared more details, as I think there are better strategies that can help you.</p>
<blockquote>
<p>Our objective is to find the amount of translation and rotation of the condition bone block relative to the neutral bone block.</p>
</blockquote>
<p>Two approaches;</p>
<ol>
<li>
<p><strong><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance" rel="noopener nofollow ugc">Model-to-Model Distance</a></strong>. Since the “bone blocks” are similar in shape, you could use this module to calculate the point-to-point displacement between the two. I am pretty sure you can then use this displacement map to approximate an overall transformation matrix that describes the overall translation and rotation matrix that describes the displacement of the part.</p>
</li>
<li>
<p><strong><a href="https://github.com/SlicerIGT/SlicerIGT" rel="noopener nofollow ugc">Fiducial Registration Wizard</a></strong>. You can use fiducials to determine the rigid transformation that describes the displacement of the part. This module returns the transformation matrix itself! You have to download the SlicerIGT module to use this tool.</p>
</li>
</ol>
<blockquote>
<p>In method <span class="hashtag-raw">#1</span> which you have explained in your reply, did you move the centroids of both models to the origin? or just the reference model?<br>
Further, it would be awesome if you could provide me with some guidance as to where I could learn the coding for using the arc length to calculate the rotation.</p>
</blockquote>
<p>If you use the two new solutions I propose here, you wont need to program at all <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=12" title=":rofl:" class="emoji" alt=":rofl:" loading="lazy" width="20" height="20">. Assuming the result is what you want of course.</p>
<p>Now, I guess the other question is… are the frames of reference aligned? In other words, are the two imaging datasets (DICOM) aligned? If they are not, you may need to align them to remove that additional transformation from your final displacement. Does that make sense?</p>

---

## Post #5 by @matsuba8 (2021-09-01 17:55 UTC)

<p>Hi again,</p>
<p>I have not tried using</p>
<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="4" data-topic="19446">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p><strong><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance" rel="noopener nofollow ugc">Model-to-Model Distance</a></strong> .</p>
</blockquote>
</aside>
<p>yet, but I have tried using the IGT model registration module. The only problem with this is that when I use the matrix to extract the rotational values, it’s in terms of the global coordinate system. I have attached an image with planes running through the model, to demonstrate how I would like the coordinate system to be oriented.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc08d463ab413d5e99dd6e717d1d348450acee24.jpeg" data-download-href="/uploads/short-url/qPqGh7vTM1gn635N6tOgfTJxsgI.jpeg?dl=1" title="Screen Shot 2021-08-26 at 9.00.20 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc08d463ab413d5e99dd6e717d1d348450acee24_2_345x215.jpeg" alt="Screen Shot 2021-08-26 at 9.00.20 PM" data-base62-sha1="qPqGh7vTM1gn635N6tOgfTJxsgI" width="345" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc08d463ab413d5e99dd6e717d1d348450acee24_2_345x215.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc08d463ab413d5e99dd6e717d1d348450acee24_2_517x322.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc08d463ab413d5e99dd6e717d1d348450acee24_2_690x430.jpeg 2x" data-dominant-color="BDBFDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-26 at 9.00.20 PM</span><span class="informations">1920×1200 91.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In terms of</p>
<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="4" data-topic="19446">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p><strong><a href="https://github.com/SlicerIGT/SlicerIGT" rel="noopener nofollow ugc">Fiducial Registration Wizard</a></strong> .</p>
</blockquote>
</aside>
<p>I am unsure whether the bone blocks have enough reliable landmarks for it to be accurate. Further, I believe the same problem regarding the coordinate system still exists for this method.</p>
<p>I have aligned the two datasets already:)</p>

---

## Post #6 by @mau_igna_06 (2021-09-01 18:01 UTC)

<p>This bone looks like a thick elliptical disk. If I were you I would make PCA to the points of the bone mesh. With that you would get two vectors that you could use to create a frame (coordinate system) I think. Hope it helps</p>

---

## Post #7 by @Fluvio_Lobo (2021-09-01 18:37 UTC)

<p><a class="mention" href="/u/matsuba8">@matsuba8</a>,</p>
<p>What about;</p>
<ol>
<li>Moving both models to the center of the scene (origin)</li>
<li>Creating three orthogonal planes that delineate the local coordinate system (or more like the basis) on both models (e.g. xy1, xz1, yz1, xy2, xz2, yz2)… similar to what you did on your screenshot…</li>
<li>Calculate the angles between corresponding planes using the Python interactor and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-markup-planes" rel="noopener nofollow ugc">this example</a>… this should be equivalent to a dot product between vectors, so the angle will not be tied to the overall coordinate system as in “angle planes” module you are using.</li>
</ol>
<p>The challenge here is making sure those planes are made with the same features/landmarks on the model. My guess is that you already thought of this though.</p>

---

## Post #8 by @matsuba8 (2021-09-01 20:37 UTC)

<p>Hello Mauro,</p>
<p>Thank you for your response. I am unfamiliar with the term PCA, but is that “Principal Components Analysis”?<br>
I will look into this, thanks again.</p>
<p>Michele</p>

---

## Post #9 by @matsuba8 (2021-09-01 20:39 UTC)

<p>Hi again Fluvio,</p>
<p>Yes, I have thought about this but I haven’t found a way to make sure that the planes are orthogonal to each other… Do you know how to do this?<br>
Perhaps if I can find a way to ensure this, calculating the angles between the corresponding planes is my best bet!</p>
<p>Michele</p>

---

## Post #10 by @mau_igna_06 (2021-09-01 21:06 UTC)

<p>Yes. I’m referring to Principal Component Analysis</p>

---

## Post #11 by @mikebind (2021-09-01 21:28 UTC)

<p>If you have a linear transformation matrix which takes the position of one bone block to the other (as can be produced as an output from any Slicer registration technique), you can easily extract the rotation component of that transform using a module I developed for Slicer called CharacterizeTransformMatrix (available at <a href="https://github.com/mikebind/SlicerCharacterizeTransformMatrix" class="inline-onebox" rel="noopener nofollow ugc">GitHub - mikebind/SlicerCharacterizeTransformMatrix</a>).  I’m not sure what you want to use the new coordinate system for, but if you just want to know how rotated one block is relative to the other, this module will answer that.</p>

---

## Post #12 by @Fluvio_Lobo (2021-09-02 01:24 UTC)

<p><a class="mention" href="/u/matsuba8">@matsuba8</a>,</p>
<p>Give PCA a try. I am not familiar with the process myself but I think this will ensure your analysis process carries less user error. Also, PCA seems like the more scalable solution.</p>
<p>If you still want to do something with planes, let me know!</p>

---

## Post #13 by @mau_igna_06 (2021-09-02 19:42 UTC)

<p>Your module looks good and I think it will be very useful for lots of Slicer users.</p>
<p>Although I didn’t catch how you calculate the scaleMatrices from the eigenvectors and eigenValues here: <a href="https://github.com/mikebind/SlicerCharacterizeTransformMatrix/blob/bde60887b7291c5ffd337e382f469ed5aadaf569/CharacterizeTransformMatrix/CharacterizeTransformMatrix.py#L323-L325" rel="noopener nofollow ugc">https://github.com/mikebind/SlicerCharacterizeTransformMatrix/blob/bde60887b7291c5ffd337e382f469ed5aadaf569/CharacterizeTransformMatrix/CharacterizeTransformMatrix.py#L323-L325</a></p>
<p>I suppose you have some formula to create a symmetric matrix but it’s just a guess.</p>

---

## Post #14 by @mikebind (2021-09-02 20:22 UTC)

<p>Yes, each scale matrix is symmetric, and is constructed by computing the outer product of the eigenvector with itself (which is symmetric by construction), multiplying that by the (eigenvalue - 1) and adding the result to the identity matrix. Each scale matrix has the effect of stretching vectors by a factor of the eigenvalue in the direction of the eigenvector (for the eigenvalue and eigenvector used to construct it).</p>
<aside class="onebox stackexchange" data-onebox-src="https://math.stackexchange.com/questions/237369/given-this-transformation-matrix-how-do-i-decompose-it-into-translation-rotati/417813#417813">
  <header class="source">

      <a href="https://math.stackexchange.com/questions/237369/given-this-transformation-matrix-how-do-i-decompose-it-into-translation-rotati/417813#417813" target="_blank" rel="noopener nofollow ugc">math.stackexchange.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://math.stackexchange.com/users/61427/merv" target="_blank" rel="noopener nofollow ugc">
    <img alt="merv" src="https://www.gravatar.com/avatar/27ce5101af57acecf9a5fe563b6192b1?s=128&amp;d=identicon&amp;r=PG" class="thumbnail onebox-avatar" width="128" height="128">
  </a>

<h4>
  <a href="https://math.stackexchange.com/questions/237369/given-this-transformation-matrix-how-do-i-decompose-it-into-translation-rotati/417813#417813" target="_blank" rel="noopener nofollow ugc">Given this transformation matrix, how do I decompose it into translation, rotation and scale matrices?</a>
</h4>

<div class="tags">
  <strong>matrices</strong>
</div>

<div class="date">
  
  answered by
  <a href="https://math.stackexchange.com/users/61427/merv" target="_blank" rel="noopener nofollow ugc">
    merv
  </a>
  on <a href="https://math.stackexchange.com/questions/237369/given-this-transformation-matrix-how-do-i-decompose-it-into-translation-rotati/417813#417813" target="_blank" rel="noopener nofollow ugc">08:05PM - 11 Jun 13 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #15 by @mau_igna_06 (2021-09-02 20:41 UTC)

<p>Thanks. That was a good explanation. I didn’t know that formula</p>

---

## Post #16 by @lassoan (2021-09-03 04:40 UTC)

<p>You can define a coordinate system using a markups plane node:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fd6fd42bfe7e90bf0b890105aa4424e79e42ae5.jpeg" data-download-href="/uploads/short-url/boikCzGpiFFwX5LNcAuEO8jNLBb.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd6fd42bfe7e90bf0b890105aa4424e79e42ae5_2_543x500.jpeg" alt="image" data-base62-sha1="boikCzGpiFFwX5LNcAuEO8jNLBb" width="543" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd6fd42bfe7e90bf0b890105aa4424e79e42ae5_2_543x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd6fd42bfe7e90bf0b890105aa4424e79e42ae5_2_814x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd6fd42bfe7e90bf0b890105aa4424e79e42ae5_2_1086x1000.jpeg 2x" data-dominant-color="7C7A84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1324×1217 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The advantage of using this instead of a transform that you can conveniently place the node using 3 points and then further adjust its position and orientation using interaction handles.</p>
<p>Once you have defined the plane, you can get the the transform between this coordinate system and the RAS coordinate system like this:</p>
<pre><code class="lang-python">planeToWorld = vtk.vtkMatrix4x4()
getNode('P').GetObjectToWorldMatrix(planeToWorld)
</code></pre>
<p>If you concatenate this transform with the result of the model registration then you’ll get the rotation and translation between the bones in the plane coordinate system.</p>

---

## Post #17 by @matsuba8 (2021-09-13 17:52 UTC)

<p>Hello Andras,</p>
<p>Thank you very much for your response!<br>
I just had a question while I was attempting this method: Is there a code to place a fiducial at a specific coordinate?<br>
For example, as seen in the image below, the centroid of the red segment is at (-110.676, -105.632, 31.2008), and I would like to set my ‘P’ fiducial at this point.</p>
<p>Thank you for your help in advance.<br>
Best,</p>
<p>Michele</p>

---

## Post #18 by @lassoan (2021-09-13 18:36 UTC)

<aside class="quote no-group" data-username="matsuba8" data-post="17" data-topic="19446">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/59ef9b/48.png" class="avatar"> matsuba8:</div>
<blockquote>
<p>Is there a code to place a fiducial at a specific coordinate?</p>
</blockquote>
</aside>
<p>You can use <a href="http://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#ae2b237c8d8ca2bbb6c304263f2800720">markupsNode.SetNthControlPointPositionWorld(i, r, a, s)</a> method.</p>

---

## Post #19 by @mau_igna_06 (2021-11-05 12:58 UTC)

<p>I think this it is a common need to define a frame that follows some principal directions of the model. I’ve created a script for this. Also, it allows interaction to transform the model and give it different position/orientation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea5a68f1130fc2f4ec8c1344442ecd571e4a3861.png" data-download-href="/uploads/short-url/xrbqGHw5YewZfzvjX8CcnRmRNbr.png?dl=1" title="frameOfTibiaInPCDirections" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea5a68f1130fc2f4ec8c1344442ecd571e4a3861_2_690x499.png" alt="frameOfTibiaInPCDirections" data-base62-sha1="xrbqGHw5YewZfzvjX8CcnRmRNbr" width="690" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea5a68f1130fc2f4ec8c1344442ecd571e4a3861_2_690x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea5a68f1130fc2f4ec8c1344442ecd571e4a3861.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea5a68f1130fc2f4ec8c1344442ecd571e4a3861.png 2x" data-dominant-color="9B9DCA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">frameOfTibiaInPCDirections</span><span class="informations">846×612 25.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is the code:</p>
<pre><code class="lang-auto">#Create a frame for the model in the principal components directions, 
#set up a plane with interaction handles to move it.
#The script can be reused to allow interactions with n models

import numpy as np

#Change this number for more accuracy (more points, take more time to compute)
numberOfSampledPointsOfModel = 2000
model = getNode('mymodel')

maskPointsFilter = vtk.vtkMaskPoints()
maskPointsFilter.SetInputData(model.GetPolyData())

if model.GetPolyData().GetNumberOfPoints() &gt; numberOfSampledPointsOfModel:
  ratio = round(model.GetPolyData().GetNumberOfPoints()/numberOfSampledPointsOfModel)
else:
  ratio = 1

#This works but the sampling could be biased spatially I think
#If you have vtk9 you should use  UNIFORM_SPATIAL_SURFACE option
maskPointsFilter.SetOnRatio(ratio)
maskPointsFilter.RandomModeOn()
maskPointsFilter.Update()

polydata = vtk.vtkPolyData()
polydata.ShallowCopy(maskPointsFilter.GetOutput())

#Calculate the SVD and mean
from vtk.util.numpy_support import vtk_to_numpy
modelPoints = vtk_to_numpy(polydata.GetPoints().GetData())

# Calculate the mean of the points, i.e. the 'center' of the cloud
modelPointsMean = modelPoints.mean(axis=0)

# Do an SVD on the mean-centered data.
uu0, dd0, eigenvectors0 = np.linalg.svd(modelPoints - modelPointsMean)

# Create a frame for the model
modelZ = np.zeros(3)
modelX = eigenvectors0[0]
modelY = eigenvectors0[1]
vtk.vtkMath.Cross(modelX, modelY, modelZ)
modelZ = modelZ/np.linalg.norm(modelZ)
modelOrigin = modelPointsMean

#Create the plane to move the model
planeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsPlaneNode", slicer.mrmlScene.GetUniqueNameByString("modelToWorldPlane"))
slicer.modules.markups.logic().AddNewDisplayNodeForMarkupsNode(planeNode)

displayNode = planeNode.GetDisplayNode()
displayNode.SetGlyphScale(2.5)
displayNode.SetOpacity(0)
displayNode.HandlesInteractiveOn()

planeNode.SetAxes(modelX,modelY,modelZ)
planeNode.SetOrigin(modelOrigin)

#Create the transformNode that the model will observe
planeToWorldTransformNode = slicer.vtkMRMLLinearTransformNode()
planeToWorldTransformNode.SetName(slicer.mrmlScene.GetUniqueNameByString("planeToWorld"))
slicer.mrmlScene.AddNode(planeToWorldTransformNode)

#Save initial transform of the plane
worldToInitialModelTransformNode = slicer.vtkMRMLLinearTransformNode()
worldToInitialModelTransformNode.SetName(slicer.mrmlScene.GetUniqueNameByString("worldToInitialModel"))
slicer.mrmlScene.AddNode(worldToInitialModelTransformNode)

SLICER_CHANGE_OF_API_REVISION = '29927'
planeToWorldMatrix = vtk.vtkMatrix4x4()
if int(slicer.app.revision) &gt; int(SLICER_CHANGE_OF_API_REVISION):
  planeNode.GetObjectToWorldMatrix(planeToWorldMatrix)
else:
  planeNode.GetPlaneToWorldMatrix(planeToWorldMatrix)

planeToWorldTransformNode.SetMatrixTransformToParent(planeToWorldMatrix)
planeNode.SetAttribute('planeNodeToWorldTransformNodeID',planeToWorldTransformNode.GetID())

worldToInitialModelMatrix = vtk.vtkMatrix4x4()
worldToInitialModelMatrix.DeepCopy(planeToWorldMatrix)
worldToInitialModelMatrix.Invert()

worldToInitialModelTransformNode.SetMatrixTransformToParent(worldToInitialModelMatrix)
planeNode.SetAttribute('worldToInitialModelTransformNodeID',worldToInitialModelTransformNode.GetID())

model.SetAndObserveTransformNodeID(worldToInitialModelTransformNode.GetID())
worldToInitialModelTransformNode.SetAndObserveTransformNodeID(planeToWorldTransformNode.GetID())

###THIS PART SHOULD ONLY BE COPYPASTED ONCE TILL MARKED
#update model's position/orientation interactively
def onPlaneModified(sourceNode,event):
  SLICER_CHANGE_OF_API_REVISION = '29927'
  planeToWorldMatrix = vtk.vtkMatrix4x4()
  if int(slicer.app.revision) &gt; int(SLICER_CHANGE_OF_API_REVISION):
    sourceNode.GetObjectToWorldMatrix(planeToWorldMatrix)
  else:
    sourceNode.GetPlaneToWorldMatrix(planeToWorldMatrix)
  
  planeNodeToWorldTransformNode = slicer.mrmlScene.GetNodeByID(sourceNode.GetAttribute('planeNodeToWorldTransformNodeID'))
  planeNodeToWorldTransformNode.SetMatrixTransformToParent(planeToWorldMatrix)

planeNodesAndObservers = []
###TILL HERE SHOULD ONLY BE COPYPASTED ONCE

planeNodesAndObservers.append(
  [planeNode,planeNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent,onPlaneModified)]
)




#If you want to stop interactions for plane i, do this:
i = 0#change this number
planeNodesAndObservers[i][0].RemoveObserver(planeNodesAndObservers[i][1])



#If you want the model to world transform AFTER YOU MOVE IT for plane i, do this:
i = 0#change this number
worldToInitialModelTransformNode = slicer.mrmlScene.GetNodeByID(planeNodesAndObservers[i][0].GetAttribute('worldToInitialModelTransformNodeID'))
modelToWorldMatrix = vtk.vtkMatrix4x4()
worldToInitialModelTransformNode.GetMatrixTransformToWorld(modelToWorldMatrix)
print(modelToWorldMatrix)



#If you just want to define a frame for the model (assigned to plane i), do this:
i = 0#change this number
worldToInitialModelTransformNode = slicer.mrmlScene.GetNodeByID(planeNodesAndObservers[i][0].GetAttribute('worldToInitialModelTransformNodeID'))
initialModelToWorldMatrix = vtk.vtkMatrix4x4()
worldToInitialModelTransformNode.GetMatrixTransformToParent(initialModelToWorldMatrix)
initialModelToWorldMatrix.Invert()
print(initialModelToWorldMatrix)
</code></pre>
<p><a class="mention" href="/u/lassoan">@lassoan</a> maybe this can be added to the script repository</p>

---

## Post #20 by @lassoan (2021-11-05 14:52 UTC)

<p>Thank you <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> this is example works very nicely. It would be probably too long for including it entirely in the script repository but you can upload it into a gist and we can link it from the script repository (as we do it for other longer examples). Gists are version controlled, so you can update the gist and the same link will automatically post to the latest version (and user has access to previous versions of the gist, too).</p>
<p>There are also a few things to fix/improve, such as:</p>
<ul>
<li>Node IDs are not persistent (when you save the scene and load it again a different ID may be assigned to the node), therefore they must never stored in node attributes. Instead, node references can be used, which maintain link between nodes, even if the node IDs change. Since parent transform is already stored using node references, you don’t even need to add another node reference.</li>
<li>Simplify the sampling. If ratio=1 then just use the model output and skip the filter. It would be also more relevant to use the VTK9 filter, as VTK8 will not be around for long.</li>
<li>Always leave a space after the <code>#</code> character</li>
<li>Instead of hardcoding any specific revision, put the method call in a try/except block (put the more recent API in the main path and the old API in the except path), as it is more pythonic and may be faster (not that speed would matter here, just as a general note)</li>
<li>Instead of updating the transform in the main path and then implementing it again in onPlaneModified function, just call onPlaneModified once.</li>
<li>I would remove the multiple planes support and the <code>i</code> variable to keep things simple.</li>
<li>Remove the <code>THIS PART SHOULD ONLY BE COPYPASTED ONCE TILL MARKED</code> comments. It is understood that the entire code snippet is to be executed once. It would just confuse users that they are not allowed to copy-paste some parts.</li>
<li>Comment out the …RemoveObserver… line so that if the user copy-pastes the entire code snippet the axes are kept interactive</li>
</ul>
<p>Two notes for using principal axes of surface mesh points as object coordinate system:</p>
<ol>
<li>
<p>For solid objects Segment Statistics module gives more relevant axis directions. Principal X, Y, Z axes computed by Segment Statistics provides the object’s true principal axes of inertia, based on its volume. PCA of surface mesh points can be quite similar for many shapes, but they are not the same. Even if you sample the surface uniformly, a small feature with a large surface area can throw off the axis directions computed by surface mesh points PCA.</p>
</li>
<li>
<p>For models that have flat sides (such as CAD models) Segment Statistics module’s oriented bounding box axis directions are more relevant than principal axes. The oriented bounding box axes will not be slightly off if you have small attachments or engravings in the object, but the axes will be generally aligned with flat sides.</p>
</li>
</ol>

---

## Post #21 by @mau_igna_06 (2021-11-05 19:58 UTC)

<p>All changes done except this one:</p>
<blockquote>
<p>It would be also more relevant to use the VTK9 filter, as VTK8 will not be around for long.</p>
</blockquote>
<p>I’ll update the gist when Slicer changes VTK version.</p>
<p>Thanks for the notes.</p>
<p>Here is the gist: <a href="https://gist.github.com/mauigna06/434784dac9e5704198b80b179e037d0e" class="inline-onebox" rel="noopener nofollow ugc">Create a frame for the model in the principal components directions, set up a plane with interaction handles to move it. · GitHub</a></p>
<p>Do you know if the option <a href="https://vtk.org/doc/nightly/html/classvtkMaskPoints.html#aebcc12a9a5f2045e1d9c80ba358e392ea2c411bb42a81fff5f7495b754e3e7a45" rel="noopener nofollow ugc">UNIFORM_SPATIAL_VOLUME</a> for the maskPointsFilter will make it return points inside the volume of the mesh? We could try that for this script later, maybe it would give more robust results…</p>

---

## Post #22 by @mau_igna_06 (2021-11-10 18:23 UTC)

<p>I tried to use <code>vtkPoissonDiskSampler</code> to update the script that creates a frame for a model using the principal directions of the surface but I couldn’t find the filter on latest preview release of Slicer.<br>
<code>maskFilter = vtk.vtkPoissonDiskSampler()</code> gives this exception: <code>AttributeError: module 'vtkmodules.all' has no attribute 'vtkPoissonDiskSampler'</code></p>

---

## Post #23 by @lassoan (2021-11-10 18:39 UTC)

<p>The <a href="https://github.com/Kitware/VTK/commits/7a9dfc464d37abf91d96f7ace6d37c665b987abe/Filters/Points/vtkPoissonDiskSampler.h">vtkPoissonDiskSampler class was added earlier this year</a> and is not included in SLicer’s VTK yet. This issue tracks the <a href="https://github.com/Slicer/Slicer/issues/5956">next VTK update</a>.</p>
<p>However, uniform sampling will probably not make much difference, unless your surface has huge variations in surface area of cells and you don’t use many samples.</p>
<p>For significant change you could use volumetric sampling (to get true mechanical moments) or oriented bounding box (so that small indentations or extrusions do not affect the axis directions in objects with flat sides).</p>

---

## Post #25 by @GL1984 (2022-07-20 16:11 UTC)

<p>Hi,<br>
I have been trying to “define a coordinate system using a markups plane node” as suggested by <span class="mention">@Iassoan</span>. I have unfortunately no knowledge in coding and have not used the python interactor before.<br>
I was wondering if there is any way to generate the plane linked to the 3 defining points without using the python interactor?<br>
Is there a module that would do this?<br>
I mainly use 3D Slicer to plan screw positioning in vertebrae and the first step of the workflow is to manually align the bone model to the RAS coordinate system using a transform. It would be much easier to place 3 points defining the sagittal plane assuming I can then define my screw positions in that coordinate system.<br>
Many thanks,<br>
Guillaume</p>

---

## Post #26 by @mau_igna_06 (2022-07-20 18:18 UTC)

<p>Try this:</p>
<pre><code class="lang-auto">PlaneNode = getNode('P')
PlaneNode.SetPlaneType(PlaneNode.PlaneTypePlaneFit)
</code></pre>
<p>And restrict yourself to using 3 points while creating the plane.</p>

---

## Post #27 by @GL1984 (2022-07-21 13:50 UTC)

<p>Thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a><br>
I am afraid I am not sure I know how to.<br>
Is there a basic tutorial on the steps to run a script like this?<br>
I don’t want to waste your time as I have no experience at all in any scripting/coding so maybe I need to start somewhere else?</p>
<p>I tried to copy and paste these 2 lines in the python interactor using an empty Slicer scene, press enter and obtained a few error lines:</p>
<blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>PlaneNode = getNode(‘P’)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 1312, in getNode<br>
raise MRMLNodeNotFoundException(“could not find nodes in the scene by name or id ‘%s’” % (pattern if (isinstance(pattern, str)) else “”))<br>
slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘P’<br>
PlaneNode.SetPlaneType(PlaneNode.PlaneTypePlaneFit)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘PlaneNode’ is not defined</p>
</blockquote>
</blockquote>
</blockquote>
</blockquote>
<p>I suspect I need a plane object in my scene maybe, which should be named P? Or is the P node the Fiducial list which is F by default in my 3D Slicer version? Do I need 3 points in the scene before I run the code or after? Will the plane appear as I place the 3 points? Is there any other prerequisite in the the scene before the script is run? Like a 3D object or a CT study?<br>
Very sorry if these questions are extremely basic. I completely understand if this scripting module is meant for people with basic programming skills and maybe I should stick to the modules already created.<br>
Guillaume</p>

---

## Post #28 by @mau_igna_06 (2022-07-21 17:14 UTC)

<blockquote>
<p>I suspect I need a plane object in my scene maybe, which should be named P?</p>
</blockquote>
<p>You have to do that, yes.</p>
<blockquote>
<p>Do I need 3 points in the scene before I run the code or after?</p>
</blockquote>
<p>You should have drawn a plane before running the code I think</p>
<blockquote>
<p>Is there any other prerequisite in the the scene before the script is run? Like a 3D object or a CT study?</p>
</blockquote>
<p>No</p>

---

## Post #29 by @jegberink (2022-10-14 17:58 UTC)

<pre><code class="lang-python">planeToWorld = vtk.vtkMatrix4x4()
getNode('P').GetObjectToWorldMatrix(planeToWorld)
</code></pre>
<p>This part does not appear to work for me, Plane node is named “P”, however i cant get the matrix.<br>
Has something changed or am i doing something wrong?</p>
<p>thank you</p>

---

## Post #30 by @lassoan (2022-10-14 23:15 UTC)

<p>I’ve just tested this in the current stable release (5.0.3) and it works well. You can print matrix values:</p>
<pre><code class="lang-python">&gt;&gt;&gt; planeToWorld = vtk.vtkMatrix4x4()
&gt;&gt;&gt; getNode('P').GetObjectToWorldMatrix(planeToWorld)
&gt;&gt;&gt; print(planeToWorld)
vtkMatrix4x4 (000001D1F157F7B0)
  Debug: Off
  Modified Time: 4320154
  Reference Count: 1
  Registered Events: (none)
  Elements:
    1 0 0 87.172 
    0 1 0 -74.5663 
    0 0 1 -75.25 
    0 0 0 1 
</code></pre>

---

## Post #31 by @jegberink (2022-10-15 18:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="30" data-topic="19446">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>print(planeToWorld)</code></p>
</blockquote>
</aside>
<p>Thank you so much, i still make a lot of small misstakes so i truly appreciate you helping me. I dont know how i did it but i messed up my print command.</p>
<p>Last question, what would be the best way to measure the model registration from point 1? could i transform the model to the world coordinate system using the inverse of the matrix i now have to allign my model with the world coordinate system?</p>
<p>again, thank you.</p>

---

## Post #32 by @jegberink (2022-10-15 19:21 UTC)

<p>I figured i might aswell try, took the inverse matrix and it worked. no more help needed for now, thank you!</p>

---

## Post #33 by @GL1984 (2022-10-19 21:38 UTC)

<p>Apologies for not following up on this thread after guidance provided. I only have limited opportunities to work on this project and it has been several months since I have tried again.<br>
The recent discussions motivated me to try again and I have made progress. The reason I could not figure out how to use mark-up plane nodes is that I was using an older version of Slicer (4.11) and I believe that function was not fully available then.<br>
I am now able to to generate the plane with 3 points and could obtain the transformation matrix as suggested.<br>
My residual problem is that transformation seem to cause a 90 degree rotation around the A axis when I try to align my model to the world coordinate. I am not sure I understand why? Maybe it has to do with the way the plane coordinates are defined?<br>
I am attaching a screen shot so you can visualise what I am talking about (green model before transformation, red model post transformation).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80c0563f067dc9b06b0a79480a80c503a1ed4ca7.jpeg" data-download-href="/uploads/short-url/imZc9TILOu6saHPxAMbukqO5dEb.jpeg?dl=1" title="Screen Shot 2022-10-19 at 22.36.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80c0563f067dc9b06b0a79480a80c503a1ed4ca7_2_690x388.jpeg" alt="Screen Shot 2022-10-19 at 22.36.06" data-base62-sha1="imZc9TILOu6saHPxAMbukqO5dEb" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80c0563f067dc9b06b0a79480a80c503a1ed4ca7_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80c0563f067dc9b06b0a79480a80c503a1ed4ca7_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80c0563f067dc9b06b0a79480a80c503a1ed4ca7_2_1380x776.jpeg 2x" data-dominant-color="2D2E35"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-10-19 at 22.36.06</span><span class="informations">1920×1080 76.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Anyone knows what I am doing wrong?</p>

---

## Post #34 by @jegberink (2022-10-26 13:40 UTC)

<p>hey!<br>
You can see if this helps:</p><aside class="quote quote-modified" data-post="2" data-topic="19726">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/defining-a-new-coordinate-system-using-markups-plane-node/19726/2">Defining a new coordinate system using markups plane node</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The axes of a MarkupsPlane node are always orthogonal, even if the triangle of points used to define the plane is not a right triangle. If you have a MarkupsFiducial node with your three defining points, this function will produce a MarkupsPlane node 
def makePlaneMarkupFromFiducial(self, FNode, planeName):
    """Create MarkupsPlane using first three control points of the input fiducial node.
    """
    if FNode.GetNumberOfControlPoints()&lt;3:
      logging.warning('Not enough control points to…
  </blockquote>
</aside>

<p>Your point 1 to point 2 is your positive X-axis, which should correspond to the LR axis in Slicer.</p>

---

## Post #35 by @GL1984 (2022-10-26 15:23 UTC)

<p>Thanks <a class="mention" href="/u/jegberink">@jegberink</a><br>
This explains well my problem. I am not sure how to resolve it though.<br>
The way I want to use this coordinate system is by defining 3 points in the Sagittal plane so unfortunately I don’t have the option to use point 1 and 2 in the left to right direction. I want to use this to plan dog’s neurosurgeries so in the spine the easiest plane to define is sagittal (plane of symmetry). I could however use point 1 and 2 in either the inferior to superior or posterior to anterior direction.<br>
Would there be a way to modify the code so I get a transform matrix in the proper orientation?<br>
Otherwise I guess I would have to add a 90 degree rotation manually so I get the proper anatomical alignment.</p>

---

## Post #36 by @jegberink (2022-10-26 16:23 UTC)

<p>I had the same problem, a 90 degree transform is the easiest solution. Create a linear transform and rotate it 90 degrees towards the the axis you prefer.<br>
Do keep in mind that point 1 will remain in 0.</p>
<p>Good luck!</p>

---

## Post #37 by @GL1984 (2022-11-01 11:33 UTC)

<p>Thanks,<br>
The method is working now.<br>
I would like to find a way to simplify it in the future but need to explore other steps in my workflow to decide the best way forward. I suspect setting up a module will be the end goal.</p>

---

## Post #38 by @lili-yu22 (2022-11-10 09:30 UTC)

<p>I have  doubts. I registered two objects in the world coordinate system and got a matrix 1. Then I can know how an object moves and rotates in the world coordinate system to register with another object. If I create a local coordinate system using the makeupplane node and want to know the movement in the local coordinate system, How do I deal with these two matrices next, as shown in the figure, is it right?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba3c35972d32f83f2a2b116c9c2223721e437ea1.png" alt="mmexport1668071826179" data-base62-sha1="qzvO3HFNvZxaEk4oOqgSoCKJAul" width="495" height="201"></p>

---

## Post #40 by @lili-yu22 (2024-10-25 07:52 UTC)

<p>can you tell me how  to make  the plane parallel to the world’s x or y or z axis using the script</p>

---

## Post #41 by @lassoan (2024-10-25 11:27 UTC)

<p>You can create a plane with patient RAS axes if you set plane to world to identity matrix. Change order of columns to change what plane axis is aligned with which patient axis.</p>

---

## Post #42 by @lili-yu22 (2024-10-25 23:30 UTC)

<aside class="quote no-group" data-username="jegberink" data-post="29" data-topic="19446">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jegberink/48/16031_2.png" class="avatar"> jegberink:</div>
<blockquote>
<pre><code class="lang-auto">planeToWorld = vtk.vtkMatrix4x4()
getNode('P').GetObjectToWorldMatrix(planeToWorld)
</code></pre>
</blockquote>
</aside>
<p>first,thanks for your reply.<br>
according to the above script:<br>
planeToWorld = vtk.vtkMatrix4x4()<br>
getNode(‘P’).GetObjectToWorldMatrix(planeToWorld)<br>
I can get the matix，then I use the matrix on the plane.Do I understand correctly that ？</p>

---

## Post #43 by @lili-yu22 (2024-10-26 00:53 UTC)

<p>if I want use the above matrix to the plane，how to describe in the python ，thank you</p>

---

## Post #44 by @lassoan (2024-10-26 03:22 UTC)

<p>Probably the easiest is to use <a href="https://apidocs.slicer.org/main/classvtkMRMLMarkupsPlaneNode.html#a586879796afd9f81187c3c8333370f51">SetAxesWorld() method</a>.</p>

---

## Post #45 by @lili-yu22 (2024-10-26 03:46 UTC)

<p>when I paste the script.error happen<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17e9948d9d2bb747bce1fb7531849b3cf1f13d29.jpeg" data-download-href="/uploads/short-url/3pxqmKSHFFGSKlc3amCCvD1q4oF.jpeg?dl=1" title="IMG_20241026_114328" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17e9948d9d2bb747bce1fb7531849b3cf1f13d29_2_375x500.jpeg" alt="IMG_20241026_114328" data-base62-sha1="3pxqmKSHFFGSKlc3amCCvD1q4oF" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17e9948d9d2bb747bce1fb7531849b3cf1f13d29_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17e9948d9d2bb747bce1fb7531849b3cf1f13d29_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17e9948d9d2bb747bce1fb7531849b3cf1f13d29_2_750x1000.jpeg 2x" data-dominant-color="3E383C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20241026_114328</span><span class="informations">1920×2560 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #46 by @lassoan (2024-10-26 14:07 UTC)

<p>To get answer for questions on basic Python syntax, I would recommend to ask an AI chatbot, such as Microsoft Copilor or ChatGPT. For example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f941f69e1f79bb573164377f9b51134e8facea24.png" data-download-href="/uploads/short-url/zz2dobdgMkfGRgul3W6c6B8q0LO.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f941f69e1f79bb573164377f9b51134e8facea24_2_656x499.png" alt="image" data-base62-sha1="zz2dobdgMkfGRgul3W6c6B8q0LO" width="656" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f941f69e1f79bb573164377f9b51134e8facea24_2_656x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f941f69e1f79bb573164377f9b51134e8facea24_2_984x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f941f69e1f79bb573164377f9b51134e8facea24_2_1312x998.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1767×1345 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #47 by @lili-yu22 (2024-10-26 14:56 UTC)

<p>thank you very much​:+1:<img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=12" title=":rose:" class="emoji" alt=":rose:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=12" title=":rose:" class="emoji" alt=":rose:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=12" title=":rose:" class="emoji" alt=":rose:" loading="lazy" width="20" height="20"></p>

---
