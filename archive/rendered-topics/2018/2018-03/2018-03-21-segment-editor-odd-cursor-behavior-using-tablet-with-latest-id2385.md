---
topic_id: 2385
title: "Segment Editor Odd Cursor Behavior Using Tablet With Latest"
date: 2018-03-21
url: https://discourse.slicer.org/t/2385
---

# Segment Editor - Odd cursor behavior using tablet with latest nightly builds

**Topic ID**: 2385
**Date**: 2018-03-21
**URL**: https://discourse.slicer.org/t/segment-editor-odd-cursor-behavior-using-tablet-with-latest-nightly-builds/2385

---

## Post #1 by @hherhold (2018-03-21 12:06 UTC)

<p>Hey guys,</p>
<p>In the March 18 nightly build, I noticed some odd behavior when using my wacom tablet with the Segment Editor. If I select the paint tool and move the tool around with my mouse, the circle that represents the paintbrush moves around. If I use my pen/tablet and move the cursor around without touching the tablet to paint, the cursor moves around but there is no circle to show the paintbrush. When I touch down and paint with the pen, the circle shows up immediately and painting works fine. (Hopefully this explanation is clear…)</p>
<p>Any ideas? I’ve updated my tablet drivers. It is a Wacom Intuos Pro (Medium), MacOS 10.12.6.</p>
<p>I don’t remember having this issue a week or so ago. If someone can point me to how to get previous daily builds, I can try to narrow down when it started happening - I don’t remember how to download a nightly from say a week or two ago.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2018-03-21 13:08 UTC)

<p>Can you double-check if the behavior is different with an older version of Slicer? You can download older versions using the “offset” parameter as described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F</a></p>
<p>I don’t think we’ve changed anything related to this in the past several months. There might have been a change in how the tablet simulates mouse events. Maybe there are settings that you can adjust (maybe you need to activate a “mouse mode” where pen generates regular mouse events).</p>

---

## Post #3 by @hherhold (2018-03-21 17:39 UTC)

<p>Thanks for the download link - I knew it was in there somewhere.</p>
<p>It works properly with 1/23, fails with 2/26. Narrowing the window down now (lots of downloading). I haven’t changed any settings on my tablet, but I did try mouse vs tablet mode and there’s no difference.</p>
<p>Thanks, and I will keep you updated.</p>
<p>-Hollister</p>

---

## Post #4 by @cpinter (2018-03-21 18:20 UTC)

<p>Probably this came with Qt5 then. Not sure if we can do anything, because it is a change on a very low level.</p>

---

## Post #5 by @hherhold (2018-03-21 18:32 UTC)

<p>OK. Do you think it’s a Qt or a VTK thing?</p>

---

## Post #6 by @lassoan (2018-03-21 18:40 UTC)

<p>This is a Qt bug: <a href="https://bugreports.qt.io/browse/QTBUG-65559">https://bugreports.qt.io/browse/QTBUG-65559</a>. It is categorized to be quite low priority, so probably won’t be fixed anytime soon. You can use this workaround: hover the pen over tablet when application is started.</p>

---

## Post #7 by @hherhold (2018-03-21 18:43 UTC)

<p>Hey, thanks Andras! Good find, and thanks for the workaround!</p>
<p>You guys are awesome!</p>
<p>-Hollister</p>

---
