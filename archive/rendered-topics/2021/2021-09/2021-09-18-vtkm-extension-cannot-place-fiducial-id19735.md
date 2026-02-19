---
topic_id: 19735
title: "Vtkm Extension Cannot Place Fiducial"
date: 2021-09-18
url: https://discourse.slicer.org/t/19735
---

# vtkm Extension: Cannot Place Fiducial

**Topic ID**: 19735
**Date**: 2021-09-18
**URL**: https://discourse.slicer.org/t/vtkm-extension-cannot-place-fiducial/19735

---

## Post #1 by @adamgranthendry (2021-09-18 01:54 UTC)

<h3><a name="p-66464-problem-1" class="anchor" href="#p-66464-problem-1" aria-label="Heading link"></a>Problem:</h3>
<p>I cannot place fiducials on my 3D STL model for extracting centerlines. Please let me know if I am performing a step incorrectly.</p>
<h3><a name="p-66464-system-2" class="anchor" href="#p-66464-system-2" aria-label="Heading link"></a>System:</h3>
<p><strong>OS:</strong> Windows 10<br>
<strong>3D Slicer:</strong> 4.10.2</p>
<h3><a name="p-66464-steps-to-reproduce-3" class="anchor" href="#p-66464-steps-to-reproduce-3" aria-label="Heading link"></a>Steps to Reproduce</h3>
<ol>
<li>
<p>Choose file to add  (<code>data.stl</code>)<br>
<img src="https://user-images.githubusercontent.com/77850046/133849893-3a8f2661-6fca-49fe-99c2-f908159b02bf.png" alt="image" width="480" height="281"></p>
</li>
<li>
<p>Load the data as a <code>Model</code><br>
<img src="https://user-images.githubusercontent.com/77850046/133850043-d9a23ffc-f6d5-40cc-a4da-ae89217bb3e2.png" alt="image" width="480" height="282"></p>
</li>
<li>
<p>Convert Model to Segmentation Node</p>
</li>
</ol>
<p><img src="https://user-images.githubusercontent.com/77850046/133850270-e31d9c48-5487-431e-a818-eec29ac8098c.png" alt="image" width="432" height="270"></p>
<ol start="4">
<li>Open the Centerline Computation module</li>
</ol>
<p><img src="https://user-images.githubusercontent.com/77850046/133850415-37a4848e-9c43-4ed4-9b69-91a5b87772a7.png" alt="image" width="458" height="500"></p>
<ol start="5">
<li>Choose <code>data</code> as the <code>Vessel tree model</code> and choose <code>Create new MarkupsFiducial</code></li>
</ol>
<p><img src="https://user-images.githubusercontent.com/77850046/133850574-89470319-ab7f-4b70-b1b5-c18fe03c45a1.png" alt="image" width="480" height="480"></p>
<ol start="6">
<li>Fiducial does not appear when attempting to add to model</li>
</ol>

---

## Post #2 by @lassoan (2021-09-18 01:56 UTC)

<p>Slicer-4.10 is very old. Please use latest Slicer Stable Release or latest Slicer Preview Release and let us know if you run into any problems.</p>

---

## Post #3 by @adamgranthendry (2021-09-18 01:59 UTC)

<p>The only reason I used 4.10 is because 4.10.1, 4.10.2, 4.11, and the master branch have not worked.</p>

---

## Post #4 by @adamgranthendry (2021-09-18 02:00 UTC)

<p>I started at master and worked my way back. By version 4.10.1, I decided it was time to post an issue.</p>

---

## Post #5 by @adamgranthendry (2021-09-18 02:33 UTC)

<p>Should I try 4.11.20210226?</p>

---

## Post #6 by @lassoan (2021-09-18 02:33 UTC)

<p>I would recommend the latest Slicer Preview Release Slicer-4.13-2021-09-16.</p>
<p>Hit Ctrl-F top open the module finder and type “extract”, then choose “Extract centerline” module.</p>

---

## Post #7 by @adamgranthendry (2021-09-18 02:34 UTC)

<p>Will do. Please give me a moment to install.</p>

---

## Post #8 by @adamgranthendry (2021-09-18 02:54 UTC)

<p>I can confirm fiducials appear with Slicer Preview Release Slicer-4.13-2021-09-17</p>

---
