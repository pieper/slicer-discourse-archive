---
topic_id: 46506
title: "Publishing A New Slicer Python Extension"
date: 2026-03-19
url: https://discourse.slicer.org/t/46506
---

# Publishing a new Slicer Python extension

**Topic ID**: 46506
**Date**: 2026-03-19
**URL**: https://discourse.slicer.org/t/publishing-a-new-slicer-python-extension/46506

---

## Post #1 by @MaxHoges (2026-03-19 18:49 UTC)

<p>Hi all,</p>
<p>I’ve been developing a Slicer extension in Python over the past 6 months to perform material mapping of Young’s modulus onto meshes from CT data, using Dr Elise Pegg’s project to perform the main material mapping, which copies BoneMat’s methods (her repo: <a href="https://github.com/elisepegg/py_bonemat_abaqus/tree/master" class="inline-onebox" rel="noopener nofollow ugc">GitHub - elisepegg/py_bonemat_abaqus: Assign material properties of bone to a finite element mesh · GitHub</a> ). I started this whole project using the extension skeleton provided by the Extension Wizard, and I’ve been doing all my UI and functionality testing by adding it as an additional module to my local Slicer installation and going from there.</p>
<p>I’m almost done on the development side, and I’m looking to make it available for everyone to use soon. I’ve looked through the docs on publishing an extension (i.e. this page: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a> ) but I’m still slightly confused.</p>
<p>As far as I understand it, all I need to do is to fork the ExtensionsIndex repo, upload the proper JSON file and then submit a proper pull request. I just have some questions around testing. I’ve obviously done my own independent testing, but I haven’t written any tests in a class which inherits the ScriptedLoadableModuleTest class. Do I need to write those tests before submitting the extension?</p>
<p>Also, how does the Slicer testing dashboard work? Does my extension automatically get uploaded/tested there once my ExtensionsIndex pull request gets approved? Or do I need to upload it there myself and make sure everything passes/build correctly before it can be approved?</p>
<p>Finally, with the ‘tier’ system of requirements for these extensions, do I get to decide whether I want my extension to be a tier 1/3/5 extension? Does it just depend on what kind of commitment I want to make to maintaining it for users and future slicer versions?</p>
<p>Thanks in advance for any advice, I appreciate it.</p>

---

## Post #2 by @pieper (2026-03-19 21:19 UTC)

<aside class="quote no-group" data-username="MaxHoges" data-post="1" data-topic="46506">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a88e4f/48.png" class="avatar"> MaxHoges:</div>
<blockquote>
<p>As far as I understand it, all I need to do is to fork the ExtensionsIndex repo, upload the proper JSON file and then submit a proper pull request.</p>
</blockquote>
</aside>
<p>Yes, that’s right.</p>
<aside class="quote no-group" data-username="MaxHoges" data-post="1" data-topic="46506">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a88e4f/48.png" class="avatar"> MaxHoges:</div>
<blockquote>
<p>I haven’t written any tests in a class which inherits the ScriptedLoadableModuleTest class. Do I need to write those tests before submitting the extension?</p>
</blockquote>
</aside>
<p>It’s considered good practice to have tests and to check that they are working.  Once your extension is in the nightly build it will be tested each night on both the stable release and on the preview build on all three supported platforms.  It’s a good way for you to have confidence that the code will work well for users.</p>
<aside class="quote no-group" data-username="MaxHoges" data-post="1" data-topic="46506">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a88e4f/48.png" class="avatar"> MaxHoges:</div>
<blockquote>
<p>do I get to decide whether I want my extension to be a tier 1/3/5 extension?</p>
</blockquote>
</aside>
<p>Yes, you can propose a tier as part of your PR.  If you want to be in a higher tier you need to make sure you meet all the checkbox items for that tier.</p>
<aside class="quote no-group" data-username="MaxHoges" data-post="1" data-topic="46506">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a88e4f/48.png" class="avatar"> MaxHoges:</div>
<blockquote>
<p>Does it just depend on what kind of commitment I want to make to maintaining it for users and future slicer versions?</p>
</blockquote>
</aside>
<p>This is an important point.  Even tier.1 extensions should really only be submitted if you are going to make a reasonable effort to respond to questions and maybe do simple fixes.  If you just want to use the code yourself or you don’t want to make any commitments then it may be better to just provide installation instructions on a github page with a disclaimer that the code is not being actively maintatined.  If your code is all in python and you don’t have any tests then the whole nightly factory process isn’t doing anything except making it show up in the extension dialog box.</p>

---
