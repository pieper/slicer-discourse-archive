---
topic_id: 33279
title: "Grow From Seeds Error Minimum 2 Visible Segments Required"
date: 2023-12-07
url: https://discourse.slicer.org/t/33279
---

# Grow from seeds error - minimum 2 visible segments required

**Topic ID**: 33279
**Date**: 2023-12-07
**URL**: https://discourse.slicer.org/t/grow-from-seeds-error-minimum-2-visible-segments-required/33279

---

## Post #1 by @JamesM (2023-12-07 06:18 UTC)

<p>Hello! I am measuring tumor volume, segmenting the inside and background separately and using the “grow from seed” function. However, when I try to use “grow from seed” again after filling in the completed volume where there were gaps, I encounter the following error. I would appreciate advice on how to resolve this issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd2b60ea333046e29242ceb95cdb4b936428785b.jpeg" data-download-href="/uploads/short-url/A7DJLB5MX7Hrs8evMt2pigSWTAT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd2b60ea333046e29242ceb95cdb4b936428785b_2_690x419.jpeg" alt="image" data-base62-sha1="A7DJLB5MX7Hrs8evMt2pigSWTAT" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd2b60ea333046e29242ceb95cdb4b936428785b_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd2b60ea333046e29242ceb95cdb4b936428785b_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd2b60ea333046e29242ceb95cdb4b936428785b.jpeg 2x" data-dominant-color="8A8B8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1312×798 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-12-07 14:39 UTC)

<p>I cannot reproduce the issue. Please share a screen capture video or describe every click you make.</p>

---

## Post #3 by @JamesM (2023-12-08 07:51 UTC)

<p>I uploaded my capture video.<br>
this video is little bit different situation.<br>
but still same error message with the grow from seed function.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56f31986deb5991e0a8d2c3c887111bfc0421a56.mp4">
  </div><p></p>

---

## Post #4 by @lassoan (2023-12-08 12:57 UTC)

<p>Thanks for the video. It nicely shows how the error occurs in the end, but I still cannot reproduce this if I perform these steps starting from a segmentation that I create. You might have performed some extra steps that triggered this issue.</p>
<p>Could you please upload a video that shows all the steps, starting with launching Slicer, loading a sample data set, … ending with the error displayed?</p>

---

## Post #5 by @JamesM (2023-12-10 04:30 UTC)

<p>When I started recording again from the beginning, the issue did not occur again.</p>
<p>Thanks…</p>

---

## Post #6 by @D_Dand (2024-02-06 16:15 UTC)

<p>I do have same issue with you. How did you fix it?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f516536ba2e70fa4be9218f71e8deffe7e2444.jpeg" data-download-href="/uploads/short-url/qfmto7VYWUIVndbZlfW8CBAWp6s.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7f516536ba2e70fa4be9218f71e8deffe7e2444_2_689x368.jpeg" alt="image" data-base62-sha1="qfmto7VYWUIVndbZlfW8CBAWp6s" width="689" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7f516536ba2e70fa4be9218f71e8deffe7e2444_2_689x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7f516536ba2e70fa4be9218f71e8deffe7e2444_2_1033x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f516536ba2e70fa4be9218f71e8deffe7e2444.jpeg 2x" data-dominant-color="ACA9A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1240×662 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2024-02-06 18:53 UTC)

<p>Please try to reproduce it with the latest Slicer Preview Release. If you can reproduce the problem then please provide step-by-step instructions that we can follow.</p>
<p>If we can reproduce the issue then we can immediately fix it, but without sufficiently detailed instructions we cannot even investigate the problem.</p>

---

## Post #8 by @Redamancy_Duan (2024-03-26 06:47 UTC)

<p>根据提示，我找到一个解决方法是用Threshold工具规定一个灰度范围</p>

---

## Post #9 by @jwal (2024-09-23 21:58 UTC)

<p>I believe I’m experiencing a similar error attempting to segment a CT. Please see attached video and image.<br>
Thank You.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/020eab51630099eb5ca1ebaa875665198d5384d8.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c1eadd6687be6804f68ea77a749a6bc06e6acd2.png">
  </div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75020ae614d9c8cbf5000e2723dec798c800014c.jpeg" alt="Seg Op Failed - slicer error" data-base62-sha1="gH6eTsRzMUyWH2pJ0kkNR2u9hko" width="555" height="218"><p></p>

---

## Post #10 by @cpinter (2024-09-24 08:54 UTC)

<p>This is really strange, as far as I see everything is in order. Can you reproduce it with a sample data, such as CT Chest in the Sample Data module?</p>

---

## Post #11 by @jwal (2024-09-24 11:49 UTC)

