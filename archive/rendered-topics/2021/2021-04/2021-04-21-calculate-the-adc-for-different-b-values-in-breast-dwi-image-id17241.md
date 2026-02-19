---
topic_id: 17241
title: "Calculate The Adc For Different B Values In Breast Dwi Image"
date: 2021-04-21
url: https://discourse.slicer.org/t/17241
---

# Calculate the ADC for different b values in Breast DWI images

**Topic ID**: 17241
**Date**: 2021-04-21
**URL**: https://discourse.slicer.org/t/calculate-the-adc-for-different-b-values-in-breast-dwi-images/17241

---

## Post #1 by @Mgi (2021-04-21 23:53 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20200930<br>
Expected behavior: I used the DWModeling module to calculate the ADC from Breast DWI images with b values 0-400-700-1100.<br>
Actual behavior: I can not see the results of ADC values. Neither I can’t load the segmentated region in .seg.nrrd, maybe I will apply in .labelmap, but I don’t know.</p>
<p>Hope for any kind help or comment, thanks a lot!</p>

---

## Post #2 by @pieper (2021-04-22 14:47 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> will probably reply when he gets a chance, but in the mean time if you could look in the error log for any suspicious messages and or just post the whole log here.</p>
<p>See: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog" class="inline-onebox">Documentation/Nightly/SlicerApplication/ErrorLog - Slicer Wiki</a></p>

---

## Post #3 by @fedorov (2021-04-22 14:49 UTC)

<p>I have to admit I have not used that module in a very long time, and am not sure about the status. It may be that the extension did not survive the various ITK and other infrastructure upgrades, and needs attention. Yes, sharing a log would be a good start.</p>

---

