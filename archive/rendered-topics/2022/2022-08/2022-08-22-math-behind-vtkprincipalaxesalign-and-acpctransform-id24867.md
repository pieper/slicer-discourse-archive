---
topic_id: 24867
title: "Math Behind Vtkprincipalaxesalign And Acpctransform"
date: 2022-08-22
url: https://discourse.slicer.org/t/24867
---

# Math behind vtkPrincipalAxesAlign and ACPCTransform 

**Topic ID**: 24867
**Date**: 2022-08-22
**URL**: https://discourse.slicer.org/t/math-behind-vtkprincipalaxesalign-and-acpctransform/24867

---

## Post #1 by @Brandon_Z (2022-08-22 14:58 UTC)

<p>Hello all,</p>
<p>I am not sure this is the right place to ask this question, but I’m wondering about the math behind the PCA implementation in “vtkPrincipalAxesAlign” as well as some other steps in the ACPCTransform module. I’ve been trying to develop a registration pipeline in python, and while I have results that mirror the Slicer c++ function, I’m a little unsure about why it works. I tried using a function I had which implements PCA with a simple SVD, but got different results. I have limited background in c++, and was hoping for some additional assistance in understanding.</p>
<p>Any links to the rationale behind this function? Primarily, I don’t quite understand how the eigenvalueProblem matrix is constructed.</p>
<p>Second, I am wondering if there is any resources to understand how the transformation matrix is constructed from the resulting lowest valued eigenvalue eigenvector. I think I’m missing the point of the various operations to implement the 3x3 core transformation.</p>

---

## Post #2 by @lassoan (2022-08-22 22:39 UTC)

<p>You can simply <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-run-a-cli-module-from-python">run the ACPC registration module from Python</a>.</p>
<p>If you want to understand/reproduce the math in a different environment:</p>
<ul>
<li>The module fits a plane on the points dropped on the midsagittal plane, using PCA of the covariance matrix (because PCA is a simple textbook method for plane fitting), but any other plane fitting method should work.</li>
<li>Then, you compute a rotation matrix from the plane normal. Again, there are many ways to do this, the authors chose a formula similar to <a href="https://math.stackexchange.com/a/1957132">this</a>.</li>
<li>Finally, if the ACPC line is provided then you apply an additional rotation so that the ACPC line is rotated into the axial plane.</li>
</ul>

---
