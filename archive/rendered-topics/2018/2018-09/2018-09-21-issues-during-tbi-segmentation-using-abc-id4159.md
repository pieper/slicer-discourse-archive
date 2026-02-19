---
topic_id: 4159
title: "Issues During Tbi Segmentation Using Abc"
date: 2018-09-21
url: https://discourse.slicer.org/t/4159
---

# Issues during TBI segmentation using ABC

**Topic ID**: 4159
**Date**: 2018-09-21
**URL**: https://discourse.slicer.org/t/issues-during-tbi-segmentation-using-abc/4159

---

## Post #1 by @Alexxx9596 (2018-09-21 02:00 UTC)

<p>Hello Slicer community!</p>
<p>First post on a public forum so bare with me. I am attempting to segment brain lesions using Atlas based classification (ABC). Following through the tutorials that are provided both on this webpage and on the <a href="http://nitrc.org/projects/abc" rel="nofollow noopener">nitrc.org/projects/abc</a> website, I have had 2 problems. First off, whenever I attempt to click apply using ABC (following their guidelines exactly) it results in the brain turning completely black. So much so that there is nothing left in each view and just a black screen. I have tried with newer and older version and have redownloaded ABC multiple times. Furthermore, whenever I attempt to find the color map schemes they refer to many times I am unable to. In their tutorial (<a href="https://www.slicer.org/slicerWiki/images/d/de/TBISegmentation_tutorial.pdf" rel="nofollow noopener">https://www.slicer.org/slicerWiki/images/d/de/TBISegmentation_tutorial.pdf</a>), it references color map schemes model_1_jake, module_2_peach and module_3_Brain. I was only able to find them referencing these three specific color map schemes, but never how to actually get them in 3DSlice. When I attempt to find them under module maker, I cannot. Thank you for any support you can provide. Also, I have a feeling I am not including many important details, so please let me know what I should include to make it easier to help.</p>
<p>Thanks again!<br>
Alex</p>

---

## Post #2 by @pieper (2018-09-21 17:55 UTC)

<p>Unfortunately that’s a pretty old extension so I’m not sure anyone uses or maintains it.  You could try contacting the authors of the corresponding papers.  Probably it could be fixed if someone is able to put in the time for debugging.</p>

---

## Post #3 by @lassoan (2018-09-22 12:05 UTC)

<p>I’ve tried the ABC module on Windows by following <a href="https://www.slicer.org/wiki/Documentation/4.4/Modules/ABC">instructions on the Slicer wiki</a> and got the same result - black image. Application log does not indicate any trivial software error - it seems that EM algorithm does not converge (nan values appear in all metrics after 3 iterations).</p>
<p>I would suggest to contact Marcel Prastawa, who is listed as maintainer on the <a href="https://www.slicer.org/wiki/Documentation/4.4/Modules/ABC">project page</a>. If he does not respond then try others who are associated with this project.</p>

---

## Post #4 by @Alexxx9596 (2018-09-24 19:03 UTC)

<p>Thank you! I will do so and if I get a response will update this forum.</p>

---
