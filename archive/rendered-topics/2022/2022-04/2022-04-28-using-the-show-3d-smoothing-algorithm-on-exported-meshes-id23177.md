---
topic_id: 23177
title: "Using The Show 3D Smoothing Algorithm On Exported Meshes"
date: 2022-04-28
url: https://discourse.slicer.org/t/23177
---

# Using the show 3D smoothing algorithm on exported meshes

**Topic ID**: 23177
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/using-the-show-3d-smoothing-algorithm-on-exported-meshes/23177

---

## Post #1 by @Tommaso (2022-04-28 16:47 UTC)

<p>Hello everybody,</p>
<p>I am a new user of Slicer and I realized a segmentation based on a US file which I would like to export for additional post processing in a dedicated software</p>
<p>Can you explain me if the algorithm used for mesh display smoothing (described in the link below) can be applied to the mesh as a segmentation smoothing (e.g. like the <em>Joint smoothing</em> algorithm)?</p>
<aside class="quote" data-post="1" data-topic="1933">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/35a633/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/turn-off-all-smoothing-in-segmentation/1933">Turn off all smoothing in segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    O.S. Win 10 - 64bit 
Version: 4.8.1 
Hi there, 
We are willing to apply this software to segment the thalamus and need to correct segmentation errors on a pixel-by-pixel basis. For this reason, we need to abolish any possible type of smoothing on the source image. Is that by any means possible? 
With very best wishes and many thanks in advance, 
Leonardo
  </blockquote>
</aside>

<p>To sum up, I would like to export an STL file containing the mesh:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccd25d31a869093946f3ca760968288c2174134f.png" alt="image" data-base62-sha1="tdW6CIvsmqlBI9FNBSEzPmewpeD" width="658" height="256"></p>
<p>Thanks for the Support,</p>
<p>Tommaso</p>

---

## Post #2 by @lassoan (2022-04-30 04:08 UTC)

<p>You can use the Export to files feature in Segmentations module. All the smoothing that you see is already applied in the exported mesh.</p>

---

## Post #3 by @Tommaso (2022-05-02 07:40 UTC)

<p>Thank you Andras, it worked exactly how I wanted.</p>
<p>Apologies for the silly question.</p>
<p>Tommaso</p>

---
