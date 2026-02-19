---
topic_id: 31736
title: "Annotate A Segment With Properties From A Popup Window"
date: 2023-09-15
url: https://discourse.slicer.org/t/31736
---

# Annotate a segment with properties from a popup window

**Topic ID**: 31736
**Date**: 2023-09-15
**URL**: https://discourse.slicer.org/t/annotate-a-segment-with-properties-from-a-popup-window/31736

---

## Post #1 by @biocyberman (2023-09-15 12:50 UTC)

<p>Hi<br>
I am new to 3D Slicer. I am trying to figure out the following to add some custom enhancement to the  <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer/MONAILabel" rel="noopener nofollow ugc">MONAIlabel plugin</a>:</p>
<h2><a name="p-100515-operating-system-ubuntu-jammy-1" class="anchor" href="#p-100515-operating-system-ubuntu-jammy-1" aria-label="Heading link"></a>Operating system: Ubuntu Jammy</h2>
<h2><a name="p-100515-slicer-version-54-2" class="anchor" href="#p-100515-slicer-version-54-2" aria-label="Heading link"></a>Slicer version: 5.4</h2>
<h2><a name="p-100515-expected-behavior-3" class="anchor" href="#p-100515-expected-behavior-3" aria-label="Heading link"></a>Expected behavior:</h2>
<ul>
<li>When using the segment editor, user can do <code>Ctrl + RighClick</code> to annotate the segment under the mouse cursor.</li>
<li>A popup dialog show up by <code>Ctrl + RighClick</code> (because the default <code>RightClick</code> already has a popup dialog.</li>
<li>User then can check or uncheck items and click “OK” to save the choices.</li>
<li>Checkboxes state is saved together with the segment, identified by SegmentID.</li>
</ul>
<h2><a name="p-100515-actual-behavior-emtpy-4" class="anchor" href="#p-100515-actual-behavior-emtpy-4" aria-label="Heading link"></a>Actual behavior: Emtpy</h2>

---

## Post #2 by @lassoan (2023-09-15 13:13 UTC)

<p>There are several easy way to implement this with a little Python scripting.</p>
<p>If you just want to be able to select a segment at the current mouse position and specify some properties for it, you could implement a segment editor effect, which could observe left-click (or any other) event and when it is triggered then get the segment at the current position and show the popup to enter additional information. You can see it in qSlicerSegmentEditorPaintEffectPrivate::segmentAtPosition how you can get the segment(s) visible at the current position in a Segment Editor effect.</p>
<p>If you want to annotate segments independent from Segment Editor widgets then you can implement a Python scripted Subject Hierarchy plugin. Right-click menu items are populated by these plugins by implementing its <code>viewContextMenuActions</code> and <code>showViewContextMenuActionsForItem</code> methods (see for example in <code>qSlicerSubjectHierarchyMarkupsPlugin</code>). The plugin gets notified when the user right-clicks in the view and you can determine what segments are visible at that position and add items to the context menu accordingly. Context menu actions can have submenus, checkboxes, etc. so you may be able to add everything under a single menu action.</p>
<p>To determine what segments are visible at that position you can do what is done in DataProbe module (that displays the list of segments at the current position in the Data Probe window in the bottom-left corner:</p>
<pre><code class="lang-auto">        # collect information from displayable managers
        displayableManagerCollection = vtk.vtkCollection()
        if sliceNode:
            sliceWidget = slicer.app.layoutManager().sliceWidget(sliceNode.GetName())
            if sliceWidget:
                # sliceWidget is owned by the layout manager
                sliceView = sliceWidget.sliceView()
                sliceView.getDisplayableManagers(displayableManagerCollection)
        aggregatedDisplayableManagerInfo = ''
        for index in range(displayableManagerCollection.GetNumberOfItems()):
            displayableManager = displayableManagerCollection.GetItemAsObject(index)
            infoString = displayableManager.GetDataProbeInfoStringForPosition(xyz) 
</code></pre>
<p>Instead of calling <code>GetDataProbeInfoStringForPosition</code>, you would call the <code>GetVisibleSegmentsForPosition(double ras[3], vtkMRMLSegmentationDisplayNode* displayNode, vtkStringArray* segmentIDs, vtkDoubleArray* segmentValues = nullptr)</code> method.</p>

---
