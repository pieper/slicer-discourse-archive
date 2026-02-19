---
topic_id: 13226
title: "Radiomics Not Found In Slicer Extensions Manager"
date: 2020-08-29
url: https://discourse.slicer.org/t/13226
---

# 'Radiomics' not found in Slicer extensions manager

**Topic ID**: 13226
**Date**: 2020-08-29
**URL**: https://discourse.slicer.org/t/radiomics-not-found-in-slicer-extensions-manager/13226

---

## Post #1 by @Cody_Keller (2020-08-29 02:40 UTC)

<p>Hello,</p>
<p>I’ve newly downloaded the nightly-updating version of Slicer and am unable to find the Radiomics extension in the extensions manager. On the web-based archive, I found the extension for an older version of Slicer; however, manual installation via DeveloperToolsForExtensions was unable to install throwing an error “Extension file for wrong platform.” Haven’t been able to find info on what problem this represents, and hoping someone here could help.</p>
<p>Best,</p>
<p>Cody</p>

---

## Post #2 by @pieper (2020-08-29 14:29 UTC)

<p>Looks like a python version issue on the windows build.</p>
<pre><code class="lang-auto">CUSTOMBUILD : error : scikit-image 0.17.2 has requirement PyWavelets&gt;=1.1.1, but you'll have pywavelets 0.5.2 which is incompatible. [D:\D\P\S-0-E-b\Radiomics-build\python-pyradiomics.vcxproj]

</code></pre>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1999956" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1999956</a></p>

---

## Post #3 by @Jeff_W (2020-09-16 06:20 UTC)

<aside class="quote no-group" data-username="Cody_Keller" data-post="1" data-topic="13226">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cody_keller/48/7918_2.png" class="avatar"> Cody_Keller:</div>
<blockquote>
<p>hive, I found the extension for an older version of Slicer; however, manual installation via Developer</p>
</blockquote>
</aside>
<p>下载稳定版就可以了<br>
download stable one</p>

---

## Post #4 by @Elaine_CHEN (2025-10-21 06:40 UTC)

<p>Hello, I am unable to find the Radiomics plugin or download it on the latest version of the 3dslicer for the Macos，If you are willing to reply, I would be very grateful.</p>

---

## Post #5 by @pieper (2025-10-21 12:06 UTC)

<p>Unfortunately there’s still a build error and the project has no active funded maintainers.  Any community help would be great.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.cdash.org/viewBuildError.php?buildid=3967104">
  <header class="source">
      <img src="https://slicer.cdash.org/favicon.ico" class="site-icon" alt="" width="32" height="32">

      <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3967104" target="_blank" rel="noopener">slicer.cdash.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.cdash.org/viewBuildError.php?buildid=3967104" target="_blank" rel="noopener">SlicerPreview - Build Errors</a></h3>

  <p>
            CDash is an open source, web-based software testing server. CDash aggregates, analyzes, and displays the
            results of software testing processes submitted from clients located around the world. CDash is a part of a
           ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
