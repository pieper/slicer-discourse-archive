---
topic_id: 14836
title: "Troubleshooting Extension Build Process Manually Building An"
date: 2020-12-02
url: https://discourse.slicer.org/t/14836
---

# Troubleshooting Extension Build Process - Manually Building an Extension

**Topic ID**: 14836
**Date**: 2020-12-02
**URL**: https://discourse.slicer.org/t/troubleshooting-extension-build-process-manually-building-an-extension/14836

---

## Post #1 by @nrex45 (2020-12-02 00:55 UTC)

<p>Hello all. There is quite a bit of documentation on building extensions available, but admittedly I’m a novice programmer and am having some trouble understanding a few of the steps and am looking for some guidance.</p>
<p>I have used the extension wizard to build and extension and am in the process of going through the “publishing an extension” checklist" and would like to manually build an extension to test it as documented <a href="https://www.slicer.org/w/index.php/Documentation/Nightly/Developers/Build_ExtensionsIndex#Manual_build" rel="noopener nofollow ugc">here</a>.<br>
A. I’m trying to follow the steps listed under " Build your own set of extensions against Slicer trunk build tree" and running into problems. I do not understand the prerequisit "2. Slicer trunk has been checkout into <code>/path/to/Slicer-master</code> and built into <code>/path/to/Slicer-master-SuperBuild-Release</code><br>
What exactly does this mean? I’m having trouble understanding the goal here.</p>
<p>B. Also, the code block specifies “export SLICER=${HOME}/slicer4/latest/Slicer”… I am working on a mac and the default installation location, I believe, is “export Slicer_DIR=/Users/Applications/Slicer.app”… Is this the appropriate location for this variable, or should it be export “Slicer_DIR=/Users/Applications/Slicer.app/Contents/MacOS/Slicer”? (I think this is an incredibly simple question but I’m having trouble googling it)</p>
<p>C. Is a test manual build really even necessary if I have a .s4ext file “ready” (but not tested) and have otherwise completed the majority of the checklist?</p>
<p>I will likely have more questions but this is probably a fine place to start.</p>

---

## Post #2 by @jamesobutler (2020-12-02 01:43 UTC)

<aside class="quote no-group" data-username="nrex45" data-post="1" data-topic="14836">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nrex45/48/7664_2.png" class="avatar"> nrex45:</div>
<blockquote>
<p>Slicer trunk has been checkout into <code>/path/to/Slicer-master</code> and built into <code>/path/to/Slicer-master-SuperBuild-Release</code><br>
What exactly does this mean? I’m having trouble understanding the goal here.</p>
</blockquote>
</aside>
<p>This just means you have a built version of Slicer. It is the same as described at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#set-up-source-and-build-folders" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a>. Do you have a built version of Slicer already? Based on your “B)” section I’m thinking not. Is your extension C++ based modules or python based modules?</p>
<p>There is also another documentation section about building an individual extension <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_build_an_extension_.3F" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/FAQ/Extensions - Slicer Wiki</a>. This is a little different than building the Slicer extensions index which can build a set of extensions.</p>
<aside class="quote no-group" data-username="nrex45" data-post="1" data-topic="14836">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nrex45/48/7664_2.png" class="avatar"> nrex45:</div>
<blockquote>
<p>C. Is a test manual build really even necessary if I have a .s4ext file “ready” (but not tested) and have otherwise completed the majority of the checklist?</p>
</blockquote>
</aside>
<p>It is of course good to test building your extension otherwise your extension might fail and then won’t show up as an option to distribute if you choose to submit to the Slicer Extensions Index. Generally the .s4ext is less necessary to test directly since it is fairly simple formatting, but the appropriate building of your extension (the CMakeLists.txt and supporting files) is what is more important and the more likely area where issues occur.</p>
<p>What method have you been using to install/use the modules of your extension in Slicer during your development period?</p>

---

## Post #3 by @nrex45 (2020-12-02 23:06 UTC)

<p>Hey James,</p>
<p>Thanks for the reply! My extension is a python based module. Thanks for highlighting the difference between needing to build an extension index and simply creating an extension.</p>
<p>I used the ExtensionWizard to create the basic code and mostly copied from a variety of other example extensions that had somewhat similar code to what I was trying to do. I’ve successfully downloaded the zipped folder from my github page and imported it. If my extension builds properly being imported through the ExtensionWizard is it reasonable to assume that it will “build properly” if the s4ext file works?</p>

---

## Post #4 by @jamesobutler (2020-12-03 00:27 UTC)

<p>I’ve honestly never tried installing an extension through the ExtensionsManager using the GitHub downloaded zip file. I typically always build the extension using a Slicer build tree which then creates the zip package.</p>
<p>It sounds like you’re following the extension development process well and doing the extension checklist. So I would suggest you go ahead and submit the PR to the slicer extensions index. I could try building it like how the factory build machine will do it, once you have that PR up and I can see where your extension is located.</p>

---

## Post #5 by @nrex45 (2020-12-06 21:41 UTC)

<p>Hey James,</p>
<p>I attempted to make a PR a few days ago, can you confirm that it went through? It’s very possible that I didn’t submit it properly.</p>

---

## Post #6 by @jamesobutler (2020-12-06 23:56 UTC)

<p>You submitted a PR to your fork’s master branch (<a href="https://github.com/naterex23/ExtensionsIndex/pull/1" rel="noopener nofollow ugc">https://github.com/naterex23/ExtensionsIndex/pull/1</a>) instead of the upstream (Slicer) repository (see <a href="https://github.com/Slicer/ExtensionsIndex/pulls" rel="noopener nofollow ugc">https://github.com/Slicer/ExtensionsIndex/pulls</a>).</p>

---

## Post #7 by @jamesobutler (2020-12-07 00:04 UTC)

<p>See this link <a href="https://github.com/Slicer/ExtensionsIndex/compare/master...naterex23:naterex23-patch-1" rel="noopener nofollow ugc">https://github.com/Slicer/ExtensionsIndex/compare/master...naterex23:naterex23-patch-1</a> which should show that the Base Repository is “Slicer/ExtensionsIndex” and the head repository “naterex23/ExtensionsIndex”.</p>

---

## Post #8 by @nrex45 (2020-12-07 00:37 UTC)

<p>I suspected this after I took a look at the PR today… thanks for confirming!</p>
<p>I’ll see if I can sort this out…</p>

---

## Post #9 by @jamesobutler (2020-12-07 01:55 UTC)

<p><a href="https://github.com/Slicer/ExtensionsIndex/pull/1750" rel="noopener nofollow ugc">https://github.com/Slicer/ExtensionsIndex/pull/1750</a> Is correct <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=9" title=":clap:" class="emoji" alt=":clap:">. Everyone struggles a bit to learn the GitHub upstream/fork workflows, but you’ll learn over time. The slicer developers will likely review your extension PR in the upcoming week or so and once merged then it will be distributed through the Slicer Extensions Manager, but until then others can manually build and install or specify the files as additional modules to load.</p>

---
