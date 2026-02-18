# Dynamic Modeler Subdivision tool new mode

**Topic ID**: 44692
**Date**: 2025-10-08
**URL**: https://discourse.slicer.org/t/dynamic-modeler-subdivision-tool-new-mode/44692

---

## Post #1 by @mau_igna_06 (2025-10-08 00:34 UTC)

<p>Hi, I could create a <a href="https://en.wikipedia.org/wiki/Incenter" rel="noopener nofollow ugc">incenter</a> subdivision algorithm. It creates 3 triangles per each one on the input data, each one of those triangles will include the incenter point and one side of the original triangle.<br>
If someone thinks is useful I could make it available inside the Dynamic Modeler Subdivide tool. Please see picture below for before and after subdivision (left and right sides of the screenshot correspondingly)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfdb124558c69fea1ca66c3878a45c47634eaac4.jpeg" data-download-href="/uploads/short-url/tEMc49KWHi38DZ5ciJN8jELh5v6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfdb124558c69fea1ca66c3878a45c47634eaac4_2_690x389.jpeg" alt="image" data-base62-sha1="tEMc49KWHi38DZ5ciJN8jELh5v6" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfdb124558c69fea1ca66c3878a45c47634eaac4_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfdb124558c69fea1ca66c3878a45c47634eaac4_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfdb124558c69fea1ca66c3878a45c47634eaac4_2_1380x778.jpeg 2x" data-dominant-color="A69C87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1084 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I thought this could be useful to improve the WrapSolidify algorithm because it creates a new point in the middle of the earlier triangle (not over the already existing edges as <code>vtkLinearSubdivision</code>) because of this maybe the new point could intrude into a hole on the mesh to be wrapped</p>
<p>Branch: <a href="https://github.com/mauigna06/VTK/tree/feature_incenterSubdivisionFilter" class="inline-onebox" rel="noopener nofollow ugc">GitHub - mauigna06/VTK at feature_incenterSubdivisionFilter</a></p>

---

## Post #2 by @mau_igna_06 (2025-10-10 01:06 UTC)

<p>Ok. So, after working a bit, on this I realized I needed a remeshing algorithm not a subdivision algorithm. I did implement incenterRemeshing but it was not useful to improve the wrap solidy effect. Then I realized what I needed was isotropic remeshing. I was able to implement it.</p>
<p>I would be glad if someone tests this algorithm and gives feedback. See demo picture below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8292686248a31b9c33067ff6d04d33de64c6cfd.jpeg" data-download-href="/uploads/short-url/syHEPDQMzJtDBzZwr8HANWdmqHb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8292686248a31b9c33067ff6d04d33de64c6cfd_2_690x389.jpeg" alt="image" data-base62-sha1="syHEPDQMzJtDBzZwr8HANWdmqHb" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8292686248a31b9c33067ff6d04d33de64c6cfd_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8292686248a31b9c33067ff6d04d33de64c6cfd_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8292686248a31b9c33067ff6d04d33de64c6cfd_2_1380x778.jpeg 2x" data-dominant-color="AAA8B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1084 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/mauigna06/VTK/tree/feature_isotropicRemeshing">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/mauigna06/VTK/tree/feature_isotropicRemeshing" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/mauigna06/VTK/tree/feature_isotropicRemeshing" target="_blank" rel="noopener nofollow ugc">GitHub - mauigna06/VTK at feature_isotropicRemeshing</a></h3>

  <p><a href="https://github.com/mauigna06/VTK/tree/feature_isotropicRemeshing" target="_blank" rel="noopener nofollow ugc">feature_isotropicRemeshing</a></p>

  <p><span class="label1">WARNING: This is NOT the official upstream VTK git repository</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I still don’t know how to use it without shrinkage but at least works and produces a result in less than 1 second</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/mauigna06/Slicer-SurfaceWrapSolidify/tree/master">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/mauigna06/Slicer-SurfaceWrapSolidify/tree/master" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/mauigna06/Slicer-SurfaceWrapSolidify/tree/master" target="_blank" rel="noopener nofollow ugc">GitHub - mauigna06/Slicer-SurfaceWrapSolidify: 3D Slicer extension which...</a></h3>

  <p><a href="https://github.com/mauigna06/Slicer-SurfaceWrapSolidify/tree/master" target="_blank" rel="noopener nofollow ugc">master</a></p>

  <p><span class="label1">3D Slicer extension which contains a Segment Editor Effect that solidifies and extracts the surface of a segmentation - mauigna06/Slicer-SurfaceWrapSolidify</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5b739458e2ff1b53e97d6564d2bdac65bc234d2.jpeg" data-download-href="/uploads/short-url/z3HxbyvYV0AdKnyQ8OuaYEWc22e.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5b739458e2ff1b53e97d6564d2bdac65bc234d2_2_690x389.jpeg" alt="image" data-base62-sha1="z3HxbyvYV0AdKnyQ8OuaYEWc22e" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5b739458e2ff1b53e97d6564d2bdac65bc234d2_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5b739458e2ff1b53e97d6564d2bdac65bc234d2_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5b739458e2ff1b53e97d6564d2bdac65bc234d2_2_1380x778.jpeg 2x" data-dominant-color="A8A4C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1084 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2025-10-10 12:23 UTC)

