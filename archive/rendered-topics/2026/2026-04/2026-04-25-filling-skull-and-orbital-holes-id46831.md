---
topic_id: 46831
title: "Filling skull and orbital holes"
date: 2026-04-25
url: https://discourse.slicer.org/t/46831
last_bumped: 2026-04-30T10:21:52.494Z
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

## Post #5 by @Bouroumane_Mohamed_r (2026-04-29 12:03 UTC)

<p>thanks for your answer dear colleague.<br>
I pointed the holes that I want to fill : artifact holes not the natural ones (normal canals and fissures and sutures are respected).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0130f159a48593cea8069bd34ff9f93f644ba39.jpeg" data-download-href="/uploads/short-url/yfNqrk1wq4DILp2D01jjOUqoR29.jpeg?dl=1" title="capture orbite" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0130f159a48593cea8069bd34ff9f93f644ba39_2_458x500.jpeg" alt="capture orbite" data-base62-sha1="yfNqrk1wq4DILp2D01jjOUqoR29" width="458" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f0130f159a48593cea8069bd34ff9f93f644ba39_2_458x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0130f159a48593cea8069bd34ff9f93f644ba39.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0130f159a48593cea8069bd34ff9f93f644ba39.jpeg 2x" data-dominant-color="638066"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture orbite</span><span class="informations">669×730 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32a23e11fa0af2c1644bf4837f2b28219b9be760.jpeg" data-download-href="/uploads/short-url/7dVtxfXWTa5CLkwSRs6TjbAPzGw.jpeg?dl=1" title="capture face post crane.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32a23e11fa0af2c1644bf4837f2b28219b9be760.jpeg" alt="capture face post crane.PNG" data-base62-sha1="7dVtxfXWTa5CLkwSRs6TjbAPzGw" width="534" height="500" data-dominant-color="718D86"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture face post crane.PNG</span><span class="informations">564×528 75.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2026-04-29 12:17 UTC)

<p><a class="mention" href="/u/bouroumane_mohamed_r">@Bouroumane_Mohamed_r</a> - I think you are missing the message some of us are trying to convey, which is that any surface rendering or 3D print is going to convey only partial (and therefor possibly misleading) information.  Trying to manually correct issues may only make the misinformation worse.  If you plan to use this to inform the clinical evaluation of the case, it’s a good strategy to remain faithful to the scan data.</p>
<p>It sounds like you want to make a 3D print.  Rather than trying to make the print look like what you think a skull should look like, you should say that this is a print of all tissue with greater than a certain threshold in CT units.  No extra intererence, no attempt to “fix” the data.</p>
<p>This is why a few of us have suggested volume rendering for a case like this.  I’m not an expert in skull growth, but I understand there is often a gradient of densities and it may be useful to visually evaluate the pattern of these gradients in 3D when considering treatment.</p>

---

## Post #7 by @mohammed_alshakhas (2026-04-29 15:00 UTC)

<p>i do repair those with " fill holes " . the trick here is to use 3d rendering . its very much more sesitive guiding very delicate areas . but in the end you have to use some clinical sense in repair especial if your scan is low quality as in your example .    you can also  use monai AI segmentation its good and will save you time and effort .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/666824b0c76663f9bc7704933f85e5e173f978b6.png" data-download-href="/uploads/short-url/eBVPkVyCjGaZkqe55OkE5Yu94X4.png?dl=1" title="Screenshot 2026-04-29 at 17.57.57" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/666824b0c76663f9bc7704933f85e5e173f978b6_2_690x286.png" alt="Screenshot 2026-04-29 at 17.57.57" data-base62-sha1="eBVPkVyCjGaZkqe55OkE5Yu94X4" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/666824b0c76663f9bc7704933f85e5e173f978b6_2_690x286.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/666824b0c76663f9bc7704933f85e5e173f978b6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/666824b0c76663f9bc7704933f85e5e173f978b6.png 2x" data-dominant-color="F2F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-04-29 at 17.57.57</span><span class="informations">882×366 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Bouroumane_Mohamed_r (2026-04-29 18:50 UTC)

<p>the purpose of the skull model is for craniosynostosis surgical plan, the surgeon only need the skull vault with sutures; thus it’s not mandatory to fill all artifact holes in that case. But I’m curious to know how to fill them in case i would need that</p>

---

## Post #9 by @Bouroumane_Mohamed_r (2026-04-29 19:02 UTC)

<p>thanks for your answer.<br>
I used a 3D Dicom file from the scan of the patient. Is that what you mean?</p>

---

## Post #10 by @ThomasVanParys (2026-04-30 10:21 UTC)

<p>For Volume Rendering:</p>
<ol>
<li>Load in the DICOM file into Slicer (Add DICOM Data)</li>
<li>Navigate to Volume Rendering Module</li>
<li>Select preset (e.g., CT bone) and adjust threshold</li>
<li>volume render should appear in the 3D viewer<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" class="inline-onebox" rel="noopener nofollow ugc">Volume rendering — 3D Slicer documentation</a></li>
</ol>

---
