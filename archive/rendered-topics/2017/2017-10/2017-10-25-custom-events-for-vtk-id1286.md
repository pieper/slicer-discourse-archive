# Custom Events for VTK

**Topic ID**: 1286
**Date**: 2017-10-25
**URL**: https://discourse.slicer.org/t/custom-events-for-vtk/1286

---

## Post #1 by @thomasyi17 (2017-10-25 17:41 UTC)

<p>Hello,</p>
<p>I was wondering if there is a convenient way to define custom vtk events (preferably at a high level) and thereafter attach a data payload to them?</p>
<p>As an analogous example, the qt slider widget has a valueChanged signal that has an attached payload containing the new value. In the context of vtk, one could then do something along the lines of (perhaps as a static variable):</p>
<p>var = vtk.vtkCommand.UserEvent + 100</p>
<p>Many thanks in advance.</p>

---

## Post #2 by @cpinter (2017-10-25 18:35 UTC)

<p>Examples of the stages of creating and using such a custom event (through SegmentModified):</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkSegmentation.h#L102">Definition</a></li>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkSegmentation.cxx#L577">Invocation with “payload” data</a></li>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/qSlicerSegmentationsModule.cxx#L265">Making connection</a></li>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/SubjectHierarchyPlugins/qSlicerSubjectHierarchySegmentationsPlugin.cxx#L606">Getting the “payload” data</a></li>
</ul>
<p>Handling the event is possible in Python as well (see example for <a href="https://github.com/SlicerRt/FilmDosimetryAnalysis/blob/master/FilmDosimetryAnalysis/FilmDosimetryAnalysis.py#L123">connecting</a> and <a href="https://github.com/SlicerRt/FilmDosimetryAnalysis/blob/master/FilmDosimetryAnalysis/FilmDosimetryAnalysis.py#L934">using</a>), but I’m not sure if you can define such an event from Python.</p>

---

## Post #3 by @pieper (2017-10-25 20:28 UTC)

<p>For some types of data can add a decorator to your callback that interprets the call data in python.</p>
<p><a href="https://github.com/Kitware/VTK/blob/master/Wrapping/Python/vtk/util/misc.py#L6-L27" class="onebox" target="_blank">https://github.com/Kitware/VTK/blob/master/Wrapping/Python/vtk/util/misc.py#L6-L27</a></p>
<p>For most data types in Slicer, a vtkObject is actually returned as a wrapped version of whatever concrete subclass was passed in the payload, so it actually covers all slicer events that come from nodes or the scene or other classes.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/ee5c8703642cf8f42e9594bc780cb0801623b39d/Modules/Scripted/DICOMLib/DICOMWidgets.py#L828-L832" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/ee5c8703642cf8f42e9594bc780cb0801623b39d/Modules/Scripted/DICOMLib/DICOMWidgets.py#L828-L832" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/ee5c8703642cf8f42e9594bc780cb0801623b39d/Modules/Scripted/DICOMLib/DICOMWidgets.py#L828-L832</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="828" style="counter-reset: li-counter 827 ;">
<li>@vtk.calldata_type(vtk.VTK_OBJECT)</li>
<li>def onNodeAdded(caller, event, calldata):</li>
<li>  node = calldata</li>
<li>  if isinstance(node, slicer.vtkMRMLVolumeNode):</li>
<li>    loadedNodeIDs.append(node.GetID())</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>You can also call InvokeEvent from python with a calldata (payload) argument.</p>
<p>In practice it’s often the case in Slicer that you don’t need calldata because knowing the caller is enough to get the information you want because what would otherwise be the payload data has already been set in the corresponding instance variable of the caller.</p>

---
