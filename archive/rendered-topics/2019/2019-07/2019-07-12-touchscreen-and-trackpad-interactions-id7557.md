---
topic_id: 7557
title: "Touchscreen And Trackpad Interactions"
date: 2019-07-12
url: https://discourse.slicer.org/t/7557
---

# Touchscreen and trackpad interactions

**Topic ID**: 7557
**Date**: 2019-07-12
**URL**: https://discourse.slicer.org/t/touchscreen-and-trackpad-interactions/7557

---

## Post #1 by @Sunderlandkyl (2019-07-12 20:30 UTC)

<p>Interaction with 2D and 3D views using touchscreen and MacOS trackpad is now included in the latest nightly release.</p>
<div class="lazyYT" data-youtube-id="7lsN93iPmbg" data-youtube-title="3D Slicer - Touchscreen and trackpad interaction" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>If anyone has a chance to try them and would like to give feedback or suggestions, it would be appreciated.</p>

---

## Post #2 by @lassoan (2019-07-12 23:46 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@sunderlandkyl</a> This works really well, thank you! Could you describe the list of new gestures supported? If you describe it here then I’ll add it to the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html" rel="nofollow noopener">user interface documentation</a>.</p>
<p><strong>Note for Mac users:</strong> Mac touchpad gestures are shown from 0:39.</p>

---

## Post #3 by @chir.set (2019-07-13 13:26 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="1" data-topic="7557">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>If anyone has a chance to try them and would like to give feedback or suggestions,</p>
</blockquote>
</aside>
<p>I could not get it working on a touchpad on Linux. I used both Slicer nightly from your repository, and Slicer home built with unaltered code. The build machine has Qt 5.12.4, and the work laptop has Qt 5.13.0.</p>
<p>Commit 8f4af3d7596 states ‘<em>If slice intersection is visible</em>’. Even when slice intersection is visible, with any combination of crosshair, I could not get ‘rotate’ to work on a touchpad. I don’t have a touchscreen to test.</p>
<p>Can you elaborate on exact steps to follow ? Thanks.</p>

---

## Post #4 by @Sunderlandkyl (2019-07-13 14:29 UTC)

<p>The list of supported gestures are:</p>
<h1>Windows</h1>
<h2>Touchscreen</h2>
<ul>
<li>
<p>3D View:</p>
<ul>
<li>Pinch (2 finger pinch): Zoom the camera in and out at the pinch center</li>
<li>Rotate (2 finger rotate): Spin the camera around the pinch center</li>
<li>Pan (2+ finger translation): Translate the the camera</li>
</ul>
</li>
<li>
<p>2D View:</p>
<ul>
<li>Pinch (2 finger pinch): Zoom the slice in and out at the pinch center</li>
<li>Rotate (2 finger rotate): Rotate the slice intersection</li>
<li>Pan (2+ finger translation): Translate the slice</li>
</ul>
</li>
</ul>
<h1>MacOS</h1>
<h2>Trackpad</h2>
<ul>
<li>
<p>3D View:</p>
<ul>
<li>Pinch (2 finger pinch): Zoom the camera in and out at the pinch center</li>
<li>Rotate (2 finger rotate): Spin the camera around the pinch center</li>
<li>Pan (Long tap and move): Translate the the camera</li>
</ul>
</li>
<li>
<p>2D View:</p>
<ul>
<li>Pinch (2 finger pinch): Zoom the slice in and out at the pinch center</li>
<li>Rotate (2 finger rotate): Rotate the slice intersection</li>
<li>Pan (Long tap and move): Translate the slice</li>
</ul>
</li>
</ul>
<h1>Linux</h1>
<p>Untested.  Probably some touchpad gestures work. Touchscreen may require configuration tuning (setting environment variables, etc.).</p>

---

## Post #5 by @Sunderlandkyl (2019-07-13 14:41 UTC)

<p>The interactions only work for trackpads that recognize gestures, such as the MacOS trackpad.<br>
Other platforms (only tested windows) don’t support the use of the pinch/pan/rotate gestures with the trackpad.</p>
<p>If you have a debug build, you can try placing a breakpoint <a href="https://github.com/Kitware/VTK/blob/master/GUISupport/Qt/QVTKInteractorAdapter.cxx#L373" rel="nofollow noopener">here</a> to see if the gestures are received by Qt at all.</p>

---

## Post #6 by @lassoan (2019-07-13 15:19 UTC)

<p>Windows and Linux only supports basic multitouch gestures on the touchpad (tap, click-and-drag, zoom, scroll), and pinch/rotate/pan only supported on the touchscreen. We have not tested touchscreen on Linux, but if multitouch is supported at operating system, driver, and Qt levels, then it should work in Slicer.</p>

---

## Post #7 by @chir.set (2019-07-13 15:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="7557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Windows and Linux only supports basic multitouch gestures on the touchpad</p>
</blockquote>
</aside>
<p>I guess that’s the problem. I recompiled with Qt 5.13.0 and it does not work as expected. In 3D, only zooming works, and in 2D, only scrolling. Tested on two laptops, both running Linux/KDE. Rotating in 2D would have been useful to me. I’ll research touchpad specifics on Linux, and post here if anything interesting comes up.</p>
<p>Regards.</p>

---

## Post #8 by @lassoan (2019-07-13 16:41 UTC)

<p>Note that you can rotate slice intersections with basic gesture, too: using Ctrl+Alt+Left-click-and-drag.</p>

---

## Post #9 by @chir.set (2019-07-13 17:41 UTC)

<p>Yup, I can’t believe I missed that for so long. I usually tinker with the reformat widget for the same result. It’s just quicker and precise this way.</p>
<p>By the way, I could not find a simple and decent soulution for enhanced touchpad gestures on Linux.</p>
<p>Thank you very much for this tip.</p>

---

## Post #10 by @apparrilla (2024-05-08 21:39 UTC)

<p>Hi everyone!<br>
Is there any advance in Linux touchscreen gestures?</p>
<p>I´m trying to run 3DSlicer in a i5 all-in-one pc with touchscreen but without mouse or keyboard.<br>
2 finger zoom/drag is full functional in Slicer Views but not in 3dViews.<br>
Is there any way to fix it?</p>
<p>Thanks in advance!</p>

---
