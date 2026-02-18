#  Issue with Resliced Images from SPM12 Not Reflecting Alignment in 3D Slicer

**Topic ID**: 40716
**Date**: 2024-12-16
**URL**: https://discourse.slicer.org/t/issue-with-resliced-images-from-spm12-not-reflecting-alignment-in-3d-slicer/40716

---

## Post #1 by @Akihito (2024-12-16 15:00 UTC)

<p>I am currently evaluating the effects of hypertensive disorders of pregnancy on white matter in children using pediatric brain MRI data and 3D Slicer. After performing image alignment on 3DT1 images using SPM12, I noticed that the alignment adjustments were not reflected when checking the images in 3D Slicer.</p>
<h3><a name="p-120583-steps-taken-1" class="anchor" href="#p-120583-steps-taken-1" aria-label="Heading link"></a>Steps Taken:</h3>
<ol>
<li>In SPM12, I used the <strong>Display</strong> tab to load the images and adjusted the <code>pitch, roll, and yaw</code> values for alignment.</li>
</ol>
<ul>
<li>The alignment values were within approximately ±0.2, with fine adjustments in the range of 0.0X.</li>
</ul>
<ol start="2">
<li>After performing the alignment, I executed <strong>reslice</strong> processing and then loaded the images into 3D Slicer.</li>
</ol>
<ul>
<li><strong>Result:</strong> The alignment adjustments were not reflected.</li>
</ul>
<h3><a name="p-120583-test-results-2" class="anchor" href="#p-120583-test-results-2" aria-label="Heading link"></a>Test Results:</h3>
<ul>
<li><code>pitch = 0.5</code> → The alignment was reflected correctly.</li>
<li><code>pitch = 0.4</code> → The alignment was reflected, but the output image was identical to the one generated with <code>pitch = 0.5</code>.</li>
<li><code>pitch = 0.3</code> → The alignment was reflected, but again identical to the <code>pitch = 0.5</code> image.</li>
<li><code>pitch = 0.2</code> → The alignment was <strong>not</strong> reflected.</li>
</ul>
<p>From these results, I suspect that the <code>pitch</code> values are being rounded, as follows:<br>
<code>0.1 → 0, 0.2 → 0, 0.3 → 0.5, 0.4 → 0.5, 0.5 → 0.5</code>.</p>
<hr>
<h3><a name="p-120583-question-3" class="anchor" href="#p-120583-question-3" aria-label="Heading link"></a>Question:</h3>
<p>Could you advise me on the appropriate steps or settings to ensure that the alignment results from SPM12 are accurately reflected when viewed in 3D Slicer?</p>

---

## Post #2 by @lassoan (2024-12-16 15:17 UTC)

<p>How did you conclude that the alignment asjustments were not reflected in Slicer? What you expected to see and what you saw instead?</p>
<p>What file format have you used? NIFTI file format has a flaw that image orientation can be specified redundant ways and each software interprets ambiguous cases differently. If you are using NIFTI and not familiar with qform and sform already, then it could be useful if you could read up a bit on it and then investigate how SPM changes the files during alignment.</p>
<p>We could look into this alsonif you share the files (image before and after alignment) by uploading to dropbox, onedrive, etc. and post the link here; or at least print the headers of the two files and copy it here.</p>

---
