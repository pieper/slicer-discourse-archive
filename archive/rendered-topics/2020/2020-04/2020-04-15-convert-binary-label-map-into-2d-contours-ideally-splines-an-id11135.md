---
topic_id: 11135
title: "Convert Binary Label Map Into 2D Contours Ideally Splines An"
date: 2020-04-15
url: https://discourse.slicer.org/t/11135
---

# Convert binary label map into 2D contours (ideally splines) and back

**Topic ID**: 11135
**Date**: 2020-04-15
**URL**: https://discourse.slicer.org/t/convert-binary-label-map-into-2d-contours-ideally-splines-and-back/11135

---

## Post #1 by @jcfr (2020-04-15 22:54 UTC)

<p>From <a class="mention" href="/u/dzenanz">@dzenanz</a>:</p>
<p>Background: we are writing custom application with web UI for segmentation of 2D+time data. The semi-automatic algorithm relying on <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkImageGrowCutSegment.cxx">grow from seeds</a> works well, but not all the time. So manual corrections are needed. Ideally, convert the label map into a 2D spline for each time point, to allow easy interaction. The structure of interest is smooth in these images, so smoothing of splines is a welcome side-effect. Converting that into a fractional label map is preferred over binary label map.</p>
<p>Segmentation module’s <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations">documentation</a> mentions these conversions. It was <a href="https://discourse.slicer.org/t/editing-of-planar-contours-without-converting-to-binary-label-map/9475">already answered</a> that direct editing of contours is not possible with Slicer. Is this still true? How hard would that be with an API, if one exists? Reuse is preferred over reimplementation.</p>
<p>Is conversion from binary label map into planar contours best done by <a href="https://discourse.slicer.org/t/extract-labelmap-contour/410">converting to 3D mesh first</a>, then <a href="https://vtk.org/doc/nightly/html/classvtkCutter.html#details">cutting</a> the mesh? Is that already implemented in Slicer, and where?</p>
<p>Is there an easy or already implemented way of converting the resulting 2D polygon into a spline? Pointers into relevant code are appreciated, as <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRML/vtkLinearSpline.cxx">vtkLinearSpline.cxx</a> does not contain a lot of code.</p>
<p>The last <a href="https://discourse.slicer.org/t/planar-contours-and-binary-label-maps/3778">question about this</a> was two years ago. Did anything important change? Can someone point me to relevant pieces of code for ripping it out of Slicer and into a stand-alone executable?</p>

---

## Post #2 by @jcfr (2020-04-15 22:57 UTC)

<p>From <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>:</p>
<p>I don’t think anything has changed since the previous postings regarding planar contours.</p>
<p>Conversions between different representations are managed by conversion rules, which would be the best place to look for code to reuse:</p>
<p>Slicer: <a href="https://github.com/Slicer/Slicer/tree/master/Libs/vtkSegmentationCore">https://github.com/Slicer/Slicer/tree/master/Libs/vtkSegmentationCore</a></p>
<p>SlicerRT: <a href="https://github.com/SlicerRt/SlicerRT/tree/master/DicomRtImportExport/ConversionRules">https://github.com/SlicerRt/SlicerRT/tree/master/DicomRtImportExport/ConversionRules</a></p>

---

## Post #3 by @jcfr (2020-04-15 23:00 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> Similarly to what we <a href="https://github.com/Slicer/Slicer/pull/4763#issuecomment-603381897">did for vtkAddons</a>, we also talked about moving vtkSegmentationCore into its own repository.</p>
<p>See <a href="https://github.com/Slicer/Slicer/issues/4792">https://github.com/Slicer/Slicer/issues/4792</a></p>
<p>Let me know if expediting this would be helpful for your project.</p>

---

## Post #4 by @cpinter (2020-04-16 08:31 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="11135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Is that already implemented in Slicer, and where?</p>
</blockquote>
</aside>
<p>Storing and managing segmentation data in a series of 2D contours is a legacy method, and so far we only needed it for DICOM-RT Structure Set, and did not want to encourage its use (especially that there is the DICOM Segmentation Object, which is much superior to RTSS). This is why we did not even implement a conversion rule going from labelmap to planar contour, but the code that does the conversion is in the exporter function itself:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2451-L2499">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2451-L2499" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2451-L2499" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2451-L2499</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="2451" style="counter-reset: li-counter 2450 ;">
          <li>std::string studyID = "";
