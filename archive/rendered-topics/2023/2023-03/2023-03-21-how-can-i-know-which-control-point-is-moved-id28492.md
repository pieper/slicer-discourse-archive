# How can I know which control point is moved?

**Topic ID**: 28492
**Date**: 2023-03-21
**URL**: https://discourse.slicer.org/t/how-can-i-know-which-control-point-is-moved/28492

---

## Post #1 by @nnzzll (2023-03-21 08:14 UTC)

<p>I am developing a C++ extension and my code goes like:</p>
<pre><code class="lang-auto">qvtkConnect(fidNode, vtkMRMLMarkupsFiducialNode::PointEndInteractionEvent, this, SLOT(onPointMoved()));
</code></pre>
<p>Since I have to do some operation according to control point’s position, how can I know which control point of <code>fidNode</code> is moved in slot function <code>onPointMoved()</code>?</p>

---

## Post #2 by @cpinter (2023-03-21 11:12 UTC)

<p>This works during the interaction, not sure what happens right after<br>
<code>markupIndex = int(caller.GetAttribute('Markups.MovingMarkupIndex'))</code></p>

---
