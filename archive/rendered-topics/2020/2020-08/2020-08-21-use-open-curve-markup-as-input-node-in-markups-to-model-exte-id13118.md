# Use Open Curve Markup as input node in "Markups To Model" extension

**Topic ID**: 13118
**Date**: 2020-08-21
**URL**: https://discourse.slicer.org/t/use-open-curve-markup-as-input-node-in-markups-to-model-extension/13118

---

## Post #1 by @mangotee (2020-08-21 09:35 UTC)

<p>Hi,</p>
<p>I was just working with the “Markups To Model” extension for the first time and I saw that it only accepts markup fiducial lists as an input. Is there a reason why it does not take markup curves (open or closed) as input? I know how to convert a markups open curve into a markup fiducial list programmatically (via arrayFromMarkupsCurvePoints()), but the name “Markups to Model” implies that this is already supported anyway, directly from the UI.</p>
<p>A bit of context why I’m doing this: I’m currently trying to find an easy way to accurately segment bone fractures, specifically skull fractures. The way I do it right now works, but is a bit cumbersome, with roughly the following steps:</p>
<ol>
<li>segment the skull via thresholding</li>
<li>erode that by 1mm and export that as a model</li>
<li>use “Probe Volume With Model” to get a textured mesh with ImageScalars (the fracture is nicely visible in these scalars)</li>
<li>place an open-curve-markup with a few control points on the mesh surface</li>
<li>constrain the curve path to lie on the skull surface model, and the path should follow a shortest-distance path on the model with an “Additive” cost function that is “distance + 10*ImageScalars” - Now, the open curve follows exactly the HU intensity dip along the fracture line.</li>
<li>Here is where the above part is a bit of an inconvenience… I wanna import this path into the segmentation node… to do this I have to i) resample the path with a large number of fiducials, ii) convert the curve to a fiducials list, iii) use “Markups to Model” to convert this into a model, and iv) import the model into the segmentation.</li>
</ol>
<p>Especially point 6 would get a bit simpler, if it was possible to directly convert the open curve into a model (without resampling and/or converting to a fiducial list).</p>
<p>Maybe this way to segment a fracture is way too complex. If anyone has an idea how to do it better, I’d be greatful for suggestions. I can also open a new topic for this… This topic is mainly for the “Markups to Model” feature request to accept “Open Curve Markups” as well.</p>

---

## Post #2 by @lassoan (2020-08-21 17:18 UTC)

<p>Thanks you for the information, it is good to know that this processing flow works well.</p>
<aside class="quote no-group" data-username="mangotee" data-post="1" data-topic="13118">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>resample the path with a large number of fiducials</p>
</blockquote>
</aside>
<p>You can resample a curve using Markups module (resample section).</p>
<aside class="quote no-group" data-username="mangotee" data-post="1" data-topic="13118">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>convert the curve to a fiducials list, iii) use “Markups to Model” to convert this into a model, and iv) import the model into the segmentation</p>
</blockquote>
</aside>
<p>I’m not sure what these steps are needed for. You can clip a surface along enclosing curve and planes using <em>Dynamic modeler</em> module:</p>
<aside class="quote quote-modified" data-post="1" data-topic="11759">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-dynamic-modeler-parametric-surface-editing-for-biomedical-applications/11759">New module: Dynamic Modeler - parametric surface editing for biomedical applications</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We have added a new module called “Dynamic Modeler” to the latest Slicer preview releases (4.11). This module provides an extensible framework for automatic processing of mesh nodes by executing “Tools” on the input to generate output mesh. 

  <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" target="_blank" class="video-thumbnail" rel="noopener">
    [3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications]
  </a>


Output of a tool can be used as input in another tool, which allows specification of complex editing operations. This is similar to “parametric editing” in eng…
  </blockquote>
</aside>


---

## Post #3 by @mangotee (2020-08-24 14:05 UTC)

<p>Thanks Andras… the reason I need to do steps 6.i/ii/iii are because I want to convert the open curve itself into a model (a tube of certain diameter), then import that tube into the segment editor. I don’t see a quicker way how to accomplish that right now.<br>
The Dynamic Modeler module can clip a surface along an open curve - but it cannot convert the curve itself into a tube model, right?</p>

