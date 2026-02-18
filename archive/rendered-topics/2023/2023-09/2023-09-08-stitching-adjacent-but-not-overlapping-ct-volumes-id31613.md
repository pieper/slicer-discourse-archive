# Stitching adjacent but not overlapping CT volumes

**Topic ID**: 31613
**Date**: 2023-09-08
**URL**: https://discourse.slicer.org/t/stitching-adjacent-but-not-overlapping-ct-volumes/31613

---

## Post #1 by @phiro753 (2023-09-08 01:03 UTC)

<p>Operating system: Windows 10 Pro<br>
Slicer version: 5.2</p>
<p>Hi Slicer3D community,</p>
<p>I am pursing a PhD looking into histology to radiology registration process for sarcomas. Enough to say there are multiple considerations that go into this…</p>
<p>This post is about a roadblock. How could we stitch two CT volumes of a femur - focus on reconstructing whole femur back together…<br>
1 - I started with surface registration to get a good transform of bringing the halves together<br>
2 - I am struggling on how to fuse volumes without overwriting bone… I don’t care if we overwrite soft tissue or background signal…</p>
<p>Image attached<br>
1 - Visualising two halves overlaid (but not fused…).png shows bone halves next to each other as we want them…<br>
2 - Fused volumes.png shows overwriting so part of the bone information is gone…</p>
<p>Is there any way of combining volumes to keep all bone signal, while ignoring other parts of the volumes? Potentially using the bone segmentations to tell Slicer what is bone signal and what is not…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5f31c78c6ce463424b392a565f8b9a286b0feb1.png" data-download-href="/uploads/short-url/uwGz0h5dsvkzZy6Q2vqZ693LaJb.png?dl=1" title="Visualising two halves overlaid (but not fused...)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5f31c78c6ce463424b392a565f8b9a286b0feb1_2_664x500.png" alt="Visualising two halves overlaid (but not fused...)" data-base62-sha1="uwGz0h5dsvkzZy6Q2vqZ693LaJb" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5f31c78c6ce463424b392a565f8b9a286b0feb1_2_664x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5f31c78c6ce463424b392a565f8b9a286b0feb1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5f31c78c6ce463424b392a565f8b9a286b0feb1.png 2x" data-dominant-color="797979"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Visualising two halves overlaid (but not fused...)</span><span class="informations">992×746 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e30c94fa7ef180a820c2c345cafed6b8000a4681.png" data-download-href="/uploads/short-url/wozlewRLBrfuX0qFvJwtBSoz3Fv.png?dl=1" title="Fused volumes" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e30c94fa7ef180a820c2c345cafed6b8000a4681_2_664x500.png" alt="Fused volumes" data-base62-sha1="wozlewRLBrfuX0qFvJwtBSoz3Fv" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e30c94fa7ef180a820c2c345cafed6b8000a4681_2_664x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e30c94fa7ef180a820c2c345cafed6b8000a4681.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e30c94fa7ef180a820c2c345cafed6b8000a4681.png 2x" data-dominant-color="939393"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fused volumes</span><span class="informations">992×746 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-09-08 03:28 UTC)

<p>You can stitch multiple volumes into one using <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">Stitch Volumes</a> module in Sandbox extension.</p>

---

## Post #3 by @phiro753 (2023-09-08 04:09 UTC)

<p>Hi Andras,  thanks for replying so promptly.</p>
<p>Stitch Volumes was used for computing the FusedHalfVols volume attached and previous. (Unfortunately I am not able to crop volumes as this impacts the organic femoral shape as seen on the green slide in the attached image…)</p>
<p>Attached - two planes of the volume created using Stitch Volumes module in Sandbox.</p>
<p>Question;<br>
Is there a way to tell Slicer which is the important information that must not be overwritten when using Stitch Volumes?</p>
<p>More details. We have a;<br>
1 - lateral half CT volume<br>
2 - medial half CT volume<br>
3 - whole CT volume<br>
Surface Registration of the half CT volume together is neat and tidy - if we can get a fused volume I’m hoping this will register nicely to the whole CT volume.<br>
…I have also dabbled at inverting the problem and surface register each half to the whole volume, however this is less robust/reliable…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb7b83b2dfc7a9001b99b2643038b1261c6dda9d.jpeg" data-download-href="/uploads/short-url/zSItmonpejQRzJr30SxefuriJEp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb7b83b2dfc7a9001b99b2643038b1261c6dda9d_2_496x500.jpeg" alt="image" data-base62-sha1="zSItmonpejQRzJr30SxefuriJEp" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb7b83b2dfc7a9001b99b2643038b1261c6dda9d_2_496x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb7b83b2dfc7a9001b99b2643038b1261c6dda9d_2_744x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb7b83b2dfc7a9001b99b2643038b1261c6dda9d.jpeg 2x" data-dominant-color="787874"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">770×775 79.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2023-09-08 04:28 UTC)

