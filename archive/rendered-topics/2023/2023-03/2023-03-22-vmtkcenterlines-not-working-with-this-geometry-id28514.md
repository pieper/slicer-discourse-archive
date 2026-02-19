---
topic_id: 28514
title: "Vmtkcenterlines Not Working With This Geometry"
date: 2023-03-22
url: https://discourse.slicer.org/t/28514
---

# vmtkcenterlines not working with this geometry

**Topic ID**: 28514
**Date**: 2023-03-22
**URL**: https://discourse.slicer.org/t/vmtkcenterlines-not-working-with-this-geometry/28514

---

## Post #1 by @amscosta (2023-03-22 03:01 UTC)

<p>Hello All,<br>
My question is very simple. When I try :<br>
vmtkcenterlines -ifile manifold_shell.stl -ofile manifold_centerlines.vtp<br>
After selecting source and target points graphically, The vmtk enters in a crash loop.<br>
Any clue how to extract the centerlines is very welcome.<br>
Here it follows the manifold_shell.stl  (renamed to .mp4 for uploading purposes).<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4eeacfec93ccf2aa3a24b7f25bef554c975c953.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4eeacfec93ccf2aa3a24b7f25bef554c975c953.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4eeacfec93ccf2aa3a24b7f25bef554c975c953.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @lassoan (2023-03-22 03:04 UTC)

<p>This was due to a VTK bug that has been fixed in VTK about 8 months ago, which might not have made it into your VMTK distribution yet. The was backported to Slicer’s VTK a few days ago (in Slicer revision 31684).</p>

---

## Post #3 by @amscosta (2023-03-23 14:35 UTC)

<p>Hi Andreas,<br>
I just followed the steps in your youtube video. Please see the attached video. However de centerlines curves are not so “smooth” as expected for this manifold.<br>
Any guidance about how to improve the centerlines are very welcome.</p>
<p>(Attachment manifold_3d_slicer_centerline_extract.mp4 is missing)</p>

---

## Post #4 by @lassoan (2023-03-23 14:36 UTC)

<p>The video is missing. Please try uploading it again (use the Slicer Forum web interface, email attachments probably don’t get posted).</p>

---

## Post #5 by @amscosta (2023-03-23 18:06 UTC)

<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/11m_0siqv_wa6NQVgIORft06fvdvP72lp/view?usp=share_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/11m_0siqv_wa6NQVgIORft06fvdvP72lp/view?usp=share_link" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://lh3.googleusercontent.com/aStOfkMukKgkUoKN8PAVWjXZUe5eFXkZ0ZsvcU24sqRbF8ItZFF1ypbGdrvzH1oM2Qs=w1200-h630-p" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://drive.google.com/file/d/11m_0siqv_wa6NQVgIORft06fvdvP72lp/view?usp=share_link" target="_blank" rel="noopener nofollow ugc">manifold_3d_slicer_centerline_extract.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2023-03-24 04:22 UTC)

<p>To me the result shown on the video is very good. I’m not sure what kind of smoothness you are looking for. Maybe you could grab one frame of the video and just draw the curve shape that you would expect.</p>
<p>“Network” method extract centerline purely based on the geometry of the input surface. It will be just as smooth as the input shape dictates. Resolution of the input mesh migh affect the result (if the elements are large or their sizes are highly varying). Could you show the input model with edges displayed (models module → Display → 3D Display → Representation → Surface with edges)? You can try if uniform resampling in Surface toolbox module makes any difference in the output.</p>
<p>“Tree” method creates more realistic, directional flow pattern.</p>

---
