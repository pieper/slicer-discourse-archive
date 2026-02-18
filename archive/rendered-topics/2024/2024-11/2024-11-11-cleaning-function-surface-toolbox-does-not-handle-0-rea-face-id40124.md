# Cleaning Function Surface Toolbox does not handle 0 rea faces/duplicate edges

**Topic ID**: 40124
**Date**: 2024-11-11
**URL**: https://discourse.slicer.org/t/cleaning-function-surface-toolbox-does-not-handle-0-rea-faces-duplicate-edges/40124

---

## Post #1 by @evaherbst (2024-11-11 15:51 UTC)

<p>Hello,</p>
<p>I noticed that the clean function in the Surface Toolbox does not handle duplicate edges ie 0 area faces.<br>
Therefore it does not completely fix non manifold meshes.</p>
<p>Here you can see a mesh that I cleaned with the surface toolbox and checked in Blender. The highlighted edges are duplicated:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/527eccc6cddbc0af9503bd0088d01b4bf0a9cdbf.png" data-download-href="/uploads/short-url/bLMOQzrf3JRj7MvAM4P7gj2CRMX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/527eccc6cddbc0af9503bd0088d01b4bf0a9cdbf_2_661x500.png" alt="image" data-base62-sha1="bLMOQzrf3JRj7MvAM4P7gj2CRMX" width="661" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/527eccc6cddbc0af9503bd0088d01b4bf0a9cdbf_2_661x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/527eccc6cddbc0af9503bd0088d01b4bf0a9cdbf.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/527eccc6cddbc0af9503bd0088d01b4bf0a9cdbf.png 2x" data-dominant-color="A7A9A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">916×692 53.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I move them you can see the issue:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/127e3456fbbef32bd05669029e2b0af98fad6fb2.png" data-download-href="/uploads/short-url/2DAZ9bnq4OeJRqD3pVOpifdO9Sq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/127e3456fbbef32bd05669029e2b0af98fad6fb2_2_624x500.png" alt="image" data-base62-sha1="2DAZ9bnq4OeJRqD3pVOpifdO9Sq" width="624" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/127e3456fbbef32bd05669029e2b0af98fad6fb2_2_624x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/127e3456fbbef32bd05669029e2b0af98fad6fb2_2_936x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/127e3456fbbef32bd05669029e2b0af98fad6fb2.png 2x" data-dominant-color="A6A8A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">998×799 70.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Would there be a way of adding a fix for this?<br>
Previously I have done a lot of semiautomatic mesh cleaning for FE meshes and 3D printing in Blender but would like to migrate everything to Slicer.</p>
<p>Also, I noticed a possible typo in the logic, should line 575 in <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/SurfaceToolbox/SurfaceToolbox.py" rel="noopener nofollow ugc">SurfaceToolbox.py</a>  be</p>
<blockquote>
<p>SurfaceToolboxLogic.clean(inputModel, outputModel)</p>
</blockquote>
<p>instead of</p>
<blockquote>
<p>SurfaceToolboxLogic.clean(outputModel, outputModel) ?</p>
</blockquote>

---

## Post #2 by @pieper (2024-11-11 16:12 UTC)

<p>Internally the code uses the vtk class with the default parameters.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/SurfaceToolbox/SurfaceToolbox.py#L506-L513">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/SurfaceToolbox/SurfaceToolbox.py#L506-L513" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/master/SurfaceToolbox/SurfaceToolbox.py#L506-L513" target="_blank" rel="noopener">Slicer/SlicerSurfaceToolbox/blob/master/SurfaceToolbox/SurfaceToolbox.py#L506-L513</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="506" style="counter-reset: li-counter 505 ;">
          <li>@staticmethod
</li>
          <li>def clean(inputModel, outputModel):
</li>
          <li>  """Merge coincident points, remove unused points (i.e. not used by any cell), treatment of degenerate cells.
</li>
          <li>  """
</li>
          <li>  cleaner = vtk.vtkCleanPolyData()
</li>
          <li>  cleaner.SetInputData(inputModel.GetPolyData())
</li>
          <li>  cleaner.Update()
