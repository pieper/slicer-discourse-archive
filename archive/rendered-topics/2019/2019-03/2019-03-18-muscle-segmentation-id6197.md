---
topic_id: 6197
title: "Muscle Segmentation"
date: 2019-03-18
url: https://discourse.slicer.org/t/6197
---

# Muscle segmentation

**Topic ID**: 6197
**Date**: 2019-03-18
**URL**: https://discourse.slicer.org/t/muscle-segmentation/6197

---

## Post #1 by @Melodicpinpon (2019-03-18 21:30 UTC)

<p>Good evening gentlemen,</p>
<p>I would like to get a visualisation / segmentation of isolated muscles.</p>
<p>Which method do you recommend?</p>
<p>The purpose is to get the general volume of each of the muscles to create a 2D drawings of the 3D.<br>
The coloured dicom could be used for learning too.</p>

---

## Post #2 by @timeanddoctor (2019-03-19 05:00 UTC)

<p>you can use segmentation module and there is tutorial <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Image_Segmentation" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Image_Segmentation</a></p>

---

## Post #3 by @Melodicpinpon (2019-03-19 07:48 UTC)

<p>Thank you!<br>
I already watched the tutorials on the bones and the heart segmentation; my question was more specificaly directed on the muscular tissue:</p>
<p>-Are there parameters that could make the difference with the fat?<br>
-Is it recommended to work on an IRM? Is there a faster way to do it? (semi-automatic recognition)</p>
<p>Somebody must have tried…</p>
<p>I watched a tutorial on heart segementation basically saying that with ‘ITK’ he achieved a clean 3D model in 8 hours (instead of 24!?): <a href="https://www.youtube.com/watch?v=AQFvfPUD6QA" rel="nofollow noopener">https://www.youtube.com/watch?v=AQFvfPUD6QA</a>.<br>
-I guess on a dead body’s scan- and I can not afford to spend so much time on each structure…</p>

---

## Post #4 by @lassoan (2019-03-19 13:12 UTC)

<p>You need to figure out a segmentation procedure for each project, because even for the same anatomy each study has very different requirements and constraints (how accurate the segmentation it must be, where accuracy is critical and where you can accept inaccuracies, what kind of errors are acceptable, how much time you have for the segmentation, what is the imaging modality and image quality, etc).</p>
<p>For an anatomical model that will be used for teaching hundreds of students for thousands of hours, spending several days with segmenting a single case is completely normal. In contrast, when you segment a tumor from an intraoperative image during a surgical procedure then you may have a time limit of 2 minutes. Slicer has been used successfully in all these scenarios, so it is very likely that you’ll be able to establish a segmentation protocol that fulfills your needs.</p>
<p>When you segment muscles, there is no often no image intensity difference between nearby segments that you would like to separate, so most automatic segmentation methods would fail. However, you may very efficiently segment the volume by segmenting only a couple of slices and interpolate between them using “Fill between slices” effect.</p>
<p>To give more specific advice, we would need to know much more about your requirements and constraints.</p>

---

## Post #5 by @Melodicpinpon (2019-03-20 08:28 UTC)

<p>Alright, thank you for answering.<br>
I have had the confirmation from my radiologist boss that it was  the segmentation was well part of my job.</p>
<p>I had not tried the option fill beween slices, and I am glad to hear about it.</p>
<p>Have a good day.</p>

---
