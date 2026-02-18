# How to improve OptiTrack Duo tool tracking stability

**Topic ID**: 19882
**Date**: 2021-09-27
**URL**: https://discourse.slicer.org/t/how-to-improve-optitrack-duo-tool-tracking-stability/19882

---

## Post #1 by @drvarunagarwal (2021-09-27 04:26 UTC)

<p>Hello everyone,</p>
<p>we are also facing some problems but slightly different.<br>
We are using optitrack duo, Which are tracking commercial instruments from medtronic (which I had lying spare so used these)</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f3cb80d0999e6ff9f2b3f7f338f243beb9a43ab.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f3cb80d0999e6ff9f2b3f7f338f243beb9a43ab.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f3cb80d0999e6ff9f2b3f7f338f243beb9a43ab.mp4</a>
    </source></video>
  </div><p></p>
<p>As you can see from the attached video, Even though the stylus is fixed and not moving at all, there is some “Jitter” with the stylus. As a result ICP registration also suffers.</p>
<p>My commercial medtronic system (stealthstation S7 - using polaris) doesn’t behave this way.</p>
<p>Please advise how to fix this,</p>
<p>thanks in anticipation.</p>

---

## Post #2 by @drvarunagarwal (2021-09-27 04:28 UTC)

<p>The motive window also shows markers to be perfectly stable…</p>

---

## Post #3 by @lassoan (2021-09-27 04:43 UTC)

<aside class="quote no-group" data-username="drvarunagarwal" data-post="1" data-topic="19882">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drvarunagarwal/48/8914_2.png" class="avatar"> drvarunagarwal:</div>
<blockquote>
<p>My commercial medtronic system (stealthstation S7 - using polaris) doesn’t behave this way.</p>
</blockquote>
</aside>
<p>Medtronic StealthStation uses an NDI Polaris tracker with a much wider baseline than the OptiTrack Duo (it is also about 5-6x more expensive). If you need higher accuracy then you can get an OptiTrack Trio (still much cheaper than a Polaris). There are also many parameters in Motive that you can tune to get more accurate tracking.</p>
<aside class="quote no-group quote-post-not-found" data-username="drvarunagarwal" data-post="4" data-topic="19862" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drvarunagarwal/48/8914_2.png" class="avatar"><a href="https://discourse.slicer.org/t/how-to-make-the-stylus-more-smooth-and-stable/19862/4">How to make the stylus more smooth and stable</a></div>
<blockquote>
<p>The motive window also shows markers to be perfectly stable…</p>
</blockquote>
</aside>
<p>This is expected, because you see the marker positions in Motive, while the tooltip position is far away and may be computed relative to a reference marker:</p>
<ul>
<li>If you use a reference marker then the transform that you see is computed by concatenating two transforms (stylus to tracker, tracker to reference), therefore the jitter will be much larger than just one transform’s jitter.</li>
<li>You visualize the tooltip, which may be 10-15cm away from the marker. A 1deg rotational jitter in the tracking error will result in 2-3mm jitter of the tooltip.</li>
</ul>

---

## Post #4 by @pll_llq (2021-09-27 09:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="19882">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There are also many parameters in Motive that you can tune to get more accurate tracking.</p>
</blockquote>
</aside>
<p>Based on your experience what parameters in Motive or in the surrounding environment (flickering LED lights in the room etc.) give biggest impact on tracking stability?<br>
I’ve tried playing around with exposure and trajectory smoothing but the first one doesn’t appear to give significant impact and the second one as expected introduces an extra 300 ms lag.</p>

---

## Post #5 by @drvarunagarwal (2021-09-27 10:38 UTC)

<p>I understand your saying that the tip may be 10-15 cm away.<br>
that may be true when the tool is held in hand.</p>
<p>However for a stationary tool these should not change. Stationary and fixed to a wall for example…</p>
<p>also with your experience with polaris in plus toolkit and slicer IGT, do polaris also causes some jitter?</p>

---

## Post #6 by @lassoan (2021-09-27 15:12 UTC)

