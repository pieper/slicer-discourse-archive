---
topic_id: 6455
title: "Single Markup Fiducial Event Listener"
date: 2019-04-10
url: https://discourse.slicer.org/t/6455
---

# Single markup fiducial event listener

**Topic ID**: 6455
**Date**: 2019-04-10
**URL**: https://discourse.slicer.org/t/single-markup-fiducial-event-listener/6455

---

## Post #1 by @michalikthomas (2019-04-10 20:11 UTC)

<p>Is there any way how to observe events for a single markup fiducial? My goal is to detect a change of fiducial position.</p>

---

## Post #2 by @pieper (2019-04-11 20:03 UTC)

<p>The event includes the index <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L190" rel="nofollow noopener">as call data</a>.</p>
<p>You can <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function" rel="nofollow noopener">decorate your python callback</a> with the type, and then you know which control point was being interacted with.</p>
<p>You’ll still get events for any of the points being changed, but you can ignore any you don’t want to process.</p>
<pre><code class="lang-auto">@vtk.calldata_type(vtk.VTK_INT)
def callback(node,event,index):
    print(node, object, index)
    
markupNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, callback)
</code></pre>

---
