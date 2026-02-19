---
topic_id: 10379
title: "Dislocation Of Some Sections In My 3D Model"
date: 2020-02-21
url: https://discourse.slicer.org/t/10379
---

# Dislocation of some sections in my 3D model

**Topic ID**: 10379
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/dislocation-of-some-sections-in-my-3d-model/10379

---

## Post #1 by @o.ozkan.oguz (2020-02-21 12:37 UTC)

<p>I am working on Visible Human Project dataset which is cryosection images of human body. I changed the format of BMP images to PNG format and translated the colours to gray scale. In the dataset there are a few dislocation of some sections/images. And this dislocations are effecting the 3D models, as expected. I want to know how can I perform the re-orientation of the sections after manually segmentation process? Or is there any way to perform the orientation step?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/466a5c08977cfe748fa94ae670fd7a56344c110a.jpeg" data-download-href="/uploads/short-url/a2Viq8z3lhIVVufF4kSLBqlVqLU.jpeg?dl=1" title="yıldızlı 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/466a5c08977cfe748fa94ae670fd7a56344c110a_2_652x500.jpeg" alt="yıldızlı 2" data-base62-sha1="a2Viq8z3lhIVVufF4kSLBqlVqLU" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/466a5c08977cfe748fa94ae670fd7a56344c110a_2_652x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/466a5c08977cfe748fa94ae670fd7a56344c110a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/466a5c08977cfe748fa94ae670fd7a56344c110a.jpeg 2x" data-dominant-color="837C7E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">yıldızlı 2</span><span class="informations">769×589 85.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ebf0d04a9ae210e2fa57c6a076e4a65604da7fc.jpeg" data-download-href="/uploads/short-url/dwacOSOQFm4n5fYYQx2nzDOisri.jpeg?dl=1" title="yıldızlı" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ebf0d04a9ae210e2fa57c6a076e4a65604da7fc_2_553x500.jpeg" alt="yıldızlı" data-base62-sha1="dwacOSOQFm4n5fYYQx2nzDOisri" width="553" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ebf0d04a9ae210e2fa57c6a076e4a65604da7fc_2_553x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ebf0d04a9ae210e2fa57c6a076e4a65604da7fc_2_829x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ebf0d04a9ae210e2fa57c6a076e4a65604da7fc.jpeg 2x" data-dominant-color="787475"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">yıldızlı</span><span class="informations">847×765 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Ozkan Oguz</p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @timeanddoctor (2020-02-21 12:52 UTC)

<p>yes, you can change the coordinate by the transform module.</p>

---

## Post #3 by @lassoan (2020-02-21 14:24 UTC)

<p>By today’s standards, quality of Visible Human Project data is quite poor. You may find better quality atlases now, such as <a href="https://www.openanatomy.org/atlas-pages/">OpenAnatomy</a> or <a href="https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html">BodyParts3D</a>.</p>
<p>You can still fix up and work with Visible Human Project data. If there are misaligned slices then you can run it through stack alignment tool in ImageJ/Fiji before loading it into Slicer. Since the data set is now available without registration and license agreement, you might find pre-processed, corrected versions on the internet (I haven’t checked).</p>

---

## Post #5 by @o.ozkan.oguz (2020-02-22 16:50 UTC)

<p>Thank you very much for your suggestion.<br>
Best wishes</p>
<p>iPhone’umdan gönderildi</p>

---

## Post #6 by @bhowmisp (2022-05-03 18:07 UTC)

<p>Hi, could you solve the problem? I am working with the VHP data and have the same issue.</p>

---

## Post #7 by @bhowmisp (2022-05-03 18:08 UTC)

<p>Hi, I am also working on the VHP images, could you kindly elaborate on the Stack alignment in FIJI, because the inbuilt plugins aren’t producing satisfactory result, is there any special tools to consider?</p>
<p>Thanks</p>

---

## Post #8 by @lassoan (2022-05-03 18:31 UTC)

<p>If you just want to have smooth segments then you can use <code>Smoothing</code> effect in Segment Editor with <code>Joint smoothing</code> method to make the surface more even. You can also use the smoothing brush to apply some additional smoothing locally.</p>
<p>However, in general there is no easy solution for these misalignment/distortion/smudging issues. Grinding layers off of a frozen cadaver has some inherent variance in it. Maybe somebody opened a door and the room temperature changed by a few degrees, so tissues smudged a bit differently for a couple of minutes. Or the angle of the specimen or grinder was off for a couple of slices and then it was readjusted. Some of the errors can be compensated for with some additional computational corrections - see for example <a href="https://www.voxel-man.com/">https://www.voxel-man.com/</a> and related papers. But maybe the VHP data set cannot fulfill your accuracy requirements and you need to look for other, higher-quality data.</p>

---
