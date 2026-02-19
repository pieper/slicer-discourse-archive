---
topic_id: 43435
title: "This Is About Extension To Upload To Extension Manager"
date: 2025-06-20
url: https://discourse.slicer.org/t/43435
---

# This is about extension to upload to extension manager

**Topic ID**: 43435
**Date**: 2025-06-20
**URL**: https://discourse.slicer.org/t/this-is-about-extension-to-upload-to-extension-manager/43435

---

## Post #1 by @Pranav_Rai (2025-06-20 14:47 UTC)

<p>I am trying to create extensions for my custom slicer application by running the command given in the docs. Still, after running it and setting everything in place, the final folder comes empty every time, and the solutions that is available online is not working. So help fix this issue forefront.</p>

---

## Post #2 by @muratmaga (2025-06-20 23:00 UTC)

<aside class="quote no-group" data-username="Pranav_Rai" data-post="1" data-topic="43435">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pranav_rai/48/80279_2.png" class="avatar"> Pranav_Rai:</div>
<blockquote>
<p>by running the command given in the docs.</p>
</blockquote>
</aside>
<p>You need to be more specific than that. Which commands, whats the output?</p>

---

## Post #3 by @Pranav_Rai (2025-06-23 10:04 UTC)

<p>this command I have used :<br>
cd /d C:\D\ExtensionsIndexR</p>
<p>“c:\Program Files\CMake\bin\cmake.exe” -DSlicer_DIR:PATH=C:/D/SR/Slicer-build ^<br>
-DSlicer_EXTENSION_DESCRIPTION_DIR:PATH=C:/D/ExtensionsIndex ^<br>
-DCMAKE_BUILD_TYPE:STRING=Release ^<br>
C:/D/S/Extensions/CMake</p>
<p>“c:\Program Files\CMake\bin\cmake.exe” --build . --config Release</p>
<p>and the build folder for the extension is coming empty everytime</p>

---
