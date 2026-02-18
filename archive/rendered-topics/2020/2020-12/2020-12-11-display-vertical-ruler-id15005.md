# Display vertical ruler

**Topic ID**: 15005
**Date**: 2020-12-11
**URL**: https://discourse.slicer.org/t/display-vertical-ruler/15005

---

## Post #1 by @Hamid (2020-12-11 14:26 UTC)

<p>The Ruler shows up at the bottom and in horizontal position. Is there any way to rotate the ruler e.g to the vertical position?</p>

---

## Post #2 by @lassoan (2020-12-11 14:50 UTC)

<p>The ruler can only be displayed at the bottom, but for some cases it would be nice to be able to show it vertically. If you are somewhat familiar with C++ programming then you should be able to modify <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLRulerDisplayableManager.cxx">vtkMRMLRulerDisplayableManager</a> to show a vertical ruler. If you can do that then we’ll help with adding GUI to choose between orientations and getting it integrated into Slicer core.</p>
<p>If you don’t have time to do that but it is important to you then you can give a contract to one of the Slicer commercial partners.</p>
<p>If none of these work for you then as a workaround you can add a markups line to measure/display distances along a vertical line. You can always keep it in the current slice plane by adding an observer to the slice not and updating the line position if you change the slice position.</p>

---
