---
topic_id: 36974
title: "New Feature Interactive Transformation Adjustable Center Of"
date: 2024-06-24
url: https://discourse.slicer.org/t/36974
---

# New feature: Interactive transformation + adjustable center of rotation

**Topic ID**: 36974
**Date**: 2024-06-24
**URL**: https://discourse.slicer.org/t/new-feature-interactive-transformation-adjustable-center-of-rotation/36974

---

## Post #1 by @Sunderlandkyl (2024-06-24 13:14 UTC)

<p>Any nodes can now be translated, rotated, or scaled by interactive handles.  Editing operations can be constrained to specific axes and center of rotation can be freely chosen. The handles are available both in slice and 3D views.</p>
<p>Transform nodes can be easily added and visualized for any node in 3D Slicer by right-clicking on the node in the Subject hierarchy visibility column and checking “Interaction”.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="ielxgJS-6SI" data-video-title="Transform Interaction Handles in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=ielxgJS-6SI" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/ielxgJS-6SI/maxresdefault.jpg" title="Transform Interaction Handles in 3D Slicer" width="690" height="388">
  </a>
</div>

<h1><a name="p-113161-visualization-options-1" class="anchor" href="#p-113161-visualization-options-1" aria-label="Heading link"></a>Visualization options</h1>
<p>Visualization options for interaction handle widgets can customized in 3D and Slice views to display only the relevant handles/axes in each view.</p>
<p><img src="https://github.com/Slicer/Slicer/releases/download/docs-resources/module_transforms_display_interaction.png" alt="" role="presentation" width="519" height="314"></p>
<h1><a name="p-113161-center-of-transformation-2" class="anchor" href="#p-113161-center-of-transformation-2" aria-label="Heading link"></a>Center of transformation</h1>
<p>The center of rotation/scaling can now be updated for transform nodes. To change the center of transformation hold ALT and left-click on a translation handle to adjust the center of transformation. Right clicking on a transform in 2D/3D will also display options to reset the center of transformation.</p>
<p><img src="https://github.com/Slicer/Slicer/releases/download/docs-resources/interaction_context_menu_1.png" alt="" role="presentation" width="391" height="169"></p>
<p>The center of transformation is also applied to the sliders in the Transforms module widget. Adjusting the rotation sliders will rotate the transform around the center of transformation. The center of transformation can also be changed from the Transforms module widget:</p>
<p><img src="https://github.com/Slicer/Slicer/releases/download/docs-resources/center_of_transformation.png" alt="" role="presentation" width="466" height="90"></p>
<h1><a name="p-113161-markups-3" class="anchor" href="#p-113161-markups-3" aria-label="Heading link"></a>Markups</h1>
<p>This updated interaction handle pipeline is also integrated with Markups, providing the same improved visualization for both Transforms and Markups.</p>
<h1><a name="p-113161-acknowledgements-4" class="anchor" href="#p-113161-acknowledgements-4" aria-label="Heading link"></a>Acknowledgements</h1>
<p>Development was funded in part by a Children’s Hospital of Philadelphia (CHOP) Cardiac Center Innovation Grant, a CHOP Cardiac Center Research Grant, a CHOP Frontier Grant, NIH R01 HL153166 and T32GM008562.</p>

---

## Post #2 by @philippepellerin (2024-06-26 19:29 UTC)

<p>Fantastic, it is exactly what I was waiting for. Thank you so much.</p>

---

## Post #3 by @chir.set (2024-06-26 20:28 UTC)

<p>Out of curiosity, what are the recent additions to the transform widget? The updated widget, much more intuitive from the one available in 5.6.2, seems quite old, already there in 5.7.0-2024-05-15 r32859 / 332732c for example. Has there been very recent enhancements?</p>

---

## Post #4 by @philippepellerin (2024-06-27 08:41 UTC)

<p>Sorry, may be I am doing something wrong or not doing right, but when I hold Alt, and left click, the handles move along with the node. I did not find a way to relocate the handles relatively to the node, which was what I am waiting for .<br>
I am always able to do that by manually changing the settings of the coordinates for the center of rotation, but it is a fuss</p>

---

## Post #5 by @Sunderlandkyl (2024-06-28 13:46 UTC)

<p>What platform are you using?</p>

---

## Post #6 by @Sunderlandkyl (2024-06-28 13:49 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="36974" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Out of curiosity, what are the recent additions to the transform widget? The updated widget, much more intuitive from the one available in 5.6.2, seems quite old, already there in 5.7.0-2024-05-15 r32859 / 332732c for example. Has there been very recent enhancements?</p>
</blockquote>
</aside>
<p>There have not been any significant enhancements since May.</p>
<p>There simply hadn’t been an official announcement of the feature on Discourse until this week.</p>

