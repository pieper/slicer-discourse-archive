# Accessing the Module Window

**Topic ID**: 2241
**Date**: 2018-03-05
**URL**: https://discourse.slicer.org/t/accessing-the-module-window/2241

---

## Post #1 by @asheu (2018-03-05 17:38 UTC)

<p>Hi there,</p>
<p>I was wondering if there was any way to access the currently running module and its corresponding widgets through code. By this, I mean for example if I were running the Segmentation module, is it possible for me to access the module that is on the display menu, and then isolate the SliceFill widget that is present in the module?</p>
<p>Thank you very much for the help.</p>

---

## Post #2 by @lassoan (2018-03-05 18:42 UTC)

<p>Yes, you can access any module from any other module.</p>
<p>A module must not use another module’s GUI (the GUI is only for user interactions), but instead a module should create/modify MRML nodes and call module logic functions.</p>
<p>Specifically about Segment Editor - you can find here are examples for running Segment Editor effects from a Python script:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #3 by @asheu (2018-03-05 18:47 UTC)

<p>I used the segmentation editor as an example but am more specifically looking to pull the widgets out of the Reformat module. I’m having a bit of trouble locating the module (i.e, I am able to call the widgets present on the mainWindow() but could not find access to the module window) and as such, cannot find the widgets that the Reformat module has built in.</p>

---

## Post #4 by @lassoan (2018-03-05 19:03 UTC)

<p>You cannot reuse the module’s main GUI widgets, but usually a module widget consists of reusable widgets. How to find a widget:</p>
<ul>
<li>Go to Slicer’s github page: <a href="https://github.com/Slicer/Slicer">https://github.com/Slicer/Slicer</a>
</li>
<li>Search for any text that appears in the widget, for example, for reformat widget you can search for <code>Normal to Camera</code> - <a href="https://github.com/Slicer/Slicer/search?l=XML&amp;q=normal+to+camera&amp;type=&amp;utf8=%E2%9C%93">https://github.com/Slicer/Slicer/search?l=XML&amp;q=normal+to+camera&amp;type=&amp;utf8=✓</a>
</li>
</ul>
<p>In Reslice module’s case, search result shows that the button is in a module widget (qSlicerReformatModuleWidget.ui), so the widget is not reusable. If you are familiar with C++ then you can refactor the code to move the part you need to a separate reusable widget and use that widget in your module. However, it may be simpler to just have a look at the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Reformat/qSlicerReformatModuleWidget.cxx">module widget’s code</a> and reimplement in your code whatever you need.</p>
<p>Reslicing a volume using sliders is really simple to implement. See for example how it is done in ValveView module in SlicerHeart extension: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveView/ValveView.py">https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveView/ValveView.py</a></p>

---

## Post #5 by @jcfr (2018-03-05 23:07 UTC)

<blockquote>
<p>You cannot reuse the module’s main GUI widgets, but usually a module widget consists of reusable widgets.</p>
</blockquote>
<p>To complete the answer of <a class="mention" href="/u/lassoan">@lassoan</a>, we introduced a method named <a href="http://apidocs.slicer.org/master/classqSlicerAbstractCoreModule.html#a4e33c1cc55d85bbf8739763f347bf906">createNewWidgetRepresentation</a> to support creating new module representation.</p>
<p>In your case, the following would work:</p>
<pre><code class="lang-auto">reformatModuleWidget = slicer.modules.reformat.createNewWidgetRepresentation()
reformatModuleWidget.setMRMLScene(slicer.app.mrmlScene())
reformatModuleWidget.show()
</code></pre>
<p>That said, your module and workflow would be dependent on the layout of that specific module.</p>

---

## Post #6 by @asheu (2018-03-06 02:13 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> in the scenario that you have stated above, does this not take the entire reformat module and simply create a widget elsewhere? in which case the individually packaged components would still not be retrievable, is that correct?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> thank you for the response! i will certainly take a look into the code and try to develop the widget after i figure out all the individual components of it</p>

---

## Post #7 by @jcfr (2018-03-06 02:43 UTC)

<aside class="quote no-group" data-username="asheu" data-post="6" data-topic="2241">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/db5fbb/48.png" class="avatar"> asheu:</div>
<blockquote>
<p>in the scenario that you have stated above, does this not take the entire reformat module and simply create a widget elsewhere? in which case the individually packaged components would still not be retrievable, is that correct?</p>
</blockquote>
</aside>
<p>This is correct, you would get the following:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57f62f05a381ce118df09e1f0f99b25c0df97053.png" alt="reformat-ui-standalone" data-base62-sha1="cy8Z8iFpnznXXekGQhIu2Xk8jET" width="540" height="417"></p>
<p>Then, if you only want to hide part of it, you could do something like this:</p>
<pre><code class="lang-auto">slicer.util.findChild(reformatModuleWidget, "OriginCoordinatesGroupBox").hide()
</code></pre>
<p>and you would get:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1e0e89fc47a095322929944cb372521d4c122de.png" alt="reformat-ui-standalone-tweaked" data-base62-sha1="tWFEFwSYHLmvIeFolAvwyd4w9rg" width="536" height="336"></p>
<p>Name of the object to access is found in the associated UI file: <a href="https://github.com/Slicer/Slicer/blob/0ab294089b4827fea3272417a23c321d57e391b4/Modules/Loadable/Reformat/Resources/UI/qSlicerReformatModuleWidget.ui">qSlicerReformatModuleWidget.ui</a></p>
<p>This approach is suitable for fast prototyping and experimenting with UI. After, an approach is validated, I suggest to refactor the module so that you could reuse its components.</p>

---

## Post #8 by @asheu (2018-03-06 03:12 UTC)

<p>thank you so much, this has been extremely helpful</p>

---
