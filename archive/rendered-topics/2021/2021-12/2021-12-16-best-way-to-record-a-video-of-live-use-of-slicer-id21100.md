# Best way to record a video of live use of Slicer

**Topic ID**: 21100
**Date**: 2021-12-16
**URL**: https://discourse.slicer.org/t/best-way-to-record-a-video-of-live-use-of-slicer/21100

---

## Post #1 by @mau_igna_06 (2021-12-16 20:11 UTC)

<p>Hi devs.</p>
<p>For what I have read I should use C++ CLI modules so Slicer GUI doesn’t turn unresponsive to achieve my goal. That would be a CLI module call to takeScreenShot every 33mseg after a button is pressed, till that button is pressed again, then a CLI module convertFolderWithTempPicturesToVideo should be called. And the result would be the desired functionality (i.e. record live use videos of Slicer) without disturbing the user. Is this way okey? Is there any other way to do this (e.g. using other threads for these operations)?</p>

---

## Post #2 by @adamrankin (2021-12-16 20:29 UTC)

<p>Does it have to be done from Slicer? Could you use an external program to record?</p>

---

## Post #3 by @pieper (2021-12-16 20:39 UTC)

<p>I would not suggest a CLI here.  You can get a screenshot quickly by grabbing a widget in a <code>QTimer</code> callback.  Look how it is done in the ScreenCapture and Sequences modules.</p>

---

## Post #4 by @mau_igna_06 (2021-12-17 13:36 UTC)

<p>Yes. I have a working TakeScrenshot function that came from editing <a href="https://github.com/Slicer/Slicer/blob/936675ac035c38999f4ed8d3c9d03fb4e2c9cbdc/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1010">this</a>.</p>
<p>I’ve got to take the screenshots with a timer callback and then I could create the video.<br>
The intended FPS is 30 for recording (e.g. timer.setInterval(1000//30)) but it really is like 5 or 8 (and Slicer GUI gets jumpy). So when the video gets compiled at 30FPS it looks like it is fast-speed. Do you know how to really get 30FPS while recording and a fluid Slicer GUI interaction?</p>

---

## Post #5 by @jamesobutler (2021-12-17 14:03 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="2" data-topic="21100" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>Does it have to be done from Slicer? Could you use an external program to record?</p>
</blockquote>
</aside>
<p>I have found it easy to use the “Xbox Game Bar” app that comes with Windows. I just do Windows Key + G which brings up the app identifying the current application in use, press the record button then press the hovering stop button when I’m finished. Recording starting/stopping is a manual action by the user, but doesn’t require reinventing a screen recorder.</p>

---

## Post #6 by @pieper (2021-12-17 15:39 UTC)

<p>+1 to using the built in OS tools - for reference I use QuickTime Player on mac, which also has a screen recording utility and basic editing tools.  VLC is handy for exporting to other file formats.</p>

---

## Post #7 by @mau_igna_06 (2021-12-17 16:20 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="21100">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>+1 to using the built in OS tools</p>
</blockquote>
</aside>
<p>It is for a Slicelet that will be launched on the cloud.<br>
I think if we use a Windows docker container, we could use shell calls to start and stop recording with a built in Windows tool. Do you think that would be possible?</p>

---

## Post #8 by @pieper (2021-12-17 16:22 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="7" data-topic="21100">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>It is for a Slicelet that will be launched on the cloud.<br>
I think if we use a Windows docker container, we could use shell calls to start and stop recording with a built in Windows tool. Do you think that would be possible?</p>
</blockquote>
</aside>
<p>Im sure there’s a way to make it work, but I haven’t looked into the details.</p>

---

## Post #9 by @Greydon_Gilmore (2022-01-01 20:54 UTC)

<p>You could look into Open Broadcaster Studio (<a href="https://obsproject.com/" rel="noopener nofollow ugc">https://obsproject.com/</a>), which is an excellent open-source screen recorder for all platfoms. If you are thinking of using a container OBS might work for you.</p>
<p>The GitHub repo: <a href="https://github.com/obsproject/obs-studio" class="inline-onebox" rel="noopener nofollow ugc">GitHub - obsproject/obs-studio: OBS Studio - Free and open source software for live streaming and screen recording</a></p>
<p>Greydon</p>

---
