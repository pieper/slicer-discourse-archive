---
topic_id: 29153
title: "Set View Perpendicular To A Markup Line"
date: 2023-04-26
url: https://discourse.slicer.org/t/29153
---

# Set view perpendicular to a Markup Line

**Topic ID**: 29153
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/set-view-perpendicular-to-a-markup-line/29153

---

## Post #1 by @mahi2208 (2023-04-26 20:59 UTC)

<p>Hi,</p>
<p>I am relatively new to Slicer and not sure how to do thiis. Here is some background for what I am trying to do:</p>
<ol>
<li>I draw a line using markupsLine to depict a possible path for a neurosurgical procedure.</li>
<li>I need to be able to set the view of the camera perpendicular to the line so that after doing that, the line essentially becomes like a point and I can move through slices to see if the line is interfering with the vessels.</li>
<li>If that happens, I should be able to move the point in either direction and do the view change again to make it perpendicular to that new point and repeat the process until no vessels are hit.</li>
</ol>
<p>Please let me know if someone has faced this before and how to solve it. I am using Slicer version 4.11.20210226</p>

---

## Post #2 by @lassoan (2023-04-26 21:03 UTC)

<p>The Path Explorer module in SlicerIGT extension implements this. Its user interface is a bit clunky (you need to add target point(s) and candiate entry point(s) and then create candidate paths from them, then enable/disable driving of each slice), so if you have trouble figuring out how it works then let us know.</p>
<p>Use the most recent Slicer Stable Release. Slicer-4.11 is really old, current version has many fixes and improvements.</p>

---

## Post #3 by @mahi2208 (2023-04-28 18:19 UTC)

<p>Hi Andras,</p>
<p>Thanks for the quick reply! It worked and its exactly what I needed.</p>
<p>I will also update the Slicer version.</p>
<p>Thanks again!</p>

---
