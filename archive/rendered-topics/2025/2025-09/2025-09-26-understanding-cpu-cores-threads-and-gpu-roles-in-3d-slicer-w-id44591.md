# Understanding CPU cores/threads and GPU roles in 3D Slicer workflows

**Topic ID**: 44591
**Date**: 2025-09-26
**URL**: https://discourse.slicer.org/t/understanding-cpu-cores-threads-and-gpu-roles-in-3d-slicer-workflows/44591

---

## Post #1 by @JaredAmudeo (2025-09-26 05:50 UTC)

<p>Hello, I’m not sure if this is the right place to ask, but I would like to know where I could learn more about the hardware and how it is involved in the different modules.</p>
<p>From what I understand, the GPU is mainly used for volume rendering, while most other tasks are CPU-RAM dependent. But regarding the CPU—how much does it really matter? For example, how do modules like <em>Grow from Seeds</em>, <em>Threshold</em>, or <em>Level Tracing</em> behave, or even editing directly in the 3D view?</p>
<p>Do these tools typically run single-core or multi-core, and how do threads and cores affect performance?</p>
<p>Finally, between Intel and AMD, is there any substantial difference? For instance, would CPUs with 3D cache like the 9950X3D behave differently compared to Intel’s Core Ultra processors?</p>

---

## Post #2 by @lassoan (2025-10-02 20:57 UTC)

<p>GPU is heavily utilized for volume rendering, rendering of very large models (you’ll start seeing slower rotation of the view using integrated graphics card when the model has more than 1M points), and of course all AI segmentations.</p>
<p>Number of CPU cores don’t really matter, probably you won’t notice speed improvements over 6-8 cores. Maximum CPU frequency matters more, but most CPUs are about in the same category (you cannot buy a CPU with 2x or 4x higher clock rate). If you have the option then choose a CPU that has a high boost rate (clock rate is automatically increased when the load is high).</p>
<p>Intel/AMD is probably not a significant difference. Slicer and underlying libraries are not specifically optimized for either, so I don’t think 3D cache or other special features would provide perceivable performance difference. If for the same price you need to choose between higher clock rate or higher number of threads then I would recommend to go with the higher clock rate, which would slightly favor Intel CPUs.</p>

---
