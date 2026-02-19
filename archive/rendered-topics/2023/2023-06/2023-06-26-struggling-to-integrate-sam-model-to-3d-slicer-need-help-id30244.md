---
topic_id: 30244
title: "Struggling To Integrate Sam Model To 3D Slicer Need Help"
date: 2023-06-26
url: https://discourse.slicer.org/t/30244
---

# Struggling to integrate SAM model to 3D slicer, need help

**Topic ID**: 30244
**Date**: 2023-06-26
**URL**: https://discourse.slicer.org/t/struggling-to-integrate-sam-model-to-3d-slicer-need-help/30244

---

## Post #1 by @Sobia_Khan (2023-06-26 20:51 UTC)

<p>Hi,</p>
<p>I was wondering if anyone could help me with integrating the SAM model into the 3D slicer.</p>
<p>I have spent two days on it and am stuck.</p>
<p>Help will be highly appreciated.</p>
<p>Thanks</p>

---

## Post #2 by @jcfr (2023-06-26 21:27 UTC)

<p>Thanks for reaching out and sorry to hear that you were not able to accomplish your goal.</p>
<p>To help us better understand your issue, would you provide some more context ?</p>

---

## Post #3 by @Sobia_Khan (2023-06-26 21:34 UTC)

<p>I am trying this</p><aside class="onebox githubblob" data-onebox-src="https://github.com/bingogome/samm/blob/main/README.md">
  <header class="source">

      <a href="https://github.com/bingogome/samm/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/bingogome/samm/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">bingogome/samm/blob/main/README.md</a></h4>


      <pre><code class="lang-md"># Segment Any Medical-Model (SAMM): A 3D Slicer integration to Meta's SAM.

[paper](https://arxiv.org/abs/2304.05622)

[Laboratory of Biomechanical and Image Guided Surgical Systems](https://bigss.lcsr.jhu.edu/), [Johns Hopkins University](https://www.jhu.edu/)

[Yihao Liu](https://yihao.one/), [Jeremy Zhang](https://jeremyzz830.github.io/), Zhangcong She

## Known issues
#13 Resolved with a not-so-elegant way. Tested work on MRHead, DZ-MR, MRBrainTumor2 and CTChest data from Slicer. Please report a bug if your data is not working. Note for the first few seconds when you start "Mask Sync", the server is not so stable, wait a few seconds then slide it up and down, the mask then will be updated. Note now you can only work on the RED view. Will update later to support all 3 views.

#17 4GB Nvidia GeForce RTX 3050Ti VRAM issue. On testing a larger test machine, the VRam usage is at around 3GB. Might have issues with smaller machines.

Switch out the model to smaller ones if you have VRAM limit.

## Demo

https://www.youtube.com/watch?v=vZK45noZVIA

## Motivation
</code></pre>



  This file has been truncated. <a href="https://github.com/bingogome/samm/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>First, I have enabled developer tools but I still don’t see the developer tools dropdown on the left.<br>
I tried doing the extension wizard, and then it said install from a file.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24ea5569d1c61a684fdeb2ab6d89e6d5341e7475.png" data-download-href="/uploads/short-url/5gzfhnCTLr0sNObsRgLWKnJofqZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ea5569d1c61a684fdeb2ab6d89e6d5341e7475_2_690x107.png" alt="image" data-base62-sha1="5gzfhnCTLr0sNObsRgLWKnJofqZ" width="690" height="107" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ea5569d1c61a684fdeb2ab6d89e6d5341e7475_2_690x107.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ea5569d1c61a684fdeb2ab6d89e6d5341e7475_2_1035x160.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24ea5569d1c61a684fdeb2ab6d89e6d5341e7475_2_1380x214.png 2x" data-dominant-color="FAFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1913×297 22.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But I am not sure what to upload here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b75e8666c6cae8dbfaed743850e423bc1175f615.png" data-download-href="/uploads/short-url/qa9Ty9Py9tDczujdkL2KQjbNUuF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b75e8666c6cae8dbfaed743850e423bc1175f615.png" alt="image" data-base62-sha1="qa9Ty9Py9tDczujdkL2KQjbNUuF" width="690" height="309" data-dominant-color="F7F9FB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">873×392 16.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>can you please guide me?</p>
<p>Thanks</p>

---

## Post #4 by @Sobia_Khan (2023-06-26 21:39 UTC)

<p>I tried to zip the samm directory and install it from that but this is what I get<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82c8e52e6ad327612fdf8423532ab68466187f7b.png" data-download-href="/uploads/short-url/iEYucT7rD5uoXxiVS5NsFm2iIQz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c8e52e6ad327612fdf8423532ab68466187f7b_2_690x265.png" alt="image" data-base62-sha1="iEYucT7rD5uoXxiVS5NsFm2iIQz" width="690" height="265" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c8e52e6ad327612fdf8423532ab68466187f7b_2_690x265.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c8e52e6ad327612fdf8423532ab68466187f7b_2_1035x397.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82c8e52e6ad327612fdf8423532ab68466187f7b_2_1380x530.png 2x" data-dominant-color="FDFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1764×679 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @pieper (2023-06-26 21:48 UTC)

<p>Maybe have a look at this work and see if it either addresses what you are trying to do or helps narrow down what’s not working for you.</p>
<aside class="quote quote-modified" data-post="24" data-topic="28787">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fsemerar/48/66457_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/integration-of-segment-anything-model/28787/24">Integration of “Segment Anything Model”?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi everybody!  My team and I have just released a new extension called TomoSAM that integrates SAM into Slicer: 


Here is a youtube tutorial video to get started with it: 

  <a href="https://www.youtube.com/watch?v=4nXCYrvBSjk" target="_blank" rel="noopener">
    [TomoSAM Tutorial]
  </a>
  </blockquote>
</aside>


---

## Post #6 by @Sobia_Khan (2023-06-26 21:57 UTC)

<p>Thank you for this Pieper. It is definitely something I would need next, but it doesn’t address how to import and integrate the model into the Slicer, where I am facing the problem.</p>

---

## Post #7 by @jamesobutler (2023-06-26 22:20 UTC)

<p>It appears we need to improve documentation related to the topic of how to load scripted modules that are not available from the Extensions Manager.</p>
<p>The “Additional Module Paths” setting allows for specifying a scripted module’s directory for loading. See <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#additional-module-paths" class="inline-onebox" rel="noopener nofollow ugc">Application settings — 3D Slicer documentation</a>. This is also described in <a href="https://github.com/fsemerar/SlicerTomoSAM#installation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - fsemerar/SlicerTomoSAM: An extension of 3D Slicer using the Segment Anything Model (SAM) to aid the segmentation of 3D data from tomography or other imaging techniques.</a>.</p>
<p>Additionally if using lates Slicer Preview, you can also drag-and-drop the directory into the Slicer main window and it will detect it as a new module to load. See <a href="https://github.com/Slicer/Slicer/commit/1f4ba1af5d019accbe45e2efc637f09f3ca2ef0e" class="inline-onebox" rel="noopener nofollow ugc">ENH: Improve Python scripted module detection when drag-and-dropping · Slicer/Slicer@1f4ba1a · GitHub</a></p>

---
