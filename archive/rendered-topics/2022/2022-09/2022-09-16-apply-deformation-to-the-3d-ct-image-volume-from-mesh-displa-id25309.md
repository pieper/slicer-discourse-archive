---
topic_id: 25309
title: "Apply Deformation To The 3D Ct Image Volume From Mesh Displa"
date: 2022-09-16
url: https://discourse.slicer.org/t/25309
---

# Apply deformation to the 3D-CT image volume from mesh displacement

**Topic ID**: 25309
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/apply-deformation-to-the-3d-ct-image-volume-from-mesh-displacement/25309

---

## Post #1 by @suranga (2022-09-16 16:17 UTC)

<p>I have a reference mesh and a deformed version of it (they are unstrcuted grid saved in vtk file format). The reference mesh was acquired from a 3D-CT volume.</p>
<p>I would want to apply the same deformation to the reference 3D-CT volume so that it align with the deformed mesh configuration.</p>
<p>How can I achieve this with 3D slicer?  Any help would be appreciated (It would be greate if you could provide steps)</p>
<p>I have herewith shared a sample reference mesh, deformed mesh and corresponding reference CT volume in the link given below for your further consideration.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1opb2Hz85RoHrCqrfWtZ-EsjHoEkwIhLd/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1opb2Hz85RoHrCqrfWtZ-EsjHoEkwIhLd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1opb2Hz85RoHrCqrfWtZ-EsjHoEkwIhLd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1opb2Hz85RoHrCqrfWtZ-EsjHoEkwIhLd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">sample_data.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @muratmaga (2022-09-16 17:32 UTC)

<aside class="quote no-group" data-username="suranga" data-post="1" data-topic="25309">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/8491ac/48.png" class="avatar"> suranga:</div>
<blockquote>
<p>I would want to apply the same deformation to the reference 3D-CT volume so that it align with the deformed mesh configuration.</p>
</blockquote>
</aside>
<p>For that you need the deformation field applied to the reference mesh. If you have that, you might be able to import it into slicer as a Transform, and then apply that transformation to the CT have. It boils down to what software you created the deformation and whether you can export the transform in a format slicer understands…</p>

---

## Post #3 by @lassoan (2022-09-16 20:51 UTC)

<p>The difficulty is that you only know displacements at mesh points, but you would need the displacement at the position of every image voxel. Slicer has two tools that you can use for this:</p>
<ul>
<li>Option A: You can use the known point pair positions in a thin-plate spline transform, but if there are many points then the computation can be slow and if the distance between the points is varying and the displacement field is complex then there could be instabilities.</li>
<li>Option B: Use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ScatteredTransform">ScatteredTransform extension</a> to reconstruct a bspline transform from the sparse point set. This may not reproduce the exact displacement but it should be much faster and more robust.</li>
</ul>
<p>It would be a much better (more accurate, more robust solution) to save the full transform when the mesh registration software aligns the meshes (instead of just saving the displacements at the mesh points). If your current registration software does not support this then you can do this for example in Slicer’s <a href="https://github.com/SlicerRt/SegmentRegistration#segment-registration">SegmentRegistration extension</a> (it supports rigid and warping registration between meshes).</p>

---
