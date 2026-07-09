---
topic_id: 47576
title: "issue with automated dental tools "
date: 2026-07-08
url: https://discourse.slicer.org/t/47576
last_bumped: 2026-07-08T11:07:49.589Z
---

# issue with automated dental tools 

**Topic ID**: 47576
**Date**: 2026-07-08
**URL**: https://discourse.slicer.org/t/issue-with-automated-dental-tools/47576

---

## Post #1 by @deepak_R (2026-07-08 11:07 UTC)

<p>Hello everyone,</p>
<p>I am using <strong>3D Slicer 5.12.0</strong> (also tested with <strong>5.10.0</strong>) and the latest <strong>AutomatedDentalTools</strong> extension from the Extension Manager.</p>
<p>I am trying to run <strong>ALI</strong> on <strong>Carestream CBCT DICOM</strong> data.  The volume loads correctly as <code>3DSlice1.dcm</code>.</p>
<p>However, when I run ALI, the prediction fails.</p>
<h3><a name="p-134791-in-slicer-5120-1" class="anchor" href="#p-134791-in-slicer-5120-1" aria-label="Heading link"></a>In Slicer 5.12.0:</h3>
<pre><code class="lang-auto">
</code></pre>
<pre><code class="lang-auto">ALI_CBCT_preprocess - ERROR - Fatal error during DICOM conversion:
[WinError 267] The directory name is invalid:
.../3DSlice1.dcm
</code></pre>
<p>It appears that ALI is trying to use <code>3DSlice1.dcm</code> as the DICOM directory instead of the original DICOM folder.</p>

---
