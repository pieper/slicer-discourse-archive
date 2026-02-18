# 3DSlicer VR and Unity

**Topic ID**: 3289
**Date**: 2018-06-25
**URL**: https://discourse.slicer.org/t/3dslicer-vr-and-unity/3289

---

## Post #1 by @Aenz (2018-06-25 21:12 UTC)

<p>Hey there,<br>
I’m pretty new in VR and development, maybe you can help me.<br>
Well, i want to create a crossSection plane, which i can move with my controllers, so i can see the inside of an object, like in this video</p>
<div class="lazyYT" data-youtube-id="pvwVg9JiMKQ" data-youtube-title="VTK OpenVR + HTC vive" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>my problem is, i really don’t know how to do this, i tried for many hours but it didn’t work.<br>
I work with unity, windows mixed reality and looking for a solution. Is there a possibility to connect the 3D Slicer with unity and VR?</p>
<p>Would be so glad to hear from you, thanks a lot!</p>

---

## Post #2 by @lassoan (2018-06-26 00:11 UTC)

<p>Slicer can display anything that you see in the 3D viewer in a virtual reality headset directly, using SteamVR, without Unity. Unity is really limited when it comes to medical image visualization: you have to work hard to get such basic features as reslicing volumes, volume rendering, and visualization of meshes that consists of more than a few hundred thousand points.</p>
<p>We only use Unity in connection with Slicer when we run standalone applications on Microsoft HoloLens - in that case Slicer sends transforms, images, and surface meshes through OpenIGTLink. However, probably this is not what you are looking for.</p>
<p>Currently, we find that moving your head inside organs works very well as a “dynamic clipping plane”, but of course having an additional independent cutting can be very useful.</p>
<p>Slicer’s virtual reality extension has already a built-in cutting plane feature. You can change controller mode by clicking one of the buttons on the controller then tilting the controller to choose mode. However, this is still experimental (you can only clip meshes, they are only clipped in the virtual reality view, etc.) but it’s there, so you can try it and maybe improve it.</p>

---

## Post #3 by @Aenz (2018-06-29 09:37 UTC)

<p>Thanks a lot for your quick reply.</p>
<p>That sounds great, exactly the thing i was looking for.</p>
<p>Is it possible to see the example scene „slicer 4minute“ in VR?</p>
<p>And do you know if i can work with VTK datasets as well?</p>

---

## Post #4 by @lassoan (2018-06-29 14:44 UTC)

<p>You can work with any data sets, and not just surface rendering but also direct volume rendering, in 2D, 3D, or 4D. Anything that you see in the 3D view you can show in the headset by a single click.</p>

---

## Post #5 by @timeanddoctor (2020-09-18 03:58 UTC)

<p>can I connect the hololens2 in slicer?</p>

---

## Post #6 by @lassoan (2020-09-21 20:19 UTC)

<p>There have been a number of projects using HoloLens as a renderer for models created in Slicer, sending transforms and images interactively from Slicer to HoloLens, but I’m not aware of any mature extension and HoloLens client that would be ready to use.</p>
<p>Most groups that I know of scaled back on HoloLens projects after their initial enthusiasm, because while the device is awesome, it is still just not good enough for many clinical use cases. Main problems are convergence/accommodation mismatch at arm-length distance, tracking instability, limited field of view, difficult access to data streams, and limited on-board computational resources. While I heard that HoloLens2 has greatly improved ergonomics, most of the issues still remain the same.</p>

---

## Post #7 by @timeanddoctor (2020-09-22 12:24 UTC)

<p>Thank you for your advice</p>

---

## Post #8 by @kopachini (2021-09-18 06:27 UTC)

<p>Dear Andras,</p>
<p>is there any news regarding HoloLens and Slicer? I saw <a href="https://www.youtube.com/watch?v=KdUdFQ44h3U&amp;list=LL&amp;index=1&amp;t=36s" rel="noopener nofollow ugc">this</a> video so I really want to buy HoloLens.</p>
<p>Could HoloLens be used just for viewing models using Slicer’s VR extension, too, or do we need appropriate VR googles like HTC Vive or Oculus Rift?</p>

---

## Post #9 by @lassoan (2021-09-18 13:27 UTC)

<p>There are a number of demos (including the YouTube video you are referring to) that uses Slicer to import image data, create models, and then then send them for display to a headset running a separate viewer implemented in Unity.</p>
<p>With <a href="https://developer.nvidia.com/nvidia-cloudxr-sdk">CloudXR</a> it should now be possible to stream VR and AR content from Slicer to HTC Vive, Oculus Quest 2, HoloLens 2, etc. devices directly from Slicer, without the need to develop and maintain a separate viewer. Slicer’s visualization toolkit, VTK, is also moving towards supporting OpenXR, which also promises direct rendering from desktop applications to headsets (including wireless and AR devices). These developments will greatly simplify and accelerate medical AR/VR application development in Slicer. However, these technologies are still very new and it is not a turnkey solution yet but some experimentation is required.</p>

---

## Post #10 by @kopachini (2021-09-23 16:44 UTC)

<p>Thank you for the answer.<br>
You mentioned HoloLens2, but what about HoloLens (1)?<br>
I know that I am being annoying but I have opportunity to buy HoloLens and want to be sure it will also work with 3D Slicer.</p>

---

## Post #11 by @lassoan (2021-09-23 16:49 UTC)

