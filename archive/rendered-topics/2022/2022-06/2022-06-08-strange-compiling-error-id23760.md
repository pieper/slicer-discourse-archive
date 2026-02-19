---
topic_id: 23760
title: "Strange Compiling Error"
date: 2022-06-08
url: https://discourse.slicer.org/t/23760
---

# Strange compiling error

**Topic ID**: 23760
**Date**: 2022-06-08
**URL**: https://discourse.slicer.org/t/strange-compiling-error/23760

---

## Post #1 by @whu (2022-06-08 03:26 UTC)

<p>When I compiled the SlicerHeart again using CMake.  I just want a Release version.<br>
The <code>OPENSLL_INCLUDE_DIR</code> was set to <code>C:/Slicer/SlicerBuild/OpenSSL-install/Release/include</code><br>
But when compiling, there is error:</p>
<pre><code class="lang-auto">8&gt;CMake Error at C:/Slicer/SlicerBuild/Slicer-build/SlicerConfig.cmake:704 (message):
8&gt;  Variable OPENSSL_INCLUDE_DIR defined prior calling 'find_package(Slicer)'
8&gt;  does NOT match value used to configure Slicer.  It probably means that a
8&gt;  different OPENSSL_INCLUDE_DIR has been used to configure this project and
8&gt;  Slicer.
8&gt;
8&gt;  OPENSSL_INCLUDE_DIR=C:/Slicer/SlicerBuild/OpenSSL-install/Debug/include
8&gt;
8&gt;
8&gt;  Slicer_OPENSSL_INCLUDE_DIR=C:/Slicer/SlicerBuild/OpenSSL-install/Release/include
8&gt;Call Stack (most recent call first):
8&gt;  C:/Slicer/SlicerBuild/Slicer-build/SlicerConfig.cmake:747 (slicer_config_set_ep)
8&gt;  CMakeLists.txt:21 (find_package)
8&gt;
8&gt;
8&gt;-- Configuring incomplete, errors occurred!
</code></pre>
<p>Maybe the <code>OPENSSL_INCLUDE_DIR=C:/Slicer/SlicerBuild/OpenSSL-install/Debug/include</code> is set automatically ??</p>
<p>Anyone who occurred this ?</p>
<p>thanks</p>

---

## Post #2 by @mau_igna_06 (2022-06-08 09:54 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> <a class="mention" href="/u/jcfr">@jcfr</a> may be able to help woth this I think. Thank you guys</p>

---

## Post #3 by @RafaelPalomar (2022-06-13 08:33 UTC)

<p>Hello <a class="mention" href="/u/whu">@whu</a>. I can try to reproduce this on Linux. I’ll try 3D Slicer <code>master</code> branch and SlicerHeart <code>master</code> branch. Please, let me know if you have used any other version/commit of any of those.</p>
<p>Rafael.</p>

---

## Post #4 by @whu (2022-06-14 00:55 UTC)

<aside class="quote no-group" data-username="whu" data-post="1" data-topic="23760">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/7ab992/48.png" class="avatar"> whu:</div>
<blockquote>
<p>ybe the OPENSSL_INCLUDE_DIR=C:/Slicer/SlicerBuild/OpenSSL-install/De</p>
</blockquote>
</aside>
<p>Thanks.<br>
Taht is windows platform, VS2019.</p>

---

## Post #5 by @RafaelPalomar (2022-06-20 07:08 UTC)

<p><a class="mention" href="/u/whu">@whu</a>, I’ve tried the latest Slicer (<code>master</code> branch) with the latest SlicerHeart (<code>master</code> branch) and I cannot reproduce this problem (Linux, though). From your last reply, it is not clear whether you are using the <code>master</code> branch for both Slicer and SlicerHeart. Could  you give it a try and let us know if there are still problems?</p>

---

## Post #6 by @jcfr (2022-06-20 20:17 UTC)

<p><a class="mention" href="/u/whu">@whu</a> Could you make sure you are configuring both Slicer and SlicerHeart specifying the same configuration (Debug, Release, …) ?</p>

---

## Post #7 by @whu (2022-06-21 15:12 UTC)

<p>I used the debug mode under Windows using vs2019, successful.<br>
Later I changed to Release mode, then that compiling error happened.<br>
I am not sure that would be occured again.</p>

---

## Post #8 by @jcfr (2022-06-21 15:31 UTC)

<blockquote>
<p>Later I changed to Release mode, then that compiling error happened.</p>
</blockquote>
<p>If this was not a clean build, it likely explained the issue. Toggling between built type on windows is not tested or supported.</p>

---
