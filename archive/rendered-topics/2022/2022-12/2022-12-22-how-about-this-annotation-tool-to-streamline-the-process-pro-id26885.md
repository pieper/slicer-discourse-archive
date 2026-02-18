# How about this annotation tool to streamline the process ? (Prototype)

**Topic ID**: 26885
**Date**: 2022-12-22
**URL**: https://discourse.slicer.org/t/how-about-this-annotation-tool-to-streamline-the-process-prototype/26885

---

## Post #1 by @Tibo (2022-12-22 14:42 UTC)

<p>Hello,</p>
<p>I’ve recently built a small “extension” for Slicer that automatizes a bit the annotation process (loading patients, exporting segmentations, switching to the next patient, displays information about the patient for the doctors to have a basic idea of what they are looking for…). The implementation is pretty naive and really fine tuned for my needs but it seems interesting and it has been used for other projects as well.</p>
<p>However it is not a proper extension as the installation process relies in replacing the .slicerrc.py file with the one provided. The github link is <a href="https://github.com/ThibaultSau/Slicer-Annotation/" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ThibaultSau/Slicer-Annotation: Script for 3d Slicer that automates annotation process</a> (apologies part of it is in french).</p>
<p>What I want to gather is :</p>
<ul>
<li>Is there an extension that already allows this kind of automation ? (I haven’t found one in the marketplace but you never know)</li>
<li>Would it be interesting to make this a proper extension ?</li>
</ul>
<p>Thank you !</p>

---

## Post #2 by @pieper (2022-12-22 15:31 UTC)

<p>Yes, I think there’s a need for this kind of tooling.  Your work reminds me a bit of the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator">CaseIterator</a>.  It’s a challenge to make a general purpose tool that also solves specific use cases well, but if you have the time and interest in making your work general purpose it would make a nice extension.</p>

---

## Post #3 by @lassoan (2022-12-22 16:56 UTC)

<p>I agree, these kind of tools makes review/segmentation of many cases more convenient. MONAILabel module provides some of these features, too (loads the next case, may provide automatic segmentation, saves the results, learns from that, loads the next case, …).</p>
<p>It would be nice to build a single module that can readily fulfill the most common use cases and would allow customization for a perfect fit for each project’s workflow. The CaseIterator extension might be a good starting point if the workflow is based on a single shared folder. For a remote server based solution MONAILabel might be considered, too.</p>
<p>I’ve noticed that you used GPLv3 license for your scripts. It may not be obvious that this is a very unfriendly license for open science, as it severely limits how the software can be used. In this community we use permissive licenses (BSD, Apache, MIT, etc.) for our open-source contributions, which allow free collaboration - building on each other’s work and extending, improving, and sharing our results freely and voluntarily - and anyone to use it without imposing any restrictions.</p>

---

## Post #4 by @Tibo (2022-12-23 10:22 UTC)

<p>Thanks for your inputs,</p>
<p>I’ll be first doing a bit of cleaning up of the code and making it a bit more generic (make some files not required and such, maybe get a language option…) and then I’ll release it on a proper extension.</p>
<p>I’ll change the license and then we can go on from there changing it as needed</p>

---
