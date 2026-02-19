---
topic_id: 1783
title: "Cannot Find Snrmeasurement Module In Slicer 4 8 0"
date: 2018-01-08
url: https://discourse.slicer.org/t/1783
---

# Cannot find SNRMeasurement Module in Slicer 4.8.0

**Topic ID**: 1783
**Date**: 2018-01-08
**URL**: https://discourse.slicer.org/t/cannot-find-snrmeasurement-module-in-slicer-4-8-0/1783

---

## Post #1 by @xaggi (2018-01-08 14:07 UTC)

<p>I want to measure SNR in MRI images. I checked the documentation, one of the methods to measure SNR is using SNRMeasurement module. But I cannot find it in the modules list <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:"> Please guide. Also, if there is any better method to measure SNR, please let me know.</p>
<p>Thanks in advance!</p>

---

## Post #3 by @tokjun (2018-01-08 14:57 UTC)

<p>Thanks for your interest. The source code for the module is available at:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SNRLab/SNRMeasurement">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SNRLab/SNRMeasurement" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/8b4a4ff8bf6017d864fb595deb1a459e0b4ef48e03b6c0f33b4e06fd6b0dbe89/SNRLab/SNRMeasurement" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SNRLab/SNRMeasurement" target="_blank" rel="noopener nofollow ugc">GitHub - SNRLab/SNRMeasurement: 3D Slicer CLI to calculate signal-to-nose...</a></h3>

  <p>3D Slicer CLI to calculate signal-to-nose ratio using "difference image" method - GitHub - SNRLab/SNRMeasurement: 3D Slicer CLI to calculate signal-to-nose ratio using "difference im...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It is a scripted module and should run on a binary package of 3D Slicer. I haven’t used it for a while, and am not sure if it runs on the recent version of 3D Slicer. If you find any error, please let me know. It is not in the Slicer Extensions, but if there are some needs, I would be happy to put there.</p>
<p>Thanks,</p>

---

## Post #4 by @lassoan (2018-01-08 18:08 UTC)

<p><a class="mention" href="/u/tokjun">@tokjun</a> It seems that it is a CLI module, so users would need to build Slicer first and then build the module, which could be significant effort. I’ve tried and the module can be built and packaged successfully on Windows. Could you submit it to the extension manager to make it easy to access for users?</p>

---

## Post #5 by @tokjun (2018-01-08 20:08 UTC)

<p>Sorry, <a class="mention" href="/u/lassoan">@lassoan</a> is correct. Good to know that it is working on Windows. I’ll submit it to the extension manager.</p>

---

## Post #6 by @xaggi (2018-01-09 05:03 UTC)

<p>Yess, please submit it and make it easily accessible. Thank you very much!</p>

---
