---
topic_id: 48998
title: "Delayed 2D Erase brush response on Windows with hybrid Intel/NVIDIA graphics"
date: 2026-11-20
url: https://discourse.slicer.org/t/48998
last_bumped: 2026-11-20T13:54:08.276Z
---

# Delayed 2D Erase brush response on Windows with hybrid Intel/NVIDIA graphics

**Topic ID**: 48998
**Date**: 2026-11-20
**URL**: https://discourse.slicer.org/t/delayed-2d-erase-brush-response-on-windows-with-hybrid-intel-nvidia-graphics/48998

---

## Post #1 by @cnionita (2026-11-20 13:54 UTC)

<p>Hello,</p>
<p>Over the past several days, Slicer has developed a noticeable delay when moving the Erase brush over a 2D image slice. The brush follows the mouse a fraction of a second late. Editing itself can work, but the movement is still laggy. Reinstalling Slicer did not resolve it.</p>
<p>Environment:</p>
<ul>
<li>3D Slicer 5.12.4, 64-bit application.</li>
<li>Windows 11 Pro 26H2, build 26300.10075.</li>
<li>Dell XPS 17 9720, 32 GB RAM.</li>
<li>Intel Iris Xe, driver 32.0.101.7088.</li>
<li>NVIDIA RTX 3060 Laptop GPU, now driver 610.74 / 32.0.16.1074.</li>
<li>External Dell S3222DGM monitor.</li>
</ul>
<p>The NVIDIA driver was updated from 596.08 through Windows Update. I retested afterward and the 2D brush delay remains. There has also been occasional external-monitor blinking and typing-focus loss outside Slicer, so I am not assuming this is exclusively a Slicer bug.</p>
<p>Checks so far:</p>
<ul>
<li>Before the NVIDIA update, a blank startup with temporary settings and the startup script ignored succeeded. Startup with saved settings also succeeded.</li>
<li>A simple synthetic VTK render reported the RTX 3060 and OpenGL 4.5 and completed successfully before the driver update. This was a rendering check, not a Paint/Erase performance test.</li>
<li>A separate episode where clicks had no effect involved Margin being active and the editable area being restricted. Selecting Erase restored editing, but did not resolve the cursor/brush delay.</li>
<li>No clean Sample Data reproduction, measured frame rate, or controlled single-slice versus multi-view comparison has been completed yet.</li>
</ul>
<p>I saw the forum’s highlighted screen-glitch notice about NVIDIA 595.71. My current driver is 610.74, so I do not know whether that is related.</p>
<p>What is the most useful next diagnostic to distinguish brush/rendering overhead, scene-specific complexity, and a system/driver issue? In particular, should I compare a single slice view, Show 3D off, and Data Probe magnification/crosshair settings? Is there a recommended local timing/profile procedure or public sample dataset for this?</p>
<p>No patient data, screenshots, scene files, or raw logs are attached. I can provide focused, non-identifying technical details if needed.</p>
<p>Thank you.</p>

---
