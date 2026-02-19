---
topic_id: 44745
title: "Help With Segmentation Of 3D Scans Of Wood"
date: 2025-10-13
url: https://discourse.slicer.org/t/44745
---

# Help with segmentation of 3D scans of wood

**Topic ID**: 44745
**Date**: 2025-10-13
**URL**: https://discourse.slicer.org/t/help-with-segmentation-of-3d-scans-of-wood/44745

---

## Post #1 by @franco_otaola (2025-10-13 14:23 UTC)

<p>Hello,</p>
<p>I just began using slicer 3D, it is quite powerfull tool!</p>
<p>I am not using it for medical application, but in material science.<br>
I have 3D scans from wood, that I would like to segment.</p>
<p>when the data has been imported it looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c12d0bba6c35d70beec4af374ba2901bc9f1a757.jpeg" data-download-href="/uploads/short-url/ryUF2KIuuHDmtZ6RCWpsUt5n9WL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c12d0bba6c35d70beec4af374ba2901bc9f1a757_2_690x300.jpeg" alt="image" data-base62-sha1="ryUF2KIuuHDmtZ6RCWpsUt5n9WL" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c12d0bba6c35d70beec4af374ba2901bc9f1a757_2_690x300.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c12d0bba6c35d70beec4af374ba2901bc9f1a757_2_1035x450.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c12d0bba6c35d70beec4af374ba2901bc9f1a757_2_1380x600.jpeg 2x" data-dominant-color="4F4F4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1386×604 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the data is for a small hexahedral section (cubish like) of the complete scan. using the threshold i was able to differentiate the three main volumes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b989a1d5795edbc64d12f52073d4932283369bd9.jpeg" data-download-href="/uploads/short-url/qtlcRWZL25rlJq5JscbZeenMFoR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b989a1d5795edbc64d12f52073d4932283369bd9.jpeg" alt="image" data-base62-sha1="qtlcRWZL25rlJq5JscbZeenMFoR" width="654" height="298"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">654×298 56.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>nevertheless, i have some issues with the results:</p>
<ol>
<li>in reality the 3 different regions, the black/red (frist picture/3D image) envelopes the grey/yellow one, and lastly the white/green comes. this images are the result from using threshold, but it can be seen that it is far from perfect:</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8355ddafc414351c87356bedf0b317a0673ce328.jpeg" data-download-href="/uploads/short-url/iJQvXZud4kEjFtK0w65RYvcVt0s.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8355ddafc414351c87356bedf0b317a0673ce328.jpeg" alt="image" data-base62-sha1="iJQvXZud4kEjFtK0w65RYvcVt0s" width="654" height="298"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">654×298 55.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but i dont know if this is possible to improve while using the threshold filter, I also tried painting and grow from seeds, option but did not gave good results (actually the best results i got where from threshold). any recommendations that someone could give me in this regards?</p>
<ol start="2">
<li>I would like to have the different regions that the common boundaries are shared, i mean, in the surfaces that the regions are touching each other that the surface is the same, is this possible?</li>
</ol>
<p>here is the <a href="https://filesender.renater.fr/?s=download&amp;token=7debf4bb-5d93-47fe-b0af-4db6c6ced398" rel="noopener nofollow ugc">data</a> if anyone wants to play with.</p>

---

## Post #2 by @pieper (2025-10-13 18:21 UTC)

<p>That looks quite promising.  You may have a classic case for the Median Image Filter module (implements <a href="https://en.wikipedia.org/wiki/Median_filter">this</a>), since you are trying to remove noise from within contiguous regions but want to maintain the sharp boundaries.  Also some of the small artifacts you see are due to the sampling.  Thresholding may still not completely separate the regions due to natural variations in the material,</p>
<p>I suggest you use Crop Volume to get a small region for testing, and you scale the spacing by .5 or even .25 and experiment with different median kernel sizes.  You can also specify a higher segmentation resolution.</p>
<p>Regarding the second question, if i understand correctly, you can write a small python script to do this using numpy to select the indices of segmentation voxels that have label A and neighbors of label B.  Then you can create a new segment from those locations.  You could just brute force iterate or probably there is a way to make this efficient using numpy indexing magic.</p>

---

## Post #3 by @franco_otaola (2025-10-14 11:27 UTC)

