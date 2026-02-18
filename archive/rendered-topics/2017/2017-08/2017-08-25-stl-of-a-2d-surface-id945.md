# STL of a 2d surface

**Topic ID**: 945
**Date**: 2017-08-25
**URL**: https://discourse.slicer.org/t/stl-of-a-2d-surface/945

---

## Post #1 by @brhoom (2017-08-25 09:42 UTC)

<p>Dear all,<br>
I have a png image loaded to slicer and segmented. When I try generate the model using Model Maker I get this error:<br>
Model Maker standard error:<br>
The volume is not 3D.<br>
Image data extents: 0 511 0 361 0 0</p>
<p>When I use “Create Surface” in “Segment Editor”, The surface is generated and viewed in the 3D view but it does not appear  in the “Subject hierarchy” or in “Save”.<br>
Any suggestion?<br>
best regards!<br>
Ibraheem</p>

---

## Post #2 by @lassoan (2017-08-25 11:29 UTC)

<p>I’ve just tested and it works well in a recent nightly version of Slicer. To export the segment to a model, go to Data module (Subject hierarchy section), right-click on the segment, and choose “Export visible segments to models”</p>

---

## Post #3 by @brhoom (2017-08-25 12:01 UTC)

<p>This works, thanks Andras. I suggest to make the model generation automatic.</p>

---

## Post #4 by @lassoan (2017-08-25 12:48 UTC)

<p>Generation of 3D closed surface representation of segments is already automatic.<br>
Can you describe why you need to automate exporting to model nodes?</p>

---

## Post #5 by @brhoom (2017-08-28 15:42 UTC)

<p>Because it is expected since it is already implemented for 3D. I wanted to test an external tool i.e statismo, the example required a poly-data as input.</p>

---

## Post #6 by @cpinter (2017-08-28 15:53 UTC)

<p>Your answer is extremely brief, and calls for a lot of extrapolation and assumptions. You say you use an external tool. I can see two ways for doing that:</p>
<ol>
<li>You need to save the STL to disk, and load it in your tool. In that case updating the STL on disk real-time as it changes seems like a dangerous operation. It should be done on-demand, which you can do easily</li>
<li>You built the tool and use it as an extension, from python for example. You say it needs vtkPolyData. You can get the poly data directly from the segmentation node, no need to go through the model node loop:<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_representation_of_a_segment">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_representation_of_a_segment</a>
</li>
</ol>

---

## Post #7 by @brhoom (2017-08-28 15:58 UTC)

<p>oh Andras post already solved the issue. I just replied to his question <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=5" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"> but thanks for explaining.</p>

---
