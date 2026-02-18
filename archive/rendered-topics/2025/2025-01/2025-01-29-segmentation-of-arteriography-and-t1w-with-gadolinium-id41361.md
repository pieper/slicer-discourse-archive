# Segmentation of arteriography and T1w with Gadolinium

**Topic ID**: 41361
**Date**: 2025-01-29
**URL**: https://discourse.slicer.org/t/segmentation-of-arteriography-and-t1w-with-gadolinium/41361

---

## Post #1 by @papagif66 (2025-01-29 18:21 UTC)

<p>Hello,<br>
I’m working on a Moya Moya patient dataset, that includes T1w with Gadolinuim, CT, and arteriography.<br>
I registered the images and segmented the skull, from the CT and also from the T1Gado using mri_synthstrip.<br>
Now, I want to segment vessels, both on the arteriography and on the T1Gado.<br>
Especially the ones close to or crossing the skull.<br>
I started playing with various modules, but mostly used Volume Rendering to get that kind of image:</p>
<div class="d-image-grid">
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24fb7dc620f547243454006eca2975a48f56ca46.jpeg" data-download-href="/uploads/short-url/5ha0pg2I1xK9HYKfXbCiFa7wTRA.jpeg?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24fb7dc620f547243454006eca2975a48f56ca46_2_401x499.jpeg" alt="Screenshot_2" data-base62-sha1="5ha0pg2I1xK9HYKfXbCiFa7wTRA" width="401" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24fb7dc620f547243454006eca2975a48f56ca46_2_401x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24fb7dc620f547243454006eca2975a48f56ca46_2_601x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24fb7dc620f547243454006eca2975a48f56ca46_2_802x998.jpeg 2x" data-dominant-color="8A8099"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">972×1211 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6e826bf156666a2933cf10ffaf20de6c60365a2.jpeg" data-download-href="/uploads/short-url/snBV6OTjOmH4Vj8gNPONhSZbT9w.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6e826bf156666a2933cf10ffaf20de6c60365a2_2_401x499.jpeg" alt="Screenshot_1" data-base62-sha1="snBV6OTjOmH4Vj8gNPONhSZbT9w" width="401" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6e826bf156666a2933cf10ffaf20de6c60365a2_2_401x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6e826bf156666a2933cf10ffaf20de6c60365a2_2_601x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6e826bf156666a2933cf10ffaf20de6c60365a2_2_802x998.jpeg 2x" data-dominant-color="4E4D54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">972×1211 92.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e25496f3551f18837a362e7195ab0033d0065eb6.jpeg" data-download-href="/uploads/short-url/wid8JhnSmygGMZ9fHkUe3D03sPA.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25496f3551f18837a362e7195ab0033d0065eb6_2_401x499.jpeg" alt="Screenshot" data-base62-sha1="wid8JhnSmygGMZ9fHkUe3D03sPA" width="401" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25496f3551f18837a362e7195ab0033d0065eb6_2_401x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25496f3551f18837a362e7195ab0033d0065eb6_2_601x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25496f3551f18837a362e7195ab0033d0065eb6_2_802x998.jpeg 2x" data-dominant-color="53525A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">972×1211 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</div>
<p>Any advices/hints/tricks how I could process the T1Gado and the Arterio to obtain nice and accurate vessels, including small ones?<br>
Thanx,<br>
Eric</p>

---

## Post #2 by @pieper (2025-01-30 21:26 UTC)

<p>Both datasets look really nice.  Did you try registering them?  And did the vessels align well?  The volume renderings look cluttered by noise (and enhancement from small vessels).  Maybe try adding the two scans together with Add ScalarVolumes and then volume rendering or thresholding the result.  This could cancel out the noise.</p>

---

## Post #3 by @papagif66 (2025-02-07 13:09 UTC)

<p>Dear Steve, thanks for your comment. I registered everything indeed. I’ll try following your advice. Sara also remembered me to look at related topics <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> I’ll do that . Best</p>

---

## Post #4 by @anita_ghodsi (2025-02-07 22:17 UTC)

<p>Hi Eric,<br>
I am relatively new to 3D slicer and was wondering if you could instruct me on how to create a similar segmentation of the vessels. The data I am working with is a high resolution CT scan of mouse liver–I am interested in the connectivity of the vasculature.</p>
<p>Thank you!<br>
Anita</p>

---

## Post #5 by @papagif66 (2025-02-08 09:04 UTC)

<p>Hi Anita,<br>
Actually, I didn’t segment the vessels, I only loaded the arteriography (DCT) volume in the Volume Rendering plugin, chose a PreSet and play with the Shift value and Advanced …<br>
My problem is indeed also to get a segmentation of the vessels.<br>
I can share my data, and/or you can share yours, and I’ll try to play with it.<br>
Let me know.<br>
Best,<br>
Eric</p>

---

## Post #6 by @papagif66 (2025-03-12 18:25 UTC)