<p>Thanks for sharing, this looks interesting. Overall, looks similar to vtkSmoothPolyDataFilter: it keeps mesh topology the same, iteratively relaxes points to make the mesh more uniform. It may be possible that you can make the convergence significantly faster by tweaking the point position update rules.</p>
<p>Could you do some side-by-side comparison of vtkIsotropicRemeshing and vtkSmoothPolyDataFilter? In vtkSmoothPolyDataFilter set the input surface both as InputData and SourceData and set the number of iterations high. Setting the source data makes sure points move tangentially (on the surface), completely eliminating any shrinking. Setting the number of iteration high ensures that we can see the highest quality result that the filter can provide; later you can play with reducing the number of iterations and increasing the relaxation factor to speed up the processing. If you find that your update rule works much better then it could be added as an option to vtkSmoothPolyDataFilter instead of adding a completely new filter. It would reduce the amount of added code and it would allow combining your algorithm with all the features of vtkSmoothPolyDataFilter (constraining to source data, feature edges, boundary smoothing, error metric computations, double/float support, etc.).</p>
<p>It might be interesting to compare with vtkConstrainedSmoothingFilter, too. The filter is nice because it is highly parallelized and it allows setting custom smoothing constraints per point.</p>
<hr>
<p>For wrap solidify: If you have concavities in the input segment then for a fair comparison you need to enable “Carve holes” (the hole size is similar to the hole size in the vtkFillHolesFilter). Please compare again with this option.</p>
<p>Making the mesh more uniform by a smoothing filter (your filter or vtkSmoothPolyDataFilter) instead of remeshing by converting to labelmap image could be a good idea. As I remember, we tried very similar ideas with you a few years ago and somehow the results were not better, but maybe we did not try this exactly. More testing would be useful.</p>

---

## Post #4 by @mau_igna_06 (2025-10-10 13:40 UTC)

