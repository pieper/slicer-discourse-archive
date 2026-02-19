---
topic_id: 15631
title: "Imported Dicom Image Appears Blurred In 2 Out Of 3 Slice Vie"
date: 2021-01-22
url: https://discourse.slicer.org/t/15631
---

# Imported DICOM image appears blurred in 2 out of 3 slice views

**Topic ID**: 15631
**Date**: 2021-01-22
**URL**: https://discourse.slicer.org/t/imported-dicom-image-appears-blurred-in-2-out-of-3-slice-views/15631

---

## Post #1 by @Marjorie (2021-01-22 14:55 UTC)

<p>Operating system: MAC OS<br>
Slicer version: Slicer 4.11.20200930 r29402 / 002be18<br>
Expected behavior: read a dicom in the windows (axial, coronal, sagittal)<br>
Actual behavior: it doesn’t work, even if my dicom is correct.</p>
<p>Is it a bug on mac or do i do something wrong ?<br>
I try the same dicom on slicer on windows and it works well.<br>
I try others dicom on mac and I have the same dysfunction.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc6b30b8779925b6fd9cb7fb5d78b1ba31aa28ae.jpeg" data-download-href="/uploads/short-url/tan3BzAeMTH3Wmioau0jPXTNLps.jpeg?dl=1" title="Capture d’écran 2021-01-22 à 15.50.24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc6b30b8779925b6fd9cb7fb5d78b1ba31aa28ae_2_690x420.jpeg" alt="Capture d’écran 2021-01-22 à 15.50.24" data-base62-sha1="tan3BzAeMTH3Wmioau0jPXTNLps" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc6b30b8779925b6fd9cb7fb5d78b1ba31aa28ae_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc6b30b8779925b6fd9cb7fb5d78b1ba31aa28ae_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc6b30b8779925b6fd9cb7fb5d78b1ba31aa28ae_2_1380x840.jpeg 2x" data-dominant-color="84848A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2021-01-22 à 15.50.24</span><span class="informations">1970×1200 322 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83d6446636b35c6dc8a0bbde30ac350d0ddfc5c1.jpeg" data-download-href="/uploads/short-url/iOhC42BVc0D0FHuIuHAYNIlO4St.jpeg?dl=1" title="Capture d’écran 2021-01-22 à 15.54.16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83d6446636b35c6dc8a0bbde30ac350d0ddfc5c1_2_690x423.jpeg" alt="Capture d’écran 2021-01-22 à 15.54.16" data-base62-sha1="iOhC42BVc0D0FHuIuHAYNIlO4St" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83d6446636b35c6dc8a0bbde30ac350d0ddfc5c1_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83d6446636b35c6dc8a0bbde30ac350d0ddfc5c1_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/83d6446636b35c6dc8a0bbde30ac350d0ddfc5c1_2_1380x846.jpeg 2x" data-dominant-color="8A8A8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2021-01-22 à 15.54.16</span><span class="informations">1957×1200 432 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-01-22 15:14 UTC)

<p>The screenshots show very sparse volumes (e.g., 3 slices very far from each other). For volumes that do not appear as you expect, could you go to Volumes module and take a screenshot of the “Volume information” section?</p>
<p>Did you get any warning while loading the volumes into the scene?</p>
<p>An imaging study often contains various reconstructions for various purposes. In general, you can ignore those that are not useful for you. However, if you expect to find complete volumes and instead you find incomplete/sparse volumes then check if your data set is complete (you have all the image slices). Unfortunately, most commonly used DICOM file formats contain each image slice in a separate file and there is no way to tell if a file is missing because it was not acquired or it was just lost while you were copying files.</p>

---

## Post #3 by @Marjorie (2021-01-25 16:11 UTC)

