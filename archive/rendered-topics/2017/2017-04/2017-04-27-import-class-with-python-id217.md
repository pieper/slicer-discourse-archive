# Import Class with Python

**Topic ID**: 217
**Date**: 2017-04-27
**URL**: https://discourse.slicer.org/t/import-class-with-python/217

---

## Post #1 by @basti (2017-04-27 21:03 UTC)

<p>I have a very basic question:</p>
<p>When I find a class using the documentation, for example: <a href="http://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html" rel="nofollow noopener">http://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html</a></p>
<p>How can I know how import this class in my Python Module? For example to import the class behind the link I figured out I need write:</p>
<pre><code> import qSlicerSegmentationsModuleWidgetsPythonQt
 self.editor = qSlicerSegmentationsModuleWidgetsPythonQt.qMRMLSegmentEditorWidget()
</code></pre>
<p>Is there a way to get this information from the documentation for other classes?</p>

---

## Post #2 by @pieper (2017-04-27 21:18 UTC)

<p>These are pulled into the slicer module, so you can access it like this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.qMRMLSegmentEditorWidget()
</code></pre>
<p>From python you can get the API documentation (basically like doxygen) like this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; help(slicer.qMRMLSegmentEditorWidget)
</code></pre>
<p>is that what you were looking for?</p>

---

## Post #3 by @basti (2017-04-27 21:29 UTC)

<p>Thanks for the fast answer!</p>
<p>My problem is, for example, when I try to acces qSlicerSegmentationsModuleWidget by using:</p>
<pre><code>slicer.qSlicerSegmentationsModuleWidget()
</code></pre>
<p>It tells me</p>
<blockquote>
<p>‘module’ object has no attribute ‘qSlicerSegmentationsModuleWidget’</p>
</blockquote>

---

## Post #4 by @lassoan (2017-04-27 22:19 UTC)

<p>qSlicerSegmentationsModuleWidget is for exclusive use of the Segmentations module. It is built from reusable widgets that you can put in your own module widget. You can have a look at the widget’s source code and .ui file to see exactly which widgets are used and how.</p>

---
