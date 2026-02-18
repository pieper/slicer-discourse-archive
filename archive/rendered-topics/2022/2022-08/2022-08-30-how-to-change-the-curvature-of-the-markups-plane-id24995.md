# How to change the curvature of the markups plane

**Topic ID**: 24995
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/how-to-change-the-curvature-of-the-markups-plane/24995

---

## Post #1 by @1023185654 (2022-08-30 07:52 UTC)

<p>Hello, everyone. Recently, i used markups plane, Then I found out that Plan has rotation and translate functions, but i want that plane also can change the curvature and retaining the translation and rotation functions.</p>

---

## Post #2 by @lassoan (2022-08-30 20:14 UTC)

<p>What do you mean you want to change the <em>curvature</em> of a plane. Would you like to create a curved surface from a plane or just change its orientation?</p>

---

## Post #3 by @1023185654 (2022-08-31 01:52 UTC)

<p>I want to generate a plane that can interactively adjust the curvature in a 3D window, similar to markupsPlane’s rotation and translation function</p>

---

## Post #4 by @lassoan (2022-08-31 02:18 UTC)

<p>You cannot adjust a markup plane’s curvature. Do you mean adjusting the orientation?</p>

---

## Post #5 by @1023185654 (2022-08-31 02:46 UTC)

<p>I want to create a plane that can adjust the curvature, that can rotate, that can translate</p>

---

## Post #6 by @lassoan (2022-08-31 02:50 UTC)

<p>A plane has 0 curvature. You cannot adjust this curvature because then it would not be a plane anymore.</p>
<p>You can use the markup plane for displaying and interactively rotate and translate a plane node. It seems that you are already aware of this, so I’m not sure what do you need help with. Would you like to know how to add a new markup plane using Python scripting?</p>

---

## Post #7 by @1023185654 (2022-08-31 03:00 UTC)

<p>i know that, Maybe I didn’t make myself clear, Or can a curveNode be made into a rectangle shape</p>

---

## Post #8 by @lassoan (2022-08-31 03:07 UTC)

<p>If you want to fit a shape, such as a rectangle, to a point cloud then you can use an optimizer to compute the unknown parameters of the shape (for example, corners of the rectangle). See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-control-points">this example</a> for fitting a sphere to a point cloud using <code>scipy.optimize</code>.</p>

---

## Post #9 by @1023185654 (2022-08-31 03:10 UTC)

<p>Thanks for reply, lasson <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---