---

## Post #7 by @chir.set (2024-06-28 14:05 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="6" data-topic="36974">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>There simply hadn’t been an official announcement</p>
</blockquote>
</aside>
<p>Ok, that’s clear. I was just asking myself what selective recent addition I was missing.</p>

---

## Post #8 by @philippepellerin (2024-06-28 14:22 UTC)

<p>I am running the 5.7.0-2024-06-24 on a Mac Mini 2023-chip M2pro, 16GB.</p>

---

## Post #9 by @lassoan (2024-07-02 02:37 UTC)

<aside class="quote no-group" data-username="philippepellerin" data-post="4" data-topic="36974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>when I hold Alt, and left click, the handles move along with the node</p>
</blockquote>
</aside>
<p>You need to click-and-drag the center (not the arrows).</p>

---

## Post #10 by @philippepellerin (2024-07-02 06:23 UTC)

<p>It what I do, as I use to with the boxes in the old issue, but it does not operate. The handles and the node move altogether…</p>
<p>Envoyé de mon iPhone</p>

---

## Post #11 by @philippepellerin (2024-07-02 09:23 UTC)

<p>This is a screen grab. I am holding the Alt key and left click when moving the mouse on the medial white dot.</p>
<p>(Attachment Screen Recording 2024-07-02 at 11.17.38.mov is missing)</p>

---

## Post #12 by @philippepellerin (2024-07-02 10:29 UTC)

<p>I actually left-click on the white dot in the center among the handles when holding the Alt key. Hereafter I join a screengrab…</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c967b80e7f6c8c953c71e002e827d536093fb1cb.mp4">
  </div><p></p>

---

## Post #13 by @lassoan (2024-07-02 11:36 UTC)

<p>Thanks for the screen capture, it is very useful. You activated the touch and hold gesture by keeping your finger on the touchpad without moving it or clicking. Once this gesture is activated, dragging the mouse will just pan the view.</p>
<p>On other operating systems, you can click-and-drag really easily with tap-and-move, but macOS touchpad does not support this gesture, so you need to drag your finger while pressing down, which either wears down your skin or you have to learn to orchestrate a two-finger click-and-drag. On other operating systems, you also have two click areas on the touchpad, so you can do a left or right click with the touchpad. Due to all these limitations of the macOS touchpad, many mac users switch to a mouse when they use software that uses many mouse gestures. I would recommend you to do the same.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> it works be great if you could play a but with the macOS touchpad and see if you could improve the usability. Maybe we could remap tap-and-hold to click-and-drag in certain cases?</p>

---

## Post #14 by @Sunderlandkyl (2024-07-02 13:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="36974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You need to click-and-drag the center (not the arrows).</p>
</blockquote>
</aside>
<p>Holding down alt should work on the arrows as well.</p>

---

## Post #15 by @philippepellerin (2024-07-02 14:05 UTC)

<p>Thanks for your efforts in helping. I don’t use a trackpad but an Apple Magic Mouse, and I have the issue we are talking about: mouse left click on the white dot at the center of the handles and grading the mouse keep moving tha handles and the node at the same time.</p>

---

## Post #16 by @philippepellerin (2024-07-02 14:13 UTC)

<p>I found the solution. It is by using the option key instead of the Alt key, and then one can move the handles. It is very useful, and I am very happy since it was a function I expected. Thank you so much. Best regards.</p>

---

## Post #17 by @philippepellerin (2024-07-02 15:01 UTC)

<p>I believe that it would be kind to warn Mac users that they can move the center of rotation by left-clicking when holding the Option key (⌥) and dragging the handles with the mouse…</p>

---

## Post #18 by @Marta_Fernandez (2024-08-06 13:06 UTC)

<p>I have a problem despite having updated the program and everything but the interactively does not appear. Can someone tell me what is happening and why it does not appear even though I have the dicom file inserted. I need the arrows to appear so I can work with precision but there is no way. Help</p>

---

## Post #19 by @lassoan (2024-08-15 13:29 UTC)

<p>Make sure you use the latest Slicer Preview Release (not the latest Slicer Stable Release. If you still cannot activate the handles then please share a screen recording of how you are doing it (upload the video file to somewhere - dropbox/onedrive/google drive/etc. and copy the link here).</p>

---
