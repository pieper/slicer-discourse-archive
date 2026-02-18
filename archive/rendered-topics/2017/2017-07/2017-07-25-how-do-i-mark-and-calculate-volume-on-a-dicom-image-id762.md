# How do I mark and calculate volume on a dicom image?

**Topic ID**: 762
**Date**: 2017-07-25
**URL**: https://discourse.slicer.org/t/how-do-i-mark-and-calculate-volume-on-a-dicom-image/762

---

## Post #1 by @anubhutig (2017-07-25 15:12 UTC)

<p>Hi guys<br>
I’m new to slicer.<br>
I’m a postgrad in Endodontics.<br>
Could anyone help me with a project I’m doing with CBCT?<br>
I need to mark and calculate volumes of specific objects on a dicom image.<br>
Could I please get some help with that?<br>
It’ll be a big favour!<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Thanks in advance!</p>
<p>Operating system: Win 10 64bit<br>
Slicer version: Latest<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2017-07-25 18:01 UTC)

<p>Segment your object of interests using <code>Segment editor</code> module and then compute volumes using <code>Segment statistics</code> module. Use the latest <strong>nightly</strong> version of Slicer (Slicer 4.6.2 is not suitable).</p>

---

## Post #3 by @soulrin072 (2024-09-10 04:44 UTC)

<p>Can you explain more about this<br>
I do have a dicom file &gt;&gt; MRI brain<br>
I need to calculate volume of pituitary<br>
Can you explain how to calculate it or show me the link of video or step to follow<br>
Thank you so much</p>

---

## Post #4 by @lassoan (2024-09-10 21:28 UTC)

<p>First you need to segment the pituitary. A good starting point for image segmentation is <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">this page</a>. You can then use “Segment Statistics” module to get the volume (just 1-2 clicks). You can find video tutorials for all these on youtube but you can also ask for clarification here if you get stuck at any point.</p>

---