<blockquote>
<p>Could you do some side-by-side comparison of vtkIsotropicRemeshing and vtkSmoothPolyDataFilter? In vtkSmoothPolyDataFilter set the input surface both as InputData and SourceData and set the number of iterations high.</p>
</blockquote>
<p>I did this, apparently, smoothFilter solves only degenerate triangles but it does not make triangle edges have a more or less uniform length. See pictures below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8e9668836dce60b933edc4e441a670399856c9c.jpeg" data-download-href="/uploads/short-url/sFlyfnLNmY8ScMtfHBZOnqyYHG4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8e9668836dce60b933edc4e441a670399856c9c_2_690x389.jpeg" alt="image" data-base62-sha1="sFlyfnLNmY8ScMtfHBZOnqyYHG4" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8e9668836dce60b933edc4e441a670399856c9c_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8e9668836dce60b933edc4e441a670399856c9c_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8e9668836dce60b933edc4e441a670399856c9c_2_1380x778.jpeg 2x" data-dominant-color="A3A8A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1084 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
For picture above, vtkSmoothPolyDataFilter on the left side, inputPolyData on the right side</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8a3e123abe8dfd5a694a21be40e1bea17e37770.jpeg" data-download-href="/uploads/short-url/sCWBswbvS1tPj7xVrxgvVFf5i7e.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8a3e123abe8dfd5a694a21be40e1bea17e37770_2_690x389.jpeg" alt="image" data-base62-sha1="sCWBswbvS1tPj7xVrxgvVFf5i7e" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8a3e123abe8dfd5a694a21be40e1bea17e37770_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8a3e123abe8dfd5a694a21be40e1bea17e37770_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8a3e123abe8dfd5a694a21be40e1bea17e37770_2_1380x778.jpeg 2x" data-dominant-color="A3A0A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1084 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
For picture above, vtkIsotropicRemeshing on the left side, vtkSmoothPolyDataFilter on the right side</p>

---

## Post #5 by @lassoan (2025-10-10 13:56 UTC)

<p>In vtkSmoothPolyDataFilter eventually produces a uniform mesh, but you may need to set the number of iterations higher (e.g., try 10000) and/or increase the relaxation factor (try 2x, 5x, 10x, … larger than default), maybe decrease convergence limit. Adding an option to make vtkSmoothPolyDataFilter explicitly favor uniform triangle size could speed this up significantly (as currently uniform triangle size is more of a byproduct than a primary goal). I would recommend to improve vtkSmoothPolyDataFilter instead of introducing a new filter, because it would significantly reduce implementation and testing workload and would eliminate long-term maintenance efforts (VTK core developers would do it).</p>

---

## Post #6 by @mau_igna_06 (2025-10-11 02:44 UTC)

<blockquote>
<p>I would recommend to improve vtkSmoothPolyDataFilter instead of introducing a new filter, because it would significantly reduce implementation and testing workload and would eliminate long-term maintenance efforts (VTK core developers would do it).</p>
</blockquote>
<p>I added a new mode as you suggested but the movement of the points decreases asymptotically with the number of iterations so the output mesh never ends with very low variance of the edge length of the triangles</p>
<p>I created a new DynamicModeler tool for remeshing (ideally it could later be transitioned to a shrink-wrap tool) the code is fast enough on C++ and the license is commercial friendly (see <a href="https://github.com/sgsellan/gpytoolbox" rel="noopener nofollow ugc">gpytoolbox</a>)</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/feature_remeshTool">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/feature_remeshTool" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/feature_remeshTool" target="_blank" rel="noopener nofollow ugc">GitHub - mauigna06/SlicerSurfaceToolbox at feature_remeshTool</a></h3>

  <p><a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/feature_remeshTool" target="_blank" rel="noopener nofollow ugc">feature_remeshTool</a></p>

  <p><span class="label1">Supports various cleanup and optimization processes on surface models</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3ba7f26c36b61b34ce75b0ae2e15d15575418278.jpeg" data-download-href="/uploads/short-url/8vJZIzBaugI4vf6A0GUVtzVsDfG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba7f26c36b61b34ce75b0ae2e15d15575418278_2_690x389.jpeg" alt="image" data-base62-sha1="8vJZIzBaugI4vf6A0GUVtzVsDfG" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba7f26c36b61b34ce75b0ae2e15d15575418278_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba7f26c36b61b34ce75b0ae2e15d15575418278_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba7f26c36b61b34ce75b0ae2e15d15575418278_2_1380x778.jpeg 2x" data-dominant-color="9895A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1084 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2025-10-11 03:11 UTC)

