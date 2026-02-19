---
topic_id: 1711
title: "Crash When Using Volumes Module On Windows 7 After 4 9 Versi"
date: 2017-12-23
url: https://discourse.slicer.org/t/1711
---

# Crash when using Volumes module on Windows 7 after 4.9 version

**Topic ID**: 1711
**Date**: 2017-12-23
**URL**: https://discourse.slicer.org/t/crash-when-using-volumes-module-on-windows-7-after-4-9-version/1711

---

## Post #1 by @timeanddoctor (2017-12-23 02:42 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2c33dd9a5b555b03c10b15cb7e4c2946ddd633d.jpeg" data-download-href="/uploads/short-url/rMWVOpU5SXZ0dRR7GrwOKCYBXNr.jpg?dl=1" title="2017-12-23_103535" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2c33dd9a5b555b03c10b15cb7e4c2946ddd633d_2_690x383.jpg" alt="2017-12-23_103535" data-base62-sha1="rMWVOpU5SXZ0dRR7GrwOKCYBXNr" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2c33dd9a5b555b03c10b15cb7e4c2946ddd633d_2_690x383.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2c33dd9a5b555b03c10b15cb7e4c2946ddd633d_2_1035x574.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2c33dd9a5b555b03c10b15cb7e4c2946ddd633d.jpeg 2x" data-dominant-color="8C888B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2017-12-23_103535</span><span class="informations">1366×760 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-12-23 05:11 UTC)

<p>I could not reproduce the crash.</p>
<p>Do you have this problem with all volumes that you are trying to visualize? For example, does everything work well wit MRHead and CTChest sample data sets?</p>

---

## Post #3 by @timeanddoctor (2017-12-23 06:23 UTC)

<p>Thank you very much.<br>
The crash phenomenon never happened for the Volumes module by the sample data.<br>
Hum, maybe the problem is from my data. But I still couldnot understand well that I can deal with it in 4.6 version successfully.</p>

---

## Post #4 by @pieper (2017-12-23 14:27 UTC)

<p>If it’s possible to share data that reproduces the crash we’d like to fix it.  Thanks for the report.</p>

---

## Post #5 by @pieper (2017-12-23 16:37 UTC)

<p>Thanks for sending me the data to check - I was able to replicate the issue on Slicer 4.8 on the mac. and also on a build local build with Qt5/vtk9 on mac, but not with a local build with Qt4/vtk7. The stack trace is below, but it’s not clear to me what is going on.</p>
<p>If I save the data as nrrd and then load it I am able to read it and then go into the volumes module.</p>
<p>I suspect there is an issue with the nifti header that causes a memory corruption and that leads to the crash.  How was the nii.gz file created?</p>
<pre><code class="lang-auto">Process:               Slicer [76322]
Path:                  /Applications/Slicer-4.8.0.app/Contents/MacOS/Slicer
Identifier:            ???
Version:               4.8.0 (4.8.0)
Code Type:             X86-64 (Native)
Parent Process:        ??? [1]
Responsible:           Slicer [76322]
User ID:               501

Date/Time:             2017-12-23 11:24:24.795 -0500
OS Version:            Mac OS X 10.13.2 (17C88)
Report Version:        12
Anonymous UUID:        AE9D173E-A1E8-E500-62F7-C31D0E540E6E


Time Awake Since Boot: 320000 seconds

System Integrity Protection: enabled

