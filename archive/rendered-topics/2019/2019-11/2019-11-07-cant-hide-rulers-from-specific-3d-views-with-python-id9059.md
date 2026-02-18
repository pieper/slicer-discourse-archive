# Can't hide rulers from specific 3d Views (with python)

**Topic ID**: 9059
**Date**: 2019-11-07
**URL**: https://discourse.slicer.org/t/cant-hide-rulers-from-specific-3d-views-with-python/9059

---

## Post #1 by @Brian_N (2019-11-07 13:59 UTC)

<p>I’m having trouble displaying an Annotation Ruler in only certain 3D views.</p>
<p>For example, when using the Dual 3D Layout, I quickly create both a Fiducial and Ruler.  If I input the following up the python interactor, the Fiducial disappears from the second 3D view (as expected):</p>
<p><code>getNode('vtkMRMLMarkupsFiducialNode1').GetDisplayNode().AddViewNodeID('vtkMRMLViewNode1')</code></p>
<p>However, if I input the following for the AnnotationRulerNode, the ruler does not disappear from the second 3D View:</p>
<p><code>getNode('vtkMRMLAnnotationRulerNode1').GetDisplayNode().AddViewNodeID('vtkMRMLViewNode1')</code></p>
<p>The ruler node actually has 3 display nodes, so I tried it on all 3, but it still did not work:</p>
<p><code>getNode('vtkMRMLAnnotationRulerNode1').GetNthDisplayNode(0).AddViewNodeID('vtkMRMLViewNode1')</code><br>
<code>getNode('vtkMRMLAnnotationRulerNode1').GetNthDisplayNode(1).AddViewNodeID('vtkMRMLViewNode1')</code><br>
<code>getNode('vtkMRMLAnnotationRulerNode1').GetNthDisplayNode(2).AddViewNodeID('vtkMRMLViewNode1')</code></p>
<p>And finally, the ruler automatically appears under a hierarchy, so I also tried the following, but again without success:</p>
<p><code>getNode('vtkMRMLAnnotationHierarchyNode2').GetDisplayNode().AddViewNodeID('vtkMRMLViewNode1')</code><br>
<code>getNode('vtkMRMLAnnotationHierarchyNode1').GetDisplayNode().AddViewNodeID('vtkMRMLViewNode1')</code></p>
<p>I also removed the ruler from the hierarchy, and tried all of the above, but it did not work. Is there something I am missing, or is this a bug in Slicer?</p>
<p>Thanks,<br>
Brian</p>

---

## Post #2 by @lassoan (2019-11-07 14:01 UTC)

<p>You may try calling <code>RemoveAllViewNodeIDs</code> before adding node IDs.</p>
<p>Annotation rulers are being phased out. In recent Slicer Preview Releases you can use Markups lines instead.</p>

---

## Post #3 by @aiden.zhu (2019-11-07 14:45 UTC)

<p>Hi Brian,</p>
<p>I encountered the same case not long before. I did a silly way to go through all rulers and check their names to let decide show or hide:</p>
<pre><code>  value = 0 # hide
  value = 1 # show
  for i in range(NumofRulers):
        nodeName = 'Line-Ruler_No'+str(i+1)  # ruler Node's name
        node = slicer.util.getNode(nodeName)
        if node:
             node.SetDisplayVisibility(value)
</code></pre>
<p>Hope it helps.</p>

---

## Post #4 by @Brian_N (2019-11-11 13:21 UTC)

<p>Thanks.  I ended up using Markup Lines, and everything works as expected</p>

---
