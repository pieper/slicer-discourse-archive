---
topic_id: 39518
title: "Plane Fitting And Local To Global Transform Calculation"
date: 2024-10-03
url: https://discourse.slicer.org/t/39518
---

# Plane Fitting and Local to Global Transform Calculation

**Topic ID**: 39518
**Date**: 2024-10-03
**URL**: https://discourse.slicer.org/t/plane-fitting-and-local-to-global-transform-calculation/39518

---

## Post #1 by @evaherbst (2024-10-03 13:00 UTC)

<p>Hello,</p>
<p>I am trying to fit a plane to the glenoid to define a new local coordinate system, to calculate the transform between that coordinate system and a previous one.</p>
<p>The glenoid’s previous coordinate system is currently aligned with the global coordinate system, so as far as I understand I can use <a href="https://discourse.slicer.org/t/creating-a-new-coordinate-system/19446/16">this code from</a> <a class="mention" href="/u/lassoan">@lassoan</a> for the transform calculation.</p>
<p>However, I am running into issues defining my new coordinate system.<br>
My goal is to create a plane fit to the eigenvectors of the glenoid surface mesh, and then simply translate the origin of the coordinate system to 0,0,0 (so that I am only checking rotation differences from the original coordinate system).</p>
<p>I found <a href="https://gist.github.com/mauigna06/434784dac9e5704198b80b179e037d0e" rel="noopener nofollow ugc">this very useful code</a> by <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> from <a href="https://discourse.slicer.org/t/creating-a-new-coordinate-system/19446/19">this related topic</a>.<br>
It is exactly what I am looking for.</p>
<p>However, when I test it, the plane x and y are not aligned with the surface object y and y:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49b93b16ee9b9e2e785bbd42be2d826884699fa8.png" data-download-href="/uploads/short-url/awbI3jVScSEvD5N7bLhog78NYYo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49b93b16ee9b9e2e785bbd42be2d826884699fa8_2_479x499.png" alt="image" data-base62-sha1="awbI3jVScSEvD5N7bLhog78NYYo" width="479" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49b93b16ee9b9e2e785bbd42be2d826884699fa8_2_479x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49b93b16ee9b9e2e785bbd42be2d826884699fa8_2_718x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49b93b16ee9b9e2e785bbd42be2d826884699fa8.png 2x" data-dominant-color="9C9ACA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">903×941 25.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Looking at this section of the code</p>
<blockquote>
<p>modelZ = np.zeros(3)<br>
modelX = eigenvectors0[0]<br>
modelY = eigenvectors0[1]<br>
vtk.vtkMath.Cross(modelX, modelY, modelZ)<br>
modelZ = modelZ/np.linalg.norm(modelZ)<br>
modelOrigin = modelPointsMean</p>
</blockquote>
<p>I would expect the X and Y axes to be like this (my end goal):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25d19aec5200902d77e5dade0baa0808d1e04028.png" alt="image" data-base62-sha1="5oyK5Fa2DnaICHZ90G9bWBKGC2A" width="443" height="463"></p>
<p>In fact, it seems like the code is somehow fitting to the orginal scapula model - I made the glenoid with the curve cut tool. Could the vertices of the rest of the scapula somehow still be references by the plane fitting code?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/303b1e1d44f07d8a6e08df3ba2a995be90e9dc64.png" data-download-href="/uploads/short-url/6SFzO1d9k2ceMcVu3r4RC0foMa8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303b1e1d44f07d8a6e08df3ba2a995be90e9dc64_2_561x500.png" alt="image" data-base62-sha1="6SFzO1d9k2ceMcVu3r4RC0foMa8" width="561" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303b1e1d44f07d8a6e08df3ba2a995be90e9dc64_2_561x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303b1e1d44f07d8a6e08df3ba2a995be90e9dc64_2_841x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/303b1e1d44f07d8a6e08df3ba2a995be90e9dc64.png 2x" data-dominant-color="ADA6A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×881 85.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I also tested the script <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#fit-markups-plane-to-model" rel="noopener nofollow ugc">Fit Markups Plane to Model</a> and the plane is similarly misaligned (this code explicitly defines center and normal direction, so I wanted to use it as a test - and do not understand why the normal is not aligned to the global Z axis):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/319c34c2ca7a4094df7a51ed46eed5ae0b04b5dd.png" data-download-href="/uploads/short-url/74S45YN39DxLfrPZxZ3y24usarH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/319c34c2ca7a4094df7a51ed46eed5ae0b04b5dd.png" alt="image" data-base62-sha1="74S45YN39DxLfrPZxZ3y24usarH" width="528" height="500" data-dominant-color="9A95C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">533×504 14.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Additional question:</strong><br>
Is there a way to visualize the global CS as axes centered at 0,0,0 instead of in the bottom right of the screen?</p>
<p>Thank you!<br>
Eva</p>

