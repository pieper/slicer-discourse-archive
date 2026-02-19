---
topic_id: 37832
title: "How To Run A Built Slicer Loadable Module On A Released Slic"
date: 2024-08-11
url: https://discourse.slicer.org/t/37832
---

# How to Run a Built Slicer Loadable Module on a Released Slicer Version

**Topic ID**: 37832
**Date**: 2024-08-11
**URL**: https://discourse.slicer.org/t/how-to-run-a-built-slicer-loadable-module-on-a-released-slicer-version/37832

---

## Post #1 by @park (2024-08-11 15:17 UTC)

<p>Hello,</p>
<p>I am currently developing a loadable module for 3D Slicer and have successfully built the module. I have also tested running the module within the built version of Slicer.</p>
<p>One thing I am curious about is how to run the built module on a released version of Slicer, such as the .exe or .dmg versions. Could you provide guidance on how to achieve this?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2024-08-11 21:31 UTC)

<p>If you’ve added the module to the Slicer build system, you can just run <code>make package</code> (or build the Windows PACKAGE target).</p>

---

## Post #3 by @park (2024-08-12 13:32 UTC)

<p>Thank you for the response, Steve.</p>
<p>So, after creating the package, do we just place the .dll files in the Extensions-### folder? Our ultimate goal is to make our module easy to install, similar to how an extension manager works.</p>

---

## Post #4 by @pieper (2024-08-12 14:03 UTC)

<p>You can bundle loadable modules in the build tree just by adding them in cmake like the other built-in ones.  This will automatically make them part of the packaging process so you don’t need to have them as extensions.</p>

---

## Post #5 by @park (2024-08-12 14:17 UTC)

<p>I apologize for the lack of clarity in my previous explanation.</p>
<p><strong>What I’m looking for is a way to load a custom loadable module into the “Release” Slicer provided on the “Slicer website”.</strong></p>
<p>Through this, we believe that only those developing loadable modules would need to build Slicer, while those using scripted modules could simply use the released version of Slicer. This would allow for more efficient management of the development environment.</p>

---

## Post #6 by @pieper (2024-08-12 15:00 UTC)

<p>In theory you can build Slicer modules using exactly the same compiler versions and flags so that your locally-built dlls will load in the release of Slicer from the download site, but in practice this is pretty difficult, so it’s better to make a build that has both the core Slicer and your C++ code.</p>

---

## Post #7 by @park (2024-08-12 15:03 UTC)

<p>Then, how do we install a loadable module from the Extension Manager?</p>

---

## Post #8 by @pieper (2024-08-12 15:08 UTC)

<p>Well, you could also build the extension, package it, and install from the file.  This would allow you to update the extension without rebuilding the base Slicer.  Or if you add your modules to Slicer’s modules/loadable directory and cmake files it would build and package up as one unit.</p>

---

## Post #9 by @park (2024-08-13 12:12 UTC)

<p>Following your advice, I successfully loaded the module.<br>
Thank you as always, Steve.</p>

---
