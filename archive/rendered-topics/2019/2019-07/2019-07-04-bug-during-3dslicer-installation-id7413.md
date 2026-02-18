# Bug during 3DSlicer installation

**Topic ID**: 7413
**Date**: 2019-07-04
**URL**: https://discourse.slicer.org/t/bug-during-3dslicer-installation/7413

---

## Post #1 by @MachadoL (2019-07-04 15:44 UTC)

<p>Hi, guys.</p>
<p>I’m trying to install <strong>Slicer release 4.10.2</strong> in my Linux Mint 18.3 Sylvia Desktop.<br>
I  correctly installed <strong>CMake 3.13.4 and Qt 5.11.0</strong>.<br>
I go with CMake, configure and generate, everything goes ok!</p>
<p>But when I do <strong>sudo make</strong> in the slicer build folder… it runs and <strong>crashes</strong> with the following error:</p>
<pre><code>CMake Error at PCRE-prefix/src/PCRE-stamp/download-PCRE.cmake:159 (message):
Each download failed!
error: downloading 
'https://github.com/Slicer/SlicerBinaryDependencies/releases/download/PCRE/pcre-8.38.tar.gz' failed
     status_code: 1
     status_string: "Unsupported protocol"
     log:
     --- LOG BEGIN ---
     Protocol "https" not supported or disabled in libcurl

Closing connection -1
</code></pre>
<p>As trials to fix it, I did reinstall to the latest version <strong>OpenSSL</strong> and <strong>Clurl --with-ssl</strong>, with the last one not working well (I then installed that through synaptic). But no success at all.</p>
<p>Any help is very welcome.<br>
Thanks!</p>
<p>P.S. I just installed pure ITK 5.0, everything worked very well!</p>

---

## Post #2 by @lassoan (2019-07-04 17:12 UTC)

<p>This error seems to be a CMake SSL configuration error, which is not related to Slicer. There are several similar error reports on the web (such as <a href="https://stackoverflow.com/questions/29816529/unsupported-protocol-while-download-tar-gz-package" rel="nofollow noopener">this</a>) - one of the suggested solutions should work for you, too.</p>

---

## Post #3 by @MachadoL (2019-07-04 17:39 UTC)

<p>Thanks, Andrass.</p>
<p>Checking that right now!</p>

---

## Post #4 by @fedorov (2019-07-05 02:06 UTC)

<aside class="quote no-group" data-username="MachadoL" data-post="1" data-topic="7413">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/machadol/48/3372_2.png" class="avatar"> MachadoL:</div>
<blockquote>
<p>when I do <strong>sudo make</strong> in the slicer build folder</p>
</blockquote>
</aside>
<p>Just curious, why do you use sudo for building Slicer?</p>

---

## Post #5 by @MachadoL (2019-07-05 17:46 UTC)

<p>I guess I do this just to be sure it will not stop with some “permission denied” error… haha</p>

---

## Post #6 by @MachadoL (2019-07-08 13:06 UTC)

<p><strong>[SOLVED]</strong></p>
<p>In fact, as Andrass pointed out, it was a <strong>CMAKE PROBLEM</strong>. I did as it follows:</p>
<p>install the <strong>lib libcurl4-openssl-dev:</strong>:</p>
<pre><code>sudo apt-get install libcurl4-openssl-dev
</code></pre>
<p><strong>Rebuild CMake from source</strong> with the following comands:</p>
<pre><code>sudo ./bootstrap --system-curl
Make
Make install
</code></pre>
<p>Finally, I ran the standard recommendations for building 3D SLICER!</p>

---

## Post #7 by @jcfr (2019-07-08 13:48 UTC)

<p>Thanks for the update.</p>
<p>To simplify your workflow. Instead of building CMake from source, I suggest you download the CMake binaries available at <a href="https://cmake.org/download/" rel="nofollow noopener">https://cmake.org/download/</a></p>

---
