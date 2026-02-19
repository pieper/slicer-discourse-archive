---
topic_id: 31070
title: "Landmarks Model"
date: 2023-08-09
url: https://discourse.slicer.org/t/31070
---

# Landmarks - model

**Topic ID**: 31070
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/landmarks-model/31070

---

## Post #1 by @Vignesh_Chakravarthy (2023-08-09 16:38 UTC)

<p>Hi,</p>
<p>Is there any particular tool available to automatically generate landmarks based on 3d model. I want to create landmarks to use it in ALPACA module for registration. Please help me.</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2023-08-09 16:44 UTC)

<p>PseudoLMGenerator in SlicerMorph will allow you uniformly sample pseudolandmarks from a 3D model.</p>

---

## Post #3 by @Vignesh_Chakravarthy (2023-08-10 15:12 UTC)

<p>Thanks Murat for the information. Please let me know if models could be deformably registered using Slicer.</p>

---

## Post #4 by @muratmaga (2023-08-10 15:21 UTC)

<p>Models can be registered deformably using Slicer, but I am not sure if there is any user facing module that actually does that. <code>Model Registration</code> does rigid, iterative closest point.</p>
<p>We have recently implemented <code>Fast Model Align</code> in SlicerMorph to do rigid and affine registration, and the module can be expanded to do the deformable registration via coherent point drift, but we do not have time to implement it. Is this something you would be interested in contributing?</p>

---

## Post #5 by @Vignesh_Chakravarthy (2023-08-16 15:37 UTC)

<p>Hi Murat,</p>
<p>Thanks for the clarification. I am beginner with registration techniques and  I hope I can implement that in upcoming days.</p>
<p>Thanks,<br>
Vignesh</p>

---
