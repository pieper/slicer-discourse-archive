# Combine two surface meshes and stitch edges

**Topic ID**: 39467
**Date**: 2024-10-01
**URL**: https://discourse.slicer.org/t/combine-two-surface-meshes-and-stitch-edges/39467

---

## Post #1 by @darabi (2024-10-01 08:45 UTC)

<p>Hello,<br>
I have two surfaces which are generated with a 3D scanner and registered using Fiducial Registration. Irrelevant parts of the scan are removed after registration by cutting along a manually placed curve on the surface of the two models.</p>
<p>Now, I would like to combine the two surfaces into a closed surface, by filling the holes which are created inevitably as the cut curves along the two different surfaces will always have some displacement.</p>
<p>I have tried ‘Combine Models’ but it ends with ‘[VTK] Contact ends suddenly.’ without creating a result for which I found this vtkbool issue: <a href="https://github.com/zippy84/vtkbool/issues/40" class="inline-onebox" rel="noopener nofollow ugc">Difference of meshes sometimes an empty mesh · Issue #40 · zippy84/vtkbool · GitHub</a>.</p>
<p>I hope that there is a way to achieve this without manual intervention as it is one step in a series of operations which are automated in a custom extension.</p>
<p>In the following screenshot, the blue and yellow surfaces are separated by gaps on the left side while they intersect on the right side:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca3c1b877dab12f6dc6957140ac40fb34d83a195.jpeg" data-download-href="/uploads/short-url/sR3ebDjUxeAARz7ZNMUitIqDKQt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca3c1b877dab12f6dc6957140ac40fb34d83a195_2_690x288.jpeg" alt="image" data-base62-sha1="sR3ebDjUxeAARz7ZNMUitIqDKQt" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca3c1b877dab12f6dc6957140ac40fb34d83a195_2_690x288.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca3c1b877dab12f6dc6957140ac40fb34d83a195_2_1035x432.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca3c1b877dab12f6dc6957140ac40fb34d83a195_2_1380x576.jpeg 2x" data-dominant-color="6D9394"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2169×906 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you</p>
<p>Kambiz</p>

---

## Post #2 by @cpinter (2024-10-01 08:55 UTC)

<p>It would be extremely difficult to automatically stitch the two surface patches correctly. I handle similar situations by voxelizing the appended mesh using a grid where the sampling direction is set such that it does not “flow out”, i.e. the sampling lines likely do not meet a hole between the patches. What this means is that I 1) append the meshes, 2) create a segmentation and set a reference geometry according to the desired voxelization directions, 3) import the mesh, 4) convert to binary labelmap representation.</p>

---

## Post #3 by @JASON (2024-10-02 02:40 UTC)

<p>You could try making a pointcloud from the vertices of both meshes and then mesh the pointcloud using something like this :</p>
<p><a href="https://examples.vtk.org/site/Cxx/Points/CompareExtractSurface/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://examples.vtk.org/site/Cxx/Points/CompareExtractSurface/</a></p>

---
