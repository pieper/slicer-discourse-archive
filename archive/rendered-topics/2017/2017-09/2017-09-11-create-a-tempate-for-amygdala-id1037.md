# Create a tempate for amygdala

**Topic ID**: 1037
**Date**: 2017-09-11
**URL**: https://discourse.slicer.org/t/create-a-tempate-for-amygdala/1037

---

## Post #1 by @bpaniagua (2017-09-11 20:33 UTC)

<p>Hi Beatriz</p>
<p>I am a Msc student in Neuroscience in Ege University, Turkey. I am doing shape analysis for amygdala. I could not find a template for amygdala. So,I would like to create template.</p>
<p>I have 30 amygdala in my population. First I run all the steps in SPHARM-PDM (SegPostProcess, GenParaMesh and ParaToSPHARMMesh).</p>
<p>After SegPostProcess I end up having 30 *_SegPost.nii files.</p>
<p>After GenParaMesh I end up having 30 *_para.vtk and 30 *_surp.vtk files.</p>
<p>After ParaToSPHARMMesh I end up having 30 *_MedialAxisScalars.csv, 30 *_SPHARM.coef, 30 *_SPHARM.vtk, 30 *_SPHARM_ellalign.coef, 30 *_SPHARM_ellalign.vtk and 30 *_SPHARMMedialAxis.vtk files.</p>
<p>I need a regTemplate and a flipTemplate. How can I create these two templates and which outcome files can I use while creating these templates?</p>
<p>best regards,</p>
<p>Gozde Kizilates</p>

---

## Post #2 by @bpaniagua (2017-09-11 20:38 UTC)

<p>Hi Gozde,</p>
<p>Thank you for your email.</p>
<p>The choice of regTemplates and flipTemplates is up to you. Some people generate an average of the whole population after running the whole SPHARM-PDM pipeline once, some other people just randomly choose a single mesh of the population representative of the anatomy to be the regTemplate/flipTemplate.</p>
<p>For the flipTemplate is worth mentioning that <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SpharmPdm">the new SPHARM-PDM extension</a> now incorporates a module to do the flip of the parameterizations easily. Also, see the <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Doc/SPHARM-PDM-Tutorial.pdf">new documentation here</a>.</p>
<p>There is thread <a href="https://discourse.slicer.org/t/group-analysis-with-spharm-pdm/885">here</a> in which we discussed (among other things) how to create average meshes in SlicerSALT-SPHARM.</p>
<p>I hope this helps.<br>
Best,</p>
<p>Bea</p>

---
