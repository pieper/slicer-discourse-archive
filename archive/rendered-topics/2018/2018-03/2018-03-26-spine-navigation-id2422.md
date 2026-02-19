---
topic_id: 2422
title: "Spine Navigation"
date: 2018-03-26
url: https://discourse.slicer.org/t/2422
---

# Spine navigation

**Topic ID**: 2422
**Date**: 2018-03-26
**URL**: https://discourse.slicer.org/t/spine-navigation/2422

---

## Post #1 by @Dr_Ahmed_Maher (2018-03-26 13:06 UTC)

<p>Dear fiends, I am still a fresh joiner for slicer community, so please forgive my silly questions. I need to build up a navigation system to be used in spine interventions (mostly needling techniques). If I will register the patient’s spine using natural landmarks e.g spine transverse processes, will I face big errors provided that position of the patient during his CT scan is quite different from position during procedures? Any previous experience?</p>

---

## Post #2 by @lassoan (2018-03-26 13:17 UTC)

<p>Vertebrae moves by tens of millimeters between pre-operative CT imaging (acquired in supine position) and surgery (done in prone or lateral position). Typically this displacement is much larger that the required accuracy for any spinal intervention (up to a few millimeters). Therefore, you must register each vertebra separately. You typically also need a rigid reference (drilled into the bone) for at least every 2nd or 3rd vertebrae - for best accuracy, for each affected vertebra.</p>

---

## Post #3 by @Dr_Ahmed_Maher (2018-03-26 14:16 UTC)

<p>Usually in my practice,2 to 3 vertebraes are only needed for intervention.so what’s your recommendation for registration???..would I use natural landmarks or tracked ultrasound?..</p>

---

## Post #4 by @timeanddoctor (2018-03-27 11:02 UTC)

<p>In my opinion, you can register between the intraoperative x-RAY and the preoperative CT. I donnot kown the althem but you can have a research.</p>

---

## Post #5 by @ungi (2018-03-27 14:51 UTC)

<p>Vertebrae move relative to each other between different patient positions. But the vertebrae themselves are rigid. I think the key to X-ray free navigation is to accurately register the one or two vertebrae where you need high accuracy. Or directly visualize the target anatomy with a tracked ultrasound, and mark the 3D position on the tracked ultrasound. If this is done as part of the needle insertion procedure, the target will not move significantly.</p>

---
