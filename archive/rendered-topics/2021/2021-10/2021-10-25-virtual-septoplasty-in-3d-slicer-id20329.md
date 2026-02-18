# Virtual septoplasty in 3D slicer

**Topic ID**: 20329
**Date**: 2021-10-25
**URL**: https://discourse.slicer.org/t/virtual-septoplasty-in-3d-slicer/20329

---

## Post #1 by @Sliceeeeee (2021-10-25 05:24 UTC)

<p>i am going to make 3D model of nasal airway with 3D slicer ,but from a data of nasal septum deviation i want to make a corrected nasal airway by virtual septoplasty , how i can do that in 3D slicer ?</p>

---

## Post #2 by @caioath (2021-10-26 02:09 UTC)

<p>That might be hard because the septal deviation is only part of the asymmetry.</p>
<p>You may be able to erase the septum through segmenting it and masking the volume with air intensity. Then you create a new septum (again through segmentation + mask volume). But you will probably face difficulties in creating the new (straight) nasal septum because the turbinates and other structures might be in your way.</p>

---

## Post #3 by @lassoan (2021-10-26 14:06 UTC)

<p>You can use landmark-based warping to simulate soft-tissue deformations using Fiducial Registration Wizard. You can specify non-deforming regions and points that are displaced and the module computes a smooth displacement field. See step-by-step instructions in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="GfDDQykH1iY" data-video-title="Soft tissue deformation simulation" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=GfDDQykH1iY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/GfDDQykH1iY/maxresdefault.jpg" title="Soft tissue deformation simulation" width="" height="">
  </a>
</div>


---

## Post #4 by @caioath (2021-10-26 18:54 UTC)

<p>That is amazing. Thanks!<br>
Will try on my dataset.</p>

---

## Post #5 by @Sliceeeeee (2021-10-27 00:56 UTC)

<p>Thank you very much, I will try this method</p>

---

## Post #6 by @Sliceeeeee (2021-10-28 15:07 UTC)

<p>is it possible to reduce septal thickness?</p>

---

## Post #7 by @lassoan (2021-10-28 15:09 UTC)

<p>Yes, you can do that by placing two series of points along the septum (on both sides). If you move those points closer to each other then the septal thickness will be reduced.</p>

---

## Post #8 by @Sliceeeeee (2021-10-29 00:36 UTC)

<p>Thanks a lot for your answer .</p>
<p>is there any method where i can compare with the dimension of healthy septum and will reduce thickness whenever there is a deviation from healthy one? can i do it simultaneosly in 3d slicer?</p>

---

## Post #9 by @lassoan (2021-10-29 02:42 UTC)

<p>You can use markups module’s line tool or specialized extensions (such as BoneThicknessMapping) or custom scripts to measure bone thickness. If you know what is the healthy thickness value then you can use that to compute how much closer you need to move the control points to each other.</p>

---

## Post #10 by @Sliceeeeee (2021-11-01 09:30 UTC)

<p>In line tool how can i ensure that whatever line i am drawing is a perfect horizontal line?</p>

---

## Post #11 by @lassoan (2021-11-11 06:02 UTC)

<p>There is no such constraint during point placement, but after you have placed the line endpoints you can go to Markups module / Control points and copy-paste the coordinate values to force points to be on the same slice or line. If you need this frequently then you can automate this using a few lines of Python code.</p>

---

## Post #12 by @Sliceeeeee (2021-11-11 13:45 UTC)

<p>Hello , Is there any method where I can export STL file from 3D slicer and process it in other software and again import to 3D slicer?</p>

---

## Post #13 by @lassoan (2021-11-11 17:17 UTC)

<p>Yes, you can save and load STL files in Slicer. Slicer has also a number of segment and surface editing tools. What editing operations would you like to do in the external software?</p>

---

## Post #14 by @Sliceeeeee (2021-11-11 17:20 UTC)

