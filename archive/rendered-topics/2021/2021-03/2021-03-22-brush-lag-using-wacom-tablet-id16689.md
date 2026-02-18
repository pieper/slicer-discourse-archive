# Brush lag using Wacom tablet

**Topic ID**: 16689
**Date**: 2021-03-22
**URL**: https://discourse.slicer.org/t/brush-lag-using-wacom-tablet/16689

---

## Post #1 by @opetne (2021-03-22 13:34 UTC)

<p>My Wacom Intuos worked fine with the older version of Slicer (from Sept of 2020). I downloaded the latest stable version 4.11.20210226 and after starting to paint anything with the brush after the first touch the brush freezes (it makes the segment) and it follows the move after some seconds lag. Is there a solution for that?</p>

---

## Post #2 by @lassoan (2021-03-24 17:44 UTC)

<p>Most likely the stylus floods the application with events. You can probably control the behavior in your tablet settings.</p>
<p>Since we cannot reproduce this with our own hardware (touchscreen of Windows tablets work well), it may help if you could determine in which exact Slicer version between September and February the behavior has changed. You can get installers of previous Slicer versions as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">here</a>.</p>

---

## Post #3 by @opetne (2021-03-29 08:27 UTC)

<p>Dear Andras, thank you, I’ll try this</p>

---
