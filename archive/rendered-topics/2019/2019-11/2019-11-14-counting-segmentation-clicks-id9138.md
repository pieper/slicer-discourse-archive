---
topic_id: 9138
title: "Counting Segmentation Clicks"
date: 2019-11-14
url: https://discourse.slicer.org/t/9138
---

# Counting segmentation clicks

**Topic ID**: 9138
**Date**: 2019-11-14
**URL**: https://discourse.slicer.org/t/counting-segmentation-clicks/9138

---

## Post #1 by @conrad (2019-11-14 00:25 UTC)

<p>I’m trying to count the number of clicks required to complete a segmentation in segment editor as a rough measure of difficulty. It doesn’t matter to me which segmentation tool is being used, but I would want to only track clicks that are made in the viewing window (so that would exclude clicks for changing segmentation tools or adjusting brush sizes, etc).</p>
<p>If I can just keep track of every time that a segment editor node changes size that should do the trick. It seems like it should be easy to implement, but I don’t know where start.</p>

---

## Post #2 by @lassoan (2019-11-14 01:18 UTC)

<p>We have a module that collects statistics about which modules and features are used, and in particular detailed information about segment editor operations. It saves user information, list of operations, duration, idle times, computation times, etc. in a csv file and it can also take screenshots to better document the procedure.</p>
<p>The module will be available in “Sandbox” extension for Slicer Preview Releases downloaded tomorrow or later.</p>
<p>It would be great to get feedback and suggestions about the module.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #3 by @conrad (2019-11-14 12:52 UTC)

<p>It sounds exactly like what I need and more. I’ll keep an eye out for the release.</p>

---
