---
topic_id: 1122
title: "Shape Analysis Between Non Similar Objects"
date: 2017-09-26
url: https://discourse.slicer.org/t/1122
---

# Shape analysis between non-similar objects?

**Topic ID**: 1122
**Date**: 2017-09-26
**URL**: https://discourse.slicer.org/t/shape-analysis-between-non-similar-objects/1122

---

## Post #1 by @shahrokh (2017-09-26 14:25 UTC)

<p>Dear SPHARM and SlicerSALT developers and users</p>
<p>Hi, I have some problems about shape analysis between non-similar objects. Suppose I have 5 groups with names A, B, C, D and E and in each group there are 8 meat samples such as below:</p>
<p>A1, A2, A3, A4, A5, A6, A7, A8</p>
<p>B1, B2, B3, B4, B5, B6, B7, B8</p>
<p>C1, C2, C3, C4, C5, C6, C7, C8</p>
<p>D1, D2, D3, D4, D5, D6, D7, D8</p>
<p>E1, E2, E3, E4, E5, E6, E7, E8</p>
<p>Each group was subjected to different laboratory procedures (physicochemical methods) and these procedures had a significant effect on the surface of the samples.</p>
<p>I should point out that the cutting of meat samples has been carried out manually. Although I tried to be careful enough, this led to a significant difference in the shape and size of meat samples (due to the non-rigidity of meat samples).</p>
<p>After completing these steps, MRI images with T2 contrast were acquired. Although I have downloaded and installed SlicerSALT, but I’ve done the Preprocessing, Parameterization, and SPHARM-PDM steps with the Shape Analysis Module in Slicer.</p>
<p>At now, my question is how can I do a surface analysis on them, without considering the overall shape of the meat samples and their volume?</p>
<p>As mentioned above, three steps of Preprocessing, Parameterization and SPHARM-PDM were performed completely with the Shape Analysis Module in Slicer. For example, I’ve got the output files for one meat sample in the following steps:</p>
<p>in <strong>Step1</strong>_SegPostProcess: sample1_group04_pp.nii</p>
<p>in <strong>Step2</strong>_GenParaMesh: sample1_group04_pp_para.vtk,<br>
sample1_group04_pp_surf.vtk, sample1_group05_pp_para.vtk, sample1_group05_pp_surf.vtk, sample1_group06_pp_para.vtk, sample1_group06_pp_surf.vtk</p>
<p>in <strong>Step3</strong>_ParaToSPHARMMesh:<br>
sample1_group04_pp_surf_MedialAxisScalars.csv, sample1_group04_pp_surf_para.vtk, sample1_group04_pp_surf_paraMix.txt, sample1_group04_pp_surf_paraPhi.txt, sample1_group04_pp_surf_paraPhiHalf.txt, sample1_group04_pp_surf_paraTheta.txt, sample1_group04_pp_surf_SPHARM.coef, sample1_group04_pp_surf_SPHARM.vtk, sample1_group04_pp_surf_SPHARM_ellalign.coef, sample1_group04_pp_surf_SPHARM_ellalign.vtk, sample1_group04_pp_surf_SPHARMMedialAxis.vtk, sample1_group05_pp_surf_MedialAxisScalars.csv, sample1_group05_pp_surf_para.vtk, sample1_group05_pp_surf_paraMix.txt, sample1_group05_pp_surf_paraPhi.txt, sample1_group05_pp_surf_paraPhiHalf.txt, sample1_group05_pp_surf_paraTheta.txt, sample1_group05_pp_surf_SPHARM.coef,<br>
sample1_group05_pp_surf_SPHARM.vtk, sample1_group05_pp_surf_SPHARM_ellalign.coef, sample1_group05_pp_surf_SPHARM_ellalign.vtk, sample1_group05_pp_surf_SPHARMMedialAxis.vtk, sample1_group06_pp_surf_MedialAxisScalars.csv, sample1_group06_pp_surf_para.vtk, sample1_group06_pp_surf_paraMix.txt, sample1_group06_pp_surf_paraPhi.txt, sample1_group06_pp_surf_paraPhiHalf.txt, sample1_group06_pp_surf_paraTheta.txt, sample1_group06_pp_surf_SPHARM.coef, sample1_group06_pp_surf_SPHARM.vtk, sample1_group06_pp_surf_SPHARM_ellalign.coef, sample1_group06_pp_surf_SPHARM_ellalign.vtk, sample1_group06_pp_surf_SPHARMMedialAxis.vtk</p>
<p>The solution to my mind for this analysis is to use Parameterization outputs, especially Parameterization spheres. Is it true? Since I think that mapping the surface mesh of each sample onto a unit sphere causes the  surface analysis between samples to be independent of the radius and geometric shapes of samples, and analysis is done on characteristics and surface differences (such as roughness and smoothness).  Is that true? In  other words, can surface analysis be done using these unit spheres? Because, in my opinion, the quantities on these unit spheres represent the amplitude of the three-dimensional frequency signal of the sample surface.  Is it OK?</p>
<p>My next question starts with the fact that, as I pointed out above, meat samples that are inside a group, although they look different in terms of geometric shape, but they are similar in appearance and surface  characteristics. I must mentioned that if I put all the meat samples (8 * 5 = 40) inside a container, they can be distinguished only by their surface properties. At now, my question is that: Can we create an average  surface using SPHARM for each group and consider it as representative of that group and then compare the surfaces between these representatives?</p>
<p>I am very interested in the topic of Shape Analysis using SPHARM method. I think it’s possible to use this method to compare the surfaces of non-similar objects in the Fourier domain.</p>
<p>Please guide me to do it.</p>
<p>Thanks a lot.</p>
<p>Shahrokh.</p>

---

## Post #2 by @shahrokh (2017-09-29 13:04 UTC)

<p>Hi dear SlicerSALT and spharm developers and users</p>
<p>Unfortunately, I did not receive any feedbacks. Perhaps, my questions are likely to be very preliminary; however, I really hope you help me to understand of basic concepts about spharm and working with SPHARM correctly and scientifically.<br>
I’m waiting for your guidance.</p>
<p>Thanks a lot.<br>
Shahrokh</p>

---

## Post #3 by @bpaniagua (2017-09-29 13:33 UTC)

<p>Hi Shahrokh,</p>
<p>Your email is really complete, thanks for explaining. There are several things that you have to consider before considering any analysis schemes for your data.</p>
<ol>
<li>
<p>Have you checked if correspondence is good across all meat samples? It is important to check the quality of the sampling of your SPHARM meshes moving forward. The SPHARM tutorial includes information on <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Doc/SPHARM-PDM-Tutorial.pdf">how to QC your SPHARM computed meshes</a>. Basically involves visualizing parameterization color maps (ParaPhi or ParaTheta) in Shape Population Viewer and making sure all colors match correspondent areas.</p>
</li>
<li>
<p>Once you confirm everything is fine you can compute averages across groups and compare them or use shape classification methods.</p>
</li>
</ol>
<p>Thank you,<br>
Bea</p>
<p>ps. There is a great tutorial to learn the basics of SPHARM <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Doc/SPHARM-PDM-Tutorial.pdf">here</a>.</p>

---

## Post #4 by @shahrokh (2017-09-30 07:17 UTC)

<p>Hi Beatriz</p>
<p>Thank you very much for the explanations and preconditions that I should consider. I do steps that you mentioned.</p>
<p>Shahrokh</p>

---

## Post #5 by @bpaniagua (2017-10-02 12:43 UTC)

<p>Please, let us know when the QC step is complete and we will try to help a bit further.<br>
Thank you!</p>
<p>Bea</p>

---
