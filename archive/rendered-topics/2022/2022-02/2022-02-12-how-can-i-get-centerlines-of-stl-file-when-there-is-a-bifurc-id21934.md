# How can I get centerlines of .stl file when there is a bifurcation?

**Topic ID**: 21934
**Date**: 2022-02-12
**URL**: https://discourse.slicer.org/t/how-can-i-get-centerlines-of-stl-file-when-there-is-a-bifurcation/21934

---

## Post #1 by @SuHong_Park (2022-02-12 13:55 UTC)

<p>Hi, I’m just downloaded 3d slicer to get center line of a vessel(.stl file).<br>
Since I’m new to 3d slicer and vmtk, I prepared a small part of my research domain with a bifurcation.<br>
But, the result didn’t turned out so well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e21d0814496f4da8a13c3adab52055424d6f5069.png" data-download-href="/uploads/short-url/wgi6HJp0b7DehWzq7JxS42Y43cl.png?dl=1" title="Screen Shot 2022-02-12 at 5.44.54 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e21d0814496f4da8a13c3adab52055424d6f5069_2_569x500.png" alt="Screen Shot 2022-02-12 at 5.44.54 PM" data-base62-sha1="wgi6HJp0b7DehWzq7JxS42Y43cl" width="569" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e21d0814496f4da8a13c3adab52055424d6f5069_2_569x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e21d0814496f4da8a13c3adab52055424d6f5069.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e21d0814496f4da8a13c3adab52055424d6f5069.png 2x" data-dominant-color="9A9BD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-12 at 5.44.54 PM</span><span class="informations">816×716 49.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Using ‘Extract Centerline’ module,</p>
<ol>
<li>I made three end points(create new markups fiducial)</li>
<li>Centerline model : create new model</li>
<li>Centerline curve : create new markup curve<br>
and then I clicked ‘Apply’.</li>
</ol>
<p>As a result, only two end points were connected, and one was left along.<br>
I tried to follow Iassoan’s video(<a href="https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117" class="inline-onebox">New module: Extract Centerline (in SlicerVMTK extension)</a>) but in the example there was only two end points so I couldn’t figure it out.</p>
<p>Here is my stl file I wanted to make centerline.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/GormWH/bifurcation-stl">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/GormWH/bifurcation-stl" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/cd4e072ee8386f5553e2f33ab3c99f1866665e2516ae787f299d1564b33d3a0a/GormWH/bifurcation-stl" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/GormWH/bifurcation-stl" target="_blank" rel="noopener nofollow ugc">GitHub - GormWH/bifurcation-stl</a></h3>

  <p>Contribute to GormWH/bifurcation-stl development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @chir.set (2022-02-12 16:29 UTC)

<p>Try to move your endpoints a little and extract again.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de010d0e42948be7947e75d4550e76e340f02085.png" alt="Screenshot" data-base62-sha1="vFWfvKjns7YfUNvVCGJtgCo1RXL" width="587" height="424"></p>

---

## Post #3 by @lassoan (2022-02-12 16:37 UTC)

<p>The mesh has serious errors. The left image shows the mesh rendered with surface normals to better show the meshing errors, which seem like duplicate and inverted triangles. The right image shows what I got after converting the model to labelmap representation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/162cd3843b1aaf3f923ed1e8e12af32d6ce4984b.png" data-download-href="/uploads/short-url/3aaxJAFS7nsbisv63dDfrD93UYb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/162cd3843b1aaf3f923ed1e8e12af32d6ce4984b_2_690x267.png" alt="image" data-base62-sha1="3aaxJAFS7nsbisv63dDfrD93UYb" width="690" height="267" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/162cd3843b1aaf3f923ed1e8e12af32d6ce4984b_2_690x267.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/162cd3843b1aaf3f923ed1e8e12af32d6ce4984b_2_1035x400.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/162cd3843b1aaf3f923ed1e8e12af32d6ce4984b_2_1380x534.png 2x" data-dominant-color="9C9DAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1563×606 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This mesh error breaks the automatic centerline endpoint computation, but amazingly, the centerline extraction still works well with manually defined endpoints:</p>
<p></p><div class="video-placeholder-container" data-video-src="/404" data-orig-src="upload://lBeO77euPt1ZUrJCiIPspGUWDob.mp4">
  </div><p></p>

---

## Post #4 by @SuHong_Park (2022-02-13 02:00 UTC)

<p>Thank you for your advice!<br>
I wonder why mine didn’t work out.</p>

---

## Post #5 by @SuHong_Park (2022-02-13 02:04 UTC)

<p>I managed to extract centerlines following your video!<br>
Thank you so much for the video and pointing out the error in the mesh.<br>
I’m new to slicer and 3D mesh things, so I probably messed up during making that stl file.</p>

---
