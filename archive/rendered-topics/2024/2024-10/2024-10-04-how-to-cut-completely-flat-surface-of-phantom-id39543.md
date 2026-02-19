---
topic_id: 39543
title: "How To Cut Completely Flat Surface Of Phantom"
date: 2024-10-04
url: https://discourse.slicer.org/t/39543
---

# How to cut completely flat surface of phantom

**Topic ID**: 39543
**Date**: 2024-10-04
**URL**: https://discourse.slicer.org/t/how-to-cut-completely-flat-surface-of-phantom/39543

---

## Post #1 by @HAN (2024-10-04 12:31 UTC)

<p>Dear all,<br>
Hello, I need some help to resolve this problem.<br>
I wanted to cut the phantom and use it to 3D printer. So, I tried to use Cut function of Segment Editor tap.<br>
But, the sample phantom below doesn’t have the completely flat surface.<br>
Currently, the bottom surface of the sample is uneven and looks like a gravel field.</p>
<p>What should I do next step…?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/957f1bc5ed10dfdaced7d470893c24e92c43ef36.png" alt="Example" data-base62-sha1="lkvtfvZ6gKCJbIStdK5Pw3RhkoK" width="622" height="162"></p>

---

## Post #2 by @ungi (2024-10-07 16:51 UTC)

<p>Hi, have you tried the Dynamic Modeler module in a recent version of Slicer? It only works with models, not segmentations. But it can cut a perfect plane.</p>

---

## Post #3 by @lassoan (2024-10-07 22:18 UTC)

<p>Segment Editor always modifies a labelmap representation of the segmentation, which can only represent details up to the resolution of this labelmap. <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">Increasing the resolution to be able to represent sufficiently smooth planes</a> would be one option to deal with this. But probably it is better to export the segmentation to model and use Dynamic Modeler as <a class="mention" href="/u/ungi">@ungi</a> suggested.</p>

---

## Post #4 by @HAN (2024-10-08 06:47 UTC)

<p>Thank you so much! The problem was fixed by Dynamic Modeler function! Thanks for your help!</p>

---
