---
topic_id: 24375
title: "Customized Tabbed View"
date: 2022-07-18
url: https://discourse.slicer.org/t/24375
---

# Customized tabbed view

**Topic ID**: 24375
**Date**: 2022-07-18
**URL**: https://discourse.slicer.org/t/customized-tabbed-view/24375

---

## Post #1 by @michabermoy (2022-07-18 17:17 UTC)

<p>Is there a way to create a customized tabbed view so that one tab has multiple windows? For example, one tab of the customized tabbed view will have a table window and the four default view windows (3D, Axial, Sagittal, Coronal). Other tabs may or may not have multiple windows. I’ve tried messing with the XML code for the Tabbed 3D and Tabbed Slice view, but have not figured out how to do this yet.</p>

---

## Post #2 by @jcfr (2022-07-18 21:21 UTC)

<p>This example allows to have two tabs, each with multiple viewer.</p>
<p>That said, this use case hasn’t been tested as we usually compose viewer within a single pane or across tabs.</p>
<p>While we could further test and improve (e.g to ensure a name is associated with the tab), could you further describe your use case ?</p>
<p>Ready this entry of the developer guide may also be helpful: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#layout">MRML Overview / Advanced Topic / Layout</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>  may have additional feedback.</p>
<pre><code class="lang-python">customLayout = """
&lt;layout type="tab"&gt;
 &lt;item name="tab1" splitSize="300"&gt;
  &lt;layout type="vertical"&gt;
   &lt;item&gt;
    &lt;view class="vtkMRMLSliceNode" singletontag="Red"&gt;
     &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
     &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
     &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
    &lt;/view&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;view class="vtkMRMLSliceNode" singletontag="Green"&gt;
     &lt;property name="orientation" action="default"&gt;Coronal&lt;/property&gt;
     &lt;property name="viewlabel" action="default"&gt;G&lt;/property&gt;
     &lt;property name="viewcolor" action="default"&gt;#6EB04B&lt;/property&gt;
    &lt;/view&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;view class="vtkMRMLSliceNode" singletontag="Yellow"&gt;
     &lt;property name="orientation" action="default"&gt;Sagittal&lt;/property&gt;
     &lt;property name="viewlabel" action="default"&gt;Y&lt;/property&gt;
     &lt;property name="viewcolor" action="default"&gt;#EDD54C&lt;/property&gt;
    &lt;/view&gt;
   &lt;/item&gt;
  &lt;/layout&gt;
 &lt;/item&gt;
 
 &lt;item name="tab2"&gt;
  &lt;layout type="horizontal"&gt;
   &lt;item&gt;
    &lt;view class="vtkMRMLViewNode" singletontag="2" type="secondary"&gt;
     &lt;property name="viewlabel" action="default"&gt;2&lt;/property&gt;
    &lt;/view&gt;
   &lt;/item&gt;
   &lt;item&gt;
    &lt;view class="vtkMRMLViewNode" singletontag="3" type="endoscopy"&gt;
     &lt;property name="viewlabel" action="default"&gt;3&lt;/property&gt;
    &lt;/view&gt;
   &lt;/item&gt;
  &lt;/layout&gt;
&lt;/item&gt;
 
&lt;/layout&gt;
"""

# Built-in layout IDs are all below 100, so you can choose any large random number
# for your custom layout ID.
customLayoutId=501

layoutManager = slicer.app.layoutManager()
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)

# Switch to the new custom layout
layoutManager.setLayout(customLayoutId)
</code></pre>

---

## Post #3 by @lassoan (2022-07-18 22:48 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="24375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>While we could further test and improve (e.g to ensure a name is associated with the tab)</p>
</blockquote>
</aside>
<p>I’ve edited your example above and added names for the tabs (<code>tab1</code> and <code>tab2</code>).</p>

---

## Post #4 by @michabermoy (2022-07-19 12:33 UTC)

<p>This is exactly what I needed to get the display I had in mind started! When writing the xml code, I was running into a problem with the <code>&lt;item&gt;</code> tag underneath <code>&lt;layout type="tab"&gt;</code> and I would only get a blank screen when attempting to display the multiple windows in one tab. I think your code solves my issue with the display!</p>
<p>As for my use case, the goal is to have a custom display that works as follows:</p>
<ul>
<li>The first tab displays all segments (3D, Axial, Coronal, Sagittal) and their volumes in a table.</li>
<li>Following the first tab, there will be one tab per segment. Each will have the 3D, Axial, Coronal, and Sagittal windows.</li>
</ul>
<p>For example, if there are 5 segments, there will be a total of 6 tabs. The first tab shows all segments, the remainder 5 tabs each display a different segment.<br>
Thank you!</p>

---
