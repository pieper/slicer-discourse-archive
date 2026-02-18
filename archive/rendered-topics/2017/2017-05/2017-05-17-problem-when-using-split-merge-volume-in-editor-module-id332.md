# Problem when using "Split Merge Volume" in "Editor" module

**Topic ID**: 332
**Date**: 2017-05-17
**URL**: https://discourse.slicer.org/t/problem-when-using-split-merge-volume-in-editor-module/332

---

## Post #1 by @brhoom (2017-05-17 12:11 UTC)

<p>Dear all,<br>
Here is what I did:</p>
<ul>
<li>I segmented different objects with different colors of an image manually using Editor module.</li>
<li>I used Split Merge Volume to get these objects separated then I saved them in different files.</li>
<li>I closed Slicer, opened it and loaded the original image and one of these parts.<br>
I noticed in Pre-Structured the color is changed to black and when I try to make a model using Merge and Build Slicer crashed.<br>
What did I do wrong?<br>
Thanks !<br>
Ibraheem</li>
</ul>

---

## Post #2 by @lassoan (2017-05-17 12:25 UTC)

<p>Switch to the Segment editor module (in the latest nightly build). You can manage separate segments very easily and it has much more and more capable effects than then old Editor module.</p>

---

## Post #3 by @brhoom (2017-05-17 12:58 UTC)

<p>Thanks for the suggestion. I like the editor because of its simplicity. The “Segment Editor” works with segmentations and does not support labels. It would be nice if you add an option to convert the label  e.g. In Segmentation Selector, one can load the label and it converted to segmentation.</p>

---

## Post #4 by @brhoom (2017-05-17 13:12 UTC)

<p>Aaaaand how can I save the created surface?</p>

---

## Post #5 by @cpinter (2017-05-17 13:29 UTC)

<p>Segmentation nodes are suprerior to labelmaps in many ways, see<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations</a><br>
Here you can also find info about how to export it to labelmaps. Besides what you read there, you can also do that with fewer clicks in the Data module (Subject hierarchy tree) by right-clicking the segmentation. I’ll add this info to the page now.</p>

---

## Post #6 by @cpinter (2017-05-17 13:37 UTC)

<p>I updated the page for your convenience</p>

---

## Post #7 by @brhoom (2017-05-17 13:50 UTC)

<p>Thanks a lot, I will try it soon.</p>

---
