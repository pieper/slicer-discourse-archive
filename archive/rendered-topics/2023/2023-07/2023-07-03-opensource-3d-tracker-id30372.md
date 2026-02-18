# Opensource 3D Tracker

**Topic ID**: 30372
**Date**: 2023-07-03
**URL**: https://discourse.slicer.org/t/opensource-3d-tracker/30372

---

## Post #1 by @Agung_Alfiansyah1 (2023-07-03 15:40 UTC)

<p>Dear all,<br>
Sorry I’m new to this forum and a bit unsure of the question I’m going to ask. But well, I still dare to ask it. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>If I have a stereo pair of cameras (quite good), is there any open source libraries that would allow me to build my own 3D tracker?</p>
<p>It would be ideal if the tracker is also compatible with the IGT Slicer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks for all the help.</p>

---

## Post #2 by @lassoan (2023-07-03 15:59 UTC)

<p>Probably it only makes sense to make your own tracker if your main interest is designing and building tracking systems yourself. If you just want to have a tracker then it is much simpler and less expensive to buy a tracker.</p>
<p>Cameras is a very small part of a tracking system. You need to have a lot of additional hardware (a solid frame that can hold the cameras in place, with strong mounting point(s), built-in ring lighting, memory to store calibration data, power supply, communication interface to the computer, etc. all in a compact enclosure) and software (for calibration, marker tracking, 3D pose computation with filtering, automatic camera control, interfacing with drivers and operating system). While you can use off-the-shelf components and open-source libraries (e.g., calibrate cameras using OpenCV, detect/track markers using ArUco), you need to still spend a lot on buying all the hardware pieces and develop and maintain the software.</p>
<p>You can get accurate, convenient, integrated, factory-calibrated optical trackers with built-in infrared lighting and tracking software at very affordable price. For example, an <a href="https://www.optitrack.com/cameras/v120-duo/">OptiTrack Duo</a> costs just $3000.</p>

---

## Post #3 by @Agung_Alfiansyah1 (2023-07-14 06:31 UTC)

<p>Hi Andras,<br>
Thank you for your reply. Your suggestion to take a commercial tracker with wwoer cost makes a lot of sense for me.</p>
<p>One more question if you don’t mind, how about Optitrack Duo, is it compatble also with Slicer IGSTK ?</p>
<p>Thanks \</p>

---

## Post #4 by @lassoan (2023-07-14 16:02 UTC)

<p>Yes, Optitrack Duo is supported by Plus/SlicerIGT.</p>

---

## Post #5 by @Agung_Alfiansyah1 (2023-07-15 00:38 UTC)

<p>Sorry, I made a typo. I wanted to ask about Optotrack Trio actually. Is it also supported?</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2023-07-15 01:18 UTC)

<p>Yes, the Optitrack Trio is supported as well.</p>

---

## Post #7 by @slicer365 (2023-07-15 02:50 UTC)

<p>What about  Flex 3, is IGT supported?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fef09274f6a3a6c8460f12972cc8251acd38b20.png" data-download-href="/uploads/short-url/6Q2zw3LcdGyfB9MAS0xKz825e0M.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fef09274f6a3a6c8460f12972cc8251acd38b20_2_517x181.png" alt="image" data-base62-sha1="6Q2zw3LcdGyfB9MAS0xKz825e0M" width="517" height="181" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fef09274f6a3a6c8460f12972cc8251acd38b20_2_517x181.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fef09274f6a3a6c8460f12972cc8251acd38b20_2_775x271.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fef09274f6a3a6c8460f12972cc8251acd38b20.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">896×315 39.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2023-07-15 03:08 UTC)

<p>All Motive2 compatible trackers are supported.</p>
<p>Note that setting up a system of multiple cameras is more complicated and more expensive than getting a Duo. You need to buy a calibration tool, power supply, networking equipment, buy license, etc. With the Duo the setup is really easy, you just plug it in, and it works (it is recalibrated and perpetual license key is a included).</p>

---
