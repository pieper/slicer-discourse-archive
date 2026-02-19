---
topic_id: 5653
title: "Detecting And Loading Loadable Modules"
date: 2019-02-05
url: https://discourse.slicer.org/t/5653
---

# Detecting and loading Loadable modules

**Topic ID**: 5653
**Date**: 2019-02-05
**URL**: https://discourse.slicer.org/t/detecting-and-loading-loadable-modules/5653

---

## Post #1 by @Amn3s14 (2019-02-05 22:19 UTC)

<p>Hello, I have written a custom C++ loadable module in Slicer, and it works fine when I run it on my built version of Slicer. However, when I try to run it on a standard version of Slicer, it does not load my module, it appears greyed out in the Module list in Application Settings. Does this guide still apply for Slicer4:</p>
<p><a href="https://www.slicer.org/wiki/Slicer3:Loadable_Modules:HOWTO" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Slicer3:Loadable_Modules:HOWTO</a></p>
<p>If so, would it be possible to link a module that has implemented the required changes. I do not see these changes in the CropVolume module for example.</p>

---

## Post #2 by @cpinter (2019-02-05 22:26 UTC)

<p>The page you linked belongs to Slicer version 3, which is a completely different architecture. Please confirm you’re using Slicer 4.</p>
<p>However in general if you build something locally, it is basically impossible to expect that the configuration of your build environment (Qt version, etc.) will be exactly the same as in the factory machine.</p>
<p>The best way to use your module with factory-built Slicer is to publish it as an extension and install it from Extension Manager after the factory machine built it against the factory Slicer.</p>

---

## Post #3 by @Amn3s14 (2019-02-05 22:57 UTC)

<p>Yes I am using Slicer 4. I posted that link to see if there was a newer version I could follow. I think I understand what you’re saying. I bundled my module into an extension, built the extension, but I do not have a PACKAGE target. Did I do something wrong?</p>

---

## Post #4 by @cpinter (2019-02-05 23:15 UTC)

<p>This is the main developer wiki page that points to all the how-tos:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers</a></p>
<p>A few of them that are related to the one you linked before:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module</a><br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Module" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Module</a><br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Extension" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Extension</a></p>
<p>As for the missing package target, I’m not sure. If your extension is not a superbuild extension, then it should be in the Extension.sln solution, or available for make if you use Mac (which in this case will be “make package” - lower case).</p>

---

## Post #5 by @Amn3s14 (2019-02-05 23:52 UTC)

<p>Thank you, I had accidentally selected superbuild when I initially made the extension. I fixed that, built the PACKAGE target, installed the zip from the Extension Manager, but my module is still greyed out. Any advice?</p>

---

## Post #6 by @cpinter (2019-02-05 23:57 UTC)

<p>Please see what I wrote above:</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="5653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>However in general if you build something locally, it is basically impossible to expect that the configuration of your build environment (Qt version, etc.) will be exactly the same as in the factory machine.</p>
<p>The best way to use your module with factory-built Slicer is to publish it as an extension and install it from Extension Manager after the factory machine built it against the factory Slicer.</p>
</blockquote>
</aside>

---

## Post #7 by @Amn3s14 (2019-02-07 04:41 UTC)

<p>Thank you for your patience. I understand what you mean now. When I try to publish using the following command from my slicer-build directory:</p>
<p><code>bin/slicerExtensionWizard --publish ~/MyExtension</code></p>
<p>I receive the following output:</p>
<pre><code>bin/slicerExtensionWizard: line 4: declare: `APPLAUNCHER_0_CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files': not a valid identifier
bin/slicerExtensionWizard: line 4: declare: `APPLAUNCHER_0_ProgramFiles(x86)=C:\Program Files (x86)': not a valid identifier
bin/slicerExtensionWizard: line 4: declare: `APPLAUNCHER_0_asl.log=Destination=file': not a valid identifier
Creating initial commit containing the following files:
</code></pre>
<p>And then it lists all the right files, but Git Bash seems to hang forever. Are those errors preventing the publishing?</p>

---

## Post #8 by @cpinter (2019-02-07 14:35 UTC)

<p>Publishing an extension consists of submtting the s4ext file to the ExtensionIndex repository. That way when the factory build machine parses the extensions it will find yours and build that one as well.</p>
<p>Here’s the guide:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions</a></p>
<p>Let us know if something is not straightforward or if some parts of the wiki page are outdated. Thanks!</p>

---
