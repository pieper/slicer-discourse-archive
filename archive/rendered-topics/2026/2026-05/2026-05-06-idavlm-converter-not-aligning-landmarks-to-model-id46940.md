---
topic_id: 46940
title: "IDAVLM Converter Not Aligning Landmarks to Model"
date: 2026-05-06
url: https://discourse.slicer.org/t/46940
last_bumped: 2026-05-07T14:31:45.640Z
---

# IDAVLM Converter Not Aligning Landmarks to Model

**Topic ID**: 46940
**Date**: 2026-05-06
**URL**: https://discourse.slicer.org/t/idavlm-converter-not-aligning-landmarks-to-model/46940

---

## Post #1 by @ThomasVanParys (2026-05-06 15:28 UTC)

<p>Hello All,</p>
<p>I have create a patch in Landmark IDAV, converting the .PTS in SlicerMorph IDAVLM converter. However, they do not align with the corresponding mesh used in Landmark as seen in the UI:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60eb67ea9d63cd73a4a669aa9b8292ece3ba31cb.jpeg" data-download-href="/uploads/short-url/dPobU9MnODfYK8ssgTuZwKW5HVp.jpeg?dl=1" title="Screenshot 2026-05-06 162357" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60eb67ea9d63cd73a4a669aa9b8292ece3ba31cb_2_543x500.jpeg" alt="Screenshot 2026-05-06 162357" data-base62-sha1="dPobU9MnODfYK8ssgTuZwKW5HVp" width="543" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60eb67ea9d63cd73a4a669aa9b8292ece3ba31cb_2_543x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60eb67ea9d63cd73a4a669aa9b8292ece3ba31cb.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60eb67ea9d63cd73a4a669aa9b8292ece3ba31cb.jpeg 2x" data-dominant-color="9C9DA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-05-06 162357</span><span class="informations">608×559 57.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am clearly missing a stage, but cannot work it out (both mesh and landmarks need a common coordinate system clearly…).</p>
<p>Thanks for the help</p>

---

## Post #2 by @muratmaga (2026-05-06 15:40 UTC)

<p>We don’t really support the IdavLMConverter anymore, and soon will remove it. There is the similar functionality in SlicerMorph in the module <code>PlaceLandmarkGrid</code>. <a href="https://github.com/SlicerMorph/Tutorials/tree/main/GridBasedLandmarking" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/GridBasedLandmarking at main · SlicerMorph/Tutorials · GitHub</a></p>
<p>It might be LPS vs RAS issue, but again it is not supported. I suggest not using it.</p>

---

## Post #3 by @ThomasVanParys (2026-05-06 18:22 UTC)

<p>Thanks Murat,<br>
I find that SlicerMorph’s <code>PlaceLandmarkGrid</code> function struggles with even distribution of semi-landmarks within the patch and their projection onto a surface (such as a scapular fossa I am currently dealing with). Any tips with this other than manual adjustment and boosting the projection factor? Thanks!<br>
Tom</p>

---

## Post #4 by @muratmaga (2026-05-06 19:21 UTC)

<p>If you can share models and landmarks that goes with them, along with a screenshot of how you are placing the grid, I can take a look.</p>

---

## Post #5 by @ThomasVanParys (2026-05-07 08:25 UTC)

<p>Thanks Murat<br>
Actually, I have had a look and it seems to be working fine now(?!). Some scapulae are easier to apply patches to than others, however, my plan is to merge two smaller patches to minimise bending energy and complicated geometric spread over a single grid… I appreciate the help.</p>

---

## Post #6 by @muratmaga (2026-05-07 14:31 UTC)

<aside class="quote no-group" data-username="ThomasVanParys" data-post="5" data-topic="46940">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>Actually, I have had a look and it seems to be working fine now(?!). Some scapulae are easier to apply patches to than others, however, my plan is to merge two smaller patches to minimise bending energy and complicated geometric spread over a single grid… I appreciate the help.</p>
</blockquote>
</aside>
<p>I am glad to hear it is working. There are quite a bit of heuristics (such as projection factor) that depends on the scale of the data, and sometimes what we exposed on the UI is not within the range that is relevant for that specific data. I find it quite useful to give the source code to the LLM and explain problem show it visually and ask suggestions.</p>

---
