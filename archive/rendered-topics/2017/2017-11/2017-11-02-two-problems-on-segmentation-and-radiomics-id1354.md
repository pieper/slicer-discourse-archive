---
topic_id: 1354
title: "Two Problems On Segmentation And Radiomics"
date: 2017-11-02
url: https://discourse.slicer.org/t/1354
---

# Two problems on segmentation and radiomics

**Topic ID**: 1354
**Date**: 2017-11-02
**URL**: https://discourse.slicer.org/t/two-problems-on-segmentation-and-radiomics/1354

---

## Post #1 by @happyle (2017-11-02 16:02 UTC)

<p>Operating system:windows 7<br>
Slicer version:3DSLICER 4.7.0<br>
Expected behavior:<br>
First,how can i add some more features to the Radiomics ?like 75Percentile for example,as i notise there are only two Percentiles (90Percentile and 10Percentile) in the firstorder feature.<br>
Secondly,i draw a segmentation using threshold of Segment Edtor,with a threshold range from 0 to 1000.but when i calculate the radiomic feature,it’s found that the value of Minimum and the Maximum is out of the range,that means there are still some area Unwanted in the segment and i did found them in the image,how to fix this?<br>
Thank you for the staff!</p>

---

## Post #2 by @lassoan (2017-11-02 16:27 UTC)

<aside class="quote no-group" data-username="happyle" data-post="1" data-topic="1354">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ec9cab/48.png" class="avatar"> happyle:</div>
<blockquote>
<p>Minimum and the Maximum is out of the range</p>
</blockquote>
</aside>
<p>Can you reproduce this using any of the sample data sets in Slicer?</p>
<p>I let <a class="mention" href="/u/fedorov">@Fedorov</a> or others comment on how to add more features.</p>

---

## Post #3 by @fedorov (2017-11-02 16:51 UTC)

<aside class="quote no-group" data-username="happyle" data-post="1" data-topic="1354">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ec9cab/48.png" class="avatar"> happyle:</div>
<blockquote>
<p>First,how can i add some more features to the Radiomics ?like 75Percentile for example,as i notise there are only two Percentiles (90Percentile and 10Percentile) in the firstorder feature.</p>
</blockquote>
</aside>
<p>New features should be added to pyradiomics directly, you should create an issue to discuss this here: <a href="https://github.com/Radiomics/pyradiomics/issues" class="inline-onebox">Issues · AIM-Harvard/pyradiomics · GitHub</a></p>
<aside class="quote no-group" data-username="happyle" data-post="1" data-topic="1354">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ec9cab/48.png" class="avatar"> happyle:</div>
<blockquote>
<p>Secondly,i draw a segmentation using threshold of Segment Edtor,with a threshold range from 0 to 1000.but when i calculate the radiomic feature,it’s found that the value of Minimum and the Maximum is out of the range,that means there are still some area Unwanted in the segment and i did found them in the image,how to fix this?</p>
</blockquote>
</aside>
<p>I don’t quite understand this. Are you saying that min and max reported by the Radiomics module are not the same as the actual range of the image for the segmented region?</p>

---

## Post #4 by @cpinter (2017-11-02 18:32 UTC)

<p>I tested the Threshold function in Segment Editor. Chose minimum of 70 and maximum of 120 on MRHead, then ran Segment Statistics. The minimum and maximum values under the segment in the volume were exactly 70 and 120.</p>

---

## Post #5 by @fedorov (2017-11-02 18:32 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I think that user was referring to using the Radiomics module/extension.</p>

---

## Post #6 by @cpinter (2017-11-02 18:42 UTC)

<p>I just confirmed that the error is not with the thresholding, so it doesn’t need to be checked.</p>

---

## Post #7 by @lassoan (2017-11-02 18:46 UTC)

<p>I’ve tried min/max computed by Radiomics module on one example and it worked correctly.</p>

---

## Post #8 by @happyle (2017-11-03 10:44 UTC)

<p>Thank you! <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/cpinter">@cpinter</a> and Fedorov<br>
I try again and find the problem is not exist.<br>
Maybe i have clicked on the smoothing or what?sorry for that~</p>

---
