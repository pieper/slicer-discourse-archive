---
topic_id: 19644
title: "Trying To Integrate Qslicermarkupsplacewidget Into App"
date: 2021-09-13
url: https://discourse.slicer.org/t/19644
---

# Trying to integrate qSlicerMarkupsPlaceWidget into app

**Topic ID**: 19644
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/trying-to-integrate-qslicermarkupsplacewidget-into-app/19644

---

## Post #1 by @shatz (2021-09-13 13:02 UTC)

<p>Any tutorials on how to integrate fiducials into our app? I clearly dont know the “proper” way to do this but I was just trying to follow how the <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/tree/master/LungCTSegmenter" rel="noopener nofollow ugc">Lung CT segmenter module</a> did it (while cutting out a lot of fat that I dont need, as I only need 1 fiducial), and I cant seem to get it to work.</p>
<p>Is there a minimal example of these working? If not, does this error tell anyone more than it tells me: <code>void qSlicerMarkupsPlaceWidget::setPlaceModeEnabled(bool)  activate failed: Markups module logic, scene, or interaction node is invalid</code></p>

---

## Post #2 by @lassoan (2021-09-13 13:45 UTC)

<p>Before using any MRML widgets, you need to set the scene in the widget. It is commonly done using a signal/slot in Qt Designer (connecting the module widget’s <code>mrmlSceneChanged(vtkMRMLScene*)</code> signal to the MRML widget’s <code>setMRMLScene(vtkMRMLScene*)</code> slot), but you can do it by a method call in the module widget’s <code>setup</code> method, too.</p>
<p>You can find a simpler, less interactive seed placement example in VMTK’s vesselness filtering module:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py#L97-L109">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py#L97-L109" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py#L97-L109" target="_blank" rel="noopener">vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py#L97-L109</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="97" style="counter-reset: li-counter 96 ;">
          <li>self.seedFiducialsNodeSelector = slicer.qSlicerSimpleMarkupsWidget()</li>
          <li>self.seedFiducialsNodeSelector.objectName = 'seedFiducialsNodeSelector'</li>
          <li>self.seedFiducialsNodeSelector = slicer.qSlicerSimpleMarkupsWidget()</li>
          <li>self.seedFiducialsNodeSelector.objectName = 'seedFiducialsNodeSelector'</li>
          <li>self.seedFiducialsNodeSelector.toolTip = "Select a point in the largest vessel. Preview will be shown around this point. This is point is also used for determining maximum vessel diameter if automatic filtering parameters computation is enabled."</li>
          <li>self.seedFiducialsNodeSelector.setNodeBaseName("DiameterSeed")</li>
          <li>self.seedFiducialsNodeSelector.tableWidget().hide()</li>
          <li>self.seedFiducialsNodeSelector.defaultNodeColor = qt.QColor(255,0,0) # red</li>
          <li>self.seedFiducialsNodeSelector.markupsSelectorComboBox().noneEnabled = False</li>
          <li>self.seedFiducialsNodeSelector.markupsPlaceWidget().placeMultipleMarkups = slicer.qSlicerMarkupsPlaceWidget.ForcePlaceSingleMarkup</li>
          <li>ioFormLayout.addRow("Seed point:", self.seedFiducialsNodeSelector)</li>
          <li>self.parent.connect('mrmlSceneChanged(vtkMRMLScene*)',</li>
          <li>                    self.seedFiducialsNodeSelector, 'setMRMLScene(vtkMRMLScene*)')</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