## Post #4 by @Mgi (2021-04-22 20:48 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/fedorov">@fedorov</a>! thank for your response. The whole log is too long and didn´t load then I copied only a part here.<br>
<a class="mention" href="/u/fedorov">@fedorov</a>, you said may be this extenison did not survive the upgrades, Could you recommend to me another extension for calculate the ADC in breast images?</p>
<p>[DEBUG][Qt] 21.04.2021 20:09:03 [] (unknown:0) - “DICOM indexer has successfully processed 200 files [4.19s]”<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:03 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[WARNING][Qt] 21.04.2021 20:09:04 [] (unknown:0) - Patient ID is empty, using studyInstanceUID (1.3.46.670589.11.71403.5.0.8896.2019060609534063092) as patient ID<br>
[DEBUG][Qt] 21.04.2021 20:09:04 [] (unknown:0) - “DICOM indexer has updated display fields for 200 files [0.15s]”<br>
[INFO][Python] 21.04.2021 20:09:04 [Python] (C:\Users\Vane\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMBrowser.py:268) - Imported a DICOM directory, checking for extensions<br>
[INFO][Stream] 21.04.2021 20:09:04 [] (unknown:0) - Imported a DICOM directory, checking for extensions<br>
[DEBUG][Python] 21.04.2021 20:09:11 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 21.04.2021 20:09:11 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[WARNING][Python] 21.04.2021 20:09:12 [Python] (C:\Users\Vane\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py:629) - Geometric issues were found with 1 of the series. Please use caution.<br>
[CRITICAL][Stream] 21.04.2021 20:09:12 [] (unknown:0) - Geometric issues were found with 1 of the series. Please use caution.<br>
[CRITICAL][Stream] 21.04.2021 20:09:12 [] (unknown:0) -<br>
[DEBUG][Python] 21.04.2021 20:09:12 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 21.04.2021 20:09:12 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 21.04.2021 20:09:12 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 21.04.2021 20:09:15 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[INFO][Python] 21.04.2021 20:09:28 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM<br>
[INFO][Python] 21.04.2021 20:09:29 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:457) - Window/level found in DICOM tags (center=447.0, width=777.0) has been applied to volume 401: DWI_400-700-1100<br>
[DEBUG][Python] 21.04.2021 20:09:29 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:790) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.33179e-05 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 21.04.2021 20:09:28 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 21.04.2021 20:09:29 [] (unknown:0) - Window/level found in DICOM tags (center=447.0, width=777.0) has been applied to volume 401: DWI_400-700-1100<br>
[CRITICAL][Qt] 21.04.2021 20:09:29 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( “1onDisplayNodeModified(vtkObject*, vtkObject*)” ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 21.04.2021 20:09:29 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 21.04.2021 20:09:29 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM<br>
[INFO][Python] 21.04.2021 20:09:29 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:457) - Window/level found in DICOM tags (center=264.0, width=459.0) has been applied to volume 401: DWI_400-700-1100_1<br>
[DEBUG][Python] 21.04.2021 20:09:29 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:790) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.33179e-05 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 21.04.2021 20:09:29 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 21.04.2021 20:09:29 [] (unknown:0) - Window/level found in DICOM tags (center=264.0, width=459.0) has been applied to volume 401: DWI_400-700-1100_1<br>
[CRITICAL][Qt] 21.04.2021 20:09:29 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 21.04.2021 20:09:29 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 21.04.2021 20:09:30 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM<br>
[INFO][Python] 21.04.2021 20:09:30 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:457) - Window/level found in DICOM tags (center=232.0, width=404.0) has been applied to volume 401: DWI_400-700-1100_2<br>
[DEBUG][Python] 21.04.2021 20:09:30 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:790) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.33179e-05 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 21.04.2021 20:09:30 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 21.04.2021 20:09:30 [] (unknown:0) - Window/level found in DICOM tags (center=232.0, width=404.0) has been applied to volume 401: DWI_400-700-1100_2<br>
[CRITICAL][Qt] 21.04.2021 20:09:30 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 21.04.2021 20:09:30 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 21.04.2021 20:09:30 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM<br>
[INFO][Python] 21.04.2021 20:09:31 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:457) - Window/level found in DICOM tags (center=233.0, width=405.0) has been applied to volume 401: DWI_400-700-1100_3<br>
[DEBUG][Python] 21.04.2021 20:09:31 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:790) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.33179e-05 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 21.04.2021 20:09:30 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 21.04.2021 20:09:31 [] (unknown:0) - Window/level found in DICOM tags (center=233.0, width=405.0) has been applied to volume 401: DWI_400-700-1100_3<br>
[CRITICAL][Qt] 21.04.2021 20:09:31 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 21.04.2021 20:09:31 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject *,class vtkObject *) : Invalid object type calling display node modified event<br>
[DEBUG][Qt] 21.04.2021 20:14:57 [] (unknown:0) - Switch to module:  “DWModeling”<br>
[DEBUG][Qt] 21.04.2021 20:15:52 [] (unknown:0) - “Segmentation” Reader has successfully read the file “F:/BREAST STUDY/FCDN_001/Segmentation.seg.nrrd” “[0.48s]”<br>
[DEBUG][Qt] 21.04.2021 20:19:01 [] (unknown:0) - Found SharedObject Module<br>
[DEBUG][Qt] 21.04.2021 20:19:01 [] (unknown:0) - ModuleType: SharedObjectModule<br>
[DEBUG][Qt] 21.04.2021 20:19:07 [] (unknown:0) - DWModeling command line:</p>
<p>slicer:00007FFC3AF79720 --processinformationaddress 000001FC12D75B88 --model BiExponential --fittedVolume C:/Users/Vane/AppData/Local/Temp/Slicer/HABG_vtkMRMLMultiVolumeNodeD.nrrd --rsqrVolume slicer:000001FC574F9F00#vtkMRMLScalarVolumeNode22 --slowDiff slicer:000001FC574F9F00#vtkMRMLScalarVolumeNode23 --fastDiff slicer:000001FC574F9F00#vtkMRMLScalarVolumeNode24 --fastDiffFraction slicer:000001FC574F9F00#vtkMRMLScalarVolumeNode25 --monoExpInitParameters 0,0.0015 --biExpInitParameters 0,0.7,0.00025,0.002 --kurtosisInitParameters 0,1,0.0015 --stretchedExpInitParameters 0,0.0017,0.7 --gammaInitParameters 0,1.5,0.002 C:/Users/Vane/AppData/Local/Temp/Slicer/HABG_vtkMRMLMultiVolumeNodeC.nrrd<br>
[DEBUG][Qt] 21.04.2021 20:23:26 [] (unknown:0) - DWModeling standard output:</p>
<p>Will use the following b-values: 0 400 700 1100<br>
[INFO][VTK] 21.04.2021 20:23:26 [vtkMRMLScene (000001FC15FF3030)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[INFO][Stream] 21.04.2021 20:23:27 [] (unknown:0) - Display node set and observed<br>
[DEBUG][Qt] 21.04.2021 20:24:07 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 21.04.2021 20:29:48 [] (unknown:0) - Switch to module:  “DWModeling”<br>
[DEBUG][Python] 21.04.2021 20:29:53 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\SlicerDevelopmentToolbox\lib\Slicer-4.11\qt-scripted-modules\SlicerDevelopmentToolboxUtils\decorators.py:239) - calling refreshUIElementsAvailability after setup<br>
[DEBUG][Qt] 21.04.2021 20:29:53 [] (unknown:0) - Switch to module:  “QuantitativeReporting”<br>
[WARNING][Qt] 21.04.2021 20:29:54 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Qt] 21.04.2021 20:30:32 [] (unknown:0) - Switch to module:  “DWModeling”</p>

