# How to go to cumulative histogram from lung density histogram in parenchyma analysis module?

**Topic ID**: 163
**Date**: 2017-04-21
**URL**: https://discourse.slicer.org/t/how-to-go-to-cumulative-histogram-from-lung-density-histogram-in-parenchyma-analysis-module/163

---

## Post #1 by @broccoli (2017-04-21 11:30 UTC)

<p>Hello,</p>
<p>Below you’ll find the lung density histogram I’ve generated with the parenchyma analysis module provided in the chest imaging platform extension.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e08d44f77f19b1a8f91aeead13a136bfab0315ac.png" alt="image" data-base62-sha1="w2tCxJ8c21nZ73hIUdZPT1n8n00" width="597" height="463"></p>
<p>How can I use this histogram to determine the density (HU) at 15% of the cumulative frequency?<br>
Perhaps I am overlooking a built-in function, and otherwise I would like some advice on how to use the python interactor for this.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @raul (2017-04-22 00:14 UTC)

<p>Hi,</p>
<p>The module was updated recently to provide Perc15 and Perc10  metrics. Those should appear in the table that is part of the module. We only provide graphics for the PDF and not the CDF.</p>
<p>Thanks</p>
<p>/R</p>

---

## Post #3 by @broccoli (2017-04-24 07:47 UTC)

<p>In the Slicer appstore I only find the cip version from 12-12-2016 for Slicer version 4.6.2 (<a href="http://slicer.kitware.com/midas3/slicerappstore?os=win&amp;arch=amd64&amp;revision=25516&amp;category=Chest%20Imaging%20Platform&amp;search=&amp;layout=empty" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore?os=win&amp;arch=amd64&amp;revision=25516&amp;category=Chest%20Imaging%20Platform&amp;search=&amp;layout=empty</a>), which is the version I’ve been working with. Is it right that the updated version of chest imaging platform is only available for Slicer 4.7.0?</p>
<p>Thank you.</p>

---

## Post #4 by @raul (2017-04-24 12:45 UTC)

<p>Hi,</p>
<p>You will have to download Slicer nightly to get the latest version of the module.</p>
<p>Thanks</p>
<p>/R</p>

---

## Post #5 by @broccoli (2017-04-24 13:09 UTC)

<p>Perfect. It is works, thank you for your information!</p>

---
