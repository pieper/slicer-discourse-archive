---
topic_id: 6332
title: "Handle Markups Events From An External Module"
date: 2019-03-28
url: https://discourse.slicer.org/t/6332
---

# Handle Markups events from an external module

**Topic ID**: 6332
**Date**: 2019-03-28
**URL**: https://discourse.slicer.org/t/handle-markups-events-from-an-external-module/6332

---

## Post #1 by @mirclem (2019-03-28 20:37 UTC)

<p>Hi,</p>
<p>I noticed there is a massive work in progress on the markups widget which affects some modules using markups interaction. As the markup position is now previewed when hovering a slice, “PointAddedEvent” is triggered when entering the view and “PointModifiedEvent” is permanently triggered when hovering the view.</p>
<p>I wanted to use “PointStartInteractionEvent” but it is listed as deprecated in <a class="mention" href="/u/lassoan">@lassoan</a> recent commit. I had a quick look at the newly created vtkMRMLInteractionEventData.h and the way it is done in the <a href="https://github.com/Slicer/Slicer/blob/e9e96fc3f285b8c9a45869ce0a98b799f81ec807/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidget.cxx#L493" rel="nofollow noopener">SlicerMarkupsWidget</a> but I can’t retranslate it into a python scripted module.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2019-03-28 23:19 UTC)

<p>The API is still being worked on. What would you like to do?</p>

---

## Post #4 by @mirclem (2019-03-29 14:35 UTC)

<p>I would like to get a callback function only when a marker is placed and dragged in a view. Basically, the behavior that an observer of “PointModifiedEvent” did before the update and preventing this callback to be called during the preview phase.<br>
I want to use that when you move a markup in one view, so the other views follow. (Double left-click current action)</p>
<p>Also, in this <a href="https://github.com/Slicer/Slicer/commit/6289b33445e6a0ee412476f3fb82cbe360238f0d#diff-e7034a6ddfa3156097919e3390b88a61" rel="nofollow noopener">commit</a> you mention that markups should now “Slide on surface”, but can’t find what changed compared to previous versions. Most of the modules I have been working on were using this:</p>
<pre><code>@vtk.calldata_type(vtk.VTK_INT)
def onPointModifiedEvent(self, caller, event, call_data):
    caller.RemoveObserver(tag["PointModifiedEventTag"])

    markupCoord = [0,0,0]
    caller.GetNthFiducialPosition(call_data, markupCoord)
    pointLocator = vtk.vtkPointLocator()
    pointLocator.SetDataSet(self.myModel.GetPolyData())
    pointLocator.AutomaticOn()
    pointLocator.BuildLocator()
    indexClosestPoint = pointLocator.FindClosestPoint(markupCoord)
    self.myModel.GetPolyData().GetPoints().GetPoint(indexClosestPoint, markupCoord)
    caller.SetNthFiducialPositionFromArray(call_data, markupCoord)

    PointModifiedEventTag = obj.AddObserver(obj.PointModifiedEvent, self.onPointModifiedEvent)</code></pre>

---

## Post #5 by @lassoan (2019-03-29 15:29 UTC)

<p>You can check the status of a point (undefined/previewed/placed) to distinguish between previewed and already placed state. Let me know if this information is enough.</p>
<p>Jumping slice views while moving a markup seems to be a common need, so we may just add a flag to the markups display widget to enable/disable this.</p>
<p>Also note that now you can click on a markup to jump to it in all slice views. This, combined with the ability to see out-of-plane markup points (enable <em>projection</em> in display settings), tracking the point on other slices might not be as important as before.</p>
<aside class="quote no-group" data-username="mirclem" data-post="4" data-topic="6332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mirclem/48/3356_2.png" class="avatar"> mirclem:</div>
<blockquote>
<p>you mention that markups should now “Slide on surface”,</p>
</blockquote>
</aside>
<p>Yes, all markups slide on visible surface now. There is a single picker that is shared between all widgets to improve performance.</p>

---

