---
topic_id: 26190
title: "Registration Request For 3D Objects"
date: 2022-11-11
url: https://discourse.slicer.org/t/26190
---

# Registration request for 3D objects

**Topic ID**: 26190
**Date**: 2022-11-11
**URL**: https://discourse.slicer.org/t/registration-request-for-3d-objects/26190

---

## Post #1 by @Chm (2022-11-11 06:56 UTC)

<p>Dear all,</p>
<p>I would like to ask if there is any fully automatic registration tool for 3D objects registration.</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2022-11-11 19:59 UTC)

<p>There are several fully automatic registration methods - see a brief overview <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">here</a>. We can give you more specific help if you tell us more about what you want to do - what objects you need to register, how they are represented (images, surface meshes, …), how similar they are, if you already have some initial guess for the alignment, etc.</p>

---

## Post #3 by @Chm (2022-11-11 22:14 UTC)

<p>First of all, thanks for your prompt reply</p>
<p>I load (Data=obj file)  the 3D Objects (description=Model)  as showing in the screenshot. I need to proceed with auto (only) registration and save this registration model as obj file.</p>
<p>So what are the next steps ? Please be detailed because im new with this toll.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/706218b4943f308e743654cab1b471ccb0d13dba.jpeg" data-download-href="/uploads/short-url/g2bE8VwZVeg9REoL5o0sAKoR8TM.jpeg?dl=1" title="3D Spine Objects" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706218b4943f308e743654cab1b471ccb0d13dba_2_690x439.jpeg" alt="3D Spine Objects" data-base62-sha1="g2bE8VwZVeg9REoL5o0sAKoR8TM" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706218b4943f308e743654cab1b471ccb0d13dba_2_690x439.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706218b4943f308e743654cab1b471ccb0d13dba_2_1035x658.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/706218b4943f308e743654cab1b471ccb0d13dba_2_1380x878.jpeg 2x" data-dominant-color="C3C6DE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D Spine Objects</span><span class="informations">1480×943 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks in advance</p>

---

## Post #4 by @sandress (2022-11-12 17:40 UTC)

<p>Hi, if the two meshes possibly deviate maybe this extension might be helpful:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/sebastianandress/Slicer-SurfaceFragmentsRegistration">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/sebastianandress/Slicer-SurfaceFragmentsRegistration" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/d78e970d5572bbe1ced7855554c7435e59a36208874f6866dd357d552d5bc9bd/sebastianandress/Slicer-SurfaceFragmentsRegistration" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/sebastianandress/Slicer-SurfaceFragmentsRegistration" target="_blank" rel="noopener nofollow ugc">GitHub - sebastianandress/Slicer-SurfaceFragmentsRegistration: This 3D Slicer...</a></h3>

  <p>This 3D Slicer extension is intended to find different surface error types. Unless traditional methods, it tries to find correlating subgroups of vertices, that show high accuracy (within this subg...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Nevertheless it contains code for icp and landmark registration.</p>

---

## Post #5 by @lassoan (2022-11-13 02:32 UTC)

<p>The models look very intricate with lots of details, so you can expect to get very accurate registration. However, you need to start the optimization from a good initial alignment (not more than a couple of millimeters off). You can try landmark registration followed by ICP. It seems that the extension <a class="mention" href="/u/sandress">@sandress</a> recommended could do the job. If not, you can use SlicerIGT extension’s Fiducial Registration Wizard module for initial alignment and then the Model Registration module for automatic accurate alignment.</p>

---

## Post #6 by @Chm (2022-11-13 15:06 UTC)

<p>Dear Team,</p>
<p>I used the General Registration (ANTs) module because unfortunately all the others registration modules crush till now.</p>
<p>I loaded my new 3D objects as segmentation(descriptions) and then transformed them to volumes through the Segmentation module. Then I used General Registration (ANTs) module as showing in the first picture and after the segmentation i got the result showing in the last picture.</p>
<p>I need a final step to complete the automatic registration, and this this the rotation of Obj1. Can I achieve that through the General Registration (ANTs) module settings? and which setting is that ?</p>
<p>Thanks again for you valuable guidance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3a0658bdbeddb6a1058a6fc16b76776d5bcec6.png" data-download-href="/uploads/short-url/vQKNc20ztu2NsnISd1srDFEfI7Y.png?dl=1" title="General Registration(ANTs)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df3a0658bdbeddb6a1058a6fc16b76776d5bcec6_2_690x294.png" alt="General Registration(ANTs)" data-base62-sha1="vQKNc20ztu2NsnISd1srDFEfI7Y" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df3a0658bdbeddb6a1058a6fc16b76776d5bcec6_2_690x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df3a0658bdbeddb6a1058a6fc16b76776d5bcec6_2_1035x441.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df3a0658bdbeddb6a1058a6fc16b76776d5bcec6_2_1380x588.png 2x" data-dominant-color="B8B8D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">General Registration(ANTs)</span><span class="informations">1627×694 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5abf7c782065f67ecde594d90bbd1a8b1ded7faa.png" data-download-href="/uploads/short-url/cWNeeLLRPhzSCpJ1BfvmkGlvDsK.png?dl=1" title="after registration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5abf7c782065f67ecde594d90bbd1a8b1ded7faa_2_690x242.png" alt="after registration" data-base62-sha1="cWNeeLLRPhzSCpJ1BfvmkGlvDsK" width="690" height="242" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5abf7c782065f67ecde594d90bbd1a8b1ded7faa_2_690x242.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5abf7c782065f67ecde594d90bbd1a8b1ded7faa_2_1035x363.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5abf7c782065f67ecde594d90bbd1a8b1ded7faa_2_1380x484.png 2x" data-dominant-color="B9B9D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">after registration</span><span class="informations">1639×577 76.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2022-11-13 15:17 UTC)

