# Calculate angle between oriented bounding boxes

**Topic ID**: 15241
**Date**: 2020-12-27
**URL**: https://discourse.slicer.org/t/calculate-angle-between-oriented-bounding-boxes/15241

---

## Post #1 by @Emrah_Akay (2020-12-27 19:07 UTC)

<p>Operating system : Win10 x64:<br>
Slicer version : 4.11.20200930</p>
<p>I’m  a medical doctor and fairly new to the slicer 3d application, I am trying to calculate the angles between oriented bounding boxes created with the python code here <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_size.2C_position.2C_and_orientation_of_each_segment" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b880e801953933c6058c76777f5a3752add37543.jpeg" data-download-href="/uploads/short-url/qkc2at0YBOjvD65rysRH4xAtzsT.jpeg?dl=1" title="Ekran Alıntısı" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b880e801953933c6058c76777f5a3752add37543_2_635x500.jpeg" alt="Ekran Alıntısı" data-base62-sha1="qkc2at0YBOjvD65rysRH4xAtzsT" width="635" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b880e801953933c6058c76777f5a3752add37543_2_635x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b880e801953933c6058c76777f5a3752add37543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b880e801953933c6058c76777f5a3752add37543.jpeg 2x" data-dominant-color="9597CB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Alıntısı</span><span class="informations">763×600 46.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I tried to use the segment statistics module for this task but cannot fully understand how to use the data provided. What i need is a simple solution like the angle planes module since i’ll be dealing with huge amount of calculations. Thanks for your patience…</p>

---

## Post #2 by @lassoan (2020-12-27 20:08 UTC)

<p><code>obb_direction_ras_x</code>, <code>obb_direction_ras_y</code>, and <code>obb_direction_ras_z</code> are vectors specifying direction of coordinate system axes. You can get angles between vectors using standard vector math, but you can also use convenience functions in VTK, for example:</p>
<pre><code class="lang-python">v1 = box1_obb_direction_ras_x
v2 = box2_obb_direction_ras_x
box1_box2_x_angle = vtk.vtkMath.DegreesFromRadians(vtk.vtkMath.AngleBetweenVectors(v1, v2))
</code></pre>

---

## Post #3 by @Emrah_Akay (2020-12-28 13:40 UTC)

<p>Thank you for quick reply. I have managed to measure the vector angles as you described but was unable to produce accurate reproducible results. I need to measure a specific angle for each OBB like this one <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b27e4fdaeb81c38b81421146b25f072e2b89fe5.jpeg" data-download-href="/uploads/short-url/m8ztQOQgiCk6IsSW62Hem1sw473.jpeg?dl=1" title="Ekran Alıntısı" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b27e4fdaeb81c38b81421146b25f072e2b89fe5_2_438x500.jpeg" alt="Ekran Alıntısı" data-base62-sha1="m8ztQOQgiCk6IsSW62Hem1sw473" width="438" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b27e4fdaeb81c38b81421146b25f072e2b89fe5_2_438x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b27e4fdaeb81c38b81421146b25f072e2b89fe5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b27e4fdaeb81c38b81421146b25f072e2b89fe5.jpeg 2x" data-dominant-color="9C9DD0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Alıntısı</span><span class="informations">568×647 29.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> Actually it’s the angle between the central planes of each OBB <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03566cad66d3b38e424532c8038aa4cea51101c2.jpeg" data-download-href="/uploads/short-url/twAXnKuvaL7GjryuPRyTaEHTKq.jpeg?dl=1" title="Ekran Alıntısı2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/03566cad66d3b38e424532c8038aa4cea51101c2_2_440x500.jpeg" alt="Ekran Alıntısı2" data-base62-sha1="twAXnKuvaL7GjryuPRyTaEHTKq" width="440" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/03566cad66d3b38e424532c8038aa4cea51101c2_2_440x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03566cad66d3b38e424532c8038aa4cea51101c2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03566cad66d3b38e424532c8038aa4cea51101c2.jpeg 2x" data-dominant-color="AE82AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Alıntısı2</span><span class="informations">568×645 48.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> would you please point me to the right direction?. Thanks in advance…</p>

---
