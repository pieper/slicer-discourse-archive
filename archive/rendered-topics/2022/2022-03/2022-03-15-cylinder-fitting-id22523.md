---
topic_id: 22523
title: "Cylinder Fitting"
date: 2022-03-15
url: https://discourse.slicer.org/t/22523
---

# Cylinder fitting

**Topic ID**: 22523
**Date**: 2022-03-15
**URL**: https://discourse.slicer.org/t/cylinder-fitting/22523

---

## Post #1 by @alyssan (2022-03-15 17:18 UTC)

<p>I have a segmentation that has a cylindical shape but is uneven and has different radii throughout. I would like to calculate the radius at different intervals to find the largest and smallest radius. Then fit a cylinder to that segmentation that has that radius and the correct angle. How could I achieve this? Thanks</p>

---

## Post #2 by @lassoan (2022-03-16 20:06 UTC)

<p>You can use Segment Statistics module to get:</p>
<ul>
<li>center of gravity: on point along the cylinder axis</li>
<li>principal axis: direction of the cylinder axis</li>
<li>volume: you can use this value along with the length of the cylinder (from oriented bounding box size) to get the average radius of the cylinder</li>
</ul>
<p>Alternatively, you can use VMTK extension to get all the cylinder axis points and radius values along the axis.</p>
<p>If you know the expected cylinder length and radius then you can also use Model Registration or Segment Registration modules (provided by extensions).</p>

---

## Post #3 by @alyssan (2022-03-18 15:59 UTC)

<p>Great, thank you for your help. I am still struggling with how to find the length can you explain this a bit more?</p>
<p>Also, I am still not clear on how to generate a cylinder that fits my segmentation. Can I do this using the General Registration module?</p>

---

## Post #4 by @lassoan (2022-03-19 00:30 UTC)

<p>Length is provided by the orientation d bounding box size.</p>
<p>You can use a model node to display the cylinder. Set the output of a <a href="https://vtk.org/doc/nightly/html/classvtkCylinderSource.html">vtkCylinderSource</a> as input polydata of the model. See many of examples in the script repository: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---

## Post #5 by @alyssan (2022-03-21 16:29 UTC)

<p>I am having trouble using the python code to generate the bounding box. Its is giving me an error AttributeError: ‘MRMLCorePython.vtkMRMLLabelMapVolumeDisplayNode’ object has no attribute ‘GetVisibleSegmentIDs’</p>
<p>Is there a way to fix this or generate bounding box manually?</p>

---

## Post #6 by @alyssan (2022-03-21 16:30 UTC)

<p>The error is given for the code, segStatLogic.computeStatistics()</p>

---

## Post #7 by @alyssan (2022-03-21 16:36 UTC)

<p>Under what header in the script repository would an example of generating a cylinder be? I cant locate it</p>

---

## Post #8 by @lassoan (2022-03-21 18:12 UTC)

<aside class="quote no-group" data-username="alyssan" data-post="5" data-topic="22523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3da27b/48.png" class="avatar"> alyssan:</div>
<blockquote>
<p>I am having trouble using the python code to generate the bounding box. Its is giving me an error AttributeError: ‘MRMLCorePython.vtkMRMLLabelMapVolumeDisplayNode’ object has no attribute ‘GetVisibleSegmentIDs’</p>
</blockquote>
</aside>
<p>Segment Statistics module requires segmentation input. You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file">load a binary volume as segmentation; or load it as labelmap and then convert it to segmentation</a>.</p>
<aside class="quote no-group" data-username="alyssan" data-post="7" data-topic="22523" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3da27b/48.png" class="avatar"> alyssan:</div>
<blockquote>
<p>Under what header in the script repository would an example of generating a cylinder be? I cant locate it</p>
</blockquote>
</aside>
<p>There are a number of relevant examples in the Models section. For example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-simple-surface-mesh-as-a-model-node">this one</a>.</p>

---

## Post #9 by @alyssan (2022-03-23 15:20 UTC)

<p>Thank you for your help it is much appreciated.</p>
<p>I tried out the code:<br>
implant = vtk.vtkCylinderSource()<br>
implant.SetHeight(100)<br>
implant.SetRadius(8)<br>
implant.SetCenter(-78.778,102.725,-181.217)<br>
implant.SetResolution(100)</p>
<p>implantNode = slicer.modules.models.logic().AddModel(implant.GetOutputPort())<br>
implantNode.GetDisplayNode().SetColor(0,0,1)<br>
implantNode.GetDisplayNode().SetOpacity(1)</p>
<p>I used some of the values I obtained from segment statistics. However, I am trying to automate this process. Is there a way that I can use variables to input for the radius and height instead of values?</p>

---

## Post #10 by @alyssan (2022-03-23 15:21 UTC)

<p>I am also having trouble with some of the values. Is their a variable that contains the length? And how do I find the angle of rotation so that the cylinder is in the same direction?</p>

---

## Post #11 by @alyssan (2022-03-23 15:25 UTC)

<p>The segment statistics gives me the ferret diameter which is not the correct diameter of my segmentation.</p>
<p>I tried using VMTK to extract centerline however it only gives me one value for the radius. How do I get multiple values along the length of the segmentation as displayed in the example picture? Thank you!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bde17d61287c4527c6474ed69bdd8010f8b7850.png" alt="pic1" data-base62-sha1="foeV8KLfhbntZLujO9a7C2Wothu" width="355" height="180"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329574b453aa14ff988ebc85a58ce88aaa7887ca.png" alt="pic2" data-base62-sha1="7du52mP4McJLJGdBYWjvgkvoWrE" width="509" height="478"></p>

---

## Post #12 by @chir.set (2022-03-23 18:00 UTC)

<aside class="quote no-group" data-username="alyssan" data-post="11" data-topic="22523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3da27b/48.png" class="avatar"> alyssan:</div>
<blockquote>
<p>VMTK to extract centerline however it only gives me one value for the radius. How do I get multiple values</p>
</blockquote>
</aside>
<p>‘<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CrossSectionAnalysis.md" rel="noopener nofollow ugc">Cross-section analysis</a>’ module should fulfil this part of your needs. You can get diameters at each centerline point in a table, and plot them in a graph.</p>

---

## Post #13 by @alyssan (2022-03-23 20:19 UTC)

<p>I am not sure what I am doing wrong but I can not figure out how to get my segmentation(1st pic) to look like the 2nd with all the centerline points along the line. I tried using cross section analysis but cannot get it to work.</p>

---

## Post #14 by @alyssan (2022-03-23 20:24 UTC)

<p>Is their a step i need to do between creating the centerline and using the cross section analysis tool?</p>

---

## Post #15 by @chir.set (2022-03-23 20:52 UTC)

<p>You are showing a centerline model in the first image. 'Extract centerline allows to generate a centerline curve too (second image). 'Cross-section analysis ’ works with both centerline models and curves. Prefer the curve variant as the centerline model is, though not really so, but nearly legacy.</p>

---
