# Collaborative surgery planning in virtual reality

**Topic ID**: 6407
**Date**: 2019-04-05
**URL**: https://discourse.slicer.org/t/collaborative-surgery-planning-in-virtual-reality/6407

---

## Post #1 by @cpinter (2019-04-05 14:53 UTC)

<p>Hi all,</p>
<p>While working on some potential clinical use cases, we (with <a class="mention" href="/u/lassoan">@lassoan</a>) made a video about collaborative planning in VR, in which two Slicer instances using the same scene are connected through OpenIGTLink, so we can see each other in VR. We thought you’ll find this interesting.</p>
<div class="lazyYT" data-youtube-id="rG9ST6xv6vg" data-youtube-title="Collaborative surgery planning in virtual reality" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #2 by @cpinter (2019-04-05 18:44 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I like the new tag you created <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=9" title=":rofl:" class="emoji" alt=":rofl:"></p>

---

## Post #3 by @Nicholas.jacobson (2019-04-08 17:10 UTC)

<p>This is great guys! We’ve been trying to use your process in 3d slicer for VR but its been a big learning curve. This helps.</p>

---

## Post #4 by @sarvpriya1985 (2019-04-25 13:45 UTC)

<p>Hi,<br>
It looks great! Is there any tutorial for this (about linking)</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #5 by @cpinter (2019-04-25 14:20 UTC)

<p>There is no tutorial, because the process is not polished at all (it was quite lengthy to set up), and this was just an experiment.</p>
<p>We’re planning to develop a module in the near future that helps setting up the Slicer instances for VR collaboration. Probably we’ll make a tutorial for the module once it’s done.</p>

---

## Post #6 by @sarvpriya1985 (2019-04-25 15:26 UTC)

<p>Thanks for getting back.</p>
<p>One more question. I am working with windows mixed reality headset. I am planning to invest in a new headset. I read in one of the discussions somewhere that HTC vive is good one. Is there any specific thing that can be done by HTC vive regarding virtual display. Also any suggestions on the model of HTC vive to be used for use with SLicer.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #7 by @lassoan (2019-04-25 15:50 UTC)

<p>The main difference of HTC Vive compared to Windows MR headsets is that HTC Vive uses fixed lighthouse devices, which make tracking initialization more robust (you don’t need to look around after you put on the headset but you can start tracking right away). So, if you have a dedicated place where you use your virtual reality system then I would recommend HTC Vive; if you want to have a portable system then I would recommend any Windows MR headset.</p>
<p>If you use a laptop then probably go with the classic HTC Vive (it is hard to find laptops that can drive an HTC Vive Pro), if you have a desktop system with one of the newest GPUs then you can use an HTC Vive Pro (it has somewhat better specs than the basic HTC Vive).</p>

---

## Post #8 by @sarvpriya1985 (2019-04-25 16:16 UTC)

<p>Thanks for clarifying Andras. I guess I have to stick to windows headset as I don’t have a dedicated place.</p>
<p>Thanks again,<br>
Sarv</p>

---

## Post #9 by @lassoan (2019-05-07 23:14 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="6407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>There is no tutorial, because the process is not polished at all (it was quite lengthy to set up),</p>
</blockquote>
</aside>
<p>I think the setup is quite painless, especially if you just modify an existing scene that has the controller transforms sharing already configured. The setup could be also automated with a short Python script.</p>
<p>The main idea is that you run two instances of Slicer, each of them connected to a headset. Both instances contain the same data nodes (models, volumes, etc.) and their parent transforms are set as outgoing nodes in OpenIGTLinkIF module (which ensures the transform nodes are synchronized between the instances). The scene that we used in the video is available <a href="https://1drv.ms/u/s!Arm_AFxB9yqHt6I_2zmVp7FhX9b0Cw">here</a>.</p>

---

## Post #10 by @sarvpriya1985 (2019-05-08 04:49 UTC)

<p>Thanks Andras.</p>
<p>I haven’t worked with Open IGTLimk module. So have to see if I can recreate the scene. I will post if I am able to achieve similar results.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #11 by @Isam_Al_Hassan (2021-12-15 06:41 UTC)

<p>Hi sir , I’m working with unity , is their any chance to exchange developments so we all reach to the best of it? i need MRI scan from hospitals so i do the experience. my email <a href="mailto:isam.al.hassan@gmail.com">isam.al.hassan@gmail.com</a></p>
<p>thank you</p>

---
