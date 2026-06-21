---
topic_id: 47405
title: "NIfTI (.nii.gz) loading failure for TotalSegmentator samples in 3D Slicer 5.10.0 on Apple M4 Pro"
date: 2026-06-20
url: https://discourse.slicer.org/t/47405
last_bumped: 2026-06-20T21:39:13.796Z
---

# NIfTI (.nii.gz) loading failure for TotalSegmentator samples in 3D Slicer 5.10.0 on Apple M4 Pro

**Topic ID**: 47405
**Date**: 2026-06-20
**URL**: https://discourse.slicer.org/t/nifti-nii-gz-loading-failure-for-totalsegmentator-samples-in-3d-slicer-5-10-0-on-apple-m4-pro/47405

---

## Post #1 by @khorlint (2026-06-20 21:39 UTC)

<p><strong>Description:</strong></p>
<p>I am encountering a consistent error when loading multiple samples from the TotalSegmentator dataset in 3D Slicer (version 5.10.0) on an Apple M4 Pro machine.</p>
<p><strong>Environment:</strong></p>
<ul>
<li>3D Slicer version: 5.10.0</li>
<li>OS: macOS (Apple Silicon M4 Pro)</li>
<li>Dataset: TotalSegmentator v201</li>
<li>File format: <code>.nii.gz</code> (NIfTI compressed)</li>
</ul>
<p><strong>Issue:</strong></p>
<p>When attempting to load CT volumes (e.g. <code>s0000/ct.nii.gz</code>), 3D Slicer fails to load the file. This issue is not consistent across the dataset, as other samples load correctly.</p>
<p><strong>Error message:</strong></p>
<pre><code class="lang-auto">Error occurred while loading the selected files.
Click 'Show details' button and check the application log for more information.
Error: Loading /Users/&lt;user&gt;/Documents/Datasets/Totalsegmentator_dataset_v201/s0000/ct.nii.gz - load failed.
</code></pre>
<p><strong>Behavior:</strong></p>
<ul>
<li>The same error occurs across multiple samples, not limited to <code>s0000</code></li>
<li>No additional information is shown in the UI beyond the generic load failure</li>
<li>File paths and dataset structure are correct</li>
</ul>
<p><strong>Expected behavior:</strong></p>
<p>The <code>.nii.gz</code> CT volumes should load normally into Slicer as volumetric data.</p>
<p><strong>Request:</strong></p>
<p>Any insights into:</p>
<ul>
<li>Potential incompatibility with Apple Silicon (M4 Pro) builds</li>
<li>Known issues with <code>.nii.gz</code> loading in Slicer 5.10.0</li>
<li>Required configuration, plugins, or ITK settings</li>
<li>Possible workaround or diagnostic steps</li>
</ul>

---
