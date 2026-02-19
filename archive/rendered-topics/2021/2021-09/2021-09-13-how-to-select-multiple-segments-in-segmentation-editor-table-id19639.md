---
topic_id: 19639
title: "How To Select Multiple Segments In Segmentation Editor Table"
date: 2021-09-13
url: https://discourse.slicer.org/t/19639
---

# How to select multiple segments in segmentation editor table view

**Topic ID**: 19639
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/how-to-select-multiple-segments-in-segmentation-editor-table-view/19639

---

## Post #1 by @upupming (2021-09-13 08:36 UTC)

<p>In the table view, we have a context menu item named show only selected items, since it says ‘segments’, I assume we should be able to select multiple segments at once, however, I found I can only select one segment once. But I have an amount of 50 segments, how can I select and show them at once? Thanks!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6a58f94fbf841fb3aa1ffcfd8bfe5010bb0da08.png" alt="image" data-base62-sha1="uCQTfLpgK6AugaZ4GLpVmMBhsbC" width="667" height="406"></p>
<p>I have read the source code, it seems single selection is intended:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L484">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L484" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L484" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L484</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="474" style="counter-reset: li-counter 473 ;">
          <li>QObject::connect( this-&gt;MasterVolumeIntensityMaskRangeWidget, SIGNAL(valuesChanged(double,double)), q, SLOT(onMasterVolumeIntensityMaskRangeChanged(double,double)));</li>
          <li>QObject::connect( this-&gt;OverwriteModeComboBox, SIGNAL(currentIndexChanged(int)), q, SLOT(onOverwriteModeChanged(int)));</li>
          <li></li>
          <li>QObject::connect( this-&gt;UndoButton, SIGNAL(clicked()), q, SLOT(undo()) );</li>
          <li>QObject::connect( this-&gt;RedoButton, SIGNAL(clicked()), q, SLOT(redo()) );</li>
          <li></li>
          <li>q-&gt;qvtkConnect(this-&gt;SegmentationHistory, vtkCommand::ModifiedEvent,</li>
          <li>  q, SLOT(onSegmentationHistoryChanged()));</li>
          <li></li>
          <li>// Widget properties</li>
          <li class="selected">this-&gt;SegmentsTableView-&gt;setSelectionMode(QAbstractItemView::SingleSelection);</li>
          <li>this-&gt;SegmentsTableView-&gt;setHeaderVisible(true);</li>
          <li>this-&gt;SegmentsTableView-&gt;setVisibilityColumnVisible(true);</li>
          <li>this-&gt;SegmentsTableView-&gt;setColorColumnVisible(true);</li>
          <li>this-&gt;SegmentsTableView-&gt;setOpacityColumnVisible(false);</li>
          <li>this-&gt;AddSegmentButton-&gt;setEnabled(false);</li>
          <li>this-&gt;RemoveSegmentButton-&gt;setEnabled(false);</li>
          <li>this-&gt;Show3DButton-&gt;setEnabled(false);</li>
          <li>this-&gt;SwitchToSegmentationsButton-&gt;setEnabled(false);</li>
          <li>this-&gt;EffectsGroupBox-&gt;setEnabled(false);</li>
          <li>this-&gt;OptionsGroupBox-&gt;setEnabled(false);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Can anyone explain why not support multiple rows selection, thanks!</p>

---

## Post #2 by @lassoan (2021-09-13 14:29 UTC)

<p>You can go to Segmentations module for a segment list with multi-select enabled.</p>
<p>All the segment editor effects currently assume that there is only a single segment is selected. Simply enabling multiple selection would break them. Multi-select would be meaningful for some effects, with certain parameter settings, so it could be useful to implement this. We don’t have plans for implementing this, but contributions are welcome!</p>

---
