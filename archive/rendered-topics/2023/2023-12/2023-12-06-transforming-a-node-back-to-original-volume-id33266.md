---
topic_id: 33266
title: "Transforming A Node Back To Original Volume"
date: 2023-12-06
url: https://discourse.slicer.org/t/33266
---

# Transforming a node back to original volume

**Topic ID**: 33266
**Date**: 2023-12-06
**URL**: https://discourse.slicer.org/t/transforming-a-node-back-to-original-volume/33266

---

## Post #1 by @Yoyoman (2023-12-06 21:25 UTC)

<p>Sorry if this question is rather basic. Please direct me to the thread if this topic has already been covered. I did look.<br>
This is my typical workflow…I import a DICOM file then centre the volume then rotate the volume, harden it and possible reslice the volume. I am wanting to transform the model/s created (from a segmentation) using this transformed volume back to the position and rotation of the original volume.<br>
I am hoping there is an easy way to do this…<br>
Thanks</p>

---

## Post #2 by @lassoan (2023-12-06 21:27 UTC)

<p>You can “undo” a linear transformation by applying the inverse of the transform, but probably the best is not to alter the volume in the first place.</p>
<p>Why did you apply a centering transform on the volume and why did you even harden it?</p>

---

## Post #3 by @Yoyoman (2023-12-06 23:00 UTC)

<p>Hi Andras, thanks for the response. I’ve been following your instructions and tutorials for a wee while. Even though I have been using Slicer for years I’m still trying to get a good grasp on the whys and how slicer works. I like to centre volumes before rotating them so they stay on screen etc. this also puts things in a good spot for exporting to other programs. I rotate for a similar reason… basically in preparation for 3d printing where we add walls/ floors to models.<br>
The only reason I would like to transform the model back is to verify that no geometric mistakes have occurred…IE it matches the original volume data.<br>
Thanks</p>

---

## Post #4 by @lassoan (2023-12-06 23:27 UTC)

<aside class="quote no-group" data-username="Yoyoman" data-post="3" data-topic="33266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/a3d4f5/48.png" class="avatar"> Yoyoman:</div>
<blockquote>
<p>I like to centre volumes before rotating them so they stay on screen etc.</p>
</blockquote>
</aside>
<p>For this, click on the “Center view” (little crosshair) button in the view controller. You can also right-click at any point in the 3D view and choose “Refocus camera on this point” to set that point as center of rotation.</p>
<aside class="quote no-group" data-username="Yoyoman" data-post="3" data-topic="33266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/a3d4f5/48.png" class="avatar"> Yoyoman:</div>
<blockquote>
<p>this also puts things in a good spot for exporting to other programs.</p>
</blockquote>
</aside>
<p>In the DICOM file, a universally unique identifier is assigned to the coordinate system that the image is specified in. This coordinate system is used by all DICOM-compliant software. By keeping your image and all derived data in this coordinate system ensures that all your data always appears correctly in any software you are using. You would not want to sacrifice all this for some little conveniences, such as making the image appear in the center of the screen by default.</p>

---

## Post #5 by @Yoyoman (2023-12-07 01:18 UTC)

<p>Yes, I use the Centre view/ reset field of view button but if the volume is a long way from the centre of rotation “center volume” makes the rotation stay central in all the views while rotating it.<br>
I can see your point here. Unfortunately most of the tutorials and written adavice don’t mention this type of manipulation is not best practice.<br>
You’ve given me much to think about…<br>
But let’s say, for arguements sake, I still wanted to apply an inverse transform to my model, how do I do that?</p>

---

## Post #6 by @lassoan (2023-12-07 15:03 UTC)

<aside class="quote no-group" data-username="Yoyoman" data-post="5" data-topic="33266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/a3d4f5/48.png" class="avatar"> Yoyoman:</div>
<blockquote>
<p>Yes, I use the Centre view/ reset field of view button but if the volume is a long way from the centre of rotation “center volume” makes the rotation stay central in all the views while rotating it.</p>
</blockquote>
</aside>
<p>Do you mean that the issue is that you use multiple 3D views and you need to “Click center” volume in each? How many 3D views are you using? We could potentially auto-center (similarly how we reset the field of view in slice views by default when a volume is loaded) if clicking the centering button is a significant burden.</p>
<aside class="quote no-group" data-username="Yoyoman" data-post="5" data-topic="33266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/a3d4f5/48.png" class="avatar"> Yoyoman:</div>
<blockquote>
<p>I can see your point here. Unfortunately most of the tutorials and written adavice don’t mention this type of manipulation is not best practice.</p>
</blockquote>
</aside>
<p>Since centering is disabled by default and even if you enable it, the volume is not modified, only a transform is applied to it, and the feature is not advertised in tutorials and barely mentioned in the documentation, we expect that only those users perform this action who have a strong reason to use it.</p>
<p>I usually advise users to avoid this feature when it comes up (see for example <a href="https://discourse.slicer.org/t/call-center-volume-button-from-python-script/1132/4">here</a>), but of course I would not expect anyone to search until running into an issue, so probably it does not help much.</p>
<p>I’m not sure how to make users more aware of what they lose by centering a volume. We could add more information to the documentation, but I would not expect users to read the documentation before using a feature. Anyway, if you find documentation or tutorial that mentions it then let me know and I’ll add a note there. We could also consider removing the feature from the user interface (from the loading options and/or the Volumes module).</p>
<aside class="quote no-group" data-username="Yoyoman" data-post="5" data-topic="33266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/a3d4f5/48.png" class="avatar"> Yoyoman:</div>
<blockquote>
<p>But let’s say, for arguements sake, I still wanted to apply an inverse transform to my model, how do I do that?</p>
</blockquote>
</aside>
<p>You can click <code>Invert</code> in Transforms module to inverse the centering transform and apply it to the centered volume (and other derived data) to transform back to the original position.</p>

---

## Post #7 by @labixin (2025-02-01 10:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="33266">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Since centering is disabled by default and even if you enable it, the volume is not modified, only a transform is applied to it, and the feature is not advertised in tutorials and barely mentioned in the documentation, we expect that only those users perform this action who have a strong reason to use it.</p>
<p>I usually advise users to avoid this feature when it comes up (see for example <a href="https://discourse.slicer.org/t/call-center-volume-button-from-python-script/1132/4">here</a>), but of course I would not expect anyone to search until running into an issue, so probably it does not help much.</p>
<p>I’m not sure how to make users more aware of what they lose by centering a volume. We could add more information to the documentation, but I would not expect users to read the documentation before using a feature. Anyway, if you find documentation or tutorial that mentions it then let me know and I’ll add a note there. We could also consider removing the feature from the user interface (from the loading options and/or the Volumes module).</p>
</blockquote>
</aside>
<p>Hi Andras,</p>
<p>Thanks for your explanation. The reason why I need to use “center volume” button is that I can further quickly apply same transformations to different volumes for deep learning purpose. I want to confirm that if this action only means applying a linear transform to the volume and just modify the image origin (but not dimension or spacing). Is there anything else changed? Besides, are there any tutorials for more information?</p>
<p>Your help is highly appreciated!</p>
<p>Sincerely,</p>
<p>Crayon</p>

---
