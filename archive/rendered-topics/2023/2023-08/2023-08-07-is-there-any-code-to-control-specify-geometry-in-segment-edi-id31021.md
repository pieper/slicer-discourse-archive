---
topic_id: 31021
title: "Is There Any Code To Control Specify Geometry In Segment Edi"
date: 2023-08-07
url: https://discourse.slicer.org/t/31021
---

# Is there any code to control 'specify geometry in Segment editor?

**Topic ID**: 31021
**Date**: 2023-08-07
**URL**: https://discourse.slicer.org/t/is-there-any-code-to-control-specify-geometry-in-segment-editor/31021

---

## Post #1 by @telomere (2023-08-07 08:35 UTC)

<p>I made a shortcut to go Segment Editor module and automatically load source volume and add segmentation and segment.<br>
In this situation, I also want to control “specify geometry” button which is next to source volume.<br>
I want to choose ROI that I made previously and set spacing as 0.15mm.<br>
But I never could find the function codes for controlling ‘specify geometry’ <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>I also saw the script of Segment Editor module but I can’t find the ‘specify geometry’ part…</p>

---

## Post #2 by @simonoxen (2023-08-07 09:07 UTC)

<p>hi, not an expert here, but this test seems to have examples that could help:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/7ef59614c2458e4f693ab77834e6726cf6ae0540/Modules/Loadable/Segmentations/Testing/Python/SegmentationWidgetsTest1.py#L171">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/7ef59614c2458e4f693ab77834e6726cf6ae0540/Modules/Loadable/Segmentations/Testing/Python/SegmentationWidgetsTest1.py#L171" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/7ef59614c2458e4f693ab77834e6726cf6ae0540/Modules/Loadable/Segmentations/Testing/Python/SegmentationWidgetsTest1.py#L171" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/7ef59614c2458e4f693ab77834e6726cf6ae0540/Modules/Loadable/Segmentations/Testing/Python/SegmentationWidgetsTest1.py#L171</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="161" style="counter-reset: li-counter 160 ;">
          <li>    if imageData is None:</li>
          <li>        logging.error('Invalid input image data')</li>
          <li>        return False</li>
          <li>    imageAccumulate = vtk.vtkImageAccumulate()</li>
          <li>    imageAccumulate.SetInputData(imageData)</li>
          <li>    imageAccumulate.SetIgnoreZero(1)</li>
          <li>    imageAccumulate.Update()</li>
          <li>    return imageAccumulate.GetVoxelCount()</li>
          <li></li>
          <li># ------------------------------------------------------------------------------</li>
          <li class="selected">def TestSection_03_qMRMLSegmentationGeometryWidget(self):</li>
          <li>    logging.info('Test section 2: qMRMLSegmentationGeometryWidget')</li>
          <li></li>
          <li>    binaryLabelmapReprName = slicer.vtkSegmentationConverter.GetBinaryLabelmapRepresentationName()</li>
          <li>    closedSurfaceReprName = slicer.vtkSegmentationConverter.GetClosedSurfaceRepresentationName()</li>
          <li></li>
          <li>    # Use MRHead and Tinypatient for testing</li>
          <li>    import SampleData</li>
          <li>    mrVolumeNode = SampleData.downloadSample("MRHead")</li>
          <li>    [tinyVolumeNode, tinySegmentationNode] = SampleData.downloadSamples('TinyPatient')</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also using ROIs as inputs</p>

---
