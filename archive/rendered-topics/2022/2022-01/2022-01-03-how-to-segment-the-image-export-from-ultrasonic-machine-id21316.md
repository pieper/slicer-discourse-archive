---
topic_id: 21316
title: "How To Segment The Image Export From Ultrasonic Machine"
date: 2022-01-03
url: https://discourse.slicer.org/t/21316
---

# How to segment the image export from ultrasonic machine?

**Topic ID**: 21316
**Date**: 2022-01-03
**URL**: https://discourse.slicer.org/t/how-to-segment-the-image-export-from-ultrasonic-machine/21316

---

## Post #1 by @BARNEY (2022-01-03 09:07 UTC)

<p>Hello, guys!<br>
The thing is, we’re doing some work on 3D ultrasound navigation, and PerkLab videos on YouTube are very helpful, so thanks! We used the epiphan <a href="http://AV.io" rel="noopener nofollow ugc">AV.io</a> HD capture card  to export ultrasonic images, and the format is VEG to DVI. However, it seems that we were exporting the ultrasound screen image rather than the ultrasound image stream. During the calibration process, we found that the command for image segmentation did not work, perhaps because the exported image had lost the MF coordinate system information？<br>
Furthermore, the built-in calibration program of FCAL was very powerful, but we only had a magnetic tag, so we couldn’t complete the standard calibration program. Spatial registration we’ve built a program to do that, and I think even with a magnetic tag, time registration can be done with FCAL, right?<br>
I would be very happy if anyone could answer or comment on either of these two questions. Happy New Year to you all!</p>

---

## Post #2 by @lassoan (2022-01-03 20:20 UTC)

<p>If you only had a single sensor then the calibration would be much harder: you would need to determine two transforms PhantomToTracker and ImageToProbe matrices from a series of tracked images; and you could not move the phantom (which would make acquisition of high-quality images more difficult). I would recommend to get a second sensor.</p>

---

## Post #3 by @BARNEY (2022-01-05 01:56 UTC)

<p>Thank you! We’re thinking about buying an optical tracking system. Do you have any advice about the exported ultrasonic image segmentation?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6a69c41d553f18946b3c7ef5d584d1a21553717.png" data-download-href="/uploads/short-url/zbYpXX5A0cs3NIq7z5Re3u6KIPt.png?dl=1" title="WechatIMG2133" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6a69c41d553f18946b3c7ef5d584d1a21553717_2_690x407.png" alt="WechatIMG2133" data-base62-sha1="zbYpXX5A0cs3NIq7z5Re3u6KIPt" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6a69c41d553f18946b3c7ef5d584d1a21553717_2_690x407.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6a69c41d553f18946b3c7ef5d584d1a21553717.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6a69c41d553f18946b3c7ef5d584d1a21553717.png 2x" data-dominant-color="FDF4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WechatIMG2133</span><span class="informations">822×486 57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-01-05 05:35 UTC)

<p>If you use a standard fCal phantom and acquire good quality images then it should not be necessary to modify these parameters except <code>ClipRectangleOrigin</code> and <code>ClipRectangleSize</code> (that you can visually edit in the fCal application).</p>

---
