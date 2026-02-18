# Cardiac CT and CMR postprocessing

**Topic ID**: 30222
**Date**: 2023-06-25
**URL**: https://discourse.slicer.org/t/cardiac-ct-and-cmr-postprocessing/30222

---

## Post #1 by @Villurca (2023-06-25 15:54 UTC)

<p>&lt;I need to CPR coronary arteries for evaluation grade stenosis Agatson coronay score and 3D VRI. In VR the tools no working (scissors and so on) with python console filling a lot of error of any tool. I want to know how to do them Thank you</p>

---

## Post #2 by @lassoan (2023-06-25 17:12 UTC)

<p>Agatston scoring: <a class="mention" href="/u/curtislisle">@curtislisle</a> offered to put the computation script into an easy-to-use Slicer module - see details <a href="https://discourse.slicer.org/t/cardiac-agatston-scoring-module/1544/25">here</a></p>
<p>I don’t know what you mean by “3D VRI”. Some kind of volume rendering, or virtual reality, or something else?</p>
<blockquote>
<p>In VR the tools no working</p>
</blockquote>
<p>Do you mean virtual reality or volume rendering?</p>
<p>Could you describe what you did, what you expected to happen, and what happened instead?</p>
<hr>
<p>Maybe instead of answering very specific questions, it could be better if you described your clinical end goal and then we would tell how to accomplish those in Slicer.</p>

---

## Post #3 by @Villurca (2023-06-27 00:49 UTC)

<p>I mean Curved Planar Reformation (CPR) of coronary arteries. CPR evaluation of pat calicum and stenosis coronary artery stenosis percentage and corfirm coronary artery disease and further coronary cathterization<br>
I mean 3D VRI, 3D Volumen Rendering Images. Specially for coronary arteries paths regarde to CPR and anomlous coronoary origins, pulmonary veins paths, dimesions of lumen, left atrial appendage and trunk previous Ablation in patients with Atrial Fibrilaltion, Double oblique of Left ventricle outlet tract to anlize aortic annulus for TAVI procedures. Thank you for your answuer. Regards</p>

---

## Post #4 by @lassoan (2023-06-27 02:36 UTC)

<p><a href="https://github.com/PerkLab/SlicerSandbox/tree/master#curved-planar-reformat">Curved Planar Reformat module</a> is available in Sandbox extension.</p>
<p>Volume rendering is provided by <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html">Volume rendering module</a>.</p>
<p><a href="https://github.com/SlicerHeart/SlicerHeart#slicerheart-extension-for-3d-slicer">SlicerHeart extension</a> contains modules for cardiac device placement analysis, such as assessment of Harmony device in the left ventricular outflow tract. We also have work-in-progress modules, such as for coronary artery compression analysis for right ventricular outflow tract devices.</p>

---

## Post #5 by @Villurca (2023-07-28 13:12 UTC)

<p>Thank your for your instructions but nothing works. I am cardiologist looking for a appropiate post processing MSCT system. I ussually have many problems with errors and errors. Slicer 3D must go for a long way to be friendly for end users. Good bye</p>

---
