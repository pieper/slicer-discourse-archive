# Extension can't be installed!

**Topic ID**: 12012
**Date**: 2020-06-13
**URL**: https://discourse.slicer.org/t/extension-cant-be-installed/12012

---

## Post #1 by @sunshine_boycn (2020-06-13 23:57 UTC)

<p>Recently, Slicer can’t download the extension from extension manager.</p>
<p>The hint is :<br>
No extensions found for win:64-bit, revision: ‘1c531bd’. Please try a different combination</p>
<p>And my slicer is built on windows with the version of 4.11.0-2020-03-04 r1c531bd.</p>
<p>Thanks.</p>

---

## Post #2 by @jamesobutler (2020-06-14 00:11 UTC)

<p>Please see this response in another thread discussing the need to build your own extensions if you have built your own Slicer for development purposes.</p>
<aside class="quote quote-modified" data-post="12" data-topic="5126">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/macos-mojave-slicer4-10-install/5126/12">MacOS Mojave Slicer4.10 install </a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If you build your own Slicer, you are also expected to build all extensions, to ensure ABI compatibility. 
Once you have built Slicer, it is easy to build all extensions, since their build is fully automated. You can bundle any extension in your custom build so that your users don’t need to install any extensions. 
You can also try to replicate build environment of official Slicer builds on your computer (so that your custom Slicer build is ABI compatible with extensions in the official app stor…
  </blockquote>
</aside>

<p>You can also use the following reference about building extensions:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_build_an_extension_.3F" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_build_an_extension_.3F</a></p>

---

## Post #3 by @sunshine_boycn (2020-06-15 09:43 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="12012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>You can also use the following reference about building extensions:</p>
</blockquote>
</aside>
<p>But I means some other extensions such as SlicerRT, IGT and so on.</p>
<p>I have built the slicer from source but I can’t get all of them.</p>
<p>I still remember I could install the other extensions from “Extension Manager”.</p>

---

## Post #4 by @lassoan (2020-06-16 05:08 UTC)

<aside class="quote no-group" data-username="sunshine_boycn" data-post="3" data-topic="12012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ed8c4c/48.png" class="avatar"> sunshine_boycn:</div>
<blockquote>
<p>But I means some other extensions such as SlicerRT, IGT and so on.</p>
</blockquote>
</aside>
<p>Yes, and you can <em>all</em> the extension by building a single target (as described above). Building all the extensions is really easy after you have already built Slicer.</p>
<p>You might be able to install an extension package built by the official Slicer factory computer into Slicer that you have built yourself, but it would be hard to ensure ABI compatibility between these builds, so this is not recommended.</p>

---

## Post #5 by @sunshine_boycn (2020-06-25 05:33 UTC)

<p>Thank you very much~</p>
<p>Finally I understand what you mean. However another question is how to install ALL Extension once?</p>
<p>I could build one extension. It is the same with building my own C++ extension. But all the other extension is on the github? Have I need to download them one by one and build them seperately?</p>
<p>Thanks.</p>

---

## Post #6 by @lassoan (2020-06-25 12:41 UTC)

<p>After your local Slicer build is completed, you can <em>build</em> all the extensions very easily, as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_ExtensionsIndex#Manual_build">here</a>.</p>
<p>You should not install all extensions - for similar reasons you should not install all apps available in the app store to your phone. There are just too many extensions, installing all of them would clutter the module list, slow things down, and experimental modules may make the application unstable.</p>

---

## Post #7 by @Wenjun_Dong (2024-07-09 12:06 UTC)

<h1><a name="p-113804-extensions-can-not-be-installed-1" class="anchor" href="#p-113804-extensions-can-not-be-installed-1" aria-label="Heading link"></a>Extensions can not be installed.</h1>
<ul>
<li>Extensions install directory does NOT exist: <strong>/Volumes/Slicer-5.6.2-macosx-amd64/Slicer.app/Contents/Extensions-32448</strong></li>
</ul>
<p>How can I solve this problem?</p>

---

## Post #8 by @pieper (2024-07-09 12:14 UTC)

<p>You’ll need to drag copy the application into a writable directory (the disk-image is read-only)</p>

---
