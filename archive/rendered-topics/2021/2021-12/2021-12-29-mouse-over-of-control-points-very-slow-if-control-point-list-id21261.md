# Mouse over of control points very slow if control point list visible (segment with 20M+ polys)

**Topic ID**: 21261
**Date**: 2021-12-29
**URL**: https://discourse.slicer.org/t/mouse-over-of-control-points-very-slow-if-control-point-list-visible-segment-with-20m-polys/21261

---

## Post #1 by @hherhold (2021-12-29 13:08 UTC)

<p>MacOS 12.1, Slicer 12-19 nightly, MacBook Pro 16", 64MB ram, AMD Radeon Pro 5500M 8 GB.</p>
<p>I have a complex model/segmentation, well over 20 million polygons, and a markup list with about 200 control points. Just points, no curves or measurements, etc.</p>
<p>In the Markups module, if the list of control points is NOT visible, I can mouse-over points to change the name, etc. But if the list of control points IS visible, mousing over control points is VERY slow - it takes several seconds for the control point to change color, for example. This appears to be the case regardless of whether or not a segment or model is visible - I can make all segments and models not visible, so the screen is just control points, and mousing over is still very slow.</p>
<p>I don’t see control points highlighted or anything in the list during mouse-over. Are intersection tests being performed or something if the list is visible?</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #2 by @pieper (2021-12-30 20:34 UTC)

<p>Can you make a dummy scene, maybe small with just the point, that could be used for profiling this issue?  Probably there’s some kind of nested loop that causes a polynomially increasing slowdown for large numbers of points.</p>

---

## Post #3 by @hherhold (2021-12-31 18:37 UTC)

<p>I’ll see what I can do - I’m guessing any file with a ton of polys will work, with a couple of markup control points.</p>
<p>I’m also rebuilding from source (build I had was quite out of date) and I’ll run Instruments (MacOS) to profile it.</p>

---

## Post #4 by @pieper (2021-12-31 18:54 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="3" data-topic="21261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I’ll run Instruments (MacOS) to profile it.</p>
</blockquote>
</aside>
<p>Excellent - yes <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> let us know what  you find.</p>

---

## Post #5 by @hherhold (2022-01-01 13:39 UTC)

