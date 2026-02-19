---
topic_id: 32593
title: "Projecting Points To The Positive External Surface"
date: 2023-11-03
url: https://discourse.slicer.org/t/32593
---

# Projecting points to the positive external surface

**Topic ID**: 32593
**Date**: 2023-11-03
**URL**: https://discourse.slicer.org/t/projecting-points-to-the-positive-external-surface/32593

---

## Post #1 by @chz31 (2023-11-03 23:35 UTC)

<p>Dear all,</p>
<p>I am trying to register and deform a surgical plate (roughly pre-registered using a few discrete landmarks) to adapt to the surface of the orbit. The plate has a thickness. You can see that some parts of the pre-registered unbended plate is “sinking” into the orbit.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afefe00c7938968d9c3d9f4c9726d6a06101b59f.jpeg" data-download-href="/uploads/short-url/p6pue9GvB9Fio8K3XHtpnzBdHd5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afefe00c7938968d9c3d9f4c9726d6a06101b59f_2_273x250.jpeg" alt="image" data-base62-sha1="p6pue9GvB9Fio8K3XHtpnzBdHd5" width="273" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afefe00c7938968d9c3d9f4c9726d6a06101b59f_2_273x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afefe00c7938968d9c3d9f4c9726d6a06101b59f_2_409x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afefe00c7938968d9c3d9f4c9726d6a06101b59f_2_546x500.jpeg 2x" data-dominant-color="877E59"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1117×1022 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The approach I am testing to adapt the plate to the orbital surface is to 1) sample same points at both the upper and undersurface of the plate, and 2) project the points at the upper surface of the plate to the orbit, and 3) run a registration between the points at the under plate surface to the points projected to the orbit, followed by a thin-plate spline (TPS) transformation (deform the plate at the same type).Though not perfect, it did adapt most of the plate to the surface of the orbit.</p>
<p>Points at the upper surface of the plate. Same points were also sampled at the under surface.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f550fe527a9896e09926056a1bd438a694bc5ccf.jpeg" data-download-href="/uploads/short-url/z0avur2xOXOSU7M7NT2Ze338Jzh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f550fe527a9896e09926056a1bd438a694bc5ccf_2_309x250.jpeg" alt="image" data-base62-sha1="z0avur2xOXOSU7M7NT2Ze338Jzh" width="309" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f550fe527a9896e09926056a1bd438a694bc5ccf_2_309x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f550fe527a9896e09926056a1bd438a694bc5ccf_2_463x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f550fe527a9896e09926056a1bd438a694bc5ccf_2_618x500.jpeg 2x" data-dominant-color="7E8158"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1265×1023 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Points projected to the orbital surface from points plated at the upper surface of the plate.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58d7521c5a56a75689a57d7706dd71d25358a19d.jpeg" data-download-href="/uploads/short-url/cFVl4PYKxs5Ul8ETrYPe6rTnx13.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58d7521c5a56a75689a57d7706dd71d25358a19d_2_288x250.jpeg" alt="image" data-base62-sha1="cFVl4PYKxs5Ul8ETrYPe6rTnx13" width="288" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58d7521c5a56a75689a57d7706dd71d25358a19d_2_288x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58d7521c5a56a75689a57d7706dd71d25358a19d_2_432x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58d7521c5a56a75689a57d7706dd71d25358a19d_2_576x500.jpeg 2x" data-dominant-color="797E3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1484×1287 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Deformed plate adapt to the orbital surface based on register the points at the undersurface of the plate to the points projected to the orbital surface followed by a thin-plate spline transformation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f0513c75cc1c9c58af9a45e6fe1e7eebb2451e3.jpeg" data-download-href="/uploads/short-url/i7Fw2iLGTQSQ7YaBTSJI8BtvIsP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f0513c75cc1c9c58af9a45e6fe1e7eebb2451e3_2_266x250.jpeg" alt="image" data-base62-sha1="i7Fw2iLGTQSQ7YaBTSJI8BtvIsP" width="266" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f0513c75cc1c9c58af9a45e6fe1e7eebb2451e3_2_266x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f0513c75cc1c9c58af9a45e6fe1e7eebb2451e3_2_399x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f0513c75cc1c9c58af9a45e6fe1e7eebb2451e3_2_532x500.jpeg 2x" data-dominant-color="837A57"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1089×1022 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, a small part of the plate was still under the surface. This is because a few points (31, 32, 44) at that region were projected to another side of the orbit due to the presence of a convex area at the medial orbital wall. Thus, a portion of the plate “sank” too deep under that convex area and got too close to under side of the orbital surface.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd5b54443f771ddf3befafcb3e499772380cd368.jpeg" data-download-href="/uploads/short-url/vAdbX9117TCv1aVmXpSZNs69A6c.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd5b54443f771ddf3befafcb3e499772380cd368_2_272x250.jpeg" alt="image" data-base62-sha1="vAdbX9117TCv1aVmXpSZNs69A6c" width="272" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd5b54443f771ddf3befafcb3e499772380cd368_2_272x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd5b54443f771ddf3befafcb3e499772380cd368_2_408x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd5b54443f771ddf3befafcb3e499772380cd368_2_544x500.jpeg 2x" data-dominant-color="856336"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">625×573 82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77c375577530e6cc03c672653acfb759badd09fa.jpeg" data-download-href="/uploads/short-url/h5tAmTnltv1EQMxdLDyvTCEVvdw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77c375577530e6cc03c672653acfb759badd09fa_2_270x249.jpeg" alt="image" data-base62-sha1="h5tAmTnltv1EQMxdLDyvTCEVvdw" width="270" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77c375577530e6cc03c672653acfb759badd09fa_2_270x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77c375577530e6cc03c672653acfb759badd09fa_2_405x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77c375577530e6cc03c672653acfb759badd09fa_2_540x498.jpeg 2x" data-dominant-color="87893C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">610×564 90.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab738b1a7bbb6f8f52c20cad2fae27052d596442.png" data-download-href="/uploads/short-url/osJch2wdySsa89GkeiY5TTrckGm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab738b1a7bbb6f8f52c20cad2fae27052d596442_2_264x250.png" alt="image" data-base62-sha1="osJch2wdySsa89GkeiY5TTrckGm" width="264" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab738b1a7bbb6f8f52c20cad2fae27052d596442_2_264x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab738b1a7bbb6f8f52c20cad2fae27052d596442_2_396x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab738b1a7bbb6f8f52c20cad2fae27052d596442_2_528x500.png 2x" data-dominant-color="B49C3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">640×604 90.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any way to project points into a designated upper surface of the orbit?</p>
<p>The way I do the projection is by using the the <code>runPointProjection()</code> function based on the <code>projectPointsPolydata</code> in the <code>ALPACA</code> module of the <code>SlicerMorph</code> extension, which is about casting a ray along the normal of each point and find the intersection with the surface of another model (<a href="https://github.com/SlicerMorph/SlicerMorph/blob/8c1419d0a6da86f8009980f8925a238cbd2fa88d/ALPACA/ALPACA.py#L2977C4-L3073C1" rel="noopener nofollow ugc">https://github.com/SlicerMorph/SlicerMorph/blob/8c1419d0a6da86f8009980f8925a238cbd2fa88d/ALPACA/ALPACA.py#L2977C4-L3073C1</a>).</p>
<p>The script I did was:</p>
<pre><code class="lang-auto">import ALPACA
logic = ALPACA.ALPACALogic()
plate_model_node = slicer.util.getNode("preregistered_plate")
lm_plate_upper_node = slicer.util.getNode("lm_plate_upper_surface")
orbit_model_node = slicer.util.getNode("orbit")

projectionFactor = 0.001 #I've been playing with the parameter.
lm_projected_to_orbit = logic.runPointProjection(plate_model_node, orbit_model_node, lm_plate_upper_node , projectionFactor) 
projected_plate_below_to_orbit_lm.SetName("lm_projected_to_orbit")
</code></pre>
<p>Orbit and plate and landmark files can be accessed at: <a href="https://drive.google.com/file/d/1bwM1fcNCERFoZEvuz4DNXbNs_te8FYOR/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">orbit_and_plate.zip - Google Drive</a></p>
<p>Thank you!</p>
<p>Chi</p>

---

## Post #2 by @pieper (2023-11-05 15:15 UTC)

<p>Can you just extend the segmentation at the back of the orbit so that only the front surface is close to the plate?</p>

---

## Post #3 by @chz31 (2023-11-06 01:22 UTC)

<p>Thanks! This sounds like a good idea, at least it would make it much more convenient for data analysis. I’ll give it a try soon. I also need to check with the surgeon if he wants the orbital wall particularly well segmented.</p>
<p>What I did to “lift” the plate out of the orbit was by registering the landmarks at the under surface to those at the upper surface and then transform the undeformed plate accordingly. Iterate the process for a few time would “lift” the plate up.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cd57cee3795eed2a1b454f2ca50cf62b92a6a60.jpeg" data-download-href="/uploads/short-url/hOkBlbXevgnH6TER5S8dm1zLU3K.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cd57cee3795eed2a1b454f2ca50cf62b92a6a60_2_330x250.jpeg" alt="image" data-base62-sha1="hOkBlbXevgnH6TER5S8dm1zLU3K" width="330" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cd57cee3795eed2a1b454f2ca50cf62b92a6a60_2_330x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cd57cee3795eed2a1b454f2ca50cf62b92a6a60_2_495x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7cd57cee3795eed2a1b454f2ca50cf62b92a6a60_2_660x500.jpeg 2x" data-dominant-color="8A884C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1458×1104 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I was then able to project all the points from the plate to the upper orbital surface and run a TPS deformation to adapt the plane to the surface of the orbit (visually satisfied at least).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a212ee9c99077e6669a1f61eae366b546aff5cb.jpeg" data-download-href="/uploads/short-url/1rBRUmcJHYJbmZP0w7UALAYDDmj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a212ee9c99077e6669a1f61eae366b546aff5cb_2_282x249.jpeg" alt="image" data-base62-sha1="1rBRUmcJHYJbmZP0w7UALAYDDmj" width="282" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a212ee9c99077e6669a1f61eae366b546aff5cb_2_282x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a212ee9c99077e6669a1f61eae366b546aff5cb_2_423x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a212ee9c99077e6669a1f61eae366b546aff5cb_2_564x498.jpeg 2x" data-dominant-color="616F4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1359×1201 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For repeatability, I am thinking about using something similar to Model-to-Model distance to calculate a scalar value at the plate (e.g., <a href="https://discourse.slicer.org/t/python-code-model-to-model-distance/15593/2" class="inline-onebox">Python code model-to-model distance - #2 by smrolfe</a>). If the scalar values become all negative, it means the plate has “lifted” to just a position just above the orbit. If this sounds reasonable, is there a way to calculate signed distance between particular landmarks and a surface?</p>

---

## Post #4 by @mau_igna_06 (2023-11-06 18:25 UTC)

<aside class="quote no-group" data-username="chz31" data-post="3" data-topic="32593">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chz31/48/77363_2.png" class="avatar"> chz31:</div>
<blockquote>
<p>is there a way to calculate signed distance between particular landmarks and a surface?</p>
</blockquote>
</aside>
<p>The example below should allow you to create a vertex-only polydata you could embed in a vtkMRMLModelNode with <a href="https://apidocs.slicer.org/master/classvtkMRMLModelNode.html#a195cf29c5e86b8251fc3fffcc7131827" rel="noopener nofollow ugc">SetAndObservePolyData</a> and then use Model-to-Model distance.</p>
<pre><code class="lang-auto">def __init__(self, pointlist=[]):
        points = vtk.vtkPoints()
        cellArr = vtk.vtkCellArray()
        Colors = vtk.vtkUnsignedCharArray()
        Colors.SetNumberOfComponents(3)
        Colors.SetName("Colors")
        
        n=0
        for p in pointlist:
            vert = vtk.vtkVertex()
            points.InsertNextPoint(p.x, p.y, p.z)
            vert.GetPointIds().SetId(0,n)
            cellArr.InsertNextCell( vert )
            col = clColor(p.cc())
            Colors.InsertNextTuple3( float(255)*col[0], float(255)*col[1], float(255)*col[2] )
            n=n+1
            
        polydata= vtk.vtkPolyData()
        polydata.SetPoints(points)
        polydata.SetVerts( cellArr )
        polydata.GetPointData().SetScalars(Colors)
</code></pre>
<p>But if you need spheres instead of vertices (because Model-to-Model module needs surface normals) you could use:</p>
<ul>
<li><a href="https://vtk.org/doc/nightly/html/classvtkSphereSource.html" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkSphereSource Class Reference</a> + <a href="https://vtk.org/doc/nightly/html/classvtkGlyph3D.html#details" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkGlyph3D Class Reference</a></li>
<li>or, <a href="https://vtk.org/doc/nightly/html/classvtkSphereSource.html" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkSphereSource Class Reference</a> + <a href="https://vtk.org/doc/nightly/html/classvtkAppendPolyData.html" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkAppendPolyData Class Reference</a></li>
</ul>
<p>Hope it helps</p>

---

## Post #5 by @chz31 (2023-11-08 14:42 UTC)

<p>This looks great. Thank you very much!</p>

---

## Post #6 by @lassoan (2023-11-08 15:17 UTC)

<p>Several people reported that they could reliable extract a continuous inner surface of the orbital wall using Wrap Solidify effect in Segment Editor (provided by SurfaceWrapSolidify extension). Since it is simple, a single surface, you can snap your plate model directly to it, without any further processing, iterations, etc.</p>
<p>You need to set these inputs to the solidify effect:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96762423bf40f6f23164cc048f55959000d1920e.jpeg" data-download-href="/uploads/short-url/lt2JGtOZZAvQ1wy7iNlgshdk4Vw.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96762423bf40f6f23164cc048f55959000d1920e_2_690x365.jpeg" alt="image" data-base62-sha1="lt2JGtOZZAvQ1wy7iNlgshdk4Vw" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96762423bf40f6f23164cc048f55959000d1920e_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96762423bf40f6f23164cc048f55959000d1920e_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96762423bf40f6f23164cc048f55959000d1920e_2_1380x730.jpeg 2x" data-dominant-color="524D4E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1016 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You then get the complete, solid model of the orbital cavity in a couple of seconds. Even if the orbital wall is incomplete (which is very often the case, because it is a thin bone and the partial volume effect makes the bone density too similar to soft tissues), the extracted surface is complete and smooth:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d41deb897275529b50da5867b21a6cd631b06f1.jpeg" data-download-href="/uploads/short-url/fAxaxUqVxAY4Ke2glprt8IfOKMV.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d41deb897275529b50da5867b21a6cd631b06f1_2_690x364.jpeg" alt="image" data-base62-sha1="fAxaxUqVxAY4Ke2glprt8IfOKMV" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d41deb897275529b50da5867b21a6cd631b06f1_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d41deb897275529b50da5867b21a6cd631b06f1_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d41deb897275529b50da5867b21a6cd631b06f1_2_1380x728.jpeg 2x" data-dominant-color="514F51"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1013 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @chz31 (2023-11-09 01:25 UTC)

<p>Thanks a lot! I am able to generate an “endocast” of the orbital cavity by using paint brush to create a smaller segment within it and then use the Wrap Solidify to fill the cavity.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3928accfcbb4c54582a67cd34dee290a878d759.jpeg" data-download-href="/uploads/short-url/rU74svvvlTbFr2gqvzh8Z9OPNwJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3928accfcbb4c54582a67cd34dee290a878d759_2_517x287.jpeg" alt="image" data-base62-sha1="rU74svvvlTbFr2gqvzh8Z9OPNwJ" width="517" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3928accfcbb4c54582a67cd34dee290a878d759_2_517x287.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3928accfcbb4c54582a67cd34dee290a878d759_2_775x430.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3928accfcbb4c54582a67cd34dee290a878d759_2_1034x574.jpeg 2x" data-dominant-color="403D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1067 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This tool definitely has lots of potential. It turns out that during surgery, they’ll just remove all the bones surrounding the fracture site and fit the plate to the area. The only hard requirement appears to be aligning the peripheral and the posterior stop (usually the palatine process deep in the orbit). The “endocast”, at least as far as I can tell, captured the peripheral very well, therefore it should be very helpful to use as a reference for adapting the plate. I’ll keep you updated once I get some feedback.</p>

---
