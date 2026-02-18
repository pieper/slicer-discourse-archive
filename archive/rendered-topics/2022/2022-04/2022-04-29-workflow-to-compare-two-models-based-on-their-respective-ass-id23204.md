# Workflow to compare two models based on their respective associated scalars

**Topic ID**: 23204
**Date**: 2022-04-29
**URL**: https://discourse.slicer.org/t/workflow-to-compare-two-models-based-on-their-respective-associated-scalars/23204

---

## Post #1 by @tristan421 (2022-04-29 22:38 UTC)

<p>Hi, fantastic work here. Slicer is great.<br>
I have advanced on my own but could do with a kind and helping hand for the last step.</p>
<p>Very quickly :</p>
<p>I have two models. The fist one has been created from a segmented volume and “painted” by probevolumefrommodel. The other model is a polydata model imported from an electro-anatomical CARTO® map. <strong>I need to compare the values associated with those two models on a “point by point” basis</strong>, to draw some correlation.</p>
<p>What I did :</p>
<ol>
<li>
<p>I  created 5000 fiducials points on the first model,</p>
</li>
<li>
<p>I registered the model to the other one by means of non rigid transformation, and  applied this transformation to the fiducials.</p>
</li>
<li>
<p>I projected the 5000  transformed points to the second model using nearest distance projection. I now have 2 sets of related fiducials, one on each model surface, that i would like to compare in term of the underlying scalar data.</p>
</li>
</ol>
<p>How should I proceed in order to sample each model at each and every fiducial point ?</p>
<p>Alternativly I could use another approach if more practical.</p>
<p>Regards, and again many thanks for this gem of a software.</p>

---

## Post #2 by @pieper (2022-04-30 17:15 UTC)

<p>Hi - great that you are finding Slicer useful <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>A couple thoughts - if you are trying to find the values you painted onto the module with ProbeVolumeFromModel, you could just look up the points in the volume, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates">like this</a>.</p>
<p>Or if you are going the other way and want to sample on the carto volume, you can use a <a href="https://vtk.org/doc/nightly/html/classvtkPointLocator.html">locator</a> to get the point indices and look up the scalar data.</p>

---

## Post #3 by @tristan421 (2022-05-07 22:24 UTC)

<p>Thank you, it works like a charm. I did something like that to iterate on the fiducials. Perfect</p>
<blockquote>
<p>Blockquote</p>
</blockquote>
<p>for i in range(numControlPoints):</p>
<pre><code>ras = vtk.vtkVector3d(0,0,0)
pointListNode.GetNthControlPointPosition(i,ras)
closestPointId = pointsLocator.FindClosestPoint(ras)
ras = modelNode.GetPolyData().GetPoint(closestPointId)
closestPointValue = modelPointValues.GetTuple(closestPointId)
measurements.append(str(closestPointValue[0]))
</code></pre>
<p>slicer.app.clipboard().setText(“\n”.join(measurements))</p>

---
