# Adding Rulers to Python Code

**Topic ID**: 13802
**Date**: 2020-10-01
**URL**: https://discourse.slicer.org/t/adding-rulers-to-python-code/13802

---

## Post #1 by @kleingeo (2020-10-01 17:08 UTC)

<p>I am currently working on a plugin for people not familiar with Slicer to use, so I am trying to keep the plugin self-contained. I am trying to add functionality for the user to add rulers for it for later measurements. What is the best way to do this? The only thing I’ve had some success with so far is using <code>markerTable = slicer.qSlicerSimpleMarkupsWidget()</code> but it only supports fiducial markers rather than rulers.</p>

---

## Post #2 by @lassoan (2020-10-02 23:43 UTC)

<aside class="quote no-group" data-username="kleingeo" data-post="1" data-topic="13802">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kleingeo/48/6772_2.png" class="avatar"> kleingeo:</div>
<blockquote>
<p>I am currently working on a plugin for people not familiar with Slicer to use, so I am trying to keep the plugin self-contained.</p>
</blockquote>
</aside>
<p>Very good.</p>
<aside class="quote no-group" data-username="kleingeo" data-post="1" data-topic="13802">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kleingeo/48/6772_2.png" class="avatar"> kleingeo:</div>
<blockquote>
<p>The only thing I’ve had some success with so far is using <code>markerTable = slicer.qSlicerSimpleMarkupsWidget()</code> but it only supports fiducial markers rather than rulers.</p>
</blockquote>
</aside>
<p>By default, <code>qSlicerSimpleMarkupsWidget</code>’s node selector shows fiducial nodes, but you can <a href="http://apidocs.slicer.org/master/classqSlicerSimpleMarkupsWidget.html#a22ad5ec34cc62da601554176a8d4f3ba">get the node selector combobox</a> and <a href="http://apidocs.slicer.org/master/classqMRMLNodeComboBox.html#a167e0d372b20a5ec1cbea308c3b4b6ae">set node types</a> (class names) that you want to work with.</p>
<aside class="quote no-group" data-username="kleingeo" data-post="1" data-topic="13802">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kleingeo/48/6772_2.png" class="avatar"> kleingeo:</div>
<blockquote>
<p>I am trying to add functionality for the user to add rulers for it for later measurements. What is the best way to do this?</p>
</blockquote>
</aside>
<p>If you just want to place a line (not display point coordinates) then it is probably better to use simpler and more compact <a href="http://apidocs.slicer.org/master/classqSlicerMarkupsPlaceWidget.html">markups place widget</a>.</p>

---