<p>The result looks nice! Does it actually do remeshing or it keeps the topology of the mesh (subdivides and collapses triangles) and just moves the mesh points?</p>
<p>I’ve had a look at the implementation. It is good that you build the libigl project as is, instead of vendorizing it (it allows us to get fixes and improvements in the future). However, for consistency with how all the other extensions use external libraries and since other extensions may also use libigl project, we need to follow the conventions on how third-party libraries are built in extensions. Unfortunately, SurfaceToolbox is not a regular extension and it is bundled with 3D Slicer core by default, so making it a superbuild-type may not be trivial. For this reason, and also because libigl is not a small project and it could have non-trivial dependencies, it may be easier to get it integrated via an extension. Maybe a new 'libigl" utility extension could be added for this.</p>

---

## Post #8 by @mau_igna_06 (2025-10-11 03:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="44692">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The result looks nice! Does it actually do remeshing or it keeps the topology of the mesh (subdivides and collapses triangles) and just moves the mesh points?</p>
</blockquote>
</aside>
<p>Thank you, it does change the number of triangles so I would say topology changes</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="44692">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Unfortunately, SurfaceToolbox is not a regular extension and it is bundled with 3D Slicer core by default, so making it a superbuild-type may not be trivial. For this reason, and also because libigl is not a small project and it could have non-trivial dependencies, it may be easier to get it integrated via an extension. Maybe a new 'libigl" utility extension could be added for this.</p>
</blockquote>
</aside>
<p>I thought about exposing the whole library but I did not see any algorithm of interest other than the remeshing one</p>

---

## Post #9 by @lassoan (2025-10-11 03:35 UTC)

<p>Even if we use a single method from the library, we need to make it a superbuild-type extension. But then the extension may be called uniform remeshing extension or something like that. It could have a more generic name if we think we will add more methods from libigl or elsewhere.</p>
<p>If you find this too much work then vendorizing (copying from the library) could be an option, but then it becomes very difficult to get future updates.</p>

---

## Post #10 by @mau_igna_06 (2025-10-13 22:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="44692">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Even if we use a single method from the library, we need to make it a superbuild-type extension. But then the extension may be called uniform remeshing extension or something like that. It could have a more generic name if we think we will add more methods from libigl or elsewhere.</p>
</blockquote>
</aside>
<p>Done.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/mauigna06/SlicerUniformRemesh">
  <header class="source">

      <a href="https://github.com/mauigna06/SlicerUniformRemesh" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/8aac01e50cbde7814f0f280a9b485a6e/mauigna06/SlicerUniformRemesh" class="thumbnail">

  <h3><a href="https://github.com/mauigna06/SlicerUniformRemesh" target="_blank" rel="noopener nofollow ugc">GitHub - mauigna06/SlicerUniformRemesh</a></h3>

    <p><span class="github-repo-description">Contribute to mauigna06/SlicerUniformRemesh development by creating an account on GitHub.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @mau_igna_06 (2025-10-14 14:55 UTC)

<p>The new filter can be used in python console or using the CLI module <code>UniformRemesh</code></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9fc87039ba7e7974ab4cc835ac3803c4f1e6643.jpeg" data-download-href="/uploads/short-url/zFtVvGHjIUpRaAKnnVY5mWGIQa7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9fc87039ba7e7974ab4cc835ac3803c4f1e6643_2_690x388.jpeg" alt="image" data-base62-sha1="zFtVvGHjIUpRaAKnnVY5mWGIQa7" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9fc87039ba7e7974ab4cc835ac3803c4f1e6643_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9fc87039ba7e7974ab4cc835ac3803c4f1e6643_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9fc87039ba7e7974ab4cc835ac3803c4f1e6643_2_1380x776.jpeg 2x" data-dominant-color="95919A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1082 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @chir.set (2025-10-16 11:29 UTC)

