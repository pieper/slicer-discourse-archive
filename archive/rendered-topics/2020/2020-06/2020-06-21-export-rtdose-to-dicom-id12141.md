# Export RTDOSE to DICOM

**Topic ID**: 12141
**Date**: 2020-06-21
**URL**: https://discourse.slicer.org/t/export-rtdose-to-dicom/12141

---

## Post #1 by @jannah_fj (2020-06-21 14:10 UTC)

<p>Helo there, I have trouble when I want to export RTDose to  Dicom. I’ve tried to export but there is just the image or CT that exported on the output file. Meanwhile there is no RTDose. Thank you for your help.</p>
<p>Let me Explain more specific. First, I Accumulated 5 RTDose into one named RTDOSE Accumulate. Then, I want to export this RTDOSE to dicom because I want to import into another software. May I import the Accumulation of RT Dose into dicom?</p>

---

## Post #2 by @cpinter (2020-06-21 14:28 UTC)

<p>Without knowing more, it’s possible you don’t have the SlicerRT extension installed. In any case, please do a search on this forum for RT export, because there are several topics about it that could help.</p>

---

## Post #3 by @jannah_fj (2020-06-21 14:35 UTC)

<p>Thanks for the answer. But I have installed the SlicerRT extension.</p>

---

## Post #4 by @cpinter (2020-06-21 19:14 UTC)

<p>In this case please</p>
<ol>
<li>Do a search in the forum, because many people have asked questions about RT export that have been solved.</li>
<li>Give us more information on what is it that you do, what do you expect, and what happens differently and how.</li>
</ol>

---

## Post #5 by @jannah_fj (2020-06-21 19:40 UTC)

<p>I try to search but there’s no case like what I do.<br>
I want to comparing DVH form TPS and 2 Software, 3Slicer and PRIMO. Data of patient from TPS are CT, RTStruct, RTPlan and RTDose. Primo Software just can comparing dose with one file dicom, meanwhile I have 5 RTDose from TPS that represent of 5 beams. Thats why I have to accumulate the RTDose with slicer. Then, I want to export this accumulation of RTDose to dicom so that I can compare with PRIMO. But I have trouble because there’s just image on the output folder and there’s no RT dose.</p>
<p>What should I do?</p>

---

## Post #6 by @cpinter (2020-06-22 08:32 UTC)

<p>Thanks, now we understand your motivation.</p>
<p>But we still don’t have any information about the actual problem.</p>
<aside class="quote no-group" data-username="jannah_fj" data-post="5" data-topic="12141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jannah_fj/48/7185_2.png" class="avatar"> jannah_fj:</div>
<blockquote>
<p>But I have trouble because there’s just image on the output folder and there’s no RT dose</p>
</blockquote>
</aside>
<p>What do you mean by this? What output folder? Can you please describe what are the exact steps you take, what do you expect, and what happens differently and how?</p>

---

## Post #7 by @icetomato (2020-11-16 07:22 UTC)

<p>I also want to konw----“how to export a dose Accumulate result to a dicom file”</p>

---

## Post #8 by @icetomato (2020-11-23 01:20 UTC)

<p>HI, jannah_fj<br>
I find a way to export rtdose and the dose pixdata is right,   you can choose save butten  choose the rtdose save as .VTK file ,is’t a Binary file, you can  conversion Acsii</p>

---

## Post #9 by @jannah_fj (2021-02-02 13:28 UTC)

<p>Thank you for your information, maybe i will try this next time</p>

---