<p>Unfortunately, Yes.  I did reproduce it in the CT Chest Sample Data.  Hmmmm.</p>

---

## Post #12 by @lassoan (2024-09-24 12:31 UTC)

<p>Is it fixed in the latest Slicer Preview Release?</p>

---

## Post #13 by @cpinter (2024-09-24 13:48 UTC)

<p>Grow from seeds works for me with 2 segments and little seeding on CT Chest in a nightly from July. Could this error be due to some peculiarity in how you add the seeds?</p>
<p>It would be very useful to try this in the latest preview as <a class="mention" href="/u/lassoan">@lassoan</a> suggests.</p>

---

## Post #14 by @lassoan (2024-09-24 13:58 UTC)

<p>Please also try if you do this after a fresh restart of Slicer. It may be possible that a previously cancelled segment editing causes this (e.g., you started some segmentation, then closed the scene). So, please test again, with the latest Slicer Preview Release and after a Slicer restart.</p>
<p>I’ve also noticed that it took considerable time to locate the tumor on all 3 slices. You can do this automatically by holding down the Shift key while moving the mouse in a view (no need to click just move the mouse). This makes all slice views jump to the mouse pointer location.</p>

---

## Post #15 by @jwal (2024-09-25 17:15 UTC)

<p>Ohhhh, I love that Shift key trick!  I have a lot to learn here.  So 5.7.0 version successfully segmented the tumor.  Now Im stuck not being able to edit the segmented tumor in 3D as Id like.  See video.<br>
Thanks for your help.<br>
Jim<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57033634744f63298f2cf945a3367de644e3715f.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce1ce91f37bb76dfce9f87583ea66844fb0ad1f4.jpeg">
  </div><p></p>

---

## Post #16 by @lassoan (2024-09-25 20:01 UTC)

<p>While “Grow from seeds” effect is active, you are editing the seeds that are automatically grown. Therefore, once you like the previewed segmentation results, switch to “Grow from seeds” effect and click <code>Apply</code>.</p>

---

## Post #17 by @Ninjaa (2025-02-09 01:55 UTC)

<p>Running into same issue on Slicer 5.8.0.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c6476a869b7d8b6ef698d506d86859a847646bb.jpeg" data-download-href="/uploads/short-url/1LCYfhnyWmVf9y4VA3TL50NenoL.jpeg?dl=1" title="Screenshot from 2025-02-08 17-54-09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c6476a869b7d8b6ef698d506d86859a847646bb_2_690x343.jpeg" alt="Screenshot from 2025-02-08 17-54-09" data-base62-sha1="1LCYfhnyWmVf9y4VA3TL50NenoL" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c6476a869b7d8b6ef698d506d86859a847646bb_2_690x343.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c6476a869b7d8b6ef698d506d86859a847646bb_2_1035x514.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c6476a869b7d8b6ef698d506d86859a847646bb_2_1380x686.jpeg 2x" data-dominant-color="444346"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-02-08 17-54-09</span><span class="informations">1920×955 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>. Tried restarting 3D Slicer as recommended above but still encountering, is there anything obvious I am messing up? Thank you.</p>

---

## Post #18 by @Ninjaa (2025-02-09 18:39 UTC)

<p>Tried flow in 5.9.0 preview build 2025-02-08 as well yielding the same error. Painting more of the segments doesn’t seem to make a difference. <a class="mention" href="/u/lassoan">@lassoan</a> any noticable setup issue from my screenshot above? Would appreciate any input.</p>

---

## Post #19 by @lassoan (2025-02-09 23:10 UTC)

<p>I dont see any obvious issues. Can you share the scene (upload somewhere and post the link here)?</p>

---

## Post #20 by @Ninjaa (2025-02-13 08:35 UTC)

<p>Was not able to reproduce again (still on version 2025-02-08) even though had the occurrence on both stable and preview couple days ago across restarts, whatever I must have subtly done different in steps today led to initialization working great.</p>
<p>Will share scene + sequence of steps I did if I manage to trigger issue again.</p>

---

## Post #21 by @bilbro (2025-08-05 17:53 UTC)

<p>Getting same error message in 5.8.1. any fixes?</p>

---

## Post #22 by @cpinter (2025-08-06 14:42 UTC)

<p>I think the fix is to have at least two visible segments with seeds painted. Or are you experiencing a bug we are not aware of? In that case please elaborate. Thanks!</p>

---

## Post #23 by @Dien-Yu_Tsai (2025-11-19 04:23 UTC)

<p>Having the exact same error in slicer 5.10.0 version here. Is there any general suggestions on troubleshooting? Thanks!</p>

---
