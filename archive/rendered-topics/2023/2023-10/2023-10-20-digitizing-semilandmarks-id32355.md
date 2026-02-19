---
topic_id: 32355
title: "Digitizing Semilandmarks"
date: 2023-10-20
url: https://discourse.slicer.org/t/32355
---

# Digitizing semilandmarks 

**Topic ID**: 32355
**Date**: 2023-10-20
**URL**: https://discourse.slicer.org/t/digitizing-semilandmarks/32355

---

## Post #1 by @codyprang (2023-10-20 19:15 UTC)

<p>Hello,</p>
<p>Does anyone know if there is a way to digitize equally spaced semilandmarks over (and constrained by) a selected area of a surface mesh? In other words, can I ‘paint’ or ‘highlight’ the faces of a surface mesh over which SlicerMorph could place equally spaced (surface) semilandmarks? Currently, I use Viewbox software to do this and, I must admit, this is the one feature that makes it difficult for me to abandon. It makes the generation of a template fast and easy, and it provides a lot of flexibility in the placement of surface semilandmarks.</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2023-10-20 19:21 UTC)

<p>Yes, you first manually draw a curve, and then use the resampling function of the curveMarkup to specify the number of equidistant point (with or without constraining to the surface).</p>
<p>For more details see the tutorial:</p>
<p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/Markups_2#resampling-curves" rel="noopener nofollow ugc">Tutorials/Markups_2 at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #3 by @codyprang (2023-10-20 19:44 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Thanks for this. I was wondering about digitizing surface semilandmarks. For example, can you specify an area, rather than a curve, over which to generate semilandmarks? I know that PseudoLMGenerator can be used to digitize a large number of landmarks that can then be removed. But is it possible to constrain the generation of pseudo-landmarks over a number of painted or highlighted faces of a mesh rather than using the entire mesh? That would really speed up the process of digitizing surface semilandmarks. If that was possible, then I could quickly add a specified number of equally spaced landmarks over a surface of my choosing, or multiple surfaces (such as the different articular surfaces of a tarsal or a carpal). Thank you!</p>

---

## Post #4 by @muratmaga (2023-10-20 21:06 UTC)

<aside class="quote no-group" data-username="codyprang" data-post="3" data-topic="32355">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/dc4da7/48.png" class="avatar"> codyprang:</div>
<blockquote>
<p>number of painted or highlighted faces of a mesh rather than using the entire mesh?</p>
</blockquote>
</aside>
<p>But then how do you know what’s the corresponding vertex in the next mesh? What if the mesh densities are different?<br>
To my knowledge, this usually done by drawing a polygon shape on the mesh manually and subdividing through some sort of a grid, so that when you are sampling on a new mesh, the grid structure allows for correct correspondence.<br>
All the necessary pieces are available in slicer (see surface markups extension), but it needs to be optimized by someone who are familiar with this workflow more carefully. <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup">GitHub - SlicerHeart/SlicerSurfaceMarkup: Extension to test the new grid surface markup with</a></p>

---

## Post #5 by @codyprang (2023-10-20 21:12 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a>! The function I’m describing is implemented in dhal Viewbox software. I just wanted to confirm that it was not possible in SlicerMorph before giving up!</p>

---

## Post #6 by @muratmaga (2023-10-20 21:47 UTC)

<aside class="quote no-group" data-username="codyprang" data-post="5" data-topic="32355">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/dc4da7/48.png" class="avatar"> codyprang:</div>
<blockquote>
<p>it was not possible in SlicerMorph</p>
</blockquote>
</aside>
<p>There is no such thing as not possible in 3D Slicer. It is a matter of someone putting the time and resources in the making it happen. We find the tools within 3D Slicer and SlicerMorph to be sufficient for the types of analysis we do.</p>
<p>If you are missing a specific function, instead of opting for commercial software for it, you can consider hiring the people (e.g., on this forum, or locally) to develop the tool you are missing, and contribute back to the community. It might be cheaper than buying licenses of viewbox. Just a thought.</p>

---

## Post #7 by @jamalgiri (2024-01-07 11:59 UTC)

