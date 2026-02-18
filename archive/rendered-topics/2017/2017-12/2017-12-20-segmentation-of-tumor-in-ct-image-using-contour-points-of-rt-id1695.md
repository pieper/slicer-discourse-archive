# Segmentation of tumor in CT image using contour points of RT Struct

**Topic ID**: 1695
**Date**: 2017-12-20
**URL**: https://discourse.slicer.org/t/segmentation-of-tumor-in-ct-image-using-contour-points-of-rt-struct/1695

---

## Post #1 by @Apurva (2017-12-20 22:53 UTC)

<p>Hey, I am Apurva. I am currently pursuing my Masters at George Washington University.<br>
I am currently working on analysis of the effectiveness of Radiation Therapy for the treatment of patients suffering from Head and Neck Squamous Cell Carcinoma. The dataset has been obtained from TCIA ( The Cancer Imaging Archive).<br>
I have RTSTRUCT, RTPLAN and RTDOSE and CT files for a patient. I want to know the location of the tumor in the CT image using the coplanar points present in the RTSTRUCT information.<br>
The Segmentations module in 3D Slicer 4.8.0 helps me create a binary labelmap using the RTSTRUCT data. However, I am not sure of how to use this labelmap to get the tumor boundary on the CT image ( or how to map the points present in the RTSTRUCT to the CT image).<br>
Also, the Isodose module in the tutorial shows that the isodose lines will be indicated on the CT image. However, in my case, even after I click on the “Apply” option in the Isodose module, there is no change observed in the original CT image.<br>
Can you please tell me how to proceed with the problem?<br>
Thanks,<br>
Apurva</p>

---

## Post #2 by @lassoan (2017-12-20 22:58 UTC)

<p>Install SlicerRT extension and load a study that has contours defined in RTSTRUCT. Slicer will load and display the contours overlaid on the CT image.</p>
<p>To generate isodose lines/surfaces, you need to use RTDOSE volume as input.</p>
<p>Which TCIA collection and data set you are looking at?</p>

---

## Post #3 by @Apurva (2017-12-20 23:27 UTC)

<p>Dear Sir,<br>
I already installed the SlicerRT extension from the 3 D<br>
Slicer but I am not very sure how to use it because although it is<br>
displayed in the Manage Extension section,it does not get displayed when I<br>
click on the modules list.<br>
I am using the TCIA HNSCC database.<br>
Regards<br>
Apurva</p>

---

## Post #4 by @cpinter (2017-12-20 23:42 UTC)

<p>SlicerRT is not one module, it is many modules, one of which is integrated with DICOM loading. You need to load the DICOM-RT files the same way as you would load other DICOM files after installing SlicerRT.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM</a></p>

---

## Post #5 by @Apurva (2017-12-21 04:38 UTC)

<p>Dear Sir,<br>
Thanks for the prompt reply. I will try this module out.<br>
Regards<br>
Apurva</p>

---

## Post #6 by @lassoan (2019-12-26 22:48 UTC)

<p>A post was merged into an existing topic: <a href="/t/how-to-analyse-ct-data/9620/3">How to analyse CT data?</a></p>

---
