# Creating a custom Annotation node in a Python scripted module

**Topic ID**: 2331
**Date**: 2018-03-15
**URL**: https://discourse.slicer.org/t/creating-a-custom-annotation-node-in-a-python-scripted-module/2331

---

## Post #1 by @mschumaker (2018-03-15 20:34 UTC)

<p>I’m trying to create a “slider ring” in the MRML scene via a Python scripted module. The idea is to be able to grab the ring (modelled as a vtkPolyData torus) and move it along a path defined by another vtkPolyData.<br>
The vtkMRMLAnnotationControlPointsNode in the Annotation module looks like a place to start. It has derived classes that appear to do some of what I am trying.<br>
I have two questions:<br>
The first is whether I’m on the right track, or if there is a better way to accomplish what I’m trying to do.<br>
The second is, can I make a derived class of vtkMRMLAnnotationControlPointsNode in Python, or otherwise customize this class in my module? I see that Annotations is a loadable module, and my attempts so far have not worked.<br>
Thank you for any assistance.</p>

---

## Post #2 by @lassoan (2018-03-15 20:46 UTC)

<p>What we usually do is to define curve using markup fiducials, interpolate using Markups to models module. You can get model points as a numpy array and do least squares fit in a small neighborhood to get position and direction vector along the curve. To fully constrain the rotation, we use normal vector of the plane that is least-square-fit to the entire curve. All easily doable from Python.</p>
<p>Moving along the curve with a GUI slider is easy, but interacting in viewers is more tricky. Maybe you can snap the position to the closest position to the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_current_mouse_coordinates_in_a_slice_view">cursor</a> that you can move around by Shift+MouesMove.</p>
<p>What is the clinical application?</p>

---

## Post #3 by @mschumaker (2018-03-16 15:31 UTC)

<p>Thanks, Andras.<br>
The application is a viewer for MR image sets of peripheral arteries. The plan is to reformat the 2D slices so that their normals are always oriented along the centreline of the artery (hence my previous question about VMTK).<br>
Your description of getting the point positions and creating the path with a least-squares fit makes sense. Thank you. I’m confused by the part about constraining the rotation with a normal vector from a least-squares fit to the full curve. I understand the need to constrain the rotation, but what direction does it end up pointing in?</p>
<p>Regarding the object in the 3D view, I’ll experiment with ways to snap it to cursor positions as you suggest, but my first question is how to create a handle from a given polydata in Slicer. How do I create a handle that I can move with the mouse?</p>
<p>Thanks very much for your help.</p>

---

## Post #4 by @mschumaker (2018-03-16 17:22 UTC)

<p>This navigation style isn’t our idea. We’re trying to emulate some of the features in TeraRecon’s EVAR module:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.terarecon.com/advanced-visualization/evar-planning-package">
  <header class="source">
      <img src="https://www.terarecon.com/hubfs/terarecon-monogram.ico" class="site-icon" width="" height="">

      <a href="https://www.terarecon.com/advanced-visualization/evar-planning-package" target="_blank" rel="noopener nofollow ugc">terarecon.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://www.terarecon.com/advanced-visualization/evar-planning-package" target="_blank" rel="noopener nofollow ugc">EVAR (Vessel Analysis) Planning   | TeraRecon</a></h3>

  <p>TeraRecon's EVAR (vessel analysis) package includes an advanced measurement protocol option, user definable planning template with report output, &amp; embedded instructions.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2018-03-16 18:00 UTC)

<p>Yes it is standard curved planar reformatting. The functionality is already available in Slicer, it just not easy to figure out how. It is described in detail here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="1015">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/2bfe46/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/cross-sectional-area-of-a-ring/1015">Cross Sectional Area of a Ring</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I am looking to calculate the cross sectional area at multiple points around the ring (I tried to mark where I would like to slice the ring and measure the area using pairs of fiducials in the image below). 
I am not sure what the best method is as the orientation of the slice is constantly changing, so I’m just looking for an idea of what add-on or method would be best. Thank you! 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ebb246889d2b85c9f1cb84b30ccebe398acad4e.jpeg" data-download-href="/uploads/short-url/26jDmISbHdABbbUkMlpOpQHY8aO.jpg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>

