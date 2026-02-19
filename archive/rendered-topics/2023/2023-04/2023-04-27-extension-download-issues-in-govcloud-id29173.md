---
topic_id: 29173
title: "Extension Download Issues In Govcloud"
date: 2023-04-27
url: https://discourse.slicer.org/t/29173
---

# Extension download issues in govcloud

**Topic ID**: 29173
**Date**: 2023-04-27
**URL**: https://discourse.slicer.org/t/extension-download-issues-in-govcloud/29173

---

## Post #1 by @bbkonk (2023-04-27 13:31 UTC)

<p>I have slicer installed on a Windows ec2 instance in govcloud. I’ve tried a few versions (5.2.1, 5.2.2, 5.3.0).</p>
<p>If I attempt to install from extensions manager, I receive “Failed downloading: <a href="https://slicer-packages.kitware.com/api/v1/file/...../download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/...../download</a>”. I’m trying to install the MONAILabel plugin, but the issue I’m running into happens with any extension install.</p>
<p>I tried using the extensions catalog website (<a href="https://extensions.slicer.org/catalog/All/30893/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>) provided in this thread: <a href="https://discourse.slicer.org/t/new-release-5-0-3-unable-to-download-extension/24524" class="inline-onebox">New release 5.0.3, unable to download extension</a>. I’m able to download and then install from file, but the plugin isn’t findable in slicer (I’ve done a number of restarts). I still see MONALabel as installed in extensions manager, but if I try to uninstall I receive: “Failed to open extensions settings file C:/apps/bin/…/NA-MIC/Slicer-31317.ini” (I’ve also tried 30893.ini).</p>
<p>Hoping for any tips on what to try next.</p>

---

## Post #2 by @pieper (2023-04-27 13:40 UTC)

<p>Be sure to follow these instructons:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions-without-network-connection" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions-without-network-connection</a></p>
<p>If that;s not working probably you should start fresh, maybe on a fresh VM instance and follow these instructions:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerCloud/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerCloud/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerCloud/" target="_blank" rel="noopener">NA-MIC Project Weeks</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Check the log files and see where the first error messages come up.  I’ve never used govcloud but it’s probably locked down in some way that will require you to do some workarounds.</p>

---
