---
topic_id: 20208
title: "Window Resize With Model Clipping Enabled Is Extremely Slow"
date: 2021-10-18
url: https://discourse.slicer.org/t/20208
---

# Window resize with model clipping enabled is extremely slow

**Topic ID**: 20208
**Date**: 2021-10-18
**URL**: https://discourse.slicer.org/t/window-resize-with-model-clipping-enabled-is-extremely-slow/20208

---

## Post #1 by @hherhold (2021-10-18 16:23 UTC)

<p>I have a relatively complex model (20 million polys). When I enable clipping, resizing the slicer window is <em>extremely</em> slow - it basically hangs the program for 30-40 seconds. If I select “Keep only whole cells when clipping” it’s quite a bit faster (as is all clipping when this is enabled) but it’s still somewhat delayed.</p>
<p>It’s almost like resizing the window makes the clipping operation occur again and again during the resize. I attached “Instruments” to the running process (MacOS) and a stack trace of the slow thread is attached below. I’ve picked out the one taking the longest (towards the bottom), and it’s <code>vtkMergePoints::InsertUniquePoint()</code>.</p>
<p>Any idea why this would happen? Should it really be re-doing the clipping operation when the window is resized?</p>
<pre><code>35.33 s   43.0%	35.33 s vtkMergePoints::InsertUniquePoint(double const*, long long&amp;)


 128  82037.0  Slicer (99188) :0
 127  81727.0  -[NSApplication sendEvent:]  0x96bf37 :0
 126 QtWidgets 38959.0  QBoxLayout::setGeometry(QRect const&amp;)
 125 QtWidgets 38959.0  QWidgetItem::setGeometry(QRect const&amp;)
 124 QtWidgets 38959.0  QWidget::setGeometry(QRect const&amp;)
 123 QtWidgets 38958.0  QWidgetPrivate::setGeometry_sys(int, int, int, int, bool)
 122 QtCore 38958.0  QCoreApplication::notifyInternal2(QObject*, QEvent*)
 121 libqSlicerBaseQTGUI.dylib 38958.0  qSlicerApplication::notify(QObject*, QEvent*)
 120 QtWidgets 38958.0  QApplication::notify(QObject*, QEvent*)
 119 QtWidgets 38958.0  QApplicationPrivate::notify_helper(QObject*, QEvent*)
 118 QtWidgets 38955.0  QLayoutPrivate::doResize()
 117 QtWidgets 38955.0  QBoxLayout::setGeometry(QRect const&amp;)
 116 QtWidgets 38955.0  QWidgetItem::setGeometry(QRect const&amp;)
 115 QtWidgets 38955.0  QWidget::setGeometry(QRect const&amp;)
 114 QtWidgets 38955.0  QWidgetPrivate::setGeometry_sys(int, int, int, int, bool)
 113 QtCore 38955.0  QCoreApplication::notifyInternal2(QObject*, QEvent*)
 112 libqSlicerBaseQTGUI.dylib 38955.0  qSlicerApplication::notify(QObject*, QEvent*)
 111 QtWidgets 38955.0  QApplication::notify(QObject*, QEvent*)
 110 QtWidgets 38955.0  QApplicationPrivate::notify_helper(QObject*, QEvent*)
 109 QtWidgets 38955.0  QFrame::event(QEvent*)
 108 QtWidgets 38955.0  QWidget::event(QEvent*)
 107 QtWidgets 38955.0  0x10cfe6960
 106 QtWidgets 38955.0  0x10cfe7320
 105 QtWidgets 38955.0  QWidget::setGeometry(QRect const&amp;)
 104 QtWidgets 38955.0  QWidgetPrivate::setGeometry_sys(int, int, int, int, bool)
 103 QtCore 38955.0  QCoreApplication::notifyInternal2(QObject*, QEvent*)
 102 libqSlicerBaseQTGUI.dylib 38955.0  qSlicerApplication::notify(QObject*, QEvent*)
 101 QtWidgets 38955.0  QApplication::notify(QObject*, QEvent*)
 100 QtWidgets 38955.0  QApplicationPrivate::notify_helper(QObject*, QEvent*)
  99 QtWidgets 38955.0  QLayoutPrivate::doResize()
  98 QtWidgets 38955.0  QBoxLayout::setGeometry(QRect const&amp;)
  97 QtWidgets 38955.0  QWidgetItem::setGeometry(QRect const&amp;)
  96 QtWidgets 38955.0  QWidget::setGeometry(QRect const&amp;)
  95 QtWidgets 38955.0  QWidgetPrivate::setGeometry_sys(int, int, int, int, bool)
  94 QtCore 38955.0  QCoreApplication::notifyInternal2(QObject*, QEvent*)
  93 libqSlicerBaseQTGUI.dylib 38955.0  qSlicerApplication::notify(QObject*, QEvent*)
  92 QtWidgets 38955.0  QApplication::notify(QObject*, QEvent*)
  91 QtWidgets 38955.0  QApplicationPrivate::notify_helper(QObject*, QEvent*)
  90 QtWidgets 38955.0  QLayoutPrivate::doResize()
  89 QtWidgets 38955.0  QBoxLayout::setGeometry(QRect const&amp;)
  88 QtWidgets 38955.0  QWidgetItem::setGeometry(QRect const&amp;)
  87 QtWidgets 38955.0  QWidget::setGeometry(QRect const&amp;)
  86 QtWidgets 38955.0  QWidgetPrivate::setGeometry_sys(int, int, int, int, bool)
  85 QtCore 38955.0  QCoreApplication::notifyInternal2(QObject*, QEvent*)
  84 libqSlicerBaseQTGUI.dylib 38955.0  qSlicerApplication::notify(QObject*, QEvent*)
  83 QtWidgets 38955.0  QApplication::notify(QObject*, QEvent*)
  82 QtWidgets 38955.0  QApplicationPrivate::notify_helper(QObject*, QEvent*)
  81 QtWidgets 38955.0  QLayoutPrivate::doResize()
  80 QtWidgets 38955.0  QBoxLayout::setGeometry(QRect const&amp;)
  79 QtWidgets 38955.0  QWidgetItem::setGeometry(QRect const&amp;)
  78 QtWidgets 38955.0  QWidget::setGeometry(QRect const&amp;)
  77 QtWidgets 38955.0  QWidgetPrivate::setGeometry_sys(int, int, int, int, bool)
  76 QtCore 38955.0  QCoreApplication::notifyInternal2(QObject*, QEvent*)
  75 libqSlicerBaseQTGUI.dylib 38955.0  qSlicerApplication::notify(QObject*, QEvent*)
  74 QtWidgets 38955.0  QApplication::notify(QObject*, QEvent*)
  73 QtWidgets 38955.0  QApplicationPrivate::notify_helper(QObject*, QEvent*)
  72 QtWidgets 38955.0  QLayoutPrivate::doResize()
  71 QtWidgets 38955.0  QBoxLayout::setGeometry(QRect const&amp;)
  70 QtWidgets 38955.0  QWidgetItem::setGeometry(QRect const&amp;)
  69 QtWidgets 38955.0  QWidget::setGeometry(QRect const&amp;)
  68 QtWidgets 38955.0  QWidgetPrivate::setGeometry_sys(int, int, int, int, bool)
  67 QtCore 38955.0  QCoreApplication::notifyInternal2(QObject*, QEvent*)
  66 libqSlicerBaseQTGUI.dylib 38955.0  qSlicerApplication::notify(QObject*, QEvent*)
  65 QtWidgets 38955.0  QApplication::notify(QObject*, QEvent*)
  64 QtWidgets 38955.0  QApplicationPrivate::notify_helper(QObject*, QEvent*)
  63 QtCore 38955.0  QCoreApplicationPrivate::sendThroughObjectEventFilters(QObject*, QEvent*)
  62 libCTKVisualizationVTKWidgets.0.1.dylib 38955.0  ctkVTKSliceView::eventFilter(QObject*, QEvent*)
  61 libCTKVisualizationVTKWidgets.0.1.dylib 38955.0  ctkVTKSliceView::resized(QSize const&amp;)
  60 QtCore 38955.0  0x10dc0fab0
  59 libqMRMLWidgets.dylib 38955.0  qMRMLSliceWidgetPrivate::setSliceViewSize(QSize const&amp;)
  58 libMRMLLogic.dylib 38955.0  vtkMRMLSliceLogic::ResizeSliceNode(double, double)
  57 libMRMLCore.dylib 38955.0  vtkMRMLNode::InvokePendingModifiedEvent()
  56 libvtkCommon-9.0.1.dylib 38955.0  vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*)
  55 libvtkCommon-9.0.1.dylib 38955.0  vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
  54 libMRMLCore.dylib 38955.0  vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*)
  53 libMRMLCore.dylib 38955.0  vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*)
  52 libvtkCommon-9.0.1.dylib 38955.0  vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
  51 libMRMLLogic.dylib 38955.0  vtkMRMLAbstractLogic::MRMLNodesCallback(vtkObject*, unsigned long, void*, void*)
  50 libMRMLLogic.dylib 38955.0  vtkMRMLSliceLogic::OnMRMLNodeModified(vtkMRMLNode*)
  49 libMRMLLogic.dylib 38955.0  vtkMRMLSliceLogic::SetSliceExtentsToSliceNode()
  48 libMRMLCore.dylib 38955.0  vtkMRMLSliceNode::UpdateMatrices()
  47 libMRMLCore.dylib 38955.0  vtkMRMLNode::InvokePendingModifiedEvent()
  46 libvtkCommon-9.0.1.dylib 38955.0  vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*)
  45 libvtkCommon-9.0.1.dylib 38955.0  vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
  44 libMRMLCore.dylib 38955.0  vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*)
  43 libMRMLCore.dylib 38955.0  vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*)
  42 libvtkCommon-9.0.1.dylib 38955.0  vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
  41 libMRMLLogic.dylib 38955.0  vtkMRMLAbstractLogic::MRMLNodesCallback(vtkObject*, unsigned long, void*, void*)
  40 libMRMLLogic.dylib 38955.0  vtkMRMLAbstractLogic::InvokePendingModifiedEvent()
  39 libvtkCommon-9.0.1.dylib 38955.0  vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*)
  38 libvtkCommon-9.0.1.dylib 38955.0  vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
  37 libMRMLCore.dylib 38955.0  vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*)
  36 libMRMLCore.dylib 38955.0  vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*)
  35 libvtkCommon-9.0.1.dylib 38955.0  vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
  34 libMRMLLogic.dylib 38955.0  vtkMRMLAbstractLogic::MRMLLogicsCallback(vtkObject*, unsigned long, void*, void*)
  33 libMRMLLogic.dylib 38955.0  vtkMRMLSliceLogic::ProcessMRMLLogicsEvents()
  32 libvtkCommon-9.0.1.dylib 38955.0  vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*)
  31 libvtkCommon-9.0.1.dylib 38955.0  vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
  30 libMRMLCore.dylib 38955.0  vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*)
  29 libMRMLCore.dylib 38955.0  vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*)
  28 libvtkCommon-9.0.1.dylib 38955.0  vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
  27 libCTKVisualizationVTKCore.0.1.dylib 38955.0  ctkVTKConnectionPrivate::execute(vtkObject*, unsigned long, void*, void*)
  26 libCTKVisualizationVTKCore.0.1.dylib 38955.0  ctkVTKConnection::emitExecute(vtkObject*, void*, unsigned long, void*)
  25 QtCore 38955.0  0x10dc0fab0
  24 libqSlicerBaseQTGUI.dylib 38955.0  qSlicerApplication::setRenderPaused(bool)
  23 libqMRMLWidgets.dylib 38955.0  qMRMLLayoutManager::setRenderPaused(bool)
  22 libCTKVisualizationVTKWidgets.0.1.dylib 38955.0  ctkVTKAbstractView::setRenderPaused(bool)
  21 libCTKVisualizationVTKWidgets.0.1.dylib 38955.0  ctkVTKAbstractView::resumeRender()
  20 libvtkOpenGL-9.0.1.dylib 38955.0  vtkGenericOpenGLRenderWindow::Render()
  19 libvtkOpenGL-9.0.1.dylib 38955.0  vtkOpenGLRenderWindow::Render()
  18 libvtkRendering-9.0.1.dylib 38955.0  vtkRenderWindow::Render()
  17 libvtkRendering-9.0.1.dylib 38955.0  vtkRenderWindow::DoStereoRender()
  16 libvtkRendering-9.0.1.dylib 38955.0  vtkRendererCollection::Render()
  15 libvtkRendering-9.0.1.dylib 38955.0  vtkRenderer::Render()
  14 libvtkRendering-9.0.1.dylib 38559.0  vtkRenderer::AllocateTime()
  13 libvtkRendering-9.0.1.dylib 38559.0  vtkFrustumCoverageCuller::Cull(vtkRenderer*, vtkProp**, int&amp;, int&amp;)
  12 libvtkRendering-9.0.1.dylib 38559.0  vtkActor::GetBounds()
  11 libvtkRendering-9.0.1.dylib 38559.0  vtkPolyDataMapper::GetBounds()
  10 libvtkCommon-9.0.1.dylib 38559.0  vtkAlgorithm::UpdatePiece(int, int, int, int const*)
   9 libvtkCommon-9.0.1.dylib 38559.0  vtkAlgorithm::Update(vtkInformation*)
   8 libvtkCommon-9.0.1.dylib 38559.0  vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector*)
   7 libvtkCommon-9.0.1.dylib 38559.0  vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*)
   6 libvtkCommon-9.0.1.dylib 38559.0  vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*)
   5 libvtkCommon-9.0.1.dylib 38559.0  vtkCompositeDataPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*)
   4 libvtkCommon-9.0.1.dylib 38559.0  vtkDemandDrivenPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*)
   3 libvtkCommon-9.0.1.dylib 38559.0  vtkExecutive::CallAlgorithm(vtkInformation*, int, vtkInformationVector**, vtkInformationVector*)
   2 libvtkFilters-9.0.1.dylib 38559.0  vtkClipPolyData::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*)
   1 libvtkCommon-9.0.1.dylib 36972.0  vtkTriangle::Clip(double, vtkDataArray*, vtkIncrementalPointLocator*, vtkCellArray*, vtkPointData*, vtkPointData*, vtkCellData*, long long, vtkCellData*, int)
   0 libvtkCommon-9.0.1.dylib 35326.0  vtkMergePoints::InsertUniquePoint(double const*, long long&amp;)</code></pre>