</li>
          <li>vtkIdType firstShItemID = firstExportable-&gt;GetSubjectHierarchyItemID();
</li>
          <li>if (firstShItemID != vtkMRMLSubjectHierarchyNode::INVALID_ITEM_ID)
</li>
          <li>{
</li>
          <li>  vtkIdType studyItemID = shNode-&gt;GetItemAncestorAtLevel(firstShItemID, vtkMRMLSubjectHierarchyConstants::GetDICOMLevelStudy());
</li>
          <li>  if (studyItemID != vtkMRMLSubjectHierarchyNode::INVALID_ITEM_ID)
</li>
          <li>  {
</li>
          <li>    studyInstanceUid = shNode-&gt;GetItemUID(studyItemID, vtkMRMLSubjectHierarchyConstants::GetDICOMUIDName());
</li>
          <li>    studyID = shNode-&gt;GetItemAttribute(studyItemID, vtkMRMLSubjectHierarchyConstants::GetDICOMStudyIDTagName());
</li>
          <li>  }
</li>
          <li>  else
</li>
          <li>  {
</li>
          <li>    vtkWarningMacro("ExportDicomRTStudy: Failed to get ancestor study from exportable with subject hierarchy item ID " + firstExportable-&gt;GetSubjectHierarchyItemID());
</li>
          <li>  }
</li>
          <li>}
</li>
          <li>else
</li>
          <li>{
</li>
          <li>  vtkWarningMacro("ExportDicomRTStudy: Failed to get SH item from exportable with item ID " + firstExportable-&gt;GetSubjectHierarchyItemID());
</li>
          <li>}
</li>
          <li>
</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2451-L2499" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
If you want it could be outsourced though. Any thoughts <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>?</p>
<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="11135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Is there an easy or already implemented way of converting the resulting 2D polygon into a spline? Pointers into relevant code are appreciated, as <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRML/vtkLinearSpline.cxx">vtkLinearSpline.cxx</a> does not contain a lot of code.</p>
<p>The last <a href="https://discourse.slicer.org/t/planar-contours-and-binary-label-maps/3778">question about this</a> was two years ago. Did anything important change? Can someone point me to relevant pieces of code for ripping it out of Slicer and into a stand-alone executable?</p>
</blockquote>
</aside>
<p>With the recent addition of the new Markup type of closed curve this would be much easier to do than before. The only thing we’d need is a converter from/to planar contour segmentations (and the abovementioned labelmap → contours conversion, since the other way is implemented already).</p>

---

## Post #5 by @lassoan (2020-04-16 15:22 UTC)

