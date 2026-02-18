# Create a Volumen from axial,sagital and coronal series

**Topic ID**: 20093
**Date**: 2021-10-11
**URL**: https://discourse.slicer.org/t/create-a-volumen-from-axial-sagital-and-coronal-series/20093

---

## Post #1 by @MAURICIO_ALBERTO_LED (2021-10-11 05:31 UTC)

<p>Operating system: Linux Ubuntu<br>
Slicer version: 4.11.20210226<br>
Hello my name is Mauricio and  i am currently working on determining the trajectory of bullets in head wounds. I have a problem and is that when the radiology share me the DICOM file of a MIP angiography, it share the imagen in three different series: axial, coronal and sagital. I need a single volumen series. it is possible to convert the 3 series to one volumen series with 3d slicer?</p>
<p>PD: This is how appears in the DICOM load data<br>
PATIENT NAME<br>
DSA  ANGIO CRANEO(Adulto) (20210125) (study)<br>
1012: AXIAL MIP_1   (serie)<br>
1014: CORONAL MIP (serie)<br>
1016: SAGITAL MIP_1 (serie)</p>
<p>Thanks for the time.</p>

---

## Post #2 by @lassoan (2021-10-11 14:13 UTC)

<p>It is not possible to reconstruct a 3D volume from just 3 projections.</p>
<p>There is an axial image, which indicates that the acquired rotational angio is suitable for 3D reconstruction. Therefore, most likely the radiologists can give you a reconstructed 3D volume and not just 3 projection images.</p>

---

## Post #3 by @MAURICIO_ALBERTO_LED (2021-10-11 17:41 UTC)

<p>Than you, i would contact the radiologists and solicitate a reconstructed 3D volume.<br>
Thank you for your prompt response.</p>

---
