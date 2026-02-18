# Exporting multiple dose distributions to DICOM

**Topic ID**: 19101
**Date**: 2021-08-06
**URL**: https://discourse.slicer.org/t/exporting-multiple-dose-distributions-to-dicom/19101

---

## Post #1 by @sokol (2021-08-06 12:40 UTC)

<p>Dear Slicer experts,</p>
<p>I am working with a research treatment planning system, and my CTs, as well as the dose distributions, are in the .nrrd format, and I need to convert them to DICOM.</p>
<p>So far I’ve been following the steps described here <a href="https://discourse.slicer.org/t/convert-image-and-segmentation-to-dicom/543" class="inline-onebox">Convert image and segmentation to DICOM</a> which worked wonderfully, and as an output I get a series of .dcm files for my CT, one file for contours, and one file for the dose distribution.</p>
<p>However, I am now producing several different dose distributions from one treatment plan, and I would like to export all of them to DICOM. If I repeat the steps described above and drag all my dose distributions under the same study and do Export, I still get only one RT Dose file in the destination folder.</p>
<p>Thus, I was wondering if there is any additional step required to have multiple dose distributions exported at once? Or there is no such option, and the only thing left to do is to repeat conversion for each of the dose file separately?</p>
<p>Many thanks in advance for your advice!<br>
Regards,<br>
Olga</p>
<p>Operating system: Linux<br>
Slicer version: 4.8.1 r26813</p>

---

## Post #2 by @lassoan (2021-08-07 17:31 UTC)

<p>DICOM RT exporter probably assumes that there is only a single dose volume series per study. It may be either due to a limitation of Plastimatch (that SlicerRT uses for DICOM export) or it is implemented like this in SlicerRT because this need has not come up before.</p>
<p><a class="mention" href="/u/gcsharp">@gcsharp</a> can Plastimatch export multiple dose volumes series in a single study?</p>

---

## Post #3 by @cpinter (2021-08-09 15:19 UTC)

<p>As far as I remember, the exporter expects a CT, dose, RTSS triplet and there needs to be exactly one of each.</p>

---

## Post #4 by @lassoan (2021-08-09 15:28 UTC)

<p>Do you mean the exporter in <em>Plastimatch</em> requires this triplet or the exporter in Slicer?<br>
If it is a limitation in Plastimatch then <a class="mention" href="/u/gcsharp">@gcsharp</a> would need to improve the API before the feature can be added in Slicer.</p>

---

## Post #5 by @cpinter (2021-08-10 13:36 UTC)

<p>It is a limitation in Plastimatch (that said the implementation in Slicer also would have to be improved a bit if this was added in Plastimatch).</p>
<p>I just checked the code. This single object passing is there at the lowest levels as well. This is how we pass the dose volume to the writer in SlicerRT:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2638">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2638" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2638" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L2638</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="2628" style="counter-reset: li-counter 2627 ;">
          <li>    doseOrientedImageData-&gt;SetGeometryFromImageToWorldMatrix(identityMatrix);
</li>
          <li>  }
</li>
          <li>  // Set anatomical image to RT writer
</li>
          <li>  Plm_image::Pointer dose_img = PlmCommon::ConvertVtkOrientedImageDataToPlmImage(doseOrientedImageData);
</li>
          <li>  if (dose_img-&gt;dim(0) * dose_img-&gt;dim(1) * dose_img-&gt;dim(2) == 0)
</li>
          <li>  {
</li>
          <li>    error = "Failed to convert dose volume to Plastimatch format";
</li>
          <li>    vtkErrorMacro("ExportDicomRTStudy: " + error);
</li>
          <li>    return error;
</li>
          <li>  }
</li>
          <li class="selected">  rtWriter-&gt;SetDose(dose_img);
</li>
          <li>}
</li>
          <li>
</li>
          <li>// Convert input segmentation to the format Plastimatch can use
</li>
          <li>if (segmentationNode)
</li>
          <li>{
</li>
          <li>  // If master representation is labelmap type, then export binary labelmap
</li>
          <li>  vtkSegmentation* segmentation = segmentationNode-&gt;GetSegmentation();
</li>
          <li>  if (segmentation-&gt;IsMasterRepresentationImageData())
</li>
          <li>  {
</li>
          <li>    // Make sure segmentation contains binary labelmap
</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
And this is how the Plastimatch writer uses it:</p><aside class="onebox gitlabblob" data-onebox-src="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/plastimatch/base/rtds_dcmtk.cxx#L53">
  <header class="source">

      <a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/plastimatch/base/rtds_dcmtk.cxx#L53" target="_blank" rel="noopener">gitlab.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/plastimatch/base/rtds_dcmtk.cxx#L53" target="_blank" rel="noopener">plastimatch/plastimatch/-/blob/master/src/plastimatch/base/rtds_dcmtk.cxx#L53</a></h4>

  <pre><code class="lang-"></code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
A single CT / RTSS / dose object all along the way.</p>

---
