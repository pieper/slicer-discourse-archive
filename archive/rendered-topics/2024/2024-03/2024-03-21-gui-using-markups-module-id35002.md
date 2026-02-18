# GUI using markups module

**Topic ID**: 35002
**Date**: 2024-03-21
**URL**: https://discourse.slicer.org/t/gui-using-markups-module/35002

---

## Post #1 by @rkraaijveld (2024-03-21 08:43 UTC)

<p>Hi there!</p>
<p>I’m trying to add the markups module into my own module, particularly the ruler button. I’ve worked with the segment editor widget before, but I can’t seem to find as much information about the markups module. (Also, I’m not that familiar with C++). Could someone share some python code with me that allows me to import the markups module into my module?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2024-03-23 15:16 UTC)

<p>An entire module cannot be imported into another module, but a module can use any other modules and can add use widgets provided by other modules.</p>
<p>Reusable widgets provided my Markups module are available <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Loadable/Markups/Widgets">here</a>. These widgets should also be available in Qt Designer, so that you can just drag-and-drop them into your module GUI. If you describe specifically what functionality you need then we may be able to recommend GUI widgets that can be used.</p>

---
