---
topic_id: 733
title: "Subject Hierarchy Combobox Showing A Drop Down Tree"
date: 2017-07-20
url: https://discourse.slicer.org/t/733
---

# Subject hierarchy combobox showing a drop-down tree

**Topic ID**: 733
**Date**: 2017-07-20
**URL**: https://discourse.slicer.org/t/subject-hierarchy-combobox-showing-a-drop-down-tree/733

---

## Post #1 by @dzenanz (2017-07-20 20:11 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Labs/SubjectHierarchy#New_features" rel="nofollow noopener">New features</a> section in the documentaion mentions a combobox showing a drop-down tree, but in the designer (started by Slicer-build\Slicer.exe --designer) I only see qMRMLSubjectHierarchyTreeView widget. Is the documentation wrong, or am I doing something wrong?</p>

---

## Post #2 by @cpinter (2017-07-20 21:07 UTC)

<p>I think what you need is qMRMLSubjectHierarchyComboBox</p>

---

## Post #3 by @dzenanz (2017-07-20 21:29 UTC)

<p>I don’t see that in Designer, and if I add qMRMLSubjectHierarchyTreeView and then manually change it into qMRMLSubjectHierarchyComboBox (by text editing .ui file), I get the following error at run time:</p>
<blockquote>
<p>AttributeError: QTreeView has no attribute named ‘setMRMLScene’</p>
</blockquote>
<p>When was this control added to Slicer? Was it added after qMRMLSubjectHierarchyTreeView?</p>
<p>Edit: <em>I haven’t updated Slicer in a few weeks.</em></p>

---

## Post #4 by @dzenanz (2017-07-20 21:47 UTC)

<p>Directly creating it through Python works:<br>
<code>shcb=slicer.qMRMLSubjectHierarchyComboBox()</code></p>

---

## Post #5 by @cpinter (2017-07-20 22:46 UTC)

<p>You cannot make such substitutions in a ui file unless you edit the signals/slots as well (if you do that it should work).</p>
<p>That said you can also very easily create a Qt Deesigner plugin for the combobox widget, see <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/SubjectHierarchy/Widgets/DesignerPlugins">that of the tree view</a></p>

---

## Post #6 by @lassoan (2017-07-21 03:52 UTC)

<p>Yes, you just need to add two files (copy&amp;paste + find&amp;replace, no thinking is needed) and add them to CMakeLists.txt. Pull request would be very welcome.</p>

---

## Post #7 by @dzenanz (2017-07-21 17:19 UTC)

<p>Thanks for pointing me to the right place. I will probably make a PR for it next week.</p>

---

## Post #8 by @dzenanz (2017-07-22 18:06 UTC)

<p><a href="https://github.com/Slicer/Slicer/pull/748" rel="nofollow noopener">Pull request</a> created.</p>

---

## Post #9 by @lassoan (2017-07-23 02:08 UTC)

<p>The pull request is merged. Thank you!</p>

---

## Post #10 by @cpinter (2017-07-23 15:11 UTC)

<p>Thank you, <a class="mention" href="/u/dzenanz">@dzenanz</a>!</p>

---
