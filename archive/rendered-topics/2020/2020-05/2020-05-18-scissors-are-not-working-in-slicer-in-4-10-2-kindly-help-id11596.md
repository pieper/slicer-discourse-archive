---
topic_id: 11596
title: "Scissors Are Not Working In Slicer In 4 10 2 Kindly Help"
date: 2020-05-18
url: https://discourse.slicer.org/t/11596
---

# Scissors are not working in slicer in 4.10.2 kindly help

**Topic ID**: 11596
**Date**: 2020-05-18
**URL**: https://discourse.slicer.org/t/scissors-are-not-working-in-slicer-in-4-10-2-kindly-help/11596

---

## Post #1 by @shivaprasad_kolur (2020-05-18 06:00 UTC)

<p>scissors are not working in slicer 4.10.2 kindly help</p>

---

## Post #2 by @muratmaga (2020-05-18 06:24 UTC)

<p>Scissors tools in 4.10.2 is indeed working. We can help you better if you can describe what is not working in more detail (e.g., your data, steps that you have done prior to scissor, any error message etc)…</p>

---

## Post #3 by @shivaprasad_kolur (2020-05-18 06:32 UTC)

<p>after creating a 3D model after using segment editor , i wanted to cutoff few small unwanted islands lying seperately from the ct chest 3d model , but couldnt do so</p>

---

## Post #4 by @shivaprasad_kolur (2020-05-18 06:32 UTC)

<p>i didnt get any error message</p>

---

## Post #5 by @shivaprasad_kolur (2020-05-18 07:50 UTC)

<p>sequence of steps<br>
loaded sample CTChest<br>
opened module segment editor<br>
created two segments<br>
created a mask by using threshold to seperate out the airways and lungs<br>
generated a 3d model using grow from seeds<br>
used segment statstics to generate volume of lung with airway<br>
tried to use scissors to cut out the lung lobes so that only the airway remains behind , but the scissors wouldnt work<br>
plz help</p>

---

## Post #6 by @doc-xie (2020-05-18 09:15 UTC)

<p>Maybe you choose the wrong segment in segmentations list. It is better you can attach the screenshot of every step.<br>
Best wishes,<br>
Xie</p>

---

## Post #7 by @shivaprasad_kolur (2020-05-18 07:53 UTC)

<p>Operating system:windows<br>
Slicer version:4.10.2 and 4.11 preview</p>
<p>sequence of steps<br>
loaded sample CTChest<br>
opened module segment editor<br>
created two segments<br>
created a mask by using threshold to seperate out the airways and lungs<br>
generated a 3d model using grow from seeds<br>
used segment statstics to generate volume of lung with airway<br>
tried to use scissors to cut out the lung lobes so that only the airway remains behind , but the scissors wouldnt work<br>
plz help</p>

---

## Post #8 by @cpinter (2020-05-18 09:33 UTC)

<p><a class="mention" href="/u/shivaprasad_kolur">@shivaprasad_kolur</a> Please use a recent preview version. 4.10.2 is more than one and a half year old, and an immense amount of stabilization and improvement work has been done in Segment Editor. Let us know if it works for you.</p>
<p>If not, then please elaborate on how the scissors tool did not work. It would also help if we could see a video or something that helps us better to understand the problem.</p>

---

## Post #9 by @lassoan (2020-05-18 17:22 UTC)

<p>Without seeing screenshots or screen capture videos, we can only guess. Just a few more guesses:</p>
<ul>
<li>You haven’t clicked Apply when you are finished with “Grow from seeds”</li>
<li>You have chosen masking settings that allow editing the selected segment at the location you wanted to cut</li>
<li>You have not selected the correct segment (Scissors only cuts the selected segment)</li>
</ul>

---
