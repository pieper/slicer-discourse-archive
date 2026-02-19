---
topic_id: 28939
title: "Patients Breathing Solutions"
date: 2023-04-16
url: https://discourse.slicer.org/t/28939
---

# Patient's breathing solutions

**Topic ID**: 28939
**Date**: 2023-04-16
**URL**: https://discourse.slicer.org/t/patients-breathing-solutions/28939

---

## Post #1 by @jay1987 (2023-04-16 06:44 UTC)

<p>Due to the patient’s breathing, it is difficult for the target in the chest to stay at the same position in space. Therefore, it is difficult to accurately locate the target whether it is radiotherapy or ultrasound focusing. Are there any solutions that can achieve the effect of long-term positioning of a target in the chest through radiotherapy or ultrasound focusing</p>

---

## Post #2 by @pieper (2023-04-16 16:09 UTC)

<p>Maybe you want something like this: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8319119/" class="inline-onebox">Ultrasound-based sensors to monitor physiological motion - PMC</a></p>

---

## Post #3 by @lassoan (2023-04-16 18:39 UTC)

<p>SlicerIGT and related extensions offer lots of solutions for such problems (optical and electromagnetic tracking, ultrasound imaging, real-time MRI, etc.). To give more specific advice we need to know more about your clinical application - what organ, disease, procedure (biopsy, external beam, RF ablation, brachytherapy, etc), what pre- and intra-procedural imaging are available, etc.</p>

---

## Post #4 by @jay1987 (2023-04-17 11:44 UTC)

<p>thank you pieper,i will try to learn the paper</p>

---

## Post #5 by @jay1987 (2023-04-17 11:54 UTC)

<p>thank you lassoan,We want to use focused ultrasound to ablate a target on the kidney,We have developed a preliminary plan<br>
1.Obtain a patient’s abdominal CT image before surgery<br>
2.Bind reflective balls on the front end of the robotic arm and the patient’s body<br>
3.Using NDI to integrate the coordinate system of CT images and the coordinate system of the robotic arm into a coordinate system<br>
4.Positioning the target and entry points on the CT image<br>
5.During surgery, use NDI to observe the reflective ball bound to the patient’s body, draw a respiratory curve, and use focused ultrasound for ablation at the peak of the wave</p>
<p>This plan may encounter some problems in implementation, such as when I want the ultrasound to focus for 10 minutes, the robotic arm needs to follow the breathing curve for movement, but we cannot guarantee the accuracy of this approach</p>
<p>i want to get help from community , For example, is there a mature plan for abdominal radiation therapy that uses breath following, or what other plan can make patients focus more accurately during breathing</p>

---

## Post #6 by @gcsharp (2023-04-17 19:51 UTC)

<p>There are multiple solutions in RT.</p>
<ol>
<li>Respiratory gating.  Deliver treatment when tumor is in a pre-determined phase (usually exhale).</li>
<li>Voluntary breath hold.  Patient takes deep inspiration, then deliver beam.</li>
<li>Tumor tracking.  Continuous delivery, with beam position continuously updated.</li>
<li>Margin selection.  Include motion within treatment volume.</li>
</ol>
<p>Solutions (1) and (3) and even (4) imply you are able to take a 4D-CT (or equivalent) for planning.  Solution (2) implies your patient is conscious during treatment.</p>

---

## Post #7 by @jay1987 (2023-04-18 00:57 UTC)

<p>thank you gcsharp for the professional solution<br>
if the hospital don’t have the 4D-CT ,Just like some small hospitals,Are there any alternative solutions available?</p>

---

## Post #8 by @gcsharp (2023-04-18 18:05 UTC)

<p>You are most welcome.  There are always options.</p>
<p>(1) Estimate motion amplitude from fluoro or ultrasound<br>
(2) Estimate motion amplitude from exhale / inhale pair<br>
(3) Voluntary deep inspiration breath hold<br>
(4) Make your own 4D-CT using the NDI device<br>
(5) Purchase an upgrade from the CT vendor</p>
<p>For (1), you might need implanted fiducials if you are using fluoro.</p>
<p>For (2), this can over-estimates motion amplitude.  To get this right, you need the patient to hold at a “normal” inhale rather than a “deep” inhale.</p>
<p>For (3), you would typically take two inhale scans to verify reproducibility.</p>

---

## Post #9 by @jay1987 (2023-04-19 01:58 UTC)

<p>Thank you for the professional response from <a class="mention" href="/u/gcsharp">@gcsharp</a> . I have learned a lot from your solution and the detailed planning of GPT4 for your solution. Thank you very much</p>

---
