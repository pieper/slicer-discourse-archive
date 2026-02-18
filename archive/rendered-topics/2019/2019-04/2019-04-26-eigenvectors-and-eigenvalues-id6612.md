# Eigenvectors and eigenvalues

**Topic ID**: 6612
**Date**: 2019-04-26
**URL**: https://discourse.slicer.org/t/eigenvectors-and-eigenvalues/6612

---

## Post #1 by @Ilaria_Cinelli (2019-04-26 02:25 UTC)

<p>I need to extract values and distributions of eigenvalues and eigenvectors to import them in another software, and direction of eigenvectors.<br>
In “Diffusion Tensor Scalar Maps” I can plot the eigenvalues and in the “Volume-&gt;Color Orientation” I can plot the gluph eigenvectors.<br>
In both case, I can see the values only if I put the mouse on the image but I cannot export or see the distribution of values as in other software (as Comsol).</p>
<p>What should I do?</p>
<p>Operating system: windows 10<br>
Slicer version: 4.10.0<br>
Expected behavior: values, distributions, directions<br>
Actual behavior: I see the distribution only</p>

---

## Post #2 by @ljod (2019-04-26 12:11 UTC)

<p>Hi. What is your use case or goal?</p>
<p>You can export the entire computed DTI volume in nrrd format. This happens when you use the Save button or menu item to save the scene. Then if you are a programmer you can access the tensors in any way you would like.</p>
<p>SlicerDMRI is designed for typical use cases for medical imaging, so it’s easy to quantify things like mean FA within a region, or the mean of the maximum eigenvalue within a region for example. If you want to measure the mean and standard deviation of these numbers within a given region, that’s possible.</p>

---
