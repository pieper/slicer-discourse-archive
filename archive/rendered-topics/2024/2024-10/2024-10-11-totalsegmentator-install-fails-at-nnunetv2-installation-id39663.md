---
topic_id: 39663
title: "Totalsegmentator Install Fails At Nnunetv2 Installation"
date: 2024-10-11
url: https://discourse.slicer.org/t/39663
---

# TotalSegmentator install fails at nnunetv2 installation

**Topic ID**: 39663
**Date**: 2024-10-11
**URL**: https://discourse.slicer.org/t/totalsegmentator-install-fails-at-nnunetv2-installation/39663

---

## Post #1 by @mikebind (2024-10-11 18:37 UTC)

<p>I want to try out the TotalSegmentator extension, however I can’t get it to run.  From a clean install of the most recent Slicer preview on Windows (5.7.0-2024-10-08), I installed TotalSegmentator extension plus other bookmarked extensions using the extension manager, then restarted Slicer.  In the TotalSegmentator module, I pressed the “Force Reinstall” button and installation appeared to proceed normally until installation of nnunetv2, which failed, stopping the installation process.  I ran into the exact same problem on 5.6.1, which led to me trying this on the most recent 5.7.0. Any suggestions?  The full log from the restarted session is below:</p>
<p>Actually, it was too long to paste into this post, instead it is linked here:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pastebin.com/4mTyqZqU">
  <header class="source">
      <img src="https://pastebin.com/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://pastebin.com/4mTyqZqU" target="_blank" rel="noopener nofollow ugc">Pastebin</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://pastebin.com/i/facebook.png" class="thumbnail">

<h3><a href="https://pastebin.com/4mTyqZqU" target="_blank" rel="noopener nofollow ugc">Slicer Log - Pastebin.com</a></h3>

  <p>Pastebin.com is the number one paste tool since 2002. Pastebin is a website where you can store text online for a set period of time.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2024-10-11 19:05 UTC)

<p>Thanks for reporting this.  Hopefully we can get TotalSegmentator working again.</p>
<p>For what it’s worth, the Auto3DSeg models are working well for me with similar results.</p>

---

## Post #3 by @mikebind (2024-10-11 19:07 UTC)

<p>Thanks, I’m currently installing Auto3DSeg to try that out as well.</p>

---

## Post #4 by @muratmaga (2024-10-11 19:22 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a></p>
<p>I am always suspicious of the paths that contain special characters. While Slicer is ok with them, I am not sure if every package/library is ok. Perhaps a quick test would be to try a path that doesn’t have “@” sign in it:</p>
<pre><code class="lang-auto">[INFO][Stream] 11.10.2024 10:42:44 [] (unknown:0) -   creating build\bdist.win-amd64\wheel\nnunetv2\dataset_conversion\datasets_for_integration_tests
[INFO][Stream] 11.10.2024 10:42:44 [] (unknown:0) -   copying build\lib\nnunetv2\dataset_conversion\datasets_for_integration_tests\Dataset996_IntegrationTest_Hippocampus_regions_ignore.py -&gt; build\bdist.win-amd64\wheel\.\nnunetv2\dataset_conversion\datasets_for_integration_tests
[INFO][Stream] 11.10.2024 10:42:44 [] (unknown:0) -   error: could not create 'build\bdist.win-amd64\wheel\.\nnunetv2\dataset_conversion\datasets_for_integration_tests\Dataset996_IntegrationTest_Hippocampus_regions_ignore.py': No such file or directory
[INFO][Stream] 11.10.2024 10:42:44 [] (unknown:0) -   [end of output]
[INFO][Stream] 11.10.2024 10:42:44 [] (unknown:0) -
[INFO][Stream] 11.10.2024 10:42:44 [] (unknown:0) -   note: This error originates from a subprocess, and is likely not a problem with pip.
[INFO][Stream] 11.10.2024 10:42:45 [] (unknown:0) -   ERROR: Failed building wheel for nnunetv2
[INFO][Stream] 11.10.2024 10:42:45 [] (unknown:0) - Failed to build nnunetv2
[INFO][Stream] 11.10.2024 10:42:45 [] (unknown:0) - ERROR: Could not build wheels for nnunetv2, which is required to install pyproject.toml-based projects
[ERROR][Python] 11.10.2024 10:42:45 [Python] (C:\Users\mike.bindschadler@seattlechildrens.org\AppData\Local\slicer.org\Slicer 5.7.0-2024-10-08\bin\Python\slicer\util.py:3049) - Failed to upgrade TotalSegmentator
</code></pre>

---

## Post #5 by @mikebind (2024-10-11 19:34 UTC)

<p>Thanks, I’ll try on a different machine.  That folder is my user directory on the institution-owned laptop, so I can’t change it, and I don’t know whether I have full permissions to other directories.  One other thought I had was that perhaps this could be running into <a href="https://www.google.com/search?q=windows+path+length+limit" rel="noopener nofollow ugc">Windows path length limits</a>.  I also don’t think I can do anything about that on this machine, but if that’s what’s happening, then it isn’t anything linked to nnunetv2 specifically.</p>

---

## Post #6 by @muratmaga (2024-10-11 19:40 UTC)

<p>You can still be able to try to install (or copy existing one) to a path like C:\Slicer (that used to be allowed at SCH).</p>

---

## Post #7 by @mikebind (2024-10-11 19:41 UTC)

<p>OK, thanks, I’ll try that.</p>

---

## Post #8 by @jamesobutler (2024-10-11 20:16 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="1" data-topic="39663">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>From a clean install of the most recent Slicer preview on Windows (5.7.0-2024-10-08)</p>
</blockquote>
</aside>
<p>I did the same thing and with a fresh pip cache so that all whls were redownloaded or regenerated. I can report that TotalSegmentator installation was successful for me and I ran the package against the CTChest sample data set.</p>
<p>My Windows username is only 11 characters compared to your 38 characters. It also does not have any special characters. So as Murat mentioned that @ character very well could be causing the problems when building that nnunetv2 whl.</p>

---

## Post #9 by @mikebind (2024-10-11 21:39 UTC)

<p>Updates:  I tried again from a C:\Slicer directory, and ran into the same error at the same point, so it does not appear to be a special character in path problem, or a path length problem.</p>
<p>I did get Auto3DSeg working fine, and got some moderately helpful partial results out of that, though I did have to scale up the infant data set I was working to closer to adult size before it would recognize anything at all. Saying that, it ran fast enough (&lt;30 sec), that it feels almost cost-free to try and just keep what might be useful.</p>
<p>I tried clearing the pip cache, and also tried not installing my other bookmarked extensions (just in case of some weird conflict there).  Same nnunetv2 error.</p>
<p>At some point in the past, I did try TotalSegmentator (I think back before v2) on a different machine and got it working successfully, but was generally unimpressed with the results on the data I was working with.  If Auto3DSeg quality is generally comparable to the current TotalSegmentator results, then I’m fine with just continuing to explore Auto3DSeg and give up on retrying TotalSegmentator.  Thanks for the help and suggestions, everyone!</p>

---
