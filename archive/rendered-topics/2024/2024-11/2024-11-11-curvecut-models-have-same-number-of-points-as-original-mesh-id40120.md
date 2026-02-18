# CurveCut models have same number of points as original mesh

**Topic ID**: 40120
**Date**: 2024-11-11
**URL**: https://discourse.slicer.org/t/curvecut-models-have-same-number-of-points-as-original-mesh/40120

---

## Post #1 by @evaherbst (2024-11-11 11:34 UTC)

<p>Hello,</p>
<p>After using a curve cut on a 3D model, the resulting output model mesh looks fine, but when I check th point number in the output model, it still has the original number of points. Same if I save as .vtk and reimport.</p>
<p>If I do any calculations on the vtk polydata of the resulting model (e.g. sphere fitting), it still uses all of the original points.</p>
<p>If I save as .stl and reimport then the point number is updated and so is the polydata.</p>
<p>Is this expected behaviour?</p>
<p>Thank you,<br>
Eva</p>

---

## Post #2 by @cpinter (2024-11-11 11:39 UTC)

<p>If you run a Clean operation in Surface Toolbox on the output mesh does it remove the stray points?</p>

---

## Post #3 by @evaherbst (2024-11-11 11:48 UTC)

<p>Yes that works!</p>
<p>Thank you.</p>
<p>I can batch run the cleaning on my own files, but it might be nice to incorporate this cleaning directly into the CurveCut module, <a class="mention" href="/u/cpinter">@cpinter</a> would this be an option?</p>

---

## Post #4 by @cpinter (2024-11-11 12:30 UTC)

<p>I think it would make sense. However, this module exists for years now and this has not come up yet. I use it in some of my applications myself, and have not had this problem. Maybe this is specific to your data? It would help if you showed your use case. In the meantime I’ll do some simple tests and see if this issue always happens or not.</p>
<p>Update: a simple test showed that the number of points is not the same after cutting. It really would help if you’d illustrate your application. Thanks</p>

---

## Post #5 by @evaherbst (2024-11-11 14:43 UTC)

<p>Thanks for running some tests.<br>
I just replicated the issue.<br>
Here is the scapula model, curve cut, inside point, resulting surface mesh (glenoid):</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1j70ZADmvxSvkJEm2jxyhJk3CLTfZD_km/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1j70ZADmvxSvkJEm2jxyhJk3CLTfZD_km/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1j70ZADmvxSvkJEm2jxyhJk3CLTfZD_km/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1j70ZADmvxSvkJEm2jxyhJk3CLTfZD_km/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">troubleshooting_pointNum_curveCut.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I also tested cleaning the scap input mesh for the curve cut first, still did not fix it.<br>
Thank you very much,<br>
Eva</p>

---

## Post #6 by @Sunderlandkyl (2024-11-11 15:24 UTC)

<p>The same behavior happens with plane cut. All of the the points were left as-is to preserve point IDs: <a href="https://discourse.slicer.org/t/dynamic-modeler-plane-cut-type-affecting-number-of-points-in-output-models/30915/3" class="inline-onebox">Dynamic modeler plane cut type affecting number of points in output models - #3 by lassoan</a></p>
<p>Closed PR here: <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/60" class="inline-onebox" rel="noopener nofollow ugc">BUG: Remove unused points during plane cut by Sunderlandkyl · Pull Request #60 · Slicer/SlicerSurfaceToolbox · GitHub</a></p>
<p>We decided to leave the behavior as it was, but if it proves to be a problem then we can update it or add a flag to the relevant tools to clean the output.</p>

---

## Post #7 by @evaherbst (2024-11-11 15:30 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> thanks for the response!<br>
Makes sense that it is kept to preserve the same node IDs, but yes it does lead to unexpected behaviour if fitting spheres to the new surface, running SVD etc on it</p>
<p>It would be great to have an option in curveCut to specify if we want cleaning or not.</p>
<p>Thank you!<br>
Eva</p>

---

## Post #8 by @evaherbst (2024-11-11 15:42 UTC)

<p>Update:</p>
<p>I just uploaded a script to batch clean objects in a scene in case anyone has the same issue.<br>
Maybe it can also be incorporated into the Dynamic Modeler module if you do end up adding the cleaning option.<br>
<a href="https://github.com/evaherbst/slicerScripts/blob/e2059c62525ab24bbdc663259194ca0bb7be6486/cleanMeshesBatch.py" rel="noopener nofollow ugc">Script here</a></p>

---
