# Partial correlation

**Topic ID**: 12394
**Date**: 2020-07-06
**URL**: https://discourse.slicer.org/t/partial-correlation/12394

---

## Post #1 by @quentin_devignes (2020-07-06 13:28 UTC)

<p>Hello SlicerSALT Team,</p>
<p>As far as partial correlation can not be done with shapeAnalysisMANCOVA, do you know I could perform it? I thought I could use the distance at each vertex between my patients’ shapes and the mean shape (I used the option “Use mean as Template”) and do the statistical analyses with another software (like R) but I did not find where theses distances were written and I think it will be difficult to get shape illustrations afterwards… I found a paper in which the authors did a partial correlation (<a href="https://www.sciencedirect.com/science/article/pii/S0967586819307441" rel="nofollow noopener">https://www.sciencedirect.com/science/article/pii/S0967586819307441</a>) but they did not tell how they did it and I assume there are other papers and this kind of analysis has been done several times… Could you help me please?</p>
<p>Wish you a pleasant day,<br>
Quentin</p>

---

## Post #2 by @styner (2020-07-06 16:30 UTC)

<p>Hi Question<br>
I don’t think the Yoo et al paper did partial correlations, rather (if I am reading the paper correctly) they did straightforward Pearson correlation with the local signed magnitude difference to the average object shape.</p>
<p>MeshMath operations can provide you with that information (you will need to use the terminal though for doing this).  If you run MeshMath -help then it will give you a breakdown of all the tasks it can do.</p>
<p>Computing a mean surface with MeshMath:<br>
MeshMath mesh1.vtk outputAverageMesh.vtk -avgMesh mesh2.vtk mesh3.vtk ….</p>
<p>Difference vector between meshes mesh1 - mesh2:<br>
MeshMath mesh1.vtk output_DiffVector.txt -subtract mesh2.vtk</p>
<p>Signed difference magnitude (sign is relative to reference mesh):<br>
MeshMath referenceMesh.vtk output_SignedDistanceMagnitude.txt -magDir output_DiffVector.txt</p>
<p>You can alternatively compute the normal projection of that signed difference (this would mean you are only looking at the part of the difference that goes along the surface normal of your reference mesh)"<br>
MeshMath referenceMesh.vtk output_SignedDistanceNormMagnitude.txt -magNormDir output_DiffVector.txt</p>
<p>I am not 100% sure which of the these 2 differences were used in the Yoo paper, but I think it refers to the “magNormDir” distance</p>
<p>Finally, shapeAnalysisMANCOVA will not yield partial correlations and I am not sure how you can straightforwardly do so.</p>

---

## Post #3 by @quentin_devignes (2020-07-20 08:36 UTC)

<p>Hi Martin,</p>
<p>Thank you for your reply. I have computed magNormDir distances using the process you told me. However, some points have really high values (-101507 for example). Is it possible? If yes, what is the unit of these values? I guess it’s not in millimeter.</p>
<p>Thank you again for your help,<br>
Wish you a nice day,</p>
<p>Quentin</p>

---

## Post #4 by @styner (2020-07-27 21:20 UTC)

<p>mm, that’s strange. Values should be in mm. Which surfaces did you use (I assume the procalign.vtk surfaces)? Did you inspect your generated surfaces to ensure that they all look fine and are appropriately shaped (you can use ShapePopulationViewer in SlicerSALT to efficiently look at lots of surfaces at the same time)?<br>
Martin</p>

---

## Post #5 by @quentin_devignes (2020-07-29 15:17 UTC)

<p>Martin,</p>
<p>Thank you for your reply. These values were due to a conversion problem in Excel. Everything is okay now and I managed to perform partial correlations in R using the method you described above.</p>
<p>Quentin</p>

---
