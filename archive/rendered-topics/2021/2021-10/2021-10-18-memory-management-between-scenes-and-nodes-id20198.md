# Memory management between scenes and nodes

**Topic ID**: 20198
**Date**: 2021-10-18
**URL**: https://discourse.slicer.org/t/memory-management-between-scenes-and-nodes/20198

---

## Post #1 by @ebrahim (2021-10-18 02:58 UTC)

<p>Does adding a node to a scene give ownership of the node to the scene?</p>
<p>i.e. will the node be deallocated cleanly when the scene is destroyed?</p>
<p>I am talking about adding a node via <code>vtkMRMLScene::AddNode</code></p>

---

## Post #2 by @ebrahim (2021-10-18 23:44 UTC)

<p>It was pointed to <code>vtkMRMLScene::AddNewNodeByClass</code> as the easy way to add a new node to a scene without worrying about memory issues. This worked for me. I still don’t know the answer to my question, but my problem is solved.</p>

---

## Post #3 by @lassoan (2021-10-19 04:13 UTC)

<aside class="quote no-group" data-username="ebrahim" data-post="1" data-topic="20198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>Does adding a node to a scene give ownership of the node to the scene?</p>
</blockquote>
</aside>
<p>All VTK objects have internal reference counting, so they can be always readily shared between multiple owners. The object automatically gets deleted when no other object references it anymore.</p>
<p>When you set a VTK object A into VTK object B then most of the time B will just add one more reference to B.</p>

---
