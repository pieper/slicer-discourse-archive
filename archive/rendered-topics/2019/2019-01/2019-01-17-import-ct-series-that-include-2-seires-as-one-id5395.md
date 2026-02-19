---
topic_id: 5395
title: "Import Ct Series That Include 2 Seires As One"
date: 2019-01-17
url: https://discourse.slicer.org/t/5395
---

# Import CT series, that include 2 seires as one

**Topic ID**: 5395
**Date**: 2019-01-17
**URL**: https://discourse.slicer.org/t/import-ct-series-that-include-2-seires-as-one/5395

---

## Post #1 by @hadasara (2019-01-17 10:53 UTC)

<p>Hi all,<br>
Maybe someone here would know-<br>
I came across a CT series, that include 2 series, saved as a single one.<br>
When you scroll in axial slices in a dicom viewere (RADient), you see shoulder s to pelvis and then agin shoulders to pelvis in a later contrast.<br>
Does anyone know if there is a <strong>tag in the DICOM header</strong> that can seperate them?<br>
ITK-SNAP doesn’t recognize they are seperate, and also from viewing the header I could’nt find anything.</p>
<p>I load it also into 3Dslicer and this is the erroe I get, and the images looks with wrong proprtions:</p>
<p>Imported a DICOM directory, checking for extensions<br>
Imported a DICOM directory, checking for extensions<br>
Geometric issues were found with 1 of the series.  Please use caution.<br>
Warning in DICOM plugin Scalar Volume when examining loadable 2: Unnamed Series: Images are not equally spaced (a difference of -0.5 vs 1 in spacings was detected).  If loaded image appears distorted, enable ‘Acquisition geometry regularization’ in Application settins / DICOM / DICOMScalarVolumePlugin.  Please use caution.<br>
Loading with imageIOName: GDCM<br>
Window/level found in DICOM tags (center=40.0, width=350.0) has been applied to volume 2: Unnamed Series<br>
Irregular volume geometry detected (maximum error of 218 mm is above tolerance threshold of 0.001 mm).  Regularization transform is not added, as the option is disabled.</p>
<p>Thanks!<br>
Hadas.</p>

---

## Post #2 by @pieper (2019-01-17 15:24 UTC)

<p>It sounds like the header data doesn’t describe the acquisition well.  Perhaps this is the result of deidentification or other processing.  You can try loading as a Multivolume (but maybe that’s not detected) and to dig deeper you can look at the headers using the metadata browser and see what tags might distinguish the data into two volumes.</p>

---
