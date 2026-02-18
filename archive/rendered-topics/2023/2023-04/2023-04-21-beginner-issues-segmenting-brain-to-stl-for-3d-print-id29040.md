# Beginner issues segmenting brain to stl for 3d print

**Topic ID**: 29040
**Date**: 2023-04-21
**URL**: https://discourse.slicer.org/t/beginner-issues-segmenting-brain-to-stl-for-3d-print/29040

---

## Post #1 by @H_Smith (2023-04-21 08:52 UTC)

<p>Hi!</p>
<p>My aim is to take MRI brain scan data to an .stl for 3D print, for a student I’m working with. I have 3 questions, hopefully pretty basic! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<ol>
<li>
<p>Organs vs bone<br>
I created an .stl very successfully for a skull a few years ago but trying again with a brain, it seems to be more tricky (or I’m missing a few tricks). Should it be possible to get as good a result for the brain (MRI) as with the skull - is it just a harder workflow or perhaps the MRI wasn’t very high resolution and the problem lies in the data acquisition itself and the student needs to get a dye-enchanced or higher res scan?</p>
</li>
<li>
<p>Working with data from multiple planes.<br>
I have these multiple volumes and only seem to be able to work on one at a time to make each segmentation.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4719145e818982a6a2c890218dc93020a5312689.jpeg" alt="all MRI data" data-base62-sha1="a8XDfJLqLQHFlOVSJ5pQQ8h4buF" width="461" height="203"><br>
The axial volume segmentation looks good of course from the top but terrible from the side and therefore in 3D:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c664e2d3b22e8aa9a3b673052b2e01ce42c4f06.jpeg" data-download-href="/uploads/short-url/mjzFLvQWwjvqp8rEwEiGVHNe81E.jpeg?dl=1" title="axial top" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c664e2d3b22e8aa9a3b673052b2e01ce42c4f06_2_452x499.jpeg" alt="axial top" data-base62-sha1="mjzFLvQWwjvqp8rEwEiGVHNe81E" width="452" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c664e2d3b22e8aa9a3b673052b2e01ce42c4f06_2_452x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c664e2d3b22e8aa9a3b673052b2e01ce42c4f06_2_678x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c664e2d3b22e8aa9a3b673052b2e01ce42c4f06_2_904x998.jpeg 2x" data-dominant-color="484F48"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axial top</span><span class="informations">1434×1585 301 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db195f8c6c0777e1c44a9d4f674c9f9b3321c8bd.jpeg" data-download-href="/uploads/short-url/vgeVwZhPrt2UkmAFgI3HyaHKyG9.jpeg?dl=1" title="axial 3d" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db195f8c6c0777e1c44a9d4f674c9f9b3321c8bd_2_596x500.jpeg" alt="axial 3d" data-base62-sha1="vgeVwZhPrt2UkmAFgI3HyaHKyG9" width="596" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db195f8c6c0777e1c44a9d4f674c9f9b3321c8bd_2_596x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db195f8c6c0777e1c44a9d4f674c9f9b3321c8bd_2_894x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db195f8c6c0777e1c44a9d4f674c9f9b3321c8bd_2_1192x1000.jpeg 2x" data-dominant-color="687F78"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axial 3d</span><span class="informations">1960×1644 411 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3abc2c9747e426b41ef733fa057555bdd5f65a.jpeg" data-download-href="/uploads/short-url/aSm7SiNsyl53KAD6Elv61dc9a0q.jpeg?dl=1" title="axial side" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3abc2c9747e426b41ef733fa057555bdd5f65a_2_528x500.jpeg" alt="axial side" data-base62-sha1="aSm7SiNsyl53KAD6Elv61dc9a0q" width="528" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3abc2c9747e426b41ef733fa057555bdd5f65a_2_528x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3abc2c9747e426b41ef733fa057555bdd5f65a_2_792x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3abc2c9747e426b41ef733fa057555bdd5f65a_2_1056x1000.jpeg 2x" data-dominant-color="687266"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axial side</span><span class="informations">2045×1934 376 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfa02b623805ac0e9eb37d18ff03a6ab0887b95d.jpeg" data-download-href="/uploads/short-url/vUhDwd0BE5LgMxELE21O7dCrkGV.jpeg?dl=1" title="axial 3d 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfa02b623805ac0e9eb37d18ff03a6ab0887b95d_2_582x500.jpeg" alt="axial 3d 2" data-base62-sha1="vUhDwd0BE5LgMxELE21O7dCrkGV" width="582" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfa02b623805ac0e9eb37d18ff03a6ab0887b95d_2_582x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfa02b623805ac0e9eb37d18ff03a6ab0887b95d_2_873x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfa02b623805ac0e9eb37d18ff03a6ab0887b95d_2_1164x1000.jpeg 2x" data-dominant-color="7C9592"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axial 3d 2</span><span class="informations">1389×1193 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I’m assuming I can work on the sagittal and coronal data in the same way and combine them to get an overall good result - but at what stage do I combine them and how?</p>
</li>
<li>
<p>Paint effect on sagittal<br>
I started to work on the segmentation of the sagittal volume, with the hope of later combining with the axial segmentation but despite the sagittal clearly being higher resolution from that angle as I work with the Paint tool on it, the result is super large ‘pixels’ to the scale of the voxels of the previous axial volume on that same sagittal plane:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89bcb69d21ace5d0d25e034de207430cc96e6bf8.jpeg" data-download-href="/uploads/short-url/jEtJfLmsstgQjVcv6ab1P9OaPtS.jpeg?dl=1" title="sagittal paint 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89bcb69d21ace5d0d25e034de207430cc96e6bf8_2_499x499.jpeg" alt="sagittal paint 2" data-base62-sha1="jEtJfLmsstgQjVcv6ab1P9OaPtS" width="499" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89bcb69d21ace5d0d25e034de207430cc96e6bf8_2_499x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89bcb69d21ace5d0d25e034de207430cc96e6bf8_2_748x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89bcb69d21ace5d0d25e034de207430cc96e6bf8_2_998x998.jpeg 2x" data-dominant-color="525B4B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sagittal paint 2</span><span class="informations">1781×1784 271 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ol>
<p>It feels like there should be a way to work on the segmentation of the combined volumes of all planes at the same time…?</p>
<p>Perhaps this is stupid obvious in which case apologies in adance! I have looked through a lot of videos and documentation but not found the answer.</p>
<p>Thanks for any help!!!</p>
<p>Best,<br>
Hannah</p>

---

## Post #2 by @pieper (2023-04-23 19:54 UTC)

<p>I’d suggest using <a href="https://github.com/BBillot/SynthSeg">SynthSeg</a>.  It’s not available directly in Slicer but you can load the results and use that to do any further edits and STL export.</p>

---
