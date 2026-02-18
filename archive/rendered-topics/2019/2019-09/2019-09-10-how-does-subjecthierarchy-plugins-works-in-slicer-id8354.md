# How does SubjectHierarchy Plugins works in Slicer

**Topic ID**: 8354
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/how-does-subjecthierarchy-plugins-works-in-slicer/8354

---

## Post #1 by @mikecsu (2019-09-10 05:12 UTC)

<p>Operating system:win10<br>
Slicer version:slicer 4.10.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,everyone.  I am learning the slicer source code for simplifying some operations  in Slicer. But i have trouble in understanding the SubjectHierarchy Plugins, can anyone explain it ?</p>
<p>Any help would be appreciated.</p>

---

## Post #2 by @lassoan (2019-09-11 14:45 UTC)

<p>Subject hierarchy plugins can be used to add custom icon, override default actions (such as show/hide), or define new actions in the right-click menu.</p>
<p>You can implement these plugins in either C++ or Python. There are many examples in Slicer core: download source code of Slicer and search for “SubjectHierarchyPlugins” folders.</p>

---

## Post #3 by @cpinter (2019-09-11 14:51 UTC)

<p>I suggest also reading the Information for Developers section on this page<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Data" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Data</a></p>

---
