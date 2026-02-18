# Set minimum view width/height in a layout

**Topic ID**: 16467
**Date**: 2021-03-10
**URL**: https://discourse.slicer.org/t/set-minimum-view-width-height-in-a-layout/16467

---

## Post #1 by @riep (2021-03-10 11:50 UTC)

<p>Hi everyone,<br>
I am trying to implement a custom layout very similar to SlicerLayoutFourUpQuantitativeView.<br>
However, I would like to set a minimum width/height to views so that when the user stretches one views others do not disappear.<br>
Is there already something existing to do that ?</p>
<p>Thanks in advance,<br>
Cheers</p>
<p>Pierre</p>

---

## Post #2 by @riep (2021-03-10 15:22 UTC)

<p>Probably not possible as of now</p><aside class="quote quote-modified" data-post="1" data-topic="2406">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slice-widget-size-in-custom-layouts/2406">Slice widget size in custom layouts</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    [custom-layout]I’m trying to change slice view sizes as part of the setup of a custom layout. For instance: 
def formatCustomLayout(self):
    customLayout = ( XML code )
    layoutNode = slicer.app.layoutManager().layoutLogic().GetLayoutNode()
    customLayoutId = 500
    layoutNode.AddLayoutDescription(customLayoutId, customLayout)
    slicer.app.layoutManager().setLayout(customLayoutId)

    slicer.app.layoutManager().sliceWidget('Long2').mrmlSliceNode().SetDimensions(100, 100, 1)
#end format…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2021-03-10 15:46 UTC)

<p>The proper solution would be to add attributes for this in CTK (in <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkLayoutManager.cpp#L431">ctkLayoutManager</a>). But if you have never used C++ then you can work around this in Python by looking up the widget using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.findChildren"><code>slicer.util.findChildren</code></a> and adjusting sizing properties.</p>

---

## Post #4 by @riep (2021-03-10 16:40 UTC)

<p>Thanks Andras,<br>
Do you know if there is a way to fix the size at layout creation<br>
I tried to use   verticalStretch="0" horizontalStretch="0" but it was not working</p>
<blockquote>
<p>&lt;item splitSize="300"&gt;"<br>
"      &lt;view class="vtkMRMLViewNode" singletontag="1" verticalStretch="0" horizontalStretch="0"&gt;"<br>
"       &lt;property name="viewlabel" action="default"&gt;1"</p>
</blockquote>

---

## Post #5 by @lassoan (2021-03-11 04:09 UTC)

<p>There are no such properties implemented in <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkLayoutManager.cpp">ctkLayoutManager</a> as <code>verticalStretch</code> and <code>horizontalStretch</code>. You can search for <code>.attribute</code> in the file to see what properties are available. You can modify this file to add support for more attributes.</p>

---

## Post #6 by @riep (2021-03-11 08:43 UTC)

<p>This is probably a small issue but in <a href="https://github.com/Slicer/Slicer/blob/81ff76b24d4913dbd992b7eed4d77805f306ffe8/Libs/MRML/Logic/vtkMRMLLayoutLogic.cxx#L54" class="inline-onebox" rel="noopener nofollow ugc">Slicer/vtkMRMLLayoutLogic.cxx at 81ff76b24d4913dbd992b7eed4d77805f306ffe8 · Slicer/Slicer · GitHub</a>, verticalStretch is defined</p>

---
