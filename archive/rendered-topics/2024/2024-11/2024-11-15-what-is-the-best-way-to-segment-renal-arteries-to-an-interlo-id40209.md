---
topic_id: 40209
title: "What Is The Best Way To Segment Renal Arteries To An Interlo"
date: 2024-11-15
url: https://discourse.slicer.org/t/40209
---

# What is the best way to segment renal arteries to an interlobar level?

**Topic ID**: 40209
**Date**: 2024-11-15
**URL**: https://discourse.slicer.org/t/what-is-the-best-way-to-segment-renal-arteries-to-an-interlobar-level/40209

---

## Post #1 by @ntzvetkov (2024-11-15 06:00 UTC)

<p>I’ve been struggling with the segmentation of the renal artery branches for so long. From what I have read VMTK would be a good tool to do a proper segmentation, but I just can’t figure out how to apply it. There is an module for guided artery segmentation but i can’t find a tutorial. The threshold method is ok, but after the renal hilium you get a lot of blob segmentations from the perfused kidney parenchyma, which make it even harder to find the interlobar arteries. I’m stuck to a point where i just use the brush… PLEASE HELP!</p>

---

## Post #2 by @chir.set (2024-11-15 07:14 UTC)

<aside class="quote no-group" data-username="ntzvetkov" data-post="1" data-topic="40209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ntzvetkov/48/78547_2.png" class="avatar"> ntzvetkov:</div>
<blockquote>
<p>the interlobar arteries</p>
</blockquote>
</aside>
<p>You should have good contrast intensities at this level, with different intensity ranges in the veins. If you have a dataset with such requirements, it would be a lucky one. I am assuming that you are working with CT scans with contrast. Sometimes we come to a simple conclusion: it’s not possible. Can you share your data?</p>

---

## Post #3 by @ntzvetkov (2024-11-16 07:59 UTC)

<p>Yes, we are working with contrast CT’s and a lot of what we have are good arterial phases, but not that great. Ok but if not going that far as interlobar, since that seems a little too farfetched, is there an easier way to go for the segment arteries level at least. And is it possible if I do the segmental arteries to generate perfusion zones of the kidney based on them. What kind of data do you want - the DICOM or slicer data?</p>

---

## Post #4 by @chir.set (2024-11-16 08:26 UTC)

<aside class="quote no-group" data-username="ntzvetkov" data-post="3" data-topic="40209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ntzvetkov/48/78547_2.png" class="avatar"> ntzvetkov:</div>
<blockquote>
<p>the DICOM or slicer data?</p>
</blockquote>
</aside>
<p>An NRRD file at best, or an anonymized DICOM series as a common archive (zip, tarball).</p>

---

## Post #5 by @ntzvetkov (2024-11-16 08:36 UTC)

<p>I am attaching here a NRRD file of a contrast abdomen CT. I was going for the malrotated right kindey with the big tumor. <a href="https://drive.google.com/file/d/1-MkB1eSRqyKh0YPvRLjbxceZ5b_l8FtW/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">6 Abd arterial 1.5 B41s.nrrd - Google Drive</a></p>

---

## Post #6 by @chir.set (2024-11-16 09:41 UTC)

<p>Thank you for providing the data.</p>
<p>This study is poorly contrasted. I could only get the 2 extra-hilar renal arteries using the ‘<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/GuidedArterySegmentation.md" rel="noopener nofollow ugc">Guided artery segmentation</a>’ module with an intensity tolerance of 70. The arteries in the kidney itself cannot be distinguished by the eye, even if we use colorful lookup tables and adjusting window/level.</p>
<p>The picture shows the segments and the input curves, which are self-explanatory.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/986559a783cccaad1975180e0c59b2595ccfebe9.jpeg" data-download-href="/uploads/short-url/lK9ItrqhzofXsP2FdjTVHwpFdWx.jpeg?dl=1" title="right_renal_poor_contrast" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/986559a783cccaad1975180e0c59b2595ccfebe9_2_690x464.jpeg" alt="right_renal_poor_contrast" data-base62-sha1="lK9ItrqhzofXsP2FdjTVHwpFdWx" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/986559a783cccaad1975180e0c59b2595ccfebe9_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/986559a783cccaad1975180e0c59b2595ccfebe9_2_1035x696.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/986559a783cccaad1975180e0c59b2595ccfebe9.jpeg 2x" data-dominant-color="2C2C28"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">right_renal_poor_contrast</span><span class="informations">1341×902 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The intensities in the aorta are around 200, it should be around 400 - 550 for a good quality study. IMO, it’s illusory to think about selective segmentation inside the kidney itself.</p>

---

## Post #7 by @ntzvetkov (2024-11-23 17:23 UTC)

<p>Thank you very much for the display and the vmtk guide links!! Do you have any opinion on the estimated kidney perfusion zones based on the arterial segmentation (in cases with better contrast series)?</p>

---

## Post #8 by @chir.set (2024-11-23 19:47 UTC)

<aside class="quote no-group" data-username="ntzvetkov" data-post="7" data-topic="40209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ntzvetkov/48/78547_2.png" class="avatar"> ntzvetkov:</div>
<blockquote>
<p>(in cases with better contrast series)</p>
</blockquote>
</aside>
<p>I think that CT scans won’t answer this question faithfully. We can roughly say such artery or branch for the lower or upper part of the kidney since it’s a terminal arterial tree. For precise segments, angiograms with distal catheter injection of contrast should give a better estimate.</p>

---
