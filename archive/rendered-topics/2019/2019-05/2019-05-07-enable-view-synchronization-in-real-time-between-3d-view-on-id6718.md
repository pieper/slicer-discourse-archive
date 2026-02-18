# Enable view synchronization in real-time between 3D View on Slicer and VR view on HTC vive

**Topic ID**: 6718
**Date**: 2019-05-07
**URL**: https://discourse.slicer.org/t/enable-view-synchronization-in-real-time-between-3d-view-on-slicer-and-vr-view-on-htc-vive/6718

---

## Post #1 by @mikecsu (2019-05-07 13:37 UTC)

<p>Operating system: win10<br>
Slicer version:4.11.0<br>
Expected behavior:To enable view synchronization in real-time between slicer and HTC vive<br>
Actual behavior:</p>
<p>Hi,I have been recently working on how to enable view synchronization in real-time between 3D View on Slicer and VR view on HTC vive. I noticed that i can synchronize the 3D view to VR view by clicking the button as i have shown in the below pic (red circle), and i think this button is really useful, but when it comes to real situation, we found that the patient is more likely to see the real-time change in VR view  when the doctor operates the 3D view on Slicer(instead of clicking the button each time after doctors’ operation ) . Since i am new to develop 3D slicer and nowadays i am working on the source code, i hope someone can give me some advice for this development, any help would be appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5ffc87d4ed077404713cd41596702ed4dd03851c.png" data-download-href="/uploads/short-url/dH8p2WGxpR7gegwW7bTetLjXhFO.png?dl=1" title="1557195000(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5ffc87d4ed077404713cd41596702ed4dd03851c_2_690x329.png" alt="1557195000(1)" data-base62-sha1="dH8p2WGxpR7gegwW7bTetLjXhFO" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5ffc87d4ed077404713cd41596702ed4dd03851c_2_690x329.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5ffc87d4ed077404713cd41596702ed4dd03851c_2_1035x493.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5ffc87d4ed077404713cd41596702ed4dd03851c.png 2x" data-dominant-color="C8C5D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1557195000(1)</span><span class="informations">1052×502 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-05-07 23:16 UTC)

<p>You can add an observer to the camera node so whenever the camera is rotated a callback function is called, which updates the view in the VR headset.</p>
<p>However, probably it would work better if you used two computers and two headsets and synchronize them as shown <a href="https://discourse.slicer.org/t/collaborative-surgery-planning-in-virtual-reality/6407/9">here</a>.</p>

---

## Post #3 by @mikecsu (2019-05-09 07:59 UTC)

<p>Thanks a lot. By checking the source code of Slicer Virtual Reality module ,we found that we can achieve the function that we want by continuously calling the function—updateViewFromReferenceViewCamera() which already exists in VR source code.</p>

---
