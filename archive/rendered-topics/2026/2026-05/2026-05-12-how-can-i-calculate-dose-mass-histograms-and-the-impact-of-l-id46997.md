---
topic_id: 46997
title: "How can I calculate dose-mass histograms and the impact of lung expansion"
date: 2026-05-12
url: https://discourse.slicer.org/t/46997
last_bumped: 2026-06-02T11:56:56.194Z
---

# How can I calculate dose-mass histograms and the impact of lung expansion

**Topic ID**: 46997
**Date**: 2026-05-12
**URL**: https://discourse.slicer.org/t/how-can-i-calculate-dose-mass-histograms-and-the-impact-of-lung-expansion/46997

---

## Post #1 by @zahra_Tabasi (2026-05-12 18:44 UTC)

<p>Hello everyone,</p>
<p>I am currently working on a research project involving unilateral left-sided breast cancer patients undergoing radiotherapy. My study compares Free Breathing (FB) and Deep Inspiration Breath Hold (DIBH) CT datasets, with the goal of evaluating anatomical displacement and lung expansion between the two breathing conditions.</p>
<p>I recently studied the following paper:</p>
<p>“Deep inspiration breath-hold for left-sided breast irradiation: Analysis of dose-mass histograms and the impact of lung expansion”</p>
<p>I would like to reproduce some parts of the image analysis workflow described in this study using 3D Slicer version 5.10.0, and I would greatly appreciate detailed guidance.</p>
<p>In this paper, the authors:</p>
<ul>
<li>
<p>Acquired FB and DIBH CT datasets for left-sided breast cancer patients</p>
</li>
<li>
<p>Contoured lungs, heart, and target volumes</p>
</li>
<li>
<p>Performed deformable image registration between FB and DIBH images</p>
</li>
<li>
<p>Used B-Spline deformable registration via Plastimatch</p>
</li>
<li>
<p>Generated deformation vector fields (DVFs)</p>
</li>
<li>
<p>Evaluated lung expansion using the mean values of the DVF in left, anterior, and caudal directions</p>
</li>
<li>
<p>Calculated 3D expansion using the mean displacement in all three directions</p>
</li>
<li>
<p>Visually inspected the deformation results by overlaying CT images and DVFs in 3D Slicer</p>
</li>
</ul>
<p>My goal is to understand how similar analyses can be performed inside 3D Slicer 5.10.0, especially because some extensions mentioned in older workflows (such as Plastimatch or QARegistration) are not available in the current Extension Manager.</p>
<p>I would really appreciate step-by-step beginner-friendly guidance regarding the following questions:</p>
<ol>
<li>
<p>How can deformable image registration between FB and DIBH CT datasets be performed in 3D Slicer 5.10.0?</p>
</li>
<li>
<p>Which currently supported modules or extensions are recommended for generating deformation vector fields (DVFs)?</p>
</li>
<li>
<p>How can displacement vector fields of the lungs or heart be calculated and exported?</p>
</li>
<li>
<p>How can the mean displacement of the lung in left-right, anterior-posterior, and superior-inferior (cranial-caudal) directions be measured from the DVF?</p>
</li>
<li>
<p>How can overall 3D lung expansion magnitude be calculated from these directional displacement values?</p>
</li>
<li>
<p>How can DVFs be visualized in 2D and 3D views inside Slicer?</p>
<ul>
<li>
<p>vector arrows</p>
</li>
<li>
<p>color maps</p>
</li>
<li>
<p>deformation grids</p>
</li>
<li>
<p>overlay of FB and DIBH images</p>
</li>
</ul>
</li>
<li>
<p>Is there a recommended workflow in Slicer for separating lung and non-lung tissue before deformable registration, similar to the workflow described in the paper?</p>
</li>
<li>
<p>If Plastimatch is no longer available in Slicer 5.10.0, what is the best currently supported alternative for B-Spline deformable registration?</p>
</li>
</ol>
<p>My objective is to reproduce a similar workflow for evaluating respiratory-induced anatomical changes between FB and DIBH in my own study.</p>
<p>I am a student and still a beginner in working with 3D Slicer software. Therefore, I would highly appreciate detailed and beginner-friendly explanations, including module names, extension names, and step-by-step instructions whenever possible.</p>
<p>Thank you very much for your time and help.</p>

---

## Post #2 by @ThomasVanParys (2026-05-14 13:05 UTC)

<p>I may be wrong, but could you use <code>SlicerElastix</code>? Select the Fixed Volume as the FB CT set and Moving Volume as the DIBH CT set. The following Output Volume and create a new Transform node. The resulting Transform should be your DVF… calculating DVF you could navigate to the Transforms module and Convert it, and export the resulting output as a Disaplacement Field.. X,Y,Z data could be extracted from that using the Vector to Scalar Volume module?</p>

---

## Post #3 by @cpinter (2026-06-02 11:56 UTC)

<aside class="quote no-group" data-username="zahra_Tabasi" data-post="1" data-topic="46997">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/zahra_tabasi/48/81718_2.png" class="avatar"> zahra_Tabasi:</div>
<blockquote>
<p>some extensions mentioned in older workflows (such as Plastimatch or QARegistration)</p>
</blockquote>
</aside>
<p>I’m not sure about QARegistration, but the Plastimatch modules are in the SlicerRT extension, which is available.</p>
<p>Also I agree with the previous answer that Elastix could be a good way to do the registration, as I think it is the most powerful image registration method in Slicer.</p>
<p>Happy to answer questions one by one as you proceed with the registration.</p>
<p>(Sorry for the delay, had this thread saved for weeks but just had the oportunity to look at it in more detail)</p>

---
