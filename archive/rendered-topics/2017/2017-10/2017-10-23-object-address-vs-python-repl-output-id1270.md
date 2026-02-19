---
topic_id: 1270
title: "Object Address Vs Python Repl Output"
date: 2017-10-23
url: https://discourse.slicer.org/t/1270
---

# Object address vs Python REPL output

**Topic ID**: 1270
**Date**: 2017-10-23
**URL**: https://discourse.slicer.org/t/object-address-vs-python-repl-output/1270

---

## Post #1 by @ihnorton (2017-10-23 19:14 UTC)

<p>What is the address (<code>0x1307bea10</code>) printed next to the object type below for the “basic” REPL output? I guess it might be the PythonQt temporary for the string return, or maybe the constructor? (clearly the real object address is <code>0x132f20c50</code>)</p>
<pre><code class="lang-auto">&gt;&gt;&gt; n=getNode("tissue")
&gt;&gt;&gt; n
(vtkCommonCorePython.vtkMRMLModelNode)0x1307bea10
&gt;&gt;&gt; n.__this__
'_0000000132f20c50_p_vtkMRMLModelNode'
&gt;&gt;&gt; print n
vtkMRMLModelNode (0x132f20c50)
  ID: vtkMRMLModelNode4
...
</code></pre>
<details>
<summary>
rest of output</summary>
<pre><code class="lang-auto">  Debug: Off
  Modified Time: 1075109
  Name: tissue
  Description: (none)
  SingletonTag: (none)
  HideFromEditors: 0
  Selectable: 1
  Selected: 0
  Indent:      0
  Node references:
    display [displayNodeRef]: vtkMRMLModelDisplayNode5
    storage [storageNodeRef]: (none)
    transform [transformNodeRef]: (none)
  Debug: Off
  Modified Time: 1074628
  Reference Count: 1
  Registered Events: (none)
  Name = (none)
  RestoreSelectionState = 0
  TransformNodeID: (none)
  DisplayNodeIDs[0]: vtkMRMLModelDisplayNode5
  
Poly Data:
    Debug: Off
    Modified Time: 1073925
    Reference Count: 1
    Registered Events: (none)
    Information: 0x608000e7e280
    Data Released: False
    Global Release Data: Off
    UpdateTime: 1073926
    Field Data:
      Debug: Off
      Modified Time: 1073889
      Reference Count: 1
      Registered Events: (none)
      Number Of Arrays: 0
      Number Of Components: 0
      Number Of Tuples: 0
    Number Of Points: 5917
    Number Of Cells: 1570
    Cell Data:
      Debug: Off
      Modified Time: 1073897
      Reference Count: 1
      Registered Events: 
        Registered Observers:
          vtkObserver (0x608000e58180)
            Event: 33
            EventName: ModifiedEvent
            Command: 0x608000e7dc40
            Priority: 0
            Tag: 1
      Number Of Arrays: 0
      Number Of Components: 0
      Number Of Tuples: 0
      Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 )
      Interpolate Flags: ( 1 1 1 1 1 0 0 1 )
      Pass Through Flags: ( 1 1 1 1 1 1 1 1 )
      Scalars: (none)
      Vectors: (none)
      Normals: (none)
      TCoords: (none)
      Tensors: (none)
      GlobalIds: (none)
      PedigreeIds: (none)
      EdgeFlag: (none)
    Point Data:
      Debug: Off
      Modified Time: 1073925
      Reference Count: 1
      Registered Events: 
        Registered Observers:
          vtkObserver (0x608000e57d60)
            Event: 33
            EventName: ModifiedEvent
            Command: 0x608000e7dc40
            Priority: 0
            Tag: 1
      Number Of Arrays: 1
      Array 0 name = Normals
      Number Of Components: 3
      Number Of Tuples: 5917
      Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 )
      Interpolate Flags: ( 1 1 1 1 1 0 0 1 )
      Pass Through Flags: ( 1 1 1 1 1 1 1 1 )
      Scalars: (none)
      Vectors: (none)
      Normals: 
        Debug: Off
        Modified Time: 1073922
        Reference Count: 4
        Registered Events: (none)
        Name: Normals
        Data type: float
        Size: 17754
        MaxId: 17750
        NumberOfComponents: 3
        Information: 0
        Name: Normals
        Number Of Components: 3
        Number Of Tuples: 5917
        Size: 17754
        MaxId: 17750
        LookupTable: (none)
      TCoords: (none)
      Tensors: (none)
      GlobalIds: (none)
      PedigreeIds: (none)
      EdgeFlag: (none)
    Bounds: 
      Xmin,Xmax: (-35.2613, 36.24)
      Ymin,Ymax: (-46.4626, 19.3652)
      Zmin,Zmax: (-10.8084, -5.64577)
    Compute Time: 1101077
    Number Of Points: 5917
    Point Coordinates: 0x6000008ce620
    Locator: 0
    Number Of Vertices: 0
    Number Of Lines: 0
    Number Of Polygons: 0
    Number Of Triangle Strips: 1570
    Number Of Pieces: 1
    Piece: 0
    Ghost Level: 0
</code></pre>
</details>

---

## Post #2 by @jcfr (2017-10-23 19:54 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="1" data-topic="1270">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>I guess it might be the PythonQt temporary for the string return, or maybe the constructor?</p>
</blockquote>
</aside>
<p>Base one this experiment, look like this is specific to VTK wrapping:</p>
<p>Update current environment:</p>
<pre><code class="lang-auto">eval $(./Slicer --launcher-show-set-environment-commands)
</code></pre>
<p>Start Slicer python and try to reproduce:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import mrml
&gt;&gt;&gt; n = mrml.vtkMRMLModelNode()
&gt;&gt;&gt; n
(vtkCommonCorePython.vtkMRMLModelNode)0x7fe119235db8
&gt;&gt;&gt; n.__this__
'_0000000002476cc0_p_vtkMRMLModelNode'
&gt;&gt;&gt; print(n)
vtkMRMLModelNode (0x2476cc0)
  ID: (none)
  Class: vtkMRMLModelNode
  Debug: Off
  Modified Time: 73
  Name: (none)
  Description: (none)
  SingletonTag: (none)
  HideFromEditors: 0
  Selectable: 1
  Selected: 0
  Node references:
    display [displayNodeRef]: (none)
    storage [storageNodeRef]: (none)
    transform [transformNodeRef]: (none)
  Debug: Off
  Modified Time: 75
  Reference Count: 1
  Registered Events: (none)
  Name = (none)
  RestoreSelectionState = 0
  TransformNodeID: (none)
  
Unstructured Grid: none  
Poly Data: none
</code></pre>
<p>Addresses are different outside of the PythonQt environment.</p>
<p>I suggest you bring the issue on the VTK mailing list.</p>

---

## Post #3 by @ihnorton (2017-10-23 20:36 UTC)

<p>Thanks, I see – it’s taking the <a href="https://github.com/Kitware/VTK/blob/master/Wrapping/PythonCore/PyVTKObject.cxx#L127">address of the proxy PyObject</a>. That’s a little confusing, but I only noticed because the addresses didn’t match what I saw in the debugger.</p>

---
