---
topic_id: 15611
title: "Draw Tube Cannot Be Used Normally"
date: 2021-01-21
url: https://discourse.slicer.org/t/15611
---

# Draw Tube cannot be used normally

**Topic ID**: 15611
**Date**: 2021-01-21
**URL**: https://discourse.slicer.org/t/draw-tube-cannot-be-used-normally/15611

---

## Post #1 by @slicer365 (2021-01-21 09:11 UTC)

<p>My friends have installed extension plug-ins. When they use the Draw tube function in segment editor, the arrow is always gray and cannot be used. The software is version 4.1120200930.! This is my software picture ,it is normal.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0522bb3af2493a5ac446f96e0116ce917c84bce.jpeg" data-download-href="/uploads/short-url/mSgrBnl016HAxqNKN3PuwPECxCC.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0522bb3af2493a5ac446f96e0116ce917c84bce_2_517x282.jpeg" alt="捕获" data-base62-sha1="mSgrBnl016HAxqNKN3PuwPECxCC" width="517" height="282" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0522bb3af2493a5ac446f96e0116ce917c84bce_2_517x282.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0522bb3af2493a5ac446f96e0116ce917c84bce.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0522bb3af2493a5ac446f96e0116ce917c84bce.jpeg 2x" data-dominant-color="EBECEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">758×415 68.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-01-21 16:02 UTC)

<p>Do you see any errors in the application log? (menu: Help / Report a bug)</p>

---

## Post #4 by @cyufu (2021-01-22 08:00 UTC)

<p>MarkupsToModel is not installed correctly.</p>

---

## Post #5 by @Hamid (2021-04-15 15:25 UTC)

<p>which extension should I install to have “Draw tube” module? Thanks</p>

---

## Post #6 by @cpinter (2021-04-15 16:05 UTC)

<p>SegmentEditorExtraEffects</p>

---

## Post #7 by @Hamid (2021-04-15 16:21 UTC)

<p>Thanks alot cpinter!<br>
Is this the efficient tool for creating the curve tube? I tried to make a tube but it seems the outer wall is not smooth!(Hexa or somthing like that)</p>

---

## Post #8 by @lassoan (2021-05-02 13:25 UTC)

<p>The tube is represented as a binary labelmap during segmentation editing. You can specify any resolution that your computer can handle.</p>
<p>If you want to represent curves as mesh then you can use curves Markups module.</p>

---
