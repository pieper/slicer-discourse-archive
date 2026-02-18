# Delayed callback when SegmentationNode is added to the scene

**Topic ID**: 14674
**Date**: 2020-11-18
**URL**: https://discourse.slicer.org/t/delayed-callback-when-segmentationnode-is-added-to-the-scene/14674

---

## Post #1 by @joachim (2020-11-18 15:39 UTC)

<p>I’ve created a listener when <em>SegmentationNodes</em> are added to my scene, something like this:</p>
<pre><code class="lang-auto">@vtk.calldata_type(vtk.VTK_OBJECT)
def onNodeAdded(caller, event, node):
    if node.IsA( "vtkMRMLSegmentationNode" ):
        # call `myFunction()` in current thread
        myFunction( node )

slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, onNodeAdded)
</code></pre>
<p>Actually, I’m performing some editor effects automatically whenever I add a <em>SegmentationNode</em>.</p>
<p>If I don’t use the callback (i.e. <code>slicer.mrmlScene.AddObserver()</code> not called) and do the steps manually: call <code>myFunction()</code> in the interpreter after the node was added, things works as expected. However, if I add the callback as an observer (above code block), something wrong happens so <code>myFunction()</code> fails. I guess this is because the <em>SegmentationNode</em> has to be fully added in order for <code>myFunction()</code> to work.</p>
<p>How can I call <code>myFunction()</code> after the <em>SegmentationNode</em> and its dependencies was completely added? A timed callback to <code>myFunction()</code> can be a solution (practically but not completely safe in theory).</p>

---

## Post #2 by @lassoan (2020-11-18 22:09 UTC)

<p>Yes, probably you want to wait for the segmentation node to get a default display node, etc. You can add a delayed callback (which is called when the application becomes idle) like this:</p>
<pre><code>qt.QTimer.singleShot(0, myCallback)</code></pre>

---
