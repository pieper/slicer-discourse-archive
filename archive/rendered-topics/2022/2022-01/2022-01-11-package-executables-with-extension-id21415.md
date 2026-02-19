---
topic_id: 21415
title: "Package Executables With Extension"
date: 2022-01-11
url: https://discourse.slicer.org/t/21415
---

# Package executables with extension

**Topic ID**: 21415
**Date**: 2022-01-11
**URL**: https://discourse.slicer.org/t/package-executables-with-extension/21415

---

## Post #1 by @brandus1 (2022-01-11 19:25 UTC)

<p>Hello,</p>
<p>I am building an extension and I need to package with it a couple of executables which I want to call as subprocesses from a scripted python module.</p>
<p>This seems the quickest solution for me, avoiding complex building issues.</p>
<p>I have been researching for the last weeks on how to do this but I haven’t found a solution yet.</p>
<p>I already have a slicer superbuild to build the extension.</p>
<p>Any help would be super appreciated, thanks.</p>

---

## Post #2 by @pieper (2022-01-11 23:57 UTC)

<p>If you are building these executables from source then it’s good to build them as part of the extension build.  If they are just binaries you got from somewhere you can put them in the Resources folder and install them like you would jpg or something.  Be sure to check the platform and warn the user if you don’t have binaries for their machine.</p>

---

## Post #3 by @brandus1 (2022-01-17 11:44 UTC)

<p>Works, thank you very much!<br>
A little bit trickier to copy directories though, but feasible</p>

---
