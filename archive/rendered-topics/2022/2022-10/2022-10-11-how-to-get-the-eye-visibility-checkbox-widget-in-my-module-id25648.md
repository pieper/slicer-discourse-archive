# How to get the eye visibility checkbox widget in my module

**Topic ID**: 25648
**Date**: 2022-10-11
**URL**: https://discourse.slicer.org/t/how-to-get-the-eye-visibility-checkbox-widget-in-my-module/25648

---

## Post #1 by @Niels (2022-10-11 19:44 UTC)

<p>I like the checkboxes that are used for showing and hiding.For example the one in the Volume Rendering module or to show/hide segments in the segment editor.</p>
<p>I know how to add an ordinary checkbox widget in my module using Python.</p>
<p>But how to make it into this eye-icon like checkbox?</p>

---

## Post #2 by @cpinter (2022-10-13 12:59 UTC)

<p>You need to set the icons</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce1c71ffea278fb1e28d798139f0a65cf67433a9.png" alt="image" data-base62-sha1="tpliLCqFsgYUPDP0BIWCqglsi5X" width="425" height="282"></p>

---

## Post #3 by @jmhuie (2023-01-22 16:59 UTC)

<p>Sorry, how do I actually set the icon? It looks like I need to select it from a file or resource, but I’m not sure what’s the easiest way to access that.</p>

---

## Post #4 by @cpinter (2023-01-23 09:54 UTC)

<p>You start Qt Designer as described in the documentation. Then you click on the little arrow next to the icon (see screenshot above), then select <code>Choose Resource...</code>. You can then import the resource file <code>path\to\Slicer\Libs\MRML\Widgets\Resources\qMRMLWidgets.qrc</code>. You’ll then see the icons in the resource list.</p>

---

## Post #5 by @jmhuie (2023-01-23 14:08 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="25648">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>You can then import the resource file <code>path\to\Slicer\Libs\MRML\Widgets\Resources\qMRMLWidgets.qrc</code>.</p>
</blockquote>
</aside>
<p>I am trying to add the resource file, but I am unable to navigate to it or add that path. I am also unable to find the file on my Mac within the Slicer application.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b496d1fdf3ab30f6faae5a9edf9d9f5176643db0.jpeg" data-download-href="/uploads/short-url/pLz4GLSqkO82kQbhxwmWsSPtZKg.jpeg?dl=1" title="Screen Shot 2023-01-23 at 9.02.12 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b496d1fdf3ab30f6faae5a9edf9d9f5176643db0_2_690x384.jpeg" alt="Screen Shot 2023-01-23 at 9.02.12 AM" data-base62-sha1="pLz4GLSqkO82kQbhxwmWsSPtZKg" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b496d1fdf3ab30f6faae5a9edf9d9f5176643db0_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b496d1fdf3ab30f6faae5a9edf9d9f5176643db0_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b496d1fdf3ab30f6faae5a9edf9d9f5176643db0_2_1380x768.jpeg 2x" data-dominant-color="535354"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-01-23 at 9.02.12 AM</span><span class="informations">1920×1071 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2023-01-26 23:20 UTC)

<p>It might be simpler to set the icon in the sou Ce code as it is done here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/blob/094b64a090c5433ed20b00c8980a6361bd682860/CrossSectionAnalysis/CrossSectionAnalysis.py#L91">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/094b64a090c5433ed20b00c8980a6361bd682860/CrossSectionAnalysis/CrossSectionAnalysis.py#L91" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/094b64a090c5433ed20b00c8980a6361bd682860/CrossSectionAnalysis/CrossSectionAnalysis.py#L91" target="_blank" rel="noopener">vmtk/SlicerExtension-VMTK/blob/094b64a090c5433ed20b00c8980a6361bd682860/CrossSectionAnalysis/CrossSectionAnalysis.py#L91</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="81" style="counter-reset: li-counter 80 ;">
          <li># selectionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton")</li>
          <li># unitNode = slicer.mrmlScene.GetNodeByID(selectionNode.GetUnitNodeID("length"))</li>
          <li># unitNode.SetPrecision(2)</li>
          <li># unitNode = slicer.mrmlScene.GetNodeByID(selectionNode.GetUnitNodeID("area"))</li>
          <li># unitNode.SetPrecision(2)</li>
          <li>
          </li>
<li>self.ui.segmentSelector.setVisible(False)</li>
          <li>self.ui.browseCollapsibleButton.collapsed = True</li>
          <li>
          </li>
<li>self.ui.toggleTableLayoutButton.visible = False</li>
          <li class="selected">self.ui.toggleTableLayoutButton.setIcon(qt.QIcon(':/Icons/Medium/SlicerVisibleInvisible.png'))</li>
          <li>self.ui.togglePlotLayoutButton.visible = False</li>
          <li>self.ui.togglePlotLayoutButton.setIcon(qt.QIcon(':/Icons/Medium/SlicerVisibleInvisible.png'))</li>
          <li>
          </li>
<li>layoutManager = slicer.app.layoutManager()</li>
          <li>if layoutManager is not None: # NOTE: We need the check because some tests can run without main window</li>
          <li>  self.previousLayoutId = slicer.app.layoutManager().layout</li>
          <li>
          </li>
<li>self.ui.jumpCentredInSliceNodeCheckBox.setIcon(qt.QIcon(':/Icons/ViewCenter.png'))</li>
          <li>self.ui.orthogonalReformatInSliceNodeCheckBox.setIcon(qt.QIcon(':/Icons/MouseRotateMode.png'))</li>
          <li>self.ui.outputPlotSeriesTypeComboBox.addItem("MIS diameter", MIS_DIAMETER)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