<p>thanks a lot for taking the time steve!</p>
<blockquote>
<p>That looks quite promising. You may have a classic case for the Median Image Filter module (implements <a href="https://en.wikipedia.org/wiki/Median_filter" rel="noopener nofollow ugc">this</a>), since you are trying to remove noise from within contiguous regions but want to maintain the sharp boundaries.</p>
</blockquote>
<p>so i should use median image filter on the data itself?</p>
<blockquote>
<p>Also some of the small artifacts you see are due to the sampling.</p>
</blockquote>
<p>should i re sample the data? i saw in one of the <a href="https://www.youtube.com/watch?v=BJoIexIvtGo" rel="noopener nofollow ugc">tutorial</a> that they use crop volume to divide differently the data but:<br>
a. the parameters on the tutorial 0:39 are quite different to the actual ones. (well it is 7 years old…)<br>
b. this only works in coarsing the data, not refining it</p>
<blockquote>
<p>I suggest you use Crop Volume to get a small region for testing, and you scale the spacing by .5 or even .25 and experiment with different median kernel sizes. You can also specify a higher segmentation resolution.</p>
</blockquote>
<p>well, this comes with the b. comment on the previous quote, how can a division in spacing can improve anything (if the original one is 1, the data even if i divide it in .5 or .25 it will be the same…) sorry i am trying to understand….</p>
<blockquote>
<p>Regarding the second question, if i understand correctly, you can write a small python script to do this using numpy to select the indices of segmentation voxels that have label A and neighbors of label B. Then you can create a new segment from those locations. You could just brute force iterate or probably there is a way to make this efficient using numpy indexing magic.</p>
</blockquote>
<p>what i am looking to have is 3 conformal meshes (ie., that share same nodes in the zones where they have contact between one another)</p>
<p>i see that at least the meshes that are generated using the threshold, looks like they are ‘rounded’, for example, the data is a hexagonal shape, but when one looks at the meshes generated they are rounded in the borders…</p>
<p>also, is there any place for more complete tutorials than <a href="https://training.slicer.org/" rel="noopener nofollow ugc">https://training.slicer.org/</a> ?</p>

---

## Post #4 by @pieper (2025-10-14 17:28 UTC)

<p>Yes, you should crop and upscale the resolution to get a section you can experiment with quickly and then do the median filter on the that data to make it easier to segment.  Effectively you want the pixels to be much smaller than the structures you are trying to extract.  For the median filter this will mean you will have more pixels within the homogeneous structures that are reddish brown in your images so you are less likely to have stray pixels leak through in the segmentation.</p>
<p>You will definitely need to experiment to find a good set of steps.  I looked at your data and there are also some finer features of internal structure and you’ll need to decide if those are a different material class (segment) or part of one of the others.  I don’t know of any tutorials specific to your case.</p>
<p>For the meshing you can look at the segment mesher extension and see if those will work for you.  Getting a good mesh depends a lot on your purpose so the available options may or may not work for your case.</p>

---

## Post #5 by @aiden.zhu (2025-10-17 12:55 UTC)

<p>Based on my experiences I did have a couple of years ago, <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">  it’s better to do such segmentations via machine-learning or deep-learning, while you are seeking perfect segments. Generally speaking, such segs of wood can’t be well done by just simple thresholding plus other smoothing-filters (of course, those methods works plus lots of time for manual correction if you just try to have “ok”-segmentation, totally based on your goal of satisfaction. )</p>
<p>Good luck there.</p>

---

## Post #6 by @franco_otaola (2025-10-17 13:13 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thanks a lot, right now i am testing same work in paraview (as i can do this quite fast and easy, as i am fully autonomous in it and all you suggested is faisable there also) but i will come back no worries! (i find quite difficult to understand the documentation even the one of python as there is a loooooot of acronims that i dont even finish of understanding how my data would classify )<br>
<a class="mention" href="/u/aiden.zhu">@aiden.zhu</a> thanks a lot for your input, i saw some AI segmentation tutorial but it looked super old (in the tutorial section) do you have any documentations to point on this regards? ideally in python?</p>
<p>thanks in advance to the two of you!</p>

---

## Post #7 by @pieper (2025-10-17 13:31 UTC)

<p>You may want to try nnInteractive to create some fully annotated ground truth with cropped subvolumes and then train nnU-Net.  Your data is clean and seems suitable for this approach.</p>

---

## Post #8 by @aiden.zhu (2025-10-24 12:40 UTC)

<p>sorry I can’t provide any python code from my side since all is part of the company’s asset <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Good to follow <a class="mention" href="/u/pieper">@pieper</a> ‘s suggest there, and as well as you may find a lot of useful stuff inside some webs, such as github.</p>

---