<p>Hopefully the formatting doesn’t get completely scrambled here… This is mouse-over-ing a control point with the control point list visible.</p>
<pre><code class="lang-auto">33.02 s  100.0%	0 s	 	Slicer (53375)
32.75 s   99.1%	0 s	 	 &lt;Unnamed Thread&gt; 0x296a39
32.75 s   99.1%	0 s	 	  &lt;Unknown Address&gt;
32.75 s   99.1%	0 s	 	   start
32.75 s   99.1%	0 s	 	    main
32.75 s   99.1%	0 s	 	     (anonymous namespace)::SlicerAppMain(int, char**)
32.75 s   99.1%	0 s	 	      qSlicerCoreApplication::exec()
32.75 s   99.1%	0 s	 	       QCoreApplication::exec()
32.75 s   99.1%	0 s	 	        QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;)
32.75 s   99.1%	0 s	 	         0x12fe0b3a0
32.75 s   99.1%	0 s	 	          -[NSApplication run]
22.00 ms    0.0%	0 s	 	           -[NSApplication _handleEvent:]
32.72 s   99.0%	0 s	 	           -[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:]
3.00 ms    0.0%	0 s	 	            -[NSEvent _initWithCGEvent:eventRef:]
1.00 ms    0.0%	0 s	 	            -[NSEvent dealloc]
1.00 ms    0.0%	0 s	 	            SendEventToEventTarget
32.72 s   99.0%	0 s	 	            _DPSNextEvent
32.72 s   99.0%	0 s	 	             _BlockUntilNextEventMatchingListInModeWithFilter
32.72 s   99.0%	0 s	 	              ReceiveNextEventCommon
2.00 ms    0.0%	0 s	 	               AcquireEventFromQueue
32.71 s   99.0%	1.00 ms	 	               RunCurrentEventLoopInMode
32.70 s   99.0%	0 s	 	                CFRunLoopRunSpecific
24.00 ms    0.0%	1.00 ms	 	                 __CFRunLoopDoObservers
32.67 s   98.9%	0 s	 	                 __CFRunLoopRun
2.00 ms    0.0%	0 s	 	                  CFAbsoluteTimeGetCurrent
1.00 ms    0.0%	0 s	 	                  CFDictionaryGetValue
4.00 ms    0.0%	0 s	 	                  __CFRunLoopDoBlocks
11.00 ms    0.0%	0 s	 	                  __CFRunLoopDoObservers
32.63 s   98.8%	0 s	 	                  __CFRunLoopDoSources0
1.00 ms    0.0%	0 s	 	                   CFSetApplyFunction
32.63 s   98.8%	0 s	 	                   __CFRunLoopDoSource0
32.63 s   98.8%	0 s	 	                    __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__
201.00 ms    0.6%	0 s	 	                     0x12fe0b020
32.43 s   98.2%	0 s	 	                     0x12fe0cf70
200.00 ms    0.6%	0 s	 	                      0x12fe0c750
32.23 s   97.6%	0 s	 	                      QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;)
32.23 s   97.6%	0 s	 	                       QGuiApplicationPrivate::processMouseEvent(QWindowSystemInterfacePrivate::MouseEvent*)
32.23 s   97.6%	0 s	 	                        QCoreApplication::notifyInternal2(QObject*, QEvent*)
32.23 s   97.6%	1.00 ms	 	                         qSlicerApplication::notify(QObject*, QEvent*)
32.23 s   97.5%	0 s	 	                          QApplication::notify(QObject*, QEvent*)
32.23 s   97.5%	0 s	 	                           QApplicationPrivate::notify_helper(QObject*, QEvent*)
32.23 s   97.5%	0 s	 	                            0x10bcec2f0
32.23 s   97.5%	0 s	 	                             0x10bced020
1.00 ms    0.0%	1.00 ms	 	                              QApplicationPrivate::modalState()
3.00 ms    0.0%	0 s	 	                              QApplicationPrivate::pickMouseReceiver(QWidget*, QPoint const&amp;, QPoint*, QEvent::Type, QFlags&lt;Qt::MouseButton&gt;, QWidget*, QWidget*)
32.22 s   97.5%	0 s	 	                              QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&lt;QWidget&gt;&amp;, bool, bool)
2.00 ms    0.0%	0 s	 	                               QApplicationPrivate::dispatchEnterLeave(QWidget*, QWidget*, QPointF const&amp;)
32.22 s   97.5%	0 s	 	                               QCoreApplication::notifyInternal2(QObject*, QEvent*)
32.22 s   97.5%	0 s	 	                                qSlicerApplication::notify(QObject*, QEvent*)
32.22 s   97.5%	0 s	 	                                 QApplication::notify(QObject*, QEvent*)
5.00 ms    0.0%	0 s	 	                                  0x10bce5f20
32.20 s   97.5%	0 s	 	                                  QApplicationPrivate::notify_helper(QObject*, QEvent*)
1.00 ms    0.0%	1.00 ms	 	                                   QCoreApplicationPrivate::sendThroughApplicationEventFilters(QObject*, QEvent*)
2.00 ms    0.0%	2.00 ms	 	                                   QCoreApplicationPrivate::sendThroughObjectEventFilters(QObject*, QEvent*)
1.00 ms    0.0%	0 s	 	                                   QCoreApplicationPrivate::threadRequiresCoreApplication()
32.15 s   97.3%	0 s	 	                                   QVTKOpenGLNativeWidget::event(QEvent*)
32.15 s   97.3%	0 s	 	                                    QVTKRenderWindowAdapter::handleEvent(QEvent*)
32.15 s   97.3%	0 s	 	                                     QVTKInteractorAdapter::ProcessEvent(QEvent*, vtkRenderWindowInteractor*)
1.00 ms    0.0%	0 s	 	                                      QMouseEvent::x() const
32.14 s   97.3%	0 s	 	                                      vtkObject::InvokeEvent(unsigned long, void*)
32.14 s   97.3%	1.00 ms	 	                                       vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*)
32.14 s   97.3%	1.00 ms	 	                                        vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
32.14 s   97.3%	0 s	 	                                         vtkMRMLViewInteractorStyle::CustomProcessEvents(vtkObject*, unsigned long, void*, void*)
168.00 ms    0.5%	0 s	 	                                          vtkInteractorStyle::ProcessEvents(vtkObject*, unsigned long, void*, void*)
31.97 s   96.8%	0 s	 	                                          vtkMRMLViewInteractorStyle::DelegateInteractionEventToDisplayableManagers(unsigned long)
31.97 s   96.8%	0 s	 	                                           vtkMRMLThreeDViewInteractorStyle::DelegateInteractionEventToDisplayableManagers(vtkEventData*)
2.00 ms    0.0%	0 s	 	                                            vtkMRMLInteractionEventData::SetAttributesFromInteractor(vtkRenderWindowInteractor*)
68.00 ms    0.2%	0 s	 	                                            vtkMRMLThreeDViewInteractorStyle::QuickPick(int, int, double*)
31.89 s   96.5%	0 s	 	                                            vtkMRMLViewInteractorStyle::DelegateInteractionEventDataToDisplayableManagers(vtkMRMLInteractionEventData*)
1.00 ms    0.0%	1.00 ms	 	                                             vtkEventData::GetType() const
4.00 ms    0.0%	0 s	 	                                             vtkMRMLAbstractDisplayableManager::SafeDownCast(vtkObjectBase*)
1.00 ms    0.0%	0 s	 	                                             vtkMRMLAbstractDisplayableManager::SetMouseCursor(int)
11.00 ms    0.0%	0 s	 	                                             vtkMRMLAnnotationDisplayableManager::CanProcessInteractionEvent(vtkMRMLInteractionEventData*, double&amp;)
6.00 ms    0.0%	0 s	 	                                             vtkMRMLApplicationLogic::PauseRender()
58.00 ms    0.1%	0 s	 	                                             vtkMRMLApplicationLogic::ResumeRender()
4.00 ms    0.0%	1.00 ms	 	                                             vtkMRMLCameraDisplayableManager::CanProcessInteractionEvent(vtkMRMLInteractionEventData*, double&amp;)
16.37 s   49.5%	0 s	 	                                             vtkMRMLMarkupsDisplayableManager::CanProcessInteractionEvent(vtkMRMLInteractionEventData*, double&amp;)
3.00 ms    0.0%	0 s	 	                                              vtkMRMLAbstractDisplayableManager::GetSelectionNode()
375.00 ms    1.1%	0 s	 	                                              vtkMRMLMarkupsDisplayableManager::FindClosestWidget(vtkMRMLInteractionEventData*, double&amp;)
16.00 s   48.4%	0 s	 	                                              vtkSlicerMarkupsWidget::Leave(vtkMRMLInteractionEventData*)
16.00 s   48.4%	0 s	 	                                               vtkMRMLMarkupsDisplayNode::SetActiveComponent(int, int, std::__1::basic_string&lt;char, std::__1::char_traits&lt;char&gt;, std::__1::allocator&lt;char&gt; &gt;)
16.00 s   48.4%	0 s	 	                                                vtkMRMLNode::Modified()
16.00 s   48.4%	0 s	 	                                                 vtkObject::Modified()
16.00 s   48.4%	0 s	 	                                                  vtkObject::InvokeEvent(unsigned long, void*)
16.00 s   48.4%	0 s	 	                                                   vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*)
16.00 s   48.4%	0 s	 	                                                    vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
16.00 s   48.4%	0 s	 	                                                     vtkEventBroker::Callback(vtkObject*, unsigned long, void*, void*)
16.00 s   48.4%	0 s	 	                                                      vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*)
16.00 s   48.4%	0 s	 	                                                       vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*)
16.00 s   48.4%	0 s	 	                                                        vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
1.00 ms    0.0%	0 s	 	                                                         ctkVTKConnectionPrivate::DoCallback(vtkObject*, unsigned long, void*, void*)
15.99 s   48.4%	0 s	 	                                                         vtkMRMLNode::MRMLCallback(vtkObject*, unsigned long, void*, void*)
15.99 s   48.4%	0 s	 	                                                          vtkMRMLMarkupsNode::ProcessMRMLEvents(vtkObject*, unsigned long, void*)
15.99 s   48.4%	0 s	 	                                                           vtkMRMLDisplayableNode::ProcessMRMLEvents(vtkObject*, unsigned long, void*)
15.99 s   48.4%	0 s	 	                                                            vtkObject::InvokeEvent(unsigned long, void*)
15.99 s   48.4%	0 s	 	                                                             vtkSubjectHelper::InvokeEvent(unsigned long, void*, vtkObject*)
15.99 s   48.4%	0 s	 	                                                              vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
15.99 s   48.4%	0 s	 	                                                               vtkEventBroker::Callback(vtkObject*, unsigned long, void*, void*)
15.99 s   48.4%	0 s	 	                                                                vtkEventBroker::ProcessEvent(vtkObservation*, vtkObject*, unsigned long, void*)
15.99 s   48.4%	0 s	 	                                                                 vtkEventBroker::InvokeObservation(vtkObservation*, unsigned long, void*)
15.99 s   48.4%	0 s	 	                                                                  vtkCallbackCommand::Execute(vtkObject*, unsigned long, void*)
15.97 s   48.3%	0 s	 	                                                                   ctkVTKConnectionPrivate::DoCallback(vtkObject*, unsigned long, void*, void*)
15.97 s   48.3%	0 s	 	                                                                    ctkVTKConnectionPrivate::execute(vtkObject*, unsigned long, void*, void*)
15.97 s   48.3%	0 s	 	                                                                     ctkVTKConnection::emitExecute(vtkObject*, void*, unsigned long, void*)
15.97 s   48.3%	0 s	 	                                                                      0x10da01bd0
15.97 s   48.3%	0 s	 	                                                                       qSlicerMarkupsModuleWidget::qt_static_metacall(QObject*, QMetaObject::Call, int, void**)
15.97 s   48.3%	0 s	 	                                                                        qSlicerMarkupsModuleWidget::onActiveMarkupsNodeDisplayModifiedEvent()
15.97 s   48.3%	0 s	 	                                                                         qSlicerMarkupsModuleWidget::updateWidgetFromMRML()
1.00 ms    0.0%	0 s	 	                                                                          QIcon::QIcon(QString const&amp;)
15.97 s   48.3%	0 s	 	                                                                          qSlicerMarkupsModuleWidget::updateRow(int)
15.88 s   48.0%	0 s	 	                                                                           0x10bf5d4c0
1.00 ms    0.0%	0 s	 	                                                                           &lt;Unknown Address&gt;
1.00 ms    0.0%	1.00 ms	 	                                                                           DYLD-STUB$$qMRMLSubjectHierarchyTreeView::d_func() const
1.00 ms    0.0%	0 s	 	                                                                           QFlags&lt;Qt::ItemFlag&gt;::operator&amp;(int) const
57.00 ms    0.1%	0 s	 	                                                                           QPixmap::load(QString const&amp;, char const*, QFlags&lt;Qt::ImageConversionFlag&gt;)
4.00 ms    0.0%	0 s	 	                                                                           QString::QString(char const*)
2.00 ms    0.0%	0 s	 	                                                                           QString::number(double, char, int)
1.00 ms    0.0%	1.00 ms	 	                                                                           QTableWidget::item(int, int) const
2.00 ms    0.0%	0 s	 	                                                                           QTableWidgetItem::QTableWidgetItem(QString const&amp;, int)
1.00 ms    0.0%	0 s	 	                                                                           QTableWidgetItem::setData(int, QVariant const&amp;)
1.00 ms    0.0%	0 s	 	                                                                           QTableWidgetItem::text() const
1.00 ms    0.0%	0 s	 	                                                                           operator new(unsigned long)
1.00 ms    0.0%	0 s	 	                                                                           qMRMLSubjectHierarchyTreeView::currentNode() const
1.00 ms    0.0%	0 s	 	                                                                           qSlicerMarkupsModuleWidgetPrivate::columnIndex(QString)
1.00 ms    0.0%	0 s	 	                                                                           qSlicerObject::mrmlScene() const
1.00 ms    0.0%	1.00 ms	 	                                                                           std::__1::basic_string&lt;char, std::__1::char_traits&lt;char&gt;, std::__1::allocator&lt;char&gt; &gt;::c_str() const
6.00 ms    0.0%	0 s	 	                                                                           vtkMRMLMarkupsNode::GetNthControlPointPositionWorld(int, double*)
7.00 ms    0.0%	0 s	 	                                                                           vtkMRMLScene::GetNodeByID(char const*)
1.00 ms    0.0%	1.00 ms	 	                                                                          vtkMRMLMarkupsNode::GetMarkupLabelFormat()
4.00 ms    0.0%	0 s	 	                                                                       qSlicerMarkupsPlaceWidget::qt_static_metacall(QObject*, QMetaObject::Call, int, void**)
18.00 ms    0.0%	0 s	 	                                                                   vtkMRMLAbstractLogic::MRMLNodesCallback(vtkObject*, unsigned long, void*, void*)
4.00 ms    0.0%	0 s	 	                                                               vtkMRMLSubjectHierarchyNode::ItemEventCallback(vtkObject*, unsigned long, void*, void*)

</code></pre>

---

## Post #6 by @pieper (2022-01-04 18:55 UTC)

<p>Yes, it seems that the GUI is getting refreshed on every mouse move event.  Probably this could be easily fixed by adding a <code>requestUpdate</code> similar to the <code>requestRender</code> methods on the render windows, so that multiple mouse moves are compressed to a single periodic update.  The logic wouldn’t need to be as complex as the <code>requestRender</code>, which ensure some minimum update rate, but could instead just use a <code>QTimer.singleShot</code> with a short timeout that would keep getting reset whenever a mouse move comes in and then calls <code>qSlicerMarkupsModuleWidget::updateWidgetFromMRML</code> when the timer fires.  We could add this just to the Markups, or could add this as a feature to one of the abstract classes.</p>

---