Crashed Thread:        0  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_CRASH (SIGABRT)
Exception Codes:       0x0000000000000000, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Application Specific Information:
abort() called
*** error for object 0x111e7e800: incorrect checksum for freed object - object was probably modified after being freed.
 

Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   libsystem_kernel.dylib        	0x00007fff63fdce3e __pthread_kill + 10
1   libsystem_pthread.dylib       	0x00007fff6411b150 pthread_kill + 333
2   libsystem_c.dylib             	0x00007fff63f39312 abort + 127
3   libsystem_malloc.dylib        	0x00007fff64041b28 szone_error + 596
4   libsystem_malloc.dylib        	0x00007fff6404313f small_free_list_remove_ptr_no_clear + 790
5   libsystem_malloc.dylib        	0x00007fff64037191 small_malloc_from_free_list + 403
6   libsystem_malloc.dylib        	0x00007fff6403589d szone_malloc_should_clear + 1600
7   libsystem_malloc.dylib        	0x00007fff64035201 malloc_zone_malloc + 103
8   libsystem_malloc.dylib        	0x00007fff640377cf realloc + 96
9   QtGui                         	0x00000001034b4ffb QTextEngine::LayoutData::reallocate(int) + 171
10  QtGui                         	0x00000001034ae71d QTextEngine::attributes() const + 109
11  QtGui                         	0x00000001034c040b QTextLine::layout_helper(int) + 411
12  QtGui                         	0x00000001035533d0 QCommonStylePrivate::viewItemSize(QStyleOptionViewItemV4 const*, int) const + 544
13  QtGui                         	0x0000000103553ecd QCommonStylePrivate::viewItemLayout(QStyleOptionViewItemV4 const*, QRect*, QRect*, QRect*, bool) const + 109
14  QtGui                         	0x0000000103564fab QCommonStyle::sizeFromContents(QStyle::ContentsType, QStyleOption const*, QSize const&amp;, QWidget const*) const + 1595
15  QtGui                         	0x00000001035e7300 QWindowsStyle::sizeFromContents(QStyle::ContentsType, QStyleOption const*, QSize const&amp;, QWidget const*) const + 304
16  QtGui                         	0x00000001035da1d3 QCleanlooksStyle::sizeFromContents(QStyle::ContentsType, QStyleOption const*, QSize const&amp;, QWidget const*) const + 35
17  QtGui                         	0x00000001037f452e QStyledItemDelegate::sizeHint(QStyleOptionViewItem const&amp;, QModelIndex const&amp;) const + 254
18  QtGui                         	0x0000000103785999 QTreeView::indexRowSizeHint(QModelIndex const&amp;) const + 969
19  QtGui                         	0x0000000103785aa1 QTreeViewPrivate::itemHeight(int) const + 113
20  QtGui                         	0x0000000103785cb8 QTreeViewPrivate::updateScrollBars() + 200
21  QtGui                         	0x0000000103791f5c QTreeView::updateGeometries() + 476
22  QtGui                         	0x0000000103746fde QAbstractItemView::doItemsLayout() + 46
23  QtGui                         	0x000000010378c7fe QTreeView::doItemsLayout() + 750
24  QtGui                         	0x00000001037877da QTreeView::visualRect(QModelIndex const&amp;) const + 122
25  QtGui                         	0x0000000103746a18 QAbstractItemView::setCurrentIndex(QModelIndex const&amp;) + 232
26  libqMRMLWidgets.dylib         	0x000000010062511b qMRMLNodeComboBox::setCurrentNodeID(QString const&amp;) + 587
27  libqMRMLWidgets.dylib         	0x00000001006240b3 qMRMLNodeComboBox::setCurrentNode(vtkMRMLNode*) + 67
28  libqSlicerVolumesModuleWidgets.dylib	0x000000012c8d51d5 qSlicerScalarVolumeDisplayWidget::updateWidgetFromMRML() + 149
29  libqSlicerVolumesModuleWidgets.dylib	0x000000012c8d5124 qSlicerScalarVolumeDisplayWidget::setMRMLVolumeNode(vtkMRMLScalarVolumeNode*) + 484
30  libqSlicerVolumesModuleWidgets.dylib	0x000000012c8d9816 qSlicerVolumeDisplayWidget::setMRMLVolumeNode(vtkMRMLNode*) + 486
31  QtCore                        	0x0000000103f4b6ec QMetaObject::activate(QObject*, QMetaObject const*, int, void**) + 2348
32  libqMRMLWidgets.dylib         	0x00000001006ae37d qMRMLNodeComboBox::currentNodeChanged(vtkMRMLNode*) + 61
33  libqMRMLWidgets.dylib         	0x00000001006248d1 qMRMLNodeComboBox::emitCurrentNodeChanged() + 65
34  libqMRMLWidgets.dylib         	0x00000001006ae035 qMRMLNodeComboBox::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) + 837
35  QtCore                        	0x0000000103f4b6ec QMetaObject::activate(QObject*, QMetaObject const*, int, void**) + 2348
36  QtGui                         	0x000000010360a5d2 QComboBoxPrivate::_q_emitCurrentIndexChanged(QModelIndex const&amp;) + 146
37  QtGui                         	0x000000010360f8e5 QComboBoxPrivate::setCurrentIndex(QModelIndex const&amp;) + 741
38  QtGui                         	0x000000010360e435 QComboBoxPrivate::_q_rowsInserted(QModelIndex const&amp;, int, int) + 357
39  QtGui                         	0x0000000103614592 QComboBox::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) + 802
40  QtCore                        	0x0000000103f4b6ec QMetaObject::activate(QObject*, QMetaObject const*, int, void**) + 2348
41  QtCore                        	0x0000000103f966be QAbstractItemModel::rowsInserted(QModelIndex const&amp;, int, int) + 78
42  QtCore                        	0x0000000103f2bd73 QAbstractItemModel::endInsertRows() + 83
43  QtGui                         	0x00000001037d286a QSortFilterProxyModelPrivate::insert_source_items(QVector&lt;int&gt;&amp;, QVector&lt;int&gt;&amp;, QVector&lt;int&gt; const&amp;, QModelIndex const&amp;, Qt::Orientation, bool) + 666
44  QtGui                         	0x00000001037d3005 QSortFilterProxyModelPrivate::source_items_inserted(QModelIndex const&amp;, int, int, Qt::Orientation) + 1333
45  QtGui                         	0x00000001037d520b QSortFilterProxyModelPrivate::_q_sourceRowsInserted(QModelIndex const&amp;, int, int) + 27
46  QtGui                         	0x00000001037d8395 QSortFilterProxyModel::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) + 581
47  QtCore                        	0x0000000103f4b6ec QMetaObject::activate(QObject*, QMetaObject const*, int, void**) + 2348
48  QtCore                        	0x0000000103f966be QAbstractItemModel::rowsInserted(QModelIndex const&amp;, int, int) + 78
49  QtCore                        	0x0000000103f2bd73 QAbstractItemModel::endInsertRows() + 83
50  QtGui                         	0x00000001037dfa34 QStandardItemPrivate::insertRows(int, int, QList&lt;QStandardItem*&gt; const&amp;) + 836
51  QtGui                         	0x00000001037e127d QStandardItem::insertRow(int, QList&lt;QStandardItem*&gt; const&amp;) + 77
52  libqMRMLWidgets.dylib         	0x000000010064a941 qMRMLSceneModel::insertNode(vtkMRMLNode*, QStandardItem*, int) + 353
53  libqMRMLWidgets.dylib         	0x000000010064a692 qMRMLSceneModelPrivate::insertNode(vtkMRMLNode*, int) + 706
54  libqMRMLWidgets.dylib         	0x000000010064a28f qMRMLSceneModel::populateScene() + 79
55  libqMRMLWidgets.dylib         	0x000000010064a0b4 qMRMLSceneModel::updateScene() + 2068
56  libqMRMLWidgets.dylib         	0x00000001006483df qMRMLSceneModel::setMRMLScene(vtkMRMLScene*) + 63
57  libqMRMLWidgets.dylib         	0x0000000100624cef qMRMLNodeComboBox::setMRMLScene(vtkMRMLScene*) + 143
58  libqMRMLWidgets.dylib         	0x00000001006adf25 qMRMLNodeComboBox::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) + 565
59  QtCore                        	0x0000000103f4b6ec QMetaObject::activate(QObject*, QMetaObject const*, int, void**) + 2348
60  libqSlicerBaseQTGUI.dylib     	0x00000001003f47bd qSlicerWidget::mrmlSceneChanged(vtkMRMLScene*) + 61
61  libqSlicerBaseQTCore.dylib    	0x0000000100c51f69 qSlicerAbstractCoreModule::createNewWidgetRepresentation() + 89
62  libqSlicerBaseQTCore.dylib    	0x0000000100c51ef8 qSlicerAbstractCoreModule::widgetRepresentation() + 24
63  libqSlicerBaseQTGUI.dylib     	0x0000000100377a99 qSlicerApplication::nodeModule(vtkMRMLNode*) const + 1417
64  libqSlicerBaseQTGUI.dylib     	0x0000000100378411 qSlicerApplication::openNodeModule(vtkMRMLNode*) + 49
65  libqSlicerSubjectHierarchyModuleWidgets.dylib	0x000000012a363753 qSlicerSubjectHierarchyAbstractPlugin::editProperties(long long) + 67
66  libqSlicerSubjectHierarchyModuleWidgets.dylib	0x000000012a35cfcf qMRMLSubjectHierarchyTreeView::editCurrentItem() + 351
67  libqSlicerSubjectHierarchyModuleWidgets.dylib	0x000000012a3836bc qMRMLSubjectHierarchyTreeView::qt_static_metacall(QObject*, QMetaObject::Call, int, void**) + 460
68  QtCore                        	0x0000000103f4b6ec QMetaObject::activate(QObject*, QMetaObject const*, int, void**) + 2348
69  QtGui                         	0x000000010328198c QAction::activate(QAction::ActionEvent) + 236
70  QtGui                         	0x000000010367ba0d QMenuPrivate::activateCausedStack(QList&lt;QPointer&lt;QWidget&gt; &gt; const&amp;, QAction*, QAction::ActionEvent, bool) + 77
71  QtGui                         	0x000000010367a4b9 QMenuPrivate::activateAction(QAction*, QAction::ActionEvent, bool) + 457
72  QtGui                         	0x000000010367ecea QMenu::mouseReleaseEvent(QMouseEvent*) + 218
73  QtGui                         	0x00000001032dc626 QWidget::event(QEvent*) + 662
74  QtGui                         	0x000000010367f19d QMenu::event(QEvent*) + 765
75  QtGui                         	0x000000010328abf2 QApplicationPrivate::notify_helper(QObject*, QEvent*) + 258
76  QtGui                         	0x000000010328c36b QApplication::notify(QObject*, QEvent*) + 1179
77  libqSlicerBaseQTGUI.dylib     	0x0000000100376983 qSlicerApplication::notify(QObject*, QEvent*) + 19
78  QtCore                        	0x0000000103f34cd3 QCoreApplication::notifyInternal(QObject*, QEvent*) + 115
79  QtGui                         	0x000000010328b52a QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&lt;QWidget&gt;&amp;, bool) + 426
80  QtGui                         	0x0000000103237eda qt_mac_handleMouseEvent(NSEvent*, QEvent::Type, Qt::MouseButton, QWidget*, bool) + 1018
81  com.apple.AppKit              	0x00007fff3a4aa422 -[NSWindow(NSEventRouting) _reallySendEvent:isDelayedEvent:] + 1961
82  com.apple.AppKit              	0x00007fff3a4a985c -[NSWindow(NSEventRouting) sendEvent:] + 497
83  QtGui                         	0x0000000103227bbf -[QCocoaPanel sendEvent:] + 111
84  com.apple.AppKit              	0x00007fff3a30a617 -[NSApplication(NSEvent) sendEvent:] + 307
85  QtGui                         	0x00000001032341ef -[QNSApplication sendEvent:] + 95
86  com.apple.AppKit              	0x00007fff39b6bd9d -[NSApplication run] + 812
87  QtGui                         	0x000000010323d34a QEventDispatcherMac::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 474
88  QtCore                        	0x0000000103f31df5 QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 501
89  QtGui                         	0x000000010367da27 QMenu::exec(QPoint const&amp;, QAction*) + 103
90  libqSlicerSubjectHierarchyModuleWidgets.dylib	0x000000012a3598d2 qMRMLSubjectHierarchyTreeView::mousePressEvent(QMouseEvent*) + 226
91  QtGui                         	0x00000001032dc612 QWidget::event(QEvent*) + 642
92  QtGui                         	0x000000010363d607 QFrame::event(QEvent*) + 183
93  QtGui                         	0x00000001036bf16c QAbstractScrollArea::viewportEvent(QEvent*) + 108
94  QtGui                         	0x0000000103747cca QAbstractItemView::viewportEvent(QEvent*) + 1162
95  QtGui                         	0x00000001037883b1 QTreeView::viewportEvent(QEvent*) + 225
96  QtGui                         	0x00000001036bf975 QAbstractScrollAreaFilter::eventFilter(QObject*, QEvent*) + 37
97  QtCore                        	0x0000000103f34fe0 QCoreApplicationPrivate::sendThroughObjectEventFilters(QObject*, QEvent*) + 128
98  QtGui                         	0x000000010328abdd QApplicationPrivate::notify_helper(QObject*, QEvent*) + 237
99  QtGui                         	0x000000010328c36b QApplication::notify(QObject*, QEvent*) + 1179
100 libqSlicerBaseQTGUI.dylib     	0x0000000100376983 qSlicerApplication::notify(QObject*, QEvent*) + 19
101 QtCore                        	0x0000000103f34cd3 QCoreApplication::notifyInternal(QObject*, QEvent*) + 115
102 QtGui                         	0x000000010328b52a QApplicationPrivate::sendMouseEvent(QWidget*, QMouseEvent*, QWidget*, QWidget*, QWidget**, QPointer&lt;QWidget&gt;&amp;, bool) + 426
103 QtGui                         	0x0000000103237eda qt_mac_handleMouseEvent(NSEvent*, QEvent::Type, Qt::MouseButton, QWidget*, bool) + 1018
104 com.apple.AppKit              	0x00007fff3a4ab029 -[NSWindow(NSEventRouting) _reallySendEvent:isDelayedEvent:] + 5040
105 com.apple.AppKit              	0x00007fff3a4a985c -[NSWindow(NSEventRouting) sendEvent:] + 497
106 QtGui                         	0x000000010322f41f -[QCocoaWindow sendEvent:] + 111
107 com.apple.AppKit              	0x00007fff3a30afa3 -[NSApplication(NSEvent) sendEvent:] + 2751
108 QtGui                         	0x00000001032341ef -[QNSApplication sendEvent:] + 95
109 com.apple.AppKit              	0x00007fff39b6bd9d -[NSApplication run] + 812
110 QtGui                         	0x000000010323d34a QEventDispatcherMac::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 474
111 QtCore                        	0x0000000103f31df5 QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) + 501
112 QtCore                        	0x0000000103f3524a QCoreApplication::exec() + 202
113                               	0x000000010003e349 main + 9769
114                               	0x000000010003bd14 start + 52

