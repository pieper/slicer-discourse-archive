# Slicer Preview crashes on slicer.util.resetSliceViews()

**Topic ID**: 40488
**Date**: 2024-12-03
**URL**: https://discourse.slicer.org/t/slicer-preview-crashes-on-slicer-util-resetsliceviews/40488

---

## Post #1 by @koeglfryderyk (2024-12-03 10:53 UTC)

<p>Slicer preview version: Slicer-5.7.0-2024-11-29-linux-amd64<br>
OS: Ubuntu 22.04.4 LTS</p>
<p>Slicer crashes ungracefully after calling <code>slicer.util.resetSliceViews()</code></p>
<p>Here is the log:</p>
<pre><code class="lang-auto">Python console user input: slicer.util.resetSliceViews()
error: [/home/fryderyk/Downloads/Slicer-5.7.0-2024-11-29-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>

---

## Post #2 by @pieper (2024-12-03 12:41 UTC)

<p>Thanks for the report.  I can replicate this crash on the current preview build if I make the call before loading a volume.  If I call it after loading a volume there is no crash.</p>

---

## Post #3 by @cpinter (2024-12-03 12:46 UTC)

<p>I cannot replicate this on Windows before or after loading a volume.</p>

---

## Post #4 by @pieper (2024-12-03 13:20 UTC)

<p>I can replicate this on a local mac build.  Here’s the stack trace:</p>
<pre><code class="lang-auto">Thread 0 Crashed::  Dispatch queue: com.apple.main-thread
0   libvtkCommon-9.2.9.2.dylib    	       0x12e0d6b3f vtkCollection::AddItem(vtkObject*) + 63
1   libMRMLLogic.dylib            	       0x10effa51a vtkMRMLSliceLogic::FitSliceToFirst(int, int) + 362
2   libqMRMLWidgets.dylib         	       0x10cd61215 qMRMLSliceControllerWidget::fitSliceToBackground() + 53
3   libqMRMLWidgets.dylib         	       0x10cd146eb qMRMLLayoutManager::resetSliceViews() + 187
4   libqMRMLWidgets.dylib         	       0x10cda4bbd qMRMLLayoutManager::qt_metacall(QMetaObject::Call, int, void**) + 125
5   libqSlicerBaseQTGUI.dylib     	       0x10cb0d03a qSlicerLayoutManager::qt_metacall(QMetaObject::Call, int, void**) + 42
6   libPythonQt.dylib             	       0x1112e191a PythonQtCallSlot(PythonQtClassInfo*, QObject*, _object*, bool, PythonQtSlotInfo*, void*, _object**, void**, PythonQtPassThisOwnershipType*) + 762
7   libPythonQt.dylib             	       0x1112e3328 PythonQtSlotFunction_CallImpl(PythonQtClassInfo*, QObject*, PythonQtSlotInfo*, _object*, _object*, void*, void**, PythonQtPassThisOwnershipType*) + 2184
8   libPythonQt.dylib             	       0x1112e2233 PythonQtMemberFunction_Call(PythonQtSlotInfo*, _object*, _object*, _object*) + 195
</code></pre>
<p>I’ll see if I can debug and suggest a fix</p>

---

## Post #5 by @pieper (2024-12-03 13:29 UTC)

<p>This fixes it: <a href="https://github.com/Slicer/Slicer/pull/8076" class="inline-onebox">BUG: Check for null pointer before fitting volume by pieper · Pull Request #8076 · Slicer/Slicer · GitHub</a></p>

---
