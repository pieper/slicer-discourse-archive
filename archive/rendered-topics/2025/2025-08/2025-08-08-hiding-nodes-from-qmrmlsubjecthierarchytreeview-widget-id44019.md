---
topic_id: 44019
title: "Hiding Nodes From Qmrmlsubjecthierarchytreeview Widget"
date: 2025-08-08
url: https://discourse.slicer.org/t/44019
---

# Hiding nodes from qMRMLSubjectHierarchyTreeView widget

**Topic ID**: 44019
**Date**: 2025-08-08
**URL**: https://discourse.slicer.org/t/hiding-nodes-from-qmrmlsubjecthierarchytreeview-widget/44019

---

## Post #1 by @Victor_Wayne (2025-08-08 04:01 UTC)

<p>Hello,</p>
<p>I inspected the Data module and found out that it is using qMRMLSubjectHierarchyTreeView widget for showing the nodes in a tree view. I wanted to customize the Data module by creating my own custom widget. So I created a widget, with a combo box that selects from the list plans. The plans contains lines. I want to show the lines like a list and with all the added functionality of hide/show `eye` button, transformation tracking, color picking, and their IDs like how the Data module shows it. So I created one instance of qMRMLSubjectHierarchyTreeView, and set it like this.</p>
<pre data-code-wrap="python"><code class="lang-python">self.lineDetailView = qMRMLSubjectHierarchyTreeView()
self.lineDetailView.setMRMLScene(slicer.mrmlScene)

</code></pre>
<p>The problem is that it shows all the nodes and folders. I just want to show the line that corresponds to the selected plan. I thought I could do the following</p>
<pre data-code-wrap="python"><code class="lang-python">self.lineDetailView.nodeTypes = ['vtkMRMLMarkupsLineNode']

</code></pre>
<p>but this shows the folders with the lines. even if it didn’t show the folders, I don’t know how to delete the other line nodes that doesn’t belong to the current selected plan.</p>
<p>Is there a way to hide any node, be it a folder node or a segmentation node or a line node using its ID from the tree view? I just to want to hide from the tree view. not from the scene.</p>
<p>Any help will be appreciated. Thank you for replying to me.</p>

---

## Post #2 by @cpinter (2025-08-08 09:25 UTC)

<p>Have you looked at the available filtering options as I suggested in the other thread?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.h#L87-L106">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.h#L87-L106" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.h#L87-L106" target="_blank" rel="noopener">Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.h</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.h#L87-L106" rel="noopener"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="87" style="counter-reset: li-counter 86 ;">
          <li>/// Filter to show only items that contain any of the given attributes with this name. Empty by default</li>
          <li>Q_PROPERTY(QStringList includeItemAttributeNamesFilter READ includeItemAttributeNamesFilter WRITE setIncludeItemAttributeNamesFilter)</li>
          <li>/// Filter to show only items for data nodes that contain any of the given attributes with this name. Empty by default</li>
          <li>Q_PROPERTY(QStringList includeNodeAttributeNamesFilter READ includeNodeAttributeNamesFilter WRITE setIncludeNodeAttributeNamesFilter)</li>
          <li>/// Filter to hide items that contain any of the given attributes with this name. Empty by default</li>
          <li>/// Overrides \sa includeItemAttributeNamesFilter</li>
          <li>Q_PROPERTY(QStringList excludeItemAttributeNamesFilter READ excludeItemAttributeNamesFilter WRITE setExcludeItemAttributeNamesFilter)</li>
          <li>/// Filter to hide items for data nodes that contain any of the given attributes with this name. Empty by default</li>
          <li>/// Overrides \sa includeNodeAttributeNamesFilter</li>
          <li>Q_PROPERTY(QStringList excludeNodeAttributeNamesFilter READ excludeNodeAttributeNamesFilter WRITE setExcludeNodeAttributeNamesFilter)</li>
          <li></li>
          <li>/// Filter to show only items that contain an item attribute with this name. Empty by default.</li>
          <li>/// Sets and returns the first attribute in \sa includeItemAttributeNamesFilter.</li>
          <li>/// \deprecated Kept only for backwards compatibility. Use addItemAttributeFilter() or removeItemAttributeFilter() instead.</li>
          <li>Q_PROPERTY(QString attributeNameFilter READ attributeNameFilter WRITE setAttributeNameFilter)</li>
          <li>/// Filter to show only items that contain any item attribute given in \sa includeItemAttributeNamesFilter with the value.</li>
          <li>/// If empty, then existence of the attributes is enough to show.</li>
          <li>/// Exact match is required. Empty by default.</li>
          <li>/// \deprecated Kept only for backwards compatibility. Use addItemAttributeFilter() or removeItemAttributeFilter() instead.</li>
          <li>Q_PROPERTY(QString attributeValueFilter READ attributeValueFilter WRITE setAttributeValueFilter)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>All it takes is a bit of creativity. For example you can set the plan name or some other ID as an attribute to the lines, and you can filter by attribute when you select a plan.</p>

---

## Post #3 by @Victor_Wayne (2025-08-13 04:15 UTC)

<p>Yes, I did exactly what you told here. I attached the plan name itself as an attribute to the line and then I filtered it whenever the combo box text changes. These lines have segmentation nodes attached to it. I now have to show the segmentation nodes below the appropriate line like a tree view. Are there any functions for that?</p>
<p>Thank you very much for your help btw.</p>

---

## Post #4 by @cpinter (2025-08-13 08:51 UTC)

<p>I’d probably organize all nodes that belong to a plan in folders, and filter the folders.</p>
<p>But I feel like I know too little about the use case to give you a comprehensive answer.</p>

---