<p>Initial error for intensity based automatic registration must be typically within 5-10mm translation and 5 degrees rotation.</p>
<p>If the objects have approximately the same physical extents and initial rotation error is small then then translation can be easily initialized automatically (e.g., by aligning center of gravity). So, having good initial orientation alignment is the most important. In your case it seems that it is grossly misaligned (looks like a 180deg error), so it is expected that the registration fails. You may try if ANTs has some built-in methods for aligning orientation (e.g., based on principal axis directions), but the easiest is to initialize using landmark registration as described above.</p>
<p>Note that binary images usually cannot be aligned using intensity-based image registration. Instead, you need to compute a distance map from the image (e.g., using and of the DistanceMap filters in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/simplefilters.html">Simple Filters module</a>) and register those.</p>
<aside class="quote no-group" data-username="Chm" data-post="6" data-topic="26190">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chm/48/16855_2.png" class="avatar"> Chm:</div>
<blockquote>
<p>I used the General Registration (ANTs) module because unfortunately all the others registration modules crush till now.</p>
</blockquote>
</aside>
<p>Are you sure it was a crash and not just hang (computation took long time)? We take application crashes very seriously and investigate every occurrence. Please provide step-by-step instruction and data sets that we can use to reproduce the problem.</p>

---

## Post #8 by @Chm (2022-11-14 10:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="26190">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are you sure it was a crash and not just hang (computation took long time)? We take application crashes very seriously and investigate every occurrence. Please provide step-by-step instruction and data sets that we can use to reproduce the problem.</p>
</blockquote>
</aside>
<p>to be honest i am not sure but more likely is hanging due to long time computation. I will try it with more sets and let you know.</p>
<p>Thanks a lot</p>

---

## Post #9 by @Raha_Sep (2022-11-17 19:59 UTC)

<p>Hello,<br>
I am interested in using the Elastix or  landmark registration and was wondering if there is a file or link that explains how to work with them? I uploaded two objects separately but they are stuck together and I can’t assign them to the moving and fix volume to proceed further.<br>
Thanks you for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcc641460df18e2e94baab0567695497315fb7b6.png" data-download-href="/uploads/short-url/A4954JWYkRwNdeeXDzxH6kTBOtw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcc641460df18e2e94baab0567695497315fb7b6_2_690x463.png" alt="image" data-base62-sha1="A4954JWYkRwNdeeXDzxH6kTBOtw" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcc641460df18e2e94baab0567695497315fb7b6_2_690x463.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcc641460df18e2e94baab0567695497315fb7b6_2_1035x694.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcc641460df18e2e94baab0567695497315fb7b6_2_1380x926.png 2x" data-dominant-color="D4D4D1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1788×1200 361 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @Chiararp (2023-07-05 16:00 UTC)

<p>Hi,<br>
Can you show me your data in the “data” module?<br>
Maybe there’s an errore with the download of your segmentations.<br>
Anyway, if you want to perform registration with elastix, you need volumes( for example ct scans), not segmentations</p>

---

## Post #11 by @Raha_Sep (2023-08-04 08:56 UTC)

<p>Hi Chiara,<br>
Thank you for your answer. I am currently using other tools to register as I have not found a solution since some time ago. However, I am interested in trying it again and will keep you updated.<br>
the best,<br>
Raha</p>

---