<p>Hi, I came across this thread while i was looking for ways to place semi landmarks uniformly on dental casts to evaluate the shape of human palate. I have 19 landmarks and I would like to add some semi landmarks uniformly across the palate within the anterior, posterior and lateral confines of the landmarks. Any leads?</p>
<p>Thank you.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a231061f926cc13e9fed7438639ce00db5f5fdc.png" alt="semilandmarks" data-base62-sha1="azQskZZMjWXdEq4XlWfufxip1EM" width="602" height="461"></p>

---

## Post #8 by @muratmaga (2024-01-07 23:54 UTC)

<p>Did you give the CreateSemiLMPatches module a try?</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/CreateSemiLMPatches">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/CreateSemiLMPatches" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/CreateSemiLMPatches" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/CreateSemiLMPatches" target="_blank" rel="noopener">//github.com/SlicerMorph/Tutorials/tree/main/CreateSemiLMPatches</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @jamalgiri (2024-01-08 01:05 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a>, I am trying to fit triangles on the palate to record its shape. However, there is some overlap in the middle, do you think it is a problem?<br>
I am working on different triangular configurations to best record the palate; I will let you know the final outcome.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55df5029556f88958a05f0a5bd5e274e66cfa033.jpeg" data-download-href="/uploads/short-url/cfF1VNhEEqLDm5tkaNHO7thACv9.jpeg?dl=1" title="semi-landmarks" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55df5029556f88958a05f0a5bd5e274e66cfa033.jpeg" alt="semi-landmarks" data-base62-sha1="cfF1VNhEEqLDm5tkaNHO7thACv9" width="690" height="497" data-dominant-color="9B9959"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">semi-landmarks</span><span class="informations">982×708 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @muratmaga (2024-01-08 01:11 UTC)

<p>Yes, that would be concerning. You should use smaller and non-overlapping triangulations.</p>

---

## Post #11 by @jamalgiri (2024-01-08 01:34 UTC)

<p>Thanks for your feedback. Here is a new configuration to minimize overlap. There is no overlap, but some parts of the palate could not be recorded.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/043753b2bd6c12f212cd7beaa9649763b6c86d38.jpeg" data-download-href="/uploads/short-url/BirJucjFyffs0J9lw3tM1bPwOA.jpeg?dl=1" title="semi-landmarks modified" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/043753b2bd6c12f212cd7beaa9649763b6c86d38.jpeg" alt="semi-landmarks modified" data-base62-sha1="BirJucjFyffs0J9lw3tM1bPwOA" width="690" height="497" data-dominant-color="9E9F50"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">semi-landmarks modified</span><span class="informations">982×708 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @muratmaga (2024-01-08 02:07 UTC)

<p>During the merging of semi-landmarks you can optionally create a set of average positions between the boundaries of patches. That will fill the gap some.</p>

---

## Post #13 by @jamalgiri (2024-01-09 07:06 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a>, I have created a landmarks-merged node. Next step is to place the semilandmark patches on other models. Will let you know, how it goes.</p>

---

## Post #14 by @jamalgiri (2024-01-10 03:49 UTC)

<p>This is the final outcome (palatal morphology) using the fixed and semilandmarks. While this may not be directly related to this thread, I am wondering how I can measure the volume and area of the palate. Is there a specific module in Slicer for this?<br>
Thank you in advance.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac0767a67bac6611280f29b0647cdee31ea34b29.png" data-download-href="/uploads/short-url/oxPZmP0HTYRO0gYwqRvmKDQ4BMR.png?dl=1" title="palate morphology" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac0767a67bac6611280f29b0647cdee31ea34b29_2_690x462.png" alt="palate morphology" data-base62-sha1="oxPZmP0HTYRO0gYwqRvmKDQ4BMR" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac0767a67bac6611280f29b0647cdee31ea34b29_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac0767a67bac6611280f29b0647cdee31ea34b29_2_1035x693.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac0767a67bac6611280f29b0647cdee31ea34b29.png 2x" data-dominant-color="9794C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">palate morphology</span><span class="informations">1056×708 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @muratmaga (2024-01-10 16:52 UTC)

<p>This looks a like a sufficiently good template to me. Good luck.</p>
<p>For measuring volumes you will need to do segmentation. You can possibly get by measuring the area via drawing the closed curves. However, thats the area of the closed curve and if that plane doesn’t closely follow the surface of the model, there will be some difference. Otherwise, you will need to segment the surface.</p>

---
