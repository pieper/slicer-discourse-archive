---
topic_id: 33932
title: "New Interpolation Tool"
date: 2024-01-23
url: https://discourse.slicer.org/t/33932
---

# New interpolation tool

**Topic ID**: 33932
**Date**: 2024-01-23
**URL**: https://discourse.slicer.org/t/new-interpolation-tool/33932

---

## Post #1 by @Mehran (2024-01-23 16:56 UTC)

<p>Hi All,<br>
I am thrilled to share our recent tool for filling between slices in segmentation module. We would love to hear your thoughts and feedback! <img src="https://emoji.discourse-cdn.com/twitter/nerd_face.png?v=12" title=":nerd_face:" class="emoji" alt=":nerd_face:" loading="lazy" width="20" height="20"><br>
we designed it for muscle segmentation though it can be used for tumor, bone and smooth structures. here are two examples for tumor and muscle segmentation.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fa6078798df0c089a4f25043c3657de7e488e7d.mp4">
  </div><br>
<div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/049bd349687c3ff14f8ae673f50217bc1f64559b.mp4">
  </div><br>
link to read the method:<br>
<a href="https://doi.org/10.1080/21681163.2023.2301403" class="onebox" target="_blank" rel="noopener nofollow ugc">https://doi.org/10.1080/21681163.2023.2301403</a><br>
link to download the tool:<br>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/latimagine/SlicerSpline">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/latimagine/SlicerSpline" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/e6955e767b813ac7ba5b9272c3171327ab78060889aca7c5b7bc7e729c036d78/latimagine/SlicerSpline" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/latimagine/SlicerSpline" target="_blank" rel="noopener nofollow ugc">GitHub - latimagine/SlicerSpline: A Slicer module for intepolation between...</a></h3>

  <p>A Slicer module for intepolation between manual labels - GitHub - latimagine/SlicerSpline: A Slicer module for intepolation between manual labels</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p></p>

---

## Post #2 by @lassoan (2024-01-23 21:26 UTC)

<p>Thank you, it looks nice! To make it conveniently available for users, you could add a new Segment Editor effect for it.</p>
<p>How does it compare to “Fill between slices” effect?<br>
What worries me a bit is the 12-minute computation time for 14 segments. Morphological contour interpolation in “Fill between slices” effect typically completes computation within a few seconds.</p>

---

## Post #3 by @Mehran (2024-01-24 08:02 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> , I will do it as soon as possible. In the paper, we mentioned the difference between morphological ones and ours, I would say 5-10% better on muscles. I did not try on other dataset what i asked slicer users to let us know. About time, you are right, ours is slower, though in terms of accuracy, that mostly worth it, specifically when we are trying to create ground truth. The time was calculated on a laptop i7 no GPU. it will be much less using a good ones.<br>
Best</p>

---