## Post #6 by @mirclem (2019-03-29 15:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="6332" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can check the status of a point (undefined/previewed/placed) to distinguish between previewed and already placed state. Let me know if this information is enough.</p>
</blockquote>
</aside>
<p>Oh true, this is done by <code>GetNthControlPointPositionStatus()</code>.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="6332" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Also note that now you can click on a markup to jump to it in all slice views. This, combined with the ability to see out-of-plane markup points (enable <em>projection</em> in display settings), tracking the point on other slices might not be as important as before.</p>
</blockquote>
</aside>
<p>The <em>projection</em> helps a lot to keep track of where the markup is, but when the markup slides on a round surface, it may shift to an adjacent slice and this might be confusing.</p>
<p>Anyway, thank you for the tips. I just downloaded today’s nightly version and many issues were solved compared to the one I had last week. I thought more maintenance would be needed for modules using markups but not anymore. I should not try to develop on WIP features.</p>

---

## Post #7 by @lassoan (2019-03-29 17:27 UTC)

<p>It is useful if you can test markups module and provide early feedback (what works, what you would need), because we can take those into account when refining the design or prioritizing development of new features.<br>
We’ll keep fixing and improving markups in the coming few months, so for production use, you might want to stick to the latest stable version of Slicer.</p>

---

## Post #8 by @ljod (2019-03-29 17:33 UTC)

<p>Hi Andras. This is a related question so I’m putting it here. We need to fix the SlicerDMRI usage of markups (interactive tractography) so SlicerDMRI can be available again in the nightlies. Specifically, what now replaces these events and calls (below), or where can I best look for an example of something similar?<br>
Thanks!!</p>
<p>MarkupAddedEvent<br>
MarkupRemovedEvent<br>
GetNthMarkupSelected</p>

---

## Post #9 by @lassoan (2019-03-29 17:37 UTC)

<p>Slicer5 migration guide should answer these questions, but let me know if it’s not enough.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Markups" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Markups</a></p>

---

## Post #10 by @ljod (2019-03-29 19:06 UTC)

<p>Thanks! I’ll check it out and let you know.</p>

---

## Post #11 by @lassoan (2019-03-29 19:40 UTC)

<p>Also let me know if there is any feature that you would like markups to have. Many things that were not feasible to implement with the old design are possible now.</p>

---

## Post #12 by @mirclem (2019-05-23 15:27 UTC)

<p>From what I can see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsDisplayNode.cxx#L377" rel="nofollow noopener">here</a>, “Markups.MovingInSliceView” and “Markups.MovingMarkupIndex” are only accessible when hovering the views (preview mode), why not when the point is placed and moved afterward?</p>

---

## Post #13 by @lassoan (2019-05-23 16:08 UTC)

<p>“MovingInSliceView” means that the point is moving. Anyway, it is kept for a while for backward compatibility only, since there is now much richer API (that does not rely on custom MRML node attributes) for getting much more information.</p>
<p>Event data is now vtkMRMLInteractionEventData for many events (that contains information of what part of the markup was manipulated in which view node), you can also query active component type and index from the display node, and “active” state is stored in the display node (so you can choose to highlight hovered-over markups in only selected views).</p>
<p>Let me know if you find any inconveniences with the new API. We can make improvements as needed.</p>

---

## Post #14 by @mirclem (2019-05-23 17:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="6332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Event data is now vtkMRMLInteractionEventData for many events (that contains information of what part of the markup was manipulated in which view node), you can also query active component type and index from the display node, and “active” state is stored in the display node (so you can choose to highlight hovered-over markups in only selected views).</p>
</blockquote>
</aside>
<p>I understand which information vtkMRMLInteractionEventData can carry and this is very helpful. When you say event data is vtkMRMLInteractionEventData, do you mean the third argument of the callback function should be that type?<br>
Would I change the callback definition to (following)?</p>
<pre><code>@vtk.calldata_type(vtk.VTK_OBJECT)
def onMarkupModified(self, caller, event, calldata):
</code></pre>
<p>And get current view like this:</p>
<pre><code>if isinstance(calldata, slicer.vtkMRMLInteractionEventData):
    calldata.GetViewNode()
</code></pre>

---

## Post #15 by @lassoan (2019-05-23 17:30 UTC)

<p>Yes, all above is correct.</p>

---

## Post #16 by @mirclem (2019-05-23 17:37 UTC)

<p>So far, Slicer crash without error message in the console using <code>@vtk.calldata_type(vtk.VTK_OBJECT)</code> when the mouse hovers a Slice View.</p>

---

## Post #17 by @mirclem (2019-05-23 19:09 UTC)

<p>And from Visual Studio Debugger, it says:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a8ddbbb689785e005455062c55c459e3d69e475.png" alt="error" data-base62-sha1="3MUlltYwScIzxAFMlWaXW7TlqWp" width="537" height="302"></p>

