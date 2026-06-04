---
topic_id: 47140
title: "Mensure tooth torque"
date: 2026-05-26
url: https://discourse.slicer.org/t/47140
last_bumped: 2026-06-03T05:52:56.996Z
---

# Mensure tooth torque

**Topic ID**: 47140
**Date**: 2026-05-26
**URL**: https://discourse.slicer.org/t/mensure-tooth-torque/47140

---

## Post #1 by @Kevin_Nguyen (2026-05-26 15:09 UTC)

<p>Hello!</p>
<p>I’m a dentist currently working on a project where I’m measuring tooth torque, specifically the angle of the root. I’m looking for some guidance regarding which tools and measurement methods would be most appropriate to use.</p>
<p>I would really appreciate any advice or recommendations from someone with experience in this area. Thank you!</p>

---

## Post #2 by @MasatoshiOBA (2026-05-28 11:52 UTC)

<p>Hello!</p>
<p>I would first clarify whether you mean orthodontic “tooth torque,” that is, the buccolingual inclination of the tooth/root, or mechanical torque/moment in a biomechanical sense.</p>
<p>If you mean <strong>tooth or root inclination</strong>, then 3D Slicer can probably help. A possible workflow would be to import CBCT data, segment the target tooth/root and jaw, create 3D models, define the long axis of the tooth or root, define a reference plane, and then measure the angle between them.</p>
<p>For segmentation, you may want to try the DentalSegmentator extension in 3D Slicer. It can automatically segment dental CT/CBCT volumes, including the maxilla, mandible, upper teeth, lower teeth, and mandibular canal. The result should still be checked and manually corrected when accuracy is important.</p>
<p>If you mean <strong>biomechanical torque</strong>, such as torque moment, stress distribution, or torque expression produced by brackets/wires/aligners, then Slicer alone is probably not enough. In that case, Slicer is mainly useful for the first part of the workflow: segmentation and 3D model generation. The actual mechanical simulation would usually require CAD/mesh-processing software and finite element analysis software such as ANSYS, Abaqus, etc.</p>
<p>For example, in a recent 3D finite element study of orthodontic torque expression, the authors created 3D models of brackets and a maxillary central incisor, assigned material properties, converted the models into finite element models, and simulated torque movements using ANSYS. In such a workflow, Slicer could potentially be used for the image-based segmentation/model creation part, but not for the full biomechanical simulation.</p>
<p>So I would first define the measurement target very clearly:</p>
<ul>
<li>
<p>Are you measuring a root angle, or simulating a mechanical torque?</p>
</li>
<li>
<p>What is the tooth/root axis?</p>
</li>
<li>
<p>What is the reference plane?</p>
</li>
<li>
<p>Do you need to model periodontal ligament, alveolar bone, brackets, wires, or aligners?</p>
</li>
<li>
<p>Do you need simple angular measurements, or finite element analysis?</p>
</li>
</ul>
<p>Once these definitions are clear, Slicer can be very useful for CBCT visualization, segmentation, landmark placement, and 3D model creation. For biomechanical torque analysis, I would recommend collaborating with an engineer or researcher experienced in finite element analysis.</p>
<p>Hope this helps.</p>

---

## Post #3 by @Kevin_Nguyen (2026-06-03 05:52 UTC)

<p>Thank you so much for your answer! It really helps! We are going to measure tooth/root inclination. Have you done it before with 3D-slicer?</p>

---
