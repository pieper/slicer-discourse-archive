# Severe 3D Rendering Slowdown with Many Segmentation Nodes — Can Slicer Offload Work from GPU to CPU?

**Topic ID**: 45432
**Date**: 2025-12-10
**URL**: https://discourse.slicer.org/t/severe-3d-rendering-slowdown-with-many-segmentation-nodes-can-slicer-offload-work-from-gpu-to-cpu/45432

---

## Post #1 by @Victor_Wayne (2025-12-10 11:31 UTC)

<p>Hello,</p>
<p>In my 3D slicer extenstion the frame rate of the 3D volume renderer drops significantly as I add more and more segmentation node. As the segmentation nodes increas even the UI becomes very very slow. When testing, at around 80 something probes the cursor stopped moving.  But I am not able to reproduce the cursor hanging.</p>
<p>I profiled the CPU, GPU and RAM usage when stress testing my extension with a lot of segmentation node. (Here segmentation nodes are ellipsoidal probes)</p>
<p>Only one core of the CPU was utilized properly. And around 95% of the integrated GPU of11th Gen Intel® Core™ i7-11850H × 16 provided in the DELL Precision laptop was being used. The RAM usage sits comfortably at around 45%.</p>
<p>What I am going to ask maybe a dumb question. Maybe it is not possible. But I wanted to make sure. So my question is: Is there any way to offload some of the GPU rendering to the CPU? Or a way to use the unused CPU cores parallely with the GPU to increase performance?</p>
<p>Thanks for your help in advance.</p>

---

## Post #2 by @lassoan (2025-12-14 21:30 UTC)

<p>Offloading some work to GPU usually requires the feature to be redeveloped from scratch, which would be a lot of very expensive work. It also means double maintenance effort from that point, because the existing efficient CPU implementation must be still maintained (as not everybody has a strong GPU, and for large problems GPU VRAM may be a limiting factor).</p>
<p>While there is no easy general-purpose solution for solving all performance issues by maximum utilization of any hardware that a user has, most likely there are easy ways to solve your specific problem.</p>
<p>For example: A single segmentation node is prepared to handle hundreds of segments efficiently. This means that it is extremely inefficient to have hundreds of segmentations, each containing one segment, because you still need to pay for all the infrastructure that allows managing many segments in one segmentation node. If you are segmenting 80 probes in your image then you can resolve the performance issue by storing them in a single segmentation. If you want the probes to be moved independently then you can move out the one that you are modifying temporarily into another segmentation node or to a model node. You can also consider using model nodes instead, which cannot be easily interactively edited, but may be simpler and more efficient to use.</p>

---

## Post #3 by @Victor_Wayne (2025-12-18 04:05 UTC)

<p>Sorry for the late reply.<br>
And thank you  so much for your input and suggestions.</p>
<p>Let’s say I am going to redevelop a small part of the feature so that it offloads the rendering to the CPU. How can it be done?</p>
<p>Again, thank you.</p>

---
