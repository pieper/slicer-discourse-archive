# Is there a way to use the WrapSurfaceSolidify with mammal skulls successfully

**Topic ID**: 40885
**Date**: 2024-12-28
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-use-the-wrapsurfacesolidify-with-mammal-skulls-successfully/40885

---

## Post #1 by @muratmaga (2024-12-28 17:01 UTC)

<p>For some of our procedures, we need to have watertight models (to avoid projecting points to internal surface inside the brain cavity). Using the WrapSurfaceSolidy, I managed to do it, but it does take running the extension twice and then add all the segments together.</p>
<p>I first run it with Outer Surface option with the Carve holes set to 3mm, which fills the nasal cavity and the choana. Then, I use the largest cavity option swith split cavities set to 2mm. That fills the endocranial space. Final operation is to add all segments together with the logical operations.</p>
<p>Is there a way to achieve this in a single pass?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc2304b3c9e6f7149fdd75c5a36bbfb78e6d6422.jpeg" data-download-href="/uploads/short-url/vpq4l6CE3JCUTXPyhPWKGj4PPDs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc2304b3c9e6f7149fdd75c5a36bbfb78e6d6422_2_690x314.jpeg" alt="image" data-base62-sha1="vpq4l6CE3JCUTXPyhPWKGj4PPDs" width="690" height="314" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc2304b3c9e6f7149fdd75c5a36bbfb78e6d6422_2_690x314.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc2304b3c9e6f7149fdd75c5a36bbfb78e6d6422_2_1035x471.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc2304b3c9e6f7149fdd75c5a36bbfb78e6d6422_2_1380x628.jpeg 2x" data-dominant-color="747476"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×874 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-12-30 16:21 UTC)

<p>You can do wrapping in one step when you can work with a single hole size.</p>
<p>In this case (loading the 4074_skull.vtk example and importing it as segmentation), to fill the brain cavity, you need to set a large hole size (Region: Outer surface, Carve holes: enabled, 70mm). However, this would partially fill the cavity around the eye.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd4896f0607a1c49d695965c3951852a21da1e84.jpeg" data-download-href="/uploads/short-url/vzz2H8QGXbp0ECRTKgv4aAhMVgM.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd4896f0607a1c49d695965c3951852a21da1e84_2_690x362.jpeg" alt="image" data-base62-sha1="vzz2H8QGXbp0ECRTKgv4aAhMVgM" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd4896f0607a1c49d695965c3951852a21da1e84_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd4896f0607a1c49d695965c3951852a21da1e84_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd4896f0607a1c49d695965c3951852a21da1e84_2_1380x724.jpeg 2x" data-dominant-color="7C827E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1008 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Since you need is to fill one hole (brain) with &lt;70mm opening, while not fill other holes (eye sockets) with &lt;70mm opening, you cannot do this in one step. You somehow need to tell that you only want to fill the brain cavity.</p>
<p>A simple option would be to reduce the opening of the brain cavity (e.g., paint a large sphere near the opening), but that would make the process less deterministic - shape of the filling would depend on how you reduce the opening.</p>
<p>A better option is to selectively fill the brain cavity (Region: Largest cavity, Split cavities: enabled, 50mm), which is easy to do automatically, as it is the largest cavity, then extract the outer surface (Region: Outer surface, Carve holes: enabled, 30mm). This is what you do already! It is fully automatic, therefore it is fully reproducible. If you don’t like this solution because it takes more time then you can speed up the process by lowering the “Oversampling” parameter (e.g., to 0.3). Lowering oversampling smoothes the surface (losing some small surface details, resulting in having few-voxel holes), which is not a problem in this case, as you only need this to reduce the opening before the outer surfae extraction. If you don’t like the solution because it requires the user to go through a series of steps, then a good solution could be to add a small scripted module that automates all these steps.</p>

---

## Post #3 by @muratmaga (2025-01-09 23:39 UTC)

<p>I created a tutorial for SlicerMorph based on these:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/WaterTightModels">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/WaterTightModels" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/WaterTightModels" target="_blank" rel="noopener nofollow ugc">Tutorials/WaterTightModels at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
