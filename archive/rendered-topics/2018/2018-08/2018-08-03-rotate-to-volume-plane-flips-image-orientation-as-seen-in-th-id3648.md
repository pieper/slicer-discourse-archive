---
topic_id: 3648
title: "Rotate To Volume Plane Flips Image Orientation As Seen In Th"
date: 2018-08-03
url: https://discourse.slicer.org/t/3648
---

# "Rotate to volume plane" flips image orientation as seen in the slice viewer

**Topic ID**: 3648
**Date**: 2018-08-03
**URL**: https://discourse.slicer.org/t/rotate-to-volume-plane-flips-image-orientation-as-seen-in-the-slice-viewer/3648

---

## Post #1 by @fedorov (2018-08-03 21:33 UTC)

<p>I recently discovered a rather disturbing regression. When I examine an axial image that was acquired in an oblique plane, it appears that the image is effectively flipped when “Rotate to volume plane” is toggled.</p>
<p>In the video below, I demonstrate this problem with today’s nightly and <a href="http://slicer.kitware.com/midas3/download/item/126192/5-AX_T2.zip">this prostate T2w MRI series</a></p>
<p>            <video title="2018-08-03_17-24-29.mp4" width="695" height="423" style="max-width:100%" controls="">
              <source src="https://content.screencast.com/users/andrey.fedorov/folders/Snagit/media/3322653b-eed9-40c1-83ba-8da7b9e831b9/2018-08-03_17-24-29.mp4"></source>
            </video>
</p>
<p>To explain, I first scroll through slices in the superior direction (towards the head), and as expected the bladder is closer to the head than the apex of the prostate. I then rotate to the volume plane, and do the same, and now when I scroll the image in the same direction, it scrolls in the direction of the apex. As seen in the 3d viewer, the direction is changed as compared to the original one. I say the image is “flipped”, because based on the slider position reported by the red viewer, the plane position showing bladder in Axial view shows apex in the Reformat view!</p>
<p>This is indeed a regression, since when I do the same operation in the latest stable release, the behavior is consistent with my expectations.</p>
<p>            <video title="2018-08-03_17-25-25.mp4" width="695" height="428" style="max-width:100%" controls="">
              <source src="https://content.screencast.com/users/andrey.fedorov/folders/Snagit/media/4ab93c31-8de6-4dea-8ba2-be664fb97a52/2018-08-03_17-25-25.mp4"></source>
            </video>
</p>

---

## Post #2 by @lassoan (2018-08-04 00:06 UTC)

<p>The change in behavior is the result of some recent improvements of this feature (you don’t need to reset manually to Axial/Sagittal/Coronal standard orientation and reapply “rotate to volume plane”, no need for guess which standard orientation will show a single-slice volume, etc). Part of this was standardization of coordinate axes directions, so that slice X, Y, and normal directions are always in a right-handed coordinate system (before this, it was left-handed for axial and sagittal orientations and right-handed and coronal).</p>
<p>I agree that the left/right-handedness should not flip, so this should be fixed.</p>
<p>Since all other coordinate systems in Slicer are right-handed, I would find it more intuitive to make all slice coordinate systems consistently right-handed, too. Do you have any preference for making slice XYZ coordinate system left or right handed?</p>
<p>Maybe we could postpone standardization of default orientations and just keep whatever handedness the slice coordinate system during rotate to volume plane operation.</p>

---

## Post #3 by @fedorov (2018-08-04 23:00 UTC)

<p>Andras, I just think that this is a breaking change, and in this particular situation the orientation should not change after rotating to volume plane. When I first saw this, I was confused for several minutes trying to figure out if something was wrong with the acquisition, or the image was flipped during conversion. I think the current behavior is a bug.  By the way radiologists sometime report finding location by slice position.</p>

---

## Post #4 by @lassoan (2018-08-04 23:39 UTC)

<p>I have fixed flipping of left/right-handedness when “rotate to volume plane” is clicked (<a href="https://github.com/Slicer/Slicer/commit/ea79c943d168f637cb3347bda199d47bbb111890">https://github.com/Slicer/Slicer/commit/ea79c943d168f637cb3347bda199d47bbb111890</a>).</p>
<p>Is there any preference in which slider direction corresponds to which anatomical direction? Current default directions are inconsistent from software design standpoint (sometimes left, other times right handed coordinate system), but if there is a strong user preference for slider/anatomical direction mapping then they may be left as is.</p>

---

## Post #5 by @lassoan (2018-08-05 00:10 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="3648">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>By the way radiologists sometime report finding location by slice position</p>
</blockquote>
</aside>
<p>Displayed slice position was not impacted. Only slice offset direction → slider direction mapping was flipped in some cases.</p>

---

## Post #6 by @fedorov (2018-08-05 21:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="3648">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I have fixed flipping of left/right-handedness when “rotate to volume plane” is clicked</p>
</blockquote>
</aside>
<p>Thank you! I will test it next week.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="3648">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is there any preference in which slider direction corresponds to which anatomical direction?</p>
</blockquote>
</aside>
<p>I am confused by this question. I thought Slicer uses RAS coordinate system, which means that coordinates increase as we move in the IS direction. If I am in Axial (or in Oblique view that is “close” to Axial), I expect that if I move from apex to base of the prostate, my slider position will increase.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="5" data-topic="3648">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Displayed slice position was not impacted. Only slice offset direction -&gt; slider direction mapping was flipped in some cases.</p>
</blockquote>
</aside>
<p>If you look at the first screencapture I attached, the slice position was indeed different when the axis is flipped. The same numeric location of the slider position can be either in the apex or base of the prostate, depending on whether you did rotate to volume plane or not. Maybe there is some other way to look at it, but if I think of a radiologist, who looks at the slider position, and for whom 3d view is usually a nuisance, I think they would be really scratching their heads seeing this.</p>

---

## Post #7 by @lassoan (2018-08-05 22:19 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="6" data-topic="3648">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I thought Slicer uses RAS coordinate system, which means that coordinates increase as we move in the IS direction</p>
</blockquote>
</aside>
<p>If slice positioning slider is moved to the right then the slice is moved towards slice normal direction (third column of SliceToRAS matrix). This is independent of what coordinate system is used.</p>
<aside class="quote no-group" data-username="fedorov" data-post="6" data-topic="3648">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>The same numeric location of the slider position can be either in the apex or base of the prostate, depending on whether you did rotate to volume plane or not.</p>
</blockquote>
</aside>
<p>This is a good point. Slice position in oblique views is simply the signed distance from the origin along the slice normal direction. Therefore, for oblique views, the numeric value has no absolute meaning (the same physical position may correspond to infinite number of different displayed numeric values). Maybe we should hide the numerical value from the slice slider when the slider is not aligned to world coordinate system axes to make sure users don’t want to interpret it as some anatomical coordinate.</p>

---

## Post #8 by @fedorov (2018-08-08 18:14 UTC)

<p>I confirm that the issue is fixed in the nightly, thank you <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---
