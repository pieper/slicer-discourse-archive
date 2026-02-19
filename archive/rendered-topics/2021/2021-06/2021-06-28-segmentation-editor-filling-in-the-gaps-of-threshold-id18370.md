---
topic_id: 18370
title: "Segmentation Editor Filling In The Gaps Of Threshold"
date: 2021-06-28
url: https://discourse.slicer.org/t/18370
---

# Segmentation editor: Filling in the gaps of Threshold

**Topic ID**: 18370
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/segmentation-editor-filling-in-the-gaps-of-threshold/18370

---

## Post #1 by @reddington.15 (2021-06-28 13:30 UTC)

<p>Hello,<br>
I am working on isolating the pelvis from the body and it is taking me some time, so I was curious if there was a faster way in filling in the gaps in each slice of the CT scan after thresholding. I am manually going through slice by slice of the pelvis and using the paint tool to shade in the parts that thresholding didn’t get. However, I feel like this is too time consuming and there has to be an easier way.<br>
I hope my question makes sense and that I hear back soon.</p>
<p>Thanks,<br>
Jordan</p>

---

## Post #2 by @lassoan (2021-06-28 14:17 UTC)

<p><a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify">SurfaceWrapSolidify extenstion</a> is developed for exactly this purpose. Let us know if you need any help with it.</p>

---

## Post #3 by @reddington.15 (2021-06-28 14:29 UTC)

<p>Hi Andras,</p>
<p>I actually did see this when I was doing research on how to solve this problem. I already have that extension downloaded and when I tried using it I could only create a shell. Is there a way to fill the shell in so that it is solid all the way through and not hollow?</p>
<p>Thank you,<br>
Jordan</p>

---

## Post #4 by @lassoan (2021-06-28 14:40 UTC)

<p>Unless you choose the “Create shell” option, the module generates a solid object.</p>
<p>If the tool does not do what you expect then it would be great if you could attach a screenshot and mark where you expect to see something different.</p>

---

## Post #5 by @reddington.15 (2021-06-28 15:33 UTC)

<p>I just figured it out!</p>
<p>Thank you so much for your help.</p>

---
