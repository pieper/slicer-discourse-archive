# Editing Mouse Wheel Zoom Preference

**Topic ID**: 28166
**Date**: 2023-03-04
**URL**: https://discourse.slicer.org/t/editing-mouse-wheel-zoom-preference/28166

---

## Post #1 by @S_Motch_Perrine (2023-03-04 14:19 UTC)

<p>I want to change the default function of my mouse wheel for Zoom. It is “backwards” to what I am used to using in other software. I looked in Application Settings, but don’t see if it’s possible to swap the wheel roll direction for zooming in and out. (i.e. I want the object to Zoom in closer when I scroll downward, but it currently is moving away.) I’m assuming this is possible to do, but I just can’t find the setting. Thank you!</p>

---

## Post #2 by @lassoan (2023-03-06 05:20 UTC)

<p>There was indeed no standard for mouse wheel scroll direction for a number of years, but in the end “mouse wheel forward zooms in” won. This direction is used in most (if not all) widely used applications, such as Word/Powerpoint/Excel, Web browsers, Adobe software, Blender, etc., and even hardcoded in the operating system (on Windows, pinch gesture on touchpad generates mousewheel events in this direction). Slicer conforms to this standard convention.</p>
<p>That said, you can map mousewheel events (and all other GUI events) to any widget event as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#make-the-3d-view-rotate-using-right-click-and-drag">these examples</a>.</p>

---

## Post #3 by @S_Motch_Perrine (2023-03-06 13:39 UTC)

<p>Thank you for the examples! That helps!</p>

---
