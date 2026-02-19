---
topic_id: 43652
title: "General Registration"
date: 2025-07-08
url: https://discourse.slicer.org/t/43652
---

# general registration

**Topic ID**: 43652
**Date**: 2025-07-08
**URL**: https://discourse.slicer.org/t/general-registration/43652

---

## Post #1 by @Luca_Ciani (2025-07-08 12:46 UTC)

<p>good evening,</p>
<p>i’d like to ask the reason why my microct scans can’t be seen in the general registration!<br>
I load the bitmap file series as a volume, but when I want to register them they don’t exist in the fixed image volume and moving image volume</p>

---

## Post #2 by @pieper (2025-07-08 21:34 UTC)

<p>Please try to reproduce with sample data and inspect what’s different about your data.  You say bitmap so I’m guessing maybe they loaded from png or something and are vector (RGB)  volumes.  There’s a vector to scalar converter module to fix that.</p>

---

## Post #3 by @muratmaga (2025-07-09 01:21 UTC)

<aside class="quote no-group" data-username="Luca_Ciani" data-post="1" data-topic="43652">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/luca_ciani/48/80578_2.png" class="avatar"> Luca_Ciani:</div>
<blockquote>
<p>microct scans can’t be seen in the general registration!<br>
I load the bitmap file series as a volume,</p>
</blockquote>
</aside>
<p>If you use <code>ImageStacks</code> module in SlicerMorph extension, you will avoid that issue.</p>

---
