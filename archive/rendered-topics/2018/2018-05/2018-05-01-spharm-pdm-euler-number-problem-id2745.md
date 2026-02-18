# SPHARM-PDM Euler Number problem

**Topic ID**: 2745
**Date**: 2018-05-01
**URL**: https://discourse.slicer.org/t/spharm-pdm-euler-number-problem/2745

---

## Post #1 by @doganarda (2018-05-01 15:40 UTC)

<p>Hello everyone,</p>
<p>For my M.Sc. Thesis work, I need to apply SPHARM-PDM analysis to certain number of segmented hippocampi from an experiment but I am really new to the program and I still cannot make sense out of it clearly.</p>
<p>When I follow the tutorial, I open the Slicer 3D and I go to the Shape Analysis Model and I want to apply it to the segmented hippocampi mesh file .vtk (which is not empty, I can visualize it in MATLAB through trisurf command). It first converts it from mesh to label map (Step 0 folder is non-empty), then applies post process segmentation and I get the _pp file but on second step I get the following error:</p>
<p>itk::ExceptionObject (0x7ffeb221f1a0)<br>
Location: “Unknown”<br>
File: /home/kitware/Dashboards/Stable/S-481-E-b/SPHARM-PDM/Libraries/Shape/Algorithms/BinaryMask3DEqualAreaParametricMeshSource.txx<br>
Line: 183<br>
Description: Warning: Euler equation not satisfied. Euler Number : 781156 - 781156 = 0</p>
<p>and I don’t know where to look for the problem - I looked through many forum posts and could not find a similar problem. Is it because I am using .vtk file instead of .nii.gz or something similar, a label map? Which I highly doubt because the tutorial says that .vtk files are valid inputs. Is it because there is something wrong in the segmentation or in the settings I have?</p>
<p>I would appreciate any help, thanks in advance.<br>
Arda</p>

---

## Post #2 by @lassoan (2018-05-02 22:44 UTC)

<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> <a class="mention" href="/u/laurapascal">@laurapascal</a></p>

---

## Post #3 by @bpaniagua (2018-05-03 14:33 UTC)

<p>Hi Arda,</p>
<p>Have you visualized the topology of your VTK / nii.gz object? If the Euler Number is not satisfied that means the spherical topology required by SPHARM is not met.</p>
<p>More information on the Euler Number is here <a href="https://en.wikipedia.org/wiki/Euler_characteristic#Surfaces">https://en.wikipedia.org/wiki/Euler_characteristic#Surfaces</a></p>
<p>Thank you!<br>
Beatriz</p>

---

## Post #4 by @doganarda (2018-05-04 07:58 UTC)

<p>Hi Beatriz,</p>
<p>I do not know exactly what you mean by visualizing the topology but when I visualized the .vtk file it was a normal right hippocampus of one subject which was segmented with another program that I used couple of weeks ago, named FSL. Interesting thing is that the program also gives the masks for segmenting out the subcortical structure in NIFTI format, which are label maps (1 for the structure 0 for background) and when I used these files I did not have any problem with applying SPHARM-PDM analysis - there was no Euler number error, I was able to extract SPHARM parameters and visualize the images in the tutorial. Thus, I was really confused. I am not exactly sure if it would be the same analysis doing it through the masks rather than segmented subcortical structure but I would feel more secure if I was able to carry out the analysis through the meshed segmented file .vtk. Do you have any idea what might be the cause of that? Because the structure is the same structure (probably same topology) just different representations, one mesh and one label map. At the end of the day it might not be any problem (especially since I was able to get different SPHARM parameters for different subjects as expected) but I would like to figure out why .vtk mesh file raises the problem of Euler number.</p>
<p>Thank you for your help,<br>
Arda</p>

---

## Post #5 by @bpaniagua (2018-05-04 13:04 UTC)

<p>Hi Arda,</p>
<p>I apologize for this error!</p>
<p>I would double check the SegPostprocess output. It is possible that the scan conversion from VTK to binary label map is causing topology errors. This is a new feature in SPHARM-PDM and I would recommend looking at the label created after the conversion in the Step1_SegPostprocess folder to see if the VTK topology holds after scan conversion.</p>
<p>Thanks!<br>
Bea</p>

---

## Post #6 by @Hamed_RABIEI (2018-06-19 12:46 UTC)

<p>Hi,</p>
<p>I encountered the same problem for some triangulated mouse brain surfaces (Euler number = 0). I put here a heuristic solution that I found: I applied the “Close Holes” and “TwoStep Smooth” filters of MeshLab on problematic meshes and then the SPHARM worked properly. The intuition behind this idea is to close holes and refine the problematic regions by smoothing.</p>
<p>Hamed</p>
<p>P.S. I used PyMesh package to check whether a mesh is closed through the method mesh.is_closed(). (<a href="https://github.com/qnzhou/PyMesh" rel="nofollow noopener">https://github.com/qnzhou/PyMesh</a>)</p>

---

## Post #7 by @bpaniagua (2018-06-21 13:50 UTC)

<p>Hi Hamed,</p>
<p>This is great information, thank you so much!<br>
Best,</p>
<p>Beatriz</p>

---

## Post #8 by @debin_zeng (2020-09-02 09:08 UTC)

<p>Hi Hamed,</p>
<p>I also encountered the same problem for some binary segmented hippocampal image (voxel), how can i use this tool(MeshLab) to close holes in the voxel-image? Is there any other method to deal with this issue? Thank you very much!</p>
<p>Zeng</p>

---

## Post #9 by @Hamed_RABIEI (2020-09-04 15:41 UTC)

<p>Hi Zeng,</p>
<p>You can find the close hole tool in MeshLab (<a href="https://www.meshlab.net/" rel="nofollow noopener">https://www.meshlab.net/</a>) under the menu “Filters &gt; Remeshing, simplification and reconstruction &gt; Close holes”. I’ve never tried it for voxel-images but for triangulated mesh surfaces. I’m not aware of any other tool to fix this issue.</p>
<p>Best,<br>
Hamed</p>

---

## Post #10 by @yuanzhen_cui (2022-06-12 14:54 UTC)

<p>Hi Beatriz</p>
<p>I also encountered the same problems when I try to execute “GenParaMesh”:</p>
<p>GenParaMesh standard output:<br>
itk::ExceptionObject (0x304bef2f0)<br>
Location: “Unknown”<br>
File: /Volumes/D/S/S-1-E-b/SPHARM-PDM/Libraries/Shape/Algorithms/BinaryMask3DEqualAreaParametricMeshSource.txx<br>
Line: 183<br>
Description: Warning: Euler equation not satisfied. Euler Number : 158040 - 158032 = 8</p>
<p>So how can I get the right Euler Number and how to correct the Euler Number.</p>
<p>Thanks!<br>
Cui</p>

---