</code></pre>

---

## Post #6 by @lassoan (2017-12-23 20:58 UTC)

<p>The problem is that the file contains incorrectly computed scalar range (or maybe scalar range is computed somewhere incorrectly). When Volume’s module GUI is initialized, its histogram is computed. Histogram computation uses scalar range to determine histogram’s memory buffer size. If scalar range is incorrect then it writes outside the allocated buffer, causing memory corruption.</p>
<p>I’ve observed ctkVTKHistogram causing memory corruptions several times in the past but I could not pin down the issue until now.</p>
<p>I’ve created a pull request to fix the issue in CTK: <a href="https://github.com/commontk/CTK/pull/779">https://github.com/commontk/CTK/pull/779</a></p>
<p>Until it is fixed, you should remove the incorrect scalar range from images (e.g., by writing to a format that has human-readable header, such as nrrd, and remove scalar range information using a text editor).</p>

---

## Post #7 by @timeanddoctor (2017-12-24 09:33 UTC)

<p>Thanks for the prompt reply!<br>
The dataset of "nifti " was created by Mango A  free software. I had converted the format from DICOM due to its larger size.<br>
I think I should analysis DICOM by 3d slicer directly in the future avoiding unnecessary troulbe.</p>

---

## Post #8 by @pieper (2017-12-24 17:13 UTC)

