# [Image Integration] Ensite Velocity EPS map + CT scan for radiosurgery in patients with VT

**Topic ID**: 10299
**Date**: 2020-02-16
**URL**: https://discourse.slicer.org/t/image-integration-ensite-velocity-eps-map-ct-scan-for-radiosurgery-in-patients-with-vt/10299

---

## Post #1 by @tomasz (2020-02-16 22:10 UTC)

<p>Dear All,</p>
<p>My name is Tomasz Jadczyk. I am an assistant professor and EP fellow at the Medical University of Silesia (Department of Cardiology and Structural Heart Diseases).<br>
I am interested in the application of 3D Slicer for image integration and merging electrophysiology maps (Ensite Velocity) with corresponding CT scans.</p>
<p>We are going to initiate a clinical trial for radiosurgery treatment of ventricular tachycardias. Study protocol:</p>
<ol>
<li>Patient undergoes electrophysiology mapping (Ensite Velocity) to assess the origin of ventricular arrhythmia (with additional anatomical landmarks to orientation + tagging of the arrhythmogenic areas)</li>
<li>Patient undergoes CT scan of the heart</li>
<li>Co-registration of electrophysiology map with CT scan with tagging of arrhythmogenic areas on the CT scan</li>
<li>Export of the tagged CT scan in the DICOM format</li>
<li>Import of the tagged CT scan into radioablation workstation (CyberKnife linear accelerator)</li>
<li>Drawing isodoses and prescribing application of ablation (using 3-plane CT view)</li>
</ol>
<p>The reference abstract by Sramko et al., ESC Congress 2019 (<a href="https://drive.google.com/open?id=19fRHtd518lM1PYZzkCxLZ7QDQDfVLCx_" rel="nofollow noopener">link</a>)</p>
<p>I would be grateful for your suggestions and support.</p>
<p>Kind regards,<br>
Tomasz Jadczyk MD PhD<br>
Department of Cardiology and Structural Heart Diseases<br>
Medical University of Silesia</p>

---

## Post #2 by @lassoan (2020-02-18 01:13 UTC)

<p>Import of the EP map is discussed here: <a href="https://discourse.slicer.org/t/is-there-interest-in-a-reader-for-cardiac-electrophysiology-electronanatomic-maps/6356/13" class="inline-onebox">Is there interest in a reader for cardiac electrophysiology electronanatomic maps?</a></p>
<p>The referenced Sramko 2019 slide deck approximately describes the same workflow that you would like to achieve. They used 3D Slicer for most of the steps. Have you asked them what modules they use and how?</p>

---