---

## Post #2 by @pieper (2021-10-18 20:13 UTC)

<p>Yes, it makes sense that there would be an update each time the window size changes since the slice planes are used to perform the clipping.  But since only the translation and orientation are used, this is obviously not needed when only the slice view size changes.  If someone has time and to desire, there could be some logic added to the model display pipeline to check if things have really changed before re-running the clipping.  It wouldn’t be a huge change but it would be in the C++ code and require some testing.</p>

---

## Post #3 by @lassoan (2021-10-19 04:26 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="20208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>have a relatively complex model (20 million polys).</p>
</blockquote>
</aside>
<p>This is not just relatively complex, but extremely complex. A basic mesh is a few 10k points, a complex mesh is 100k. 20 million is just crazy (but I guess it looks really cool). It is amazing that things work at all. In such extreme use cases it is expected that you find new performance bottlenecks that you need to fix. For example, a few extra redraw may take a few hundred milliseconds for most people, but for your data it may mean extra ten seconds.</p>

---

## Post #4 by @muratmaga (2021-10-19 05:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="20208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is not just relatively complex, but extremely complex. A basic mesh is a few 10k points, a complex mesh is 100k. 20 million is just crazy (but I guess it looks really cool). It is amazing that things work at all. In such extreme use cases it is expected that you find new performance bottlenecks that you need to fix. For example, a few extra redraw may take a few hundred milliseconds for most people, but for your data it may mean extra ten seconds.</p>
</blockquote>
</aside>
<p>I can’t speak for <a class="mention" href="/u/hherhold">@hherhold</a>, but the general issue is downsampling data from high resolution microCT scans rarely result in ‘good enough’ models at 100K range.  Along the way quite a bit of detail is lost, (usually thin structures such as bug limbs). I would say 20M polygon model is indeed on the quite high side, but it would be great to have really good performance support for models in the 500-1000K polygon range in Slicer.  I wouldn’t call that range extreme anymore, it is quite routine.</p>

---

## Post #5 by @hherhold (2021-10-20 12:04 UTC)

<p>Yeah, unfortunately 20 million polys isn’t even my most complex model. And <a class="mention" href="/u/muratmaga">@muratmaga</a> is correct - downsampling these scans (insects) does result in data loss.</p>
<p>500k to 1M polys is very useable in slicer depending on CPU and graphics card.</p>
<p>Thanks for the info and insights!</p>

---
