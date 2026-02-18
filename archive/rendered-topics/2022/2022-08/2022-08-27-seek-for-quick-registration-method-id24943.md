# Seek for quick registration method

**Topic ID**: 24943
**Date**: 2022-08-27
**URL**: https://discourse.slicer.org/t/seek-for-quick-registration-method/24943

---

## Post #1 by @whu (2022-08-27 07:59 UTC)

<p>Dear All,</p>
<p>Here I got the EM tracker, a STL format Geometric model and corresponding physical object.</p>
<p>I want to get three points, both with the EM positon and the Slicer posiontion information.</p>
<p>As to the tutorial in IGT, we can compute a Rigid Transform.</p>
<p>Can this kind of methond used to registration the model and the physical object ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c512944791179ad9f535bd63f0368358ad87ebc.jpeg" data-download-href="/uploads/short-url/hJL5N3vgwoqk481X8tskirrLOUc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c512944791179ad9f535bd63f0368358ad87ebc_2_690x314.jpeg" alt="image" data-base62-sha1="hJL5N3vgwoqk481X8tskirrLOUc" width="690" height="314" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c512944791179ad9f535bd63f0368358ad87ebc_2_690x314.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c512944791179ad9f535bd63f0368358ad87ebc_2_1035x471.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c512944791179ad9f535bd63f0368358ad87ebc_2_1380x628.jpeg 2x" data-dominant-color="8B909D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×874 77.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The IGT landmark registration <a href="https://1drv.ms/p/s!AhiABcbe1DBygcAwmU7_GDzj4iGxWg" class="inline-onebox" rel="noopener nofollow ugc">Microsoft OneDrive - Access files anywhere. Create docs with free Office Online.</a> may not be operated easily.</p>
<p>Thanks…</p>

---

## Post #2 by @lassoan (2022-08-27 22:41 UTC)

<p>The landmark registration tutorial that you have linked is good. We have completed it with dozens of students in our bootcamps over the years without any issues. If you have any specific questions or unclear steps then let us know.</p>

---

## Post #3 by @whu (2022-08-29 14:21 UTC)

<p>Thank you very much.<br>
As to the real application, I just want to make the EM tracker（on the physical model） registrated to the virtual Needle( on the CG model in Slicer)， like other IGT example below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f16c2767c8157e44a8527ed3d661e4b952e6ae3f.jpeg" alt="image" data-base62-sha1="yrIMVilNsl7EJT3kFAgT2y6yaVV" width="591" height="334"></p>
<p>The linked steps seem perfect, but how to load the video ?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01979ff6838f05e6b61f0303679bef45c4cd5be5.jpeg" alt="image" data-base62-sha1="e5kB4qycSLQdPpDvjxyXj3kGKF" width="585" height="402"></p>
<p>Maybe I just to compute the transform and change them like this ?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f43fbb6f88b472a961be54656d514c762dbaca1b.png" alt="image" data-base62-sha1="yQJ2ZNFWXcbfUyZUy4B97XWQUP1" width="641" height="251"></p>
<p>fused…</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji only-emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2022-08-29 16:06 UTC)

<aside class="quote no-group" data-username="whu" data-post="3" data-topic="24943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/7ab992/48.png" class="avatar"> whu:</div>
<blockquote>
<p>The linked steps seem perfect, but how to load the video ?</p>
</blockquote>
</aside>
<p>You would normally not record a video if you just want to register a model’s coordinate system to the attached tracking marker’s coordinate system. The video is just added to the tutorial so that you can complete a registration workflow without having access to real hardware. If you load the mrb file that comes with the tutorial then you should will see the video (you can show the “Sequence browser” toolbar to see play/pause button for replaying the sequence).</p>

---

## Post #5 by @whu (2022-08-30 01:19 UTC)

<p>I just want to get a simple and easy UI for registration, maybe a result transform is ok.<br>
Let uers choose three markup points pair, one from the em tracker position（physical）, and one from  the cg model（slicer）, after this we may compute the transform.<br>
Using the transform above（maybe more then one transform, we just need the result）, the real time em position to the cg model will be ok.<br>
Is this right ?</p>

---

## Post #6 by @jay1987 (2022-08-30 02:23 UTC)

<p>in my opinion , it needed to fix 3 position in em tracker(physical),after that , we only need to position 3 point in the cg model(slicer), then we can use landmark to perform a registration.</p>

---

## Post #7 by @whu (2022-08-30 02:26 UTC)

<p>yes，maybe we need a simple operation for this.</p>

---

## Post #8 by @whu (2022-09-02 02:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="24943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You would normally not record a video if you just want to register a model’s coordinate system to the attached tracking marker’s coordinate system.</p>
</blockquote>
</aside>
<p>How to finish this kind of work without a video, I get the tracker connected.<br>
“from” where ? from what ?<br>
"to " can be reagarded as the markup points.<br>
thanks.</p>

---

## Post #9 by @lassoan (2022-09-03 15:12 UTC)

