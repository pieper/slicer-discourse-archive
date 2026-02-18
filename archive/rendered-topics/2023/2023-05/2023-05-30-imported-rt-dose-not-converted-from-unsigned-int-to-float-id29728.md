# Imported RT dose not converted from unsigned int to float

**Topic ID**: 29728
**Date**: 2023-05-30
**URL**: https://discourse.slicer.org/t/imported-rt-dose-not-converted-from-unsigned-int-to-float/29728

---

## Post #1 by @alema (2023-05-30 15:26 UTC)

<p>Operating system: Linux (OpenSUSE 15.4)<br>
Slicer version: 5.2.1<br>
Expected behavior: Scalar Type of imported RT dose should float<br>
Actual behavior: Scalar Type of imported RT dose is unsigned int</p>
<p>Hi,</p>
<p>When I import a radiation treatment plan produced by Varian Eclipse (Image, RTPLAN, RTSTRUCT, and RTDOSE. All in DICOM format.), then the RTDOSE file is of type float, and the Dose Volume Histogram (DVH) module (SlicerRT) works as expected. Then I create a child study and place an imported RT dose file in the child study tree. The RT dose has the same content as the one produced by Eclipse; only the Pixel Data and Dose Grid Scaling are taken from TOPAS simulations. In this case, however, the dose volume is not converted to float and rescaled. The conversion to  RT Dose Volume does not change the data. The DVH module then generates histograms based on the unsigned int representation (max dose about 1E6 Gy).</p>
<p>Is this an expected behavior? Do I do something wrong?</p>
<p>As a workaround, I use the Cast Scalar Volume module to change unsigned int to float and the Dose Accumulation (SlicerRT) module to apply the Dose Grid Scaling factor. The dose volume then contains doses in Gy (max dose about 50 Gy), and the DVH module produces correct histograms. I get what I want, but the method is laborious.</p>
<p>Alexandr</p>

---

## Post #2 by @lassoan (2023-05-30 20:19 UTC)

<p>Yes, this is the expected behavior. Scaling of the dose volume is performed during DICOM RT import. If you import the volume in some alternative way then you need to apply scaling yourself (it is a single-line operation using numpy - see examples in the script repository).</p>
<p>If you do this frequently then there are several options to choose from to make this import really simple, few-click operation:</p>
<ul>
<li>Option A: create an RTDOSE file in your simulator</li>
<li>Option B: create a nrrd file with already scaled floating-point values (there should be no issue with directly storing these scaled values - probably RTDOSE uses integer values because at the time RTDOSE IOD was created, DICOM did not support float volumes; and they also saved some memory by using just 16 bits for each voxel)</li>
<li>Option C: create a custom file reader that recognizes your custom input file (nrrd file with some custom metadata to store the scaling value?) and applies the scaling and converts to dose volume</li>
</ul>

---
