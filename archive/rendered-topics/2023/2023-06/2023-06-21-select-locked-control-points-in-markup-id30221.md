# Select locked control points in markup

**Topic ID**: 30221
**Date**: 2023-06-21
**URL**: https://discourse.slicer.org/t/select-locked-control-points-in-markup/30221

---

## Post #1 by @Saima (2023-06-21 01:56 UTC)

<p>Yes the problem is solved but there is another problem now.</p>
<p>The user will click any of the control point. Before the user selects any control point the model position is moved to get the location to select the control point. In doing so the control points can get selected and moved from their original position.</p>
<p>I do not want the control points to move while the user is moving the model to locate the location on the model for which it will select the control points on the model.</p>
<p>Is there a way to lock and still select the control points so its position doesn’t move while moving the model.</p>
<p>thanks</p>
<p>regards,<br>
saima</p>

---

## Post #2 by @lassoan (2023-06-25 12:17 UTC)

<p>You can interact with a markup control point if you keep the node unlocked.</p>
<p>If you want to lock the <em>position</em> of control points by locking them. If you lock every control point but not lock the node then you can interact with any control point but cannot accidentally move it.</p>

---

## Post #3 by @Saima (2023-07-11 02:34 UTC)

<p>Hi Andras,<br>
Could you please refer me to the code snippet to lock the control points rather then the markupnode?</p>
<p>regards,<br>
Saima</p>

---

## Post #4 by @Saima (2023-07-11 07:58 UTC)

<p>markupnode.SetNthControlPointLocked(fid_no, True)</p>
<p>got this.</p>
<p>thanks</p>

---

## Post #5 by @Saima (2023-07-11 08:02 UTC)

<p>once the control points are locked as they are created. are they still locked when loading them in another application.</p>
<p>regards,<br>
Saima</p>

---

## Post #6 by @lassoan (2023-07-11 13:40 UTC)

<p>I’m not sure why you are asking this and what other application you mean. I would recommend to try it and if the behavior is not what you need then try to solve it. If you need help with that (e.g., you cannot solve by yourself within a half day) then you can ask here for help. You need to describ your high-level goal, and specifically what you did, what you expected to happen, and what happened instead.</p>

---

## Post #7 by @Saima (2023-07-13 05:29 UTC)

<p>Hi Andras,<br>
I created control pointsand locked them as they are created. When I reopen these control points there state of being locked remain unchanged which I wanted.</p>
<p>Thanks</p>
<p>regards,<br>
Saima</p>

---

## Post #8 by @muratmaga (2023-07-13 13:41 UTC)

<p>They would remain locked when you reload them:</p>
<ol>
<li>If you saved them as JSON (I am not sure the legacy fcsv supports locked states)</li>
<li>reload them into Slicer (we cannot be sure what other applications would do).</li>
</ol>

---
