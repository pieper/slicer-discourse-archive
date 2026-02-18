# How to display the label (or Name) of ControlPoint of vtkMRMLMarkupsCurveNode?

**Topic ID**: 25142
**Date**: 2022-09-07
**URL**: https://discourse.slicer.org/t/how-to-display-the-label-or-name-of-controlpoint-of-vtkmrmlmarkupscurvenode/25142

---

## Post #1 by @sunshine (2022-09-07 15:34 UTC)

<p>Hi everyone,</p>
<p>I have a question about the module Markups. In a PointList, I can see the label (or Name) of each ControlPoint, and I can choose to display or hide it.</p>
<p>How can I do the same thing for the MarkupsCurveNode? I was not able to display the label (or Name) of a ControlPoint of a MarkupsCurveNode.<br>
If it is possible to display, what is the function to toggle that using python code?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @Sunderlandkyl (2022-09-07 15:38 UTC)

<p>Yes, using <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsDisplayNode.html#a43df1ecfc13afd84ede7b39c2c8d2469" rel="noopener nofollow ugc">vtkMRMLMarkupsDisplayNode::SetPointLabelsVisibility</a>:</p>
<pre><code class="lang-python">curveNode.GetDisplayNode().SetPointLabelsVisibility(True)
</code></pre>

---

## Post #3 by @sunshine (2022-09-07 15:44 UTC)

<p>Hi Kyle,</p>
<p>Thank you so much for your reply!</p>
<p>Would it be possible to trigger the label visibility of only one ControlPoint?</p>
<p>I am trying to create a CurveNode, and would like to add an observer that whenever my mouse hovers over a ControlPoint, its label displays. Could you please let me know the Event or Signal I should use and the function to trigger the one-ControlPoint Visibility?</p>
<p>Thank you again!</p>

---

## Post #4 by @Sunderlandkyl (2022-09-07 16:17 UTC)

<p>No, it looks like it’s currently only applied to all control points.</p>
<p>A workaround could be to set the control point labels that you don’t want displayed to an empty string with <code>curveNode.SetNthControlPointLabel(i, "")</code>.</p>

---

## Post #5 by @sunshine (2022-09-07 16:24 UTC)

<p>Thank you so much, Kyle!</p>
<p>I have two more questions that may need your help:</p>
<ol>
<li>Do we have an Event / Signal for ControlPoint Mouse Hover detection?</li>
<li>Can we initialize empty ControlPoints as place-holder in the CurveNode, so that the number of Control Points counts but the empty CurveNode has nothing to display? In this way, I can add/remove the ControlPoints without messing up the sequential significance of each ControPoint.</li>
</ol>

---

## Post #6 by @Sunderlandkyl (2022-09-07 16:50 UTC)

<ol>
<li>
<p>You can attach a vtk.vtkCommand.ModifiedEvent observer to the display node, and can tell what control point is active using GetActiveComponentType to make sure it is a control point that is active (slicer.vtkMRMLMarkupsDisplayNode.ComponentControlPoint), and GetActiveComponentIndex to get the index of the active control point.</p>
</li>
<li>
<p>You can initialize the control points and use curveNode.UnsetNthControlPointPosition to mark them as unplaced.</p>
</li>
</ol>

---

## Post #7 by @sunshine (2022-09-07 20:50 UTC)

<p>Hi Kyle,</p>
<p>Thank you so much for your help!</p>
<p>I just tested the function <code>curveNode.UnsetNthControlPointPosition()</code>, however, I am not sure this function can help my case.</p>
<p>I would like to create a CurveNode, and add ControlPoint directly to the Nth, because the sequential value N is important to me.  Is it possible?</p>
<p>E.g., after calling</p>
<pre><code class="lang-auto">node_Curve = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
</code></pre>
<p>I would like to apply a function like this:</p>
<pre><code class="lang-auto">for idx_DataNode in range(10):
        node_Curve.UnsetNthControlPointPosition(idx_DataNode)