<p>So, you can find an example of positioning an object along a curve in Endoscopy module. I think this module uses the same method as I described above to constrain rotation around the curve direction vector. For vessels (and for any other significantly non-planar curve), I would use a Frenet-Serret frame (<a href="https://github.com/jeromevelut/SplineDrivenImageSlicer/blob/master/Filters/vtkFrenetSerretFrame.h" class="inline-onebox">SplineDrivenImageSlicer/Filters/vtkFrenetSerretFrame.h at master · djelouze/SplineDrivenImageSlicer · GitHub</a>) instead of a fixed constraining direction.</p>

---

## Post #6 by @mschumaker (2018-03-16 18:54 UTC)

<p>Thank you! The Frenet-Serret frame looks like a great approach. That gives me a solution to a couple of my next steps.</p>
<p>Back to the other question of how to customize an object that can move through the 3D view, how can I create something like the Control Points of the ROI box in the Annotations module, or the Fiducial points in the Markups module, but with my own polydata (torus) as the movable object?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92d1d1e9918e9784da4c674b70c24f63140c92c4.png" data-download-href="/uploads/short-url/kWPfmV9RCEVZ9cI6c0hLdhhj1f6.png?dl=1" title="torus3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d1d1e9918e9784da4c674b70c24f63140c92c4_2_565x500.png" alt="torus3D" data-base62-sha1="kWPfmV9RCEVZ9cI6c0hLdhhj1f6" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d1d1e9918e9784da4c674b70c24f63140c92c4_2_565x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d1d1e9918e9784da4c674b70c24f63140c92c4_2_847x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92d1d1e9918e9784da4c674b70c24f63140c92c4.png 2x" data-dominant-color="1A1918"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">torus3D</span><span class="informations">875×774 21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2018-03-18 12:19 UTC)

<p>Creating custom widgets like the ROI widget is extremely difficult. You can emulate custom widgets buy using markup fiducial points as “handles” that you can move and observer the markup node changes to update model position based on that. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer">this example</a> in the script repository where you reposition and resize a sphere model by using markup fiducials.</p>

---

## Post #8 by @mschumaker (2018-03-19 14:48 UTC)

<p>Thank you, I’ll try that approach.</p>

---

## Post #9 by @mschumaker (2018-03-27 19:51 UTC)

<p>Regarding the Frenet-Serret frame code, is there a Python-wrapped version accessible? Alternatively, how would I do so? I believe I can create a Python class inherited from vtk.vtkPolyDataAlgorithm and translate the C++ version, though it would be great if there was a way to avoid doing so.<br>
Thanks again.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/djelouze/SplineDrivenImageSlicer/blob/master/Filters/vtkFrenetSerretFrame.h" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/djelouze/SplineDrivenImageSlicer/blob/master/Filters/vtkFrenetSerretFrame.h" target="_blank" rel="nofollow noopener">djelouze/SplineDrivenImageSlicer/blob/master/Filters/vtkFrenetSerretFrame.h</a></h4>
<pre><code class="lang-h">// Copyright (c) 2010, Jérôme Velut
// All rights reserved.
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// * Redistributions of source code must retain the above copyright
// notice, this list of conditions and the following disclaimer.
// * Redistributions in binary form must reproduce the above copyright
// notice, this list of conditions and the following disclaimer in the
// documentation and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT OWNER ``AS IS'' AND ANY EXPRESS
// OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
// OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN
// NO EVENT SHALL THE COPYRIGHT OWNER BE LIABLE FOR ANY DIRECT, INDIRECT,
// INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
// OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
// LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
// NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
</code></pre>

  This file has been truncated. <a href="https://github.com/djelouze/SplineDrivenImageSlicer/blob/master/Filters/vtkFrenetSerretFrame.h" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #10 by @lassoan (2018-03-27 20:38 UTC)

<p>To add new C++ classes, you need to add a loadable module. It can be hidden, no widget is required. You can add this class to the logic folder. You may use <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/DataProbe">DataProbe</a> module as an example.</p>

---

## Post #11 by @mschumaker (2018-04-17 20:42 UTC)

<p>The Spline-Driven Image Slicer has been added to VTK as a Remote module. The CMake file in the VTKv9/Remote directory fetches from <a href="https://github.com/lorensen/midas-journal-838.git" rel="nofollow noopener">https://github.com/lorensen/midas-journal-838.git</a>, which is more recently maintained than the djelouze repository.</p>

---
