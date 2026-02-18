# Parenchyma Analysis, series and variability

**Topic ID**: 28441
**Date**: 2023-03-18
**URL**: https://discourse.slicer.org/t/parenchyma-analysis-series-and-variability/28441

---

## Post #1 by @Josune (2023-03-18 11:28 UTC)

<p>Hello everyone:</p>
<p>We would like to perform a comparative study of lung CT scans obtained on different dates, for patients who have undergone radiotherapy treatment. We would like to use the data obtained with the Parenchyma Analysis app. However the series of each study have great variability of slice thickness, pixel spacing, etc. To compare series (studies) from different dates, is it sufficient that they have the same slice thickness?<br>
Thank you very much in advance,</p>
<p>Operating system:<br>
Slicer version: 4.11.20210226<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @rbumm (2023-03-19 16:32 UTC)

<p>Do you have different image spacings between the scans?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac471c00c968c9d3de9194bb07f1b94057903338.png" alt="image" data-base62-sha1="oA2tw2iLxPHtq0CmjLpdoMuPlWg" width="536" height="494"></p>
<p>Is that what you mean by slice thickness?</p>

---

## Post #3 by @Josune (2023-03-20 13:51 UTC)

<p>Thanks for your answer,</p>
<p>I mean the “slice thickness” that appears in the metadata (the 2.5000 mm in your image). Higher slice thickness spacing leads to loss of resolution quality in the visualizations, despite higher noise.</p>
<p>When performing lung densitometry with Parenchyma Analysis we saw that for the same study of the same patient, the values obtained were different depending on the series used (series with different slice thickness). However, it is difficult to obtain series in exactly the same conditions to be able to compare them, as we would lose data relating to some dates.<br>
I do not know if scans with very slightly different values (for example 1.25mmm and 1.5 mm) would be comparable or it would be better to lose the data of that date.<br>
Thanks,</p>

---

## Post #4 by @rbumm (2023-03-20 14:30 UTC)

<p>Could you try to resample your scalar volumes to identical spacings?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/102232855238c6421e65d06708a933f565b2a153.png" alt="image" data-base62-sha1="2iIUewEgRpWiSd9RqgdZB3AfShR" width="559" height="311"></p>

---

## Post #5 by @pieper (2023-03-20 16:02 UTC)

<p><a class="mention" href="/u/josune">@Josune</a> be aware that slice thickness (collimation, or size of the x-ray beam) is different from slice spacing (distance between slices) and probably both impact the quantitative results.   We don’t track the thickness in the Slicer user interface but you can get it from the <a href="https://dicom.innolitics.com/ciods/ct-image/image-plane/00180050">DICOM tags</a>.  I don’t know if the impact has been studied for this kind of analysis but you could search the literature.  You are right to be aware of these issues when interpreting your results.</p>

---

## Post #6 by @Josune (2023-03-20 16:05 UTC)

<p>Yes, thank you. Resampling is a good option, for example, those of 1.25 to 1.5 mm.<br>
We will analyze all the scans and dates, to see if we have enough patients with studies in identical conditions. If not possible, we will use resampling. We can test the method with those studies with a large number of series at different slice thickness.</p>

---

## Post #7 by @Josune (2023-03-20 16:09 UTC)

<p>es, I suspected so, slice thickness depends on the device on which the measurement was taken, and the way it was taken. Thank you very much for confirming that.<br>
I have found some articles in the literature, not too many, I will have to do a more exhaustive search.<br>
But probably the best idea is to compare only series in identical conditions.<br>
Best regards,</p>

---
