---
topic_id: 49100
title: "Dicom export 3 D echo images "
date: 2026-11-25
url: https://discourse.slicer.org/t/49100
last_bumped: 2026-11-25T17:50:48.271Z
---

# Dicom export 3 D echo images 

**Topic ID**: 49100
**Date**: 2026-11-25
**URL**: https://discourse.slicer.org/t/dicom-export-3-d-echo-images/49100

---

## Post #1 by @Juan_Donado (2026-11-25 17:50 UTC)

<p><strong>Title:</strong> Philips CVx / EPIQ 11.0.x – No Cartesian DICOM export – volumes stored only in private attributes (Conformance Statement review)</p>
<p>Dear Slicer community,</p>
<p>I am a pediatric cardiologist working on 3D modeling of congenital atrioventricular valves using 3D Slicer + SlicerHeart.</p>
<p><strong>System:</strong> Philips CVx 3D nSIGHT Plus (upgraded EPIQ 7C), software 11.0.4, X5-1c probe.</p>
<p>Native DICOM export does not produce volumes readable by SlicerHeart’s Philips 4D US DICOM tools (only screen captures appear).</p>
<p>Philips Colombia replied in writing (November 2026) that:</p>
<p>•  Cartesian DICOM export is no longer available.</p>
<p>•  The old Qstation/Excelera route is discontinued.</p>
<p>•  No supported alternative is offered.</p>
<p>I reviewed the official DICOM Conformance Statement for EPIQ/Affiniti Release 11.0.x. It confirms that:</p>
<p>•  3D volumes are stored as Ultrasound Multiframe Image objects.</p>
<p>•  They use Presentation Intent Type (0008,0068) = “FOR PROCESSING” (Series 4), intended only for Philips 3D viewers.</p>
<p>•  Actual 3D/4D volumetric data is stored in <strong>Philips private attributes</strong>.</p>
<p>•  There is no documented Cartesian / 3DDCM export pathway.</p>
<p>Has anyone found a current practical way (2025–2026) to obtain usable 3D/4D TTE volumes from modern Philips cardiac systems (CVx / EPIQ 11.x) that can be loaded into SlicerHeart?</p>
<p>Any information about Ultrasound Workspace, residual QLAB options, or workarounds would be extremely helpful.</p>
<p>Thank you in advance.</p>
<p>Juan Roberto Donado Perna</p>
<p>Pediatric Cardiology – Medellín, Colombia</p>

---
