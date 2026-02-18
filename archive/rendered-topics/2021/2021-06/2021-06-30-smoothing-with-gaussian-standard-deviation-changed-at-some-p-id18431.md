# Smoothing with Gaussian standard deviation changed at some point

**Topic ID**: 18431
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/smoothing-with-gaussian-standard-deviation-changed-at-some-point/18431

---

## Post #1 by @jamesobutler (2021-06-30 13:57 UTC)

<p>I was using the Smoothing segment editor effect recently and noticed a change in results using a typical value for Gaussian standard deviation mm.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e97a76bd0bfc04f22b6f06e9e79a47d6152c3333.png" alt="image" data-base62-sha1="xjrCWAaPM1g0SNpVmEdam5yvaVR" width="525" height="107"></p>
<p>A commit from Oct 19th, 2020 ( <a href="https://github.com/Slicer/Slicer/commit/52b7208240145c3a6aba99b0a7af0eddaca6f0ff" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add brush option to Segment Editor Smoothing effect · Slicer/Slicer@52b7208 · GitHub</a>) included changes related to setting the standard deviation of the gaussian filter.</p>
<p>Previous Logic:</p>
<pre data-code-wrap="python"><code class="lang-python">standardDeviationMM = self.scriptedEffect.doubleParameter("GaussianStandardDeviationMm")
gaussianFilter = vtk.vtkImageGaussianSmooth()
gaussianFilter.SetStandardDeviation(standardDeviationMM)
</code></pre>
<p>New logic:</p>
<pre data-code-wrap="python"><code class="lang-python">radiusFactor = 4.0
standardDeviationMM = self.scriptedEffect.doubleParameter("GaussianStandardDeviationMm")
spacing = modifierLabelmap.GetSpacing()
standardDeviationPixel = [1.0, 1.0, 1.0]
radiusPixel = [3, 3, 3]
for idx in range(3):
  standardDeviationPixel[idx] = standardDeviationMM / spacing[idx]
  radiusPixel[idx] = int(standardDeviationPixel[idx] * radiusFactor) + 1
gaussianFilter = vtk.vtkImageGaussianSmooth()
gaussianFilter.SetStandardDeviation(*standardDeviationPixel)
</code></pre>
<p>Is the changes to setting a pixel value to standard deviation correct rather than a MM value? Had it been previously wrong for so long? Or was there a change in VTK about the input type of <code>SetStandardDeviation</code>?</p>
<p>It appears it was doing <code>gaussianFilter.SetStandardDeviation(standardDeviationMm)</code> since Segment Editor was introduced (<a href="https://github.com/Slicer/Slicer/commit/3ab0eab7cb41e23634c8f8f2b789b6531f0b6605" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add new segmentations infrastructure · Slicer/Slicer@3ab0eab · GitHub</a>) back in 2016.</p>

---

## Post #2 by @jamesobutler (2021-06-30 23:24 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="18431">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><code>vtkImageGaussianSmooth</code></p>
</blockquote>
</aside>
<p>Reviewing the filter documentation for VTK 9 it appears that the standard deviation is indeed in Pixels and that likely the Slicer code had been wrong for a long time. <a href="https://vtk.org/doc/nightly/html/classvtkImageGaussianSmooth.html" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkImageGaussianSmooth Class Reference</a></p>

---

## Post #3 by @lassoan (2021-07-01 13:05 UTC)

<p>Yes, I noticed the issue and fixed it when I implemented and tested the smoothing brush. When the standard deviation happened to be rounded to an even number then the kernel was not symmetric, and a half-voxel shift was visible. Gaussian smoothing is a very blunt tool (removes a lot of information content), therefore the parameter has to be set based on visual appearance anyway, and so the scaling change should not cause major trouble.</p>
<p>Thanks for bringing this up, I’ve added a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Smoothing_effect">note to the migration guide</a> to clarify this.</p>

---

## Post #4 by @jamesobutler (2021-07-01 13:18 UTC)

<p>Great idea for adding it to the migration guide!</p>

---
