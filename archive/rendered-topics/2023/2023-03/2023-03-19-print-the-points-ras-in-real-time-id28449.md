# Print the point's RAS in real time

**Topic ID**: 28449
**Date**: 2023-03-19
**URL**: https://discourse.slicer.org/t/print-the-points-ras-in-real-time/28449

---

## Post #1 by @slicer365 (2023-03-19 12:08 UTC)

<p>I creat a point F, I want to print the point’s RAS position in python console，in real-time，when I move it.</p>
<p>Anyone can tell me how to write the script?</p>
<p>I write it as like this，it doesn’t work:</p>
<pre><code class="lang-auto">F_Node=getNode('F')

def printRAS(Node，Event=None):
      print(Node.GetNthFiducialPosition(0, position))

Tag = F_Node.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent,  printRAS)
</code></pre>

---

## Post #2 by @pieper (2023-03-19 16:59 UTC)

<p>If you try calling your <code>printRAS</code> function with the node as a parameter you can see <code>position</code> is not defined.  Also if you do use <code>help(F_node.GetNthFiducialPosition)</code> you can see that <code>GetNthFiducialPosition</code> is deprecated and you should use <code>GetNthControlPointPosition</code> instead.</p>
<p>So the better code would be:</p>
<pre><code class="lang-auto">def printRAS(Node, Event=None):
    print(Node.GetNthControlPointPosition(0))

F_Node.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, printRAS)</code></pre>

---
