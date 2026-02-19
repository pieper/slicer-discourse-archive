---
topic_id: 12777
title: "Need Help Saved Scene Will Not Load"
date: 2020-07-29
url: https://discourse.slicer.org/t/12777
---

# Need help! Saved scene will not load. 

**Topic ID**: 12777
**Date**: 2020-07-29
**URL**: https://discourse.slicer.org/t/need-help-saved-scene-will-not-load/12777

---

## Post #1 by @Taylor (2020-07-29 21:29 UTC)

<p>Hello Slicer community,</p>
<p>I am relatively new to slicer, and I am having a problem loading a saved scene that I have been working on the past few months. Until now, the scene would load fine after saving data, turning off computer and coming back to it. Now receiving error message.<br>
Operating system: windows 10<br>
Slicer version:  4.11.0<br>
Expected behavior: drag and drop saved scene into slicer,  scene loads with all completed segmentations.<br>
Actual behavior: drag and drop saved scene into slicer, starts to load then error message below pops up.<br>
Any help appreciated! Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec95065a5cfd75fdecf4f3512b615f526e602691.jpeg" data-download-href="/uploads/short-url/xKTXY0bSQwUmGJJMdNZwfqYCAVz.jpeg?dl=1" title="IMG-8523" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec95065a5cfd75fdecf4f3512b615f526e602691_2_643x500.jpeg" alt="IMG-8523" data-base62-sha1="xKTXY0bSQwUmGJJMdNZwfqYCAVz" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec95065a5cfd75fdecf4f3512b615f526e602691_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec95065a5cfd75fdecf4f3512b615f526e602691_2_964x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec95065a5cfd75fdecf4f3512b615f526e602691_2_1286x1000.jpeg 2x" data-dominant-color="AAADA5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG-8523</span><span class="informations">2876×2236 3.6 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2020-07-29 21:51 UTC)

<p>What happens when you try to directly load that file error is reported (Slicer CNS LH dataset\Segmentation.seg.nrrd)? Just drag and drop it into the Slicer windows.</p>
<p>You have a very large segmentation file, at about 6GB. My suspicion is that during the last scene save, for whatever reason it didnt successfully write whole file, but only about 1/3rd of it.</p>

---

## Post #3 by @muratmaga (2020-07-30 00:08 UTC)

<p>Also following up on this, how long it takes to compress such large volumes might be an issue during saving scenes. You can disable compression for volume and segmentation nodes using .slirerrc.py file from here:<br>
<a href="https://seattlechildrens1.app.box.com/v/SliceMorphDownloads" class="onebox" target="_blank" rel="nofollow noopener">https://seattlechildrens1.app.box.com/v/SliceMorphDownloads</a></p>
<p>I am not entirely sure if you can recover your data (this happened to one of our workshop attendees as well). Going forward, you may individually save the segmentation file, which can give you better control over backup and versioning (like saving them in separate folders in each time).</p>

---
