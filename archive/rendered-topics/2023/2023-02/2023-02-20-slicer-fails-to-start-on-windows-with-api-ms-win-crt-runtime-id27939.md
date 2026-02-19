---
topic_id: 27939
title: "Slicer Fails To Start On Windows With Api Ms Win Crt Runtime"
date: 2023-02-20
url: https://discourse.slicer.org/t/27939
---

# Slicer fails to start on Windows with "api-ms-win-crt-runtime-l1-1-0.dll is missing" error popup

**Topic ID**: 27939
**Date**: 2023-02-20
**URL**: https://discourse.slicer.org/t/slicer-fails-to-start-on-windows-with-api-ms-win-crt-runtime-l1-1-0-dll-is-missing-error-popup/27939

---

## Post #1 by @fedorov (2023-02-20 22:17 UTC)

<p>I am trying to help a user who is unable to run the latest Slicer 5 on a windows machine due to the error " api-ms-win-crt-runtime-l1-1-0.dll is missing". At the same time, Slicer 4 works fine.</p>
<p>I pointed the user to this article, but the user is reporting that it didn’t help, and the same error message shows up on Slicer startup.</p>
<p>Is there anything else we can suggest? I will ask that user to join the forum and provide any additional details here, as needed.</p>

---

## Post #2 by @pieper (2023-02-20 22:21 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> - I’m not seeing the links in your post, but I think you mean these two that we had discussed.  To clarify, did the user confirm that they tried installing the package from the second link or did they just report that the Adobe article didn’t help them understand the issue?  Also did they report what version of Windows they are running?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://helpx.adobe.com/download-install/kb/error_on_launch.html">
  <header class="source">
      <img src="https://www.adobe.com/favicon.ico" class="site-icon" width="48" height="48">

      <a href="https://helpx.adobe.com/download-install/kb/error_on_launch.html" target="_blank" rel="noopener">helpx.adobe.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://helpx.adobe.com/download-install/kb/error_on_launch.html" target="_blank" rel="noopener">Error: api-ms-win-crt-runtime-l1-1-0.dll is missing</a></h3>

  <p>Find solution to the error: The program can't start because api-ms-win-crt-runtime-l1-1-0.dll is missing from your computer. Try reinstalling the program to fix this problem.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://support.microsoft.com/en-us/topic/update-for-universal-c-runtime-in-windows-c0514201-7fe6-95a3-b0a5-287930f3560c">
  <header class="source">
      <img src="https://support.microsoft.com/favicon-32x32.png" class="site-icon" width="32" height="32">

      <a href="https://support.microsoft.com/en-us/topic/update-for-universal-c-runtime-in-windows-c0514201-7fe6-95a3-b0a5-287930f3560c" target="_blank" rel="noopener">support.microsoft.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://support.microsoft.com/en-us/topic/update-for-universal-c-runtime-in-windows-c0514201-7fe6-95a3-b0a5-287930f3560c" target="_blank" rel="noopener">Update for Universal C Runtime in Windows - Microsoft Support</a></h3>

  <p>Describes an update for Universal C Runtime (CRT) in Windows 8.1, Windows RT 8.1, Windows Server 2012 R2, Windows 8, Windows RT, Windows Server 2012, Windows 7 SP1, Windows Server 2008 R2 SP1, Windows Vista SP2, or Windows Server 2008 SP2.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @fedorov (2023-02-20 22:23 UTC)

<p>Ah, sorry! Here’s the exchange with the user (David). I emailed David and asked him to join the discussion. Hope he can clarify what he did shortly.</p>
<blockquote>
<blockquote>
<p>can you please look at this page and see if the suggested approach resolves the problems you showed me trying to run Slicer version 5 on your computer?</p>
<p><a href="https://helpx.adobe.com/download-install/kb/error_on_launch.html" class="inline-onebox">Error :api-ms-win-crt-runtime-l1-1-0.dll is missing</a></p>
</blockquote>
</blockquote>
<blockquote>
<p>Unfortunately, installing the windows update did not help: I have still the same error message.</p>
</blockquote>

---

## Post #4 by @jamesobutler (2023-02-20 23:44 UTC)

<p>What version of Windows is this machine? Is this an old version such as Windows 7/8.1?</p>
<p>What version of Slicer 4 was working on this machine?</p>
<p>When running Slicer 5 were there any extensions installed? Was this a factory build of Slicer or some custom app?</p>

---

## Post #5 by @jamesobutler (2023-02-21 00:41 UTC)

<p>This thread details what appears to be the same issue</p><aside class="quote" data-post="1" data-topic="25340">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b2d939/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-5-1-0-crashed-on-win7/25340">Slicer 5.1.0 crashed on win7</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    api-ms-win-core-path-l1-1-0.dll error on startup. After installing the dll Slicer gives an error 0xc000007b… 
Help me with installation please
  </blockquote>
</aside>


---

## Post #6 by @gcsharp (2023-02-21 19:26 UTC)

<p>To further muddy the water, my experience is you can get this error if <strong>an unrelated</strong> statically linked dll is missing.</p>
<p>My suggestion would be to use a dependency walker to debug.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lucasg/Dependencies">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lucasg/Dependencies" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/f4235b2b2c1639fbcc836560e3275540517ed9200044aff22c2e221776d0c410/lucasg/Dependencies" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lucasg/Dependencies" target="_blank" rel="noopener nofollow ugc">GitHub - lucasg/Dependencies: A rewrite of the old legacy software...</a></h3>

  <p>A rewrite of the old legacy software "depends.exe" in C# for Windows devs to troubleshoot dll load dependencies issues. - GitHub - lucasg/Dependencies: A rewrite of the old legacy softwar...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @spiderman (2023-02-22 02:18 UTC)

<p>Hello, most of this problem is because of your computer system, I have tried three times, when I install on the win7 system will appear this error, win10 system will not.</p>

---
