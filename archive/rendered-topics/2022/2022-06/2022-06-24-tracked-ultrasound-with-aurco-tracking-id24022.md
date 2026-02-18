# Tracked Ultrasound with Aurco tracking

**Topic ID**: 24022
**Date**: 2022-06-24
**URL**: https://discourse.slicer.org/t/tracked-ultrasound-with-aurco-tracking/24022

---

## Post #1 by @J.vd.Zee (2022-06-24 10:32 UTC)

<p>Hi all!</p>
<p>I would like to create a set-up in which I use a tracked-US system for intraoperative navigation using the open-source Aruco tracking software from OpenCV. Therefore, I connected my US system via an Epiphan framegrabber and OpenIGTLink to Slicer. Now I am working on building the tracking set-up. As I will use the system for intraoperative guidance, high accuracy is acquired.</p>
<p>Therefore, I created a file with two cameras as input (1. Epiphan 2. Webcam). However, the FCal software is not able to work with this set-up as created. Moreover, I am doubtful about the accuracy of the Aruco tracking. Especially, the in-plane movements such as translating towards/away the camera. Anyone who could give me advice about which camera (Intel realsense devices, LogiTech webcams) to use for minimizing error rates? Or, is there no alternative of buying an optical tracker such as the Optitrack Duo?</p>
<p>Could anyone help me with tips or advice what to do?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2022-06-24 12:50 UTC)

<aside class="quote no-group" data-username="J.vd.Zee" data-post="1" data-topic="24022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/j.vd.zee/48/15064_2.png" class="avatar"> J.vd.Zee:</div>
<blockquote>
<p>Now I am working on building the tracking set-up. As I will use the system for intraoperative guidance, high accuracy is acquired.</p>
</blockquote>
</aside>
<p>If you need high 3D tracking accuracy then you must use something better than a single-camera tracking using Aruco markers. Aruco is used good for setting up demos for people who don’t want investing any money into buying a tracker. Aruco is also fine for many augmented reality applications, because tracking error in the image plane is small. However, out-of-plane translation and rotation measurement is very inaccurate, so you won’t be able to get accurate 3D tracking out of it (you can have several centimeters error in 3D).</p>
<p>An Optitrack Duo has magnitudes smaller error and costs just $3000, so maybe it doubles the cost of your hardware setup, but does not make it a different magnitude. In theory, by optimizing Aruco markers, combining it with a RealSense or other 3D vision systems, etc. you might get acceptable accuracy, but this may take years of R&amp;D work.</p>
<p>If the main goal of your project is not to develop a lower-cost position tracker then probably you are better off buying a tracker that is already accurate enough.</p>

---

## Post #3 by @J.vd.Zee (2022-06-24 13:12 UTC)

<p>Thanks again for your prompt reply!</p>
<p>I forgot to mention our clinical case. We would like to image the tibia intraoperatively with tracked-US. We will move the probe mostly in the lateral direction by setting-up the camera perpendicular to the tibia.</p>
<p>In summary, the major limitation of the Aruco tracking is the out-of-plane translation and rotation. Could these limitations be overcome with the newest RealSense depth cameras with larger accuracy and the use of five Aruco markers in a 3D configuration as suggested by Ošˇcádal et al. (2020). They showed an increased out-of-plane translation accuracy by updating the middle QR-code with the tracking information of the surrounded ‘skewed’ ones. What is your opinion about using the newest RealSense cameras and this 3D Aruco marker configuration in relation to our clinical user case?</p>
<p>I hope this improvement could result in avoiding the need for an expensive optical tracking system :).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0f262e20636f0b264fa5d8cd49ea0196244acaf.jpeg" data-download-href="/uploads/short-url/w5Ygl5sUOC19pd4kv9jhlIiCb5t.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0f262e20636f0b264fa5d8cd49ea0196244acaf.jpeg" alt="image" data-base62-sha1="w5Ygl5sUOC19pd4kv9jhlIiCb5t" width="523" height="500" data-dominant-color="ACA395"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">545×521 57.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>[<a href="https://www.mdpi.com/1424-8220/20/17/4825" class="inline-onebox" rel="noopener nofollow ugc">Sensors | Free Full-Text | Improved Pose Estimation of Aruco Tags Using a Novel 3D Placement Strategy</a>]</p>

---

## Post #4 by @lassoan (2022-06-24 14:07 UTC)

<p>Our initial experiments showed that by using the surface provided Intel RealSense cameras we could achieve one magnitude smaller distance error than with a simple monoscopic camera, but it was still several millimeters, instead of submillimeter that you get from a proper tracker. More work would have been needed to fuse the surface data with the 2D image based tracking data. Making the markers larger and using more markers in a 3D configuration always helps, but there is a limit in the size and weight of markers that are tolerable in the OR. Visible-light cameras are also more impacted by strong lighting in the OR (as opposed to cameras that come with their own infrared light sources and matched filters on the camera). I would estimate that it would require a few years of research work and some luck to sort out all these issues and get similar accuracy from a RealSense camera as you get from a wider-baseline infrared stereo camera such as the Optitrack Duo.</p>
<p>Intel dropped the RealSense product line, so by the time you would have a solution, you would need to look for another camera. Camera systems similar to RealSense cost about $1000 (and they may disappear from the market anytime), so the cost saving is likely to become even smaller than today. It may make sense to invest time into improving Aruco tracking if your main goal is to reduce the navigation system cost by $2000 and development (and redevelopment, when your chosen camera is discontinued) time and cost does not matter much.</p>

---
