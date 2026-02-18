# Does DSCMRIAnalysis module provide leakage correction in making rCBV map?

**Topic ID**: 3971
**Date**: 2018-09-03
**URL**: https://discourse.slicer.org/t/does-dscmrianalysis-module-provide-leakage-correction-in-making-rcbv-map/3971

---

## Post #1 by @Kyu_Sung_Choi (2018-09-03 01:02 UTC)

<p>Dear Dr. Fedorov,</p>
<p>Thank you for your awesome work on DSCMRIAnalysis module.<br>
However, I wonder if DSCMRIAnalysis module provides leakage correction in making rCBV map?<br>
I think there’s no motion correction function on DSCMRIAnalysis module, yet.<br>
Could you please let me know?<br>
Thank you in advance!</p>
<p>BR,<br>
Kyu Sung</p>

---

## Post #2 by @fedorov (2018-09-03 01:12 UTC)

<p><a class="mention" href="/u/abeers">@abeers</a> should know the answer .</p>

---

## Post #3 by @fedorov (2018-09-03 01:13 UTC)



---

## Post #4 by @abeers (2018-09-07 12:01 UTC)

<p>Hello Kyu Sung,</p>
<p>Thanks for sending this message. The DSCMRIAnalysis module does provide leakage correction when making a rCBV map. Leakage Correction is coded as “K2” in the DSCMRIAnalysis module – you should be able to create a leakage correction map by selecting an option on the “Output K2 image” dropdown menu under the “IO” dropdown menu.</p>
<p>To your question about motion correction, there is no motion correction in the DSCMRIAnalysis module as of yet. Please do not hesitate to send me any additional questions you may have.</p>
<p>All the best,<br>
Andrew Beers</p>
<p>Programmer<br>
QTIM @ MGH</p>

---

## Post #5 by @lassoan (2018-09-07 12:26 UTC)

<p>You can use SequenceRegistration extension for motion-compensation of image sequences. It takes Sequence nodes as inputs, so you need to convert between MultiVolume nodes (for example, by saving the node to file and then when loading them choose file type in description column). After we release Slicer-4.10, we should consolidate sequence and multi-volume infrastructure.</p>

---

## Post #6 by @fedorov (2018-09-07 15:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="3971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It takes Sequence nodes as inputs, so you need to convert between MultiVolume nodes</p>
</blockquote>
</aside>
<p>Or you can load the source DICOM series as a Sequence. Use “Advanced” mode in DICOM Browser, and choose the loadable that says “sequence”.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="3971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>After we release Slicer-4.10, we should consolidate sequence and multi-volume infrastructure.</p>
</blockquote>
</aside>
<p>Yes, it would be good to explore this direction and understand the effort that it will take! Good topic for a project week.</p>

---