<p>Filling some holes , separating the regions for giving inlet ,outlet boundary conditions as As STL becomes a single file it is difficult to separate it</p>

---

## Post #15 by @lassoan (2021-11-11 18:49 UTC)

<p>Filling some holes and maybe also adding inlet/outlet extensions are in Slicer’s scope. You may also generate the volumetric mesh from the segments in Slicer (using SegmentMesher extension).</p>
<p>Then, you use your the FEM modeler’s preprocessing software to specify boundary conditions, loads, material properties, and run the simulation.</p>
<p>You can then load the simulation results (meshes with computed displacements, stresses, etc.) in Slicer for visualization.</p>

---

## Post #16 by @Sliceeeeee (2021-11-11 18:52 UTC)

<p>How can I give in let outlet in slicer ?If any such tutorials are there please tell.</p>
<p>Thanks</p>

---

## Post #17 by @lassoan (2021-11-11 18:55 UTC)

<p>Do you mean how to add inlet and outlet extensions? You can use “Draw Tube” effect in Segment Editor for this (provided by SegmentEditorExtraEffects extension).</p>

---

## Post #18 by @Sliceeeeee (2021-11-12 05:52 UTC)

<p>When I am using draw tube effect, my original segment is being erased , how to handle it?</p>

---

## Post #19 by @lassoan (2021-11-12 05:57 UTC)

<p>You can add flow extensions as separate segments and when everything looks good then you can combine segments using “Logical operators” effect.</p>

---

## Post #20 by @Sliceeeeee (2021-11-12 06:20 UTC)

<p>Thank you for your reply , But again I have to make that tube hollow? For air flow simulation?</p>

---

## Post #21 by @lassoan (2021-11-12 06:23 UTC)

<p>For air flow simulation you probably need to create a volumetric mesh of the air, for example using SegmentMesher extension.</p>

---

## Post #22 by @Sliceeeeee (2021-11-12 06:40 UTC)

<p>So I shouldn’t add tube ? I have made 3D model of nasal airways , but it is not hollow, Then what should i do?</p>

---

## Post #23 by @lassoan (2021-11-12 16:45 UTC)

<p>If the goal is air flow simulation then segments must be solid (appear solid in slice views), because that is your simulation domain. You can export the segment either as a surface mesh (that is inherently hollow inside) or as a volumetric mesh (created by SegmentMesher extension).</p>
<p>What FEM software are you using? What input meshes can it accept?</p>

---

## Post #24 by @Sliceeeeee (2021-11-12 17:26 UTC)

<p>I am using Ansys CFD software , for simulation purposes, Yes Ansys can import STL file , but how can I select different regions for boundary condition that is the main concern, Because it is difficult to select separately different regions in STL file</p>

---

## Post #25 by @lassoan (2021-11-14 20:56 UTC)

<p>You can use the Dynamic modeler module to select or cut out a region from meshes. You can save selection scalars in vtk, vtp, and maybe in ply format, but Ansys most likely cannot import the scalars. So, probably the best is to save each region as separate mesh file.</p>
<p>You can then use various tools in Ansys to set the geometry, boundary conditions, loads. If nobody volunteers to describe the details here then you can ask on Ansys forums.</p>

---

## Post #26 by @lassoan (2021-11-23 18:33 UTC)

<p>4 posts were merged into an existing topic: <a href="/t/how-to-create-a-zero-thickness-plane-in-3d-slicer/20743/4">How to Create a zero thickness plane in 3D slicer?</a></p>

---

## Post #27 by @Sliceeeeee (2022-02-23 07:50 UTC)

<p>Hello sir</p>
<p>I have some doubts regarding soft tissue deformation , when I am going to fiducial registration wizard and adding some points  then performing deformation but when I am going to other coronal sections and adding some other sets of points for performing deformation then my previous deformation is getting lost (moving back to the original ) What to do in such cases ?Please help</p>

---