<p>I could build UniformRemesh but I had to comment out testing in <code>UniformRemesh/CMakeLists.txt</code>.</p>
<p>Processing an already uniform mesh completed in a breeze with no <em>apparent</em> modifications when viewed as wireframe, and with no change in the number of points and the number of cells.</p>
<p>However, with <a href="https://disk.yandex.com/d/pzbJeSW3VW2lQA" rel="noopener nofollow ugc">this non-uniform mesh</a>, it keeps running and I stopped at one hour. May be you could check the mesh and suggest a few tips. It’s only for testing, with all default parameters.</p>

---

## Post #13 by @mau_igna_06 (2025-10-16 19:08 UTC)

<p>Hi,</p>
<p>These few days I tried to make a new version of the same remeshing algorithm (i.e. Botsch-Kobbelt) that only depends on Eigen library, while I was able to make it partially work I did not get any good result, good performance or robustness for complex input meshes. One of the road blockers was that even trying to copy all auxiliary classes from <a href="https://github.com/sgsellan/gpytoolbox/tree/main/src/cpp/remesher" rel="noopener nofollow ugc">remesh_botsch</a> some of the classes depended on <code>libigl</code> components that were optimized like <a href="https://github.com/libigl/libigl/blob/ae8f959ea26d7059abad4c698aba8d6b7c3205e8/include/igl/decimate.cpp#L24" rel="noopener nofollow ugc">libigl::decimate</a></p>
<p>My Eigen implementation was at least 10 times (or more) slower than using <code>gpytoolbox::remesh_botsch</code> and the output delivered unexpected holes and self-intersections.</p>
<p>We have 2 options if we still want this algorithm to be available on Slicer:</p>
<ul>
<li>use the version that goes with the <a href="https://github.com/mauigna06/VTK/tree/feature_isotropicRemeshing" rel="noopener nofollow ugc">SurfaceToolbox</a></li>
<li>use the version that goes packaged in its own extension (<a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/feature_remeshTool" rel="noopener nofollow ugc">SlicerUniformRemesh</a>)</li>
</ul>
<p>Even with these fails, it was fun to compile these libraries, integrate them to Slicer in different ways, understand a bit more CMake configuration, how to create and register tests, how to use gdb to debug, etc. So overall it was a great learning experience</p>
<hr>
<p><a class="mention" href="/u/chir.set">@chir.set</a> I tested the data you provided, even the original <code>gpytoolbox::remesh_botsch</code> version fails with the data you provided, I don’t know how to solve it. But if you really need to remesh it, there is already a tool for this on the SurfaceToolbox that exposes <a href="https://github.com/mauigna06/SlicerSurfaceToolbox/tree/feature_remeshTool" rel="noopener nofollow ugc">ACVD remesher</a> and your file could be remeshed using it.</p>
<hr>
<p>By the way, if we want to integrate the ACVD algorithm in Slicer’s C++ code, we may consider using one of these implementations from MITK (as far as I can understand the license is commercial friendly):</p>
<ul>
<li><a href="https://github.com/MITK/MITK/blob/83a70aa30b85e842928653d6a3a949d06bb835c4/Modules/Remeshing/include/mitkRemeshing.h" class="inline-onebox" rel="noopener nofollow ugc">MITK/Modules/Remeshing/include/mitkRemeshing.h at 83a70aa30b85e842928653d6a3a949d06bb835c4 · MITK/MITK · GitHub</a></li>
<li><a href="https://github.com/RabadanLab/MITKats/blob/fb309aa05b063f71ada9d82826291016369377be/Modules/Remeshing/mitkACVD.h" class="inline-onebox" rel="noopener nofollow ugc">MITKats/Modules/Remeshing/mitkACVD.h at fb309aa05b063f71ada9d82826291016369377be · RabadanLab/MITKats · GitHub</a></li>
</ul>

---
