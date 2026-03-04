---
topic_id: 46371
title: "Grow From Seed Error Exceeded Max Number Of Voxels"
date: 2026-03-04
url: https://discourse.slicer.org/t/46371
---

# Grow from seed error — exceeded max number of voxels

**Topic ID**: 46371
**Date**: 2026-03-04
**URL**: https://discourse.slicer.org/t/grow-from-seed-error-exceeded-max-number-of-voxels/46371

---

## Post #1 by @Antmaker (2026-03-04 00:20 UTC)

<p>I was trying to use the grow-from-seed effect in the Segment Editor module and keep encountering this error.</p>
<p>At first I thought this was due to not having enough RAM, thus I’ve increased my system’s memory from 195GB to 585GB, but the issue still persist.</p>
<p>Thus, it seems that I have hit the limitation of the grow-from-seed effect here? Is there any way to increase the max number of voxels?</p>
<h2><a name="p-132417-error-output-1" class="anchor" href="#p-132417-error-output-1" aria-label="Heading link"></a>Error output</h2>
<pre data-code-wrap="bash"><code class="lang-bash">self.extentGrowthRatio = 0.1
masterImageExtent = (0, 2183, 0, 1884, 0, 2229)
labelsEffectiveExtent = (0, 2183, 0, 1884, 0, 2229)
labelsExpandedExtent = [0, 2183, 0, 1884, 0, 2229]
"3D Slicer has caught an application error, please save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at https://slicer.org\n\n\nThe message detail is:\n\nException thrown in event: /work/Stable/Slicer-0-build/ITK/Modules/Remote/GrowCut/include/itkFastGrowCut.hxx:411:\nITK ERROR: FastGrowCut(0xca91e70): Image size is too large (9180553200 voxels). Maximum number of voxels is 4294967294."
</code></pre>

---

## Post #2 by @jumbojing (2026-03-04 01:37 UTC)

<h3><a name="p-132418-regarding-grow-from-seed-limitation-1" class="anchor" href="#p-132418-regarding-grow-from-seed-limitation-1" aria-label="Heading link"></a>Regarding Grow-from-Seed Limitation:</h3>
<p>Your dataset dimensions (2184 × 1885 × 2230 ≈ <strong>9.2 billion voxels</strong>) exceeds the practical limit of the grow-from-seed algorithm. This is <strong>not a memory issue</strong> but an <strong>algorithmic complexity issue</strong>:</p>
<ul>
<li>Grow-from-seed has O(n³) to O(n⁴) complexity</li>
<li>Large datasets cause extremely slow computation or crashes</li>
</ul>
<p><strong>Recommended Solutions:</strong></p>
<ol>
<li><strong>Downsample</strong>: Resample the volume by 2x-4x before segmentation</li>
<li><strong>Crop ROI</strong>: Use Crop Volume to focus on the region of interest</li>
<li><strong>Use Alternative Methods</strong>:
<ul>
<li>Threshold segmentation (for bones like we did)</li>
<li>Deep learning (TotalSegmentator extension)</li>
<li>Level set / Region growing (with smaller seed regions)</li>
</ul>
</li>
</ol>
<hr>
<h3><a name="p-132418-disclaimer-2" class="anchor" href="#p-132418-disclaimer-2" aria-label="Heading link"></a>Disclaimer</h3>
<blockquote>
<p><strong>This AI assistant provides suggestions and code for 3D Slicer operations based on available information. Users are responsible for verifying the accuracy and appropriateness of any actions taken. The authors and developers assume no liability for any damage, data loss, or other issues that may arise from using these suggestions. Always save your work and back up important data before executing any operations. Medical imaging analysis results should be validated by qualified professionals before clinical use.</strong></p>
</blockquote>
<p>FROM: <a href="https://github.com/jumbojing/slicerClaw" class="inline-onebox" rel="noopener nofollow ugc">GitHub - jumbojing/slicerClaw: A revolutionary, lightning-fast AI assistant natively integrated into 3D Slicer. · GitHub</a></p>

---
