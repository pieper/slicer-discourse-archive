---
topic_id: 1720
title: "In Documentation Wiki Refering To Undocking Docking What Is"
date: 2017-12-26
url: https://discourse.slicer.org/t/1720
---

# In Documentation Wiki, refering to undocking/docking, what is the 'panel chrome'?

**Topic ID**: 1720
**Date**: 2017-12-26
**URL**: https://discourse.slicer.org/t/in-documentation-wiki-refering-to-undocking-docking-what-is-the-panel-chrome/1720

---

## Post #1 by @aNonprofessional (2017-12-26 06:37 UTC)

<p>In a Slicer Documentation Wiki I find the term ‘panel chrome’ in relation to re-docking the Welcome window after undocking it, when I am trying to see about expanding the 3D view to fill the screen.</p>
<p>I experimentally clicked the ‘restore’ button in the ‘Welcome To Slicer’ window, and the Welcome window  undocks, and “SlicerApp-real” is added to the previously blank title bar of that window, and at that point that window has only a close window ‘X’ control.  It surprises me that there isn’t a control present to re-dock the Welcome window. As I google around trying to figure out how to get it re-docked (having only the close window ‘X’ control present), I found at <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Module_Panel" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Module_Panel</a> the following:</p>
<p>“The panel may be undocked (by left-clicking &amp; dragging the <strong>panel chrome</strong> or by selecting its undock icon; hidden by selecting the hide (X) icon, or have its display toggled by selecting View-&gt;Module Panel. The panel can be re-docked by double-clicking on <strong>its chrome</strong>.”</p>
<p>What is the ‘<strong>panel chrome</strong>’?</p>
<p>I’ve never seen that phrase/term before.</p>
<p>I discover that double-clicking on the <strong>title bar</strong> of the Welcome window will re-dock the window, but why not just retain the ‘restore’ control in the title bar and make it toggle undock/redock?</p>

---

## Post #2 by @lassoan (2017-12-26 14:37 UTC)

<p><a href="https://www.nngroup.com/articles/browser-and-gui-chrome/">Window chrome</a> refers to nonclient area of a window. I’ve updated the wiki page to use simpler terms - window title bar and frame.</p>
<p>Qt’s default behavior is to show only a close button on undocked widgets. I agree that it could be useful to add a “dock” button in its title bar. This is already tracked here: <a href="https://issues.slicer.org/view.php?id=1323">https://issues.slicer.org/view.php?id=1323</a></p>

---
