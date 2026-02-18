# Scaling Model & Calculating transform

**Topic ID**: 7398
**Date**: 2019-07-03
**URL**: https://discourse.slicer.org/t/scaling-model-calculating-transform/7398

---

## Post #1 by @stevenagl12 (2019-07-03 15:59 UTC)

<p>Hi, I was wondering how you would go about changing the scale of an stl model in 3D slicer. Say you have two models from different species, and one is inherently smaller, but you don’t want the volume to impact analysis, how can you rescale it? In addition, what is the best method to show the transformation from one model to another if they are in alignment, for example looking at specific regions of the surface to show the deformation? Finally, can you calculate the magnitude of the Jacobian determinate from one model to another in 3D slicer to show how different two models are from each other, or the average distance between models as a single scalar value?</p>

---

## Post #2 by @pieper (2019-07-08 14:08 UTC)

<p>Hi - probably you want to look at <a href="https://slicermorph.github.io/" rel="nofollow noopener">SlicerMorph</a> and <a href="http://salt.slicer.org/" rel="nofollow noopener">SlicerSALT</a> for those kinds of operations.</p>

---

## Post #3 by @stevenagl12 (2019-07-08 19:15 UTC)

<p>How do you install SlicerMorph extensions in 3D Slicer? It seems like none of the modules are part of the extension manager?</p>

---

## Post #4 by @pieper (2019-07-08 19:54 UTC)

<p>SlicerMorph is new - it’s only available for the SlicerPreview version.</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> are there installation instructions that clarify this?</p>

---

## Post #5 by @smrolfe (2019-07-08 20:07 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, I will add installation instructions to clarify this.</p>

---

## Post #6 by @muratmaga (2019-07-09 12:23 UTC)

<p>If you do you a geometric analysis using landmarks, you can use SlicerMorph Generalized Procrustes Analysis which by default will conduct the superimposition in shape space (uniform scaling + rotation). I believe SlicerSALT always operates<br>
in the form space, thus skips the scaling step since physical size typically an important parameter in biomedical research to retain and relate back to condition being studied.</p>
<p>What you need is possibly a deformable registration framework, from which is you should be able calculate Jacobis by calculating the total warp field. I know ANTsR would do that from volumetric images, but I am not familiar with any pipeline<br>
that would do that for meshes.</p>
<p>One possibility may get you a little further is to convert the models to segments and then use segment registration to do an affine registration, and then visualize the remaining difference.</p>
<p>Mail](<a href="https://go.microsoft.com/fwlink/?LinkId=550986" rel="nofollow noopener">https://go.microsoft.com/fwlink/?LinkId=550986</a>) for Windows 10</p>

---

## Post #7 by @stevenagl12 (2019-08-19 13:03 UTC)

<p>Area there any documentation instructions now that are good for Slicer Morph?</p>

---

## Post #8 by @muratmaga (2019-08-21 03:09 UTC)

<p>We are working on finalizing the documentation. Meanwhile there are some videos that shows the existing functionality with the provided datasets.<br>
<a href="http://bit.ly/SM_youtube" class="onebox" target="_blank" rel="nofollow noopener">http://bit.ly/SM_youtube</a></p>
<p>In a nutshell, you need have a set of fiducial landmarks per sample (exact number of landmarks and in the same order) in a specified folder. FCSV is the only input format we currently support, so if you have landmarking done outside of Slicer, you need to convert your landmarks into <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Markups#File_Format" rel="nofollow noopener">fcsv format</a> first.</p>
<p>For 3D visualization of eigenvectors from PCA, you need to have a reference model, and a set of landmarks that goes with the model. Installing the SlicerMorph extension, and then downloading the sample datasets (mouse and gorilla) is the easiest way to start exploring.</p>

---
