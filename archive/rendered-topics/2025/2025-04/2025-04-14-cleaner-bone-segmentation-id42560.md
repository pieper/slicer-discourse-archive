---
topic_id: 42560
title: "Cleaner Bone Segmentation"
date: 2025-04-14
url: https://discourse.slicer.org/t/42560
---

# Cleaner bone segmentation

**Topic ID**: 42560
**Date**: 2025-04-14
**URL**: https://discourse.slicer.org/t/cleaner-bone-segmentation/42560

---

## Post #1 by @JT_GAUD (2025-04-14 15:10 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab363f13d5ccf84e684e50252a3a1af409fd55b9.jpeg" data-download-href="/uploads/short-url/oqBRVzhXOhPv2eT59uxhhQjx1lT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab363f13d5ccf84e684e50252a3a1af409fd55b9_2_690x473.jpeg" alt="image" data-base62-sha1="oqBRVzhXOhPv2eT59uxhhQjx1lT" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab363f13d5ccf84e684e50252a3a1af409fd55b9_2_690x473.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab363f13d5ccf84e684e50252a3a1af409fd55b9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab363f13d5ccf84e684e50252a3a1af409fd55b9.jpeg 2x" data-dominant-color="9A95B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">938×644 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b62e8d8425395396addef9dc0665462d573b222a.png" data-download-href="/uploads/short-url/pZEDAvJwJ3kwF1xxacuBGumVZ5E.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b62e8d8425395396addef9dc0665462d573b222a.png" alt="image" data-base62-sha1="pZEDAvJwJ3kwF1xxacuBGumVZ5E" width="669" height="439"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">669×439 67.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello !<br>
I’m currently trying to have some cleans bones and i would like to know how to have a cleaner version of my hand (without holes, noises, sponge spongy bones),  like the second photo (from what i’ve searched i think everything will be in the segment editor but i don’t understand everything and i’ve didn’t found how to use the segment editor perfectly in the tutorials</p>
<p>Do you have ideas and things about it to help me improve my models ?</p>

---

## Post #2 by @coco (2025-04-14 15:30 UTC)

<p>Hi gaud,<br>
I am not an expert but you should first check if you have some kind of smoothing on, uncheck smoothing in 3D.<br>
Use island tool: you could keep largest island to remove small ones<br>
use the tool close holes: Smoothing effect - “Closing (fill holes)” method</p>

---

## Post #3 by @JT_GAUD (2025-04-15 07:00 UTC)

<p>Hi coco<br>
thx for the respond !<br>
Do you know where i could find an explanations of all the tools of the segments Editor ?</p>

---

## Post #4 by @coco (2025-04-15 07:10 UTC)

<p>Dear Gaud,<br>
If, like me, you are completely new to imaging, it is a steep learning curve, especially for 3D and when no one is arround to show you. I’ve send you a message if you want to spend 30 mins or so online and I can give you a few tips.</p>

---

## Post #5 by @eNable_Polska (2025-04-18 18:42 UTC)

<p>Try this <a href="https://www.youtube.com/watch?v=z22Pa9PNk1E" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=z22Pa9PNk1E</a></p>

---

## Post #6 by @muratmaga (2025-04-18 19:56 UTC)

<aside class="quote no-group" data-username="JT_GAUD" data-post="3" data-topic="42560">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jt_gaud/48/78976_2.png" class="avatar"> JT_GAUD:</div>
<blockquote>
<p>Do you know where i could find an explanations of all the tools of the segments Editor ?</p>
</blockquote>
</aside>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation" target="_blank" rel="noopener nofollow ugc">Tutorials/Segmentation at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" target="_blank" rel="noopener nofollow ugc">Segment editor — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
