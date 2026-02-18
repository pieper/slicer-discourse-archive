# Rewrite qMRMLSubjectHierarchyTreeView

**Topic ID**: 25250
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/rewrite-qmrmlsubjecthierarchytreeview/25250

---

## Post #1 by @miniminic (2022-09-14 02:14 UTC)

<p>我想要修改qMRMLSubjectHierarchyTreeView实现一些功能,但是我不想改动它的源码,所以我创建了一个myTreeView继承于qMRMLSubjectHierarchyTreeView,现在问题是我应该怎么样将slicer中的qMRMLSubjectHierarchyTreeView替换成myTreeView</p>
<p>I want to change qMRMLSubjectHierarchyTreeView implement some functions, but I don’t want to change its source code, so I created a myTreeView inheritance in qMRMLSubjectHierarchyTreeView, now the problem is that I should how the slicer the qMRMLSubjectHierarchyTreeView replace myTreeView</p>

---

## Post #2 by @cpinter (2022-09-15 08:00 UTC)

<p>You can either contribute your changes as options in the existing class in Slicer, or you can fork Slicer, in which case the maintenance burden will significantly increase.</p>

---

## Post #3 by @lassoan (2022-09-15 13:34 UTC)

<aside class="quote no-group" data-username="miniminic" data-post="1" data-topic="25250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miniminic/48/16647_2.png" class="avatar"> miniminic:</div>
<blockquote>
<p>I want to change qMRMLSubjectHierarchyTreeView implement some functions</p>
</blockquote>
</aside>
<p>What are those functions?</p>
<p>The best way to proceed depends on that, because if those functions are generally useful for Slicer users then it makes sense to maintain them in Slicer core. If those features are only useful for your project then you can use existing infrastructure in subject hierarchy that already allows very flexible customization and extension. If current subject hierarchy customization/extension infrastructure in Slicer core are not sufficient then you can improve that.</p>

---

## Post #4 by @miniminic (2022-09-16 03:35 UTC)

<p>Thank you very much I have changed qMRMLSubjectHierarchyTreeView source I want to achieve</p>

---
