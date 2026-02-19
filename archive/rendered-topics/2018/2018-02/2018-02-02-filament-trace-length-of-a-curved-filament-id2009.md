---
topic_id: 2009
title: "Filament Trace Length Of A Curved Filament"
date: 2018-02-02
url: https://discourse.slicer.org/t/2009
---

# Filament trace / Length of a curved filament

**Topic ID**: 2009
**Date**: 2018-02-02
**URL**: https://discourse.slicer.org/t/filament-trace-length-of-a-curved-filament/2009

---

## Post #1 by @AnFr (2018-02-02 09:56 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,<br>
I was wondering if there is a possibility/ a module with which I can calculate the actual length of a curved line /filament. As far as I’ve experienced the “ruler” tool only gives back the length of a straight line.</p>
<p>Thank you!</p>

---

## Post #2 by @AnFr (2018-02-02 12:28 UTC)

<p>I found the extension “CurveMaker” that can do this.<br>
(<a href="https://www.slicer.org/wiki/Documentation/4.8/Extensions/CurveMaker" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.8/Extensions/CurveMaker</a>)</p>
<p>However, i would like something that works with less pre-work (placing fiducials along the curve) / automatically. So if someone has an idea, it would be highly appreciated.</p>

---

## Post #3 by @Frederic (2018-02-02 12:51 UTC)

<p>Hi.<br>
I have developed a new extension of 3dslicer that make that you want. However, my institution desire first that I value it by an article.<br>
When do you want calculate your filament trace?<br>
Since then, this <a href="https://discourse.slicer.org/t/calculate-a-scalp-to-scalp-distance/1141/51">topic</a> could help you.<br>
Best.</p>

---

## Post #4 by @AnFr (2018-02-02 13:28 UTC)

<p>Thank you for the tip.<br>
I am on it right now but since that project has no priority it can wait.<br>
I can just work with CurveMaker until your extension will be released.</p>
<p>Thank you!</p>

---

## Post #5 by @lassoan (2018-02-02 13:55 UTC)

<p>If you can segment the filament (if it’s darker or lighter than it’s surroundings then simple Thresholding in Segment Editor module will do) then you can use Extract Skeleton module to create a markup list of the centerline automatically. This requires latest nightly version of Slicer, not yet in 4.8.1.</p>

---
