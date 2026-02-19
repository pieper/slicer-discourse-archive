---
topic_id: 23945
title: "Place Markups Through Visible Model"
date: 2022-06-19
url: https://discourse.slicer.org/t/23945
---

# Place markups through visible model

**Topic ID**: 23945
**Date**: 2022-06-19
**URL**: https://discourse.slicer.org/t/place-markups-through-visible-model/23945

---

## Post #1 by @JuanPinera (2022-06-19 13:35 UTC)

<p>Hi, I want to put a fiducial on an object that has another object placed in front of it in semi-transparency. The problem I have is that it detects the surface and places it in the second object.<br>
I have searched here: <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLModelDisplayNode.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: vtkMRMLModelDisplayNode Class Reference</a><br>
but I can’t find the property that disables the interaction in 3d.<br>
Cloud you help me.<br>
Thanks</p>

---

## Post #2 by @lassoan (2022-06-21 05:52 UTC)

<p>This should be no problem at all. You can make a model non-pickable by disabling <code>Selectable</code> property. You can change this property via the Python console:</p>
<pre><code class="lang-auto">getNode('SomeModel').SelectableOff()
</code></pre>
<p>If you don’t want to type a command into the console then you can install <code>SlicerVirtualReality</code> extension. After you install it, you can right-click on a model in the Data module and check/uncheck the <code>Toggle selectable</code> option.</p>

---