<p>I agree that current markups curves should be able to handle editing quite well.</p>
<p>We just need an algorithm for getting closed curves from segmentation/slice intersections. It would require two steps:</p>
<ul>
<li>segmentation slicing (cut segmentation with slice): The implementation in the segmentation 2D displayable manager and in the exporter (that <a class="mention" href="/u/cpinter">@cpinter</a> linked above) are about the same and should be usable for simple shapes. For complex cases you would need to use vtkContourTriangulator class but we could not switch to it because it has a small but serious bug that may cause the application hang for invalid inputs (see details here: <a href="https://github.com/Slicer/SlicerGitSVNArchive/pull/1075">https://github.com/Slicer/SlicerGitSVNArchive/pull/1075</a>).</li>
<li>spline fitting: we could create a spline by resampling the linearly interpolated contour at uniform distances and use these as control points</li>
</ul>

---

## Post #6 by @dzenanz (2020-04-17 12:05 UTC)

<p>Thank you all for responses!</p>

---

## Post #7 by @laurabc (2024-12-02 13:26 UTC)

<p>Hello, I was wondering if there have been any updates on this? <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> I would be interested in fitting splines (perhaps using the closed curve markup) and manually refining the segment in the 2D views so that it is reflected smoothly in the 3D segmentation. Is there an existing module that offers this functionality? Any assistance would be greatly appreciated.</p>

---

## Post #8 by @lassoan (2024-12-02 15:46 UTC)

<p>There has been some progress:</p>
<ul>
<li>vtkContourTriangulator now works robustly (does not hang anymore), so it could be used for slicing the segmentation</li>
<li>We have now curve-based segmentation editing in mulitple effects, which could be used as an example. <code>Draw tube</code> and <code>Surface cut</code> effects in <code>SegmentEditorExtraEffects</code> extension use curves/markups to edit segmentation.</li>
</ul>
<p>Therefore, it would now be easier to implement editing segmentations using 2D contours.</p>
<p>Can you write a bit about your use case? I’m just wondering whether the need for spline-based segmentation editing is still there, now that so many “AI” segmentation tools are available. It may be possible that the need is even stronger, because we want to be able to quickly fix up automatic segmentation results. But then maybe what we would really need is 3D surface editing, and not tedious slice-by-slice editing. <code>Surface cut</code> effect does something like this, but it it is quite limited (does not work well for concave shapes; cannot initialize the surface from an existing segmentation).</p>

---

## Post #9 by @cpinter (2024-12-03 12:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="11135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>wondering whether the need for spline-based segmentation editing is still there, now that so many “AI” segmentation tools are available. It may be possible that the need is even stronger, because we want to be able to quickly fix up automatic segmentation results. But then maybe what we would really need is 3D surface editing, and not tedious slice-by-slice editing</p>
</blockquote>
</aside>
<p>Reflecting on this “3D surface editing” topic. I developed something like this almost 20 years ago in MITK. Posting part of a screenshot I have from that time:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dc06c6d1faf1bf12af7607cd7a7a57496adf221.jpeg" data-download-href="/uploads/short-url/b5P1UesQS8wJFmE0Fr69keeQm7n.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dc06c6d1faf1bf12af7607cd7a7a57496adf221_2_690x438.jpeg" alt="image" data-base62-sha1="b5P1UesQS8wJFmE0Fr69keeQm7n" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dc06c6d1faf1bf12af7607cd7a7a57496adf221_2_690x438.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dc06c6d1faf1bf12af7607cd7a7a57496adf221_2_1035x657.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dc06c6d1faf1bf12af7607cd7a7a57496adf221.jpeg 2x" data-dominant-color="494D54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1217×773 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The idea was that you “grow” a ROI on a triangle mesh, starting from a point and including cells as you keep it growing. Then “pull out” or “push in” this patch using a function (in the screenshot Gaussian is selected, but if I remember correctly the alternatives were Sine and Triangle). The goal was manual fixing of automated segmentation results.</p>
<p>It worked nicely, but an awfully complicated surface regularization post-processing step was needed due to the malformed triangles resulting after an operation, and due to possible self-intersections etc.</p>
<p>However, the project was dropped because, at least at that time, it was not considered to be easy enough to use. I was not involved in the testing phase, but you <a class="mention" href="/u/lassoan">@lassoan</a> may have been, as this was part of a collaboration with GE Healthcare and you were one of our contacts at the company back then.</p>

---

## Post #10 by @laurabc (2024-12-05 10:52 UTC)

<p>Yes, what I am looking for is a tool to manually refine automatic segmentations or even for manual labeling. Yes, I mean 3D surface editing, but I think it would be easier to make corrections by “pulling out” or “pushing in” directly from the slice view, while ensuring the corrections are applied to the 3D segmentation.</p>

---

## Post #11 by @cpinter (2024-12-05 11:27 UTC)

<p>In theory something like this could be developed in a way that operates on labelmaps in the end, which is good because 1) that’s the source representation and 2) there won’t be mesh integrity issues. Unfortunately a project like this is not something small, I’d say at the very least a master’s project.</p>

---

## Post #12 by @laurabc (2025-01-07 11:28 UTC)

<p>I’ve been experimenting with the Surface Cut effect, and it’s nearly what I need. Is there a way to import the markup points for the closed curve from a file? If not, how complex would it be to modify it for this purpose? We’re considering it.</p>

---

## Post #13 by @cpinter (2025-01-07 12:54 UTC)

<p>I don’t think you can use a loaded set of points to define the surface using just the GUI. However, you can use the loaded points in the “Markups to Model” module (from the MarkupsToModel extension, which this Segment Editor effect actually uses).</p>

---
