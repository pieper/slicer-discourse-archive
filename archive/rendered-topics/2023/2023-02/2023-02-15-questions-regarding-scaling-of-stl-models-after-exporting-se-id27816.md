# Questions regarding scaling of .stl models after exporting segmentation

**Topic ID**: 27816
**Date**: 2023-02-15
**URL**: https://discourse.slicer.org/t/questions-regarding-scaling-of-stl-models-after-exporting-segmentation/27816

---

## Post #1 by @Levi (2023-02-15 03:32 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.0.3<br>
Expected behavior: Exporting .stl models at size shown in Slicer<br>
Actual behavior:.stl files are exporting at roughly 14x initial size. For example, a diameter measured as 2mm in 3DSlicer is approximately 28 mm when measured in other programs after exporting it as an .stl file. I cannot seem to find the cause of this issue and its consistently happening.</p>

---

## Post #2 by @lassoan (2023-02-15 03:51 UTC)

<p>If you use proper file formats and don’t change defaults then all sizes are correct. However, there are various implementation errors in many imaging devices and some file formats have limitations (e.g., TIFF, PNG, STL formats do not have standard fields to store 3D scaling information), so you have to be careful.</p>
<p>Have you imported DICOM CT/MRI from a clinical scanner (not micro-CT or dental cone-beam CT)? Is the size correct when you measure in Slicer? If you loaded from NIFTI, NRRD, etc. was the spacing set in the file correctly? If you imported from TIFF, PNG, etc. stack, have you manually set the spacing value?</p>
<p>Have you modified the scaling factor in Slicer when you exported the STL file? If not, then Slicer uses millimeters as coordinates units when exporting.</p>
<p>What software did you load the STL file into? What unit did you choose when in that software when you imported the STL file?</p>

---
