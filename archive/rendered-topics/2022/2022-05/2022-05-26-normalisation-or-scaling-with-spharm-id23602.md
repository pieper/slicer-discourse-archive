---
topic_id: 23602
title: "Normalisation Or Scaling With Spharm"
date: 2022-05-26
url: https://discourse.slicer.org/t/23602
---

# Normalisation or scaling with SPHARM

**Topic ID**: 23602
**Date**: 2022-05-26
**URL**: https://discourse.slicer.org/t/normalisation-or-scaling-with-spharm/23602

---

## Post #1 by @Khalid_Saifullah (2022-05-26 23:19 UTC)

<p>Hi,</p>
<p>I would like to normalise all of my SPHARM-PDM output subjects (subjectID_pp_surf_SPHARM_procalign.vtk) by a scale factor before running any sort of statistical analysis. I am going to use a separate tool for the statistical analysis, so I would just need the scaled SPHARM-PDM output for now. Could you let me know how I can do this, please?</p>
<p>Regards,<br>
Khalid</p>

---

## Post #2 by @Khalid_Saifullah (2022-05-31 00:53 UTC)

<p><a class="mention" href="/u/styner">@styner</a> Do you have the answer to this? Or could you point me to the right person?</p>

---

## Post #3 by @styner (2022-05-31 19:49 UTC)

<p>Hi Khalid<br>
I am not sure I fully understand what you are trying to do. Do you want to simply scale the size of the mesh by a given factor (which is simply multiplying all coordinates by the scale factor), or do you want to scale the mesh to have a particular size? In case of the former, you can use MeshMath with option scaleMesh<br>
Martin</p>

---

## Post #4 by @Khalid_Saifullah (2022-06-01 03:31 UTC)

<p>Hi Martin,</p>
<p>So, I need to normalize all of the subjects (subjectID_pp_surf_SPHARM_procalign.vtk) by their intra-cranial volume (scale factor). Then I would like to calculate the signed normal distance from the mean shape followed by statistical analysis (with a separate tool). Which one of the two would be appropriate for this?</p>
<p>Regards,<br>
Khalid</p>

---

## Post #5 by @styner (2022-06-01 17:45 UTC)

<p>This is scaling with a known scaling factor (in your case 1 /  ICV^(1./3) ) , so use MeshMath. As you can see from this formula, if you use a volume measure to scale meshes, you need to take the cubic root (as scaling affects coordinates in mm)</p>
<p>Martin</p>

---

## Post #6 by @Khalid_Saifullah (2022-06-09 19:59 UTC)

<p>Hi Martin,</p>
<p>The scale factor in your SPHARM-PDM framework paper suggests this formula:<br>
Scale Factor = Mean(ICV) ∕ (ICV_subject)^⅓</p>
<p>Is this what you are saying in the previous reply? Also, is there a recommendation for number of places after decimal?</p>
<p>PaperLink: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3062073/" class="inline-onebox" rel="noopener nofollow ugc">Framework for the Statistical Shape Analysis of Brain Structures using SPHARM-PDM - PMC</a></p>
<p>Regards,<br>
Khalid</p>

---

## Post #7 by @styner (2022-06-10 13:53 UTC)

<p>Slightly different:<br>
(Mean(ICV) ∕ ICV_subject)^⅓</p>

---

## Post #8 by @Khalid_Saifullah (2022-06-11 03:15 UTC)

<p>Hi Martin,</p>
<p>Thank you for taking the time in answering all the questions!</p>
<p>I see that once scaled, the subjects are no longer spatially aligned as they were in the subject_pp_surf_SPHARM_procalign.vtk files. How can I realign them again for the accurate distance calculation?</p>
<p>Regards,<br>
Khalid</p>

---

## Post #9 by @styner (2022-06-13 13:27 UTC)

<p>The change in alignment happens, as the data is rigid-procrustes aligned (procrustes without scale)  in image space (i.e. in the average location in image space, here the average hippocampus location). As you scale the size, this also changes the location in space.</p>
<p>In order for this not to happen, you could use an alignment to origin of coordinate system when the center of gravity/0th moment is (0,0,0).</p>
<p>Of course, you can do the rescaling in the image space, you just need to redo the alignment. As always there are multiple ways to do so, but I usually use MeshMath.</p>
<p>MeshMath RefMesh.vtk -alignMesh mesh1.vtk mesh2.vtk mesh3.vtk …</p>
<p>This does rigid procrustes, unless you also specify -scalingOn and then it does full procrustes.<br>
As reference mesh, you can use the average Mesh from before you did the rescaling. If you do not have that, you can compute an average Mesh with MeshMath and -avgMesh option. Btw, if you run MeshMath without any command line options, then it will give you an usage/help outout.</p>
<p>Martin</p>

---

## Post #10 by @Khalid_Saifullah (2022-08-30 07:05 UTC)

<p>Hi <a class="mention" href="/u/styner">@Styner</a>,</p>
<p>I wanted to asked you about the following two commands. How is the second command’s output different from that of the first one in terms of alignment? I know that the first one gives procrustes alignment and the second one gives a realignment but not sure if they are the same.</p>
<p>Command 1:<br>
ParaToSPHARMMeshCLP --NoParaAlign --paraOut --spharmDegree 15 --subdivLevel 10 --regTemplate template_pp_surf_SPHARM.vtk --regTemplateFileOn Step2_GenParaMesh/subject1_pp_para.vtk Step2_GenParaMesh/subject1_pp_surf.vtk Step3_ParaToSPHARMMesh/subject1_pp_surf</p>
<p>Command 2:<br>
MeshMath RefMesh.vtk -alignMesh mesh1.vtk mesh2.vtk mesh3.vtk …</p>
<p>Regards,<br>
Khalid Saifullah</p>

---
