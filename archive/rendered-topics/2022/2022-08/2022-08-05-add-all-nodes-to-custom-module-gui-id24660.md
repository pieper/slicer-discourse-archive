---
topic_id: 24660
title: "Add All Nodes To Custom Module Gui"
date: 2022-08-05
url: https://discourse.slicer.org/t/24660
---

# Add all nodes to custom module gui

**Topic ID**: 24660
**Date**: 2022-08-05
**URL**: https://discourse.slicer.org/t/add-all-nodes-to-custom-module-gui/24660

---

## Post #1 by @rhodesdante (2022-08-05 20:57 UTC)

<p>I would like to enable the user of a custom python module to look at all the volume nodes at once, rather than selecting them using a qMRMLComboBox to select them individually. In addition, I would like to allow them to click on the “eye” icon, like in the subject hierarchy of the data module, to render the selected volume node in the slice panes. Does a widget exist for this? If not, it doesn’t need to be exactly the same–it just needs to be able to show all volume names simultaneously and load them on an icon click. I included the picture of what I’m referencing in case it helps. Any help with this task would be greatly appreciated!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76603fe35ab4878b15e36b065201b5df4288239b.png" data-download-href="/uploads/short-url/gTcyqnJjUxRfnARWcZT4jaKhDWr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76603fe35ab4878b15e36b065201b5df4288239b_2_576x500.png" alt="image" data-base62-sha1="gTcyqnJjUxRfnARWcZT4jaKhDWr" width="576" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76603fe35ab4878b15e36b065201b5df4288239b_2_576x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76603fe35ab4878b15e36b065201b5df4288239b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76603fe35ab4878b15e36b065201b5df4288239b.png 2x" data-dominant-color="F4F8FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">600×520 12 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rhodesdante (2022-08-09 13:51 UTC)

<p>Hi–I want to make sure I provide all necessary information for this question. Is there anything else I should add that would help provide full context to this topic? Thank you again for your support!</p>

---

## Post #3 by @jamesobutler (2022-08-09 15:25 UTC)

<pre data-code-wrap="python"><code class="lang-python">subject_hierarchy_table_view = slicer.qMRMLSubjectHierarchyTreeView()
subject_hierarchy_table_view.setMRMLScene(slicer.mrmlScene)  # As a mrml widget, set the mrml scene
subject_hierarchy_table_view.nodeTypes = ["vtkMRMLScalarVolumeNode"]  # limit to just Scalar Volume Nodes
subject_hierarchy_table_view.show()  # show this example widget
</code></pre>
<p>If you are using Qt Designer to create your UI, if you launch Slicer with the Designer arg (<code>./Slicer.exe --designer</code>) it will open Qt Designer with the Slicer custom widgets included. Then you can add a qMRMLSubjectHierarchyTreeView to your UI and inspect all the available options through a GUI interface.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03095eff37663d670de272a4b2d0e5401be2171d.png" data-download-href="/uploads/short-url/qRvBUgJxC4LrhDPYPYBzeFgpK5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03095eff37663d670de272a4b2d0e5401be2171d.png" alt="image" data-base62-sha1="qRvBUgJxC4LrhDPYPYBzeFgpK5" width="352" height="500" data-dominant-color="EEDDD5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">513×727 21.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Victor_Wayne (2025-08-07 07:41 UTC)

<p>If I set nodeTypes as [‘vtkMRMLMarkupsLineNode’] it shows the line nodes but, it also shows the folders. how can I remove the folders? And is there a way to hide a specific element in the tree view?</p>

---
