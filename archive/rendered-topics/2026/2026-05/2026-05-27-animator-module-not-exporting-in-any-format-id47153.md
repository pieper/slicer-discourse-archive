---
topic_id: 47153
title: "Animator module not exporting in any format"
date: 2026-05-27
url: https://discourse.slicer.org/t/47153
last_bumped: 2026-05-27T16:13:30.895Z
---

# Animator module not exporting in any format

**Topic ID**: 47153
**Date**: 2026-05-27
**URL**: https://discourse.slicer.org/t/animator-module-not-exporting-in-any-format/47153

---

## Post #1 by @Atticus (2026-05-27 15:01 UTC)

<p>I have used the Animator module in the past to produce short animations of volumes rotating, being cropped to ROIs or changing their colors.</p>
<p>I have not been able to export animations today, in any format or resolution, of the same type of animations. The rendering process seems to reach the end of the animation time (either 3 or 5 seconds) and then the render window remains open and nothing happens afterwards. I have tried reinstalling Slicermorph, saving as different file types, saving low res versions and nothing.</p>
<p>Currently running 3DSlicer 5.10.0, Slicermorph updated, on Win11 with RTX 4070</p>
<p>Any advise?</p>

---

## Post #2 by @pieper (2026-05-27 15:52 UTC)

<p>Can you look in the error log (under the Help menu, Report a Bug dialog) to see if there are any messages when the animation stops.  Also look in the python console for any messages.</p>

---

## Post #3 by @muratmaga (2026-05-27 16:13 UTC)

<p>There hasn’t been any change to the Animator in the stable branch for last three years. Given your description, I suspect your system is having a hard time locating the ffmpeg library to do the conversion to mp4.</p>
<p>Have you changed your computer? If so, you need to install ffmpeg. It is an external library needed to create the mp4s.</p>

---
