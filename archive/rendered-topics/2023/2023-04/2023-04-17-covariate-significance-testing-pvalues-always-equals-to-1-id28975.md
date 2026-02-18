# Covariate Significance testing - Pvalues always equals to 1

**Topic ID**: 28975
**Date**: 2023-04-17
**URL**: https://discourse.slicer.org/t/covariate-significance-testing-pvalues-always-equals-to-1/28975

---

## Post #1 by @Giulia_Baldassari (2023-04-17 17:52 UTC)

<p>Dear experts,<br>
I used SlicerSalt software to carry out a shape analysis but whichever database I used and for different substructures such as caudate, hippocampus and amygdala the pvalue was always non-significant. In particular, I performed the following steps:</p>
<ol>
<li>shapeAnalysisModule from which I have as input the mask of interest of the first subject. Then I set the coef of the first subject just obtained as a template and obtained the mesh of all the subjects.</li>
<li>Procrustes Registration between all the elligned.vtk meshes taking the first one as reference and scaling.</li>
<li>Population Analysis between the two sets of subjects obtaining the average surfaces</li>
<li>Covariate Significance testing by putting different covariates such as age, years of illness.<br>
I did not carry out the Correspondence Improvment as I could not find a way to obtain landmarks automatically for so many subjects. Is there something wrong with the procedure?<br>
I would also have liked to perform shapeAnalysisMANCOVA with these models but as it is an old tool it does not read the new vtk. Is there a way to convert them to the old format? otherwise how can I see the pRAW?<br>
thank you very much,<br>
Giulia</li>
</ol>

---
