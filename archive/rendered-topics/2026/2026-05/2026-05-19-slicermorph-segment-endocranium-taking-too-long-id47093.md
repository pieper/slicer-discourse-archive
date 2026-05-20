---
topic_id: 47093
title: "Slicermorph Segment Endocranium Taking Too Long"
date: 2026-05-19
url: https://discourse.slicer.org/t/47093
---

# Slicermorph- Segment Endocranium Taking Too Long

**Topic ID**: 47093
**Date**: 2026-05-19
**URL**: https://discourse.slicer.org/t/slicermorph-segment-endocranium-taking-too-long/47093

---

## Post #1 by @PitaChib (2026-05-19 20:22 UTC)

<p>Hi all, I’ve been doing rodent endocast with wrap solidify for a bit with success, but I’ve always been curious to try out segment endocranium feature automatically. Before I thought my computer was not good enough, but now I’m on a better computer and it will get stuck for overnight if I leave it on. This computer has 64GB of ram and 3D slicer is the only thing that’s on it. The volume consists of only one rodent skull, and the specs are found below.</p>
<p>For segment endocranium, I’m using the default setting, and smoothing kernel of 3mm, max whole of 15mm. Should I be measuring specific measurements before I start it?</p>
<p>This would be great help, thanks so much!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a12837d3859c187c45ad215408979394656397eb.png" data-download-href="/uploads/short-url/mZF2s4TKaBRnvfraoa5WrXmFdGj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a12837d3859c187c45ad215408979394656397eb.png" alt="image" data-base62-sha1="mZF2s4TKaBRnvfraoa5WrXmFdGj" width="482" height="338"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">482×338 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>*I just started another one where the max hole size is 3mm, and it utilizes 100% of CPU and 22GB of the memory. The interface got stuck again but I will wait in the meantime.</p>

---

## Post #2 by @muratmaga (2026-05-19 22:32 UTC)

<p>What is your smoothing kernel size? if you left it at 3mm, for your dataset that would be a 113x113x113 voxel kernel for smoothing, which will ran out of memory. Adjust it to something like 0.1mm, which will give a for more reasonable kernel size of 4x4x4 voxels.</p>
<p>Also in terms segmenting a space, you don’t need such large volume. If you downsample by factor of 2, things will go a lot faster and the difference in the volume sizes will be minuscule.</p>

---