<p>You need to get a HoloLens 2 for remote augmented reality application streaming using CloudXR. Probably Unity will support HoloLens 1 for a while, so if you want to develop your own app running on HoloLens then it could work, but it is unlikely that any significant new software will be released for HoloLens 1.</p>

---

## Post #12 by @kopachini (2021-09-24 09:05 UTC)

<p>Could I use Hololens 1 without Cloud XR, just to reproduce 3d window from slicer using SteamVR?</p>
<p>Could you recommend any other AR goggles for slicer beside HoloLens?</p>
<p>čet, 23. ruj 2021. 18:49 Andras Lasso via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; je napisao:</p>

---

## Post #13 by @lassoan (2021-09-24 13:05 UTC)

<p>Probably it would make sense to use AR/VR application streaming because then you could directly use all the results of decades of desktop 3D software development, such as 3D Slicer, in your headset.</p>
<p>If you decide not to use streaming then probably you want to implement a simple viewer for 3D objects (generated using existing 3D platforms, such as Slicer) and some basic interactions. This was the approach that most people had to use before AR streaming existed. For this, you probably don’t want invest your time into learning the native SDK of any headset, because that would lock you in to a single hardware and big part of your knowledge would get irrelevant when that headset is discontinued. It is a safer bet to use a gaming engine, such as Unity3D or Unreal. Unity3D only supports the HoloLens and Magic Leap headsets (see <a href="https://docs.unity3d.com/Manual/AROverview.html">Unity3D AR documentation</a>). I would not trust Magic Leap due to their history of misleading investors and developers, and I’m not sure how much financially stable they are now. So, probably your safest choice is HoloLens.</p>

---

## Post #14 by @kopachini (2021-09-25 10:32 UTC)

<p>Ok, thank you. I just want to use it for viewing the models directly from a 3D slicer for preoperative planning, not for development, as I am a healthcare professional.<br>
Maybe in the future, there will be a need for some other usage like merging and registration with the patient body etc.</p>

---

## Post #15 by @lassoan (2021-09-26 04:01 UTC)

<p>It is not very clear for me what you would like to achieve. Are you interested in virtual reality or augmented reality.</p>
<p>Virtual reality is easy, just get a virtual reality capable computer (a recent desktop with a strong GPU; or a good gaming laptop), an OpenVR compatible VR headset, and you are good to go. You can view and interact with Slicer’s 3D viewer in virtual reality by a single click.</p>
<p>Augmented reality is an entirely different story. If you just wan to view 3D models then probably you can find a model viewer app for the HoloLens that allows basic visualization (translate, rotate, zoom). If you want to do in situ AR (make virtual objects, such as targets, needle guides, etc. appear in their correct 3D location) then it is a much harder problem. I don’t think there is any open solution that works out of the box: in addition to buying a headset, you also need to look around for existing prototypes, choose one, build it, import your own data sets, install on your headset, calibrate the system, etc. If you don’t have collaborators with experience in this and cannot hire someone with these skills then you may check if any of the commercial products are suitable for you.</p>

---

## Post #16 by @kopachini (2021-09-26 18:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="3289">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is not very clear for me what you would like to achieve. Are you interested in virtual reality or augmented reality.</p>
</blockquote>
</aside>
<p>For now, I want to view and perform basic operations like rotate, translate, etc. I am aware of possibilities with VR goggles and I have VR ready laptop.<br>
I was wondering, could I perform the same actions (view, rotate, zoom etc.) as with VR goggles in 3D Slicer’s 3D view using HoloLens1 without additional coding?<br>
Maybe later in a few months, I would try to registrate 3D model of an anatomical region (lets say brain tumor) in AR with the patient body (head) as seen in video that I posted earlier, also without too much coding? I have opportunity to buy HoloLens1 since the price of HoloLens 2 is too high for me at this moment.</p>

---

## Post #17 by @lassoan (2021-09-26 19:36 UTC)

<aside class="quote no-group" data-username="kopachini" data-post="16" data-topic="3289">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kopachini/48/65543_2.png" class="avatar"> kopachini:</div>
<blockquote>
<p>I was wondering, could I perform the same actions (view, rotate, zoom etc.) as with VR goggles in 3D Slicer’s 3D view using HoloLens1 without additional coding?</p>
</blockquote>
</aside>
<p>HoloLens1 does not support any of the standard mixed reality software interfaces and almost sure it never will. So, without custom software development you will not be able to use a HoloLens1 for anything else than basic surface model viewing (rotate, zoom, etc.).</p>
<p>The HoloLens2 supports OpenXR and via that standard interface you’ll be able to use the headset with a wide range of applications - eventually probably with 3D Slicer, too.</p>

---

## Post #18 by @abhiazadz (2022-02-19 11:37 UTC)

<p>Hey Lassoan, I am trying to find a way to send Fiducials from Unity to Slicer through OpenIGTLink, can you please tell me how I can do it? I have never done cross-platform connections before.</p>

---

## Post #19 by @lassoan (2022-03-13 05:11 UTC)

<p>There are a few OpenIGTLink implementations for Unity. You can try those. There is a summary <a href="https://www.slicer.org/wiki/Documentation/Labs/Augmented_Reality_and_Virtual_Reality_support">here</a>. It is quite old but may be usable as a starting point.</p>
<p>In the near future we’ll focus our efforts on driving the HoloLens directly from Slicer using OpenXR to avoid the need to develop a viewer in Unity.</p>

---
