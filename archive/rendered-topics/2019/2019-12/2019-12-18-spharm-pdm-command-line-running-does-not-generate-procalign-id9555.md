---
topic_id: 9555
title: "Spharm Pdm Command Line Running Does Not Generate Procalign"
date: 2019-12-18
url: https://discourse.slicer.org/t/9555
---

# SPHARM-PDM command line running does not generate procalign files

**Topic ID**: 9555
**Date**: 2019-12-18
**URL**: https://discourse.slicer.org/t/spharm-pdm-command-line-running-does-not-generate-procalign-files/9555

---

## Post #1 by @Shane_TANG (2019-12-18 23:25 UTC)

<p>Hi all,</p>
<p>I am using command line to perform SPHARM-PDM. My command is shown below:<br>
<code>./SlicerSALT --no-main-window --python-script path-to-py path-to-param</code></p>
<p>And I have modified the <code>SPHARM-PDM-parameters.ini</code> file like this:<br>
<code>regparatemplatefileon = True</code><br>
<code>regparatemplate = ~/Step3_ParaToSPHARMMesh/L_Hippo_binary_pp_surf_SPHARM.vtk</code><br>
<code>fliptemplateon = True</code><br>
<code>fliptemplate = ~/Step3_ParaToSPHARMMesh/L_Hippo_binary_pp_surf_SPHARM.coef</code></p>
<p>But the output in <code>Step3_ParaToSPHARMMesh</code> folder does not contain *<strong>__pp_surf_SPHARM_procalign.vtk</strong> files.</p>
<p>Where did I go wrong?</p>
<p>Thanks!!</p>

---
