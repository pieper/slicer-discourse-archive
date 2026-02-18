# VR connection to steam/HTC VIVe

**Topic ID**: 5645
**Date**: 2019-02-05
**URL**: https://discourse.slicer.org/t/vr-connection-to-steam-htc-vive/5645

---

## Post #1 by @gptruncus (2019-02-05 19:26 UTC)

<p>Apologies if this has been asked and answered, when we hit the VR button to connect, a screen shows up within VR headset with 3 little dashes “thinking” and trying to connect, but never connect and show whats on 3D slicer. VR works in SteamVR just fine. Any suggestions. SteamVR panel says not connected.</p>

---

## Post #2 by @cpinter (2019-02-12 19:20 UTC)

<p>Sorry for the late reply. If you are using a laptop that has two graphics cards, make sure that Slicer is forced to use the dedicated one. Sometimes it uses the integrated one by default.</p>

---

## Post #3 by @lassoan (2019-05-11 19:08 UTC)

<p>See some troubleshooting and performance optimization tips in the extension’s documentation (<a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/README.md#rendering-is-slow" rel="nofollow noopener">FAQ section</a>).</p>

---

## Post #4 by @kopachini (2021-11-01 12:45 UTC)

<p>Hello once again…<br>
Finally, I bought Oculus Quest 2, connected it and it works… I can open a 3D slicer through my desktop mirror on my goggles but when I try to open it with Steam VR it says that the slicer is not connected with the same graphic card as the monitor. I saw on FAQ question as <a class="mention" href="/u/lassoan">@lassoan</a> said and went to the graphics section but when I want to designate my graphic card to 3d slicer, there is no SlicerApp-real. exe to choose, just Slicer.<br>
What do I have to do to enjoy the full potential of the Slicer capabilities in the VR?? How to connect it to the same graphic card as my monitor<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bf2e9bb9085c70ae767fa4f9c3a70e6a23058f5.jpeg" alt="slicer" data-base62-sha1="hGvaohlD5etf99nhqUGo4s292iV" width="585" height="434"></p>

---

## Post #5 by @muratmaga (2021-11-01 15:21 UTC)

<aside class="quote no-group" data-username="kopachini" data-post="4" data-topic="5645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kopachini/48/65543_2.png" class="avatar"> kopachini:</div>
<blockquote>
<p>there is no SlicerApp-real. exe to choose, just Slicer</p>
</blockquote>
</aside>
<p>SlicerApp-real sits one folder below where Slicer.exe is (<strong>bin/SlicerApp-real.exe</strong>)</p>

---

## Post #6 by @kopachini (2021-11-16 16:33 UTC)

<p>Thank you, I found it, and now it works just fine <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Is there any tutorial on how to use VR extension, besides the above-mentioned FAQ section?</p>
<p>I managed to zoom in and out models, rotate it… but how to make some parts slightly transparent for better visualisation (like skull), or to delete part of the model and make window for viewing inside…<br>
Any other possible actions?</p>

---

## Post #7 by @lassoan (2021-11-17 06:35 UTC)

<p>I know it is surprising, but actually all you need to set up amazing features is just those information described on the <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/README.md">SlicerVR extension main page</a>. Since the controllers and each grabbed object automatically creates transforms, you can drag-and-drop objects in the Data module’s “Transform hierarchy” tab to apply those transform to other objects, you can use the Volume Reslice Driver or Dynamic Modeler module to clip into models, and you can add observers and control any feature of Slicer using the controllers.</p>
<aside class="quote no-group" data-username="kopachini" data-post="6" data-topic="5645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kopachini/48/65543_2.png" class="avatar"> kopachini:</div>
<blockquote>
<p>how to make some parts slightly transparent for better visualisation (like skull)</p>
</blockquote>
</aside>
<p>You can go to Models module on the desktop to adjust transparency. If you want to edit transparency in the immersive view then you can place any object (load an STL file) and add an observer to its parent transform. When you grab that object with a controller then the observer calls your custom Python function that changes the appearance of any object, based on how the object is moved (e.g., up/down changes opacity, left-right changes color; about 2-3 lines of code).</p>
<aside class="quote no-group" data-username="kopachini" data-post="6" data-topic="5645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kopachini/48/65543_2.png" class="avatar"> kopachini:</div>
<blockquote>
<p>or to delete part of the model and make window for viewing inside</p>
</blockquote>
</aside>
<p>There is no need to delete any part to view inside. Usually we just make the model a comfortable size and move it in a comfortable position, then we step or peek inside. You can cut out parts by enabling model clipping and moving slice planes; or moving planes with the controller.</p>
<p>These are not convenient and requires knowledge of Slicer and some creative ideas. We are working towards having intuitive widgets (window with checkboxes, sliders, etc.) to the immersive view, which will make things much easier to discover or set up.</p>

---
