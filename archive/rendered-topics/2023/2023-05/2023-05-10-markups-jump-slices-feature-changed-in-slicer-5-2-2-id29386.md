---
topic_id: 29386
title: "Markups Jump Slices Feature Changed In Slicer 5 2 2"
date: 2023-05-10
url: https://discourse.slicer.org/t/29386
---

# Markups "jump slices" feature changed in Slicer-5.2.2

**Topic ID**: 29386
**Date**: 2023-05-10
**URL**: https://discourse.slicer.org/t/markups-jump-slices-feature-changed-in-slicer-5-2-2/29386

---

## Post #1 by @Tobias (2023-05-10 00:56 UTC)

<p>In my opinion there is a bug in markups in the 5.22 and a few other of the latest versions.</p>
<p>Historically if you pressed jump slices you could go between different markups and by selecting one you would automatically go the that markup. In the 5.22 version if you slected jump slices then then by just moving your pointer around the image will jump around in a completely useless way.</p>

---

## Post #2 by @lassoan (2023-05-10 01:01 UTC)

<p>“Jump slices” feature works well for me in Slicer-5.2.2:</p>
<ul>
<li>Load MRHead sample image</li>
<li>Create a markup point list</li>
<li>Add 5 control points in the green slice view</li>
<li>In Markups module, set “Jump slices” → “Offset”</li>
<li>Click on control points in the table → all slice views jump to the slice that contain the selected control point</li>
</ul>
<p>Let us know if Slicer works differently for you or describe your workflow that leads to unexpected results.</p>

---

## Post #3 by @Tobias (2023-05-14 20:38 UTC)

<p>Yes so far it works great. But if i want to add in a new markup while jump slices is active then the image jumps as seen in this video. This behavior seems to have no benefit as far as i can think of? Just not jumping around would be a lot better and is the behavior seen in earlier versions.<br>
<a href="https://drive.google.com/file/d/1UlVZaNxTY3kMW7U_iKyfIH63yYUrAddS/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1UlVZaNxTY3kMW7U_iKyfIH63yYUrAddS/view?usp=sharing</a></p>

---

## Post #4 by @Tobias (2023-07-25 07:35 UTC)

<p>I was wondering if anyone has looked at this and also thinks it is a bug or if it is just me that don´t understand.</p>

---

## Post #5 by @lassoan (2023-07-25 12:03 UTC)

<p>I think we don’t jump to new points anymore in recent Slicer Preview Releases. Please check and let us know.</p>

---

## Post #6 by @Tobias (2023-08-03 13:42 UTC)

<p>Hi.<br>
I just tested it on the release from today 5.3.0 and it has the same problem. If jump slices is on it is it does not work to put in a new marker as the image jumps around. The problem occurs when it is on centered but not when it is on offset.</p>

---

## Post #7 by @Tobias (2023-09-26 19:38 UTC)

<p>I have now tested it in 5.4 and the same problem is still there.</p>
<p>If jump slices is selected it moves alot when you try to add a new markup. I really can not think of anytime this would be useful so if it is possible to make it so that jumpslices is only active on slices that has already been put down it would make the function much better.</p>

---
