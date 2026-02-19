---
topic_id: 7803
title: "Pk Modelling Module Extension Missing"
date: 2019-07-29
url: https://discourse.slicer.org/t/7803
---

# PK Modelling Module Extension- Missing?

**Topic ID**: 7803
**Date**: 2019-07-29
**URL**: https://discourse.slicer.org/t/pk-modelling-module-extension-missing/7803

---

## Post #1 by @madeline (2019-07-29 22:26 UTC)

<p>Hi,</p>
<p>Just wondering if anyone can help me locate the PK Modelling Module in the latest 4.11.0 Slicer update?</p>
<p>I have been using the module for analysis for a few months and recently re-downloaded the software on a new hard drive and haven’t been able to locate it (or its merged module) in the extension manager.</p>
<p>Thanks.</p>

---

## Post #2 by @jamesobutler (2019-07-30 00:00 UTC)

<p>It appears that the extension for Slicer preview hasn’t been building successfully. <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1656227" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1656227</a></p>
<p>This is likely because the extension hasn’t been updated since Slicer transitioned to c++11 and ITK5.</p>
<p>It does appear that the extension is available if you use Slicer stable 4.10.2.</p>
<p>If you would like to use it with the latest Slicer core features, then I’d suggest contacting the maintainers of the source code and requesting an update. <a href="https://github.com/QIICR/PkModeling" rel="nofollow noopener">https://github.com/QIICR/PkModeling</a></p>

---

## Post #3 by @madeline (2019-07-30 08:00 UTC)

<p>Thanks James.</p>
<p>I did try the stable 4.10.2 version and unfortunately it wasn’t working. It still runs on my laptop using 4.10.1, but I will need to figure how to get that version on my new computer.</p>
<p>I have sent a request as you suggested. Hope to hear back soon.</p>

---

## Post #4 by @jamesobutler (2019-07-30 10:53 UTC)

<p>Could you explain the issues you are having using the extension with Slicer 4.10.2?</p>

---

## Post #5 by @madeline (2019-07-30 12:27 UTC)

<p>To use the PK modelling module, you first need to of course access the extension manager and select the module. The module is now all together missing from this library.</p>
<p>I took a guess it had been combined with another module for multi-purpose however I have been unable to identify which module that would be. If the module is having an error building, perhaps it was taken out from the library all together.</p>

---

## Post #6 by @jamesobutler (2019-07-30 12:30 UTC)

<blockquote>
<p>I did try the stable 4.10.2 version and unfortunately it wasn’t working.</p>
</blockquote>
<p>This is what I was asking about.</p>
<p>I just now tried Slicer 4.10.2 and was able to install the PK Modeling extension, so I wasn’t sure what issues you were having.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf0d4a4ca9d03eaa42cd07469b42b09c794e53c5.png" alt="pk-modeling-extension" data-base62-sha1="rg7FBvjPRllq5q8PlEQoXRoUKBT" width="631" height="420"></p>

---

## Post #7 by @madeline (2019-07-30 12:44 UTC)

<p>That is very interesting as none of the extensions were installing for me on the updated version, and you’ve managed 5… Plus PK. I will re-attempt the installation of 4.10.2 tomorrow on the hard drive and have hope it was a software installation error on my end.</p>
<p>Thanks.</p>

---

## Post #8 by @madeline (2019-08-01 02:56 UTC)

<p>Hi James,</p>
<p>Version 4.10.2 is working fine now with the PK Modelling Module. I will stick with this version until the update for 11.0 is complete. Thank you for your assistance.</p>

---
