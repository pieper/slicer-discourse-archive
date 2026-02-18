# Can't find the segmentation wizard

**Topic ID**: 1637
**Date**: 2017-12-11
**URL**: https://discourse.slicer.org/t/cant-find-the-segmentation-wizard/1637

---

## Post #1 by @CaDi (2017-12-11 18:01 UTC)

<p>Hi,</p>
<p>I use 3Dslicer for manual segmentation, modelling and visualization of EM datasets (using version 4.8.0, windows). I would be happy to use the segmentation wizard for improved segmentation:<br>
<div class="lazyYT" data-youtube-id="_7oZygGp2ds" data-youtube-title="3D Slicer Tutorial - Segmentation Wizard" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div></p>
<p>But I can’t find the tool, even in the nighty built version 4.9.0. Is there a new name? Or is the version only available using Linux or Mac?</p>
<p>Best regards,<br>
Carsten</p>

---

## Post #2 by @ihnorton (2017-12-11 18:07 UTC)

<p>The <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=wizard">build dashboard</a> looks fine. Did you install the Extension (it shows up for me on Mac / 4.8)? I think this step is not mentioned in the video:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Installing_an_extension" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Installing_an_extension</a></p>
<p>(cc <a class="mention" href="/u/abeers">@abeers</a>)</p>

---

## Post #3 by @CaDi (2017-12-11 18:21 UTC)

<p>Hi,</p>
<p>I just was confused because I lost many of the modules after changing the version. But I forgot to look at the extension manager, I opened it using the wrong window (using the modules). After opening it by the view options, another window opened where I can choose the extensions, it seems to work now (found the wizard), thanks for your fast reply!</p>

---

## Post #4 by @lassoan (2017-12-11 18:48 UTC)

<p>This extension is just one of the many tools for segmentation. If you tell us what images you have and whay you would like to segment, then we can give advise you on potential approaches.</p>

---

## Post #5 by @CaDi (2017-12-11 19:24 UTC)

<p>I have different kinds of EM structures on serial sections. Different cells (with bad signal to noise ratio, I had to find the boundaries), inclusions surrounded by cell membranes (I was able to use the tracing drawing tool in IMOD/3dmod on some of these structures) and inclusions without cell membranes. The last ones were perfect for segmentation using IMOD/3dmod and the contour auto tool, because they were very electron dense and the signal to noise ratio was very good. Here, I was able to perform almost on all of them this automated (kind of interpolation) segmentation.<br>
Does someone know a good tool/module to perform measurements? I want to measure the volume of these structures, the diamter etc. I wasn’t able to find this tool in the extension manager:<br>
<a href="https://www.slicer.org/wiki/Modules:Measurements-Documentation-3.6" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Modules:Measurements-Documentation-3.6</a></p>

---

## Post #6 by @lassoan (2017-12-14 02:29 UTC)

<p>If you segmented structures, then you can get statistics (volume, area, average intensity, etc.) using Segment Statistics module.</p>
<p>You can make size measurements by placing rulers (there is a drop-down menu on the toolbar). There is some additional options in Annotations module. We’ll add more features (measure along curves, angle measurements, etc.) in the coming few months.</p>

---
