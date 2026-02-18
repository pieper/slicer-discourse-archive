# TotalSegmentator Licensed Tasks Not Appearing in 3D Slicer Interface

**Topic ID**: 43523
**Date**: 2025-06-27
**URL**: https://discourse.slicer.org/t/totalsegmentator-licensed-tasks-not-appearing-in-3d-slicer-interface/43523

---

## Post #1 by @Guilherme_Augusto (2025-06-27 13:21 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/713c853d7f1418511674c4dc640e909259465991.png" data-download-href="/uploads/short-url/g9JCma7cIp8RZT2KcPk5KVGcdOx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/713c853d7f1418511674c4dc640e909259465991.png" alt="image" data-base62-sha1="g9JCma7cIp8RZT2KcPk5KVGcdOx" width="506" height="202"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">506×202 7.24 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h1><a name="p-126357-totalsegmentator-licensed-tasks-not-appearing-in-3d-slicer-interface-1" class="anchor" href="#p-126357-totalsegmentator-licensed-tasks-not-appearing-in-3d-slicer-interface-1" aria-label="Heading link"></a><strong>TotalSegmentator Licensed Tasks Not Appearing in 3D Slicer Interface</strong></h1>
<h2><a name="p-126357-problem-description-2" class="anchor" href="#p-126357-problem-description-2" aria-label="Heading link"></a><strong>Problem Description</strong></h2>
<p>I have TotalSegmentator v2.10.0 installed and working via Python API in 3D Slicer 5.7.0, but licensed tasks like <code>thigh_shoulder_muscles</code> and <code>thigh_shoulder_muscles_mr</code> do not appear in the module interface dropdown, even though I have a valid academic license configured.</p>
<h2><a name="p-126357-system-information-3" class="anchor" href="#p-126357-system-information-3" aria-label="Heading link"></a><strong>System Information</strong></h2>
<ul>
<li><strong>3D Slicer Version</strong>: 5.7.0-2024-11-06</li>
<li><strong>Operating System</strong>: Windows 10 (22631)</li>
<li><strong>TotalSegmentator Version</strong>: 2.10.0 (confirmed via pip)</li>
<li><strong>Python Environment</strong>: PythonSlicer.exe</li>
<li><strong>GPU</strong>: NVIDIA RTX 4060 Laptop (CUDA 12.9)</li>
</ul>
<h2><a name="p-126357-what-ive-tried-4" class="anchor" href="#p-126357-what-ive-tried-4" aria-label="Heading link"></a><strong>What I’ve Tried</strong></h2>
<ol>
<li>
<p><strong>License Configuration</strong>:</p>
<ul>
<li>Successfully configured academic license (<code>aca_65EL3LSCMMNB9J</code>) via config.json</li>
<li>License verification works in Python API</li>
<li>File location: <code>~/.totalsegmentator/config.json</code></li>
</ul>
</li>
<li>
<p><strong>Module Reinstallation</strong>:</p>
<ul>
<li>Uninstalled and reinstalled TotalSegmentator extension via Slicer</li>
<li>Confirmed v2.10.0 is installed</li>
<li>Restarted Slicer multiple times</li>
</ul>
</li>
<li>
<p><strong>Python API Testing</strong>:</p>
<ul>
<li>Basic tasks work perfectly (<code>total</code>, <code>total_mr</code>)</li>
<li>Licensed tasks fail with license validation hanging</li>
<li>Non-licensed tasks execute successfully</li>
</ul>
</li>
</ol>
<h2><a name="p-126357-current-behavior-5" class="anchor" href="#p-126357-current-behavior-5" aria-label="Heading link"></a><strong>Current Behavior</strong></h2>
<ul>
<li><strong>Interface</strong>: Only shows non-licensed tasks in dropdown (see screenshot)</li>
<li><strong>Python API</strong>: Licensed tasks start but hang during license validation</li>
<li><strong>Error Message</strong>: No explicit errors, just license validation prompt</li>
</ul>
<h2><a name="p-126357-expected-behavior-6" class="anchor" href="#p-126357-expected-behavior-6" aria-label="Heading link"></a><strong>Expected Behavior</strong></h2>
<p>Licensed tasks like <code>thigh_shoulder_muscles</code> and <code>thigh_shoulder_muscles_mr</code> should appear in the task dropdown when a valid academic license is configured.</p>
<h2><a name="p-126357-questions-7" class="anchor" href="#p-126357-questions-7" aria-label="Heading link"></a><strong>Questions</strong></h2>
<ol>
<li>
<p><strong>License Integration</strong>: How does the Slicer extension read the TotalSegmentator license configuration? Does it use the same <code>~/.totalsegmentator/config.json</code> file?</p>
</li>
<li>
<p><strong>Task Discovery</strong>: Is there a way to force the extension to re-scan available tasks after license configuration?</p>
</li>
<li>
<p><strong>Alternative Configuration</strong>: Is there a Slicer-specific way to configure the TotalSegmentator license within the extension interface?</p>
</li>
<li>
<p><strong>Version Compatibility</strong>: Could there be a version mismatch between the Slicer extension and the installed TotalSegmentator Python package?</p>
</li>
</ol>
<h2><a name="p-126357-minimal-reproduction-8" class="anchor" href="#p-126357-minimal-reproduction-8" aria-label="Heading link"></a><strong>Minimal Reproduction</strong></h2>
<pre data-code-wrap="python"><code class="lang-python"># This works (non-licensed)
from totalsegmentator.python_api import totalsegmentator
result = totalsegmentator(input="test.nii.gz", output="output/", task="total_mr")

# This hangs during license validation (licensed)
result = totalsegmentator(input="test.nii.gz", output="output/", task="thigh_shoulder_muscles_mr")
</code></pre>
<h2><a name="p-126357-additional-context-9" class="anchor" href="#p-126357-additional-context-9" aria-label="Heading link"></a><strong>Additional Context</strong></h2>
<p>I’m working on a research project for automatic rotator cuff muscle segmentation and specifically need access to the <code>thigh_shoulder_muscles_mr</code> task for MR images. The task exists and is documented in TotalSegmentator v2.10.0, but the Slicer integration seems to have issues with licensed task discovery.</p>
<p>Any help would be greatly appreciated! Is this a known issue with the current TotalSegmentator extension, or am I missing a configuration step?</p>

---

## Post #2 by @Romulo_Alfaro (2025-08-05 04:00 UTC)

<p>Hi, were you able to resolve this? I’m having the same problem.</p>

---

## Post #3 by @bulala (2025-09-22 01:59 UTC)

<p>+1  I’m having the same problem.</p>

---