<p>Stitch Volumes module could be improved to have an option to support masking: prevent voxel values below a certain threshold from overwriting the other volume.</p>
<p><a class="mention" href="/u/mikebind">@mikebind</a> would you have time to implement this or help <a class="mention" href="/u/phiro753">@phiro753</a> to do it?</p>

---

## Post #5 by @mikebind (2023-09-08 19:38 UTC)

<p>Yes, I’m willing to take a look at this and try to implement this feature if it makes sense.  I’m a little confused about the nature of the data.  I’m not sure why there are image voxels which don’t seem to have image data in them (that’s where the gaps are coming from, if I understand correctly).</p>

---

## Post #6 by @phiro753 (2023-09-08 21:53 UTC)

<p>Hi Mike,</p>
<p>The image voxels which appear to have no data will be of air in the scan Field Of View. The should have really low HU values.</p>
<p>Attached is a representative value of the air in most scan FOVs<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71a9aa1ff08ccb25b42dbee481ebf6047179d293.png" data-download-href="/uploads/short-url/gdvsryGcKxyVaPxrpTCKECtW1dF.png?dl=1" title="Screenshot 2023-09-09 094317" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71a9aa1ff08ccb25b42dbee481ebf6047179d293_2_690x194.png" alt="Screenshot 2023-09-09 094317" data-base62-sha1="gdvsryGcKxyVaPxrpTCKECtW1dF" width="690" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71a9aa1ff08ccb25b42dbee481ebf6047179d293_2_690x194.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71a9aa1ff08ccb25b42dbee481ebf6047179d293_2_1035x291.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71a9aa1ff08ccb25b42dbee481ebf6047179d293.png 2x" data-dominant-color="66656A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-09 094317</span><span class="informations">1360×383 69.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Would it be possible to ignore HU values below XX  (user specified) during the stitching operation? This could allow preservation of certain voxels from both volumes in the stitching overlap area, rather than one volume entirely overwriting voxels of the other…</p>
<p>Disclaimer; the title of this tread is slightly misleading as there is some volume stitching overlap in the data I am working with (and future data I anticipate to process with the developed pipeline)…</p>

---

## Post #7 by @phiro753 (2023-09-27 04:37 UTC)

<p>I do apologise for that last image sorry Mike. Looking back on it I didn’t make the problem very clear…</p>
<p>Essentially my difficulty is that I would like to stitch the two volumes and retain high HU values in both but currently <strong>all</strong> of one volume has to overwrite the other one. e.g. If I set example <em>image F</em> as Original Volume 1 and <em>image B</em> as Original Volume 2 in the module Original Volume 2 value of -977 (just air) will override the 1144 in the other volume. If I flip the Original volumes in the module around, I have the overwrite issue somewhere else…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6537cc24c13ab42f1618473a15fe456cd515aef9.jpeg" data-download-href="/uploads/short-url/erpLJLtILs8Si7JQgKXyNF1bNTb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6537cc24c13ab42f1618473a15fe456cd515aef9_2_520x499.jpeg" alt="image" data-base62-sha1="erpLJLtILs8Si7JQgKXyNF1bNTb" width="520" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6537cc24c13ab42f1618473a15fe456cd515aef9_2_520x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6537cc24c13ab42f1618473a15fe456cd515aef9_2_780x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6537cc24c13ab42f1618473a15fe456cd515aef9.jpeg 2x" data-dominant-color="9A9C98"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">903×868 98.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @phiro753 (2024-12-01 21:28 UTC)

<p>For anyone reading this thread - the Stitch Volumes module in future slicer releases (after 5.6.2) has functionality to specify how to perform volume stitching - solving the issue discussed in this thread. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
