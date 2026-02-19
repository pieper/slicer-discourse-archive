---
topic_id: 44261
title: "Bones Disappear At Random Frames Bug"
date: 2025-08-29
url: https://discourse.slicer.org/t/44261
---

# Bones disappear at random frames (bug?)

**Topic ID**: 44261
**Date**: 2025-08-29
**URL**: https://discourse.slicer.org/t/bones-disappear-at-random-frames-bug/44261

---

## Post #1 by @Lauren_Swain (2025-08-29 14:57 UTC)

<p>Hello,<br>
I have just recently started trying to use SAM for image registration but I have run into an issue where the bone DRR will disappear (also from the world view) for random frames during my trial. When they disappear, the rotations lines (yellow, magenta and cyan) also disappear from the timeline:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677bb8e08f3cd2eac33f7549310a36cc67937022.png" data-download-href="/uploads/short-url/eLsfGwfmQ9iuVmBHGabq0q1BXmW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677bb8e08f3cd2eac33f7549310a36cc67937022.png" alt="image" data-base62-sha1="eLsfGwfmQ9iuVmBHGabq0q1BXmW" width="240" height="300"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">320×400 3.25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It then won’t let me add a key frame for any of those points as I get the message: ‘Tracker::trackFrame(): Volume 0 is not in view of camera 0’ for both cameras. However, when I have reloaded .tra files where I have tried to add key frames, it will sometimes then have added key frames for those frames (with the bone in a seemingly random location).</p>
<p>I have had this happen for multiple bones during the same trial, with them disappearing for different frames (and different amounts of frames).</p>
<p>Has anyone else seen this happen before? I would be grateful for any help/advice!</p>
<p>Lauren</p>

---

## Post #2 by @Amy_Morton (2025-08-29 15:20 UTC)

<p>Hey <a class="mention" href="/u/lauren_swain">@Lauren_Swain</a></p>
<p>Can you provide some workspace screenshots/ possibly your camera calibration info? Did you perform your preprocessing in xmalab/ sam-pre-processing tab?</p>
<p><a class="mention" href="/u/john_holtgrewe">@John_Holtgrewe</a> have you seen anything like this?</p>

---

## Post #3 by @John_Holtgrewe (2025-08-29 17:41 UTC)

<p>I have not seen anything like this before.</p>
<p><a class="mention" href="/u/lauren_swain">@Lauren_Swain</a> Does this happen for other trials as well?</p>

---

## Post #4 by @davidelwyn (2025-09-01 11:09 UTC)

<aside class="quote no-group" data-username="Amy_Morton" data-post="2" data-topic="44261">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/amy_morton/48/67318_2.png" class="avatar"> Amy_Morton:</div>
<blockquote>
<p>Can you provide some workspace screenshots/ possibly your camera calibration info? Did you perform your preprocessing in xmalab/ sam-pre-processing tab?</p>
</blockquote>
</aside>
<p>Lauren is away on leave so I can respond on her behalf. We calibrated using xmalab and utilised the sam-pre-processing method (albeit in a slightly different way using MRI, probably worth a seperate conversation) such that it generates the PV and aut_models.</p>
<p>I have attached a screenshot (the matching is not finalised!) showing the Femur missing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c34fdd4feb02e1af5b81e47e81dd5117c2fe5c13.jpeg" data-download-href="/uploads/short-url/rROdmVkrd7u0m3mV03i9k4UBH4n.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c34fdd4feb02e1af5b81e47e81dd5117c2fe5c13_2_690x262.jpeg" alt="image" data-base62-sha1="rROdmVkrd7u0m3mV03i9k4UBH4n" width="690" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c34fdd4feb02e1af5b81e47e81dd5117c2fe5c13_2_690x262.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c34fdd4feb02e1af5b81e47e81dd5117c2fe5c13_2_1035x393.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c34fdd4feb02e1af5b81e47e81dd5117c2fe5c13_2_1380x524.jpeg 2x" data-dominant-color="06284A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2092×795 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/amy_morton">@Amy_Morton</a> regarding the camera calibration, is that the mayacam files?</p>
<p><a class="mention" href="/u/john_holtgrewe">@John_Holtgrewe</a> we have just started with SAM but should be trialing new activites in the next few weeks,</p>

---

## Post #5 by @Amy_Morton (2025-09-02 13:53 UTC)

<p>Thanks <a class="mention" href="/u/davidelwyn">@davidelwyn</a></p>
<p>What does the remainder of the Autoscoper screen look like? Specifically the volumes widget group?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d673eb507ef86a535f36104ba18f4a4a3139634.gif" alt="lceblsq5" data-base62-sha1="b2JXVgfoWkPH2pMoiVSpkVhVmxS" width="690" height="373" class="animated"></p>
<p>Example:</p>

---

## Post #6 by @Lauren_Swain (2025-09-08 10:10 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d325ee56bd34c4e241c916a1e1264073e3220a21.jpeg" data-download-href="/uploads/short-url/u7U0OhAAH4ZkwqKpAiyrQ35CUsV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d325ee56bd34c4e241c916a1e1264073e3220a21_2_690x374.jpeg" alt="image" data-base62-sha1="u7U0OhAAH4ZkwqKpAiyrQ35CUsV" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d325ee56bd34c4e241c916a1e1264073e3220a21_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d325ee56bd34c4e241c916a1e1264073e3220a21_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d325ee56bd34c4e241c916a1e1264073e3220a21_2_1380x748.jpeg 2x" data-dominant-color="42596F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1041 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi Amy,</p>
<p>See the above screenshot of the whole screen (including the volumes widget). I haven’t noticed anything unusual about the volumes widget (but as we have only just started using SAM I may not have spotted something obvious).</p>
<p>Having loaded this after a week away, it now only seems to be a problem for the femur but it was initially a problem with all three of the bones.</p>
<p>Thanks,<br>
Lauren</p>

---

## Post #7 by @Amy_Morton (2025-09-08 20:36 UTC)

<p>I’ll need some more to go on here- can you reach out via email for a 30mins zoom?</p>

---