---

## Post #18 by @mirclem (2019-05-28 17:32 UTC)

<p>Anyone tried to replicate this bug? Should I submit it?</p>

---

## Post #19 by @pieper (2019-05-28 21:19 UTC)

<p>Hi <a class="mention" href="/u/mirclem">@mirclem</a>  - Yes, if you have a simple way to reproduce this behavior definitely file an issue and put the link to it here.  It would be great to have the snippet of python code to paste in the interactor and any steps needed that lead to the crash.</p>

---

## Post #20 by @lassoan (2019-05-28 22:24 UTC)

<p>I was able to reproduce the problem but did not have time to investigate much. The problem must likely is that the event data is not derived from vtkObject but from vtkObjectBase. I don’t know if there is a VTK calldata hint for vtkObjectBase, it would need to be investigated or asked on the VTK forum.</p>

---

## Post #21 by @mirclem (2019-05-29 14:39 UTC)

<p>Hi, Ok I will do that then. Here is the code I used to get to this error:</p>
<pre><code>@vtk.calldata_type(vtk.VTK_OBJECT)
def onMarkupChanged(caller,event,call_data):
	print(event)

markupsFiducialNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode')
markupsFiducialNode.AddObserver(slicer.vtkMRMLMarkupsFiducialNode.PointModifiedEvent, onMarkupChanged)

selectionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSelectionNodeSingleton")
selectionNode.SetReferenceActivePlaceNodeID(markupsFiducialNode.GetID())
interactionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton")
interactionNode.SetCurrentInteractionMode(1)
interactionNode.SetPlaceModePersistence(0)
</code></pre>
<p>Then, just mouse over any views.</p>

---

## Post #22 by @lassoan (2019-05-29 16:39 UTC)

<p>I’ve done some debugging and it turns out that PointModifiedEvent and similar high-level events still use integer parameters, so you can access them using</p>
<pre><code class="lang-auto">@vtk.calldata_type(vtk.VTK_INT)
def onMarkupChanged(caller,event,call_data):
    print(event)
    print(call_data)
</code></pre>
<p>More sophisticated interaction events are available at lower level (in VTK widgets) and those could be propagated to MRML nodes, but vtkEventData based objects are not Python-wrapped so they could not be used from Python. I’ve <a href="https://discourse.vtk.org/t/vtkeventdata-based-classes-are-not-python-wrapped/1044/2" rel="nofollow noopener">asked about this on VTK forum</a>. We’ll proceed according to what we hear back from there (it’ll be either a VTK fix or we add a vtkObject based wrapper around the vtkEventData based object).</p>

---

## Post #23 by @Johan_Andruejol (2019-08-23 20:16 UTC)

<p>Hi,</p>
<p>I have been working with the Markups and more specifically the PointAddedEvent.<br>
I have noticed that the event is only called when you switch to one view from another (like <a class="mention" href="/u/mirclem">@mirclem</a> noticed).<br>
I need to be able to know when a Markup control point is added (i.e. defined) in the view. Unfortunately the PointAddedEvent doesn’t fire when the point becomes defined. Here is the snippet that I used:</p>
<pre><code class="lang-python">m = slicer.mrmlScene.AddNode(slicer.vtkMRMLMarkupsFiducialNode())

def onPointAdded(caller, event):
  print("added ", caller.GetNthControlPointPositionStatus(0))

m.AddObserver(slicer.vtkMRMLMarkupsNode.PointAddedEvent, p)
</code></pre>
<p>This prints:</p>
<pre><code class="lang-auto">added 1 # View change (PointUndefined)
added 1 # View change (PointUndefined)
#Missing added 2 (PointDefined) :(
</code></pre>
<p>It doesn’t send a signal when the status becomes PointDefined.</p>
<p>I am aware that I could manage that through the PointModifiedEvent and check the point’s status but that seems counter-intuitive and it makes it harder for the UI.</p>
<p>Do you think adding a PointAddedEvent when the point becomes defined makes sense ?</p>
<p>Thanks !<br>
Johan</p>

---

## Post #24 by @lassoan (2019-08-23 21:01 UTC)

<p>It seems to be a common need to get notification when a point becomes defined, so I’ll add a new event for this.</p>

---

## Post #25 by @lassoan (2019-08-27 18:09 UTC)

