---
topic_id: 28281
title: "Transformation Questions Reset Plane Angle When Adjust Anoth"
date: 2023-03-10
url: https://discourse.slicer.org/t/28281
---

# Transformation questions, reset plane angle when adjust another one[possible bug]

**Topic ID**: 28281
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/transformation-questions-reset-plane-angle-when-adjust-another-one-possible-bug/28281

---

## Post #1 by @Young_Wang (2023-03-10 15:15 UTC)

<p>Hi there,</p>
<p>I just downloaded the Slicer 5.2.2 r31382 / fb46bd1 for mac. I noticed now if I apply the transformation to a volume. It only allows adjusting one plane at a time instead of multiple planes at the same time as before. I wonder if this is a new feature or a potential bug.</p>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2023-03-10 15:20 UTC)

<p>Is this regarding rotation? See the below note which has been in the documentation for awhile, but wasn’t appropriately being enforced and in Slicer 5.2.2 is now being enforced.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#edit" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#edit</a></p>
<blockquote>
<ul>
<li>Note: Linear transform edit sliders only show relative translation and rotation because a transformation can be achieved using many different series of transforms. To make this clear to users, only one transform slider can be non-zero at a time (all previously modified sliders are reset to 0 when a slider is moved). The only exception is translation sliders in “translate first” mode (i.e., when translation in global/local coordinate system button is not depressed): in this case there is a only one way how a specific translation can be achieved, therefore transform sliders are not reset to 0. An rotating dial widget would be a more appropriate visual representation of the behavior than sliders, but slider is chosen because it is a standard widget and users are already familiar with it.</li>
</ul>
</blockquote>

---

## Post #3 by @Young_Wang (2023-03-10 15:22 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thank you for the clarification!</p>

---

## Post #4 by @Young_Wang (2023-03-10 15:23 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> following the topic on the translation I wonder if the development team is considering adding the feature where user could specify the step size in the translation used.</p>

---

## Post #5 by @jamesobutler (2023-03-10 15:30 UTC)

<p>Most spinboxes don’t have a UI control for the <a href="https://doc.qt.io/qt-5/qspinbox.html#singleStep-prop" rel="noopener nofollow ugc">singleStep</a> property. There could be a possibility of a change that works best in most cases or having it be dynamic based on some other property.</p>
<p>Of course you can also utilize the python console to grab the spinbox of interest and set the singleStep to your desired value.</p>

---

## Post #6 by @jamesobutler (2023-03-10 15:31 UTC)

<p>There is also the <a href="https://doc.qt.io/qt-5/qabstractspinbox.html#accelerated-prop" rel="noopener nofollow ugc">accelerated</a> property where holding down the increment will then speed up so that it increases/decreases faster.</p>

---

## Post #7 by @lassoan (2023-03-21 02:26 UTC)



---
