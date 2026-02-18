# Inquiry about the 'Auto' Control Mode in qMRMLVolumeThresholdWidget

**Topic ID**: 37232
**Date**: 2024-07-06
**URL**: https://discourse.slicer.org/t/inquiry-about-the-auto-control-mode-in-qmrmlvolumethresholdwidget/37232

---

## Post #1 by @WilliamDaniel (2024-07-06 20:35 UTC)

<p>Dear 3D Slicer Community,</p>
<p>I am a learner of Slicer module development. I am writing to inquire about the underlying principle/algorithm behind the “Auto” option in the Control Mode of the <strong>qMRMLVolumeThresholdWidget</strong>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80e3daf7176cc64a6f04be9591c733730d209433.png" data-download-href="/uploads/short-url/iodiecnT4yVOfzbiL0o4k6mZIIz.png?dl=1" title="Auto control mode" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80e3daf7176cc64a6f04be9591c733730d209433.png" alt="Auto control mode" data-base62-sha1="iodiecnT4yVOfzbiL0o4k6mZIIz" width="690" height="72" data-dominant-color="F1E5E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Auto control mode</span><span class="informations">768×81 2.13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Through tracing the source code in <a href="https://github.com/Slicer/Slicer/blob/9a74906052e41a297ac52cc3cb171663e2e29b29/Libs/MRML/Widgets/qMRMLVolumeThresholdWidget.cxx#L133" rel="noopener nofollow ugc">qMRMLVolumeThresholdWidget.cxx</a> and vtkMRMLScalarVolumeDisplayNode.cxx on GitHub, it appears that the following code snippet in the <strong><a href="https://github.com/Slicer/Slicer/blob/e2e05cec618a77ac30233f83da36a7037c431484/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L783" rel="noopener nofollow ugc">vtkMRMLScalarVolumeDisplayNode.cxx</a></strong> explains the basis of this “Auto” option:</p>
<pre><code class="lang-auto">void vtkMRMLScalarVolumeDisplayNode::CalculateAutoLevels()
{
  if (!this-&gt;GetAutoWindowLevel() &amp;&amp; !this-&gt;GetAutoThreshold())
  {
    vtkDebugMacro("CalculateScalarAutoLevels: " &lt;&lt; (this-&gt;GetID() == nullptr ? "nullid" : this-&gt;GetID())
                  &lt;&lt; ": Auto window level not turned on, returning.");
    return;
  }

  vtkImageData *imageDataScalar = this-&gt;GetScalarImageData();
  if (!imageDataScalar)
  {
    vtkDebugMacro("CalculateScalarAutoLevels: input image data is null");
    return;
  }
  // Make sure the point data is up to date.
  // Remember, the display node pipeline is not connected to a consumer (volume
  // display nodes are cloned by the slice logic) therefore no-one has run the
  // filters.
  if (this-&gt;GetInputImageData())
  {
    this-&gt;GetScalarImageDataConnection()-&gt;GetProducer()-&gt;Update();
  }

  if (!(imageDataScalar-&gt;GetPointData()) ||
      !(imageDataScalar-&gt;GetPointData()-&gt;GetScalars()))
  {
    vtkDebugMacro("CalculateScalarAutoLevels: input image data is null");
    return;
  }

  if (this-&gt;HistogramStatistics == nullptr)
  {
    this-&gt;HistogramStatistics = vtkImageHistogramStatistics::New();

    // Set automatic window/level to include the entire intensity range
    // (except top/bottom 0.1%, to not let a very thin tail of the intensity
    // distribution to decrease the image contrast too much).
    // While in CT and sometimes in MRI, there may be a large empty area
    // outside the reconstructed image, which could be suppressed
    // by a larger lower percentile value, it would make the method
    // too specific to particular imaging modalities and could lead to
    // suboptimal results for other types of images.
    // Therefore, we choose small, symmetric percentile values here
    // and maybe add modality-specific methods later (e.g., for CT
    // images we could set lower value to -1000HU).
    this-&gt;HistogramStatistics-&gt;SetAutoRangePercentiles(0.1, 99.9);

    // Percentiles are very low (0.1%), so there is no need for
    // range expansion.
    this-&gt;HistogramStatistics-&gt;SetAutoRangeExpansionFactors(0.0, 0.0);
  }

  this-&gt;IsInCalculateAutoLevels = true;
  this-&gt;HistogramStatistics-&gt;SetInputData(imageDataScalar);
  this-&gt;HistogramStatistics-&gt;Update();
  double* intensityRange = this-&gt;HistogramStatistics-&gt;GetAutoRange();
  vtkDebugMacro("CalculateScalarAutoLevels:"
                &lt;&lt; " lower: " &lt;&lt; intensityRange[0] &lt;&lt; " upper: " &lt;&lt; intensityRange[1]);

  int disabledModify = this-&gt;StartModify();
  if (this-&gt;GetAutoWindowLevel())
  {
    this-&gt;SetWindowLevelMinMax(intensityRange[0], intensityRange[1]);
  }
  if (this-&gt;GetAutoThreshold())
  {
    this-&gt;SetThreshold(intensityRange[0], intensityRange[1]);
  }
  this-&gt;EndModify(disabledModify);
  this-&gt;IsInCalculateAutoLevels = false;
}
</code></pre>
<p>If my tracking and understanding are correct, the above code snippet appears to primarily perform the following tasks::</p>
<ol>
<li>After loading the image data, ensure that the point data (scalar values) of the image are up to date.</li>
<li>Utilize VTK’s vtkImageHistogramStatistics class to compute the grayscale histogram statistics of the image data, setting the percentiles for the automatic range computation to (0.1, 99.9). This implies that the histogram statistics will includes all values of image intensity except the top/bottom 0.1%.</li>
<li>Update the histogram statistics and invoke the ‘GetAutoRange’ method of the vtkImageHistogramStatistics class to obtain the resulting threshold range.</li>
</ol>
<p>So, it seems that the algorithm behind this ‘Auto’ option is based on custom percentile ranges for the image’s histogram statistics rather than methods like Otsu’s method?</p>
<p>Could you please confirm if my understanding above is correct? Additionally, I would greatly appreciate any further explanation or supplementary details regarding the underlying principle/algorithm of this “Auto” option.</p>
<p>Thank you very much!</p>

---

## Post #2 by @lassoan (2024-07-11 04:36 UTC)

<p>Both window/level and threshold is set by default so that (almost) the entire data range is included in the displayed range.</p>
<p>“Almost” the entire data range, because a little bit above 0th percentile value is used instead of actual minimum voxel value; and instead of maximum scalar value, a little bit below 100th percentile value is used. These percentiles are a bit more robust: they are less sensitive to presence of a few outlier voxels.</p>
<aside class="quote no-group" data-username="WilliamDaniel" data-post="1" data-topic="37232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/williamdaniel/48/13425_2.png" class="avatar"> WilliamDaniel:</div>
<blockquote>
<p>So, it seems that the algorithm behind this ‘Auto’ option is based on custom percentile ranges for the image’s histogram statistics rather than methods like Otsu’s method?</p>
</blockquote>
</aside>
<p>I have not found classic binary thresholding methods (such as Otsu) practically useful. The problem is that the methods solve a quite simple problem in a quite unpredictable way. I’ve made them available in Segment Editor’s <code>Threshold</code> effect (in the <code>Automatic threshold</code> section), but you’ll see that it is hard to find any good use case for them.</p>

---