node_Curve.SetNthControlPoint(10, [2, 3, 4])
</code></pre>
<p>and I wish to get something like:</p>
<pre><code class="lang-auto">array = node_Curve.GetNthControlPoint(10)
print(array) : [2, 3, 4]
</code></pre>
<p>Could you please let me know how to achieve the above case?</p>

---

## Post #8 by @Sunderlandkyl (2022-09-08 14:25 UTC)

<p>You’ll need to initialize the markups node with the desired number of control points. Something like this:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#how-to-draw-a-curve-using-control-points-stored-in-a-numpy-array" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#how-to-draw-a-curve-using-control-points-stored-in-a-numpy-array</a></p>
<p>If you know ahead of time how many control points you will need, you can create the markups node with the desired number of unset control points, save it as a json and load that template to populate the curve node.</p>

---

## Post #9 by @sunshine (2022-09-08 14:54 UTC)

<p>That looks nice! However, using this array will require all ControlPoints defined.</p>
<p>Is it possible that, I know the number of maximum ControlPoints, and fill in the CurveNode one by one while keeping the undefined ControlPoints with empty place-holders?</p>

---

## Post #10 by @Sunderlandkyl (2022-09-08 16:13 UTC)

<p>If you initialize the curve using the array and unset the control points using UnsetNthControlPointPosition, then you can allow the user place the Nth control point at a later time.</p>
<p>Markups also have a “MaximumNumberOfControlPoints” variable that would limit the number of control points that can be placed, however it doesn’t seem to be exposed for curve nodes.</p>

---

## Post #11 by @sunshine (2022-09-12 19:03 UTC)

<p>Hi Kyle,</p>
<p>I really like the idea of combining array initialization <code>updateMarkupsControlPointsFromArray</code> and <code>UnsetNthControlPointPosition</code> together, however, it is unfortunately not user-friendly in practice.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2206c0a2da962acc7b8d4e1acfe465090a4410bc.png" alt="image" data-base62-sha1="4R0Ht8kmr5b5VLeGKaMt9gf8xIw" width="617" height="250"></p>
<p>As you can see from the screenshot, it cost about <strong>6 seconds</strong> for <code>updateMarkupsControlPointsFromArray</code> to initialize the CurveNode with a zero array size (640, 3), and <strong>4.5 seconds</strong> for <code>UnsetNthControlPointPosition</code>to do Unset.<br>
During the test, the Slicer interface freezes for <strong>half a minute</strong> to initialize 3 curves, which is too long.</p>

---

## Post #12 by @Sunderlandkyl (2022-09-12 19:13 UTC)

<p>Interesting. updateMarkupsControlPointsFromArray is instantaneous on my computer (with a numpy array of size [640, 3]), although UnsetAllControlPoints takes several seconds.</p>
<p>You can save the templated landmarks to a json file after they are initialized and load that file into the curve node rather than using updateMarkupsControlPointsFromArray and UnsetNthControlPointPosition every time.</p>

---

## Post #13 by @sunshine (2022-09-12 19:17 UTC)

<p>That may not fit my case <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>
<p>“640” is not a fixed number, but the length of an ultrasound sequence, which is variable as we load different sequences. <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue_winking_eye.png?v=12" title=":stuck_out_tongue_winking_eye:" class="emoji" alt=":stuck_out_tongue_winking_eye:" loading="lazy" width="20" height="20"></p>

---

## Post #14 by @Sunderlandkyl (2022-09-12 19:19 UTC)

<p>Ok, you can try wrapping your calls using:</p>
<pre><code class="lang-python">with slicer.util.NodeModify(curveNode):
  # Node updates here
</code></pre>
<p>This will prevent node modification events while you are updating the node.</p>

---

## Post #15 by @sunshine (2022-09-12 19:32 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="14" data-topic="25142">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p><code>with slicer.util.NodeModify(curveNode):</code></p>
</blockquote>
</aside>
<p>Brilliant! You saved my day!<br>
Before this, I have to write dichotomy algorithm to calculate the index, then insert/remove/replace ControlPoint one by one. Now everything is simplified!</p>
<p>Thank you so much!</p>

---
