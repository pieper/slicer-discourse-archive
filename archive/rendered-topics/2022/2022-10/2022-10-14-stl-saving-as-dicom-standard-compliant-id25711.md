---
topic_id: 25711
title: "Stl Saving As Dicom Standard Compliant"
date: 2022-10-14
url: https://discourse.slicer.org/t/25711
---

# Stl saving as DICOM (standard compliant)

**Topic ID**: 25711
**Date**: 2022-10-14
**URL**: https://discourse.slicer.org/t/stl-saving-as-dicom-standard-compliant/25711

---

## Post #1 by @mau_igna_06 (2022-10-14 23:02 UTC)

<p><a href="https://support.dcmtk.org/docs/stl2dcm.html" rel="noopener nofollow ugc">This</a> command line tool allows to save a stl as DICOM.</p>
<p>Regarding <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner#readme" rel="noopener nofollow ugc">BRP</a> would it be important to export custom surgical guides, reconstruction or anatomical models on the Slicer scene not as stl but as DICOM?</p>
<p>I found this <a href="https://dicom.nema.org/Dicom/News/September2017/docs/sups/sup205_overview.pdf" rel="noopener nofollow ugc">old presentation</a> regarding this topic.</p>

---

## Post #2 by @pieper (2022-10-14 23:21 UTC)

<p>Yes, since encapsulated stl is part of the dicom standard it would be a good way to record the needed metadata about a model and store it in a hosptial pacs or vna.  It also removes a lot of the ambiguity about coordinate systems and units that are problematic with native stl.</p>
<p>That said, it’s a somewhat obscure format so it’s not clear who else in the world would support that format.</p>

---

## Post #3 by @lassoan (2022-10-16 06:33 UTC)

<p>It would be straightforward to implement a DICOM export plugin based on DCMTK’s <a href="https://github.com/DCMTK/dcmtk/blob/master/dcmdata/apps/stl2dcm.cc">stl2dcm example</a>. However, I agree with <a class="mention" href="/u/pieper">@pieper</a> in that this is a niche file format, therefore it is not clear if it is worth the effort of implementing and maintaining importers/exporters for it. I don’t think anyone form the Slicer developer team has ever seen such a DICOM file. It is also telling that DCMTK does not have a dcm2stl utility - most likely because people don’t come across such files.</p>
<p>Note that segmentations can also be stored in a mesh format, see: <a href="https://dicom.nema.org/dicom/2013/output/chtml/part03/sect_A.57.html" class="inline-onebox">A.57 Surface Segmentation IOD</a>. It is a bit more general-purpose representation (not so tightly linked to 3D printing as the encapsulated STL), but it has not become widely used either. I only remember this single discussion on this forum about this information object: <a href="https://discourse.slicer.org/t/load-dicom-surface-segmentation-objects/1125" class="inline-onebox">Load DICOM Surface Segmentation Objects</a></p>
<p>If you just need to store encapsulated data files on a PACS in DICOM format then you may also consider Slicer’s embedded MRML scene format (read/written by the “Slicer Data Bundle” plugin). It is not compatible with any other software, but it is already implemented and it works with all data objects that Slicer supports.</p>

---