<aside class="quote no-group" data-username="pll_llq" data-post="4" data-topic="19882">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>Based on your experience what parameters in Motive or in the surrounding environment (flickering LED lights in the room etc.) give biggest impact on tracking stability?</p>
</blockquote>
</aside>
<p>I don’t remember exactly, but to make the tracking as accurate as possible, you need to make the markers appear in the image as small as possible, but large enough so that it can be still robustly detected.</p>
<p>Another issue can be that Motive might use the center of gravity of the marker instead of center of a fitted circle or ellipse. If the stylus is oriented poorly (as it is visible in the video above) then the reflective balls trimmed lower part will make the center of gravity of the reflection shifted compared to the true center of the sphere. Try to position the camera so that the marker plane of the tool is approximately orthogonal to the camera’s view direction.</p>
<aside class="quote no-group" data-username="drvarunagarwal" data-post="5" data-topic="19882">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drvarunagarwal/48/8914_2.png" class="avatar"> drvarunagarwal:</div>
<blockquote>
<p>However for a stationary tool these should not change. Stationary and fixed to a wall for example…</p>
</blockquote>
</aside>
<p>There is always vibration due to traffic outside, people walking in the room, air moving in the room, so putting down an object on the table or fixing to the wall does not actually eliminate all motion. That’s why people use optical tables when they need to reduce vibration. However, if you find that using the same setup you don’t see that much jitter with a Polaris tracker then most likely mechanical vibration is not the main contributor.</p>
<p>The measured tool pose is also affected by image noise. That may come from electronics noise (not strong enough lighting, thermal noise, electronic interference, etc.), changing lighting, etc.</p>
<p>If the tracking setup is not very robust overall then small motion or image noise can cause noticeable jitter. If the jitter is random around the correct mean value then you can enable spatial filtering either in the tracker or in Slicer. In Slicer, you can use SlicerIGT extension’s Transform Processor module (processing mode: Stabilize).</p>

---

## Post #7 by @pll_llq (2021-09-28 08:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="19882">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If the jitter is random around the correct mean value then you can enable spatial filtering either in the tracker or in Slicer. In Slicer, you can use SlicerIGT extension’s Transform Processor module (processing mode: Stabilize).</p>
</blockquote>
</aside>
<p>Thanks for your response. I will look deeper into this</p>

---

## Post #8 by @drvarunagarwal (2021-10-07 09:40 UTC)

<p>Hi,</p>
<p>just to update this issue</p>
<p>we found a solution for this.</p>
<p>we reduced the exposure to 6 micro sec from 50 micro sec and there was an immense increase in stability and almost negligible jitter.</p>
<p>This for benefit for anyone else who has faced such issue.</p>
<p>If anyone is interested in further details on such issue can refer link below:</p>
<p><a href="https://www.google.com/search?q=reduce+jitter+optitrack+motive&amp;rlz=1C5CHFA_enIN503IN504&amp;oq=reduce+jitter+optitrack+motive&amp;aqs=chrome..69i57j33i160.7470j0j4&amp;sourceid=chrome&amp;ie=UTF-8" rel="noopener nofollow ugc">https://www.google.com/search?q=reduce+jitter+optitrack+motive&amp;rlz=1C5CHFA_enIN503IN504&amp;oq=reduce+jitter+optitrack+motive&amp;aqs=chrome…69i57j33i160.7470j0j4&amp;sourceid=chrome&amp;ie=UTF-8</a></p>
<p>From optitrack wiki:</p>
<p><a href="https://v22.wiki.optitrack.com/index.php?title=Quick_Start_Guide:_Precision_Capture" rel="noopener nofollow ugc">https://v22.wiki.optitrack.com/index.php?title=Quick_Start_Guide:_Precision_Capture</a></p>
<p>For the precision capture, it is not always necessary to set the camera exposure to its lowest value. Instead, the exposure setting should be configured so that the reconstruction is most stable. Zoom into a marker and examine the jitters while changing the exposure setting, and use the exposure value that gives the most stable reconstruction. Later sections will cover how to check the reconstruction and tracking quality. For now, set this number as low as possible while maintaining the tracking without losing the contrast of the reflections.</p>
<p><a href="https://forums.naturalpoint.com/viewtopic.php?t=13917" rel="noopener nofollow ugc">https://forums.naturalpoint.com/viewtopic.php?t=13917</a></p>

---
