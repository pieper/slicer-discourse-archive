# Insert sequence Browser Toolbar in a python module

**Topic ID**: 14335
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/insert-sequence-browser-toolbar-in-a-python-module/14335

---

## Post #1 by @marianaslicer (2020-10-30 16:24 UTC)

<p>Hello!</p>
<p>I am trying to develop a python scripted module using Sequences extension. I already successfully create a sequence (although it appears as a vtkMRMLScalarVolumeNode) and I can display the sequence by using the Sequence Browser Toolbar of 3D slicer 4.11.</p>
<p>I want to insert the sequence browser toolbar in my own module but it does not activate when the sequence is created.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/695f55a3ff4544666fa21ce8531ddf59a681e5b8.jpeg" data-download-href="/uploads/short-url/f2ao2idcuCUtWE6c8HSu0MDQgnm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/695f55a3ff4544666fa21ce8531ddf59a681e5b8_2_690x339.jpeg" alt="image" data-base62-sha1="f2ao2idcuCUtWE6c8HSu0MDQgnm" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/695f55a3ff4544666fa21ce8531ddf59a681e5b8_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/695f55a3ff4544666fa21ce8531ddf59a681e5b8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/695f55a3ff4544666fa21ce8531ddf59a681e5b8.jpeg 2x" data-dominant-color="BCBCBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">944×465 78.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Can you explained me what is missing or what is wrong in my code please? Thank you!</p>
<pre><code class="lang-auto">self.sequenceBrowserToolbarButton = slicer.qMRMLSequenceBrowserToolBar()
fourDCTFormLayout.addRow(self.sequenceBrowserToolbarButton)

self.sequenceBrowserToolbarButton.connect('activeBrowserNodeChanged(vtkMRMLNode*)', self.oncreateSequenceButton)

def oncreateSequenceButton(self):
    exitString = logic.createSequence(patient.fourDCT)

    if exitString:
      self.qtMessage(exitString)
      return
</code></pre>

---

## Post #2 by @jamesobutler (2020-10-30 16:42 UTC)

<p>MRML widgets such as qMRMLSequenceBrowserToolBar in this case require that the MRML scene be set.</p>
<pre><code class="lang-python">
self.sequenceBrowserToolbarButton.setMRMLScene(slicer.mrmlScene)
</code></pre>

---

## Post #3 by @marianaslicer (2020-10-30 16:57 UTC)

<p>Thank you it worked! Another question: Is it possible to change the width of the widget?</p>

---

## Post #4 by @jamesobutler (2020-10-30 17:19 UTC)

<p>There are various methods for manipulating a QWidget’s size which you can review at <a href="https://doc.qt.io/qt-5/qwidget.html" rel="noopener nofollow ugc">https://doc.qt.io/qt-5/qwidget.html</a></p>

---
