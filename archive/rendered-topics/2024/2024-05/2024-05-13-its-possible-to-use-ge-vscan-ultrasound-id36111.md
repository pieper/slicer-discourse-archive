# It's possible to use GE Vscan Ultrasound?

**Topic ID**: 36111
**Date**: 2024-05-13
**URL**: https://discourse.slicer.org/t/its-possible-to-use-ge-vscan-ultrasound/36111

---

## Post #1 by @ruben99999 (2024-05-13 12:53 UTC)

<p>Hello, I am a master student who for his thesis project tries to use a GE Vscan Extend Ultrasound to perform a real-time 3D reconstruction of a phantom. However, from what I’ve read, I don’t think this type of scanner is supported. Is there a way to use such an ultrasound?</p>
<p>Thank you very much</p>

---

## Post #2 by @lassoan (2024-05-13 12:54 UTC)

<p><a class="mention" href="/u/coltonbarr">@ColtonBarr</a> It would be great if you could summarize the solutions that you implemented to use live GE Vscan images in Slicer.</p>

---

## Post #3 by @ruben99999 (2024-05-15 09:45 UTC)

<p>Thanks for the answer, would it be possible to contact <a class="mention" href="/u/coltonbarr">@ColtonBarr</a> privately?</p>

---

## Post #4 by @lassoan (2024-05-15 11:03 UTC)

<p>He will answer here. Probably many other people are interested in this and it would not be efficient to answer each person in private.</p>

---

## Post #5 by @ruben99999 (2024-05-15 12:10 UTC)

<p>Sorry if I said something inappropriate, thank you again for your availability.</p>

---

## Post #6 by @ColtonBarr (2024-05-15 15:29 UTC)

<p>Hi Paolo - sorry for the slow response! I ran into a similar issue when using the GE Vscan Air CL to perform 3D ultrasound reconstructions. The challenge is that the GE VScan products do not have an API that supports realtime streaming as far as I’m aware.</p>
<p>While GE does have some developer resources for interfacing with their ultrasound products (which you can apply to access through the <a href="https://www.gehealthcare.com/products/ultrasound-developer-program" rel="noopener nofollow ugc">GE Ultrasound Developer Program</a>), they do not currently support the VScan family of products. The only products for which there is an API that supports realtime streaming of image data are the Vivid and EchoPAC systems.</p>
<p>The Vscan Air CL probe that I was using primarily interfaces with an app on a mobile device. A possible workaround I explored was streaming the contents of the mobile device’s screen into Slicer. To test this I made a Slicer extension that can connect with an Android device and streams the contents of the phone screen into Slicer as a scalar volume. It uses a Python version of the Android Debug Bridge (ADB) called <a href="https://pypi.org/project/adb/" rel="noopener nofollow ugc">python-adb</a> to communicate with the phone and was able to achieve around 5 fps at full resolution with around 1 second of latency. I’m happy to package this extension into a public repository if anyone is interested.</p>
<p>There were several limitations to this approach. Text and graphics on the phone screen appeared as artifacts in the ultrasound images; I was only able to achieve this with a wired connection to the phone; and ultrasound calibration was difficult to maintain due to the probe zoom and overall field of view being altered by the user. We were still able to perform ultrasound calibration and 3D volume reconstruction despite these challenges, but the quality was poor.</p>
<p>The GE Vscan Extend that you’re using comes packaged with its own display, rather than connecting to a user’s phone, which further complicates streaming data from the device. The built-in display does appear to just be a phone running Android, but I suspect GE has put restrictions on modifying properties of the device. Communicating with a phone through Android Debug Bridge requires low-level access to the device which is likely locked in a commercial product.</p>
<p>If you do find you’re able to connect the Android display to a computer via USB and  enabling USB debugging mode on the display I can share some more details on how to setup streaming into Slicer. Otherwise unfortunately I’m not aware of any other methods of streaming the data into Slicer from that probe.</p>
<p>I hope this is helpful! Do let me know if I can clarify any details or answer any further questions.</p>

---

## Post #7 by @ruben99999 (2024-05-20 08:48 UTC)

<p><a class="mention" href="/u/coltonbarr">@ColtonBarr</a> Hi Colton, Thank you so much for the detailed explanation. I was able to enable USB debugging mode on the display and connect the Ge Vscan extend to the PC. I would be interested in understanding how you then made the extension and I would like to have more details on how to set up streaming in Slicer.</p>

---

## Post #8 by @ColtonBarr (2024-05-24 20:42 UTC)

<p>Hi <a class="mention" href="/u/ruben99999">@ruben99999</a> - happy to help! That’s great to hear that you were able to get the VScan connected to your PC. This may be a feasible method of getting data off the device.</p>
<p>I’ve created a public GitHub repo where you can access the Slicer extension for streaming from an Android device: <a href="https://github.com/ColtonBarr/StreamAndroidExtension" rel="noopener nofollow ugc">StreamAndroidExtension</a>. This extension should enable you select your Android device from a dropdown menu, set some streaming settings, and stream the contents of the Android device’s screen into a Volume node in Slicer. Here is a diagram showing the general setup:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9a0214c79ab8c2dbc2bef6054d4bba8afe429a2.jpeg" data-download-href="/uploads/short-url/xkKkjJsgCJsumkj1AOwpsL1gl8K.jpeg?dl=1" title="StreamAndroidExamplePic" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9a0214c79ab8c2dbc2bef6054d4bba8afe429a2_2_690x398.jpeg" alt="StreamAndroidExamplePic" data-base62-sha1="xkKkjJsgCJsumkj1AOwpsL1gl8K" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9a0214c79ab8c2dbc2bef6054d4bba8afe429a2_2_690x398.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9a0214c79ab8c2dbc2bef6054d4bba8afe429a2_2_1035x597.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9a0214c79ab8c2dbc2bef6054d4bba8afe429a2_2_1380x796.jpeg 2x" data-dominant-color="C5C0C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">StreamAndroidExamplePic</span><span class="informations">1867×1077 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>While this diagram covers how I used it to stream from the GE Vscan Air, the same general scheme applies to the Ge Vscan Extend. I’ve included the basic setup instructions and some troubleshooting tips in the ReadMe on GitHub.</p>
<p>Let me know if you run into any issues getting the extension running! Also feel free to submit issues to the GitHub if there are bugs that come up or features you would like added. I think streaming from an Android device into Slicer could be more broadly applicable beyond this specific use-case so I’m happy to continue improving the extension.</p>

---

## Post #9 by @lassoan (2024-09-12 01:57 UTC)

<p>A post was split to a new topic: <a href="/t/create-3d-volume-from-2d-ultrasound-with-imu/38343">Create 3D volume from 2D ultrasound with IMU</a></p>

---
