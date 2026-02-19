---
topic_id: 11330
title: "Question About Sizing Information"
date: 2020-04-28
url: https://discourse.slicer.org/t/11330
---

# question about sizing information

**Topic ID**: 11330
**Date**: 2020-04-28
**URL**: https://discourse.slicer.org/t/question-about-sizing-information/11330

---

## Post #1 by @Glass (2020-04-28 14:12 UTC)

<p>Operating system: Mac OS catalina 10.15.3<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello, I was wondering if someone could help me with something that is probably very simple.</p>
<p>I have started using Slicer, due to lockdown. I have micro-CT scans of moth brains, which are provided to me in TIFF stacks.I wish to use the software to segment parts of the moth brain and quantify the volumes for each part. I previously used Avizo and was very much still a beginner with that.</p>
<p>I’ve managed to import the TIFF stack, but there is obviously no automatic information about sizing. I have the pixel size for each scan, for example 4.9292um.</p>
<p>I changed the units to um in the application settings and set the image spacing as 4.9292 x 4.9292 x 4.9292, but when I measure the volume of the segments, the values are very unrealistic. I am just wondering where I have gone wrong?</p>
<p>Thanks for any help anyone can give.</p>

---

## Post #2 by @lassoan (2020-04-28 15:38 UTC)

<p>Changing unit in the application is still somewhat experimental and there are known issues (see for example <a href="https://github.com/Slicer/Slicer/issues/3657">https://github.com/Slicer/Slicer/issues/3657</a>). Nevertheless, it would help if you could report any places where you find that reported size is inconsistent with the specified unit and we’ll address them.</p>
<p>In the meantime, as a workaround, you can keep unit at the default (mm) and choose a scaling value that will make your image spacing to be around 0.01-10 “mm”, and consider this scaling value whenever you enter any data or read any reasults. For example, if your real image spacing is 5um, use a 100x scaling and type 0.5mm for spacing (instead of 0.005); and when for example you read a length measurement, divide it by 100 to get the actual length (and divide by 1 million to get actual volume for volume measurements).</p>

---

## Post #3 by @Glass (2020-04-29 07:22 UTC)

<p>Great, thanks for your help!</p>

---
