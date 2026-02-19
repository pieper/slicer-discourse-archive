---
topic_id: 16668
title: "How To Capture Right Clicked"
date: 2021-03-21
url: https://discourse.slicer.org/t/16668
---

# How to capture right clicked

**Topic ID**: 16668
**Date**: 2021-03-21
**URL**: https://discourse.slicer.org/t/how-to-capture-right-clicked/16668

---

## Post #1 by @luxiaoyang9999 (2021-03-21 07:20 UTC)

<p>Hi all,<br>
I am looking to capture right clicked and create a new qt page, but I do not know how to do this.<br>
Can someone tell me a possible solution</p>

---

## Post #2 by @lassoan (2021-04-14 06:23 UTC)

<p>Usually when we implement interaction in views, we use markups: You activate place mode and add an observer to the markups node that is being placed. When the user clicks in the image then the markups node is updated and you can perform any action in the callback function.</p>
<p>You can also quite easily capture interaction events by implementing a custom Segment Editor effect, which is convenient if the user is already working on segmentation.</p>
<p>If none of these options are good enough then you need to go one level lower and add observers to the view’s render window interactor.</p>

---

## Post #3 by @luxiaoyang9999 (2021-04-20 11:59 UTC)

<p>Thank you very much.</p>

---
