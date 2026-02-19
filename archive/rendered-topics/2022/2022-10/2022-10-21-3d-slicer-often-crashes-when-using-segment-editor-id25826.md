---
topic_id: 25826
title: "3D Slicer Often Crashes When Using Segment Editor"
date: 2022-10-21
url: https://discourse.slicer.org/t/25826
---

# 3D Slicer often crashes when using Segment Editor

**Topic ID**: 25826
**Date**: 2022-10-21
**URL**: https://discourse.slicer.org/t/3d-slicer-often-crashes-when-using-segment-editor/25826

---

## Post #1 by @torquil (2022-10-21 08:58 UTC)

<p>Hi! I am experience quite a lot of crashing when using the Segment Editor (newest 3D Slicer from today on Linux, but older versions also).</p>
<p>Typically it happens when I e.g. use “Keep largest island” or when using the scissor tool. On the terminal it says:</p>
<pre><code class="lang-auto">Switch to module:  "SegmentEditor"
QLayout::addChildLayout: layout "" already has a parent
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1
QXcbConnection: XCB error: 3 (BadWindow), sequence: 5047, resource id: 8397920, major code: 40 (TranslateCoords), minor code: 0
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
QList&lt;qSlicerFileWriter*&gt; qSlicerCoreIOManagerPrivate::writers(const IOFileType&amp;, const IOProperties&amp;, vtkMRMLScene*) const warning: Unable to find node with ID "" in the given scene.
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
QXcbConnection: XCB error: 3 (BadWindow), sequence: 9104, resource id: 8399650, major code: 40 (TranslateCoords), minor code: 0
QXcbConnection: XCB error: 3 (BadWindow), sequence: 9710, resource id: 8399398, major code: 40 (TranslateCoords), minor code: 0
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
QList&lt;qSlicerFileWriter*&gt; qSlicerCoreIOManagerPrivate::writers(const IOFileType&amp;, const IOProperties&amp;, vtkMRMLScene*) const warning: Unable to find node with ID "" in the given scene.
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
QXcbConnection: XCB error: 3 (BadWindow), sequence: 26881, resource id: 8400302, major code: 40 (TranslateCoords), minor code: 0
QXcbConnection: XCB error: 3 (BadWindow), sequence: 26944, resource id: 8400050, major code: 40 (TranslateCoords), minor code: 0
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
QList&lt;qSlicerFileWriter*&gt; qSlicerCoreIOManagerPrivate::writers(const IOFileType&amp;, const IOProperties&amp;, vtkMRMLScene*) const warning: Unable to find node with ID "" in the given scene.
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
QXcbConnection: XCB error: 3 (BadWindow), sequence: 43147, resource id: 8400954, major code: 40 (TranslateCoords), minor code: 0
QXcbConnection: XCB error: 3 (BadWindow), sequence: 43210, resource id: 8400702, major code: 40 (TranslateCoords), minor code: 0
QList&lt;qSlicerFileWriter*&gt; qSlicerCoreIOManagerPrivate::writers(const IOFileType&amp;, const IOProperties&amp;, vtkMRMLScene*) const warning: Unable to find node with ID "" in the given scene.
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
QXcbConnection: XCB error: 3 (BadWindow), sequence: 43404, resource id: 8401354, major code: 40 (TranslateCoords), minor code: 0
QXcbConnection: XCB error: 3 (BadWindow), sequence: 44638, resource id: 8401661, major code: 40 (TranslateCoords), minor code: 0
error: [/home/torquil/usr/slicer/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>

---

## Post #2 by @torquil (2022-10-21 12:00 UTC)

<p>It also happened just now when using the Flood filling tool, so maybe it is independent of which segmentation tool one is using. It also happens when using Slicer 5.0.3 on the same data.</p>

---

## Post #3 by @pieper (2022-10-21 12:43 UTC)

<p>Hmm, I don’t see crashing on my linux machines.  I also don’t get all those bad window messages so it may have to do with your desktop system or drivers.</p>

---

## Post #4 by @torquil (2022-10-21 13:21 UTC)

<p>You might be on to something. After cropping the volume I can do e.g. the flood filling operation without a crash, and the setSingleStep() error appears on the terminal output without Slicer crashing. So the appearance of that message is not in itself indicative of a crash. So perhaps the crash is related to something else.</p>
<p>Now I also see that Slicer can crash even without any error messages, e.g. when using the Flood Filling:</p>
<pre><code class="lang-auto">QLayout::addChildLayout: layout "" already has a parent
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1
QXcbConnection: XCB error: 3 (BadWindow), sequence: 10767, resource id: 8530827, major code: 40 (TranslateCoords), minor code: 0
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
QList&lt;qSlicerFileWriter*&gt; qSlicerCoreIOManagerPrivate::writers(const IOFileType&amp;, const IOProperties&amp;, vtkMRMLScene*) const warning: Unable to find node with ID "" in the given scene.
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
QXcbConnection: XCB error: 3 (BadWindow), sequence: 10946, resource id: 8530575, major code: 40 (TranslateCoords), minor code: 0
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1
error: [/home/torquil/usr/slicer/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>The messages from ctkSliderWidget was there long before the crash, so at the exact point in time of the crash, nothing was logged to the terminal. This happens with both the GPU and CPU volume rendering options in the Application settings. I did not have any data rendered in the 3d view. I use the “conventional” view, but I’m only working in the slice views.</p>
<p>Perhaps I have to use a debugger to get to the bottom of this problem.</p>

---

## Post #5 by @torquil (2022-10-21 20:02 UTC)

<p>When I try to do the exact same thing on 3D Slicer on windows (on the same computer), I also get a crash, but then with a pupop complaining about the following:</p>
<p>"The application has run out of memory… and so on.</p>
<p>If you have a repeatable sequence of steps that cause this message, please report the issue following the instructions available at <a href="http://www.slicer.org" rel="noopener nofollow ugc">http://www.slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: bad allocation"</p>
<p>When I then close the Slicer window, I get another popup:</p>
<p>"vtkDebugLeaks has detected LEAKS!<br>
Class “vtkCommand or subclass” has 1 instance still around.<br>
Class “class vtkBuffer has 1 instance still around.<br>
Class “vtkTypeint32Array” has 1 instance still around.”</p>
<p>But I don’t know if those memory leak warnings are real problems, perhaps just a consequence of the “out of memory” that happenede just before.</p>
<p>I will try to work with a lower voxel resolution now and see if that helps.</p>
<p>Best regards,<br>
Torquil Sørensen</p>

---

## Post #6 by @pieper (2022-10-21 20:07 UTC)

<p>Yes, the out of memory error is the key.  You can search for options like adding real memory, adding virtual memory, downsampling, etc.</p>

---
