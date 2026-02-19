---
topic_id: 3783
title: "Volume Rendering Causes Application Crash"
date: 2018-08-15
url: https://discourse.slicer.org/t/3783
---

# Volume rendering causes application crash

**Topic ID**: 3783
**Date**: 2018-08-15
**URL**: https://discourse.slicer.org/t/volume-rendering-causes-application-crash/3783

---

## Post #1 by @opetne (2018-08-15 08:43 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.9.0 2018-08-01<br>
Expected behavior:Volume rendering ability<br>
Actual behavior:TDR error code 7</p>
<p>Hi everyone,</p>
<p>I have a series of a larynx micro CT. Format nifti, size approx. 180 MB. I loaded it and want to check in Volume rendering. It starts normaly and after the first movements an error code appears: TDR error code 7 the application must close.<br>
I have an NVIDIA Quadro 1000M graphic card with 2048 MB GDDR5 memory.<br>
In the Volume rendering module I choose GPU rendering, I select 2 GB memory size and it always crashes.<br>
What could be the solution?</p>
<p>Best,</p>
<p>Ors<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b3a9dc2f057f89ec1c984178058f27aaced7232.png" data-download-href="/uploads/short-url/3SStxtBewuRHeshKHcPwN1vKMwi.png?dl=1" title="tdr" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b3a9dc2f057f89ec1c984178058f27aaced7232_2_690x371.png" alt="tdr" data-base62-sha1="3SStxtBewuRHeshKHcPwN1vKMwi" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b3a9dc2f057f89ec1c984178058f27aaced7232_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b3a9dc2f057f89ec1c984178058f27aaced7232_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b3a9dc2f057f89ec1c984178058f27aaced7232_2_1380x742.png 2x" data-dominant-color="77788D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tdr</span><span class="informations">1919×1033 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-08-15 10:08 UTC)

<p>Your video card is too slow for rendering this large data set. The operating system interprets the slow response as the video card driver is crashed and it resets the card and shuts down the application. You have to reduce data set size by cropping or resampling in Slicer, or increase TDR delay in your operating system.</p>

---

## Post #3 by @opetne (2018-08-15 11:51 UTC)

<p>Dear Andras,</p>
<p>Thanks for the information. I changed the TDR settings in registry keys and gave a value of 8. After that the system shut down. I selected the multivolume rendering option and that helped.</p>

---

## Post #4 by @lassoan (2018-08-16 05:52 UTC)

<p>Multi-volume is currently faster because it does not use shading yet, but therefore the image quality is lower.</p>
<p>Increasing TDR delay fixes issues that you described above. If it did not help then I would recommend to try it again. It is somewhat tricky to set this registry value, because if you temporarily set it to 0 (e.g., you create the registry key but not set the value yet) then it shuts down your system, as TDR delay = 0 causes immediate TDR timeouts everywhere.</p>

---

## Post #5 by @muratmaga (2018-08-16 15:36 UTC)

<p>From a user’s perspective it might be worthwhile to emphasize on the download page that the GPU H/W requirements of the current nightly series is much higher than the stable. The change in volume rendering performance is so drastic that, an occasional user coming from 4.8.1 (and not following the discussions on discourse) would think it is a serious regression or a bug.</p>

---

## Post #6 by @opetne (2018-08-17 07:41 UTC)

<p>There should be a problem with my system. After I made a search how to change the TDR value for the Win10, I made the changes. At my first attempts a month ago, after the value was set to 8 the system reacted with a message that I have no GPU card. It might be that I not remember correctly, since it was an older nightly build version of the Slicer (downladed at 07.12.). I can’t recall the message now, the value 8 seems working at the moment on this nightly build version (4.9.0.  2018-08-01)</p>
<p>Ors</p>

---

## Post #7 by @lassoan (2018-08-18 07:38 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="3783">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>From a user’s perspective it might be worthwhile to emphasize on the download page that the GPU H/W requirements of the current nightly series is much higher than the stable.</p>
</blockquote>
</aside>
<p>Do you mean that we should warn users that a more recent OpenGL API version is needed?</p>

---

## Post #8 by @opetne (2018-08-23 10:31 UTC)

<p>I could provoce the problem again. Sorry if I don’t translate it correctly, the message was:<br>
“It is not allowed for the Slicer to use the graphic hardware”<br>
For Andras:<br>
Az alkalmazás számára nem engedélyezett a grafikus hardver elérése.<br>
This happened after I changed the TDR value to 8</p>

---

## Post #9 by @lassoan (2018-08-23 11:21 UTC)

<p>This error has been reported to happen for resource-intensive applications, such as games, and seems to be caused by faulty graphics driver operating system configuration.</p>
<ul>
<li><a href="https://answers.microsoft.com/en-us/windows/forum/windows_10-hardware/application-has-been-blocked-from-accessing/ad02b3e9-0785-44c7-a916-40d05b0a246e">https://answers.microsoft.com/en-us/windows/forum/windows_10-hardware/application-has-been-blocked-from-accessing/ad02b3e9-0785-44c7-a916-40d05b0a246e</a></li>
<li><a href="https://steamcommunity.com/app/730/discussions/0/38596747815376419/">https://steamcommunity.com/app/730/discussions/0/38596747815376419/</a></li>
<li><a href="http://www.tomshardware.com/answers/id-2834294/program-denied-access-graphics-hardware.html">http://www.tomshardware.com/answers/id-2834294/program-denied-access-graphics-hardware.html</a></li>
</ul>
<p>Based on my experience, NVidia Quadro users often run into strange driver/compatibility issues. Quadro GPUs are tested very thoroughly for a small set of applications (certain CAD software, etc.) but probably not much for anything else. If you <em>only</em> use NVidia Quadro certified applications then go with a Quadro, otherwise I would recommend to use GeForce GPUs instead - it is less expensive and more robust.</p>

---
