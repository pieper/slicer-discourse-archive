# Surface Normal Calculation Issue Using SurfaceNets

**Topic ID**: 40811
**Date**: 2024-12-19
**URL**: https://discourse.slicer.org/t/surface-normal-calculation-issue-using-surfacenets/40811

---

## Post #1 by @leoavileis (2024-12-19 21:11 UTC)

<p>Dear community,</p>
<p>I’m writing to report an issue that showed up on my project regarding normal calculations when exporting models based on my segmentations. Basically when I export the models while SurfaceNets rendering is enabled under “Show 3D” on Segment Editor, the newly generated surface appears with intercalating rows of flipped normals.</p>
<p>I made a test scene that contains: 1. the segmentation; 2. models generated using default 3D rendering and SurfaceNets; 3. Models showing the effect of trying to fix the normals via the SurfaceToolbox module. The images below show the surface of the model exported with SurfaceNets (first), and the results after trying to fix with SurfaceToolbox (second). The other models exported with SurfaceNets disabled turned out fine (third).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9096777b406308330560afcd2c82a0b1d6d9d3a6.jpeg" data-download-href="/uploads/short-url/kD580HxFCXn5kRKYnISMTPMtjwy.jpeg?dl=1" title="Screenshot 2024-12-19 161722" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9096777b406308330560afcd2c82a0b1d6d9d3a6_2_690x333.jpeg" alt="Screenshot 2024-12-19 161722" data-base62-sha1="kD580HxFCXn5kRKYnISMTPMtjwy" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9096777b406308330560afcd2c82a0b1d6d9d3a6_2_690x333.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9096777b406308330560afcd2c82a0b1d6d9d3a6_2_1035x499.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9096777b406308330560afcd2c82a0b1d6d9d3a6_2_1380x666.jpeg 2x" data-dominant-color="C6B586"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-12-19 161722</span><span class="informations">1920×929 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c86c7b4e6e9fb49f1101bd634ab8e905b6836743.jpeg" data-download-href="/uploads/short-url/sB1UJcQU7HozZx07HSEeVIXYmT9.jpeg?dl=1" title="normalfix" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c86c7b4e6e9fb49f1101bd634ab8e905b6836743_2_690x334.jpeg" alt="normalfix" data-base62-sha1="sB1UJcQU7HozZx07HSEeVIXYmT9" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c86c7b4e6e9fb49f1101bd634ab8e905b6836743_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c86c7b4e6e9fb49f1101bd634ab8e905b6836743_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c86c7b4e6e9fb49f1101bd634ab8e905b6836743_2_1380x668.jpeg 2x" data-dominant-color="B4B2D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">normalfix</span><span class="informations">1920×931 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9690ed161330e3a39a611f66b0d558c30f91d187.jpeg" data-download-href="/uploads/short-url/ltY7E8aA4qy03AB2at1VYqRmZIb.jpeg?dl=1" title="fine" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9690ed161330e3a39a611f66b0d558c30f91d187_2_690x336.jpeg" alt="fine" data-base62-sha1="ltY7E8aA4qy03AB2at1VYqRmZIb" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9690ed161330e3a39a611f66b0d558c30f91d187_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9690ed161330e3a39a611f66b0d558c30f91d187_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9690ed161330e3a39a611f66b0d558c30f91d187_2_1380x672.jpeg 2x" data-dominant-color="AEB8C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fine</span><span class="informations">1920×935 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards,<br>
Leonardo</p>

---

## Post #2 by @muratmaga (2024-12-19 22:29 UTC)

<p>I have observed similar patterns myself with the mouse skulls during the course. I will try to create a small reproducible dataset.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> can you take a look? Particularly if we are going to make the surface nets the default method for model creation.</p>

---

## Post #3 by @mhalle (2024-12-20 00:12 UTC)

<p>I also noticed surface normals behaving as strangely with vtk surfacenets just when they were released. If it is the same issue, I would see patches of the surface flip orientation. Is that the same as you are seeing?</p>
<p>Surface normals are a little bit tricky to handle in surfacenets because all interfaces between adjacent segments are handled at once. Backside and front side lose their natural meaning.</p>
<p>The vtk surfacenets algorithm also keeps track of the labels on either side of the polygons of the surface (the front side and the back side based on the surface normal). It would be interesting to see if those values get flipped as well. If they do, then they would be an easy way to detect and correct the problem.</p>

---

## Post #4 by @spyridon97 (2025-01-22 17:57 UTC)

<p>I would appreciate it if someone can share an image dataset that recreates the issue, along with a picture in which you circle a wrong facing normal.</p>
<p>Thanks a lot in advance.</p>

---

## Post #5 by @muratmaga (2025-01-22 18:53 UTC)

<ol>
<li>Download MRHead</li>
<li>Segment with threshold 45-Max</li>
<li>Enable surface nets and smoothing with surfacenet</li>
<li>Show 3D</li>
<li>Go to data module and export the segmentation as amodel</li>
<li>turn off the segmentaiton and zoom in to the model to see the stripped patterns of greens (when they inverted they have the lighter color).</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1370c958fc4870c8f51a2fae332f71d61e1fad41.jpeg" data-download-href="/uploads/short-url/2LYIo2gYXT4ICUDIszwUuZTSVvX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1370c958fc4870c8f51a2fae332f71d61e1fad41.jpeg" alt="image" data-base62-sha1="2LYIo2gYXT4ICUDIszwUuZTSVvX" width="690" height="493" data-dominant-color="6E8578"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1007×720 51.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17ea8f76890549dd9acec316399c74e727025b57.png" data-download-href="/uploads/short-url/3pzwyJuJVU2bxcgUHGcEpYkauKb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17ea8f76890549dd9acec316399c74e727025b57.png" alt="image" data-base62-sha1="3pzwyJuJVU2bxcgUHGcEpYkauKb" width="169" height="209"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">169×209 3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @spyridon97 (2025-08-07 16:34 UTC)

<p>I have a potential fix for this issue here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/11847">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" class="site-icon" alt="" width="32" height="32">

      <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/11847" target="_blank" rel="noopener nofollow ugc">GitLab</a>
  </header>

  <article class="onebox-body">
    <img width="64" height="64" src="https://gitlab.kitware.com/uploads/-/system/project/avatar/13/vtk_logo-main1.png" class="thumbnail onebox-avatar" alt="">

<h3><a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/11847" target="_blank" rel="noopener nofollow ugc">vtkSurfaceNets3D: Improvements and bug fixes (!11847) · Merge requests · VTK...</a></h3>

  <p>vtkSurfaceNets3D: Improve variable names and use std containers vtkSurfaceNets3D: Convert AdvanceRowIterator to be branch-less vtkSurfaceNets3D: Fix orientation consistency and scalar data handling</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @spyridon97 (2025-10-08 13:34 UTC)

<p>The fix has been merged in VTK.</p>
<p>Slicer will get it probably in a new version when its VTK version is updated.</p>

---