<p>I’ve added a new pair of events (available in Slicer Preview Release from tomorrow): <code>slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent</code> and <code>slicer.vtkMRMLMarkupsNode.PointPositionUndefinedEvent</code>. These are only invoked when a point is placed or a placed point is removed. Not impacted by point previews.</p>
<pre><code class="lang-python">def onMarkupPointPositionDefined(caller, event):
    markupsNode = caller
    movingMarkupIndex = markupsNode.GetDisplayNode().GetActiveControlPoint()
    logging.info(f"Markup point added: point ID = {movingMarkupIndex}")

def onMarkupPointPositionUndefined(caller, event):
    markupsNode = caller
    logging.info(f"Markup point removed.")

markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
markupsNode.CreateDefaultDisplayNodes()
markupsNode.AddFiducial(0,0,0)
markupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent, onMarkupPointPositionDefined)
markupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointPositionUndefinedEvent, onMarkupPointPositionUndefined)
</code></pre>

---

## Post #26 by @Johan_Andruejol (2019-08-28 19:32 UTC)

<p>This is great ! Thanks so much !<br>
I was able to quickly make my code work with these.</p>
<p>P.S.:<br>
What’s the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L202" rel="nofollow noopener"><code>PointPlacedEvent</code></a> ? Was it added for future use ?</p>

---

## Post #27 by @lassoan (2019-08-28 19:44 UTC)

<aside class="quote no-group" data-username="Johan_Andruejol" data-post="26" data-topic="6332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/johan_andruejol/48/3639_2.png" class="avatar"> Johan_Andruejol:</div>
<blockquote>
<p>What’s the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsNode.h#L202"> <code>PointPlacedEvent</code> </a> ? Was it added for future use ?</p>
</blockquote>
</aside>
<p>I added that event ID but finally did not end up using it. I’ll write some tests and with that commit remove <code>PointPlacedEvent</code>.</p>

---

## Post #28 by @Fangwen_Zhai (2020-03-24 06:44 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="25" data-topic="6332" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve added a new pair of events (available in Slicer Preview Release from tomorrow): <code>slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent</code> and <code>slicer.vtkMRMLMarkupsNode.PointPositionUndefinedEvent</code>. These are only invoked when a point is placed or a placed point is removed. Not impacted by point previews.</p>
<pre data-code-wrap="python"><code class="lang-python">def onMarkupPointPositionDefined(caller, event):
    markupsNode = caller
    movingMarkupIndex = markupsNode.GetDisplayNode().GetActiveControlPoint()
    logging.info(f"Markup point added: point ID = {movingMarkupIndex}")

def onMarkupPointPositionUndefined(caller, event):
    markupsNode = caller
    movingMarkupIndex = markupsNode.GetDisplayNode().GetActiveControlPoint()
    logging.info(f"Markup point removed: point ID = {movingMarkupIndex}")

markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
markupsNode.CreateDefaultDisplayNodes()
markupsNode.AddFiducial(0,0,0)
markupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent, onMarkupPointPositionDefined)
markupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointPositionUndefinedEvent, onMarkupPointPositionUndefined)
</code></pre>
</blockquote>
</aside>
<p>As to the two events, there may be a bug in <code>bool vtkMRMLMarkupsNode::InsertControlPoint(ControlPoint *controlPoint, int targetIndex)</code>, line 689 of vtkMRMLMarkupsNode.cxx:</p>
<pre data-code-wrap="C++"><code class="lang-C++">// let observers know that a markup was added
  this-&gt;InvokeCustomModifiedEvent(vtkMRMLMarkupsNode::PointAddedEvent, static_cast&lt;void*&gt;(&amp;targetIndex));
  if (controlPoint-&gt;PositionStatus == vtkMRMLMarkupsNode::PositionDefined)
    {
    this-&gt;InvokeCustomModifiedEvent(vtkMRMLMarkupsNode::PointPositionUndefinedEvent, static_cast&lt;void*&gt;(&amp;targetIndex));
    }
  this-&gt;UpdateMeasurements();
</code></pre>
<p>I think PointPositionUndefinedEvent should be PointPositionDefinedEvent?</p>

---

## Post #29 by @lassoan (2020-03-24 12:19 UTC)

<p>Good catch, thank you, indeed when a point was inserted into a curve then wrong event ID was used. I’ve pushed a fix now, which will be available in the Slicer Preview Release from tomorrow.</p>

---
