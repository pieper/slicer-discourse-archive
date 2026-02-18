# The difference between model and mesh

**Topic ID**: 23389
**Date**: 2022-05-12
**URL**: https://discourse.slicer.org/t/the-difference-between-model-and-mesh/23389

---

## Post #1 by @yyl (2022-05-12 16:07 UTC)

<p>I am very happy that I can use 3D slicer to place and transfer landmarks and semilandmarks.I saw an expert in the slicer forum saying that currently 3D slicer does not support the sliding of semilandmarks and it can be achieved through R. I have some doubts when sliding according to the morpho package.</p>
<ol>
<li>What is the mesh mentioned in the morpho package manual? Is the templatemesh formed in the  PseudoLMGenerator stage? Or the model?</li>
<li>When I slide the semilandmarks points according to the code in the morpho package manual, my semilandmarks are shifted too much and obvious deformation occurs. I consult the literature, but the specific parameter settings are rarely mentioned in the literature,such as iterations. So is there a community where we can share the problems and solutions encountered in geometric morphometric measurement?<br>
I would be very happy if someone could answer my question!</li>
</ol>

---

## Post #2 by @smrolfe (2022-05-12 16:59 UTC)

<p>For questions about using the morpho package and general morphometrics discussions you can join this google group: <a href="https://groups.google.com/g/morphmet2" rel="noopener nofollow ugc">https://groups.google.com/g/morphmet2</a></p>
<p>I am not clear on your first question. ‘Model’ and ‘mesh’ are often used interchangeably in different applications. The PseudoLMGenerator in the SlicerMorph extension is only used to generate evenly spaced semi-landmark points on a model surface. The template in this module is an intermediate model only used to sample points on the original surface.</p>

---
