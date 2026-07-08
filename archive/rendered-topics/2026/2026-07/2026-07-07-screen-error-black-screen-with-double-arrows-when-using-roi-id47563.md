---
topic_id: 47563
title: "Screen error - Black screen with double arrows when using ROI in Volume Rendering"
date: 2026-07-07
url: https://discourse.slicer.org/t/47563
last_bumped: 2026-07-07T17:03:53.852Z
---

# Screen error - Black screen with double arrows when using ROI in Volume Rendering

**Topic ID**: 47563
**Date**: 2026-07-07
**URL**: https://discourse.slicer.org/t/screen-error-black-screen-with-double-arrows-when-using-roi-in-volume-rendering/47563

---

## Post #1 by @Jknaub (2026-07-07 15:47 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.8.1, 5.10,  and 5.12<br>
Expected behavior: Moving ROI bounding box during volume rendering<br>
Actual behavior: The entire screen changes to a black background with double arrows.</p>
<p>Hi all,</p>
<p>I have a student using 3D Slicer that’s run into an issue when using the ROI in Volume Rendering. Video of the behavior is here - <a href="https://fau-my.sharepoint.com/:v:/g/personal/jknaub2020_fau_edu/IQB1U6aI5bH7QbzmKs3caQ1pATs-06yeC9AtkyW0L56z-m8?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&amp;e=Ue8JE1" rel="noopener nofollow ugc">3D Slicer Error.mp4</a></p>
<p>This is only occuring when the ROI is toggled on. When it’s off, it works normally. I had her restart 3D slicer, she was able to replicate this issue with 5.8.1, 5.10, and 5.12. She uninstalled and reinstalled SlicerMorph as well. She was able to replicate this on two different PCs (same model as eachother - Dell Pro Max Tower T2, Intel Core Ultra 9, NVIDIA RTX 6000 ADA, 128GB RAM). I had her load in her scan at half resolution and she had the same issue. She tried both CPU and GPU rendering and still had this screen pop-up. Any idea what’s going on/how to fix?</p>
<p>Many thanks in advance!!!</p>
<p>-Jamie</p>

---

## Post #2 by @Sam_Horvath (2026-07-07 15:53 UTC)

<p>You likely need to update the NVIDIA driver.  See this post: <a href="https://discourse.slicer.org/t/adding-landmarks-using-point-list-results-in-screen-glitches/47173/3" class="inline-onebox">Adding landmarks using Point List results in screen glitches - #3 by jamesobutler</a></p>

---

## Post #3 by @Jknaub (2026-07-07 17:03 UTC)

<p>Thank you!! I will try that!</p>

---