<p>Thanks for the CTK fix <a class="mention" href="/u/lassoan">@lassoan</a>, it’s important to avoid the memory corruption.</p>
<p>In this case the source of the error is in vtkITK.  This code uses cal_min and cal_max to set the scalar range for a nifti file:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/11d9358cb95ec072ed4807c783d2f18d3e33db3f/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L937-L939" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/11d9358cb95ec072ed4807c783d2f18d3e33db3f/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L937-L939" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/11d9358cb95ec072ed4807c783d2f18d3e33db3f/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L937-L939</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="937" style="counter-reset: li-counter 936 ;">
<li>// https://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields_pages/cal_maxmin.html</li>
<li>range_keys[0] = "cal_min";</li>
<li>range_keys[1] = "cal_max";</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>But we should not be relying on that being correctly populated in files we read (even documentation on what is meant to be in that field is hard to find and the nih link is currently dead).</p>
<p>The vtkITK code also uses fields from Meta and NRRD headers to set the scalar range and this is dangerous because other VTK probably code trusts this to do pointer arithmetic and other calculations.</p>
<p>I’d vote to remove this feature from vtkITK and let VTK compute the scalar range when needed.</p>

---

## Post #9 by @lassoan (2017-12-24 18:00 UTC)

<p>NIR project needed reading of scalar range from file. For them, computing scalar range increased time to display the image very significantly.</p>
<p>However, I completely agree that we cannot trust these values (crash if incorrect).</p>

---

## Post #10 by @pieper (2017-12-24 19:10 UTC)

<p>Looks like there’s been some optimization of CalculateScalarRange in recent VTK versions.</p>
<p>Would an estimated scalar range work for the NIR use case?  Typically sampling just a few percent of the image gives a robust estimate (and maybe the exact value could be calculated in a separate thread or something if needed).</p>

---

## Post #11 by @lassoan (2018-09-05 17:51 UTC)

<p>A post was split to a new topic: <a href="/t/websites-not-loading-correctly-after-using-volumes-module/3994">Websites not loading correctly after using volumes module</a></p>

---
