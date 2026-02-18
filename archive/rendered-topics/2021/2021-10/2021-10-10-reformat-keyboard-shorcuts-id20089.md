# Reformat keyboard shorcuts?

**Topic ID**: 20089
**Date**: 2021-10-10
**URL**: https://discourse.slicer.org/t/reformat-keyboard-shorcuts/20089

---

## Post #1 by @sronen71 (2021-10-10 22:39 UTC)

<p>Hi,<br>
I know we can obtain oblique views via the reformat widget in a slice view.<br>
Clicking the reformat widget tool shows an arrow on the 3D view that can be dragged by mouse.<br>
Are there keyboard shortcuts for this process?<br>
I have a vague recollection of using a shortcut for this purpose but I’m not sure.<br>
I could not find in the documentation.<br>
Thanks!<br>
Shai</p>

---

## Post #2 by @lassoan (2021-10-11 00:00 UTC)

<p>You can reformat slice views in a much more precise and user-friendly way using Ctrl + Alt + Left-click-and-drag. You need to show slice intersections for this to work (because slices are rotated around the intersection point position).</p>
<p>Slice intersections will be interactive within a few months - you will be able to drag-and-drop them to translate and rotate slice views.</p>

---

## Post #3 by @sronen71 (2021-10-12 02:13 UTC)

<p>That’s awesome. Thank you very much!<br>
Is it in documentation though…?</p>

---

## Post #4 by @lassoan (2021-10-12 13:44 UTC)

<aside class="quote no-group" data-username="sronen71" data-post="3" data-topic="20089">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sronen71/48/12646_2.png" class="avatar"> sronen71:</div>
<blockquote>
<p>Is it in documentation though…?</p>
</blockquote>
</aside>
<p>Yes, of course: <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views</a></p>
<p>Let us know if you have any suggestions how to make it easier to find.</p>

---

## Post #5 by @sronen71 (2021-10-12 21:06 UTC)

<p>Ah, good.<br>
Slicer 3d  shows some shortcuts under help menu.<br>
There is “More” tab, but in Slicer 4.11 it is broken. It brings up a page that is empty:<br>
Documentation/4.11/SlicerApplication/MouseandKeyboardShortcuts</p>

---

## Post #6 by @lassoan (2021-10-13 02:57 UTC)

<aside class="quote no-group" data-username="sronen71" data-post="5" data-topic="20089">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sronen71/48/12646_2.png" class="avatar"> sronen71:</div>
<blockquote>
<p>There is “More” tab, but in Slicer 4.11 it is broken. It brings up a page that is empty:<br>
Documentation/4.11/SlicerApplication/MouseandKeyboardShortcuts</p>
</blockquote>
</aside>
<p>Thanks for the feedback. We have upgraded our servers and the links work in Slicer Preview Release but may not be up-to-date anymore in earlier Slicer versions.</p>

---
