---
topic_id: 8698
title: "Slicerrt Could Not Export Rtplan"
date: 2019-10-07
url: https://discourse.slicer.org/t/8698
---

# SlicerRT: could not export RTPLAN

**Topic ID**: 8698
**Date**: 2019-10-07
**URL**: https://discourse.slicer.org/t/slicerrt-could-not-export-rtplan/8698

---

## Post #1 by @Guangshan_Chen (2019-10-07 19:40 UTC)

<p>I load RTPLAN, RTDOSE, RTSTRUCT, and RT image into Slicer and would like to export them as dicom files.</p>
<p>I can have RTDOSE, RTSTRUCT, and RT image exported, not RTPLAN. I look at the code RTPLAN node does not get checked in SlicerRT/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx. It only check:</p>
<pre><code class="lang-auto">// Get nodes for the different roles from the exportable list
  vtkMRMLScalarVolumeNode* doseNode = nullptr;
  vtkMRMLSegmentationNode* segmentationNode = nullptr;
  vtkMRMLScalarVolumeNode* imageNode = nullptr;
</code></pre>
<p>Correspondingly, only anatomical image, dose distribution image and structure can be set in SlicerRT/DicomRtImportExport/Logic/vtkSlicerDicomRtWriter.h:</p>
<pre><code class="lang-auto">  /// Set anatomical image to Plastimatch RT study for export
  void SetImage(const Plm_image::Pointer&amp;);

  /// Set dose distribution image to Plastimatch RT study for export
  void SetDose(const Plm_image::Pointer&amp;);

  /// Add structure as image data to Plastimatch RT study for export
  void AddStructure(UCharImageType::Pointer, const char* name, double* color);
</code></pre>
<p>If anyone has exported RTPLAN, could you share your code with me?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @cpinter (2019-10-07 20:49 UTC)

<p>RT Plan export in SlicerRT has not been implemented unfortunately. We are currently writing a grant that will allow that, but it will be at least a year or two before it happens. If you or your lab has the capacity to start adding this feature I will be happy to help.</p>

---

## Post #3 by @Guangshan_Chen (2019-10-07 21:20 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="8698">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>RT Plan export in SlicerRT has not been implemented unfortunately.</p>
</blockquote>
</aside>
<p>Thanks for the information.</p>
<p>I would like to start working on it. Currently, I am thinking how to convert vtkMRMLRTPlanNode object to Rtplan object. Then I can set it in the writer. If you have any information on it, please let me know.</p>

---

## Post #4 by @gcsharp (2019-10-08 16:21 UTC)

<aside class="quote no-group" data-username="Guangshan_Chen" data-post="3" data-topic="8698">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/guangshan_chen/48/4832_2.png" class="avatar"> Guangshan_Chen:</div>
<blockquote>
<p>I would like to start working on it. Currently, I am thinking how to convert vtkMRMLRTPlanNode object to Rtplan object. Then I can set it in the writer. If you have any information on it, please let me know.</p>
</blockquote>
</aside>
<p>Most of the plan information is lost upon import.  Exporting a plan to DICOM could be done, but the resulting object would not be very useful.</p>
<p>Why do you want to export the RT Plan?  How will you use it?</p>

---

## Post #5 by @Guangshan_Chen (2019-10-08 17:22 UTC)

<p>We  want to deliver a RT plan so that the beams can be set up according to the plan.</p>

---

## Post #6 by @cpinter (2019-10-11 20:14 UTC)

<p>Can you describe your goal in a bit more detail?</p>
<p>In any case, you will need to add RTPLAN support in</p>
<ol>
<li>The plugin:<br>
<a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/DicomRtImportExportPlugin.py#L81" class="inline-onebox">SlicerRT/DicomRtImportExport/DicomRtImportExportPlugin.py at master · SlicerRt/SlicerRT · GitHub</a></li>
<li>The writer: <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtWriter.cxx#L100" class="inline-onebox">SlicerRT/DicomRtImportExport/Logic/vtkSlicerDicomRtWriter.cxx at master · SlicerRt/SlicerRT · GitHub</a></li>
<li>The import/export logic: <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L1966" class="inline-onebox">SlicerRT/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx at master · SlicerRt/SlicerRT · GitHub</a></li>
<li>Figure out how to set the plan information in Plastimatch: <a href="https://gitlab.com/plastimatch/plastimatch/blob/master/src/plastimatch/base/rt_study.h#L115" class="inline-onebox">Files · master · plastimatch / plastimatch · GitLab</a></li>
</ol>
<p>All the links above are the corresponding parts for RT dose. The same needs to be done with the plan.</p>
<aside class="quote no-group" data-username="gcsharp" data-post="4" data-topic="8698">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>but the resulting object would not be very useful.</p>
</blockquote>
</aside>
<p>What do you mean?</p>

---

## Post #7 by @Guangshan_Chen (2019-10-11 21:01 UTC)

<p>Hi cpinter,</p>
<p>My current goal is still vague. My idea is that if I create a RTPLAN in SlicerRT, I should be able to export out from Slicer and then reload it back into Slicer.</p>
<p>Thanks for pointing out the code needed to be changed.</p>
<p>I have successfully exported a RTPLAN dicom file yesterday. The following is how I implemented in <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L1966" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx</a></p>
<pre><code class="lang-auto">// Convert input RTPlan to the format Plastimatch can use
  if (planNode) {
    std::cout &lt;&lt; "chengs++: export RT study find RTPlanVolume node " &lt;&lt; std::endl;
    Rtplan::Pointer plan = Rtplan::New();
    plan-&gt;rt_plan_label = "T ORL 1C";
    plan-&gt;rt_plan_name = "T ORL 1C";
    plan-&gt;rt_plan_date = "18850827";
    plan-&gt;rt_plan_time = "111111";

    plan-&gt;patient_position = "hfs"; //patient position metadata: one of {hfs,hfp,ffs,ffp}

    rtWriter-&gt;SetPlan(plan);
  }
