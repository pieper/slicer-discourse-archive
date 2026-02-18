# UI problems: menu bar cut off, mouse click offset

**Topic ID**: 5179
**Date**: 2018-12-23
**URL**: https://discourse.slicer.org/t/ui-problems-menu-bar-cut-off-mouse-click-offset/5179

---

## Post #1 by @brookman (2018-12-23 18:38 UTC)

<p>Hello everyone</p>
<p>I’m using 3D Slicer on Windows 10 Enterprise (10.0.17763 Build 17763) and have a problem with the UI:<br>
The menu bar in the main window is missing and some of the icons are cut off. But the main problem is that all mouse clicks have an offset of maybe 50 pixels. This means that I have to click below a UI element to actually hit them.<br>
Screenshot: <a href="https://i.imgur.com/mm3FhNL.png" rel="nofollow noopener">https://i.imgur.com/mm3FhNL.png</a></p>

---

## Post #2 by @lassoan (2018-12-23 18:42 UTC)

<p>Intel has released a faulty driver some time ago and you have that version installed on your computer. The easiest fix is to update your display driver.</p>
<p>You can find some more information on the issue in this topic: <a href="https://discourse.slicer.org/t/missing-menu-items-from-slicer-application-main-window/2613" class="inline-onebox">Missing menu items from Slicer Application Main Window</a></p>

---

## Post #3 by @brookman (2018-12-23 22:16 UTC)

<p>Thank you for the hint.<br>
Assigning the it the NVidia GPU in the driver settings fixed the problem: <a href="https://i.imgur.com/i1jzBPB.png" rel="nofollow noopener">https://i.imgur.com/i1jzBPB.png</a></p>
<p>Thanks again!</p>

---

## Post #4 by @lassoan (2018-12-23 22:39 UTC)

<p>Thanks for the update. It is a good idea to assign the NVidia GPU to Slicer, as it makes volume rendering and display of large models much faster. Other applications have issues with the faulty Intel driver, too, so I would recommend to update your display driver anyway.</p>

---
