---
topic_id: 25471
title: "Scale Issue With Auto3Dgm"
date: 2022-09-28
url: https://discourse.slicer.org/t/25471
---

# Scale issue with Auto3dgm

**Topic ID**: 25471
**Date**: 2022-09-28
**URL**: https://discourse.slicer.org/t/scale-issue-with-auto3dgm/25471

---

## Post #1 by @Osteodonna (2022-09-28 22:23 UTC)

<p>I’ve run into what I hope is a newbie error–I’m using Auto3dgm to align series of meshes (all ply files of a femur, same species). The alignments look great, but the scale is completely wonky.</p>
<p>For example, when I measure length on the before scan, the ruler tool shows 135mm. When it check it on the aligned scan after running Auto3dgm the length is 0.003337mm.</p>
<p>I’ve checked the Auto3dgm settings and each of the meshes and everything looks right. Tried all the standard things like relaunch/reboot. Is there something obvious I’m missing?</p>
<p>Many thanks for your help/advice!</p>

---

## Post #2 by @muratmaga (2022-09-29 15:06 UTC)

<p>As I recall Auto3Dgm saves multiple outputs. If you want to preserve the scale and still have your pseudolandmarks on the model, I think the folder you want is OSS (original sample space or something like that).</p>

---

## Post #3 by @Osteodonna (2022-09-29 15:36 UTC)

<p>Hello,</p>
<p>Thanks for helping me troubleshoot this. The landmark files are all there as they should be, but my goal with Auto3dgm was to automate mesh alignments so I can do batch alignments and use the aligned meshes in another program where the scale will be important.</p>
<p>I’m hoping to find a way to either restore the scale on the aligned scans, or to prevent Auto3dgm from adjusting the scale at all if that’s possible.</p>
<p>Below are before-alignment and after-alignment photos of the same mesh.</p>
<p>Thanks and appreciate your help on this!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81a660b18e0b2afe85c65aad0d95c8eaf43db529.png" data-download-href="/uploads/short-url/iuW3umxFpCCJ74tKXFueQ9xmyGR.png?dl=1" title="Before" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81a660b18e0b2afe85c65aad0d95c8eaf43db529_2_690x200.png" alt="Before" data-base62-sha1="iuW3umxFpCCJ74tKXFueQ9xmyGR" width="690" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81a660b18e0b2afe85c65aad0d95c8eaf43db529_2_690x200.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81a660b18e0b2afe85c65aad0d95c8eaf43db529_2_1035x300.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81a660b18e0b2afe85c65aad0d95c8eaf43db529_2_1380x400.png 2x" data-dominant-color="999BCD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Before</span><span class="informations">2986×866 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/161d3f2b475ee0bdca21f59bc13599f08fbda025.jpeg" data-download-href="/uploads/short-url/39Daf9jU7doWCgYZvq8vsqmTvnL.jpeg?dl=1" title="After" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/161d3f2b475ee0bdca21f59bc13599f08fbda025_2_690x200.jpeg" alt="After" data-base62-sha1="39Daf9jU7doWCgYZvq8vsqmTvnL" width="690" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/161d3f2b475ee0bdca21f59bc13599f08fbda025_2_690x200.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/161d3f2b475ee0bdca21f59bc13599f08fbda025_2_1035x300.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/161d3f2b475ee0bdca21f59bc13599f08fbda025_2_1380x400.jpeg 2x" data-dominant-color="9D9FC4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">After</span><span class="informations">2986×866 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2022-09-29 18:44 UTC)

<p>If your goal is to just align models (but not create pseudoLMs), then I don’t think Auto3Dgm will work for you, as part of its pipeline requires scaling to unit size. You can of course manually scale the aligned models: Do what you just did in the screenshot, divide the numbers to each and scale the small model by that factor (using the transforms module or the surface toolbox).</p>
<p>If you are only looking into alignment, you might find ALPACA more convenient and probably faster. It is not meant as a stand alone alignment tool, so you do need to one dummy pointList to fool into thinking you are transferring points. Choose one of your samples as the sample that everything is going to be aligned against, and enter that as the target model, and set one of the femur that needs to be aligned as the source (also create a dummy markup point), and run through the ALPACA with default settings.</p>
<p>What you want (aligned sample), will be available under the Display Source Model (rigidly registered). In this case the red gorilla skull is the one that was aligned, and the yellow skull was the target.</p>
<p>You do have to run one sample at a time, but it should be relatively quick (1-2 minutes per sample). In future we hope to have a standalong pointcloud based registration of 3D models (so that you don’t fake it in ALPACA), but that’s still in works…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/242e568a6d00020715e9bddb44f766efb8c9bfcf.jpeg" data-download-href="/uploads/short-url/5a4t01Sd68Ler8B9Q0hpJA2Spjx.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/242e568a6d00020715e9bddb44f766efb8c9bfcf_2_690x388.jpeg" alt="image" data-base62-sha1="5a4t01Sd68Ler8B9Q0hpJA2Spjx" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/242e568a6d00020715e9bddb44f766efb8c9bfcf_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/242e568a6d00020715e9bddb44f766efb8c9bfcf_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/242e568a6d00020715e9bddb44f766efb8c9bfcf_2_1380x776.jpeg 2x" data-dominant-color="BFAABF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1081 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Osteodonna (2022-09-30 13:42 UTC)

<p>Hello again,</p>
<p>Thank you for the explanation on Auto3dgm–that helped me understand the scale transforms. Somewhere in the cobwebs of my mind I remember playing with ALPACA, so I’ll revisit that.</p>
<p>Many thanks for your time!</p>

---
