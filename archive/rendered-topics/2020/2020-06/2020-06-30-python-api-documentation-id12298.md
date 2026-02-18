# Python API documentation?

**Topic ID**: 12298
**Date**: 2020-06-30
**URL**: https://discourse.slicer.org/t/python-api-documentation/12298

---

## Post #1 by @joachim (2020-06-30 13:24 UTC)

<p>Is there an API documentation for the Python interface of Slicer? I haven’t found it.</p>
<p>What I’ve found is the <a href="http://apidocs.slicer.org/master/index.html" rel="nofollow noopener">C++ documentation</a>, and I use this when I try to do Python. I guess the Python interface is generated from C++ in some way. I don’t need well-commented documentation, but I’m looking for all types and functions in Slicer’s Python interface, instead of using  <code>Tab</code> in the Python Interactor. <a href="https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLabel.html" rel="nofollow noopener">The documentation for Qt’s Python API</a> is a nice example of how Python documentation can be done.</p>

---

## Post #2 by @pieper (2020-06-30 15:04 UTC)

<p>Good point - we discussed this <a href="https://discourse.slicer.org/t/2020-06-30-hangout/12286">at the developer hangout</a> and there isn’t a great universal solution given how many libraries slicer builds on an integrates.  <a href="https://www.na-mic.org/wiki/AHM2012-Slicer-Python">Here’s a very old page</a> that lists and links back to the various pieces.</p>
<p>We also noticed that while Qt’s Python documentation is good, it’s not perfect either.  For example this <a href="https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLabel.html#PySide2.QtWidgets.PySide2.QtWidgets.QLabel.linkActivated">python documentation</a> just lists the method type, while the <a href="https://doc.qt.io/qt-5/qlabel.html#linkActivated">corresponding C++ documentation includes useful text</a>.</p>
<p>It would be great if someone wants to build a better doc infrastructure, but for now I suggest looking at the source code.  And of course you can use <code>help</code> in the python interactor.</p>
<p>Hope that helps</p>

---

## Post #3 by @joachim (2020-06-30 15:42 UTC)

<p>At this point I would be very satisfied by just listing the method and types like in the Qt’s  Python API documentation. It’s so much easier to program when you can browse the API. I didn’t know about <code>help()</code> - thank you, I’m still learning Python.</p>
<h4>A short question</h4>
<p>I want to set “Modify other segments” to “Allow overlap” in my <em>.slicerrc</em> file:</p>
<pre><code class="lang-auto">ne = getNode( 'SegmentEditor' ) # singleton, type: vtkSlicerSegmentationsModuleMRMLPython.vtkMRMLSegmentEditorNode, according to Python Interactor
ne.SetOverwriteMode( 2 ) # magic number, see https://github.com/Slicer/Slicer/blob/e33439f950cca5a63976d249851eac6f52bc2530/Modules/Loadable/Segmentations/MRML/vtkMRMLSegmentEditorNode.h#L77-L87
</code></pre>
<p>How do I replace the magic number with a Python equivalent to <a href="https://github.com/Slicer/Slicer/blob/e33439f950cca5a63976d249851eac6f52bc2530/Modules/Loadable/Segmentations/MRML/vtkMRMLSegmentEditorNode.h#L77-L87" rel="nofollow noopener">C++'s <code>vtkMRMLSegmentEditorNode::OverwriteNone</code></a>? It looks like I can use <code> ne.OverwriteNone</code>, but that is not a static value. And <code>vtkMRMLSegmentEditorNode.OverwriteNone</code> is not defined, Python Interactor says.</p>

---

## Post #4 by @cpinter (2020-06-30 16:15 UTC)

<aside class="quote no-group" data-username="joachim" data-post="3" data-topic="12298">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>And <code>vtkMRMLSegmentEditorNode.OverwriteNone</code> is not defined, Python Interactor says.</p>
</blockquote>
</aside>
<p><code>slicer.vtkMRMLSegmentEditorNode.OverwriteNone</code> will work</p>

---
