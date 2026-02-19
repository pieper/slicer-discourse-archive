---
topic_id: 40474
title: "Possible Regression In Events Triggered By Plane And Roi Mar"
date: 2024-12-02
url: https://discourse.slicer.org/t/40474
---

# Possible regression in events triggered by plane and ROI markups

**Topic ID**: 40474
**Date**: 2024-12-02
**URL**: https://discourse.slicer.org/t/possible-regression-in-events-triggered-by-plane-and-roi-markups/40474

---

## Post #1 by @rfenioux (2024-12-02 11:34 UTC)

<p>Hi all,</p>
<p>I am encountering an inconsistent behavior regarding the handling of events for plane and ROI markups in the latest preview version of Slicer, comparing to the stable release (slicer 5.6.2)</p>
<p>It seems that in the cases detailed below, some events are missing.</p>
<p>Here is the detailed behaviour :</p>
<p><strong>Reproduction:</strong><br>
OS = Windows 11<br>
Slicer version  = 5.7.0 (revision 33134, built 2024-12-01) compared to slicer 5.6.2 (both installed from binaries)</p>
<ol>
<li>Create the markups (plane or ROI) using the markups module</li>
<li>use the following snippet to get the node and connect the observers</li>
</ol>
<pre><code class="lang-auto"># retrieve the node using its name (default is P for plane, R for ROI)
node = getNode("P")
# connect callbacks 
node.AddObserver(slicer.vtkMRMLMarkupsROINode.PointStartInteractionEvent, lambda *_: print("start"))
node.AddObserver(slicer.vtkMRMLMarkupsROINode.PointModifiedEvent, lambda *_: print("modified"))
node.AddObserver(slicer.vtkMRMLMarkupsROINode.PointEndInteractionEvent, lambda *_: print("end"))
</code></pre>
<ol start="3">
<li>observe the console logs while click and dragging either the center point, or the corner (or side) handles</li>
</ol>
<p><strong>Results:</strong><br>
Here are the events triggered depending on the use cases</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Use case</th>
<th>Slicer 5.6.2</th>
<th>Slicer 5.7.2 2024-12-01</th>
</tr>
</thead>
<tbody>
<tr>
<td>Dragging center of ROI</td>
<td>startInteraction, modified, endInteraction</td>
<td>modified</td>
</tr>
<tr>
<td>Dragging corner of ROI</td>
<td>startInteraction, modified, endInteraction</td>
<td>modified</td>
</tr>
<tr>
<td>Draging center of plane markup</td>
<td>startInteraction, modified, endInteraction</td>
<td>startInteraction, modifiedEvents, endInteraction</td>
</tr>
<tr>
<td>Dragging corner of plane markup</td>
<td>StartInteraction, endInteraction*</td>
<td>No event</td>
</tr>
</tbody>
</table>
</div><p>*The first time a corner of the plane is moved in 5.6.2, a single <code>modifiedEvent</code> is triggered between the <code>start</code> and <code>end</code> events</p>
<p>To me it seems like a regression, unless I have missed an API change regarding the events of these markups. I didn’t notice any change in other markups (fiducial, line, angle…) but I haven’t tried all of them.</p>
<p>I would be grateful if you have any insight on what could be causing these changes.</p>

---

## Post #2 by @lassoan (2024-12-02 16:03 UTC)

<p>Control point modifications still invoke PointStartInterActionEvent, PointModifiedEvent, PointEndInteractionEvent events. However, plane and ROI position and sizes are not defined by control points but mostly by the new vtkMRMLInteractionWidget, which does not emit start/end interaction events. It may be still possible to add these events to the interaction widget before we release Slicer-5.8. To make sure we try to include this, please add an issue at <a href="https://issues.slicer.org">https://issues.slicer.org</a>.</p>
<p>Can you write about your use case? How do you use these interaction events?</p>

---

## Post #3 by @rfenioux (2024-12-02 16:45 UTC)

<p>Thank you for the clarification.</p>
<p><a href="https://github.com/Slicer/Slicer/issues/8074" rel="noopener nofollow ugc">Here is the link</a> to the corresponding issue I created.</p>
<p>We often use markups as handles for controlling 3D assets and rely on those events to update their properties.</p>

---

## Post #4 by @lassoan (2024-12-02 17:02 UTC)

<p>You can control 3D assets using node modified events. It is only necessary to know about interaction (when the user depresses and releases the mouse button) in very rare, special cases, such as you cannot de real-time updates continuouslt. What is your special use case?</p>
<p>Are you aware that transforms have now widgets in 2D and 3D (so you don’t need to use ROIs or planes for positioning, rotating, and scaling them)?</p>

---

## Post #5 by @rfenioux (2024-12-03 13:19 UTC)

<p>Start- and End- interaction events are used for undo / redo logic.</p>
<p>Real time updates also pose a problem when performance is an issue (e.g when the event is triggering a processing pipeline on the data). Sometimes it makes more sense to let the user do the positioning and re-run the pipeline only once on mouse release than to do it real time with too much lag.</p>
<p>I understand that there are options around it, but none of them are painless. And from a developer perspective, I think it would be valuable to keep the API consistent for all markups types. Having some markups not trigger the same events as others adds a bit of complexity, since it is not immediately obvious why they would have a different behavior. So I think it could be worth adding these events back.</p>

---

## Post #6 by @lassoan (2024-12-11 14:31 UTC)

<p>We will try to get this done before releasing Slicer-5.8 within a few weeks.</p>

---
