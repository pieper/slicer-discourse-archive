# RTplan beam shape - "Block sequence" dicom parameter

**Topic ID**: 28962
**Date**: 2023-04-17
**URL**: https://discourse.slicer.org/t/rtplan-beam-shape-block-sequence-dicom-parameter/28962

---

## Post #1 by @Francesca_6 (2023-04-17 13:06 UTC)

<p>Hello everyone,</p>
<p>I am new to the community and am starting to use 3D slicer on images of veterinary patients in the context of synchrotron micro beam radiotherapy.</p>
<p>In this setting, during radiotherapy, we use masks that we place in front of the beam to shape it.</p>
<p>The shape of the used mask  is recorded in the dicom file of the RTplan in the tags that characterize the “block sequence” (300a, 00F4) (300a, 0106).</p>
<p>When I open in 3D slicer the CT scan and the RTplan, obviously the shape of the beam does not turn out to be correct because it takes into account the position of the Jaws.<br>
What can I do to give the beam the desired shape? Or to make it read the shape of the “block sequence”?</p>
<p>I already tried to add a table and give a “new shape” to the MLC collimator but I can’t get the correct shape.</p>
<p>I hope I have been clear–in any case, I am here for any clarification.</p>
<p>Thank you very much everyone!</p>

---

## Post #2 by @lassoan (2023-04-17 13:19 UTC)

<p>Shielding blocks are not yet supported in SlicerRT (see stub <a href="https://github.com/SlicerRt/SlicerRT/blob/4c0ceb8900f6c12ab9b66e2ae6e7d1077c99c409/DicomRtImportExport/Logic/vtkSlicerDicomRtReader.cxx#L120-L128">here</a>). <a class="mention" href="/u/mik">@Mik</a> do you plan to implement it at some point or help <a class="mention" href="/u/francesca_6">@Francesca_6</a> to implement it?</p>

---

## Post #3 by @Mik (2023-04-17 13:31 UTC)

<p>I don’t have datasets (CT, RTPLAN, RTDOSE, etc) to implement block sequence support. If <a class="mention" href="/u/francesca_6">@Francesca_6</a> could share the data, i possibly could add support of block-sequence. I assume that only visualization is required?</p>

---

## Post #4 by @Francesca_6 (2023-04-17 13:34 UTC)

<p>Yes, I just want to visualize it.<br>
I’ll ask for data sharing or I’ll anonymize them (how can I send them to you?)<br>
I have just CT, RTPlan and RTStruct, is it ok for you?<br>
Really thank you so much</p>

---

## Post #5 by @Mik (2023-04-17 13:49 UTC)

<p>You can upload and share the data by means of google drive or one drive.</p>
<p>Can you make a <a href="https://github.com/SlicerRt/SlicerRtData/blob/master/xio-4.64-phantom-prostate-beams-wedges/_WEDGES.jpg" rel="noopener nofollow ugc">screenshot</a> of dose distribution so i can better understand the shape of the block and the dose after the block, if the RTDose is absent.?</p>
<p>CT, RTPlan, RTStruct are enough for the start.</p>

---
