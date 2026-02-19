---
topic_id: 14462
title: "Raw Image Guess Extension Wrong File Dialog"
date: 2020-11-06
url: https://discourse.slicer.org/t/14462
---

# Raw Image Guess extension wrong file dialog

**Topic ID**: 14462
**Date**: 2020-11-06
**URL**: https://discourse.slicer.org/t/raw-image-guess-extension-wrong-file-dialog/14462

---

## Post #1 by @giovform (2020-11-06 16:55 UTC)

<p>Hi, I am using the latest stable 3D Slicer (4.11.20200930), and found a bug in an extension named “Raw Image Guess”. The input file selector dialog opens as a “Save file” dialog, instead of a “Open file” one.</p>
<p>A possible fix is to add:</p>
<pre><code>self.ui.inputFileSelector.filters = ctk.ctkPathLineEdit.Files
</code></pre>
<p>I believe this bug was introduced recently, since this fix was also used in a module of my own, and appeared after updating to the newest stable 3D Slicer version.</p>

---

## Post #2 by @lassoan (2020-11-06 17:15 UTC)

<p>Thanks for reporting. This is a regression in Slicer-4.11.20209030 that was fixed in <a href="https://github.com/Slicer/Slicer/commit/9aa9ed8b8aa06704ece1f0caa50d46cd7825ea4a">https://github.com/Slicer/Slicer/commit/9aa9ed8b8aa06704ece1f0caa50d46cd7825ea4a</a>.</p>
<p>Unfortunately, Slicer Preview Release is not functional yet (<a href="https://discourse.slicer.org/t/no-images-shown-in-slice-viewers-in-latest-preview-release-slicer-4-13-0/13899/4" class="inline-onebox">No images shown in slice viewers in latest preview release (Slicer-4.13.0)</a>).</p>

---

## Post #3 by @muratmaga (2020-11-06 18:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> since this impacts more then just RawImageGuess, but other modules that use same dialog box, is possible to patch the current stable?</p>

---

## Post #4 by @lassoan (2020-11-06 18:11 UTC)

<p>Yes, we should either patch Slicer-4.11, build Slicer-4.13 with VTK8, or fix VTK9 to work with Slicer-4.13 - see discussion <a href="https://discourse.slicer.org/t/no-images-shown-in-slice-viewers-in-latest-preview-release-slicer-4-13-0/13899/7">here</a>.</p>

---
