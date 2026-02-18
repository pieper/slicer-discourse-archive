# How to delete display node and allocated resources properly?

**Topic ID**: 19979
**Date**: 2021-10-03
**URL**: https://discourse.slicer.org/t/how-to-delete-display-node-and-allocated-resources-properly/19979

---

## Post #1 by @Mik (2021-10-03 21:12 UTC)

<p>The process of adding support of multiple color bars via displayable manager <a href="https://github.com/Slicer/Slicer/pull/5828" rel="noopener nofollow ugc">PR #5828</a>.</p>
<p>The color bar display node is added to the scalar volume:</p>
<pre><code class="lang-auto">  // Create color bar and observe color bar by displayable node
  vtkMRMLColorBarDisplayNode* colorBarNode = vtkMRMLColorBarDisplayNode::SafeDownCast(mrmlScene-&gt;AddNewNodeByClass("vtkMRMLColorBarDisplayNode"));
  if (colorBarNode)
    {
    volumeNode-&gt;AddAndObserveDisplayNodeID(colorBarNode-&gt;GetID());
    return colorBarNode;
    }
</code></pre>
<p>The information about different display nodes is stored in display manager in the std::map (key - color bar display node ID, values - VTK widget, actor, and so on).</p>
<pre><code class="lang-auto">typedef std::tuple&lt; vtkSmartPointer&lt;vtkSlicerScalarBarActor&gt;, \
                    vtkSmartPointer&lt;vtkScalarBarWidget&gt;, \
                    bool &gt; ColorBarTuple;
  /// Map stores color bar display node ID, tuple
  std::map&lt; std::string, ColorBarTuple &gt; ColorBarTupleMap;
</code></pre>
<p>If i delete color bar display node i also want to delete VTK objects from the map object in the displayable manager.</p>
<pre><code class="lang-auto">      /// Delete color bar display node
      int n = d-&gt;colorLogic()-&gt;GetColorBarDisplayNodeNumberByNode( d-&gt;volumeNode, d-&gt;ColorBarNode);
      if (n != -1)
        {
        d-&gt;volumeNode-&gt;RemoveNthDisplayNodeID(n);
        this-&gt;mrmlScene()-&gt;RemoveNode(d-&gt;ColorBarNode);
        }
</code></pre>
<p>But when i try to delete data from map in display manager the application crashes</p>
<pre><code class="lang-auto">//---------------------------------------------------------------------------
void vtkMRMLColorBarDisplayableManager::OnMRMLSceneNodeRemoved(vtkMRMLNode* node)
{
  this-&gt;Superclass::OnMRMLSceneNodeRemoved(node);

  if (!node || !this-&gt;GetMRMLScene())
    {
    vtkErrorMacro("OnMRMLSceneNodeRemoved: Invalid MRML scene or input node");
    return;
    }

  if (node-&gt;IsA("vtkMRMLColorBarDisplayNode"))
    {
    vtkUnObserveMRMLNodeMacro(node);

    vtkMRMLColorBarDisplayNode* dispNode = vtkMRMLColorBarDisplayNode::SafeDownCast(node);
 
    auto it = this-&gt;Internal-&gt;ColorBarTupleMap.find(node-&gt;GetID());
    if (it != this-&gt;Internal-&gt;ColorBarTupleMap.end())
      {
      /// Delete VTK objects

      this-&gt;Internal-&gt;ColorBarTupleMap.erase(it); /// Crash of the 3D Slicer
      }
    }
}
</code></pre>
<p>Could i delete nodes in a display manager, and what is the proper way to do that? For example in “Volume Rendering” module the display nodes are stored and deleted in a logic and not in display manager.</p>

---
