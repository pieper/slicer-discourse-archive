---
topic_id: 11091
title: "Bug In Transforms Module"
date: 2020-04-13
url: https://discourse.slicer.org/t/11091
---

# Bug in Transforms module

**Topic ID**: 11091
**Date**: 2020-04-13
**URL**: https://discourse.slicer.org/t/bug-in-transforms-module/11091

---

## Post #1 by @giovform (2020-04-13 01:29 UTC)

<p>When changing (on this order) translation, rotation, and translation again, for a volume, the rotation slider is reset to 0, but the rotation is still in effect (the rotation matrix is not reset).</p>
<p>Steps:</p>
<ul>
<li>Load a volume;</li>
<li>Go to the Transforms module;</li>
<li>Create a linear transform;</li>
<li>Set the volume to be transformed;</li>
<li>Change IS translation (for example);</li>
<li>Change IS rotation;</li>
<li>Change IS translation again;</li>
</ul>
<p>Then notice that the rotation slider is reset to zero, but the volume is still rotated, as is indicated in the transformation matrix as well.</p>
<p>Tested on the currently latest preview release 4.11.0-2020-04-10 r28945 / ea94099 for Windows.</p>

---

## Post #2 by @lassoan (2020-04-13 01:51 UTC)

<p>Thanks for letting us know. This is the intended behavior - only one slider can be at non-zero position at a time (with only one exception). See explanation in Transform’s module documentation’s <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_editing_and_application">Transform editing and application</a> section. Let us know if something is not clear.</p>

---

## Post #3 by @giovform (2020-04-13 01:54 UTC)

<p>Hi Andras, sure, I am ok with that, but the fact that only the slider is reset to zero and not the transformation related to it, seems strange for me. We lost track of how much we rotated.</p>

---

## Post #4 by @lassoan (2020-04-13 02:17 UTC)

<aside class="quote no-group" data-username="giovform" data-post="3" data-topic="11091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>We lost track of how much we rotated.</p>
</blockquote>
</aside>
<p>That’s exactly the point. Depending on what order you moved the sliders and how much, you end up with completely different transformations, so if we did not reset the sliders then users might think that there is a one-to-one correspondence between the slider values and the current transformation matrix. We could choose a particular parametrization of orientation (such as Euler angles), but it would only work intuitively for up to a few ten degrees of rotation and we would run into gimbal lock problems when approaching 90deg rotations and ambiguities when exceeding 90deg rotations.</p>
<p>You can always add rotation sliders with arbitrary behavior to your module if that is more appropriate for a particular workflow.</p>

---
