---
topic_id: 1154
title: "Odd Looking Hippocampus"
date: 2017-10-02
url: https://discourse.slicer.org/t/1154
---

# Odd looking hippocampus

**Topic ID**: 1154
**Date**: 2017-10-02
**URL**: https://discourse.slicer.org/t/odd-looking-hippocampus/1154

---

## Post #1 by @Olof (2017-10-02 13:22 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dcb8eabb369bad02d036d7b6da0a9b8ff84d00a.png" alt="Odd_loking_hippocampus" data-base62-sha1="b6cSQXmPeicBUUKf9MrBEYfZvDk" width="389" height="367"></p>
<p>HI Beatriz and Martin,</p>
<p>I am running the shape-tool and I get very odd looking hippocampus after running the shapeanalysis Mancova wizard.</p>
<p>I have no clue what is going on. I am converting the _hippocampus_left_roi_pp_surf_SPHARM.vtk files to meta. And run the analysis.</p>
<p>I looked at the individual  *_hippocampus_left_roi_pp_surf_SPHARM.vtk in the population viewer … and they look fine</p>
<p>Do you have a clue?</p>
<p>best<br>
Olof</p>

---

## Post #2 by @bpaniagua (2017-10-02 13:36 UTC)

<p>Hi Olof,</p>
<p>Have you done QC of the spharm meshes? SAM generates an average mesh where all scalar values are added that will not provide useful results unless all of the source meshes have the same orientation.</p>
<p>Bea</p>

---

## Post #3 by @Olof (2017-10-02 13:49 UTC)

<p>Well,<br>
before, in the old version, you taught me to use the proctalign version of the output … but this image seems not to be available running the new tool …   Or am I running with wrong parameters?</p>
<p>best<br>
Olof</p>

---

## Post #4 by @bpaniagua (2017-10-06 12:28 UTC)

<p>Hi Olof,</p>
<p>Yes, the procrustes aligned meshes would be the best choice to look at shape changes, procalign files are generated when the reg-template option is set up in the new GUI. I just wanted to bring up that if parameterization of the SPHARM mesh is incorrect the procrustes alignment will not work.</p>
<p>Thanks!<br>
Bea</p>

---
