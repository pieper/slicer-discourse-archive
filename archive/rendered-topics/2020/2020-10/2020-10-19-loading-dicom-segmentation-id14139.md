---
topic_id: 14139
title: "Loading Dicom Segmentation"
date: 2020-10-19
url: https://discourse.slicer.org/t/14139
---

# Loading DICOM segmentation

**Topic ID**: 14139
**Date**: 2020-10-19
**URL**: https://discourse.slicer.org/t/loading-dicom-segmentation/14139

---

## Post #1 by @yoomi (2020-10-19 15:06 UTC)

<p>Hi, I’m having some trouble loading certain DICOM segmentation’s into the Slicer scene. Importing the file is no problem (imported using DICOM database), but the error log says “could not load: [filename] as a DICOMSegmentation”. Does anyone know why this might be? Thanks</p>

---

## Post #2 by @lassoan (2020-10-19 15:17 UTC)

<p>If you only have this problem with certain segmentation files then we need one of those files so that we can investigate. You can upload the files anywhere and post the link here (make sure no patient health information is in the files).</p>

---

## Post #3 by @fedorov (2020-10-20 02:03 UTC)

<p>If you cannot share the files, it may also be helpful to share the full error log (Help &gt; Report a bug).</p>
<p>Are you able to load some DICOM segmentations, but not others, or you cannot load any?</p>

---

## Post #4 by @yoomi (2020-10-23 14:09 UTC)

<p>Hello, here is an example of a segmentation file that I am unable to upload. The full error message is just “could not load as a DICOMSegmentation”. Thanks everyone for your help.</p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1XfVcJ3DVLo6areLoOWZ72b3e-QPpZ-79/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1XfVcJ3DVLo6areLoOWZ72b3e-QPpZ-79/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1XfVcJ3DVLo6areLoOWZ72b3e-QPpZ-79/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">segmentation.dcm</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @fedorov (2020-10-23 14:32 UTC)

<p>Thank you, I can reproduce the problem.</p>
<p>I believe the segmentation series here is the one with SeriesDescription “VOI PE Segmentation thresh=70” from this study available on IDC: <a href="https://viewer.imaging.datacommons.cancer.gov/viewer/1.3.6.1.4.1.14519.5.2.1.7695.1700.186130315530827043916665138479">https://viewer.imaging.datacommons.cancer.gov/viewer/1.3.6.1.4.1.14519.5.2.1.7695.1700.186130315530827043916665138479</a>.</p>
<p>There are several issues:</p>
<ul>
<li>the MR series corresponding to this segmentation is a 4D series</li>
<li>the segmentation is encoded as FRACTIONAL</li>
</ul>
<p>It looks like this combination is not handled well at the moment by either Slicer or IDC/OHIF Viewer.</p>

---

## Post #6 by @lassoan (2020-10-23 16:45 UTC)

<p>Loading 4D MRI series should work well in Slicer already. Slicer can also represent FRACTIONAL segmentations, although right now fractional segmentations are still just loaded as binary. So, all segmentations should be possible to load.</p>
<p>The problem with this file is that it contains an empty segmentation. It has a single slice, with all zero values. Probably it is just a placeholder.</p>
<p>While checking this, I’ve found a bug in the segmentation importer for loading single-frame segmentations, and I’ve submitted a <a href="https://github.com/QIICR/dcmqi/pull/407">fix</a>.</p>

---

## Post #7 by @fedorov (2020-10-23 17:27 UTC)

<p>Andras, thank you for the fix. I merged it. I don’t think it will solve the underlying issue for the user though. We need to add a check to the SEG DICOM plugin to account for the situation when the segment is empty. I admit I didn’t even think of a possibility of someone saving a segment that is blank. Thank you for investigating this so quickly!</p>

---

## Post #8 by @lassoan (2020-10-23 17:34 UTC)

<p>In this case, there was nothing in the segmentation, so the user got all that was available (nothing).</p>
<p>But yes, the importer has to be prepared for blank segments. For example, if a segmentation has blank and non-blank segments, probably import stops due to the failed import of the first blank segment and the rest of the segments are not imported. At least we should file submit a bug report to QuantitativeReporting to remember to fix this at some point.</p>

---

## Post #9 by @fedorov (2020-10-23 17:40 UTC)

<p>I’ve just added a quick fix here: <a href="https://github.com/QIICR/QuantitativeReporting/commit/1ca31ce1681f9e04dc3129fdca42abe815c31e06" class="inline-onebox">BUG: add a check for the number of segments · QIICR/QuantitativeReporting@1ca31ce · GitHub</a></p>
<p>I confirmed with this fix there is no error, segmentation node is created, but has no segments, and there is a warning in the error log. I think now the behavior of the application makes sense.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1401434b527cc23b5f72eafb307983a64095c31b.png" alt="image" data-base62-sha1="2QYfOzpztCjDDSWaNZEQjc42Qk3" width="555" height="212"></p>

