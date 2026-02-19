---
topic_id: 8536
title: "Problems When Segmenting Blood Vessels Using Vmtk Threshold"
date: 2019-09-23
url: https://discourse.slicer.org/t/8536
---

# Problems when segmenting blood vessels using VMTK (threshold)

**Topic ID**: 8536
**Date**: 2019-09-23
**URL**: https://discourse.slicer.org/t/problems-when-segmenting-blood-vessels-using-vmtk-threshold/8536

---

## Post #1 by @Deyline (2019-09-23 14:35 UTC)

<p>Hello Slicer wizards,</p>
<p>I’ve been trying for the past weeks to segement brain arteries using Slicer. I’ve already seen a few topics on the discussin forum about this topic, but I still haven’t been successful reconstructing it.</p>
<p>Things I have tried so far:</p>
<ul>
<li>Adjusting the thresholds value in the segment editor tool;</li>
<li>Creating seeds and using the grow from seeds tool;</li>
<li>Using the VMTK module (which I believe is going to be my best option);</li>
<li>Using the SwissSkullStripper, in order to remove the skull;</li>
</ul>
<p>All of the attempts above left me in the same spot, an image where the threshold wouldn’t differentiate vessels from other entitites. I didn’t find this issue when segmenting the aorta from the sample CT-scan provided by Slicer. I could “easily” use the grow from seeds tool and the software would recognize vessels from other entities.</p>
<p>Using the VMTK module, when I preview the volume, it shows that the software recognizes vessels (Image 1), which I assume as a good sign. However, when I start the module, it doesn’t differentiate between bones and other entities (Image 2). I’ve already tried experimenting with threshold values and other options, but the outcome is the same.</p>
<p>Am I doing something wrong (very likely)?</p>
<p>Images: <a href="https://imgur.com/a/P8ZkyQT" rel="nofollow noopener">https://imgur.com/a/P8ZkyQT</a></p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2019-09-23 14:45 UTC)

<p>Have you tried the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/" rel="nofollow noopener">“Vessel Segmentation By Subtraction” segmentation recipe</a>?</p>

---

## Post #3 by @Deyline (2019-09-23 16:50 UTC)

<p>Thanks for the Reply Andras!</p>
<p>I haven’t tried this function yet, but from a quick read, I assume that I can only use this method if I have the images with and without contrast, in order to subtract both and have the vessels as an output. The problem, however, is that I only own the images with contrast, not the “baseline” as the tutorial provides. Because of this, I’m not sure whether the VMTK module will be my best option in this particular case.</p>
<p>Thanks once again!</p>

---

## Post #4 by @lassoan (2019-09-23 17:03 UTC)

<p>If you don’t have contrast-free image it is not a huge issue, you just need to remove the bones that are not well suppressed by the vesselness filter. You can use various Segment Editor tools for this.</p>
<p>Are you sure you don’t have a contrast free acquisition for these patients? Image from several months or years ago may be usable. If there is really nothing that you could use then you may try to use images from similar age/size patients and use deformable transformation in the registration step (instead of rigid).</p>

---

## Post #5 by @Deyline (2019-09-24 12:11 UTC)

<p>Thanks again for the reply Andras,</p>
<p>I spoke to the medical team about having both the contrast free and with contrast and I may be able to have them. However, I’m trying to follow your tip by using the vesselness filter to segment bones and tissues from the vessels, which is the method I was trying to use earlier with no success.<br>
After filtering the vessels, I’m still left with a lot of non-interest entities, such as bones and tissues. Should I manually remove such entities, or is there a tool that may be more efficient and precise (since tissues are so close to vessels, which might result in me losing some vessels in the segmenting process).</p>
<p>Regards.</p>

---

## Post #6 by @lassoan (2019-09-24 12:31 UTC)

<aside class="quote no-group" data-username="Deyline" data-post="5" data-topic="8536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/278dde/48.png" class="avatar"> Deyline:</div>
<blockquote>
<p>After filtering the vessels, I’m still left with a lot of non-interest entities, such as bones and tissues.</p>
</blockquote>
</aside>
<p>This is expected. However, as described in the segmentation recipe linked above, if the suppressed bones and structures are small floating pieces and the vessel tree forms one large object, you can keep the vessel tree and remove everything else by a few clicks (using Islands effect in Segment Editor).</p>

---

## Post #7 by @Deyline (2019-09-30 19:10 UTC)