---

## Post #5 by @Mgi (2021-04-23 16:26 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/fedorov">@fedorov</a> !<br>
[DEBUG][Qt] 23.04.2021 12:36:18 [] (unknown:0) - Session start time …: 2021-04-23 12:36:18<br>
[DEBUG][Qt] 23.04.2021 12:36:18 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) win-amd64 - installed release<br>
[DEBUG][Qt] 23.04.2021 12:36:19 [] (unknown:0) - Operating system …: Windows /  Personal / (Build 19041, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 23.04.2021 12:36:19 [] (unknown:0) - Memory …: 12187 MB physical, 14043 MB virtual<br>
[DEBUG][Qt] 23.04.2021 12:36:19 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 23.04.2021 12:36:19 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 23.04.2021 12:36:19 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 23.04.2021 12:36:19 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 23.04.2021 12:36:19 [] (unknown:0) - Prefer executable CLI …: no<br>
[DEBUG][Qt] 23.04.2021 12:36:19 [] (unknown:0) - Application path …: C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin<br>
[DEBUG][Qt] 23.04.2021 12:36:19 [] (unknown:0) - Additional module paths …: C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/DCMQI/lib/Slicer-4.11/cli-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/PETTumorSegmentation/lib/Slicer-4.11/qt-loadable-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/PETTumorSegmentation/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/cli-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/PET-IndiC/lib/Slicer-4.11/cli-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/PET-IndiC/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerDevelopmentToolbox/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerDMRI/lib/Slicer-4.11/cli-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerDMRI/lib/Slicer-4.11/qt-loadable-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerDMRI/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/UKFTractography/lib/Slicer-4.11/cli-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/UKFTractography/lib/Slicer-4.11/qt-loadable-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/UKFTractography/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerProstate/lib/Slicer-4.11/cli-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerProstate/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRadiomics/lib/Slicer-4.11/cli-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRadiomics/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/mpReview/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/cli-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 23.04.2021 12:36:26 [Python] (C:\Users\Vane\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[WARNING][Qt] 23.04.2021 12:36:30 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Python] 23.04.2021 12:36:35 [Python] (C:\Users\Vane\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 23.04.2021 12:36:39 [Python] (C:\Users\Vane\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Python] 23.04.2021 12:36:39 [Python] (C:\Users\Vane\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[INFO][Python] 23.04.2021 12:36:40 [Python] (C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Qt] 23.04.2021 12:36:39 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 23.04.2021 12:36:40 [] (unknown:0) - This plugin dir: C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Qt] 23.04.2021 12:37:39 [] (unknown:0) - Switch to module:  “DICOM”<br>
[INFO][VTK] 23.04.2021 12:38:45 [vtkMRMLVolumeArchetypeStorageNode (000001D66305D680)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:473) - Loaded volume from file: F:/BREAST STUDY/FCDN_001/sSUSTRACCION - as a 6 frames MultiVolume by TriggerTime frame 0.nrrd. Dimensions: 704x704x160. Number of components: 1. Pixel type: unsigned short.<br>
[INFO][VTK] 23.04.2021 12:38:45 [vtkMRMLScene (000001D652E6B7A0)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[DEBUG][Qt] 23.04.2021 12:38:45 [] (unknown:0) - “Volume” Reader has successfully read the file “F:/BREAST STUDY/FCDN_001/sSUSTRACCION - as a 6 frames MultiVolume by TriggerTime frame 0.nrrd” “[0.94s]”<br>
[DEBUG][Qt] 23.04.2021 12:38:46 [] (unknown:0) - “Segmentation” Reader has successfully read the file “F:/BREAST STUDY/FCDN_001/Segmentation.seg.nrrd” “[0.41s]”<br>
[DEBUG][Python] 23.04.2021 12:38:51 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 23.04.2021 12:38:51 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[DEBUG][Python] 23.04.2021 12:38:51 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 23.04.2021 12:38:51 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 23.04.2021 12:38:51 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 23.04.2021 12:38:52 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[INFO][Python] 23.04.2021 12:38:58 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM<br>
[INFO][Python] 23.04.2021 12:38:59 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:457) - Window/level found in DICOM tags (center=1053.0, width=1830.0) has been applied to volume 201: AXI T2<br>
[DEBUG][Python] 23.04.2021 12:38:59 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:790) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.12471e-05 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 23.04.2021 12:38:58 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 23.04.2021 12:38:59 [] (unknown:0) - Window/level found in DICOM tags (center=1053.0, width=1830.0) has been applied to volume 201: AXI T2<br>
[DEBUG][Qt] 23.04.2021 12:39:17 [] (unknown:0) - Switch to module:  “Annotations”<br>
[DEBUG][Qt] 23.04.2021 12:39:28 [] (unknown:0) - Switch to module:  “DICOM”<br>
[DEBUG][Python] 23.04.2021 12:39:33 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMParametricMapPluginClass : Caching files<br>
[DEBUG][Python] 23.04.2021 12:39:33 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMParametricMapPluginClass : Using cached files<br>
[WARNING][Python] 23.04.2021 12:39:33 [Python] (C:\Users\Vane\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py:629) - Geometric issues were found with 1 of the series. Please use caution.<br>
[CRITICAL][Stream] 23.04.2021 12:39:33 [] (unknown:0) - Geometric issues were found with 1 of the series. Please use caution.<br>
[CRITICAL][Stream] 23.04.2021 12:39:33 [] (unknown:0) -<br>
[DEBUG][Python] 23.04.2021 12:39:33 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMSegmentationPluginClass : Caching files<br>
[DEBUG][Python] 23.04.2021 12:39:33 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMSegmentationPluginClass : Using cached files<br>
[DEBUG][Python] 23.04.2021 12:39:33 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:52) - DICOMTID1500PluginClass : Caching files<br>
[DEBUG][Python] 23.04.2021 12:39:37 [Python] (C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\QuantitativeReporting\lib\Slicer-4.11\qt-scripted-modules\base\DICOMPluginBase.py:49) - DICOMTID1500PluginClass : Using cached files<br>
[DEBUG][Qt] 23.04.2021 12:40:22 [] (unknown:0) - Found CommandLine Module, target is  C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/cli-modules/DWIConvert.exe<br>
[DEBUG][Qt] 23.04.2021 12:40:22 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 23.04.2021 12:40:22 [] (unknown:0) - Diffusion-weighted DICOM Import (DWIConvert) command line:</p>
<p>C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/cli-modules/DWIConvert.exe --conversionMode DicomToNrrd --outputVolume C:/Users/Vane/AppData/Local/Temp/Slicer/BBDHG_vtkMRMLDiffusionWeightedVolumeNodeB.nrrd --inputDicomDirectory C:/Users/Vane/AppData/Local/Temp/Slicer/__SlicerTemp__2021-04-23_12+40+21.979 --outputDirectory C:/Users/Vane/AppData/Local/Temp/Slicer --smallGradientThreshold 0.2 --transposeInputBVectors<br>
[DEBUG][Qt] 23.04.2021 12:40:30 [] (unknown:0) - Diffusion-weighted DICOM Import (DWIConvert) standard output:</p>
<p>======= DWI Convert Tool Program=========<br>
=================== this-&gt;m_SlicesPerVolume:50<br>
Dicom images are ordered in a slice interleaving way.<br>
ImageOrientationPatient (0020:0037): LPS Orientation Matrix<br>
0.999882 -0.000303788 -0.0153919<br>
1.14524e-11 0.999805 -0.0197331<br>
0.0153949 0.0197307 0.999687</p>
<p>this-&gt;m_SpacingMatrix<br>
1.12903 0 0<br>
0 1.12903 0<br>
0 0 3</p>
<p>NRRDSpaceDirection<br>
1.1289 -0.000342987 -0.0461756<br>
1.29302e-11 1.12881 -0.0591993<br>
0.0173813 0.0222767 2.99906</p>
<p>Slice 0: -190.334 -159.906 -71.0699<br>
Slice 4: -190.38 -159.966 -68.0708<br>
Slice order is IS<br>
Number of Slices: 200<br>
Number of Volumes: 4<br>
Number of Slices in each volume: 50<br>
===== gradient orientations:0 C:/Users/Vane/AppData/Local/Temp/Slicer/__SlicerTemp__2021-04-23_12+40+21.979/IM-0004-0004.dcm (0018,9089)  0 0 0<br>
B-value: 0; diffusion direction: 0, 0, 0<br>
===== gradient orientations:1 C:/Users/Vane/AppData/Local/Temp/Slicer/__SlicerTemp__2021-04-23_12+40+21.979/IM-0004-0008.dcm (0018,9089)  0 0 0<br>
B-value: 400; diffusion direction: 0, 0, 0<br>
===== gradient orientations:2 C:/Users/Vane/AppData/Local/Temp/Slicer/__SlicerTemp__2021-04-23_12+40+21.979/IM-0004-0012.dcm (0018,9089)  0 0 0<br>
B-value: 700; diffusion direction: 0, 0, 0<br>
===== gradient orientations:3 C:/Users/Vane/AppData/Local/Temp/Slicer/__SlicerTemp__2021-04-23_12+40+21.979/IM-0004-0016.dcm (0018,9089)  0 0 0<br>
B-value: 1100; diffusion direction: 0, 0, 0<br>
Scale Factor for Multiple BValues: 0 – sqrt( 0 / 1100 ) = 0<br>
Scale Factor for Multiple BValues: 1 – sqrt( 400 / 1100 ) = 0.603023<br>
Scale Factor for Multiple BValues: 2 – sqrt( 700 / 1100 ) = 0.797724<br>
Scale Factor for Multiple BValues: 3 – sqrt( 1100 / 1100 ) = 1<br>
Wrote file: C:/Users/Vane/AppData/Local/Temp/Slicer/BBDHG_vtkMRMLDiffusionWeightedVolumeNodeB.nrrd<br>
[ERROR][VTK] 23.04.2021 12:40:30 [vtkSlicerCLIModuleLogic (000001D65F9E34B0): Diffusion-weighted DICOM Import (DWIConvert) standard error:</p>
<p>W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
W: processing MR image … applying modality transform may create unexpected result<br>
WARNING: In D:\D\S\Slicer-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 480<br>
ImageSeriesReader (000002521C53F030)] (D:\D\S\Slicer-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:2017) - Non uniform sampling or missing slices detected,  maximum nonuniformity:2.26131<br>
[DEBUG][Qt] 23.04.2021 12:40:30 [] (unknown:0) - Diffusion-weighted DICOM Import (DWIConvert) completed without errors<br>
[INFO][VTK] 23.04.2021 12:40:30 [vtkMRMLScene (000001D673995010)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[INFO][Python] 23.04.2021 12:40:30 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM<br>
[INFO][Python] 23.04.2021 12:40:31 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:457) - Window/level found in DICOM tags (center=447.0, width=777.0) has been applied to volume 401: DWI_400-700-1100<br>
[DEBUG][Python] 23.04.2021 12:40:31 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:790) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.33179e-05 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 23.04.2021 12:40:30 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 23.04.2021 12:40:31 [] (unknown:0) - Window/level found in DICOM tags (center=447.0, width=777.0) has been applied to volume 401: DWI_400-700-1100<br>
[CRITICAL][Qt] 23.04.2021 12:40:31 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( “1onDisplayNodeModified(vtkObject*, vtkObject*)” ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 23.04.2021 12:40:31 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 23.04.2021 12:40:31 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM<br>
[INFO][Python] 23.04.2021 12:40:32 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:457) - Window/level found in DICOM tags (center=264.0, width=459.0) has been applied to volume 401: DWI_400-700-1100_1<br>
[DEBUG][Python] 23.04.2021 12:40:32 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:790) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.33179e-05 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 23.04.2021 12:40:31 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 23.04.2021 12:40:32 [] (unknown:0) - Window/level found in DICOM tags (center=264.0, width=459.0) has been applied to volume 401: DWI_400-700-1100_1<br>
[CRITICAL][Qt] 23.04.2021 12:40:32 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 23.04.2021 12:40:32 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 23.04.2021 12:40:32 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM<br>
[INFO][Python] 23.04.2021 12:40:32 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:457) - Window/level found in DICOM tags (center=232.0, width=404.0) has been applied to volume 401: DWI_400-700-1100_2<br>
[DEBUG][Python] 23.04.2021 12:40:32 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:790) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.33179e-05 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 23.04.2021 12:40:32 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 23.04.2021 12:40:32 [] (unknown:0) - Window/level found in DICOM tags (center=232.0, width=404.0) has been applied to volume 401: DWI_400-700-1100_2<br>
[CRITICAL][Qt] 23.04.2021 12:40:32 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 23.04.2021 12:40:32 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[INFO][Python] 23.04.2021 12:40:33 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM<br>
[INFO][Python] 23.04.2021 12:40:33 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:457) - Window/level found in DICOM tags (center=233.0, width=405.0) has been applied to volume 401: DWI_400-700-1100_3<br>
[DEBUG][Python] 23.04.2021 12:40:33 [Python] (C:/Users/Vane/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:790) - Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 1.33179e-05 mm, tolerance threshold is 0.001 mm).<br>
[INFO][Stream] 23.04.2021 12:40:33 [] (unknown:0) - Loading with imageIOName: GDCM<br>
[INFO][Stream] 23.04.2021 12:40:33 [] (unknown:0) - Window/level found in DICOM tags (center=233.0, width=405.0) has been applied to volume 401: DWI_400-700-1100_3<br>
[CRITICAL][Qt] 23.04.2021 12:40:33 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 23.04.2021 12:40:33 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject *,class vtkObject *) : Invalid object type calling display node modified event<br>
[WARNING][Python] 23.04.2021 12:41:01 [Python] (C:\Users\Vane\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py:1867) - toVTKString is deprecated! Conversion is no longer necessary.<br>
[DEBUG][Qt] 23.04.2021 12:41:01 [] (unknown:0) - Switch to module:  “Elastix”<br>
[CRITICAL][Stream] 23.04.2021 12:41:01 [] (unknown:0) - toVTKString is deprecated! Conversion is no longer necessary.<br>
[INFO][Python] 23.04.2021 12:41:50 [Python] (C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py:392) - Volume registration is started in working directory: C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335<br>
[INFO][Stream] 23.04.2021 12:41:50 [] (unknown:0) - Volume registration is started in working directory: C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335<br>
[INFO][Python] 23.04.2021 12:41:51 [Python] (C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py:392) - Register volumes…<br>
[WARNING][VTK] 23.04.2021 12:41:50 [] (unknown:0) - Generic Warning: In D:\D\S\Slicer-0\Libs\MRML\Core\vtkDataFileFormatHelper.cxx, line 237<br>
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to ‘File format name (.ext)’ format! Current format string: .mha<br>
[WARNING][VTK] 23.04.2021 12:41:50 [] (unknown:0) - Generic Warning: In D:\D\S\Slicer-0\Libs\MRML\Core\vtkDataFileFormatHelper.cxx, line 237<br>
vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to ‘File format name (.ext)’ format! Current format string: .mha<br>
[INFO][Stream] 23.04.2021 12:41:51 [] (unknown:0) - Register volumes…<br>
[WARNING][Python] 23.04.2021 12:41:51 [Python] (C:\Users\Vane\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py:1867) - toVTKString is deprecated! Conversion is no longer necessary.<br>
[INFO][Python] 23.04.2021 12:41:51 [Python] (C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py:493) - Register volumes using: C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\elastix.exe: [’-f’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\input\fixed.mha’, ‘-m’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\input\moving.mha’, ‘-out’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\result-transform’, ‘-p’, ‘C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0032_rigid.txt’, ‘-p’, ‘C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0032_bsplines.txt’]<br>
[CRITICAL][Stream] 23.04.2021 12:41:51 [] (unknown:0) - toVTKString is deprecated! Conversion is no longer necessary.<br>
[INFO][Stream] 23.04.2021 12:41:51 [] (unknown:0) - Register volumes using: C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\elastix.exe: [’-f’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\input\fixed.mha’, ‘-m’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\input\moving.mha’, ‘-out’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\result-transform’, ‘-p’, ‘C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0032_rigid.txt’, ‘-p’, ‘C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Par0032_bsplines.txt’]<br>
[INFO][Python] 23.04.2021 12:44:41 [Python] (C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py:392) - Generate output…<br>
[INFO][Stream] 23.04.2021 12:44:41 [] (unknown:0) - Generate output…<br>
[INFO][Python] 23.04.2021 12:44:41 [Python] (C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py:700) - Generate output using: C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\transformix.exe: [’-tp’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\result-transform/TransformParameters.1.txt’, ‘-out’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\result-resample’, ‘-in’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\input\moving.mha’, ‘-def’, ‘all’]<br>
[INFO][Stream] 23.04.2021 12:44:41 [] (unknown:0) - Generate output using: C:\Users\Vane\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\transformix.exe: [’-tp’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\result-transform/TransformParameters.1.txt’, ‘-out’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\result-resample’, ‘-in’, ‘C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\input\moving.mha’, ‘-def’, ‘all’]<br>
[INFO][VTK] 23.04.2021 12:48:00 [vtkMRMLVolumeArchetypeStorageNode (000001D6607F9120)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:473) - Loaded volume from file: C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\result-resample\result.mhd. Dimensions: 704x704x160. Number of components: 1. Pixel type: unsigned short.<br>
[INFO][VTK] 23.04.2021 12:48:00 [vtkMRMLScene (000001D6531736A0)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[DEBUG][Qt] 23.04.2021 12:48:00 [] (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/Vane/AppData/Local/Temp/Slicer/Elastix/20210423_124150_335\result-resample\result.mhd” “[1.02s]”<br>
[WARNING][Python] 23.04.2021 12:48:00 [Python] (C:\Users\Vane\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\slicer\util.py:593) - loadNodeFromFile <code>returnNode</code> argument is deprecated. Loaded node is now returned directly if <code>returnNode</code> is not specified.<br>
[INFO][Python] 23.04.2021 12:48:00 [Python] (C:/Users/Vane/AppData/Roaming/NA-MIC/Extensions-29402/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py:392) - Registration is completed<br>
[CRITICAL][Stream] 23.04.2021 12:48:00 [] (unknown:0) - loadNodeFromFile <code>returnNode</code> argument is deprecated. Loaded node is now returned directly if <code>returnNode</code> is not specified.<br>
[INFO][Stream] 23.04.2021 12:48:00 [] (unknown:0) - Registration is completed<br>
[DEBUG][Qt] 23.04.2021 12:51:08 [] (unknown:0) - Switch to module:  “Transforms”<br>
[WARNING][Qt] 23.04.2021 12:51:08 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 23.04.2021 12:51:08 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 23.04.2021 12:51:08 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 23.04.2021 12:51:08 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  242<br>
[WARNING][Qt] 23.04.2021 12:51:08 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 23.04.2021 12:51:08 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 23.04.2021 12:51:08 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 23.04.2021 12:51:08 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[DEBUG][Qt] 23.04.2021 12:51:36 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 23.04.2021 12:53:41 [] (unknown:0) - Switch to module:  “DWModeling”<br>
[DEBUG][Qt] 23.04.2021 12:54:10 [] (unknown:0) - Switch to module:  “Transforms”<br>
[DEBUG][Qt] 23.04.2021 12:54:23 [] (unknown:0) - Switch to module:  “DWModeling”<br>
[DEBUG][Qt] 23.04.2021 12:55:55 [] (unknown:0) - Found SharedObject Module<br>
[DEBUG][Qt] 23.04.2021 12:55:55 [] (unknown:0) - ModuleType: SharedObjectModule<br>
[DEBUG][Qt] 23.04.2021 12:56:02 [] (unknown:0) - DWModeling command line:</p>
<p>slicer:00007FFC746E9720 --processinformationaddress 000001D62023CA88 --model BiExponential --fittedVolume C:/Users/Vane/AppData/Local/Temp/Slicer/BBDHG_vtkMRMLMultiVolumeNodeC.nrrd --rsqrVolume slicer:000001D649360FE0#vtkMRMLScalarVolumeNode9 --slowDiff slicer:000001D649360FE0#vtkMRMLScalarVolumeNode10 --fastDiff slicer:000001D649360FE0#vtkMRMLScalarVolumeNode11 --fastDiffFraction slicer:000001D649360FE0#vtkMRMLScalarVolumeNode12 --monoExpInitParameters 0,0.0015 --biExpInitParameters 0,0.7,0.00025,0.002 --kurtosisInitParameters 0,1,0.0015 --stretchedExpInitParameters 0,0.0017,0.7 --gammaInitParameters 0,1.5,0.002 C:/Users/Vane/AppData/Local/Temp/Slicer/BBDHG_vtkMRMLMultiVolumeNodeB.nrrd<br>
[DEBUG][Qt] 23.04.2021 13:00:19 [] (unknown:0) - DWModeling standard output:</p>
<p>Will use the following b-values: 0 400 700 1100<br>
[INFO][VTK] 23.04.2021 13:00:19 [vtkMRMLScene (000001D620FFD760)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[INFO][Stream] 23.04.2021 13:00:20 [] (unknown:0) - Display node set and observed<br>
[DEBUG][Qt] 23.04.2021 13:01:22 [] (unknown:0) - Switch to module:  “Transforms”<br>
[DEBUG][Qt] 23.04.2021 13:01:24 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[CRITICAL][Qt] 23.04.2021 13:01:46 [] (unknown:0) - double __cdecl qSlicerSubjectHierarchyFolderPlugin::canOwnSubjectHierarchyItem(__int64) const : Input item is invalid<br>
[WARNING][VTK] 23.04.2021 13:01:46 [vtkMRMLSubjectHierarchyNode (000001D65E30D4F0)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2050) - GetItemDataNode: Invalid item ID given<br>
[CRITICAL][Qt] 23.04.2021 13:01:56 [] (unknown:0) - double __cdecl qSlicerSubjectHierarchyFolderPlugin::canOwnSubjectHierarchyItem(__int64) const : Input item is invalid<br>
[WARNING][VTK] 23.04.2021 13:01:56 [vtkMRMLSubjectHierarchyNode (000001D65E30D4F0)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2050) - GetItemDataNode: Invalid item ID given<br>
[DEBUG][Qt] 23.04.2021 13:01:59 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 23.04.2021 13:02:26 [] (unknown:0) - Switch to module:  “DWModeling”<br>
[DEBUG][Qt] 23.04.2021 13:02:33 [] (unknown:0) - Found SharedObject Module<br>
[DEBUG][Qt] 23.04.2021 13:02:33 [] (unknown:0) - ModuleType: SharedObjectModule<br>
[DEBUG][Qt] 23.04.2021 13:02:40 [] (unknown:0) - DWModeling command line:</p>
<p>slicer:00007FFC746E9720 --processinformationaddress 000001D62023CA88 --model BiExponential --mask slicer:000001D649360FE0#vtkMRMLLabelMapVolumeNode1 --fittedVolume C:/Users/Vane/AppData/Local/Temp/Slicer/BBDHG_vtkMRMLMultiVolumeNodeC.nrrd --rsqrVolume slicer:000001D649360FE0#vtkMRMLScalarVolumeNode9 --slowDiff slicer:000001D649360FE0#vtkMRMLScalarVolumeNode10 --fastDiff slicer:000001D649360FE0#vtkMRMLScalarVolumeNode11 --fastDiffFraction slicer:000001D649360FE0#vtkMRMLScalarVolumeNode12 --monoExpInitParameters 0,0.0015 --biExpInitParameters 0,0.7,0.00025,0.002 --kurtosisInitParameters 0,1,0.0015 --stretchedExpInitParameters 0,0.0017,0.7 --gammaInitParameters 0,1.5,0.002 C:/Users/Vane/AppData/Local/Temp/Slicer/BBDHG_vtkMRMLMultiVolumeNodeB.nrrd<br>
[DEBUG][Qt] 23.04.2021 13:02:45 [] (unknown:0) - DWModeling standard output:</p>
<p>Will use the following b-values: 0 400 700 1100<br>
[INFO][VTK] 23.04.2021 13:02:45 [vtkMRMLScene (000001D65315B8B0)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[DEBUG][Qt] 23.04.2021 13:03:01 [] (unknown:0) - Switch to module:  “Data”</p>

---

## Post #6 by @Mgi (2021-04-27 16:39 UTC)

<p>Hi <a class="mention" href="/u/fedorov">@fedorov</a> and <a class="mention" href="/u/pieper">@pieper</a>, any ideas?</p>

---

## Post #7 by @pieper (2021-04-27 18:07 UTC)

<p>It seems the data doesn’t conform to the expectations of the module, but it’s not obvious to me why that is.  Probably someone would need to do some debugging, ideally the original developer if they are available, have time, and are able to reproduce the issue.</p>

---

## Post #8 by @fedorov (2021-04-27 18:55 UTC)

<p>Sorry, I didn’t get a chance to look into to this yet. Are you able to reproduce the issue on a publicly available de-identified dataset?</p>

---
