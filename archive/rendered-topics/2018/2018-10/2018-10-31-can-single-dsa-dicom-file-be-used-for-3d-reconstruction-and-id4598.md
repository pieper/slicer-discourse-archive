---
topic_id: 4598
title: "Can Single Dsa Dicom File Be Used For 3D Reconstruction And"
date: 2018-10-31
url: https://discourse.slicer.org/t/4598
---

# Can single DSA Dicom file be used for 3D reconstruction and viewed in 3D window？

**Topic ID**: 4598
**Date**: 2018-10-31
**URL**: https://discourse.slicer.org/t/can-single-dsa-dicom-file-be-used-for-3d-reconstruction-and-viewed-in-3d-window/4598

---

## Post #1 by @cyufu (2018-10-31 01:32 UTC)

<p>The animation in red window was made by single DSA Dicom file . I am wondering whether this kind of data , copied from DSA work station , can be used for 3D reconstruction and viewed in 3D window.</p>
<p>thanks<br>
Caoyufu</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fef04b66868c4bb434718b260100fa789bf0cce2.gif" alt="GIF" data-base62-sha1="Ani6A4bynuROQHj3yIZhglafElA" width="672" height="458"></p>

---

## Post #2 by @pieper (2018-10-31 01:48 UTC)

<p>Hi <a class="mention" href="/u/cyufu">@cyufu</a> -</p>
<p>Generally no, if you only have projection images you can’t operation on them in 3D.  If you have enough projections you can backproject and make a volume, but you probably need more than is shown in your gif.</p>
<p>There’s some more background on this thread:</p>
<aside class="quote quote-modified" data-post="1" data-topic="4272">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/db5fbb/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/volume-rendering-shows-solid-black-cube-only/4272">Volume rendering shows solid black cube only</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, 
I have a quick question as I am new to slicer and it might just be a simple error. 
I have created a stack of tiff files and managed to load them onto slicer and then adjust the image spacing so that there a full picture from each view. 
The problem comes in when I want to create a volume rendering to show the bones of the specimens in the scan. When I click on the ‘eye’ button to view the volume rendering all I get is a solid black cube and nothing of what is in the scan. 
I have tried …
  </blockquote>
</aside>


---
