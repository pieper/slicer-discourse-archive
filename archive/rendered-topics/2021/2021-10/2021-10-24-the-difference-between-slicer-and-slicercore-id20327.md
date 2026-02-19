---
topic_id: 20327
title: "The Difference Between Slicer And Slicercore"
date: 2021-10-24
url: https://discourse.slicer.org/t/20327
---

# The difference between Slicer and SlicerCore?

**Topic ID**: 20327
**Date**: 2021-10-24
**URL**: https://discourse.slicer.org/t/the-difference-between-slicer-and-slicercore/20327

---

## Post #1 by @joachim (2021-10-24 23:49 UTC)

<p>The application is divided into two parts: <em>Slicer</em> and <em>SlicerCore</em>; <code>qSlicerApplication</code> is a subclass of <code>qSlicerCoreApplication</code>, and <code>qSlicerAbstractModule</code> is a subclass of <code>qSlicerAbstractCoreModule</code>.</p>
<p>What is the intention behind this division? Could it be that <em>Slicer</em> is the GUI version of <em>SlicerCore</em>? This seems strange since <code>qSlicerCoreApplication</code> is a subclass of <code>QGuiApplication</code>. And <code>qSlicerAbstractCoreModule</code> - the foundation for Slicer modules - has actually a method <code>::widgetRepresentation()</code>.</p>
<p>And, if <em>Slicer</em> is built on top of <em>SlicerCore</em>, why is <code>qSlicerCoreModule</code> a subclass of <code>qSlicerAbstractModule</code>? Maybe the naming is wrong and misleading?</p>
<p>All these abstractions by subclassing makes me dizzy.</p>

---

## Post #2 by @pieper (2021-10-25 15:01 UTC)

<p>Yes, there’s a lot of code to parse.  In general we try to follow the design and coding conventions of the parent classes, so <code>QSlicerX</code> typically inherits from <code>QX</code> and <code>vtkSlicerX</code> from <code>vtkObject</code> ultimately.</p>
<p>Regarding Core and non-Core see:</p>
<p><a href="https://doc.qt.io/qt-5/qcoreapplication.html" class="onebox" target="_blank" rel="noopener">https://doc.qt.io/qt-5/qcoreapplication.html</a></p>

---

## Post #3 by @joachim (2021-10-25 23:42 UTC)

<p>Thanks.</p>
<p>OK, so the division of Slicer into <em>Slicer</em> and <em>SlicerCore</em> is actually an attempt to split Slicer like a Qt GUI and a Qt Core application? So <em>SlicerCore</em> is the “non-GUI version” of Slicer? This seems a bit strange since <code>qSlicerCoreApplication</code> is a subclass of <code>QApplication</code> - Qt with GUI, but I guess it is difficult to do it different.</p>
<p><code>qSlicerAbstractCoreModule</code> - the parent of all modules in Slicer and part of <em>SlicerCore</em> - has a method <code>::widgetRepresentation()</code> which returns a <code>qSlicerAbstractModuleRepresentation* </code>. I guess this type (inside <em>SlicerCore</em>) is meant to be an abstraction for something living outside <em>SlicerCore</em>, and ultimately inside <em>Slicer</em> (as a <code>qSlicerWidget : public QWidget</code>).</p>

---

## Post #4 by @lassoan (2021-10-26 02:54 UTC)

<aside class="quote no-group" data-username="joachim" data-post="3" data-topic="20327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>OK, so the division of Slicer into <em>Slicer</em> and <em>SlicerCore</em> is actually an attempt to split Slicer like a Qt GUI and a Qt Core application?</p>
</blockquote>
</aside>
<p>It is more than an attempt. GUI and non-GUI classes are strictly separated throughout the entire application. It is not two separate versions of the application, but a dependency tree. Non-GUI classes (such as in QTCore, module logics, MRML, displayable managers) don’t depend on any GUI classes (such as in QTGUI, module widgets) and can be used without GUI.</p>
<p>For example, you can create a scene, instantiate some MRML nodes and module logics and use Slicer module features without ever creating a GUI or using Qt at all. Most non-GUI tests work like this.</p>
<p>We don’t see much practical use of it other than having overall cleaner architecture. But in the future we may see significant benefit from this separation. For example, we plan to release non-GUI classes, such as MRML library, SegmentationCore, module logics (and maybe later GUI classes as well) as pip-installable Python packages that can be used without instantiating an application at all.</p>

---

## Post #5 by @joachim (2021-10-26 11:01 UTC)

<p>So the division into <em>Slicer</em> and <em>SlicerCore</em> is done in order to make it <em>possible</em> to use Slicer as non-GUI application. The “Core” in <em>SlicerCore</em> is meant to be <em>Qt Core</em> functionality.</p>
<p>The fact that the class <code>qSlicerCoreApplication</code> depends on Qt with GUI, and <code>qSlicerAbstractCoreModule</code> has a method <code>::widgetRepresentation()</code>, didn’t make this obvious, but I can see how it works now.</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
