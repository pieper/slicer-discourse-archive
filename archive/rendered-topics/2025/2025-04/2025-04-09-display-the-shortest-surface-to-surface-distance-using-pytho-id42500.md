---
topic_id: 42500
title: "Display The Shortest Surface To Surface Distance Using Pytho"
date: 2025-04-09
url: https://discourse.slicer.org/t/42500
---

# Display the shortest surface to surface distance using python

**Topic ID**: 42500
**Date**: 2025-04-09
**URL**: https://discourse.slicer.org/t/display-the-shortest-surface-to-surface-distance-using-python/42500

---

## Post #1 by @Matteboo (2025-04-09 12:14 UTC)

<p>Hello,</p>
<p>I have two segmentations. I want to measure and display the shortest distance between the surfaces (just like the picture below)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b78d91fd0c5a6b92421d68d77a6840c65ea4d9c1.png" data-download-href="/uploads/short-url/qbMGMkfXqntXo42IugmBq1CuW6l.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b78d91fd0c5a6b92421d68d77a6840c65ea4d9c1.png" alt="image" data-base62-sha1="qbMGMkfXqntXo42IugmBq1CuW6l" width="607" height="313"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">607×313 39.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can measure the distance between the two surfaces using <code>slicer.modules.modeltomodeldistance</code> but I can’t get the two points that achieve this smallest distance.</p>
<p>Does anyone knows how to get the points achieving the smallest distance given by <code>slicer.modules.modeltomodeldistance</code></p>

---

## Post #2 by @chir.set (2025-04-09 19:42 UTC)

<p>I just discovered this module and AFAIU, the following <em>should</em> solve your problem, at least if your models do not intersect.</p>
<p>If you use <code>absolute_closest_point</code>, you can get one point coordinate from the <code>Absolute</code> array of the output model (the one(s) with the minimum absolute distance). With this coordinate, the polydata of the <code>Target Model</code> can give the second coordinate using <code>FindPoint()</code> and <code>GetPoint()</code>.</p>

---

## Post #3 by @Matteboo (2025-04-10 13:24 UTC)

<p>I managed to get this using the following code</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6ccf7bc0048114d5c9beee13f417ec1ad3055303.png" data-download-href="/uploads/short-url/fwA64tRnoQkj3xMWQi9p048s0uv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6ccf7bc0048114d5c9beee13f417ec1ad3055303.png" alt="image" data-base62-sha1="fwA64tRnoQkj3xMWQi9p048s0uv" width="642" height="318"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">642×318 41.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">    # Step 2: Compute distance from inside to outside
    distance_model = findModelToModelDistance(outside_model, inside_model)  # Distance from outside to inside
    VTKFieldData = distance_model.GetMesh().GetAttributesAsFieldData(0)
    created_nodes.append(distance_model)

    # Step 3: Extract signed distances and find min
    signedVals = []
    for i in range(VTKFieldData.GetArray("Signed").GetNumberOfTuples()):
        val = VTKFieldData.GetArray("Signed").GetValue(i)
        signedVals.append(-val)  # Negate to get correct direction

    min_index = np.argmin(signedVals)
    min_distance = signedVals[min_index]

    # Step 4: Get closest point on inside
    closest_inside_point = inside_model.GetPolyData().GetPoint(min_index)

    # Step 5: Get corresponding closest point on outside
    locator = vtk.vtkPointLocator()
    locator.SetDataSet(outside_model.GetPolyData())
    locator.BuildLocator()
    closest_outside_point_id = locator.FindClosestPoint(closest_inside_point)
    closest_outside_point = outside_model.GetPolyData().GetPoint(closest_outside_point_id)

def findModelToModelDistance(modelNode1,modelNode2):
    vtkOutput = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")
    vtkOutput.SetName("m2md")

    parameters = {}
    parameters["vtkFile1"] = modelNode2
    parameters["vtkFile2"] = modelNode1
    parameters['distanceType'] = "signed_closest_point"
    parameters["vtkOutput"] = vtkOutput

    cliNode = slicer.cli.runSync(slicer.modules.modeltomodeldistance, None, parameters)
    return vtkOutput
</code></pre>

---
