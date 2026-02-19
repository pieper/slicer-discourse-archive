---
topic_id: 31865
title: "Are All Bones Modelled In 3D Slicer Hollow I Need To Use The"
date: 2023-09-24
url: https://discourse.slicer.org/t/31865
---

# Are all bones modelled in 3D Slicer hollow? I need to use them for FEA.

**Topic ID**: 31865
**Date**: 2023-09-24
**URL**: https://discourse.slicer.org/t/are-all-bones-modelled-in-3d-slicer-hollow-i-need-to-use-them-for-fea/31865

---

## Post #1 by @Danieal_Ahmad (2023-09-24 02:51 UTC)

<p>Hi, I’ve been working on Femur and Tibia bones from a CT scan. I managed to model them out pretty well.</p>
<p>However when I played around the 3D space to look inside the bones, they seem to be empty. Are all bones modelled in 3D Slicer hollow? Then how should I make the whole bone fill up? I intend to do FEA on Ansys.</p>
<p>Also, I intend to create Cancellous region for the Femur bone. Will both the Cortical and Cancellous regions be hollow when I create the Cancellous region too? Please advice me.</p>
<p>Note that I am very new to 3D slicer and have NO knowledge in Ansys. I intend to only learn Ansys when I am done modelling the Femur and Distal bones. Will I be able to fill up the hollow bones in 3D Slicer or Ansys?</p>
<p>Please help thank you.</p>

---

## Post #2 by @manjula (2023-09-24 05:36 UTC)

<p>Hi</p>
<p>you can  use wrap solidify in the segment editor. It is in the extension manager.</p>
<p>SurfaceWrapSolidify extension<br>
also you can hollow it using hollow tool in the segment editor.</p>
<p>you can see here using it to do what you want for the fibula but for different purpose.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="g9Vql5h6uHM" data-video-title="Mandible reconstruction | 3D Slicer Tutorial" data-video-start-time="2m30s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=g9Vql5h6uHM&amp;t=2m30s" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/g9Vql5h6uHM/hqdefault.jpg" title="Mandible reconstruction | 3D Slicer Tutorial" width="" height="">
  </a>
</div>

<p>hope this is what you were looking for</p>

---

## Post #3 by @Danieal_Ahmad (2023-09-24 10:18 UTC)

<p>Hi, I did use the Wrap Solidify extension and managed to beautifully construct the Femur bone. I even smoothen the bone and it looked good.</p>
<p>But I am wondering, inside of the bone however, is hollow. The bone isn’t a filled up solid structure. Is it meant to be that way for all bones constructed in 3D Slicer?</p>

---

## Post #4 by @manjula (2023-09-24 11:09 UTC)

<p>i thinkn answer is in here</p>
<aside class="quote quote-modified" data-post="4" data-topic="18562">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/create-a-3d-solid-model-from-ct-scans/18562/4">Create a 3D solid model from CT scans</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    “Don’t mesh it” is not an option. “Solid geometry” concept only exists in CAD software - it refers to parametric representation of a shape, obtained from combining simple parametric primitives and can be characterized with a few hundred or maybe a few thousand parameters. In contrast, in medical image computing you generate shapes from images, which consists of tens or hundreds of millions of voxels, so the resulting object cannot be practically stored with a parametric representation (you would…
  </blockquote>
</aside>


---

## Post #5 by @evaherbst (2023-09-25 11:28 UTC)

<p>Hello,</p>
<p>The 3D models you usually get from segmentation programs (and most 3D models in general) are surface models, so yes, they will be hollow.</p>
<p>For FEA you want a volumetric model.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> 's Segment Mesher extension for Slicer helps you create volumetric models from segmentations in Slicer: <a href="https://github.com/lassoan/SlicerSegmentMesher" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerSegmentMesher: Create volumetric mesh from segmentation using Cleaver2 or TetGen</a><br>
It uses Cleaver 2 or TetGen to create the tetrahedral elements for the volumetric model.</p>
<p>Cheers,<br>
Eva</p>

---

## Post #6 by @Danieal_Ahmad (2023-10-04 13:20 UTC)

<p>Hi,</p>
<p>Thank you for your kind response. In that case, when I am done segmenting the hollow femur bones, I want to generate volumetric model for FEA.</p>
<p>Am I able to do it in 3D Slicer or should I export the file and open it in Ansys to generate the volumetric model from the hollow model I have from 3D Slicer?</p>

---

## Post #7 by @evaherbst (2023-10-04 13:26 UTC)

<p>Up to you, I did some tests with the slicer modules I mentioned above and was happy with the resulting volumetric meshes, so I plan on making mine in Slicer and loading as volumetric meshes in my FE program.</p>
<p>Cheers,<br>
Eva</p>

---

## Post #8 by @Danieal_Ahmad (2023-10-07 10:17 UTC)

<p>That sounds promising, thank you so much for the suggestions! Will sure to give it a try once I am done segmenting the hollowed bones.</p>

---

## Post #9 by @EliasHarper (2023-10-20 11:49 UTC)

<p>Thank you sir for the video, this is the exact video I was looking for.</p>

---

## Post #10 by @Danieal_Ahmad (2023-10-31 02:40 UTC)

<p>Hi Eva,</p>
<p>I’ve completed with the modelling of all the femur bones that I wanted.</p>
<p>Now I want to prepare them for FEA. You mentioned that you did volumetric meshes in 3D Slicer.</p>
<p>Could you please share with me what are the functions you used and how you used them? Please include some pictures so I could understand better as well as the recommended numerical values to input for the functions used.</p>
<p>Thanks,<br>
Danieal</p>

---

## Post #11 by @evaherbst (2023-10-31 11:08 UTC)

<p>Hi Danieal,</p>
<p>I have done a few tests with SegmentMesher in the past, and I will use it in the future.<br>
However, the parameters really depend on your use case, so I cannot share/recommend any specific settings.</p>
<p>Cheers,<br>
Eva</p>

---
