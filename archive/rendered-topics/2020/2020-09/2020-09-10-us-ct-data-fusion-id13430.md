---
topic_id: 13430
title: "Us Ct Data Fusion"
date: 2020-09-10
url: https://discourse.slicer.org/t/13430
---

# US/ CT data fusion

**Topic ID**: 13430
**Date**: 2020-09-10
**URL**: https://discourse.slicer.org/t/us-ct-data-fusion/13430

---

## Post #1 by @emipaw (2020-09-10 21:10 UTC)

<p>Hi,</p>
<p>I have liver tumor data from US 3D (vol) and CT and I want to reg them. I tried with Landmark Segmentation but the scale wasn’t good enough (US image was too small - should I calibrate the image?). Now I am looking for other solutions. Is Slicer RT is good extension to reg different modalities? Or maybe you have other advices?</p>

---

## Post #2 by @lassoan (2020-09-10 21:19 UTC)

<p>Slicer is probably one of the best tool out there for many things, including multi-modality image registration (by relying on powerful toolkits, such as ITK, Elastix, BRAINS, VTK, …).</p>
<p>It would be better if you set your ultrasound image scale properly when you import it (what importer did you use?), but you can compute optimal correspondence automatically by setting result transform type to “Similarity” in Fiducial registration wizard module.</p>

---

## Post #3 by @emipaw (2020-09-10 22:03 UTC)

<p>I was able to open US 3D .vol files after installing SlicerHeart extension (I am not sure if it is an answer to your question about importer).</p>
<p>But I still can’t imagine how to deal with it: when I am watching Fiducial Registration module tutorial: <a href="https://www.youtube.com/watch?v=TBHr2wizGTM" rel="nofollow noopener">https://www.youtube.com/watch?v=TBHr2wizGTM</a> there are 2 segmentated skulls in one volume I assume and I would not have the same situation… I would have two different volumes and still don’t know how to proceed… Btw, is this Fiducial Registration module is available from 4.11? I am using 4.10.2 and in IGT section I see only Markups to Model…</p>
<p>Also, in my case, I was also interested in this video: <a href="https://www.youtube.com/watch?v=6VT5xPQQyBQ" rel="nofollow noopener">https://www.youtube.com/watch?v=6VT5xPQQyBQ</a> but I have a problem to load my segmentations - how it was done that data from MRI and US are loaded using “Load Dicom Data” button?</p>
<p>And the last question: I plan to perform Landmark segmentation again to try if I can achieve better results - sgould I use crop earlier? Before loading data? I am afraid that it would be inaccurate</p>

---

## Post #4 by @lassoan (2020-09-11 02:17 UTC)

<p>You can do all the things in Slicer that you asked about but there is a good chance that there are better ways to achieve what you need. Can you write a bit more about the overall goal of your project?</p>

---

## Post #5 by @emipaw (2020-09-11 09:03 UTC)

<p>Of course, sorry for being a little chaotic. My main goal is coregistration of US 3D and CT scans. I wanted to check, if this kind of fusion can be valid for doctors who are  preparing diagnosis and also I would like to check if there is a possibility to compare liver tumor volume measured on CT scans and on US 3D images. Firstly I tried to segment and measure volume for each modalities seperately and for CT I received 30 cm3 and for US 3D 12 cm3 that’s why I was starting wonder if US is scaled properly. My next move was trying use Landmark segmentation to coregistrate images (US as fixed and CT as movable) but like I mentioned before when I am doing it without cropping the US images was too small comparing to CT (I performed this alignment but it simply doesn’t look good).  If you could advice something I will be very greatful, I really want to receive something meanigful.</p>

---