---

## Post #2 by @mau_igna_06 (2024-10-03 17:21 UTC)

<p>I would expect the script to work for the purpose you intend. Could you public the exact code you are running and the model node of the glenoid (ie .vtk file) you are using?</p>

---

## Post #3 by @evaherbst (2024-10-04 10:41 UTC)

<p>Thanks Mauro for the quick reply!</p>
<p>Very strangely, when I tried to replicate the problem, I now get a correct result.<br>
I re-did the surface cut - I will see if it comes up again in future tests.</p>
<p>I do have a question about your code.</p>
<p>At the end of the code, why do you define and calculate initialModeltoWorldMatrix? Should this not be the same as planeToWorldMatrix?<br>
Since you define worldToInitialModel as the inverse of planeToWorldMatrix, and initialModeltoWorldMatrix as the inverse of worldToInitialModel?</p>
<p>Also, why is the worldToInitialModel applied as a transform to the model?<br>
Isn’t the initial model’s “frame” just whatever the global coordinates are?<br>
Indeed, when I take away the transform, the model is in the same spot.<br>
Is this just a check?</p>
<p>I would also like to propose an adjustment to your script, which is flipping the Z axis to be aligned with the normals of the surface we are fitting the plane to.</p>
<p>So for example here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/611552792ed87955ca723d88ee6504fa75cbd208.png" data-download-href="/uploads/short-url/dQPZP3KdiwtXUkWBV8NZmDJVFKo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/611552792ed87955ca723d88ee6504fa75cbd208.png" alt="image" data-base62-sha1="dQPZP3KdiwtXUkWBV8NZmDJVFKo" width="447" height="499" data-dominant-color="9B9B88"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">722×807 64.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I did this and tested it, let me know if I should make a pull request to your script?</p>
<p>E.g. by calculating average normal of the surface and if the difference between that and the normal of the plane is greater than 90 degrees, flip the plane normal (rotate by 180 degrees) about X.<br>
Of course this also reorients the Y axis.</p>
<p>I did this and tested it, let me know what you think and if I should make a pull request to your script?</p>
<p>Also, for anyone else reading this post, I figured out how to visualize the global axes.<br>
This can just be done making a new plane and setting the axes and origin to global XYZ and 0,0,0 - just didn’t think of this before.</p>
<p>Thanks again!<br>
Eva</p>

---

## Post #4 by @mau_igna_06 (2024-10-04 12:06 UTC)

<p>Hi Eva,</p>
<p>That code may not be the final version of the script, I think there maybe a newer gist on my library, please check.</p>
<p>But the description says: “Create a frame for the model in the principal components directions, set up a plane with interaction handles <em>to move it.</em>” I think that’s related to the matrix definition you asked about</p>
<p>HiH<br>
Mauro</p>

---

## Post #5 by @evaherbst (2024-10-04 15:17 UTC)

<p>Thanks Mauro.</p>
<p>Ah I see, that explains why there are the duplicate matrices, since one is before and one after manual manipulation,</p>
<p>I did not find another script in the repository. Let me know if you want to add my Z axis adjustment.</p>
<p>Thank you,<br>
Eva</p>

---

## Post #6 by @mau_igna_06 (2024-10-04 17:26 UTC)

<p>I meant this one:</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mauigna06/4345e60f04c74916f159474fb26086fa">
  <header class="source">

      <a href="https://gist.github.com/mauigna06/4345e60f04c74916f159474fb26086fa" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mauigna06/4345e60f04c74916f159474fb26086fa" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/mauigna06/4345e60f04c74916f159474fb26086fa</a></h4>

  <h5>transformModel.py</h5>
  <pre><code class="Python">
# This scripts allows you to have a widget placed initially in the model centroid and the 
# direction matching its principal components. Then two modes are possible "Transform mode" 
# and "Local mode" by pressing g key and h key correspondingly.
# You can change the center of rotation by going to Local mode, moving the widget and then 
# returning to Transform mode. This feature that let's move the plane indenpendently of the 
# model on Local mode and then lets you transform it in Transform mode is what makes this 
# feature useful for manual registration.

# Code Starts here</code></pre>
   This file has been truncated. <a href="https://gist.github.com/mauigna06/4345e60f04c74916f159474fb26086fa" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>HIH</p>

---

## Post #7 by @evaherbst (2024-10-07 13:19 UTC)

<p>Thank you!<br>
For now I was just using the code to assign new frames, get the transform between them, and use those in a different program, but I will also test your Slicer model transform tool in the future.</p>
<p>Best,<br>
Eva</p>

---
