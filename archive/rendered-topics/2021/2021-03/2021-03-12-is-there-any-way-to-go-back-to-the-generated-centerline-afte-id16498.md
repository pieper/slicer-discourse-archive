---
topic_id: 16498
title: "Is There Any Way To Go Back To The Generated Centerline Afte"
date: 2021-03-12
url: https://discourse.slicer.org/t/16498
---

# Is there any way to go back to the generated centerline after it has been modified?

**Topic ID**: 16498
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-go-back-to-the-generated-centerline-after-it-has-been-modified/16498

---

## Post #1 by @akshay_pillai (2021-03-12 16:37 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.11</p>
<p>I use the extract centerline feature to obtain a centerline for my model. Sometimes when I move my mouse over the models I click on the points in the curve by mistake and change the positions of the point. I am trying to create a button that reverts back to the previously extracted centerline. Is this possible? Also, I am trying to do get the original centerline from another module that is not extract centerline module or markups module, can this be done? and how?</p>

---

## Post #2 by @lassoan (2021-03-27 18:28 UTC)

<p>There is no undo for markups modifications. We will implement this at some point, but for now you need to lock the control points (or the entire markups node) to prevent accidental modifications. You can of course also choose to just save the scene or create clones of your markups nodes more frequently so that you can go back to the previous version if something is accidentally changed.</p>

---