<p>Hello again,<br>
I played more with my data, and discussed more with my neurovascular neurosurgeon colleague.<br>
Therefore, I can be more specific: I would like to segment the vasculature from the arterio image (DCT), but distinguish the carotid tree and tne meningeal tree.<br>
I tried to use various modules to segment vessels, playing with Segment Editor tools, but failed.<br>
Any hints / links / howto’s welcome!<br>
I can share the volume I’m dealing with, too.<br>
Images below illsutrate my attempts and show also, using volume rendering, the vasculature (both the carotid tree and the meningeal tree).<br>
Thanks!<br>
Eric<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f039303fa098f130bf051cd65e27928678a73dd4.png" data-download-href="/uploads/short-url/yh77m3BhTwVn2DgWZs4WwZi2osY.png?dl=1" title="dis1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f039303fa098f130bf051cd65e27928678a73dd4_2_577x500.png" alt="dis1" data-base62-sha1="yh77m3BhTwVn2DgWZs4WwZi2osY" width="577" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f039303fa098f130bf051cd65e27928678a73dd4_2_577x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f039303fa098f130bf051cd65e27928678a73dd4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f039303fa098f130bf051cd65e27928678a73dd4.png 2x" data-dominant-color="9698AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dis1</span><span class="informations">698×604 416 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ecd7ea203c554954aa92a54f3c5bcdf1a8b0772.jpeg" data-download-href="/uploads/short-url/mEPI3zXxUstTHmv66wkteLnNkBA.jpeg?dl=1" title="dis2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ecd7ea203c554954aa92a54f3c5bcdf1a8b0772.jpeg" alt="dis2" data-base62-sha1="mEPI3zXxUstTHmv66wkteLnNkBA" width="577" height="500" data-dominant-color="8B939F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dis2</span><span class="informations">698×604 75.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddb68440a5e8dfead3274e79638abd4dfe33366b.jpeg" data-download-href="/uploads/short-url/vDmyMvosZDSp79N5gEtnjzLGjLZ.jpeg?dl=1" title="dis3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddb68440a5e8dfead3274e79638abd4dfe33366b.jpeg" alt="dis3" data-base62-sha1="vDmyMvosZDSp79N5gEtnjzLGjLZ" width="577" height="500" data-dominant-color="9190AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dis3</span><span class="informations">698×604 55.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/770ddebe3da5dffae336e647519178f6f1148340.jpeg" data-download-href="/uploads/short-url/gZcxcwcOQOQ16GLZyAXIX3PgcRG.jpeg?dl=1" title="dis4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/770ddebe3da5dffae336e647519178f6f1148340_2_563x500.jpeg" alt="dis4" data-base62-sha1="gZcxcwcOQOQ16GLZyAXIX3PgcRG" width="563" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/770ddebe3da5dffae336e647519178f6f1148340_2_563x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/770ddebe3da5dffae336e647519178f6f1148340_2_844x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/770ddebe3da5dffae336e647519178f6f1148340_2_1126x1000.jpeg 2x" data-dominant-color="605E5D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dis4</span><span class="informations">1397×1239 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @pieper (2025-03-12 18:39 UTC)

<p>Is this data shareable publicly?  It looks like it would be a highly useful reference dataset.</p>
<p>Regarding the segmentation, are you just trying to get rid of all non-vessel structures?</p>

---

## Post #8 by @nagy.attila (2025-03-12 20:10 UTC)

<p>Hi,</p>
<p>Maybe it worth to take a look at <a href="https://lassoan.github.io/SlicerSegmentationRecipes/" rel="noopener nofollow ugc">these recipes</a> from András Lasso.<br>
The one with segmentation by subtraction worked out pretty nice in our case. We segmented the syphon part of the carotid and had pretty nice results. True, it was more specific, and in general a smaller volume of interest, but still may worth a try.<br>
Also the VMTK extension may worth another shot, even though it has its learning curve for sure <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @drnoorfatima (2026-02-17 12:54 UTC)

<p>Hi Eric,</p>
<p>Moyamoya vasculature is one of the more challenging segmentation problems precisely because of what makes it clinically interesting,  the abnormal collateral networks, the variable vessel caliber, and the proximity to skull all make standard vessel segmentation approaches unreliable.</p>
<p>Distinguishing the carotid tree from the meningeal tree adds another layer on top of that, since it requires more than just vessel extraction, it requires anatomically informed separation which automated tools generally can’t do without significant post-processing.</p>
<p>The fact that you already have registered T1Gado, CT and arteriography puts you in a much better position than most, but the vessel segmentation step itself, especially for small vessels close to the skull, is where the workflow gets non-obvious.</p>
<p>I work with neurovascular segmentation and have a clinical neurology background, so this kind of case is something I find genuinely interesting. DM me I am happy to look at what you have and discuss an approach.</p>

---