</li>
          <li>  outputModel.SetAndObservePolyData(cleaner.GetOutput())
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But there are lots of options that could address what you are seeing:</p>
<p><a href="https://vtk.org/doc/nightly/html/classvtkCleanPolyData.html" class="onebox" target="_blank" rel="noopener">https://vtk.org/doc/nightly/html/classvtkCleanPolyData.html</a></p>
<p>If you change to developer mode you can use the edit and reload options to change the settings and see what works.  If you find settings that should be exposed they can be added to the module’s gui.</p>
<aside class="quote no-group" data-username="evaherbst" data-post="1" data-topic="40124">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>possible typo</p>
</blockquote>
</aside>
<p>No, I think the code is correct.  The code above what you referenced creates a new polydata if needed and the successive steps in the toolbox operate on that <code>outputModel</code>.</p>

---

## Post #3 by @evaherbst (2024-11-11 17:26 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Great, I will look into that vtk class!<br>
I have not tried developer mode yet, that will be a good test case.</p>
<p>And ok, I was mistaken about the typo then, thanks for clarifying.</p>

---

## Post #4 by @evaherbst (2024-11-12 11:24 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> the developer mode works well.</p>
<p>I tried adding</p>
<blockquote>
<pre><code>cleaner = vtk.vtkCleanPolyData()
cleaner.ConvertLinesToPointsOn()
cleaner.ConvertPolysToLinesOn()
cleaner.ConvertStripsToPolysOn()
cleaner.SetInputData(inputModel.GetPolyData())
</code></pre>
</blockquote>
<p>However, this does not fix the non manifold issues, since it only covers some, not all, mesh issues.</p>
<p>Would it be possible to incorporate the mesh cleaning functionality from the <a href="https://projects.blender.org/extensions/print3d_toolbox/src/branch/main/source/operators/cleanup.py" rel="noopener nofollow ugc">3D print add-on in Blender</a>? It is written in Python and would enhance the Surface Toolbox cleaning function.</p>
<p>Here is the mesh that was giving me issues. I generated it by upsampling and remeshing and smoothing, all in Slicer. However, the non manifoldness remains (6 vertices, 2 edges, 2 faces): <a href="https://drive.google.com/file/d/1_dKk4dbaK7-Gzhky2Jt_IA5kuzzOR8jY/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">O45_003_SlicerClean_updatedNormals.stl - Google Drive</a></p>
<p>Thanks again!<br>
Eva</p>

---

## Post #5 by @pieper (2024-11-12 12:39 UTC)

<p>There are other mesh cleanup options in vtk (see links below - I’m sure there are more if you search).  They would be easy to add to the Surface Toolbox or as a separate module if there are lots of options.</p>
<p>But if the blender code works well you should also be able wrap and call a blender-python script as a subprocess.  I looked a the code you linked and yes it’s in python, but it relies on the blender libraries to do the work.  There is a <a href="https://pypi.org/project/bpy/">bpy</a> package, but it didn’t install for me in slicer.</p>
<p>Maybe it’s possible to compile blender and bpy expose its python libraries in slicer’s python, and that could open interesting possibilities, but it would be easier as a start to just run blender in a separate process with its own python and pass meshes as files.</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/remove-faces-in-contact-with-non-manifold-edges/4116/14">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/remove-faces-in-contact-with-non-manifold-edges/4116/14" target="_blank" rel="noopener" title="04:08AM - 13 June 2022">VTK – 13 Jun 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/remove-faces-in-contact-with-non-manifold-edges/4116/14" target="_blank" rel="noopener">Remove faces in contact with non-manifold edges</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #F7941D;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Support</span>
        </span>
      </span>
  </div>
</div>

  <p>I don’t think vtkbool is accesible via pip.  If you don’t want to build VTK then one option is to use VTK in the virtual Python environment that 3D Slicer provides. vtkbool is built as part of the Sandbox extension, so after installing 3D Slicer,...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/remove-non-manifold-edges-from-decimated-polydata/9002">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/remove-non-manifold-edges-from-decimated-polydata/9002" target="_blank" rel="noopener" title="10:18PM - 24 July 2022">VTK – 24 Jul 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/remove-non-manifold-edges-from-decimated-polydata/9002" target="_blank" rel="noopener">Remove non-manifold edges from decimated polydata</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #0088CC;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Development</span>
        </span>
      </span>
  </div>
</div>

  <p>Hope this script is useful for someone…  It’s done to be executed on Slicer but you can easily adapt it to pure vtk.  guide_dec = getNode('guide-dec')  idFilter = vtk.vtkIdFilter() idFilter.SetInputData(guide_dec.GetMesh());...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @evaherbst (2024-11-12 13:38 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> !<br>
Seems like the codes in that forum post did not fully work for others but it is a great starting point.</p>
<p>Would be great to make it work with vtk but I will also think about running Blender separately.</p>

---
