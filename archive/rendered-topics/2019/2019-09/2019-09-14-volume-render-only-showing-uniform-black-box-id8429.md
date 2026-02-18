# Volume Render only showing uniform black box

**Topic ID**: 8429
**Date**: 2019-09-14
**URL**: https://discourse.slicer.org/t/volume-render-only-showing-uniform-black-box/8429

---

## Post #1 by @aekort (2019-09-14 17:00 UTC)

<p>When I try to render the volume, it only renders a uniform black cube. I have tried shift and crop to see the scanned teeth but the are not in the volume render. I have this message in the console:</p>
<p>Failed to query vtkVolume instance for port 0</p>

---

## Post #2 by @lassoan (2019-09-14 17:03 UTC)

<p>What operating system, CPU, and graphics card do you have? How large is the volume that you are trying to render? What Slicer version do you use? Do you use CPU or GPU volume renderer? Can you volume render the sample data sets (e.g., MRHead) correctly?</p>

---

## Post #3 by @aekort (2019-09-14 17:19 UTC)

<p>Windows 10, Intel® Xeon® Silver 4110 CPU, Nvida Quadro P5000. 7.4GB. Slicer 10.4.2. GPU Volume Render. I can render other datasets. I figured out that it was a vector dataset, so I converted it to scalar and the scalar rendered fine.</p>

---
