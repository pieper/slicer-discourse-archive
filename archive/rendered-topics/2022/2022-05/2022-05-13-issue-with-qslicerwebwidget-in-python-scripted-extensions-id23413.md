---
topic_id: 23413
title: "Issue With Qslicerwebwidget In Python Scripted Extensions"
date: 2022-05-13
url: https://discourse.slicer.org/t/23413
---

# Issue with qSlicerWebWidget in python scripted extensions

**Topic ID**: 23413
**Date**: 2022-05-13
**URL**: https://discourse.slicer.org/t/issue-with-qslicerwebwidget-in-python-scripted-extensions/23413

---

## Post #1 by @im_catta (2022-05-13 16:40 UTC)

<p>If want to generate a pdf file using the <em>qSlicerWebWidget</em> I can simply type in the Python Interactor something like</p>
<pre><code class="lang-auto">w = slicer.qSlicerWebWidget()
w.webView().url = qt.QUrl("https://www.slicer.org/")
w.printToPdf(r"C:\foo\page.pdf")
</code></pre>
<p>but if I run the same code from a <em>ScriptedLoadableModuleWidget</em> it will not create the pdf. Moreover, no error message or exception is presented.</p>
<p>A similar behaviour applies if I want to <em>.show()</em> a <em>qSlicerWebWidget</em>. It’s working from the Python Interactor, but not from extensions.</p>
<p>What am I missing?</p>

---

## Post #2 by @pieper (2022-05-13 17:08 UTC)

<p>Try adding <code>slicer.app.processEvents()</code> after setting the url so the widget has a chance to render.</p>

---

## Post #3 by @im_catta (2022-05-17 11:50 UTC)

<p>I tried using <code>slicer.app.processEvents()</code>, but the same problem remains</p>

---

## Post #4 by @pieper (2022-05-17 13:00 UTC)

<p>You probably need more event processing.  The best is to write the code in an asynchronous style, where you wait to process the page when it finishes loading.  See the Signals section here:<br>
<a href="https://apidocs.slicer.org/master/classqSlicerWebWidget.html" class="onebox" target="_blank" rel="noopener">https://apidocs.slicer.org/master/classqSlicerWebWidget.html</a></p>

---

## Post #5 by @jcfr (2022-05-17 13:48 UTC)

<p>An example of use along with relevant signal connection is available at <a href="https://discourse.slicer.org/t/does-webwidgets-printtopdf-work-on-mac/19544" class="inline-onebox">Does WebWidget's printToPdf work on Mac?</a></p>
<p>It may be helpful to move forward.</p>

---
