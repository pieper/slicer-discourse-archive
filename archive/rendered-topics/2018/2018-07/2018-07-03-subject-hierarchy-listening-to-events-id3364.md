# Subject hierarchy listening to events

**Topic ID**: 3364
**Date**: 2018-07-03
**URL**: https://discourse.slicer.org/t/subject-hierarchy-listening-to-events/3364

---

## Post #1 by @Johan_Andruejol (2018-07-03 17:46 UTC)

<p>Hi all,</p>
<p>I am working a module that relies heavily on the subject hierarchy. I need to listen to its modified/added and removed item events. Here is an abstract of what I do:</p>
<pre><code>class MyClass(VTKObservationMixin):
  def __init__(self):
    VTKObservationMixin.__init__(self)
    shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
    self.addObserver(shNode, shNode.SubjectHierarchyItemModifiedEvent, self.shItemModifiedEvent)
  
  @vtk.calldata_type(vtk.VTK_LONG)
  def shItemModifiedEvent(self, caller, eventId, callData=None):
    print("SH Node mod")
    print("SH item ID: {0}".format(callData))

obj = MyClass()

shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

itemID = shNode.CreateFolderItem(shNode.GetSceneItemID(), 'Test')

wasModifying = shNode.StartModify()
shNode.SetItemName(itemID, 'NewName')
shNode.SetItemAttribute(itemID, 'NewAttribute', 'a')
shNode.EndModify(wasModifying)
</code></pre>
<p>This crashes on Slicer that I built manually.<br>
The issues comes from the<code>EndModify()</code> that will <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLNode.h#L478" rel="nofollow noopener">re-invoke all the custom events</a>. Those events however are invoked without a calldata and that makes the application crash when it tries to convert the calldata to long.</p>
<p>I am not sure what can be done for this. The naive solution I see would be to never use the calldata to answer the callback of the subject hierarchy. But then we would need a method on the subject hierarchy node to know what was the item ID that was last modified ?<br>
Or should the <a href="https://github.com/Kitware/VTK/blob/master/Wrapping/PythonCore/vtkPythonCommand.cxx#L169" rel="nofollow noopener">VTK python command handle</a> the case where the calldata is NULL better ?</p>
<p>Thanks !<br>
Johan</p>

---

## Post #2 by @Johan_Andruejol (2018-07-18 13:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/cpinter">@cpinter</a>:<br>
I am thinking to implement  a method that stores the ID of the last modified item so it’s always accessible through python. Since you implemented this node, I was wondering what you were thinking ?</p>

---

## Post #3 by @jcfr (2018-07-18 14:12 UTC)

<p>After talking with <a class="mention" href="/u/lassoan">@lassoan</a>, the current mechanism is generic and can handle any event. As you first suggested, we should instead fix the VTK wrapping layer to that the call data is None if the pointer is null.</p>
<p>From the application perspective, this would mean that we can’t know the specific ID or name or … that was modified and the UI should be refreshed.</p>

---

## Post #4 by @jcfr (2018-07-18 14:21 UTC)

<p>For all types, the code could then be changed from:</p>
<pre><code class="lang-auto">PyObject* callDataAsInt = PyLong_FromLong(*reinterpret_cast&lt;long*&gt;(callData));
arglist = BuildCallDataArgList(obj2, eventname, callDataAsInt);
</code></pre>
<p>to</p>
<pre><code class="lang-auto">PyObject* callDataAsInt = callData != nullptr ? PyLong_FromLong(*reinterpret_cast&lt;long*&gt;(callData)) : nullptr;
arglist = BuildCallDataArgList(obj2, eventname, callDataAsInt);
</code></pre>
<p>(or the more explicit multi-line version …)</p>

---

## Post #5 by @Johan_Andruejol (2018-07-18 14:37 UTC)

<p>That makes sense to me. I will create a PR.<br>
Thanks !</p>

---

## Post #6 by @cpinter (2018-07-18 14:54 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for helping Johan! I just managed to dig through the administrative stuff and get back to real work after I got back from my long trip.</p>

