---
topic_id: 49100
title: "Dicom export 3 D echo images "
date: 2026-11-25
url: https://discourse.slicer.org/t/49100
last_bumped: 2026-11-28T10:38:37.740Z
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

## Post #2 by @Juan_Donado (2026-11-28 02:33 UTC)

<p>Update after inspecting the exported files (EPIQ 7C / CVx, software 11.0.4.1266, X5-1c):</p>
<ul>
<li>SOP Class: US Multi-frame (1.2.840.10008.5.1.4.1.1.3.1), Series 1, Presentation Intent Type = FOR PRESENTATION, JPEG Baseline</li>
<li>Pixel Data = rendered screen loop only (105–322 frames)</li>
<li>The volume data appears to be in a private sequence (200D,3CF1), 59–129 MB per file</li>
<li>No Series 4 / FOR PROCESSING objects in this export</li>
</ul>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, is there any reader (or partial reverse-engineering) for the native 4D data in (200D,3CF1)? Or is QLAB Cartesian export still the only route for Philips cardiac 4D?</p>

---

## Post #3 by @Esteban_Barreiro (2026-11-28 10:38 UTC)

<p>Hi Juan,</p>
<p>Have you tried exporting in “.vol” file format? You can import .vol as  volumetric Data in 3dSlicer using the GE Kretz ultrsound converter, included in SlicerHeart Extension.</p>

---
