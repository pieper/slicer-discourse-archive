# Problem in calculating D95 using Dose Volume Histogram module

**Topic ID**: 15870
**Date**: 2021-02-05
**URL**: https://discourse.slicer.org/t/problem-in-calculating-d95-using-dose-volume-histogram-module/15870

---

## Post #1 by @aseman (2021-02-05 19:33 UTC)

<p>Hi 3D Slicer experts and all<br>
I want to calculate dosimetric parameters such as mean dose and D95 (the percentage of the prescription dose covering 95% of the volume) for some of head and neck patients(such as larynx cancer, ear cancer, etc) using Dose Volume Histogram module.<br>
Unfortunately, in some of them, the value of D95 calculated in 3D slicer is different from its value in the isogray treatment planning system( (TPS). for example, in the below image(larynx cancer patient), the yellow area is the part that received  dose of 50Gy (CTV50)and the blue area received 70Gy (CTV70). For CTV50, the calculated value of D95 in TPS is 48.8Gy and in 3D slicer is 47.56Gy.<br>
I used various versions such as slicer 4.8, 4.10 and 4.11; but the results were the same.<br>
can you help me about this problem?<br>
1- what is the cause of  this difference between the results of TPS and slicer?<br>
2- how can I calculate the correct value of D95 for these patients?</p>
<p>Thankd a lot</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e26d1c3c854e531265693ede46d9b0f5ae711ae.png" alt="Screenshot" data-base62-sha1="mz4BQKPGRDpyCFBViPjvDOtqSse" width="317" height="343"></p>

---