</code></pre>
<p>Basically, it is just dummy Rtplan object.</p>
<p>However, the problem I face now is that I could not load the RTPLAN dicom file back with Slicer. Because Slicer think this file is scalar volume. Here is the error:</p>
<p>"<br>
Warning in DICOM plugin Scalar Volume when examining loadable 114120633: Unnamed Series: Reference image in series does not contain geometry information. Please use caution.</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /tmp/IRS-gchen/DICOMExportTemp_20191011_135248/RTPLAN/rtplan_1.2.826.0.1.3680043.8.274.1.1.8323329.21835.1570819971.548083.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file /tmp/IRS-gchen/DICOMExportTemp_20191011_135248/RTPLAN/rtplan_1.2.826.0.1.3680043.8.274.1.1.8323329.21835.1570819971.548083.dcm<br>
Tried to create one of the following:<br>
BMPImageIO<br>
BioRadImageIO<br>
DCMTKImageIO<br>
GDCMImageIO<br>
GiplImageIO<br>
JPEGImageIO<br>
LSMImageIO<br>
MGHImageIO<br>
MINCImageIO<br>
MRCImageIO<br>
MetaImageIO<br>
NiftiImageIO<br>
NrrdImageIO<br>
PNGImageIO<br>
StimulateImageIO<br>
TIFFImageIO<br>
VTKImageIO<br>
MRMLIDImageIO<br>
Bruker2dseqImageIO<br>
GE4ImageIO<br>
GE5ImageIO<br>
HDF5ImageIO<br>
JPEG2000ImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.<br>
"</p>
<p>I have not figure out the reason. If you have any suggestion, please let me know.<br>
Thanks.</p>

---

## Post #8 by @Guangshan_Chen (2019-10-11 21:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/069685a3067dadc0d89f58c356ded5e1f73b4ab2.png" data-download-href="/uploads/short-url/Whm7o3WPWXcc4WnHVeKONqQqki.png?dl=1" title="Screenshot_2019-10-11_16-06-08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/069685a3067dadc0d89f58c356ded5e1f73b4ab2_2_690x228.png" alt="Screenshot_2019-10-11_16-06-08" data-base62-sha1="Whm7o3WPWXcc4WnHVeKONqQqki" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/069685a3067dadc0d89f58c356ded5e1f73b4ab2_2_690x228.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/069685a3067dadc0d89f58c356ded5e1f73b4ab2_2_1035x342.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/069685a3067dadc0d89f58c356ded5e1f73b4ab2.png 2x" data-dominant-color="D5E6F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2019-10-11_16-06-08</span><span class="informations">1055×349 29.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is how it looks like after I imported the rtplan dicom file into Slicer. It shows the modality of the file is RTPLAN.</p>

---

## Post #9 by @gcsharp (2019-10-15 21:05 UTC)

<p>Unfortunately your code snippet doesn’t tell us much.  Can you share the plan object you created?</p>

---

## Post #10 by @gcsharp (2019-10-15 21:13 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="6" data-topic="8698">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<blockquote>
<p>but the resulting object would not be very useful.</p>
</blockquote>
<p>What do you mean?</p>
</blockquote>
</aside>
<p>The plan is not completely imported.  Only the first control point is loaded, also things like beam energy, MU, etc. are not loaded.  That’s why I feel it might not be useful to export such a plan.</p>

---

## Post #11 by @Guangshan_Chen (2019-10-16 16:47 UTC)

<p>Thanks for response. I found the reason. The RTplan exported is RTIonPlan. So it is not recognized as RT loadable. Here is the comments in DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx:<br>
“”"<br>
/* Not yet supported<br>
else if (sopClass == UID_RTTreatmentSummaryRecordStorage)<br>
else if (sopClass == UID_RTIonPlanStorage)<br>
else if (sopClass == UID_RTIonBeamsTreatmentRecordStorage)<br>
*/<br>
“”"<br>
By tacking down, I found a new read function is needed to read RTIonPlan in DCMTK/dcmrt/libsrc/drtplan.cc.</p>

---

## Post #12 by @cpinter (2019-10-16 17:31 UTC)

<p>We have an unfinished implementation for RT Ion Plan import, see progress here: <a href="https://github.com/SlicerRt/SlicerRT/issues/25" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/issues/25</a></p>
<p>It would probably not take too much time to finish it, but it is not high on the priority list. If you’d like to give it a shot, I am happy to prepare you a branch and give you pointers.</p>
<p>If your goal is to have a complete import/export ion plan wofkflow with Slicer, however, it could take significant effort due to the things <a class="mention" href="/u/gcsharp">@gcsharp</a> mentions. Also see my <a href="https://discourse.slicer.org/t/slicerrt-could-not-export-rtplan/8698/2">comment above</a>.</p>

---

## Post #13 by @gcsharp (2019-10-16 17:52 UTC)

<p>Yes, indeed.  Plastimatch is hard-coded to export a plan as an RT Ion Plan.  You can see here:</p>
<p><a href="https://gitlab.com/plastimatch/plastimatch/blob/master/src/plastimatch/base/dcmtk_rtplan.cxx" rel="nofollow noopener">https://gitlab.com/plastimatch/plastimatch/blob/master/src/plastimatch/base/dcmtk_rtplan.cxx</a></p>

---

## Post #14 by @Guangshan_Chen (2019-10-18 17:12 UTC)

<p>Thanks.<br>
For now, I would like to stop here and come back later. If you have any update upon it, please let me know.</p>

---
