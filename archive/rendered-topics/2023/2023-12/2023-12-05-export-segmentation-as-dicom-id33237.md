# Export segmentation as DICOM

**Topic ID**: 33237
**Date**: 2023-12-05
**URL**: https://discourse.slicer.org/t/export-segmentation-as-dicom/33237

---

## Post #1 by @Piergiorgio_Gaudioso (2023-12-05 16:06 UTC)

<p>Operating system: macOS<br>
Slicer version: 3D Slicer 5.2.2<br>
Expected behavior: I would like to export MRI and segmentation marged as a DICOM file</p>

---

## Post #2 by @pieper (2023-12-05 17:54 UTC)

<p>In dicom segmentations are saved independently from the MRI, so there isn’t really a merge option.  Can you describe what you want to use the data for?</p>

---

## Post #3 by @Piergiorgio_Gaudioso (2023-12-10 10:44 UTC)

<p>I would like to share the segmentation of the surgical resection with radiation oncologists during the tumor board. I would like to upload the file in our PACS, so I need a merged DICOM file. Do you think there can be a solution?</p>

---

## Post #4 by @pieper (2023-12-10 16:01 UTC)

<p>Many institutions don’t allow research data to be pushed to the PACS, and in fact, most clinical systems don’t have any good way to accept third party segmentations, so we tend to have a research analysis mode that goes in parallel with the clinical workflow, under IRB approval when needed.  Maybe someone with experience working in settings like you describe could comment on what they do.</p>

---

## Post #5 by @mau_igna_06 (2023-12-10 18:07 UTC)

<p>Maybe it’s a very bad idea but I guess you could create an RGB volume (like PET scans but a fake one) for your MRI as grey scale and your segmentations as different colors</p>
<p>Hope it’s useful</p>

---

## Post #6 by @athanell (2023-12-10 19:46 UTC)

<p>I think it is feasible to merge an MRI with a segmentation into a “bundled” DICOM IOD using a secondary capture (SC IOD) with an RGB photometric interpretation. This approach results in an MRI with an overlaid segmentation mask on the volume. To maintain visibility of the MRI behind the segmentation you will need to set low opacity values for the segmentation mask. However, with this process you will loose the original dynamic range of the MRI as it becomes an RGB image (8 bits per color I think) and toggling the segmentation mask on and off is not possible. Essentially you “burn into the MRI” a segmentation mask.</p>
<p>That being said, I think it will be very unlikely to be allowed to push such an IOD to your production PACS server (assuming that your PACS implementation supports SC storage SOP) since a lot can go wrong if the SC IOD that you create is not fully valid. But if you have a non-production dicom server (e.g. DICOMweb and a viewer like OHIF) you can push it there and radiologists can review the merged image through a web-browser. They can assess whether they are comfortable with the limitations imposed by the secondary capture approach.</p>
<p>Take this suggestion with a grain of salt, and hopefully more experienced users can  offer their insights on whether the proposed approach is suitable.</p>

---
