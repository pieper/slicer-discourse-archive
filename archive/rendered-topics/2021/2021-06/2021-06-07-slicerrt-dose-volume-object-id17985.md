---
topic_id: 17985
title: "Slicerrt Dose Volume Object"
date: 2021-06-07
url: https://discourse.slicer.org/t/17985
---

# SlicerRT dose volume object

**Topic ID**: 17985
**Date**: 2021-06-07
**URL**: https://discourse.slicer.org/t/slicerrt-dose-volume-object/17985

---

## Post #1 by @edwardwang1 (2021-06-07 01:06 UTC)

<p>Hi there,</p>
<p>I am doing some work where I am creating radiation dose distributions for simulated tumours from scratch (rather than exporting from a RT planning software). In Python I generate a 3D numpy array which I convert to a <em>vtkMRMLScalarVolumeNode</em>. How do I convert my scalar volume node into a dose volume node that is used by the Dose Volume Histogram module in SlicerRT?</p>
<p>I am able to successfully load in dose volumes from DICOM data. When I investigate those volumes, I find that they are also <em>vtkMRMLScalarVolumeNodes</em>. What differentiates a dose volume node from other Scalar Volume Nodes (besides the unit).</p>
<p>Thank you,<br>
Ed</p>

---

## Post #2 by @lassoan (2021-06-07 04:03 UTC)

<p>Yes, it is mainly about setting the unit, but you also need to have the dose volume under a proper DICOM hierarchy. You can find all the necessary steps in the implementation of the right-click menu action (in Data module) that converts a regular volume to a dose volume:</p>
<aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/5bd54b56750621a31d02c17161dea2d1d88ad4c3/DicomRtImportExport/SubjectHierarchyPlugins/qSlicerSubjectHierarchyRtDoseVolumePlugin.cxx#L298-L393" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/5bd54b56750621a31d02c17161dea2d1d88ad4c3/DicomRtImportExport/SubjectHierarchyPlugins/qSlicerSubjectHierarchyRtDoseVolumePlugin.cxx#L298-L393" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/5bd54b56750621a31d02c17161dea2d1d88ad4c3/DicomRtImportExport/SubjectHierarchyPlugins/qSlicerSubjectHierarchyRtDoseVolumePlugin.cxx#L298-L393</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="298" style="counter-reset: li-counter 297 ;">
          <li>void qSlicerSubjectHierarchyRtDoseVolumePlugin::convertCurrentNodeToRtDoseVolume()
</li>
          <li>{
</li>
          <li>  vtkMRMLSubjectHierarchyNode* shNode = qSlicerSubjectHierarchyPluginHandler::instance()-&gt;subjectHierarchyNode();
</li>
          <li>  if (!shNode)
</li>
          <li>  {
</li>
          <li>    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": Failed to access subject hierarchy node";
</li>
          <li>    return;
</li>
          <li>  }
</li>
          <li>  vtkIdType currentItemID = qSlicerSubjectHierarchyPluginHandler::instance()-&gt;currentItem();
</li>
          <li>  if (!currentItemID)
</li>
          <li>  {
</li>
          <li>    qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": Invalid current item";
</li>
          <li>    return;
</li>
          <li>  }
</li>
          <li>
</li>
          <li>  // Get associated volume node
</li>
          <li>  vtkMRMLScalarVolumeNode* volumeNode = vtkMRMLScalarVolumeNode::SafeDownCast(
</li>
          <li>    shNode-&gt;GetItemDataNode(currentItemID) );
</li>
          <li>  if (!volumeNode)
</li>
          <li>  {
</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/5bd54b56750621a31d02c17161dea2d1d88ad4c3/DicomRtImportExport/SubjectHierarchyPlugins/qSlicerSubjectHierarchyRtDoseVolumePlugin.cxx#L298-L393" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @edwardwang1 (2021-06-07 16:47 UTC)

<p>Thank you, this is exactly what I was looking for!</p>

---

## Post #4 by @edwardwang1 (2021-06-07 18:40 UTC)

<p>In case this is useful for others, here is my Python code to achieve this:</p>
<pre><code class="lang-auto">sh  = slicer.util.getNodesByClass("vtkMRMLSubjectHierarchyNode")[0]
itemID = sh.GetItemByDataNode(MmNode)
sh.SetItemParent(itemID, sh.GetItemParent(sh.GetItemByDataNode(volumeNode)))
sh.SetItemAttribute(itemID, 'DoseUnitName', "Gy")
sh.SetItemAttribute(itemID, 'DoseUnitValue', "1.0")
MmNode.SetAttribute("DicomRtImport.DoseVolume", "1")
sh.RequestOwnerPluginSearch(itemID)
sh.ItemModified(itemID)
</code></pre>

---