<aside class="quote no-group" data-username="whu" data-post="5" data-topic="24943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/7ab992/48.png" class="avatar"> whu:</div>
<blockquote>
<p>I just want to get a simple and easy UI for registration, maybe a result transform is ok.<br>
Let uers choose three markup points pair, one from the em tracker position（physical）, and one from the cg model（slicer）, after this we may compute the transform.<br>
Using the transform above（maybe more then one transform, we just need the result）, the real time em position to the cg model will be ok.</p>
</blockquote>
</aside>
<p>Yes, exactly it is as simple as that.</p>
<p>Of course in reality there are small things like you first need to calibrate your stylus (so that you collect points at the tip of the stylus and not at the center of the marker), but that has to be done only once. You only need to think a bit when you set up your transform tree (what transform is applied to what node), but again that’s something that you need to understand only once and can be done by a couple of clicks in the GUI (and then you can save it in the scene). Once you have your complete workflow, you can further automate everything using Python scripting, so users only need the minimum number of clicks. This last layer of automation is not done in Slicer core or general-purpose extensions, such as SlicerIGT, because each workflow is slightly different (how many tools you have, how you attach trackers on them, what coordinate system you choose as the renderer’s world coordinate system, if you use imaging, surface scanning, etc.).</p>
<aside class="quote no-group" data-username="whu" data-post="5" data-topic="24943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/7ab992/48.png" class="avatar"> whu:</div>
<blockquote>
<p>Let uers choose three markup points pair, one from the em tracker position（physical）, and one from the cg model（slicer）, after this we may compute the transform.</p>
</blockquote>
</aside>
<p>Things are not quite as simple as this. Even in the simplest scenario you have at least these coordinate systems:</p>
<ul>
<li>Tracker (tracker’s world coordinate system)</li>
<li>Reference (coordinate system of the sensor that is attached to the patient)</li>
<li>Stylus (coordinate system of the sensor that is attached to the stylus)</li>
<li>StylusTip (coordinate system aligned to the tip of the pointer)</li>
<li>Model (coordinate system where points of the “cg” model are specified)</li>
</ul>
<p>Your goal is to compute ModelToReference, so you need to compute the transform from “Model” to “Reference”, therefore the “From” point coordinates must be specified in the Model coordinate system (you can get them by simply placing markup points on the model) and the “To” point coordinates must be specified in the Reference coordinate system (you can get them by sampling the StylusTipToReference transform).</p>
<p>I would recommend to make a drawing of all coordinate systems and transforms that you compute between them. <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT</a> and <a href="https://github.com/PerkLab/PerkLabBootcamp/tree/master/Doc">PerkLab bootcamp</a> tutorials should help you to understand the process.</p>

---

## Post #10 by @whu (2022-09-04 11:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="24943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>and the “To” point coordinates must be specified in the Reference coordinate system</p>
</blockquote>
</aside>
<p>Here I don’t know how to get the coordinate positions through the gui, though the transform can be seen from the Transform module, but there is no “record the current” transform button(that is just imagination).<br>
so, just one step left…</p>

---

## Post #11 by @lassoan (2022-09-04 12:26 UTC)

<p>You can record the current stylus tip position in “Fiducial registration wizard” module’s “Place fiducials using transforms” section.</p>

---

## Post #13 by @whu (2022-09-08 04:27 UTC)

<p>I tried it, and seemed that it worked, but still need some help.<br>
In the slicer scene, a model loaded, EM tracker loaded, as below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e6379a032f31a0cf28275b43ec73384e6aa6321.png" data-download-href="/uploads/short-url/fKxE3SkLIEWpgGdAcLVLGsn0i3L.png?dl=1" title="result2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e6379a032f31a0cf28275b43ec73384e6aa6321_2_690x414.png" alt="result2" data-base62-sha1="fKxE3SkLIEWpgGdAcLVLGsn0i3L" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e6379a032f31a0cf28275b43ec73384e6aa6321_2_690x414.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e6379a032f31a0cf28275b43ec73384e6aa6321_2_1035x621.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e6379a032f31a0cf28275b43ec73384e6aa6321_2_1380x828.png 2x" data-dominant-color="C8C9D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">result2</span><span class="informations">1546×929 73.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In the left view, LV simulator is the model;Locator_probetotracker is the “needle” model that can move freely ; the LinearTransform is added mannuly intened to receive the registration transform.<br>
After using the Fiducial registration wizard module, “From” is the markup in the LV simulator; “To” using the transform  as [quote=“lassoan, post:11, topic:24943”]“Place fiducials using transforms” section[/quote]<br>
The result as below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/043617e3ba9dadfd4cb1cb09aad695ea40e0be6a.png" data-download-href="/uploads/short-url/BfNRF1wqIii9BEpH7gNYnnA5CO.png?dl=1" title="result1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043617e3ba9dadfd4cb1cb09aad695ea40e0be6a_2_690x409.png" alt="result1" data-base62-sha1="BfNRF1wqIii9BEpH7gNYnnA5CO" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043617e3ba9dadfd4cb1cb09aad695ea40e0be6a_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043617e3ba9dadfd4cb1cb09aad695ea40e0be6a_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043617e3ba9dadfd4cb1cb09aad695ea40e0be6a_2_1380x818.png 2x" data-dominant-color="BEC4CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">result1</span><span class="informations">1594×947 75 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here I meet some questions：<br>
1）RMS Error maybe too high ? though for three point-pair …<br>
2)  How to change the</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="24943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>transform tree</p>
</blockquote>
</aside>
<p>as in the firt image, in order to fill with the expection as</p>
<aside class="quote no-group" data-username="whu" data-post="3" data-topic="24943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/7ab992/48.png" class="avatar"> whu:</div>
<blockquote>
<p>As to the real application, I just want to make the EM tracker（on the physical model） registrated to the virtual Needle( on the CG model in Slicer)， like other IGT example below.</p>
</blockquote>
</aside>
<p>Let the needle follows the EM tracker.</p>
<p>Thanks  for any advices.</p>

---
