---
topic_id: 30740
title: "What Should I Do To Activate The List"
date: 2023-07-22
url: https://discourse.slicer.org/t/30740
---

# What should I do to activate the list?

**Topic ID**: 30740
**Date**: 2023-07-22
**URL**: https://discourse.slicer.org/t/what-should-i-do-to-activate-the-list/30740

---

## Post #1 by @telomere (2023-07-22 12:29 UTC)

<p>Hi,</p>
<ol>
<li>
<p>I want to move one model to the location of the other model using model registration in SlicerIGT module.<br>
But there’s no list in ‘Input fixed(dense) model’ and ‘input moving(sparse) model’.<br>
What should I do to make the models selectable?<br>
It says ‘This model may require to contain a dense/sparse set of points’, but I don’t get what this mean.</p>
</li>
<li>
<p>More basic question…<br>
In segment editor module, I want to import other models so turning into segmentations modules, I tried to import models in ‘Export/import models and labelmaps’ but also there’s no list in Input node.<br>
What should I do?<br>
Of course I’ve already loaded other models and the lists are shown in data module.</p>
</li>
</ol>
<p>Thanks!</p>

---

## Post #2 by @telomere (2023-07-22 14:17 UTC)

<p>Self-answer and new questions.</p>
<ol>
<li>I was working with segmentation nodes…after I changed them to models and it worked.</li>
<li>Works after making a new folder. I had to use copy/move segments tab in my situation…</li>
</ol>
<p>new questions:</p>
<ol>
<li>
<p>As you can see the pictures under…when I do margin effect in segment editor, it only works within the bound. I want to apply without any limitation. WHat should I do?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2aba992350c5bb65c87b69720144258e34e598d2.png" alt="q1" data-base62-sha1="65ZPZnuNjOA8qz1aGS0VNVHDf22" width="182" height="264"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f74157fac9aa221030bf3f537a2df21874c1e61b.png" alt="q2" data-base62-sha1="zhjVRS1k1qQ9G2hc5JO0bJd90mv" width="187" height="272"></p>
</li>
<li>
<p>In contrast, if I want to apply certain effects in segment editor at specific ROI, what should I do? I tried to make a ROI in Markups module and put it to the segment for editing but it didn’t work.</p>
</li>
</ol>

---