<p>Thank you for your answer.<br>
Here is the requested screenshot.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd71a196991770bed6ae1ecc986da3b91f85e0cf.jpeg" data-download-href="/uploads/short-url/r1TH84aFTBwsGuVJwrWnhkDOBgX.jpeg?dl=1" title="Capture d’écran 2021-01-25 à 17.00.34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd71a196991770bed6ae1ecc986da3b91f85e0cf_2_690x377.jpeg" alt="Capture d’écran 2021-01-25 à 17.00.34" data-base62-sha1="r1TH84aFTBwsGuVJwrWnhkDOBgX" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd71a196991770bed6ae1ecc986da3b91f85e0cf_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd71a196991770bed6ae1ecc986da3b91f85e0cf_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd71a196991770bed6ae1ecc986da3b91f85e0cf_2_1380x754.jpeg 2x" data-dominant-color="8C8B92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2021-01-25 à 17.00.34</span><span class="informations">1915×1047 290 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I don’t get any warning while the loading of the dicom.</p>
<p>And as i said, the same dicom on windows works, that’s why I think that the dicom is not the issue. I was able to do it a few months ago on mac with still the same dicom and now it’s impossible.<br>
And I tried with other dicoms, and it’s the same problem.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/603503782248f1a8f441b2e7f75c0038e09bfbc1.jpeg" data-download-href="/uploads/short-url/dJ5pVsBdeSN9cnM2rrLZ0DqhJq9.jpeg?dl=1" title="Capture d’écran 2021-01-25 à 17.06.53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/603503782248f1a8f441b2e7f75c0038e09bfbc1_2_690x379.jpeg" alt="Capture d’écran 2021-01-25 à 17.06.53" data-base62-sha1="dJ5pVsBdeSN9cnM2rrLZ0DqhJq9" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/603503782248f1a8f441b2e7f75c0038e09bfbc1_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/603503782248f1a8f441b2e7f75c0038e09bfbc1_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/603503782248f1a8f441b2e7f75c0038e09bfbc1_2_1380x758.jpeg 2x" data-dominant-color="929198"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2021-01-25 à 17.06.53</span><span class="informations">1918×1055 313 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-01-25 16:36 UTC)

<p>Could you choose that “Active Volume” to be the same as the volume selected in the slice view and post that screenshot?<br>
(currently, Active volume is “3: …” and the displayed volume in the slice view is "4: …)</p>

---

## Post #5 by @Marjorie (2021-01-27 14:24 UTC)

<p>I’m sorry you’re right ^^</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eb175635d217bc9658624dfef40302e60f77d27.jpeg" data-download-href="/uploads/short-url/8WBNZCjejqkG6sIngua1KzEgnBR.jpeg?dl=1" title="Capture d’écran 2021-01-27 à 15.23.42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3eb175635d217bc9658624dfef40302e60f77d27_2_690x422.jpeg" alt="Capture d’écran 2021-01-27 à 15.23.42" data-base62-sha1="8WBNZCjejqkG6sIngua1KzEgnBR" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3eb175635d217bc9658624dfef40302e60f77d27_2_690x422.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3eb175635d217bc9658624dfef40302e60f77d27_2_1035x633.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3eb175635d217bc9658624dfef40302e60f77d27_2_1380x844.jpeg 2x" data-dominant-color="87878E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2021-01-27 à 15.23.42</span><span class="informations">1917×1173 323 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2021-01-27 14:57 UTC)

<p>This looks perfect then. This volume consists of two axial frames, far from each other, so that’s why it has so low resolution in the two non-axial views.</p>
<p>If you expect more frames in this series than just two then check your DICOM files. You might have lost or corrupted some files when you copied them over between different computers.</p>

---

## Post #7 by @Marjorie (2021-01-27 15:27 UTC)

<p>Thank you !!<br>
I deleted all the corrupted dicoms, tried to recover my original dicom, and you are right !!<br>
I feel like a fool, but I’m really glad you fixed this problem.<br>
To learn from my mistakes, can you explain to me where do you find the gap between the frames? Is the “image spacing” that must be 0?<br>
I’m still not very familiar with the 3D slicer, I’m trying to learn little by little, but I’m far from using it well.<br>
Thank you very much for your responsive responses, whenever I find this extremely helpful!<br>
Happy that you are there.</p>

---

## Post #8 by @lassoan (2021-01-27 16:46 UTC)

<p>Most commonly used DICOM file format is still the one file per image slice. In this format, each DICOM file contains position and orientation of the image slice and there is no way to tell if there is a larger gap between certain slices because the image was acquired with varying spacing (e.g., to reduce dose) or a slice was acquired but lost along the way.</p>
<aside class="quote no-group" data-username="Marjorie" data-post="7" data-topic="15631">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marjorie/48/5233_2.png" class="avatar"> Marjorie:</div>
<blockquote>
<p>Is the “image spacing” that must be 0?</p>
</blockquote>
</aside>
<p>DICOM does not use image spacing to define acquisition geometry, as the spacing between slices may not be uniform and slices may not be even parallel.</p>
<p>Enhanced DICOM information objects solve most of these issues, but they are still very rarely used (although the standard was defined more than a decade ago).</p>

---

## Post #9 by @Marjorie (2021-01-28 09:02 UTC)

<p>All right, I understand a little better.<br>
Thank you very much <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