---

## Post #4 by @lassoan (2020-08-24 14:15 UTC)

<p>You can draw tubes directly in Segment Editor using “Draw tube” effect (provided by SegmentEditorExtraEffects extension). Right now you cannot enable constraining of the curve in this effect (or selection of a curve node), but this would not be hard to add. The effect is just <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorDrawTube/SegmentEditorDrawTubeLib/SegmentEditorEffect.py">a short Python script</a> that you can easily modify, so it would be great if you could give it a go and make the changes that you need (e.g., add an input curve node selector). If you find that these modifications are useful then we could merge those back to the official version.</p>

---

## Post #5 by @agv (2020-08-28 10:59 UTC)

<p>Hello mangotee,</p>
<p>I found this topic since I am having the same issue for a different application (for which I’ve just posted another topic: <a href="https://discourse.slicer.org/t/create-equidistant-curves-on-a-given-surface/13212" class="inline-onebox">Create equidistant curves on a given surface</a>).</p>
<p>For what I’ve read, it seems that you managed to convert an “Open Curve Markup” into a “Markup Fiducial List”, in order to use it in “Markups to Model”. Could you please share the code with me or give me some instructions about it? I would really appreciate it.</p>
<p>Thank you very much in advance,</p>
<p>Alessandro</p>

---

## Post #6 by @mangotee (2020-08-31 09:55 UTC)

<p>Hi agv,<br>
sure, no problem. Getting an array from the curve is easy, Slicer provides a function for this. Creating a fiducial markups node from this array needs to be coded. There may be a Slicer function for this too, but I’m not aware of any. I modified a function I created for this to fit your use case. Here’s the code, obviously you can modify the function to your needs (and obviously it’s not very clean, e.g. no asserts or anything) - hope it helps:</p>
<pre><code># Utility function to create a fiducial list from a Nx3 numpy array
def fiducialListFromArray(name_fidnode, arr, fidsPrefix=''):
    # Check if a fiducial markups node with the name "name_fidnode" already exists, if not, create it and add it to the scene
    try:
        n_fid = slicer.util.getNode(name_fidnode)
    except slicer.util.MRMLNodeNotFoundException:
        n_fid = slicer.vtkMRMLMarkupsFiducialNode()
        n_fid.SetName(name_fidnode)
        slicer.mrmlScene.AddNode(n_fid)
    nrfids = arr.shape[0]
    # if no fiducial names are given, 
    if fidsPrefix=='':
        sep = ''
    else:
        sep = '-'
    listFidNames = ['%s%s%d'%(fidsPrefix,sep,i+1) for i in range(nrfids)]
    for i in range(nrfids):
        n_fid.AddFiducial(arr[i,0], arr[i,1], arr[i,2], listFidNames[i])
    return n_fid

# n_curve is the node to the open curve markup
arr = arrayFromMarkupsControlPoints(n_curve)
# A node of name 'FiducialsFromCurve' is created if it doesn't exist already
# if it exists, the fiducials in arr are simply appended to the existing list
n_fid = fiducialListFromArray('FiducialsFromCurve', arr, fidsPrefix='F')</code></pre>

---

## Post #7 by @agv (2020-08-31 15:09 UTC)

<p>Hello again mangotee,</p>
<p>thank you very much for your explanation and the attached code! I tested it and it worked perfectly for what I was trying to do <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #8 by @lassoan (2020-08-31 15:21 UTC)

<p>The method that converts numpy array to markups control points is called <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateMarkupsControlPointsFromArray"><code>slicer.util.updateMarkupsControlPointsFromArray</code></a>, so you should be able to convert <code>curveNode</code> to <code>fiducialNode</code> with something like this:</p>
<pre><code class="lang-python">fiducialNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
updateMarkupsControlPointsFromArray(fiducial Node, arrayFromMarkupsControlPoints(curveNode))
</code></pre>

---

## Post #9 by @agv (2020-09-01 09:24 UTC)

<p>It works well and saves some lines of code, thank you Andras!</p>

---
