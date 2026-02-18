# How to segment uterus and ovary automatically

**Topic ID**: 37006
**Date**: 2024-06-25
**URL**: https://discourse.slicer.org/t/how-to-segment-uterus-and-ovary-automatically/37006

---

## Post #1 by @changjiang (2024-06-25 07:26 UTC)

<p>Dear Professor Wasserth:<br>
I’m very thanks for you, today Totalsegmentator was run successfully in 3D Slicer in my computer. Thanks for you and your team hard work. I’m a doctor, we often use 3-D Slice before operation with segment editor,it waste lot of time. But a little regret for it no segment for uterus and tumor.As the proverbsaying women hold half the sky.I’m a clinical doctor,so relationship of tumor to surrounding area is very important. Irealy wish you and your team study the part to segment tumor.</p>

---

## Post #2 by @changjiang (2024-06-25 08:06 UTC)

<p>The steps for 3Dslicer to successfully run Totalsegmentator</p>
<p>Step 1: Download the new version of 3Dslicer5.70, It is best to have a memory requirement of 8GB or more.</p>
<p>Part 2: Running 3Dslicer5.70 internal Python,</p>
<ol>
<li>Install Python using internal Python</li>
</ol>
<p>The command is: pip-install (“torch torch torch vision torch studio – index URL”) <a href="https://download.pytorch.org/whl/cpu" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cpu</a> ")</p>
<ol start="2">
<li>
<p>Install totalsegmentator in the extensions of 3Dslicer</p>
</li>
<li>
<p>Install totalsegmentator using internal Python</p>
</li>
</ol>
<p>The command is: pip_istall (“TotalSegmentator”)</p>
<ol start="4">
<li>
<p>Restart 3Dslice and input you CT images, run Total Segmentator, and must with Fast.</p>
</li>
<li>
<p>Successfully you can view the 3D image.</p>
</li>
<li>
<p>In the application modules, use Date can operate segmentate parts by youself.</p>
</li>
</ol>
<p>7.Unfortunately, there is no segmentate for the uterus and ovaries.</p>

---
