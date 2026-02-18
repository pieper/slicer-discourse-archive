# Request: move one control point menu item

**Topic ID**: 34578
**Date**: 2024-02-27
**URL**: https://discourse.slicer.org/t/request-move-one-control-point-menu-item/34578

---

## Post #1 by @chir.set (2024-02-27 21:32 UTC)

<p>Hi,</p>
<p>In the context menu of control points, the ‘Delete control point’ and ‘Delete &lt;Markup&gt;’ items are one after the other. It happened (rarely though) that the markups node gets accidentally deleted while deleting one point, just a wrong mouse position in a haste.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d9715307296b9f41de487bb43c5c411934b439c.png" alt="Menu_item_ordering" data-base62-sha1="mu6EGrEzsMLzA1ZUHvieH1AiioQ" width="319" height="350"></p>
<p>Would core devs consider moving the ‘Delete control point’ item upwards? Perhaps after ‘Rename control point’.</p>
<p>Thanks for considering and regards.</p>

---

## Post #2 by @muratmaga (2024-02-27 23:20 UTC)

<p>+1.</p>
<p>It happened to me more than once.</p>

---

## Post #4 by @lassoan (2024-02-28 05:11 UTC)

<p>Probably enabling undo/redo is the right solution for this. You can enable undo/redo by copy-pasting <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/UndoRedo/">this code snippet</a> to your Python console (or add it to your startup script to always enable).</p>

---

## Post #5 by @muratmaga (2024-02-28 05:52 UTC)

<p>We incorporated that into SlicerMorph as an option. It is ok for recovering deleted control points, but it creates weird issues when you are recovering a node.</p>

---

## Post #6 by @lassoan (2024-02-28 13:38 UTC)

<p>Scene undo/redo for the node types listed in the code snippet should work well. Please report any issues that you find.</p>

---

## Post #7 by @chir.set (2024-02-28 14:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="34578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Scene undo/redo for the node types listed in the code snippet should work well.</p>
</blockquote>
</aside>
<p>It works well indeed, even to recover a deleted node.</p>
<p>One last thing, could you point to a code snippet to move a newly created toolbar to the first row?</p>
<p>Thank you.</p>

---

## Post #8 by @lassoan (2024-02-28 15:28 UTC)

<p>I don’t think you can specify where the toolbar is added, but if you move the toolbar manually then the same position will be restored after you restart the application - if “Save user interface…” option is enabled (in Application settings / Appearance).</p>

---

## Post #9 by @chir.set (2024-02-28 15:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="34578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>if “Save user interface…” option is enabled</p>
</blockquote>
</aside>
<p>This option is already activated in settings. My custom toolbar gets always created in second row and I move it up every time. I can just add the icons of the Undo/Redo code snippet in my custom toolbar, so that I don’t have 2 of them to move. This is very useful. <img src="https://emoji.discourse-cdn.com/twitter/+1/3.png?v=12" title=":+1:t3:" class="emoji" alt=":+1:t3:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @muratmaga (2024-02-28 16:23 UTC)

<p>I think measurements being blocked bug has not been addressed yet. <a href="https://github.com/Slicer/Slicer/issues/7239" class="inline-onebox">Adding a default Markups node to scene removes measurements · Issue #7239 · Slicer/Slicer · GitHub</a></p>
<p>Also, try creating a pointlist with 3-4 points. Delete the node, recover, and repeat the operation a few times (undo/redo), notice that one by one the points start to disappear from the list.</p>
<p>I also noticed a case where the node was removed from the scene by right click delete scene and yet the points remained visible in the 3D viewer. I can’t remember the sequence this was generated from. I will try to replicate…</p>
<p>But it is such a critical features, I think we should harden and incorporate into the core, as opposed to keeping at a snippet.</p>

---

## Post #11 by @chir.set (2024-02-28 16:56 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="34578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>repeat the operation a few times (undo/redo), notice that one by one the points start to disappear from the list.</p>
</blockquote>
</aside>
<p>On repeat Undo/Redo after removing a fiducial node with 3 points, I do not see the points disappearing.</p>
<p>I noticed something else:</p>
<ul>
<li>create a Fiducial node with 3 points</li>
<li>delete the node</li>
<li>Undo</li>
<li>Undo again : the third point is removed in the Markups module, but still persists in a slice view, being non-interactive. The first and second points become non-interactive also.</li>
<li>Redo - the third point reappears in the Markups module, and all three points become interactive in the slice view.</li>
</ul>
<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="34578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>But it is such a critical features, I think we should harden and incorporate into the core, as opposed to keeping at a snippet.</p>
</blockquote>
</aside>
<p>It seems to be N° 1 in the feature request section.</p>

---
