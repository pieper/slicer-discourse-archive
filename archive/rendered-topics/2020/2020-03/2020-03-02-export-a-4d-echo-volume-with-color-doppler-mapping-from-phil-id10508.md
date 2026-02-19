---
topic_id: 10508
title: "Export A 4D Echo Volume With Color Doppler Mapping From Phil"
date: 2020-03-02
url: https://discourse.slicer.org/t/10508
---

# Export a 4D echo volume with color doppler mapping from philips

**Topic ID**: 10508
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/export-a-4d-echo-volume-with-color-doppler-mapping-from-philips/10508

---

## Post #1 by @bjce (2020-03-02 20:22 UTC)

<p>I could already export a 4D echocardiography volume from Philips ultrasoud machine. In cardiac echocardiography, we can acquire 4D volume with the addition of the color doppler mapping which helps to characerize the flow, in valvular disease for example (valvular stenosis or regurgitation) What I really would like to do is to export this 4D echocardiography volume with color doppler data from philips. Is it possible to do it on with 3D slicer?</p>
<p>Many thanks in advance!</p>

---

## Post #2 by @lassoan (2020-03-03 01:51 UTC)

<p>I guess you <a href="https://github.com/SlicerHeart/SlicerHeart#philips">exported the 4D volume via QLab</a>. Unfortunately, as far as I know, QLab still cannot export color Doppler images.</p>
<p>It is not just Philips, but all other ultrasound device manufacturers store most 3D/4D data in private fields and don’t give researchers free access (in fact, Philips is among the better ones by making at least Cartesian B-mode image export availalbe). We keep complaining to them that these limitations slow down research and ultimately hurt patients, but there has not been much effect so far. Please talk to your Philips representative about this, make it clear why data export is important for you. If many users request it then maybe they will do something.</p>

---

## Post #3 by @bjce (2020-03-03 07:46 UTC)

<p>Dear Mr. Lasso</p>
<p>First of all thank you very much for developing a free high quality software such as 3D slicer which is  immensely useful for clinical research. Yes I exported 4D Volume via QLab. And yes indeed It not possible from there to export color doppler images. In fact I already contacted Philips and they told me that it is not possible to export color doppler images. Now, If you do a ultrasound exam with philips machine and export it as a whole, you have a dicomdir file + a list of other files. The number of those files correspond to the number of screenshots / 2D loops / 3D loops. There is no way to know which one is which except with the size of the files (the 3D loops files are, I think the largest). In thoses big files are 3D loops with color doppler. What I was wondering was if there was a way to directly reading those files (assuming you knew which one was which) with 3D Slicer without having to export through QLab</p>
<p>Many thanks in advance for your precious help</p>

---

## Post #4 by @lassoan (2020-03-05 01:57 UTC)

<p>I have spent some time with this and it is not entirely hopeless to reverse engineer the native file format (see current status <a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/Philips4dUsReader">here</a>), but it would probably require several more weeks of work to do that and success is not guaranteed.</p>
<p>It would be much easier to write an importer if Philips publicly released the specification of their private fields. As far as I remember last time we asked, they would have only provided that information under non-disclosure agreement and other conditions, which would prevent us from releasing our solution as a publicly available open-source tool.</p>
<p>It would be nice if you could ask them about specification of their native file format (including those private fields that are necessary to reconstruct Cartesian image volumes) and see what they tell now.</p>

---

## Post #5 by @bjce (2020-03-16 19:25 UTC)

<p>Dear Mr. Lasso</p>
<p>Thank you very much for your answer. So the answer I had previously got from Philips was “The QLAB doesn’t support Cartesian format for 3D Color datasets export. It does for non-color datasets.”. This answer was given to me the reprentative from Philips who talked to the engineers. I never directly talked with the engineer personaly. I just sent the same representative an email asking about specification of their native file format (including those private fields that are necessary to reconstruct Cartesian image volumes). But I’m not sure if they are going to be more helpful. If there is anything else I can do to help, please let me know!</p>
<p>Many thanks again for your time and your expertise</p>
<p>Best regards</p>

---
