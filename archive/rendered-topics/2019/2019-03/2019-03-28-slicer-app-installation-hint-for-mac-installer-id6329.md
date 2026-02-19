---
topic_id: 6329
title: "Slicer App Installation Hint For Mac Installer"
date: 2019-03-28
url: https://discourse.slicer.org/t/6329
---

# Slicer app installation "hint" for mac installer

**Topic ID**: 6329
**Date**: 2019-03-28
**URL**: https://discourse.slicer.org/t/slicer-app-installation-hint-for-mac-installer/6329

---

## Post #1 by @fedorov (2019-03-28 16:31 UTC)

<p>Based on the experience communicating with users, it comes up not for the first time that some users open the installer package, and then open 3D Slicer app from the package, without doing the proper install. Surprisingly or not, the app opens just fine, and they may not run into problems until they need write access (e.g., while installing extensions).</p>
<p>Does anyone know if it would be easy to add a “hint” to the package guiding the users to drag the application into the Apps folder, like they do for many mac packages (one example below)?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c80883a1ea2a1052cda3c9332b6001c49bc00234.png" alt="image" data-base62-sha1="sxzJBRwjHKtHBobHN89styc2vxa" width="396" height="488"></p>
<p>If that is difficult, maybe there should be a check on startup for being able to write to the Extensions folder, and if not possible, alert the user right away?</p>

---

## Post #2 by @fedorov (2019-03-28 16:42 UTC)

<p>Most recent motivating example is here: <a href="https://github.com/QIICR/lidc2dicom/issues/4#issuecomment-477665457" rel="nofollow noopener">https://github.com/QIICR/lidc2dicom/issues/4#issuecomment-477665457</a></p>

---

## Post #3 by @spujol (2019-03-28 17:03 UTC)

<p>The Slicer Quick Start Guide tutorial describes the installation steps:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Quick_Start_Guide" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Training#Quick_Start_Guide</a></p>
<p>An additional ‘hint’ would be great.</p>

---

## Post #4 by @pieper (2019-03-28 18:47 UTC)

<p>A hint would be nice, but actually we could also include a check at start up that offers to copy Slicer into the /Applications directory.  In fact, while we’re at it we could offer to copy with the version/date appended (I always end up renaming Slicer.app to Slicer-4.10.1.app or Slicer-2019-03-28.app or whatever and it would be nice to automate that).</p>

---

## Post #5 by @fedorov (2019-03-28 19:05 UTC)

<p>Yes, that would be nice too. But then this would introduce differences in the install procedure and the result between drag-and-drop to Apps and install from the Slicer app.</p>
<p>The good thing about the “hint” is that it is something users are already familiar with, and a practice adopted in many, if not most, application packages.</p>

---

## Post #6 by @pieper (2019-03-28 20:00 UTC)

<p>The place where the hint would be really valuable is when you open the extension manager.  I find myself trying to install extensions on read-only Slicers and it always catches me off guard.</p>

---
