# How to change height for editing mode for qMRMLSubjectHierarchyTreeView

**Topic ID**: 35177
**Date**: 2024-03-30
**URL**: https://discourse.slicer.org/t/how-to-change-height-for-editing-mode-for-qmrmlsubjecthierarchytreeview/35177

---

## Post #1 by @zina (2024-03-30 04:15 UTC)

<p>When I am editing row value in qMRMLSubjectHierarchyTreeView it’s looks very small. How can I change height? In not editing mode, rows looks ok.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d57867994a15b5eee8efa7d6f853bf5a0f4a884f.png" alt="image" data-base62-sha1="usrFm8oguHhkH2J2nf4GzhqPH8b" width="476" height="131"></p>

---

## Post #2 by @lassoan (2024-03-30 13:20 UTC)

<p>I’ve never seen anything like this. Have you edited the screenshot in some way or this is how the tree appears for you? Does the purple rounded rectangle appears when you double-click on an item? What operating system are you using? Have you installed any extension or done any customization in any way?</p>

---

## Post #3 by @zina (2024-04-01 12:07 UTC)

<p>We are using Windows 10 (64 bit) v 22H2. Purple border on rectangle our style for edit mode (double click). We did not make any changes to slider. The screenshot reflect how tree appears to me.</p>

---

## Post #4 by @cpinter (2024-04-01 14:06 UTC)

<p>I suppose then that you customize the GUI using QSS. Probably the padding or border is set to too high (or not set but should be). I suggest referring to the QSS guide at this point instead of the Slicer community as it is a purely Qt issue<br>
<a href="https://doc.qt.io/qt-5/stylesheet-reference.html" class="onebox" target="_blank" rel="noopener">https://doc.qt.io/qt-5/stylesheet-reference.html</a></p>
<p>If my assumption is wrong please give us more details.</p>

---