---

## Post #10 by @lassoan (2020-10-23 17:52 UTC)

<p>It could be nice to create the segment anyway and set its name, color, terminology, etc. instead of skipping it completely (if it is easy to implement).</p>

---

## Post #11 by @fedorov (2020-10-23 17:57 UTC)

<p>Yes, I agree it would be nice, and it’s an interesting “hack” to work around the lack of an equivalent of a “pick list” in DICOM SEG/SR.</p>
<p>I believe at the moment the behavior of empty segment import is such that no empty segment is created. The corresponding line is highlighted below. I think this would need to be implemented in the segmentations logic. I do not know how difficult it would be to implement.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/QIICR/QuantitativeReporting/blob/1ca31ce1681f9e04dc3129fdca42abe815c31e06/DICOMPlugins/DICOMSegmentationPlugin.py#L225" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/QuantitativeReporting/blob/1ca31ce1681f9e04dc3129fdca42abe815c31e06/DICOMPlugins/DICOMSegmentationPlugin.py#L225" target="_blank" rel="noopener">QIICR/QuantitativeReporting/blob/1ca31ce1681f9e04dc3129fdca42abe815c31e06/DICOMPlugins/DICOMSegmentationPlugin.py#L225</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="215" style="counter-reset: li-counter 214 ;">
<li>  for segmentLabelNode in segmentLabelNodes:</li>
<li>    self._importSegmentAndRemoveLabel(segmentLabelNode, segmentationNode)</li>
<li>
</li><li>  self.addSeriesInSubjectHierarchy(loadable, segmentationNode)</li>
<li>  if hasattr(loadable, "referencedSeriesUID"):</li>
<li>    self._findAndSetGeometryReference(loadable.referencedSeriesUID, segmentationNode)</li>
<li>
</li><li>def _importSegmentAndRemoveLabel(self, segmentLabelNode, segmentationNode):</li>
<li>  segmentationsLogic = slicer.modules.segmentations.logic()</li>
<li>  segmentation = segmentationNode.GetSegmentation()</li>
<li class="selected">  success = segmentationsLogic.ImportLabelmapToSegmentationNode(segmentLabelNode, segmentationNode)</li>
<li>  if segmentation.GetNumberOfSegments() == 0:</li>
<li>      logging.warning("Empty segment loaded from DICOM SEG!")</li>
<li>  if success and segmentation.GetNumberOfSegments()&gt;0:</li>
<li>    segment = segmentation.GetNthSegment(segmentation.GetNumberOfSegments() - 1)</li>
<li>    segment.SetName(segmentLabelNode.GetAttribute("Name"))</li>
<li>    segment.SetTag("Description", segmentLabelNode.GetAttribute("Description"))</li>
<li>    segment.SetColor([float(segmentLabelNode.GetAttribute("ColorR")),</li>
<li>                      float(segmentLabelNode.GetAttribute("ColorG")),</li>
<li>                      float(segmentLabelNode.GetAttribute("ColorB"))])</li>
<li>    segment.SetTag(vtkSegmentationCore.vtkSegment.GetTerminologyEntryTagName(),</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #12 by @lassoan (2020-10-23 18:46 UTC)

<p>It would be hard to tell what and how many empty segments <code>segmentationsLogic.ImportLabelmapToSegmentationNode</code> should create. We could add an option that would create an empty segment for each entry defined in the color node associated with the input labelmap. But this would be quite a special case, so I’m not sure if it would worth the time to implement.</p>
<p>Instead DICOMSegmentationPlugin could be updated so that if <code>_importSegmentAndRemoveLabel</code> returns an empty segmentation then it adds a new segment (using <a href="http://apidocs.slicer.org/master/classvtkSegmentation.html#aabe215076719c40187dc6d3902afbc9c"><code>segmentationNode.GetSegmentation().AddSegment(...)</code></a>).</p>

---

## Post #13 by @fedorov (2020-10-23 19:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="14139">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be hard to tell what and how many empty segments <code>segmentationsLogic.ImportLabelmapToSegmentationNode</code> should create.</p>
</blockquote>
</aside>
<p>This actually would be very easy, since when dcmqi converts DICOM SEG, each segment is saved into a separate file. So when that import function is called on a label map, the label map has one and only segment.</p>
<p>In any case, I created a ticket to keep track of this idea, if/when we get to it: <a href="https://github.com/QIICR/QuantitativeReporting/issues/253" class="inline-onebox">Create empty Slicer segmentation segments when empty segments are imported from DICOM SEG · Issue #253 · QIICR/QuantitativeReporting · GitHub</a>.</p>

---
