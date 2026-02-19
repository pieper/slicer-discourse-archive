---
topic_id: 2165
title: "No Load Loadable Modules Of An Extension After They Have Bee"
date: 2018-02-24
url: https://discourse.slicer.org/t/2165
---

# No load loadable modules of an extension after they have been installed from slicer extension catalog (Compiled Slicer 4.8.1 )

**Topic ID**: 2165
**Date**: 2018-02-24
**URL**: https://discourse.slicer.org/t/no-load-loadable-modules-of-an-extension-after-they-have-been-installed-from-slicer-extension-catalog-compiled-slicer-4-8-1/2165

---

## Post #1 by @carlos-luque (2018-02-24 12:48 UTC)

<p>Operating system: Windows 10 64 bits<br>
Slicer version: 4.8.1 (svn r26813)<br>
Compiler: Microsoft Visual Studio Community 2015<br>
Qt: 5.9.1</p>
<p>I’ve compiled the Slicer version 4.8.1 (svn 26813) without any errors and Slicer application works correctly. However if a extension is installed from Slicer extensions server, it is not showed in the menu “modules” and there are some errors:</p>
<ul>
<li>Qt: Failed to extract plugin meta data from (each loadable modules in the extension)</li>
</ul>
<p>On the other hand, If I compile the extension, and add the path in  “additional module path” in menu “modules”, all loadable modules of the extension are loaded.</p>
<p>I have some questions:</p>
<ul>
<li>If I’d like to add some new extensions (loadable modules) from the Slicer extension catalog in my compiled 3D Slicer, should I compile them?</li>
<li>If I’d like to use the install Slicer extension (extension server) in my compiled 3d Slicer, what environment should I set up? or is it impossible?</li>
</ul>
<p>Thanks in advance.<br>
Carlos Luque</p>

---

## Post #2 by @pieper (2018-02-24 19:56 UTC)

<p>Hi Carlos -</p>
<p>Right - for C++ shared libraries to be workable across builds you need to exactly match the compiler version and other settings <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory">described here</a> (VS 2013 instead of 2015).</p>
<p>If you are already building your own slicer and your own extensions probably you could just make your own installers that would be compatible.  Or you can submit your extension code and have it built on the factories so it would work with the slicer releases.</p>
<p>-Steve</p>

---

## Post #3 by @carlos-luque (2018-02-24 23:46 UTC)

<p>Hello Steve,</p>
<p>Thanks for your response.</p>
<p>I have a new doubt:</p>
<ul>
<li>If a new loadable module is designed, what Qt version should it support for the Slicer versions 4.8.1 and 4.9? Qt4 or Qt5 or both?</li>
</ul>
<p>Thanks in advance,<br>
Carlos Luque</p>

---

## Post #4 by @pieper (2018-02-25 00:07 UTC)

<p>Hi Carlos -</p>
<p>We’re in transition now - the current release 4.8.1 is still Qt4, but 4.9 (the nightly preview) and the upcoming 5.0 releases will use Qt5.  It’s possible to make your code work with both, but if you are starting development now I’d suggest only supporting Qt5.</p>
<p>Best,<br>
-Steve</p>

---

## Post #5 by @carlos-luque (2018-02-25 10:41 UTC)

<p>Hello Steve,</p>
<p>Thanks for your help. They’re useful for us.</p>
<p>Best,<br>
Carlos</p>

---
