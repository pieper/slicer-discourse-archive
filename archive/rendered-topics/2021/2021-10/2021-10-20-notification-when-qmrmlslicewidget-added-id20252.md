---
topic_id: 20252
title: "Notification When Qmrmlslicewidget Added"
date: 2021-10-20
url: https://discourse.slicer.org/t/20252
---

# Notification when `qMRMLSliceWidget` added

**Topic ID**: 20252
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/notification-when-qmrmlslicewidget-added/20252

---

## Post #1 by @keri (2021-10-20 00:06 UTC)

<p>Hi,</p>
<p>Is there some kind of signal when <code>qMRMLSliceWidget</code> added?</p>
<p>I’m trying to add a toolbutton to it and there is no preblem to do that on existing <code>qMRMLSliceWidget</code> (there is an example in scrit repo) but when new slice widget is added I need to add the same button to it.</p>

---

## Post #2 by @lassoan (2021-10-20 04:53 UTC)

<p>You can observe the <a href="https://apidocs.slicer.org/master/classqMRMLLayoutManager.html#ac5c1ebc99fe71f02ea72894df6cf56d8">layout changed signal of the layout manager</a>.</p>

---

## Post #3 by @keri (2021-10-20 13:00 UTC)

<p>Thank you for help,</p>
<p>I also found <a href="https://apidocs.slicer.org/master/classqMRMLLayoutViewFactory.html#af27583d80ef3b4ea0cd6978e092aefc0" rel="noopener nofollow ugc">qMRMLLayoutViewFactory::viewCreated(QWidget*)</a> (though as I understood it always <code>emit nullptr</code>).</p>
<p>And I reach the factory with:</p>
<pre><code class="lang-cpp">  qMRMLLayoutViewFactory* factory = app-&gt;
      layoutManager()-&gt;mrmlViewFactory("vtkMRMLSliceNode");
</code></pre>
<p>What is the preferred solution: connect to layout manager or to factory?</p>

---

## Post #4 by @lassoan (2021-10-20 14:29 UTC)

<p>Adding a connection to the <code>viewCreated</code> signal to every view types you are interested in should work, too. That signal emits a valid pointer to the widget that has just been created.</p>

---

## Post #5 by @keri (2021-10-20 15:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20252">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>That signal emits a valid pointer to the widget that has just been created.</p>
</blockquote>
</aside>
<p>I may be mistaken but in the Slicer’s source code <a href="https://github.com/Slicer/Slicer/blob/11d0ca30162e9fd0315997dd41908354376b52a4/Libs/MRML/Widgets/qMRMLLayoutViewFactory.cxx#L419" rel="noopener nofollow ugc">view factory viewCreated(viewWidget)</a> signal is emitting with widget that is created with <a href="https://github.com/Slicer/Slicer/blob/11d0ca30162e9fd0315997dd41908354376b52a4/Libs/MRML/Widgets/qMRMLLayoutViewFactory.cxx#L454-L458" rel="noopener nofollow ugc"><code>createViewFromNode(vtkMRMLAbstractViewNode* viewNode)</code> function that always returns nullptr</a></p>
<p>Is implementation of <code>QWidget* qMRMLLayoutViewFactory::createViewFromNode(vtkMRMLAbstractViewNode* viewNode)</code> is correct?</p>
<p>P.S. I’m able to catch the <code>viewCreated</code> signal but it is sent with <code>nullptr</code> parameter:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09052e34e60c5099108a7eadc3e336fd0b27b216.jpeg" data-download-href="/uploads/short-url/1hNozJtroGOwDoFYps7Jl8BGJro.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09052e34e60c5099108a7eadc3e336fd0b27b216_2_690x95.jpeg" alt="image" data-base62-sha1="1hNozJtroGOwDoFYps7Jl8BGJro" width="690" height="95" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09052e34e60c5099108a7eadc3e336fd0b27b216_2_690x95.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09052e34e60c5099108a7eadc3e336fd0b27b216.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09052e34e60c5099108a7eadc3e336fd0b27b216.jpeg 2x" data-dominant-color="E9E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">908×126 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2021-10-20 15:33 UTC)

<p><code>createViewFromNode</code> method is overridden in concrete factory classes (see qMRMLLayoutManager.cxx). You can add a breakpoint at <code>emit viewCreated(viewWidget);</code> and see that <code>viewWidget</code> is not a nullptr.</p>
<p>Most likely something is wrong where you set up the connection between the signal and your slot.</p>

---

## Post #7 by @keri (2021-10-20 16:04 UTC)

<p>I see now, thank you for explanation</p>

---
