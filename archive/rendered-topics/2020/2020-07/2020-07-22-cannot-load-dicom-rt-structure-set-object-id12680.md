# cannot load DICOM RT structure set object

**Topic ID**: 12680
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/cannot-load-dicom-rt-structure-set-object/12680

---

## Post #1 by @44REAM (2020-07-22 13:43 UTC)

<p>Im try to convert dicom file (CT, RD, RS) to nrrd by using mpreview processor but it show the error below</p>
<pre><code>    Switching to temporary DICOM database: C:/Users/dream/AppData/Local/Temp/Slicer\mpReviewPreprocessor\CtkDICOMDatabase

    Loading with imageIOName: GDCM

    Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 3: Abdomen 2.5 mm

    Loading with imageIOName: GDCM

    Could not read scalar volume using GDCM approach. Error is: FileFormatError

    Loading with imageIOName: DCMTK

    Could not read scalar volume using DCMTK approach. Error is: FileFormatError

    No node!

    Loading with imageIOName: GDCM

    Could not read scalar volume using GDCM approach. Error is: FileFormatError

    Loading with imageIOName: DCMTK

    Could not read scalar volume using DCMTK approach. Error is: FileFormatError

    No node!

    Loading with imageIOName: GDCM

    Could not read scalar volume using GDCM approach. Error is: FileFormatError

    Loading with imageIOName: DCMTK

    Could not read scalar volume using DCMTK approach. Error is: FileFormatError

    No node!

    Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects
</code></pre>
<p>I already install SlicerRT extension and reinstall it but still the same.<br>
I try using slicer version 4.11.0 2020-03-25 and 4.11.0 2020-07-20.<br>
Any one know how to fix this<br>
Thank.</p>

---

## Post #2 by @lassoan (2020-07-22 14:26 UTC)

<p>Can you load all data by following these steps:</p>
<ul>
<li>switch to DICOM module</li>
<li>drag-and-dropp the DICOM folder to the Slicer application window</li>
<li>wait for  import to complete,l</li>
<li>double-click on a patient, study, or series you want to load</li>
</ul>

---

## Post #3 by @44REAM (2020-07-22 17:34 UTC)

<p>Yes I can load all my data (CT, RD, RS) in DICOM module. But it not work in mpreviewprocessor.</p>

---

## Post #4 by @fedorov (2020-07-22 22:13 UTC)

<p>mpReviewPreprocessor is intended to organize the data into a hierarchy that is usable by the mpReview extension. At the moment, it will not process any modalities other than those that correspond to scalar volumes, or some 4d volumes. You will need to either process other modalities using other means, or modify mpReviewPreprocessor to invoke DICOM plugins that can parse those modalities.</p>

---
