# Memory Usage Increase in Looped Script

**Topic ID**: 3201
**Date**: 2018-06-15
**URL**: https://discourse.slicer.org/t/memory-usage-increase-in-looped-script/3201

---

## Post #1 by @Tom_Wei (2018-06-15 18:40 UTC)

<p>Hello,</p>
<p>I’ve written a script that uses slicer.util.loadVolume() to open a scan in each iteration of a loop, and despite using slicer.mrmlScene.RemoveNode() each time, the memory usage still goes up in task manager, suggesting that the vtk object is still in memory somewhere and not freed. Once the memory fills up all the way, slicer will crash, so I guess I can’t count on the Python GC to take care of it either.</p>
<p>I suspected an extraneous reference count might be responsible for this, but observed the exact same effect even after calling UnRegister() to manually decrement it. Is there a proper way to free the memory associated with loading a volume?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-06-15 18:57 UTC)

<p>It may be simpler to clear the scene, but if that’s not an option then delete not just the volume node but also the volume’s display node and storage node.</p>

---

## Post #3 by @ihnorton (2018-06-15 19:07 UTC)

<p>I was just running a quick test while Andras replied – the memory does stay stable if you delete those two nodes.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; def loadLoop():
...   slicer.util.loadVolume("/var/folders/7l/2qsp6sqx4_b5x9kf_yzzm4lc0000gn/T/Slicer/RemoteIO/MR-head.nrrd")
...   n = getNode("MR-head*")
...   slicer.mrmlScene.RemoveNode(n.GetStorageNode())
...   slicer.mrmlScene.RemoveNode(n.GetDisplayNode())
...   slicer.mrmlScene.RemoveNode(n)
... 
&gt;&gt;&gt; for i in xrange(0,100):
...   loadLoop()
</code></pre>
<p>If you want to find out what nodes are associated with a given data type, you can look at <code>slicer.mrmlScene.GetNodes()</code> before and after, with something like:</p>
<pre><code class="lang-auto">def getNodes():
  nodes = slicer.mrmlScene.GetNodes()
  return [nodes.GetItemAsObject(i).GetID() for i in xrange(0,nodes.GetNumberOfItems()]

nodes1 = getNodes()
#... do your load operation
nodes2 = getNodes()
filter(lambda x: x not in nodes1, nodes2)
</code></pre>

---
