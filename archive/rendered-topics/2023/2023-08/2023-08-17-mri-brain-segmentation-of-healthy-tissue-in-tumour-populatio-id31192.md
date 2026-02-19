---
topic_id: 31192
title: "Mri Brain Segmentation Of Healthy Tissue In Tumour Populatio"
date: 2023-08-17
url: https://discourse.slicer.org/t/31192
---

# MRI Brain segmentation of healthy tissue in tumour population

**Topic ID**: 31192
**Date**: 2023-08-17
**URL**: https://discourse.slicer.org/t/mri-brain-segmentation-of-healthy-tissue-in-tumour-population/31192

---

## Post #1 by @e0032127 (2023-08-17 07:56 UTC)

<p>Hello everyone! I’m new to the 3D slicer community!</p>
<p>As I’m trying out 3D slicer for the first time, I’m wondering if anyone knows of any pipelines for segmenting specific regions of the brain i.e. wm, gm and hippocampus</p>
<p>I’ve heard of FSL, freesurfer but would anyone be able to explain what the adv or disadv for each software?</p>

---

## Post #2 by @ebrahim (2023-08-17 13:31 UTC)

<p>They focus on different things. FSL is good at working with volumes while FreeSurfer has the goal of generating surfaces out of your volumes and then processing those surfaces. It’s very common to use both if your pipeline needs both of those aspects.</p>
<p>In FSL you have <a href="https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FAST" rel="noopener nofollow ugc">FAST</a> which does tissue type segmentation like you are looking for. There are also various approaches <a href="https://antspyx.readthedocs.io/en/latest/segmentation.html" rel="noopener nofollow ugc">in ANTs</a>.</p>
<p>For hippocampus you can look for tools that focus on segmentation of subcortical structures. I never used these, but just looking it up: (a) <a href="https://freesurfer.net/fswiki/SubcorticalSegmentation" rel="noopener nofollow ugc">Freesurfer includes it</a> as part of its main pipeline and (b) there is <a href="https://web.mit.edu/fsl_v5.0.10/fsl/doc/wiki/FIRST(2f)StepByStep.html" rel="noopener nofollow ugc">FSL FIRST</a></p>

---

## Post #3 by @e0032127 (2023-08-18 03:47 UTC)

<p>Hi Ebrahim,</p>
<p>Appreciate your replies. Thank you for pointing me to resources (may look at how FSL works!), will take the time to look through them <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>regards,<br>
jin</p>

---
