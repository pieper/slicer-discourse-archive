---
topic_id: 47028
title: "New Extension Radreirradiation For Radiotherapy Reirradiatio"
date: 2026-05-14
url: https://discourse.slicer.org/t/47028
---

# New extension: RadReirradiation for radiotherapy reirradiation analysis and EQD2 dose accumulation

**Topic ID**: 47028
**Date**: 2026-05-14
**URL**: https://discourse.slicer.org/t/new-extension-radreirradiation-for-radiotherapy-reirradiation-analysis-and-eqd2-dose-accumulation/47028

---

## Post #1 by @LuisParedesOcampo (2026-05-14 14:23 UTC)

<p>Hi everyone,</p>
<p>I’d like to introduce RadReirradiation, a new 3D Slicer extension designed to support clinical reirradiation workflows in radiotherapy.</p>
<p>The extension provides the following features:</p>
<p>• Voxel-by-voxel BED and EQD2 biological dose accumulation, with time-based recovery factors based on the linear-quadratic model.<br>
• An image registration wrapper (Rigid, Affine, and Deformable B-Spline) built on the BRAINSFit engine, with an interactive manual pre-alignment panel and an Auto-Center tool specifically designed to handle CBCT field-of-view discrepancies common in linac-based imaging.<br>
• Automatic resampling of the moving dose grid to match the reference geometry prior to biological accumulation.<br>
• A custom Eclipse-style dose wash colormap (Dark Blue to Red, 2 Gy threshold) for familiar TPS-like visualization.</p>
<p>The extension is implemented in Python, depends on SlicerRT, and has been tested in research scenarios at our institution.</p>
<p>The repository is available at: <a href="https://github.com/LuisParedesOcampo/SlicerRadReirradiation" rel="noopener nofollow ugc">https://github.com/LuisParedesOcampo/SlicerRadReirradiation</a></p>
<p>A web-based companion tool is also available at <a href="https://radcomp.streamlit.app" rel="noopener nofollow ugc">https://radcomp.streamlit.app</a></p>
<p>Feedback, suggestions, and contributions are very welcome!</p>
<p>Best regards,<br>
Luis Paredes - Medical Physicist, Cali, Colombia</p>

---
