# Build 3D Slicer for MacOS arm64?

**Topic ID**: 35699
**Date**: 2024-04-24
**URL**: https://discourse.slicer.org/t/build-3d-slicer-for-macos-arm64/35699

---

## Post #1 by @GeneRisi (2024-04-24 03:58 UTC)

<p>PyTorch has support for using the shaders in the M series chips, but to use it, one has to use the arm64 version of Python. Should a native (in this case, M3) build of Slicer3D be possible? If yes, where should I get the 5.15.2 Qt package (for MacOS arm64)?</p>
<p>Thank you!</p>
<p>Gene</p>

---

## Post #2 by @jamesobutler (2024-04-24 11:27 UTC)

<p>Support for a macOS arm64 version of Slicer is something planned though not for the immediate short term. If you have technical build experience you can try following the collection of work arounds to get something working posted in the following issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5944">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5944" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5944" target="_blank" rel="noopener nofollow ugc">Unable to build from source on Apple silicon</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-12" data-time="17:46:43" data-timezone="UTC">05:46PM - 12 Oct 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/kliron" target="_blank" rel="noopener nofollow ugc">
          <img alt="kliron" src="https://avatars.githubusercontent.com/u/626811?v=4" class="onebox-avatar-inline" width="20" height="20">
          kliron
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Domain: build-system
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Steps to reproduce

