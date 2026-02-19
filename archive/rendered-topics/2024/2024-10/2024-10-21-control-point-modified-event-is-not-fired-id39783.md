---
topic_id: 39783
title: "Control Point Modified Event Is Not Fired"
date: 2024-10-21
url: https://discourse.slicer.org/t/39783
---

# Control point modified event is not fired

**Topic ID**: 39783
**Date**: 2024-10-21
**URL**: https://discourse.slicer.org/t/control-point-modified-event-is-not-fired/39783

---

## Post #1 by @mau_igna_06 (2024-10-21 20:28 UTC)

<p>Hi,</p>
<p>I think I’ve found a bug:</p>
<pre><code class="lang-auto">lineNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLMarkupsLineNode")
slicer.mrmlScene.AddNode(lineNode)
slicer.modules.markups.logic().AddNewDisplayNodeForMarkupsNode(lineNode)
lineNode.SetName("myLineNode")

observerTag = lineNode.AddObserver(
    slicer.vtkMRMLMarkupsNode.PointModifiedEvent,
    lambda arg1,arg2: print("Point modified")
)

# does print
lineNode.AddControlPoint(vtk.vtkVector3d(0,0,0))
# does print
lineNode.AddControlPoint(vtk.vtkVector3d(50,50,50))

for i in range(lineNode.GetNumberOfControlPoints()):
    # doesn't print but it should
    lineNode.RemoveNthControlPoint(0) 
</code></pre>
<p>Maybe I’m doing something wrong, please explain</p>
<p>Best wishes,<br>
Mauro</p>

---

## Post #2 by @lassoan (2024-10-22 00:02 UTC)

<p>We try to invoke a <code>PointModifiedEvent</code> whenever it is possible to reduce the number of events that modules have to observe. However, in case of deleting a point it would not be clear if the point id refers to the point that was removed or to the point that was moved to the removed point’s position. Instead, <code>vtkMRMLMarkupsNode::PointAboutToBeRemovedEvent</code> and <code>vtkMRMLMarkupsNode::PointRemovedEvent</code> events are invoked with the removed point’s index.</p>
<p>I can see that this behavior may seem inconsistent and it may be inconvenient that you need to observe an additional event, so let me know if you think it would help you if different events were invoked. It would not be a problem at all to invoke a <code>PointModifiedEvent</code> with the removed point’s index if that would greatly simplify your code.</p>

---

## Post #3 by @mau_igna_06 (2024-10-22 00:10 UTC)

<p>I tried doing something like:</p>
<pre><code class="lang-auto">observerTag = lineNode.AddObserver(
    slicer.vtkMRMLMarkupsNode.PointModifiedEvent | slicer.vtkMRMLMarkupsNode.PointRemovedEvent,
    lambda arg1,arg2: print("Point modified")
)
</code></pre>
<p>But it did not work.<br>
I don’t mind another observer for the moment</p>

---

## Post #4 by @lassoan (2024-10-22 00:53 UTC)

<p>The result of <code>slicer.vtkMRMLMarkupsNode.PointModifiedEvent | slicer.vtkMRMLMarkupsNode.PointRemovedEvent</code> operation is some number that probably does not correspond to any event ID. You need to add and remove each observer separately.</p>

---

## Post #5 by @Abhishek_Markad (2024-11-04 10:29 UTC)

<p>how to access control point index in invoked function.</p>
<p>Below is the python snippet,is it right way?</p>
<pre><code class="lang-auto">pointListNode = slicer.mrmlScene.AddNewNodeByClass(
            "vtkMRMLMarkupsFiducialNode"
        )
pointListNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointAboutToBeRemovedEvent,on_point_to_be_removed)
def on_point_to_be_removed(caller,event):
        markupsNode = caller
        sliceView = markupsNode.GetAttribute("Markups.MovingInSliceView")
        movingMarkupIndex = markupsNode.GetDisplayNode().GetActiveControlPoint()
        print(movingMarkupIndex)
        label=markupsNode.GetNthControlPointLabel(movingMarkupIndex)
</code></pre>
<p>Output:<br>
-1<br>
GUI used to remove the control point.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27faad684eaa6d4fb20f8d1933c30a60fc4611bf.jpeg" data-download-href="/uploads/short-url/5HFH67MaL2YqiFAMGUC3MBAGKxV.jpeg?dl=1" title="delete_control_point" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27faad684eaa6d4fb20f8d1933c30a60fc4611bf_2_690x388.jpeg" alt="delete_control_point" data-base62-sha1="5HFH67MaL2YqiFAMGUC3MBAGKxV" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27faad684eaa6d4fb20f8d1933c30a60fc4611bf_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27faad684eaa6d4fb20f8d1933c30a60fc4611bf_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27faad684eaa6d4fb20f8d1933c30a60fc4611bf.jpeg 2x" data-dominant-color="6C6A6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">delete_control_point</span><span class="informations">1280×720 98.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to access label of control point to be removed.<br>
Thank you.</p>

---

## Post #6 by @cpinter (2024-11-05 14:38 UTC)

<p>I don’t have any working example but I think you need to define the callback function like this:</p>
<pre><code class="lang-auto">@vtk.calldata_type(vtk.VTK_INT)
def onPointAboutToBeRemoved(self, caller, eventId, callData):
</code></pre>
<p>The <code>callData</code> will be the point index. <code>self</code> obviously is only needed if the callback is a member function.</p>

---
