---
topic_id: 24350
title: "Change Color Box Within 3D View"
date: 2022-07-17
url: https://discourse.slicer.org/t/24350
---

# Change color box within 3D view

**Topic ID**: 24350
**Date**: 2022-07-17
**URL**: https://discourse.slicer.org/t/change-color-box-within-3d-view/24350

---

## Post #1 by @keri (2022-07-17 20:05 UTC)

<p>Hi,</p>
<p><a href="https://discourse.slicer.org/t/how-to-change-color-of-3d-cube-inside-3d-view/769/10">The issue already been asked</a> but still I’m  trying to struggle with this.</p>
<p>The idea is to modify the color of the cube from 3D view when the view is created within SlicerCAT.<br>
To solve this I need to understand how to get this cube as VTK or MRML object. Who is responsible for creating it?</p>
<p>For example I can see that <a href="https://github.com/Slicer/Slicer/blob/115e32bdf8e478208fc2c75179cf2ecdb555d984/Libs/MRML/Core/vtkMRMLViewNode.h#L318" rel="noopener nofollow ugc">vtkMRMLViewNode</a> has <code>BoxVisible</code> attribute. To modify visibility one simply triggers this attribute:</p>
<pre><code class="lang-python">viewNode = slicer.app.layoutManager().threeDWidget(0).mrmlViewNode()
viewNode.SetBoxVisible(1)
</code></pre>
<p>Can’t understand how it works… Who is observer or who manages it from VTK side?</p>

---

## Post #2 by @lassoan (2022-07-18 07:58 UTC)

<p>All view content is displayed using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html?highlight=displayable%20manager#the-displayable-manager">displayable managers</a>.</p>
<p>The purple box is displayed by vtkMRMLViewDisplayableManager. The color is hardcoded, so you need to add an API to change it. Probably the cleanest solution would be to add a <code>BoxColor</code> property to <code>vtkMRMLViewNode</code>.</p>

---

## Post #3 by @keri (2022-07-18 12:54 UTC)

<p>Thank you,</p>
<p>Completely forgot that such things are controlled by displayable managers.</p>
<p><a href="https://github.com/Slicer/Slicer/pull/6467" rel="noopener nofollow ugc">The PR is ready</a></p>

---
