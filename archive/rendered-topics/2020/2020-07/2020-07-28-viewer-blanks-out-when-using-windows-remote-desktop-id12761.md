# Viewer blanks out when using windows remote desktop 

**Topic ID**: 12761
**Date**: 2020-07-28
**URL**: https://discourse.slicer.org/t/viewer-blanks-out-when-using-windows-remote-desktop/12761

---

## Post #1 by @Krishna_Nanda (2020-07-28 19:30 UTC)

<p>Hello,</p>
<p>I have been trying to view an image series on slicer 4.10.2 via remote desktop. The patient list and other parts of the GUI all appear ok except for the image series in the viewer. The viewer goes blank (dark) when I load the series. I see these msgs in the logs:<br>
“GLEW could not be initialized.<br>
Hardware does not support the number of textures defined.<br>
versionFunctions: Not supported on OpenGL ES”</p>
<p>The host computer is running windows 7, Quadro P2000 graphics card. The client computer is running windows 10. I looked around the forum and it seemed like the recent versions of RDP should connect fine. But it could be that the mstsc client that comes along with the windows 10 home edition doesn’t satisfy the requirement. Any suggestions/pointers would be helpful.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-07-28 20:05 UTC)

<p>Remote desktop works fine from a Windows10 Home client to a Windows10 Pro server with Intel and AMD Radeon graphics.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a26ac7ac3028e880b2b5a9576549be6e023c31b.jpeg" data-download-href="/uploads/short-url/lZGo5FIcGDHhjfWTZfYVceQTZ7J.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a26ac7ac3028e880b2b5a9576549be6e023c31b_2_690x486.jpeg" alt="image" data-base62-sha1="lZGo5FIcGDHhjfWTZfYVceQTZ7J" width="690" height="486" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a26ac7ac3028e880b2b5a9576549be6e023c31b_2_690x486.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a26ac7ac3028e880b2b5a9576549be6e023c31b_2_1035x729.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a26ac7ac3028e880b2b5a9576549be6e023c31b_2_1380x972.jpeg 2x" data-dominant-color="D8D8D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1900×1339 478 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>NVidia chose to block their GeForce cards and make things complicated for Quadro, but finally they seem to have enabled it recently: <a href="https://www.khronos.org/news/permalink/nvidia-provides-opengl-accelerated-remote-desktop-for-geforce-5e88fc2035e342.98417181" class="inline-onebox">NVIDIA provides OpenGL-accelerated Remote Desktop for GeForce - The Khronos Group Inc</a>. Probably you just need to tune your remote desktop settings, maybe you need to adjust some Windows Remote Desktop group policy settings as described on some websites.</p>
<p>Using VNC is always an option, too. It is not as fast as RDP, but good enough for most use cases.</p>

---

## Post #3 by @Andinet_Enquobahrie (2020-07-29 10:46 UTC)

<p>I have been using NoMachine remote desktop app from a Windows 10 to a Ubuntu server with Slicer installations and it has been working really well for me.</p>
<p>Andinet</p>

---

## Post #4 by @Krishna_Nanda (2020-08-04 22:36 UTC)

<p>Hi Andras, Andinet, thanks for all the helpful suggestions. Andras, I installed the binary from the link you provided. I also tried editing the remote desktop group policy settings, as suggested by some websites, but with no luck. In one of the past threads, you had mentioned about using a script to start Slicer before connecting to the machine. Could that be useful? I couldn’t find a valid version of that script to give that a try.</p>

---

## Post #5 by @lassoan (2020-08-04 23:19 UTC)

<aside class="quote no-group" data-username="Krishna_Nanda" data-post="4" data-topic="12761">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/krishna_nanda/48/7632_2.png" class="avatar"> Krishna_Nanda:</div>
<blockquote>
<p>In one of the past threads, you had mentioned about using a script to start Slicer before connecting to the machine. Could that be useful?</p>
</blockquote>
</aside>
<p>Yes, there may be some configurations where this technique still works. To try it, you can connect to the remote computer using vnc, teamviewer, or google remote desktop, start Slicer, and then connect using Windows Remote Desktop.</p>

---

## Post #6 by @Krishna_Nanda (2020-08-07 18:21 UTC)

<p>Thanks Andras. I can confirm everything works fine when connected via chrome remote desktop or teamviewer. Starting the Slicer session via team viewer first and then connecting via RDP works fine too. Is there a simple script to start the slicer session automatically before connecting via RDP? I was checking here <a href="https://mantisarchive.slicer.org/view.php?id=4252" rel="nofollow noopener">https://mantisarchive.slicer.org/view.php?id=4252</a>, but seems like the downloaded script is empty.</p>

---

## Post #7 by @lassoan (2020-08-08 03:57 UTC)

<p>I think attachments in the the old bugtracker are not available anymore. I’ve uploaded the content of <code>start.bat</code> here: <a href="https://github.com/Slicer/Slicer/issues/4252">https://github.com/Slicer/Slicer/issues/4252</a></p>

---

## Post #8 by @Krishna_Nanda (2020-08-11 17:01 UTC)

<p>Thanks for uploading the script Andras. After setting the correct remote session ID, it ran fine. Now, I am able to load single slices from File -&gt; add data and view them fine. But for some reason, the dicom module for loading scans doesn’t open. Clicking on the DCM in the toolbar or File -&gt; DICOM. This seems to be the case on both Slicer 10.1 and 10.2. In any case, appreciate all your help with this.</p>

---

## Post #9 by @lassoan (2020-08-11 18:19 UTC)

<p>Does latest Slicer Preview Release work well?</p>

---

## Post #10 by @Krishna_Nanda (2020-08-11 18:52 UTC)

<p>The latest preview release (4.11.0) gets stuck right after I launch it on Windows 7. The initial box that displays the launch progress like “initializing modules” is frozen.</p>

---

## Post #11 by @lassoan (2020-08-11 19:55 UTC)

<p>We don’t test anything with Windows 7 anymore. Windows 7 is insecure could put the entire network it is connected to at risk. I would recommend to upgrade to Windows 10 as soon as possible.</p>

---
