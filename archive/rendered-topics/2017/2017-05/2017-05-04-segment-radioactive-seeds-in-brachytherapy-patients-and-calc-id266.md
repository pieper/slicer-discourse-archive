# Segment radioactive seeds in brachytherapy patients and calculate dose

**Topic ID**: 266
**Date**: 2017-05-04
**URL**: https://discourse.slicer.org/t/segment-radioactive-seeds-in-brachytherapy-patients-and-calculate-dose/266

---

## Post #1 by @hongtao_zhang (2017-05-04 14:47 UTC)

<p>Hi Csaba,<br>
I am working with Tina Kapur now. I am a doctor and physicist focus on 125I seeds brachytherapy in China. It is difficult to use TPS to segment the seed in CT automatically. After the brachytherapy, the physicist have to pick up the seeds one by one manually to finish the postoperative dose calculation. This is difficult sometimes and time consuming. Is there a way to segment the seeds with slicer easily? Maybe we can use slicer to calculate the dose after seeds and tumor segmentation.  In the brachytherapy TPS, the seeds were assumed as a point source to calculate dose. So if we can segment the seeds and find the center of them, we can assumed the center as the point source. Then dose can be calculated. For the tumor and organ at risks, at first we can segmented them manually or use the segmentation method of radiotherapy.<br>
Thank you very much.<br>
.​​</p>

---

## Post #2 by @cpinter (2017-05-04 17:31 UTC)

<p>Hi Hongtao,</p>
<p>I downloaded the dataset you shared. I think it can be segmented in Segment Editor by using the threshold effect first, then the Scissors effect to cut out the unneeded parts. I will try to figure out a better way if I have more time.</p>
<p>The seed locations can be then acquired as follows:</p>
<ol>
<li>Segment the seeds so that only the seeds are in the segmentation, and they are not merged (an individual “blob” for each seed)</li>
<li>Use the Island effect’s Split islands to segments option to separate them to individual segments</li>
<li>A simple script can create fiducials at the center of masses of the seeds. I can easily write such a script for you</li>
</ol>
<p>These seed ficucials can then be the input for the dose calculation, which - as Greg explained on the mailing list (for the record he pointed to the AAPM TG-43 dose calculation formalism, and mentioned that validation using film or other method is necessary) - is easy to do, I imagine with a simple convolution.</p>
<p>Also I noticed that the MRML scene that was with the volume is an outdated one. I’d like to suggest to you to use a recent nightly version of Slicer, instead of 4.6. The segmentation tools have improved a lot since the stable release.</p>
<p>Let me know if you have further questions.</p>

---

## Post #3 by @hongtao_zhang (2017-05-04 19:15 UTC)

<p>Hi Csaba,<br>
I am really glad to hear you said it is easy for you. If we can make automatic segmentation and dose calculation happen, I have almost 500 cases to study. If it is not enough, I will make a big database and persuade other doctors add the data in it. Beside segmentation and dose calculation, we can use the data to do other research such as study the dose and the tumor shrink speed. This will be useful for doctor.<br>
I used the new version to create the file. This is a new patient and the data is much better than the previous one.<br>
Thank you.<br>
Best,<br>
Hongtao</p>

---

## Post #4 by @hongtao_zhang (2017-05-04 19:15 UTC)

<p>Hi Hongtao,</p>
<p>Please use one forum for the discussion. We already use 4 (mailing list, discourse, email thread with Tina, this thread), and it already became unfollowable. Let’s add every comment and answer on discourse [1].</p>
<p>I’d like to emphasize again: I don’t have the capacity to work on dose calculation, or a planning module. I offered my help writing that script I mentioned at point 3 in my discourse answer, and to connect you with the Sunnybrook group in case you intend to also develop a planning module, not just a segmentation and dose calculation one.</p>
<p>Do you have a timeline for this work? Also do you have a student or engineer or somebody who can work on it, or you’re doing this project alone?<br>
Tina, if you feel the need to chime in, please don’t hold it back. I’m a bit confused, so some clarification would be helpful.</p>
<p>Thanks,<br>
csaba</p>

---

## Post #5 by @hongtao_zhang (2017-05-04 19:22 UTC)

<p>Hi Csaba,<br>
I am sorry for bother you a lot and I am very appreciate that you can help. I have a team of doctors and student in China work with me but without engineer. There is not a timeline for this work till now.<br>
Thank you very much.<br>
Hongtao</p>

---

## Post #6 by @cpinter (2017-05-04 20:36 UTC)

<p>Sounds good! Please review the steps I described and let me know if you have further questions.<br>
Thanks!</p>

---

## Post #7 by @lassoan (2017-05-05 13:05 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>A simple script can create fiducials at the center of masses of the seeds. I can easily write such a script for you</p>
</blockquote>
</aside>
<p>If you implement that, it would be great if you could add it to the Segment Statistics module.</p>

---

## Post #8 by @hongtao_zhang (2017-05-05 13:36 UTC)

<p>Hi Sharp,<br>
What do you mean when you say ‘‘is dead easy to implement’’. If we can segment the seeds first, is it difficult to calculate the dose with TG-43 formalism?<br>
Thank you very much.<br>
Hongtao Zhang</p>

---

## Post #9 by @jcfr (2017-05-06 03:39 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>create fiducials at the center of masses of the seeds.</p>
</blockquote>
</aside>
<p>Using the ITK filter <code>itkFFTNormalizedCorrelationImageFilter</code> could be used to find the center of each seed. In other word, the maximum of correlation between a synthetic representation of the seed and the corresponding overlapping region in the image would be the center of mass.</p>

---

## Post #10 by @lassoan (2017-05-08 11:57 UTC)

<p>9 posts were split to a new topic: <a href="/t/using-simpleitk-with-segmentations/280">Using SimpleITK with Segmentations</a></p>

---
