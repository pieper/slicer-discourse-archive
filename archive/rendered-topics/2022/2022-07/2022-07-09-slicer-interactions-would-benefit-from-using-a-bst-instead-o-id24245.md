# Slicer interactions would benefit from using a BST instead of linear search

**Topic ID**: 24245
**Date**: 2022-07-09
**URL**: https://discourse.slicer.org/t/slicer-interactions-would-benefit-from-using-a-bst-instead-of-linear-search/24245

---

## Post #1 by @mau_igna_06 (2022-07-09 00:07 UTC)

<p>I would like to make the argument that functions like <code>vtkSlicerMarkupsWidget::ProcessInteractionEvent</code> could be the reason of bottleneck performance around 100 fiducial points.</p>
<p>Because it has a switch stament with 21 cases:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/661e00945f7a1f695e939366bcaf10e9481f2ada/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidget.cxx#L823-L896">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/661e00945f7a1f695e939366bcaf10e9481f2ada/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidget.cxx#L823-L896" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/661e00945f7a1f695e939366bcaf10e9481f2ada/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidget.cxx#L823-L896" target="_blank" rel="noopener">Slicer/Slicer/blob/661e00945f7a1f695e939366bcaf10e9481f2ada/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidget.cxx#L823-L896</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="823" style="counter-reset: li-counter 822 ;">
          <li>bool vtkSlicerMarkupsWidget::ProcessInteractionEvent(vtkMRMLInteractionEventData* eventData)</li>
          <li>{</li>
          <li>  unsigned long widgetEvent = this-&gt;TranslateInteractionEventToWidgetEvent(eventData);</li>
          <li>
          </li>
<li>  if (this-&gt;ApplicationLogic)</li>
          <li>    {</li>
          <li>    this-&gt;ApplicationLogic-&gt;PauseRender();</li>
          <li>    }</li>
          <li>
          </li>
<li>
          </li>
<li>  bool processedEvent = false;</li>
          <li>  switch (widgetEvent)</li>
          <li>    {</li>
          <li>    case WidgetEventControlPointPlace:</li>
          <li>      processedEvent = this-&gt;PlacePoint(eventData);</li>
          <li>      break;</li>
          <li>    case WidgetEventStopPlace:</li>
          <li>      // cancel point placement</li>
          <li>      this-&gt;GetInteractionNode()-&gt;SwitchToViewTransformMode();</li>
          <li>      processedEvent = ProcessWidgetStopPlace(eventData);</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/661e00945f7a1f695e939366bcaf10e9481f2ada/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidget.cxx#L823-L896" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>According to math we could get interaction 4 times faster if we used binary search on a Binary Search Tree for the function callbacks instead of switch staments if it was only for this different algorithms complexity.</p>
<p>Also I found this classes to have to more than 6 or 8 case staments:</p>
<pre><code class="lang-auto">vtkMRMLSubjectHierarchyNode::ItemEventCallback
vtkMRMLAbstractThreeDViewDisplayableManager::PassThroughInteractorStyleEvent
vtkMRMLCameraWidget::ProcessInteractionEvent
vtkMRMLSliceIntersectionWidget::ProcessInteractionEvent
vtkMRMLWindowLevelWidget::ProcessInteractionEvent
vtkMRMLAbstractLogic::ProcessMRMLSceneEvents
qMRMLSceneModel::onMRMLSceneEvent
void ITKComputeThresholdFromVTKImage
vtkDiffusionTensorGlyph::RequestData
static void vtkDiffusionTensorMathematicsExecute1Eigen
void vtkDiffusionTensorMathematics::ThreadedRequestData
itk_data_types
vtkAnnotationGlyphSource2D::RequestData
vtkMarkupsGlyphSource2D::RequestData
qMRMLSegmentsModel::onEvent
qMRMLSubjectHierarchyModel::onEvent
</code></pre>
<p>I would know how to solve this is python with lambdas but I don’t know how to do it in C++.</p>
<p>Comments are welcomed</p>

---

## Post #2 by @pieper (2022-07-09 00:14 UTC)

<p>Hi <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> it would definitely be good to make the markups interactions more scalable to handle more points and other entities.  I’m skeptical that the switch statement itself is the performance bottleneck since the compiler will make those pretty efficient.  But to be sure I suggest you consider using a performance analysis tool.  People have had good luck with <a href="https://github.com/VerySleepy/verysleepy">VerySleepy on windows</a>, or similar tools on other platforms.  Once we know exactly where the time is being spent we can talk about options for improving the implementations.</p>

---