<p>Hello Andras,</p>
<p>I was able to do the segmenting after many trials and errors, using Island effects and a lot of manual erasing/painting!</p>
<p>However, now I’m encountering a different issue and a couple questions came up.</p>
<ul>
<li>
<p>I’m trying to use the “Hollow” tool in the segment editor in order to have only the surface of the vessels remaining. I watched the example video and I’m not able to recreate what is showed in the <a href="https://www.youtube.com/watch?v=jtDHTaAEilU&amp;t=93s" rel="noopener nofollow ugc">video</a>.<br>
When I apply the tool, my segmented vessel either dissapears (if I use the “inside surface” option) or it creates holes in the surface (if I use the “medial surface” option). I assume this could be happening due to the relatively small diameter of the vessels, when compared to the aorta showed in the video.</p>
</li>
<li>
<p>My other question is regarding the cross-sectional area of the vessel. Is there a specific tool that allows me to have a cross section perpendicular to the vessel, similarly to the video above? In the video, the scissor tool is used, but if I use it Slicer automatically smooths the surface.</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6140dcb659110ddf7a7c6cf9442b89c0464e7b4.png" data-download-href="/uploads/short-url/nHcdYdWkCTeiNJ9eMdxNrNWyjYM.png?dl=1" title="slicer_hollow_issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6140dcb659110ddf7a7c6cf9442b89c0464e7b4_2_690x368.png" alt="slicer_hollow_issue" data-base62-sha1="nHcdYdWkCTeiNJ9eMdxNrNWyjYM" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6140dcb659110ddf7a7c6cf9442b89c0464e7b4_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6140dcb659110ddf7a7c6cf9442b89c0464e7b4_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6140dcb659110ddf7a7c6cf9442b89c0464e7b4.png 2x" data-dominant-color="B5AFBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_hollow_issue</span><span class="informations">1365×729 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks for the support so far,<br>
Regards.</p>

---

## Post #8 by @JanWitowski (2019-10-01 08:52 UTC)

<aside class="quote no-group" data-username="Deyline" data-post="7" data-topic="8536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/278dde/48.png" class="avatar"> Deyline:</div>
<blockquote>
<p>When I apply the tool, my segmented vessel either dissapears (if I use the “inside surface” option) or it creates holes in the surface (if I use the “medial surface” option). I assume this could be happening due to the relatively small diameter of the vessels, when compared to the aorta showed in the video.</p>
</blockquote>
</aside>
<p>This is correct. You can play around with parameters such as shell thickness. Alternatively, you can artificially increase thickness of your model with Margin tool before applying Hollow.</p>
<aside class="quote no-group" data-username="Deyline" data-post="7" data-topic="8536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/278dde/48.png" class="avatar"> Deyline:</div>
<blockquote>
<p>My other question is regarding the cross-sectional area of the vessel. Is there a specific tool that allows me to have a cross section perpendicular to the vessel, similarly to the video above? In the video, the scissor tool is used, but if I use it Slicer automatically smooths the surface.</p>
</blockquote>
</aside>
<p>This is currently the best approach for it as far as I know. Regarding smoothing, you can turn off or reduce surface smoothing level in the module itself:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a340613c873d3fe5b3d658528c448cd5ff1f024.png" alt="image" data-base62-sha1="61lvSdWU4YkZHZtLHwKuxcfXfRW" width="389" height="125"></p>

---

## Post #9 by @lassoan (2019-10-02 01:21 UTC)

<p>This looks good! The only thing you missed is setting sufficiently fine resolution for your segmentation. Spacing of the segmentation’s binary labelmap representation should be at least 1/5th but preferably 1/10th of the smallest vessel diameter. See <a href="https://discourse.slicer.org/t/cannot-apply-threshold-on-roi/7269/2">here</a> how to change the resolution of a segmentation node.</p>

---

## Post #10 by @Deyline (2019-10-25 18:32 UTC)

<p>Update: I was able to reconstruct what I needed after spending some time with the software. However, after dealing with a few more images a question popped. Is it possible to reconstruct vessel volumes from CT-Scans that contain coils or other devices? For example, in the following image the patient went through an embolization process, and thus, has the presence of coils. When we look at the image, we can see some sort of “refraction” (not sure how can I call it), which hinders the reconstruction of the volume. Does this mean that any kind of Scan that contain such devices is no fit for reconstruction?</p>
<p>The reason why I’m asking this, is because I have interest in comparing the pre and post operatory situations.</p>
<p>Regards.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/284b688d6cab4c8275a1e5275f3a565bd997e577.png" alt="coils_scan" data-base62-sha1="5KsEXimdwPxyKuiUXHw7QUUFlif" width="233" height="218"></p>

---

## Post #11 by @pieper (2019-10-25 19:13 UTC)

<p>That’s metal artifact and it’s pretty hard to work around (see, for example, <a href="https://pubs.rsna.org/doi/10.1148/rg.2018170102">this paper</a>).  Generally speaking if you can’t find a window/level option that shows detail inside the flare there’s not a lot you can do.</p>

---

## Post #12 by @Reasat_E_Noor (2022-12-20 13:00 UTC)

<p>Can you create a video of this work, it would be great help for my research work</p>

---
