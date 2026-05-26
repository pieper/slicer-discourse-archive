---
topic_id: 47093
title: "Slicermorph- Segment Endocranium Taking Too Long"
date: 2026-05-19
url: https://discourse.slicer.org/t/47093
last_bumped: 2026-05-21T23:15:02.685Z
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

## Post #3 by @PitaChib (2026-05-21 19:49 UTC)

<p>Thanks for this, this actually makes a lot of sense and it worked for the first time! I ended up making a cropped downscaled volume to be faster since I don’'t really need a outside skull at the moment.</p>
<p>For anyone out there that might need this information: I’m running tests to see the best combo to save my time, and note the parameters are from my scans and the organism that I’m working with.</p>
<p>Another thing worth noting is the max. hole size is basically same parameter in SplitCavities <em>which I did not realize at first</em>. In case anyone else have the same questions. <a href="https://discourse.slicer.org/t/wrap-solidify-how-can-i-choose-split-cavities/26231" class="inline-onebox">Wrap Solidify: How can I choose "split cavities"?</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d43aa4b12e2121dc4379cdbd89bbbe20ebfb9f4.jpeg" data-download-href="/uploads/short-url/8JY63HsN4rT28K52YuUd9FNgXbK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d43aa4b12e2121dc4379cdbd89bbbe20ebfb9f4_2_690x339.jpeg" alt="image" data-base62-sha1="8JY63HsN4rT28K52YuUd9FNgXbK" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d43aa4b12e2121dc4379cdbd89bbbe20ebfb9f4_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d43aa4b12e2121dc4379cdbd89bbbe20ebfb9f4_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d43aa4b12e2121dc4379cdbd89bbbe20ebfb9f4.jpeg 2x" data-dominant-color="898884"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1320×650 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2026-05-21 22:24 UTC)

<p>Left and right has a difference of 5mm3, which is less than 1% of the total volume.</p>

---

## Post #5 by @PitaChib (2026-05-21 23:15 UTC)

<p>Yes! I was really surprised. I then ran another one with 2x downscale, and it’s even closer to the original size. Super happy about the increased efficiency. Thanks so much.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0599efc943b632c352f1f330c75e487e521f7bdb.jpeg" data-download-href="/uploads/short-url/Nyc66g7rZfRtBP6Wd0l5yjgn5p.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0599efc943b632c352f1f330c75e487e521f7bdb_2_530x499.jpeg" alt="image" data-base62-sha1="Nyc66g7rZfRtBP6Wd0l5yjgn5p" width="530" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0599efc943b632c352f1f330c75e487e521f7bdb_2_530x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/0599efc943b632c352f1f330c75e487e521f7bdb_2_795x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/0599efc943b632c352f1f330c75e487e521f7bdb.jpeg 2x" data-dominant-color="ADABA9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1034×974 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
