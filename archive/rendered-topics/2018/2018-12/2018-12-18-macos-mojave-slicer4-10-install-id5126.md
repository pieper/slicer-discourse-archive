---
topic_id: 5126
title: "Macos Mojave Slicer4 10 Install"
date: 2018-12-18
url: https://discourse.slicer.org/t/5126
---

# MacOS Mojave Slicer4.10 install 

**Topic ID**: 5126
**Date**: 2018-12-18
**URL**: https://discourse.slicer.org/t/macos-mojave-slicer4-10-install/5126

---

## Post #1 by @Roland (2018-12-18 14:41 UTC)

<p>Operating system: MacOX Mojave<br>
Slicer version: 4.10<br>
Expected behavior: Running the installed Slicer app<br>
Actual behavior: OSX linker load command limit reached</p>
<p>Hello there,<br>
I’ve installed Slicer4.10 from source on my Mac with Mojave. The install process went fine but when I execute Slicer, I get the error message from the OSX linker:</p>
<p>dyld: malformed mach-o: load commands size (36160) &gt; 32768</p>
<p>Any ideas on how to solve it are welcome !<br>
Thank you<br>
Roland</p>

---

## Post #2 by @pieper (2018-12-18 18:45 UTC)

<p>Hi <a class="mention" href="/u/roland">@Roland</a> -</p>
<p>This is your local build?  On one mac I was having similar issue so now I build with a short build tree path (e.g. I use /sq5).  But you can probably also get away with longer paths.</p>
<p>-Steve</p>

---

## Post #3 by @Roland (2018-12-19 09:47 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a><br>
Thank you for your reply. Yes, this is a local build. Do build tree paths make a difference in the linker loading commands ? (Sorry for the noob question) I wish I could avoid building again as the full process is very lengthy (~5h).<br>
Roland</p>

---

## Post #4 by @hherhold (2018-12-19 12:17 UTC)

<p>Parallel builds speed up the process greatly. Use ‘make -jN’ where N is the number of parallel build/compile processes you want to run. On my 3.5 year old MacBook pro I usually run make -j6, increasing or decreasing N depending on whatever else I’m doing while the build is running. The entire build finishes in about an hour (more or less).</p>
<p>Hope this helps.</p>

---

## Post #5 by @Roland (2018-12-19 12:30 UTC)

<p>Hi <a class="mention" href="/u/hherhold">@hherhold</a><br>
Thanks for the answer. Yes, I’ve been doing parallel build no worries, although recently.<br>
Do you suggest as <a class="mention" href="/u/pieper">@pieper</a> did, to use short tree build ?<br>
Best,</p>

---

## Post #6 by @lassoan (2018-12-19 14:27 UTC)

<p>For large projects, maximum source and/or build folder paths are limited an all platforms due to various reasons. Since the Slicer build path is not relocatable, you need to rebuild from scratch in a shorter path.</p>

---

## Post #7 by @hherhold (2018-12-19 14:39 UTC)

<p>Since running into the same problem you had, I’ve switched to shorter paths and stayed that way.</p>

---

## Post #8 by @Roland (2018-12-19 15:04 UTC)

<p>Hi guys,<br>
So the morale of the story would be to parallel build with a shorter path.<br>
Thank you, I will give it a try.<br>
Will keep you posted if successful.<br>
Best,</p>

---

## Post #9 by @Roland (2018-12-20 11:07 UTC)

<p>Just a quick comment, since this seems to be a common issue, it would be good to have it documented somewhere ?</p>

---

## Post #10 by @lassoan (2018-12-20 11:24 UTC)

<p>It was already mentioned in the build instructions but I added more details and examples when this topic came up here. See these sections:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CHECKOUT_slicer_source_files" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CHECKOUT_slicer_source_files</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#macOS:_dyld:_malformed_mach-o:_load_commands_size_.28....29_.3E_32768" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#macOS:_dyld:<em>malformed_mach-o:<em>load_commands_size</em>.28…29</em>.3E_32768</a></li>
</ul>

---

## Post #11 by @Roland (2018-12-21 12:29 UTC)

<p>Hi there,<br>
I’ve finally installed Slicer on /Slicer from the 4.10 revision. However, I’ve got the following error message when trying to install extensions:</p>
<pre><code class="lang-auto">No extensions found for mac osx:64-bit, revision: '0dc589e'. Please try a different combination
</code></pre>
<p>Any ideas why ? That’s be helpful to know.<br>
Thank you.<br>
Kind regards,</p>

---

## Post #12 by @lassoan (2018-12-21 13:19 UTC)

<p>If you build your own Slicer, you are also expected to build all extensions, to ensure ABI compatibility.</p>
<p>Once you have built Slicer, it is easy to build all extensions, since their build is fully automated. You can bundle any extension in your custom build so that your users don’t need to install any extensions.</p>
<p>You can also try to replicate build environment of official Slicer builds on your computer (so that your custom Slicer build is ABI compatible with extensions in the official app store) force your repository revision (by default a git hash) match a Slicer stable or nightly release revision (still SVN revision numbers) and then your extension manager will find the corresponding extensions.</p>

---

## Post #13 by @Roland (2018-12-21 13:31 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you for the reply. Although I’ve tried that for the <code>OpenIGTLink</code> extension but it doesn’t find it. Does the extension build need to be placed somewhere precisely ?<br>
Thanks again<br>
Roland</p>

---

## Post #14 by @lassoan (2018-12-21 22:28 UTC)

<p>After you have built the extrnsion, you need to add the folders where the shared libraries are to the additional module paths.</p>
<p>You can also specify the extension source code folder when you configure your Slicer build and then the extension gets bundled in the package that you build.</p>

---
