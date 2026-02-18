# Padding a volume with CropVolume requires "Interpolated Cropping"

**Topic ID**: 8750
**Date**: 2019-10-11
**URL**: https://discourse.slicer.org/t/padding-a-volume-with-cropvolume-requires-interpolated-cropping/8750

---

## Post #1 by @muratmaga (2019-10-11 20:11 UTC)

<p>This is more of a comment than a bug.</p>
<p>I just want to expanded a volume to accommodate a larger volume during registration. I know I can use padImage  in Simple Filters, but I wanted to do it interactively with Crop Volume (as the changes are not uniform).  It worked, but only if I chose the 'interpolated cropping", which made the intensity values of the output volume different than original volume, and also more fuzzy.</p>

---

## Post #2 by @lassoan (2019-10-12 04:12 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="8750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I just want to expanded a volume to accommodate a larger volume during registration.</p>
</blockquote>
</aside>
<p>Adding empty regions around a volume should not affect the registration (and there is a chance that it makes the registration worse).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="8750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It worked, but only if I chose the 'interpolated cropping", which made the intensity values of the output volume different than original volume, and also more fuzzy.</p>
</blockquote>
</aside>
<p>It was slightly easier to implement voxel-based cropping so that it does not make volume extents larger, but I agree that it would be more consistent to allow growing of the volume in both interpolated and non-interpolated mode. I’ll update the module.</p>

---

## Post #3 by @lassoan (2019-10-12 16:13 UTC)

<p>Crop volume module can grow the volume extent in both interpolated and non-interpolated modes in Slicer Preview Release (from rev28544).</p>

---

## Post #4 by @muratmaga (2019-10-12 17:44 UTC)

<p>Thanks Andras!!!</p>

---

## Post #5 by @muratmaga (2019-10-13 18:47 UTC)

<p>Hi Andras,<br>
I gave a quick try and there seems two issues:</p>
<ol>
<li>Interpolated cropping now flips the X and Z dimensions somehow (only with interpolated checked)</li>
<li>Without interpolation, dimensions are not expanded, but the origin is modified<br>
This is with 28544 on WIndows 10.<br>
To replicate<br>
download MRHead<br>
go to crop volume and set a the ROI to volume extends and do a interpolated cropping to see dimension value flipped in the volumes module for the new cropped volume.<br>
enlarge the ROI a bit and now do an voxel based cropping to see the dimensions remain the same but origin is shifted.</li>
</ol>

---

## Post #6 by @lassoan (2019-10-13 18:58 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="8750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Interpolated cropping now flips the X and Z dimensions somehow (only with interpolated checked)</p>
</blockquote>
</aside>
<p>When performing interpolated cropping, axis directions are determined by ROI’s axis directions. Order of input volume axes has no effect (as they may not even aligned with any of the ROI’s axes).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="8750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Without interpolation, dimensions are not expanded, but the origin is modified</p>
</blockquote>
</aside>
<p>It works well for me. Please try again. You can set a fill value of 100 to make the padded region more visible.</p>

---

## Post #7 by @muratmaga (2019-10-13 22:43 UTC)

<p>OK. I see voxel-based cropping is indeed working. What threw me off was the fields didn’t get updated in the volume information tab. I didn’t cross-checked in the volumes module.</p>
<p>However, the behavior for interpolated cropping seems a little awkward, I don’t recall being it like that.<br>
This is the original volume properties:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/652ae997316ec9602f6353ac3f24cee3dcc0f82b.png" alt="image" data-base62-sha1="eqYaaAfKiVvKbQNVJWMCgq7YFxV" width="688" height="370"></p>
<p>This is what I see after enlarging the ROI</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c3f38977da508192c7157f9ea2420a7fd030b62.png" alt="image" data-base62-sha1="k0Gindv5rgCz7z5DZ3K3OjhdpMm" width="685" height="414"></p>
<p>Scan order is property is changed, and when I look at the volume outside of Slicer, I see a different plane being shown in slices.</p>

---

## Post #8 by @lassoan (2019-10-14 13:52 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="8750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>behavior for interpolated cropping seems a little awkward</p>
</blockquote>
</aside>
<p>Interpolated cropping behavior changed a few years ago, when support for cropping with arbitrarily transformed ROIs was added. The original volume may be non-linearly warped and arbitrarily rotated, so in general there is no clear correspondence between the original and the cropped volume axes, while there is clear correspondence between the cropping ROI and the cropping volume axes. By implementing some heuristics that would try to find the closest match between the original and resampled cropped volume, we would introduce an ambiguity. Implementing this would take some effort and adding one more option would further complicate the GUI.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="8750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>the fields didn’t get updated in the volume information tab</p>
</blockquote>
</aside>
<p>Good catch, I’ve fixed this now.</p>

---

## Post #9 by @muratmaga (2019-10-14 16:01 UTC)

<p>Thank you for the clarification and adding padding option.</p>

---