---

## Post #7 by @Johan_Andruejol (2018-07-18 17:03 UTC)

<p>I created a PR on VTK (<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4513" rel="nofollow noopener">https://gitlab.kitware.com/vtk/vtk/merge_requests/4513</a>) and Slicer: <a href="https://github.com/Slicer/VTK/pull/17" rel="nofollow noopener">https://github.com/Slicer/VTK/pull/17</a>.</p>

---

## Post #8 by @Johan_Andruejol (2018-07-26 18:20 UTC)

<p>So the NULL handling bug is actually already fixed on VTK9.</p>
<p>I have noticed however that running the following code does generate a lot of errors:</p>
<pre><code>shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
itemID = shNode.CreateFolderItem(shNode.GetSceneItemID(), 'Test')

with slicer.util.NodeModify(shNode):
  shNode.SetItemName(itemID, 'NewName')
  shNode.SetItemAttribute(itemID, 'NewAttribute', 'a')
</code></pre>
<p>Errors:</p>
<pre><code>double __cdecl qSlicerSubjectHierarchyFolderPlugin::canOwnSubjectHierarchyItem(__int64) const : Input item is invalid! 
double __cdecl qSlicerSubjectHierarchyChartsPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchyPlotChartPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
GetItemDataNode: Failed to find subject hierarchy item by ID 0


double __cdecl qSlicerSubjectHierarchyVolumesPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchyLabelMapsPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchyDiffusionTensorVolumesPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchyDICOMPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchyMarkupsPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchyModelsPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchySceneViewsPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchySegmentationsPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchySegmentsPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchyTablesPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
double __cdecl qSlicerSubjectHierarchyTransformsPlugin::canOwnSubjectHierarchyItem(__int64) const : Invalid input item 
SetItemOwnerPluginName: Failed to find subject hierarchy item by ID 0
</code></pre>
<p><a class="mention" href="/u/cpinter">@cpinter</a>, <a class="mention" href="/u/jcfr">@jcfr</a>: I think the SH node should fail silently when you request an invalid item ID. What do you think ?</p>

---

## Post #9 by @cpinter (2018-07-26 18:41 UTC)

<p>I have been thinking about this as well, but haven’t made this change, because trying to find a non-existent item is an operation that probably leads to errors, so logging an error can be useful.</p>
<p>I think instead of making this fail silently you could investigate why these operations want to access this non-existent item.</p>

---

## Post #10 by @Johan_Andruejol (2018-07-26 19:16 UTC)

<p>In this case, it’s because the <code>SubjectHierarchyItemModifiedEvent</code> is called with NULL calldata. This happens whenever you group modifications of the Subject Hierarchy Node together with a <code>StartModify()/EndModify()</code> (see here: <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLNode.h#L478" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLNode.h#L478</a>).</p>
<p>As I see it, we have two options:</p>
<ul>
<li>We simply ignore any event passed with NULL calldata. Users will have to be careful when using batch updated with the Subject Hierachy Node and call ItemModified() themselves if needed.</li>
<li>We could re-implement <code>vtkMRMLNode::InvokeCustomModifiedEvent</code> and <code>vtkMRMLNode::InvokePendingModifiedEvent</code> in the Subject Hierarchy node to handle passing the item ID</li>
</ul>
<p>I don’t feel that any of these are ideal, so feel free to suggest other ideas !</p>

---

## Post #11 by @lassoan (2018-07-26 19:49 UTC)

<p>Normally, any custom modified events with NULL calldata means that multiple updates happened, so a full update is needed. Therefore, for me the obvious solution is to handle this as a full update.</p>
<p>Batch processing is always has overhead, so it should only be used if either A. it is important to not invoke (custom) modified events before multiple modifications are completed; or B. to improve performance by replacing many small updates by one big update. If you find that You may decide to call Start/EndModify only when many items are modified (similarly how it is done <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLModelHierarchyLogic.cxx#L260">here</a>, when batch processing mode is used only when more than a few models had to be updated).</p>

---
