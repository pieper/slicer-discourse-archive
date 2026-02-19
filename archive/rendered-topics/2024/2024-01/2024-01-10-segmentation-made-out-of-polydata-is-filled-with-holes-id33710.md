---
topic_id: 33710
title: "Segmentation Made Out Of Polydata Is Filled With Holes"
date: 2024-01-10
url: https://discourse.slicer.org/t/33710
---

# Segmentation made out of polydata is filled with holes

**Topic ID**: 33710
**Date**: 2024-01-10
**URL**: https://discourse.slicer.org/t/segmentation-made-out-of-polydata-is-filled-with-holes/33710

---

## Post #1 by @Gabriel_J (2024-01-10 04:27 UTC)

<p>Hello, my name is Gabriel,</p>
<p>I am in my final year of engineering school and I am relatively new to ITK, VTK, and Slicer. I have a question regarding the functioning of segmentation zones and how they are determined.</p>
<p>I am working on a project for the semi-automatic segmentation of the pulmonary arteries in the lungs. For this, we have a RANSAC algorithm that fits cylinders to the vessels in the lungs and creates a list of points along the vessels’ trajectories. We also retain the radius of the cylinder for each point in the list.</p>
<p>Next, we want to create seeds for the grow-from-seed process. Therefore, we create a new segmentation, and for each point, we create a sphere inside it, slightly smaller than the radius of the corresponding cylinder. These spheres are then added to a vtkAppendPolyData.</p>
<p>Afterward, we add our segment (vtkAppendPolyData.GetOutput()) to our segmentation using AddSegmentFromClosedSurfaceRepresentation.</p>
<pre data-code-wrap="python"><code class="lang-python">        for pointIdx in range(len(points)):
            sphere = vtk.vtkSphereSource()
            sphere.SetCenter(points[pointIdx])
            sphere.SetRadius(radius[pointIdx])
            sphere.Update()

            append.AddInputData(sphere.GetOutput())

        append.Update()

        self.segmentationNode.AddSegmentFromClosedSurfaceRepresentation(append.GetOutput(), segment_name, segment_color)
</code></pre>
<p>However, the result is disappointing:</p>
<p>It seems that the spheres are intersecting, creating peculiar holes when visualized in Slicer. I have tested visualizing by creating a mesh with Pyvista, and it works fine without these strange holes.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bebd174ae62fc2aab030c1e05d4a3dac06ed0981.png" alt="image" data-base62-sha1="rdlQo0BQVysePTyJ2dWSfrnOagV" width="480" height="270"></p>
<p>Do you know why this is happening and how I could fix it?<br>
I think, it may be because some sphere intersect with each other and the algorithm that interpret weither or not it is a closed surface do It by counting each times it encounter an edge, but I’m unsure.<br>
(Also, if you have any advice on how to better learn ITK, VTK, and Slicer, I would appreciate it.)</p>

---

## Post #2 by @cpinter (2024-01-10 10:31 UTC)

<p>It is very hard to see the exact issue, as the screenshot seems not to be enlargeable and this small I cannot see the details that could give away the source of the errors.</p>
<aside class="quote no-group" data-username="Gabriel_J" data-post="1" data-topic="33710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gabriel_j/48/68940_2.png" class="avatar"> Gabriel_J:</div>
<blockquote>
<p>may be because some sphere intersect with each other</p>
</blockquote>
</aside>
<p>This may be a problem, yes. I suggest that instead of appending the polydatas, add the sphere poly datas to a new segment each and then you can use Logical operators to add the sphere segments together. Something like this:</p>
<pre><code class="lang-auto">    logicalEffect = segmentEditorWidget.effectByName('Logical operators').self()
    logicalEffect.scriptedEffect.setParameter('Operation', 'UNION')
    for currentSegmentID in sphereSegmendIDs:
      logicalEffect.scriptedEffect.setParameter("ModifierSegmentID", currentSegmentID)
      logicalEffect.onApply()
</code></pre>
<p>Then delete the segments you don’t need.</p>
<p>Another issue may be that the segmentation’s binary labelmap image geometry is not ideal. What this means is that when you create a segmentation without a reference volume, it uses a fix RAS-aligned 1x1x1mm^3 geometry, which may be too low resolution. But first let’s see what working around the append filter does.</p>

---

## Post #3 by @pieper (2024-01-10 15:23 UTC)

<p>Another suggestion could. be to add the sphere segments as binary labelmaps instead of polydata.  Rasterizing intersecting polydata to a labelmap is a hard problem, but doing it natively as an image is easy.  You could script the paint effect with the sphere brush mode turned on or operate directly on the labelmap using something like <code>vtkImageEllipsoidSource</code>.</p>

---

## Post #4 by @Gabriel_J (2024-01-11 02:38 UTC)

<p>Hello,</p>
<p>Thank you for your very prompt responses! I tried what <a class="mention" href="/u/cpinter">@cpinter</a> suggested, and it worked very well!</p>
<p>Here is the result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/065793654aaf01afe989c851494560c2f19cd8ef.png" data-download-href="/uploads/short-url/U6uGU5O9m7oEEDwpDFMEC90uDR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/065793654aaf01afe989c851494560c2f19cd8ef_2_446x499.png" alt="image" data-base62-sha1="U6uGU5O9m7oEEDwpDFMEC90uDR" width="446" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/065793654aaf01afe989c851494560c2f19cd8ef_2_446x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/065793654aaf01afe989c851494560c2f19cd8ef.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/065793654aaf01afe989c851494560c2f19cd8ef.png 2x" data-dominant-color="9E9FD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">612×686 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see, there are no more holes in the seed area I defined, and by looking between slices I verified it was correct (and it is).</p>
<p>Thank you so much for helping me resolve my issue!</p>

---
