# Change spacing of segment using Python

**Topic ID**: 30499
**Date**: 2023-07-10
**URL**: https://discourse.slicer.org/t/change-spacing-of-segment-using-python/30499

---

## Post #1 by @ahmad_alminnawi (2023-07-10 14:07 UTC)

<p>Hi all,<br>
I would like to specify the spacing of a segment i am creating using python.</p>
<p>Manually, I can do so using “specify geometry” as seen here <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html" class="inline-onebox" rel="noopener nofollow ugc">Segmentations — 3D Slicer documentation</a><br>
under " Editing a segmentation imported from model "</p>
<p>Can anyone let me know how to do it in python? here is my code to create a segment with default (1x1x1) voxel size but I want to change it to 0.004x0.004x0.004</p>
<h1><a name="p-97425-create-segmentation-1" class="anchor" href="#p-97425-create-segmentation-1" aria-label="Heading link"></a>Create segmentation</h1>
<p>segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
segmentationNode.CreateDefaultDisplayNodes() # only needed for display<br>
segmentationNode.SetName(‘Segmentation’)</p>
<h1><a name="p-97425-import-the-model-into-the-segmentation-node-2" class="anchor" href="#p-97425-import-the-model-into-the-segmentation-node-2" aria-label="Heading link"></a>Import the model into the segmentation node</h1>
<p>slicer.modules.segmentations.logic().ImportModelToSegmentationNode(cylinderNode, segmentationNode)</p>

---

## Post #2 by @lassoan (2023-07-10 14:15 UTC)

<p>You can set the geometry (origin, spacing, axis directions, and extens) of the binary labelmap segmentation as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rasterize-a-model-and-save-it-to-a-series-of-image-files">this example in the script repository</a>.</p>

---

## Post #3 by @ahmad_alminnawi (2023-07-10 14:39 UTC)

<p>thank you for the reply but in that case I will have to allocate memory to each element which is huge in my case so it gives the error “Unable to allocate 242857881500 elements of size 1 bytes.”</p>
<p>is there a way to create the segmentation like I did before in the simple code and then modify its spacing?</p>

---

## Post #4 by @lassoan (2023-07-10 14:44 UTC)

<aside class="quote no-group" data-username="ahmad_alminnawi" data-post="3" data-topic="30499">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ahmad_alminnawi/48/66700_2.png" class="avatar"> ahmad_alminnawi:</div>
<blockquote>
<p>242857881500</p>
</blockquote>
</aside>
<p>This means that your reference image size would be 226GB. In general, I recommend to have 10x more RAM than your reference image size, which would mean that you would need 2260GB RAM and really, really fast processor to be able to do anything with this data.</p>
<p>These requirements are unrealistic to meet with today’s computing hardware, so I would recommend to reconsider your resolution needs or crop your data to a smaller region.</p>
<p>There might be also some misunderstanding about units. What is the distance unit of your model (meter, milllimeter, …)? What is the distance unit for 0.004?</p>

---

## Post #5 by @ahmad_alminnawi (2023-07-10 14:47 UTC)

<p>it it 4 mico meters (0.004 millimeters)<br>
on the GUI it is working fine which is why i am confused</p>

---

## Post #6 by @lassoan (2023-07-10 14:49 UTC)

<p>What are the bounds (min/mix x, y, z coordinates) of the model that you are importing?</p>

---

## Post #7 by @lassoan (2023-07-10 14:54 UTC)

<p>In the script example, an empty margin of 10mm is added around the model, which corresponds to about 5000 pixels along each axis. Probably you want to change it to something like <code>outputVolumeMarginMm   = 0.012</code>.</p>

---

## Post #8 by @ahmad_alminnawi (2023-07-10 14:56 UTC)

<p>I am importing an stl file of a cylinder that I created on 3dslicer<br>
I wrote a code where i would draw a 2 points (markups) and then a cylinder of radius 3mm and height 3mm would be created and exported as an stl file but I did not specify any bounds i just specified the points on the GUI to assign the center and direction along these points. this is the code</p>
<p>cylinder = pyvista.Cylinder(center=center_cylinder, direction=cylinder_direction,<br>
radius=cylinder_radius, height=cylinder_height)<br>
cylinderNode = slicer.modules.models.logic().AddModel(cylinder)</p>
<p>slicer.util.exportNode(cylinderNode, parentpath / ‘segmented_volumes’ / side / cylinder_outputfile)</p>

---

## Post #9 by @ahmad_alminnawi (2023-07-10 15:05 UTC)

<p>yes, reducing the volume margin worked like a charm! thanks</p>

---

## Post #10 by @ahmad_alminnawi (2023-07-11 14:20 UTC)

<p>One more thing,<br>
later i am trying to combine 2 segments together using the following code:</p>
<pre><code class="lang-auto">segmentName = 'pores'

addedSegmentID = seg.GetSegmentation().AddEmptySegment(segmentName)
segmentEditorNode.SetSelectedSegmentID(addedSegmentID)


# Logical operators
segmentEditorWidget.setActiveEffectByName("Logical operators")
effect = segmentEditorWidget.activeEffect()


operation = "UNION"
segment_to_add = "void"

effect.setParameter("Operation", operation) # change the operation here
effect.setParameter("ModifierSegmentID", segment_to_add)
effect.self().onApply()
</code></pre>
<p>i am also getting the same error we discussed earlier “Unable to allocate 1711230150 elements of size 1 bytes.”</p>
<p>Do I have to specify the “VolumeMargin” somewhere here as well?</p>

---

## Post #11 by @lassoan (2023-07-23 12:11 UTC)

<p><code>VolumeMargin</code> is just used in your own code, it is not an effect parameter.</p>
<p>I suspect that the two segments are far from each other, which would make the combined segmentation too large.</p>
<p>I would recommend to work with lower resolution (larger spacing) during development to make everything work faster and let you see the results even if you make some small mistakes.</p>

---
