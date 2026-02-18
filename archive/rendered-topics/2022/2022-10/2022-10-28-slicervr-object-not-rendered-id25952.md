# SlicerVR: Object not rendered

**Topic ID**: 25952
**Date**: 2022-10-28
**URL**: https://discourse.slicer.org/t/slicervr-object-not-rendered/25952

---

## Post #1 by @andreasjahnen (2022-10-28 10:44 UTC)

<p>Hello,</p>
<p>I am currently working with Slicer 5.0.3 and an freshly installed SlicerVR module and StreamVR on a laptop with an NVIDIA 3080 GPU using a HTC Vive 2 Headset on Windows 10. I configured that slicer-real.exe should use the GPU. SteamVR works using other applications. I can connect to the headset within Slicer.</p>
<p>If I select in the “Volume Rendering” tab the  “VTK CPU Ray Casting” I can see the scene. If I select “VTK GPU Ray Casting” it disappears and I see only the background color.</p>
<p>Can anybody help and suggests me how to fix this problem?</p>
<p>The task manager shows, that the GPU is used in the later case.</p>
<p>Thank you in advance!</p>
<p>Best Regards,<br>
Andreas</p>

---

## Post #2 by @pieper (2022-10-28 13:29 UTC)

<p>As I recall this is a known problem and everything is still being worked on with the current versions of VTK and the eventual move from OpenVR to OpenXR.  You should be able to install an older Slicer (one of the 4.11 releases should work).</p>

---

## Post #3 by @cpinter (2022-10-28 19:45 UTC)

<p>Yes, older versions work as Steve says. However, this volume rendering issue has recently been fixed in the SlicerVR extension. As I recall it was an issue related to camera transformations. I intend to try it next week and if the basic things work make sure that it is packaged for the preview releases. Can you please remind me in a week or so about this?</p>

---

## Post #4 by @andreasjahnen (2022-10-31 10:04 UTC)

<p>Dear Steve, dear Csaba,</p>
<p>thank you very much for your help. In Slicer 4.11, all works fine.</p>
<p>I tested as well the Slicer 5.1.0 (revision 31255) from 2022-10-29. Here it works as well, but a error message says “The action manifest for SlicerApp-real.exe was not found.” and the controllers do not work. Just for your information.</p>
<p>I will remind you end of next week to test this.</p>

---

## Post #5 by @cpinter (2022-11-04 11:34 UTC)

<p>Please see how to solve the action manifest problem here: <a href="https://github.com/KitwareMedical/SlicerVirtualReality/pull/90#issuecomment-1065076413" class="inline-onebox">Update integration to support VTK 9.1 by jcfr · Pull Request #90 · KitwareMedical/SlicerVirtualReality · GitHub</a></p>

---

## Post #6 by @andreasjahnen (2022-11-04 14:33 UTC)

<p>I tested it and the error message is gone now. But I can not manipulate the object as in the old 4.11 version.</p>

---

## Post #7 by @cpinter (2022-11-04 14:36 UTC)

<aside class="quote no-group" data-username="andreasjahnen" data-post="6" data-topic="25952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/andreasjahnen/48/17097_2.png" class="avatar"> andreasjahnen:</div>
<blockquote>
<p>can not manipulate the object as in the old 4.11</p>
</blockquote>
</aside>
<p>Please elaborate (what object, what manipulation)</p>

---

## Post #8 by @andreasjahnen (2022-11-04 14:45 UTC)

<p>There was no effect at all. And no error message in Slicer.</p>
<p>I did not investigate more, that has been the only test I have done. I can do more tests end of next weeks.</p>

---

## Post #9 by @cpinter (2022-11-04 14:49 UTC)

<p>Can you please answer the question? What object could you not manipulate and by what kind of manipulation? Do you mean moving models or segmentations in the scene with the grab button?</p>

---

## Post #10 by @rbumm (2022-11-06 13:25 UTC)

<p>Did a short test run on various Slicer versions with an Oculus Quest 2 using an identical and simple lung mask segmentation as well as a volume rendering from CT Chest demo dataset.<br>
Windows 11, OpenVR (SteamVR)</p>
<p>In 4.11 I can connect to the headset and render. The segmentation appears in VR space in front of me and can be grabbed by using the two grip buttons and moved / rotated / tilted in VR space. The function basically works but could be improved a lot. The right thumbstick button up/down moves the object in and out. It would be logical to have right/left for rotation, but this seems not to be implemented. As a minimum, it would also be necessary to have a “way out” from the VR screen (finishing the VR session and returning to desktop) but I do not see this implemented.</p>
<p>In 4.13 I get the “The action manifest for SlicerApp-real.exe was not found” error message on the Quest. This can be overcome by copying the files you mentioned above and restarting Slicer.<br>
Then rendering can be started, but the in/out function does not work, and pressing both grip buttons to grab the object lets it disappear from VR space completely.</p>
<p>Slicer 5.1.0-2022-10-21 has the same problems as 4.13 and the VR function seems not usable.</p>

---
