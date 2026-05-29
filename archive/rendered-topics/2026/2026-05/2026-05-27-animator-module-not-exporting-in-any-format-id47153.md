---
topic_id: 47153
title: "Animator module not exporting in any format"
date: 2026-05-27
url: https://discourse.slicer.org/t/47153
last_bumped: 2026-05-28T16:41:54.646Z
---

# Animator module not exporting in any format

**Topic ID**: 47153
**Date**: 2026-05-27
**URL**: https://discourse.slicer.org/t/animator-module-not-exporting-in-any-format/47153

---

## Post #1 by @Atticus (2026-05-27 15:01 UTC)

<p>I have used the Animator module in the past to produce short animations of volumes rotating, being cropped to ROIs or changing their colors.</p>
<p>I have not been able to export animations today, in any format or resolution, of the same type of animations. The rendering process seems to reach the end of the animation time (either 3 or 5 seconds) and then the render window remains open and nothing happens afterwards. I have tried reinstalling Slicermorph, saving as different file types, saving low res versions and nothing.</p>
<p>Currently running 3DSlicer 5.10.0, Slicermorph updated, on Win11 with RTX 4070</p>
<p>Any advise?</p>

---

## Post #2 by @pieper (2026-05-27 15:52 UTC)

<p>Can you look in the error log (under the Help menu, Report a Bug dialog) to see if there are any messages when the animation stops.  Also look in the python console for any messages.</p>

---

## Post #3 by @muratmaga (2026-05-27 16:13 UTC)

<p>There hasn’t been any change to the Animator in the stable branch for last three years. Given your description, I suspect your system is having a hard time locating the ffmpeg library to do the conversion to mp4.</p>
<p>Have you changed your computer? If so, you need to install ffmpeg. It is an external library needed to create the mp4s.</p>

---

## Post #4 by @Atticus (2026-05-28 14:19 UTC)

<p>I have now checked the error log (thanks pieper) and from what I can understand it seems to be what muratmaga indicated regarding the ffmpeg. This is the error I see in the log, regardless of the resolution and format I am trying to save:</p>
<p>"[INFO][Python] 27.05.2026 16:53:38 [Python] (C:\Users\attic\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\ScreenCapture.py:856) - Export to video…</p>
<p>[CRITICAL][Stream] 27.05.2026 16:53:38 [] (unknown:0) - Traceback (most recent call last):</p>
<p>[CRITICAL][Stream] 27.05.2026 16:53:38 [] (unknown:0) - File “C:/Users/attic/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/SlicerMorph/lib/Slicer-5.10/qt-scripted-modules/Animator.py”, line 948, in onExport</p>
<p>[CRITICAL][Stream] 27.05.2026 16:53:38 [] (unknown:0) - logic.createVideo(</p>
<p>[CRITICAL][Stream] 27.05.2026 16:53:38 [] (unknown:0) - File “C:\Users\attic\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\ScreenCapture.py”, line 1432, in createVideo</p>
<p>[CRITICAL][Stream] 27.05.2026 16:53:38 [] (unknown:0) - raise ValueError(_(“Video creation failed: ffmpeg executable path is invalid: {path}”).format(filepath=ffmpegPath))</p>
<p>[CRITICAL][Stream] 27.05.2026 16:53:38 [] (unknown:0) -"</p>
<p>I have not changed computer nor installations of 3DSlicer. I tried reinstalling ffmpeg but it does not seem to have changed anything, same error comes up.</p>

---

## Post #5 by @muratmaga (2026-05-28 14:30 UTC)

<p>Error is very clear: ffmpeg path is invalid. Try downloading and unzipping somewhere else, maybe like your desktop or documents folder.</p>

---

## Post #6 by @Atticus (2026-05-28 14:58 UTC)

<p>I reinstalled ffmpeg in the Documents folder and still did not work. I had to specify the new path in the “Screen Capture” module, and then the Animator export did work.</p>
<p>Thanks for the advise!</p>

---

## Post #7 by @muratmaga (2026-05-28 16:41 UTC)

<p>Sorry, yes you have to specify where you install in the Screen Capture glad that you figured it out.</p>

---
