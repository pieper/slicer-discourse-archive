---
topic_id: 46831
title: "Filling Skull And Orbital Holes"
date: 2026-04-25
url: https://discourse.slicer.org/t/46831
---

# Filling skull and orbital holes

**Topic ID**: 46831
**Date**: 2026-04-25
**URL**: https://discourse.slicer.org/t/filling-skull-and-orbital-holes/46831

---

## Post #1 by @Bouroumane_Mohamed_r (2026-04-25 10:10 UTC)

<p>Hello dear Slicer Community,<br>
It’s a pleasure and honor to post my first message.<br>
I’m a beginner using 3D Slicer software.<br>
I share with you a case of child craniosynostosis, surgeons asked for a 3D model to plan surgery.<br>
I need the steps (step by step) to fill skull and orbital walls’ holes without affecting sutures too much.<br>
i downloaded the wrapSolidify Extension but i don’t know how to fix the parameters for this specific indication.<br>
thanks a lot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/346549a9e891cd2638af46dab3d1256d8d44e408.jpeg" data-download-href="/uploads/short-url/7tvPRmTpVZEhyy9ByzQ4yweyWs8.jpeg?dl=1" title="capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/346549a9e891cd2638af46dab3d1256d8d44e408.jpeg" alt="capture" data-base62-sha1="7tvPRmTpVZEhyy9ByzQ4yweyWs8" width="534" height="500" data-dominant-color="748E84"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture</span><span class="informations">564×528 69.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c982dc79d26cb2915523689ae555604b33eb5264.jpeg" data-download-href="/uploads/short-url/sKEl6Jkpl68YSejo50fsBQjmcNm.jpeg?dl=1" title="capture orbite" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c982dc79d26cb2915523689ae555604b33eb5264_2_458x500.jpeg" alt="capture orbite" data-base62-sha1="sKEl6Jkpl68YSejo50fsBQjmcNm" width="458" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c982dc79d26cb2915523689ae555604b33eb5264_2_458x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c982dc79d26cb2915523689ae555604b33eb5264.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c982dc79d26cb2915523689ae555604b33eb5264.jpeg 2x" data-dominant-color="628166"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture orbite</span><span class="informations">669×730 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-04-25 13:08 UTC)

<p>I’m not sure which holes you want to fill, but you need to be very careful modifying the geometry of the scan.  If you are planning to 3D print something you want be sure it is as faithful as possible to the actual scan or it could mislead the surgeons about the actual anatomy.</p>
<p>For this application a volume rendering of the data with no editing at all might be the safest route.</p>

---

## Post #3 by @manjula (2026-04-25 17:39 UTC)

<p>I would suggest you to try dental segmentator module for the segmentation of the skull and you will end up.with good results</p>

---

## Post #4 by @ThomasVanParys (2026-04-25 17:41 UTC)

<p>I recommend you use the volume rendering from the scan instead of the segmented mesh, as this will display sutures (patent or fused) more clearly.</p>

---
