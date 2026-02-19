---
topic_id: 4946
title: "Sharing Virtual Reality View With Users"
date: 2018-12-04
url: https://discourse.slicer.org/t/4946
---

# Sharing virtual reality view with users

**Topic ID**: 4946
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/sharing-virtual-reality-view-with-users/4946

---

## Post #1 by @sarvpriya1985 (2018-12-04 01:52 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.1.10<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I recently tried windows mixed reality headset at RSNA. My question is the headset let me see the desktop but I cant show the same to another individual in real space ( i mean only the person wearing headset can see the image). Do we have any headset (other than hololens) that can project the virtual image in real space that can be seen by everyone even without glasses.<br>
Other thing is if I use Microsoft hololens (it is expensive but can show virtual image in real space), do i need to do something extra.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @cpinter (2018-12-04 03:11 UTC)

<p>Hi Sarv,</p>
<p>I’m not sure what you mean exactly by “project the virtual image in real space that can be seen by everyone even without glasses”. If I discard the idea of how Leia’s message was played in Star Wars (I don’t think it’s possible yet), then I assume you’re asking about showing the VR rendering on the monitor.</p>
<p>When you do VR in Slicer it uses SteamVR. It has a small window that pops up when you start VR. In that small window you’ll find an option to show the mirror image. It will open a new window which contains the same image you see in the headset.</p>
<p>I’ll let others answer about Hololens.</p>

---

## Post #3 by @sarvpriya1985 (2018-12-04 11:08 UTC)

<p>Hi</p>
<p>Thanks for replying. What I mean is that Hololens (Microsoft’s headset) places the 3D scene in such a way ( not on monitor but in actual physical space) that it can be seen by everyone without glasses and the one wearing glasses can manipulate the images. I was looking for a way out of this as hololens is quite expensive.</p>
<p>Thanks</p>
<p>Sarv</p>

---

## Post #4 by @lassoan (2018-12-04 13:58 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="3" data-topic="4946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>What I mean is that Hololens (Microsoft’s headset) places the 3D scene in such a way ( not on monitor but in actual physical space) that it can be seen by everyone without glasses</p>
</blockquote>
</aside>
<p>This would be wonderful, but unfortunately holograms are only visible to people wearing the HoloLens headset.</p>
<p>You can see (slightly inaccurate) preview of what the person wearing the HoloLens can see by using the Device Portal. If you mean that you would like to see this kind of preview of virtual reality then you can use the mirror option as <a class="mention" href="/u/cpinter">@cpinter</a> described above. To facilitate communication between the virtual reality user and others, you can also make the controllers show up in the 3D viewer in the desktop by exposing the controller transforms in the scene.</p>

---

## Post #5 by @sarvpriya1985 (2018-12-04 19:05 UTC)

<p>Thanks Andrass,<br>
Will try mirroring the scene and see how it goes.</p>
<p>Thanks,</p>
<p>Sarv</p>

---

## Post #6 by @kopachini (2018-12-05 21:51 UTC)

<p>Hi Sarv,<br>
I was also at RSNA this year but didn’t see what are you mentioning about HoloLens.<br>
I tried working with them at last years RSNA (augmented reality during surgery show) and it looked cool but only thing what was visible to the crowd was video (operator’s view) projected on the big screen, no holograms.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b0a79ec4cb8a67a3ca7a2fce1ae923951dc0daa.jpeg" data-download-href="/uploads/short-url/8qiCc4yuRcqLx8fR4oPAraZKrTc.jpeg?dl=1" title="20171126_121550" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b0a79ec4cb8a67a3ca7a2fce1ae923951dc0daa_2_690x388.jpeg" alt="20171126_121550" data-base62-sha1="8qiCc4yuRcqLx8fR4oPAraZKrTc" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b0a79ec4cb8a67a3ca7a2fce1ae923951dc0daa_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b0a79ec4cb8a67a3ca7a2fce1ae923951dc0daa_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b0a79ec4cb8a67a3ca7a2fce1ae923951dc0daa.jpeg 2x" data-dominant-color="7E6867"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20171126_121550</span><span class="informations">1354×763 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Vjeko.</p>

---

## Post #7 by @sarvpriya1985 (2018-12-06 14:11 UTC)

<p>Hi,<br>
I saw the Hololens at SPR conference this year in which one person wore the headset and all of us in the room could see the image that was projected in space. I was hoping if we could do the same with less expensive headsets.</p>
<p>Sarv</p>

---

## Post #8 by @sarvpriya1985 (2018-12-06 14:13 UTC)

<p>Hi,</p>
<p>I tried HP windows mixed reality headset yesterday. I was looking for the mirror image option but could not see it. Could you pls guide me further how to fix this. If not in real space I wish to project the view on monitor or projector atleast.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #9 by @cpinter (2018-12-06 14:53 UTC)

<p>It’s an option in the SteamVR panel that shows up when you start VR from Slicer</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/3786b588a0a880b00bcaff70965361ece69ab7a7.png" alt="image" data-base62-sha1="7VcSaYTry77tdAJYiFJdQ46iIh9" width="267" height="419"></p>

---

## Post #10 by @sarvpriya1985 (2018-12-06 15:19 UTC)

<p>Hi,<br>
The display mirror option was checked but it didnt’t work. Want to clarify one thing: when i visualize segmented heart, do I need to zoom in the 3d view in the monitor or it doesnt matter. The reason I am asking is if I zoomed too much (in slicer window)  I could not manipulate image through my headset.</p>
<p>Sarv</p>

---

## Post #11 by @lassoan (2018-12-06 15:26 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="10" data-topic="4946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>The display mirror option was checked but it didnt’t work.</p>
</blockquote>
</aside>
<p>We use it regularly with all kinds of headsets. What do you mean by that it does not work? Can you share a screen capture video or screenshot of what you do and what happens?</p>
<aside class="quote no-group" data-username="sarvpriya1985" data-post="10" data-topic="4946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>when i visualize segmented heart, do I need to zoom in the 3d view in the monitor or it doesnt matter</p>
</blockquote>
</aside>
<p>Desktop 3D view zoom only matters if you reset the virtual reality view to match the desktop 3D view. Reset may be performed when you connect and when you click the corresponding toolbar button. Other than that, you can freely move/rotate/scale the world in your virtual reality view, independently from what is done in desktop views.</p>

---

## Post #12 by @sarvpriya1985 (2018-12-06 15:28 UTC)

<p>Thanks Andras<br>
I will post the screenshot soon.</p>
<p>Sarv</p>

---

## Post #13 by @sarvpriya1985 (2018-12-07 16:24 UTC)

<p>I was able to mirror the VR view on monitor.</p>
<p>Thanks everyone.</p>
<p>Sarv</p>

---
