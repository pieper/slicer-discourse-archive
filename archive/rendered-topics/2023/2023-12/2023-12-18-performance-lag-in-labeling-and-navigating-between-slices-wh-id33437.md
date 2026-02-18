# Performance lag in labeling and navigating between slices when using Chrome Remote Desktop

**Topic ID**: 33437
**Date**: 2023-12-18
**URL**: https://discourse.slicer.org/t/performance-lag-in-labeling-and-navigating-between-slices-when-using-chrome-remote-desktop/33437

---

## Post #1 by @doc87 (2023-12-18 02:29 UTC)

<p>Hi<br>
I am trying to use 3d slicer installed on a vm with the following specs:</p>
<blockquote>
<p>Enabled Virtual Workstation (NVIDIA GRID)<br>
g2-standard-4 (4 vCPU, 2 core, 16 GB memory)<br>
However, when I use Chrome Remote Desktop- there is a severe performance lag as compared to when I use the 3D Slicer app on my local machine. I have tried all possible options but cant get past this.</p>
</blockquote>

---

## Post #2 by @muratmaga (2023-12-18 07:13 UTC)

<p>Remote desktop issues can be due to network latency, which is usually out of your control. Try with a faster network connection or try to use VM site that’s geographically closer to you (if that’s an option).</p>
<p>Also the specs of the VM is pretty low, but should be sufficient for typical clinical datasets. Anything higher resolution, you are probably quite under-powered.</p>

---

## Post #3 by @pieper (2023-12-18 18:21 UTC)

<p>Different remote desktop software may also be an option.  I have pretty good results with x11vnc plus noVNC, but <a href="https://aws.amazon.com/hpc/dcv/">niceDCV</a> is very fast as are some other proprietary tools.</p>

---
