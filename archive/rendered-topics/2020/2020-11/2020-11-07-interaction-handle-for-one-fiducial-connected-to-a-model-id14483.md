# Interaction Handle for one Fiducial connected to a Model

**Topic ID**: 14483
**Date**: 2020-11-07
**URL**: https://discourse.slicer.org/t/interaction-handle-for-one-fiducial-connected-to-a-model/14483

---

## Post #1 by @mau_igna_06 (2020-11-07 22:07 UTC)

<p>I connected the PointModifiedEvent of a fiducial list to a function to update a transform that is applied to a model so that the model’s origin is the position of the first fiducial point on the list. In other words, I made the model follow the 1st fiducial point position.</p>
<p>I have seen the Interaction handles on the display collapsable botton of the Markups module.<br>
And I’d like to use it but only to move the 1st fiducial of the list, not all the fiducials on the list (I’d like the interaction handles to be positioned over the 1st fiducial of the list, not over the gravity center of the list). Also I’d like to use the rotation handles to rotate the model around the 1st fiducial on the list.<br>
Can all these things be done? I suspect there is signal send by the interaction handles that I could use</p>

---

## Post #2 by @lassoan (2020-11-08 05:10 UTC)

<p>We’ll add a transform widget that will support the features that you describe, probably within a few months. Until then, I would recommend to use a markups plane node to specify position/orientation using the interaction handles (you can hide the plane itself). You can get the transform corresponding to the position/orientation of the plane using <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsPlaneNode.html#aee11e275c748479d7a7232f36e291563">GetPlaneToWorldMatrix</a> method.</p>

---

## Post #3 by @mau_igna_06 (2020-11-16 22:51 UTC)

<p>It’s a good workaround but at last the interaction handles didn’t give me the fine adjustment I was looking for. So I’ll have to wait for the new widget to come</p>

---

## Post #4 by @lassoan (2020-11-16 23:19 UTC)

<p>What kind of fine adjustment were you looking for?</p>

---

## Post #5 by @mau_igna_06 (2020-11-16 23:44 UTC)

<p>I have to ask for permission to upload a video to show you Andras</p>

---

## Post #6 by @mau_igna_06 (2020-11-17 01:59 UTC)

<p>A widget like the one with arrows in the <a href="https://youtu.be/bxgalMFUhLg" rel="noopener nofollow ugc">video</a> would be great. It is good because every touch just makes a small movement to the model</p>

---

## Post #7 by @lassoan (2020-11-17 02:48 UTC)

<p>I’m not sure what of that is shown in the video looks appealing to you. Pushbuttons that make the object position small amount may be OK on a touchscreen (because it may be hard to slide the finger in gloves and the finger may also occlude the image), but it would be terrible to use with a mouse. If you mean translation/rotation along world axis (instead of object axis), we plan to have that option in the transform widget.</p>

---

## Post #8 by @mau_igna_06 (2020-11-17 13:30 UTC)

<p>Your points are very valid Andras. I forgot to mention that I found somewhat of a bug in the Interaction Handle: If you make very small movements very slowly it recoils and incorporates unacceptable errors to the intended translation/rotation. You can place a fiducial, turn on the interaction handles and recreate this bug very easely.</p>

---

## Post #9 by @mau_igna_06 (2020-11-17 21:27 UTC)

<p>Andras were you able to reproduce the bug?</p>

---

## Post #10 by @lassoan (2020-11-17 22:00 UTC)

<p>Yes, I know about this bug (markups jumps when translated using the arrows in the interaction widget), it is a minor thing but still annoying.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> do you know about this problem? I think somebody reported this before, but I could not find an issue on github. It would be nice if you could fix it. Thank you!</p>

---

## Post #11 by @Sunderlandkyl (2020-11-17 22:04 UTC)

<p>Sure, the issue tracking the bug is here: <a href="https://github.com/Slicer/Slicer/issues/5257" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/5257</a></p>

---

## Post #12 by @manjula (2021-10-24 16:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We’ll add a transform widget that will support the features that you describe, probably within a few months.</p>
</blockquote>
</aside>
<p>Is SetHandlesInteractive for Models implemented yet?</p>
<p>Is there an easier way of enabling interactive handles for models?</p>
<p>thank you</p>

---

## Post #13 by @pieper (2021-10-24 17:17 UTC)

<p>For now you could just put the model in a transform.</p>

---
