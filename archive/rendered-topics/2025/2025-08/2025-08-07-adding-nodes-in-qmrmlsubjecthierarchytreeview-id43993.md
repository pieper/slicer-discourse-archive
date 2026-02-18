# Adding nodes in qMRMLSubjectHierarchyTreeView

**Topic ID**: 43993
**Date**: 2025-08-07
**URL**: https://discourse.slicer.org/t/adding-nodes-in-qmrmlsubjecthierarchytreeview/43993

---

## Post #1 by @Victor_Wayne (2025-08-07 07:49 UTC)

<p>Hello,</p>
<p>I am tracking some line nodes of type `vtkMRMLMarkupsLineNode` in a class called Plan for specific plan created by the user. How can I add those lines to the  qMRMLSubjectHierarchyTreeView that I created in my custom widget?</p>
<p>if I set nodeType = [‘vtkMRMLMarkupsLineNode’] it correctly shows the lines only but it also shows the folder. How can I get rid of the folders if I can’t add a node to the tree view?</p>
<p>One last thing, How can I remove a specific node from the tree view but not from the scene?</p>
<p>Any help will be appreciated and thanks for your precious time.</p>

---

## Post #2 by @cpinter (2025-08-07 12:28 UTC)

<p>This question seems to be more or less a duplicate of this:</p>
<aside class="quote quote-modified" data-post="16" data-topic="29499">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/victor_wayne/48/80778_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/how-to-add-folder-in-scene/29499/16">How to add folder in scene?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    I have to admit that I don’t quite get what you are saying. 
Here’s what I want to do. 
I inspected the Data module and found out that it is using qMRMLSubjectHierarchyTreeView widget for showing the nodes in a tree view. I wanted to customize the Data module by creating my own custom widget. So I created a widget, with a combo box that selects from the list plans. The plans contains lines. I want to show the lines like a list and with all the added functionality of hide/show `eye` button, trans…
  </blockquote>
</aside>


---