I followed all the instructions from the [docs](https:/<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">/slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html#prerequisites) to build slicer from source. 

Build halts with the following error while trying to build DCMTK:

```
make[2]: *** [DCMTK-prefix/src/DCMTK-stamp/DCMTK-configure] Error 1
make[1]: *** [CMakeFiles/DCMTK.dir/all] Error 2
-- OpenSSL: Errors detected - See below.

ld: warning: double slash removed from -install_name (/Users/kliron/opt/slicer/OpenSSL//libcrypto.1.1.dylib)
ld: warning: The i386 architecture is deprecated for macOS (remove from the Xcode build setting: ARCHS)
ld: warning: ignoring file /Users/kliron/opt/slicer/zlib-install/lib/libz.a, building for macOS-i386 but attempting to link with file built for macOS-arm64
ld: warning: ignoring file /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.3.sdk/usr/lib/libSystem.tbd, missing required architecture i386 in file /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.3.sdk/usr/lib/libSystem.tbd (3 slices)

Undefined symbols for architecture i386:

"__DefaultRuneLocale", referenced from:
      _CONF_parse_list in conf_mod.o
  "___bzero", referenced from:
      _ASN1_BIT_STRING_set_bit in a_bitstr.o
      _asn1_item_embed_new in tasn_new.o
      _addr_strings in b_addr.o
      _mem_ctrl in bss_mem.o
      _BLAKE2b_Final in blake2b.o
      _BLAKE2s_Final in blake2s.o
      _bn_div_fixed_top in bn_div.o
      ...

[...an extensive output of a lot more missing symbols...]

ld: symbol(s) not found for architecture i386
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[4]: *** [libcrypto.dylib] Error 1
make[3]: *** [build_libs] Error 2

CMake Error at /Users/kliron/Projects/slicer/CMake/ExternalProjectForNonCMakeProject.cmake:104 (message):
  OpenSSL: build step failed with exit code '2'.
```

## Expected behavior

A successful build.

## Environment
- Slicer version: latest source tree
- Operating system: MacOS Big Sur 11.6

Has anyone been able to compile slicer from source on a M1 Mac? How do I bypass the missing i386 openssl library?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Some uses of PyTorch in things like TotalSegmentator are still not optimized for the MPS usage in PyTorch as seen at:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/wasserth/TotalSegmentator/issues/250">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/issues/250" target="_blank" rel="noopener nofollow ugc">github.com/wasserth/TotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/wasserth/TotalSegmentator/issues/250" target="_blank" rel="noopener nofollow ugc"> TotalsegmentatornRunning Slow on New M3Max Macbook Pro</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-12-29" data-time="17:56:48" data-timezone="UTC">05:56PM - 29 Dec 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/QianMuXiao" target="_blank" rel="noopener nofollow ugc">
          <img alt="QianMuXiao" src="https://avatars.githubusercontent.com/u/40720829?v=4" class="onebox-avatar-inline" width="20" height="20">
          QianMuXiao
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I'm running TotalSegmentator on my M3Max chip (16-core CPU 40-core GPU) Macbook <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">Pro and it's taking over 600 seconds to fully segment a 3D CT image of size 512*512*54, whereas it tends to take about 60 seconds on my 3070 GPU desktop. Is it possible that the latest version of totalsegmentator just uses the Macbook's CPU instead of calling the Macbook's "MPS" when using pytorch?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Therefore I can’t say for sure how much benefit you may get at this time.</p>

---

## Post #3 by @GeneRisi (2025-07-16 17:16 UTC)

<p>Hi James. I am still wondering about a Universal MacOS build or specifically an ARM64 MacOS build.</p>

---

## Post #4 by @mau_igna_06 (2025-07-16 17:23 UTC)

<p>Do you mean something like this guide below?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/BuildsOfSlicerForArmBasedSystemsMacAndLinux/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" alt="" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/BuildsOfSlicerForArmBasedSystemsMacAndLinux/" target="_blank" rel="noopener nofollow ugc">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/BuildsOfSlicerForArmBasedSystemsMacAndLinux/" target="_blank" rel="noopener nofollow ugc">Project Description</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @GeneRisi (2025-07-16 19:32 UTC)

<p>Does a native ARM64 version exist? I didn’t see a status update for the plan you pointed me to. Thanks!</p>

---

## Post #6 by @mau_igna_06 (2025-07-16 20:39 UTC)

<p>See <a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/BuildsOfSlicerForArmBasedSystemsMacAndLinux/#progress-and-next-steps" rel="noopener nofollow ugc">point 6 of section ProgressAndNextSteps</a> or the link below:</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e">
  <header class="source">

      <a href="https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e</a></h4>

  <h5>README.md</h5>
  <pre><code class="Markdown"># Slicer on ARM aarch64

These scripts were initially created to support building Slicer on ARM aarch64 associated with NVIDIA IGX running Ubuntu.

```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.4 LTS
Release:	22.04</code></pre>
   This file has been truncated. <a href="https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e" target="_blank" rel="noopener nofollow ugc">show original</a>
  <h5>build-CTKAppLauncher.sh</h5>
  <pre><code class="Shell">#!/bin/bash

# SPDX-FileCopyrightText: 2025 Jean-Christophe Fillion-Robin &lt;jcfr@kitware.com&gt;
# SPDX-License-Identifier: Apache-2.0

set -eo pipefail

script_dir=$(cd $(dirname $0) || exit 1; pwd)

err() { echo -e &gt;&amp;2 ERROR: $@\\n; }</code></pre>
   This file has been truncated. <a href="https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e" target="_blank" rel="noopener nofollow ugc">show original</a>
  <h5>build-Slicer.sh</h5>
  <pre><code class="Shell">#!/bin/bash

# SPDX-FileCopyrightText: 2025 Jean-Christophe Fillion-Robin &lt;jcfr@kitware.com&gt;
# SPDX-License-Identifier: Apache-2.0

set -eo pipefail

script_dir=$(cd $(dirname $0) || exit 1; pwd)

err() { echo -e &gt;&amp;2 ERROR: $@\\n; }</code></pre>
   This file has been truncated. <a href="https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
    There are more than three files. <a href="https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e" target="_blank" rel="noopener nofollow ugc">show original</a>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope it helps</p>

---

## Post #7 by @jamesobutler (2025-07-16 22:04 UTC)

<p><a class="mention" href="/u/generisi">@GeneRisi</a> There are some various scripts around that people have tried to build Slicer from source to build a ARM64 variant, but nothing official yet such as Slicer preview build of such a version.</p>
<p>The below issue is still in progress and various Slicer developers have been actively working on a long chain of dependency updates including Qt5 → Qt6 that is part of bringing in ARM64 support across all the various libraries that Slicer uses. It is currently being worked on and I expect it to continue for a month or two.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5944">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5944" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5944" target="_blank" rel="noopener nofollow ugc">Unable to build from source on Apple silicon</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-12" data-time="17:46:43" data-timezone="UTC">05:46PM - 12 Oct 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/kliron" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/626811?v=4" class="onebox-avatar-inline" width="20" height="20">
          kliron
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Domain: build-system
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Steps to reproduce

I followed all the instructions from the [docs](https:/<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">/slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html#prerequisites) to build slicer from source. 

Build halts with the following error while trying to build DCMTK:

```
make[2]: *** [DCMTK-prefix/src/DCMTK-stamp/DCMTK-configure] Error 1
make[1]: *** [CMakeFiles/DCMTK.dir/all] Error 2
-- OpenSSL: Errors detected - See below.

ld: warning: double slash removed from -install_name (/Users/kliron/opt/slicer/OpenSSL//libcrypto.1.1.dylib)
ld: warning: The i386 architecture is deprecated for macOS (remove from the Xcode build setting: ARCHS)
ld: warning: ignoring file /Users/kliron/opt/slicer/zlib-install/lib/libz.a, building for macOS-i386 but attempting to link with file built for macOS-arm64
ld: warning: ignoring file /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.3.sdk/usr/lib/libSystem.tbd, missing required architecture i386 in file /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.3.sdk/usr/lib/libSystem.tbd (3 slices)

Undefined symbols for architecture i386:

"__DefaultRuneLocale", referenced from:
      _CONF_parse_list in conf_mod.o
  "___bzero", referenced from:
      _ASN1_BIT_STRING_set_bit in a_bitstr.o
      _asn1_item_embed_new in tasn_new.o
      _addr_strings in b_addr.o
      _mem_ctrl in bss_mem.o
      _BLAKE2b_Final in blake2b.o
      _BLAKE2s_Final in blake2s.o
      _bn_div_fixed_top in bn_div.o
      ...

[...an extensive output of a lot more missing symbols...]

ld: symbol(s) not found for architecture i386
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[4]: *** [libcrypto.dylib] Error 1
make[3]: *** [build_libs] Error 2

CMake Error at /Users/kliron/Projects/slicer/CMake/ExternalProjectForNonCMakeProject.cmake:104 (message):
  OpenSSL: build step failed with exit code '2'.
```

## Expected behavior

A successful build.

## Environment
- Slicer version: latest source tree
- Operating system: MacOS Big Sur 11.6

Has anyone been able to compile slicer from source on a M1 Mac? How do I bypass the missing i386 openssl library?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @GeneRisi (2025-08-22 00:57 UTC)

<p>Hi James! Any updates on building on Apple silicon ?</p>
<p>Gene</p>

---

## Post #9 by @jamesobutler (2025-08-22 01:15 UTC)

<p>Nothing to report yet. <a class="mention" href="/u/jcfr">@jcfr</a> has been working diligently to upgrade Slicer to Qt6 and following that should be able to get to a native arm64 build.</p>
<p>Following some special instructions you can successfully build Slicer on arm64 by building an Intel x86_64 version of the application that runs on Apple Silicon through Rosetta.</p>

---

## Post #10 by @andy97 (2025-09-10 04:36 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="9" data-topic="35699">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>uccessfully build Slicer on arm64 by building an Intel x86_64 version of the application that runs on Apple Silicon through Rosetta.</p>
</blockquote>
</aside>
<p>Hi james,</p>
<p>do you have the link/docs to do this? and will building like this still run the compiled application on intel macs? or will it only work on arm64 (through rosetta) macs?</p>
<p>thanks!</p>

---

## Post #11 by @jamesobutler (2025-09-10 11:18 UTC)

<p>The following discourse post provides some details primarily about building for developing features with Slicer, but does include a comment of mine about the qt-easy-build process to build Qt from source while on a macOS arm machine which is necessary for packaging and distribution to other computers to be successful. Even on Intel Macs it is currently required to build Qt for on source to successfully package and distribute. And Yes these instructions will work for distribution onto Intel Macs as well as the arm Macs which will run it through Rosetta.</p>
<aside class="quote quote-modified" data-post="1" data-topic="40686">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/arhowe00/48/80367_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/developing-for-slicer-on-apple-silicon-build-targeting-x86-64/40686">Developing for Slicer on Apple Silicon (build targeting x86_64)</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
    </div>
  </div>
  <blockquote>
    The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html" rel="noopener nofollow ugc">developer docs</a> may need a minor update addressing development on the newer Macs (M-series chips). Here is a sufficient-for-development build from source on arm64 MacOS without requiring niche workarounds for specific libraries. The following steps explain how to build Slicer from source on M-chip computers. Note that the Slicer build still targets x86_64 (i.e. run through Rosetta 2), but native arm64 builds may be rolled out at a future date. To summarize the steps: 

Install Qt5 with x86_64…
  </blockquote>
</aside>


---

## Post #12 by @GeneRisi (2025-12-04 15:17 UTC)

<p>Hello James! Is there a status update on the arm64 MacOS build requirements?</p>
<p>Thank you.</p>
<p>Gene</p>

---

## Post #13 by @jamesobutler (2025-12-04 16:01 UTC)

<p>The preceding work of updating Slicer from Qt5 to Qt6 has made progress and <a class="mention" href="/u/lassoan">@lassoan</a> has been working to integrate a large number of commits recently to support this effort. Remaining changes for Qt6 support should hopefully wrap up here in the next week and then we will likely update the Slicer Preview to Qt6.</p>
<p>After that support for native arm64 builds will come. With the holidays and an upcoming Slicer project week in late-January - this task may ultimately happen later at that time. <a class="mention" href="/u/jcfr">@jcfr</a> has switched jobs and has less time available for the Slicer project, but others from Kitware will help support the infrastructure changes necessary to build and distribute arm64 native builds using Slicer factory build machines.</p>

---
