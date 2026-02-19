---
topic_id: 8372
title: "Lab And Lecture Materials From First 3D Imaging And Morphome"
date: 2019-09-10
url: https://discourse.slicer.org/t/8372
---

# Lab and lecture materials from first 3D imaging and morphometrics workshops for SlicerMorph

**Topic ID**: 8372
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/lab-and-lecture-materials-from-first-3d-imaging-and-morphometrics-workshops-for-slicermorph/8372

---

## Post #1 by @muratmaga (2019-09-10 20:09 UTC)

<p>It is available at: <a href="https://github.com/SlicerMorph/S_2019" rel="nofollow noopener">https://github.com/SlicerMorph/S_2019</a><br>
Materials in Labs 2-6 might be useful for people who wants to start with 3D Slicer (and in particular working with non-medical CT datasets).</p>

---

## Post #2 by @stevenagl12 (2019-11-13 19:20 UTC)

<p>Quick question about the tutorials. It mentions that you can select a model for the 3D visualization, but do you select one at random and it creates the 3D model based off from it (and allows you to warp that model), or do you have to somehow create a mean model?</p>

---

## Post #3 by @smrolfe (2019-11-13 22:46 UTC)

<p>You can load either a mean model or a representative sample for the 3D visualization. It will be warped to the mean shape in the “Set up for Visualization” step.</p>

---

## Post #4 by @stevenagl12 (2019-11-14 11:23 UTC)

<p>Do you know if slicer has a way of importing statistical shape models (.h5 files). Or will that ever be a part of slicermorph? Also, will there be registration parameters for mesh registration for example using parametric non-rigid registration, iterative closest point, or coherent point drift?</p>

---

## Post #5 by @stevenagl12 (2019-11-14 11:25 UTC)

<p>Also, how would you create a mean model for the use for visualization in this case?</p>

---

## Post #6 by @muratmaga (2019-11-14 19:03 UTC)

<p>There is currently no support of mean model creation with SlicerMorph without using landmarks. Depending on your needs you can do couple things.</p>
<ul>
<li>If you want to visualize shape PCAs, you can select the sample closest to the mean shape and use that as reference. SlicerMorph will report the sample closest to the mean in the Python window, or you can use the procrustes distance table to identify the sample. GPA module will take that reference model, and use landmark based TPS deformation to create a mean mesh. You can export that if you like, however know that due to the scaling step in Procrustes, the coordinates will not be in the original space (you can skip that step if you want to preserve scale).</li>
<li>If you want landmark-free correspondence you will have to turn to registration-based pipelines. What you do with them will depend on the modality of your data. You need to use surface registration techniques with models (I believe SlicerSalt has that), and volumetric registration (like Brains, Elastix) for CT and such. In all cases you need to choose a sample to initiate the registration process, where everything else will be registered against, and then you typically average all the samples and apply some filters to deal with the fuzziness in the resultant template. However, initial template selection is an important step, and can skew your results. Most template building pipelines that I am aware of will start with an initial guess (e.g., linear average of all samples), and iterate over the result.</li>
</ul>
<p>For volumetric data, I would suggest you try the antsMultivariateTemplateConstruction.sh from ANTs library (<a href="https://github.com/ANTsX/ANTs/blob/master/Scripts/antsMultivariateTemplateConstruction.sh" rel="nofollow noopener">https://github.com/ANTsX/ANTs/blob/master/Scripts/antsMultivariateTemplateConstruction.sh</a>)</p>
<p>This is not available in Slicer, you will have to build ANTs on your own.</p>

---
