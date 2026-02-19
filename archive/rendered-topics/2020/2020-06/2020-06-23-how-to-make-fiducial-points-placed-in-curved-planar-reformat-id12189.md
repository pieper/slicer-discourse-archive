---
topic_id: 12189
title: "How To Make Fiducial Points Placed In Curved Planar Reformat"
date: 2020-06-23
url: https://discourse.slicer.org/t/12189
---

# How to make fiducial points placed in Curved Planar Reformatted image appear in the original image

**Topic ID**: 12189
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/how-to-make-fiducial-points-placed-in-curved-planar-reformatted-image-appear-in-the-original-image/12189

---

## Post #1 by @Romeo_Guevara (2020-06-23 22:36 UTC)

<p>It is possible that the fudicials that are placed in the Curved Planar Reformat may appear in the segmentation? Because I must place them at specific points to be able to make measurements, for example: from the exact beginning of the lower edge of the ostium of the renal artery, to the iliac bifurcation.</p>
<p>thanks and happy afternoon<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8289cd6ce767ecdb8127e4733dd260bdd1446519.jpeg" data-download-href="/uploads/short-url/iCNjjwwz0T1K6Qp024FSJjVfLyF.jpeg?dl=1" title="Screenshot_20200621_151637_com.whatsapp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8289cd6ce767ecdb8127e4733dd260bdd1446519_2_690x332.jpeg" alt="Screenshot_20200621_151637_com.whatsapp" data-base62-sha1="iCNjjwwz0T1K6Qp024FSJjVfLyF" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8289cd6ce767ecdb8127e4733dd260bdd1446519_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8289cd6ce767ecdb8127e4733dd260bdd1446519_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8289cd6ce767ecdb8127e4733dd260bdd1446519_2_1380x664.jpeg 2x" data-dominant-color="272F2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20200621_151637_com.whatsapp</span><span class="informations">2244×1080 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-06-23 23:53 UTC)

<p>Would you like to place the point in the straightened image or in the original image?</p>

---

## Post #3 by @Romeo_Guevara (2020-06-24 00:06 UTC)

<p>If they can appear in both, it would be best</p>

---

## Post #4 by @lassoan (2020-06-25 21:53 UTC)

<p>I’ve implemented this, it’s available in latest Slicer Preview Release (I’ve pushed some more fixes today, so if inverse transform computation is not robust then wait for tomorrow’s release). The Curve Planar Reformat module provides a “straightening” transform, which transforms points from original image space to the straightened image. You can then add/delete/modify points in the straightened image space. To get these point positions in the original image space again, remove the straightening transform. See demo video here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="WJQexDTiRRc" data-video-title="Transform markups between original and straightened vessel" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=WJQexDTiRRc" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/WJQexDTiRRc/maxresdefault.jpg" title="Transform markups between original and straightened vessel" width="" height="">
  </a>
</div>


---

## Post #5 by @Romeo_Guevara (2020-06-26 21:31 UTC)

<p>Perfect, thank you very much, the new functions allow a fast and effective measurement, another suggestion would be to see if it is possible to make automatic diameter measurements through the centerline as shown in the attached image.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfa2f8e6f419c5513d41a65ad6e338a6db05803f.jpeg" data-download-href="/uploads/short-url/rlimwGIKuSgipk6C9GyjOktX7Mb.jpeg?dl=1" title="2020-06-26 (3)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfa2f8e6f419c5513d41a65ad6e338a6db05803f_2_690x419.jpeg" alt="2020-06-26 (3)" data-base62-sha1="rlimwGIKuSgipk6C9GyjOktX7Mb" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bfa2f8e6f419c5513d41a65ad6e338a6db05803f_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfa2f8e6f419c5513d41a65ad6e338a6db05803f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfa2f8e6f419c5513d41a65ad6e338a6db05803f.jpeg 2x" data-dominant-color="352E2D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-06-26 (3)</span><span class="informations">904×549 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2020-06-26 21:50 UTC)

<p>VMTK computes centerline radius, so we could display that. Why are there two diameters?</p>
<p>Could you describe your complete workflow (what is the overall goal, how do you segment, what inputs you provide, and what measurements you need). Probably the best would be to add a dedicated module that implements all the steps in a single place.</p>

---

## Post #7 by @Romeo_Guevara (2020-06-26 22:13 UTC)

<p>Fabulous, I will get to work on the workflow you request and I will send it to you as soon as possible, regarding the two measurements, the largest diameter is used to decide the size (diameter) of the stent that we will use, sometimes we use two or 3 measurements to average the diameter of the blood vessel</p>

---

## Post #8 by @Romeo_Guevara (2020-06-27 22:21 UTC)

<p>I send the workflow for the planning of the  endovascular aortic repair (EVAR). Infrarenal Segment  If<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c661bf35da3d6324402d384f09d3ee4641169aa4.png" data-download-href="/uploads/short-url/siXXzTahx7bs55hk3QL7AYey8Mk.png?dl=1" title="2020-06-27 (4)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c661bf35da3d6324402d384f09d3ee4641169aa4_2_690x384.png" alt="2020-06-27 (4)" data-base62-sha1="siXXzTahx7bs55hk3QL7AYey8Mk" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c661bf35da3d6324402d384f09d3ee4641169aa4_2_690x384.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c661bf35da3d6324402d384f09d3ee4641169aa4_2_1035x576.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c661bf35da3d6324402d384f09d3ee4641169aa4_2_1380x768.png 2x" data-dominant-color="ECE9E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-06-27 (4)</span><span class="informations">1390×775 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2020-06-28 04:21 UTC)

<p>Thank you, this is a very nice requirement specification. A simple module could be implemented with a couple of days of work for an experienced Slicer developer; or in a few weeks for a newcomer with some Python programming experience. I can help with advice and maybe some work, but things would go faster if you could find someone who could help with the development. Do you know someone (a student, staff engineer, …) who could volunteer for this? Or do you have budget to hire a Slicer developer (see a few potential companies <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#commercial-partners">here</a>)? You could team up and share the cost with a couple of other vascular surgery groups who would be interested in having a free, open-source, customizable EVAR planning tool.</p>
<p>You could also try to apply for some small internal research grant at your institution to get funding for this. The unique value proposition would not be that this tool is free but it would be more advanced, more customizable than existing commercial solutions (could support new techniques, devices, etc.).</p>

---

## Post #10 by @Romeo_Guevara (2020-06-30 17:09 UTC)

<p>Thanks engineer, I will start working on the project and recruiting other vascular surgeons, we will write to you soon.</p>

---
