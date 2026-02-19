---
topic_id: 8248
title: "Nightly 4 11 0 2019 8 30 Fails To Open On Some Windows Machi"
date: 2019-08-31
url: https://discourse.slicer.org/t/8248
---

# Nightly 4.11.0-2019-8-30 fails to open on some Windows machines

**Topic ID**: 8248
**Date**: 2019-08-31
**URL**: https://discourse.slicer.org/t/nightly-4-11-0-2019-8-30-fails-to-open-on-some-windows-machines/8248

---

## Post #1 by @mikebind (2019-08-31 14:13 UTC)

<p>Yesterday I downloaded the Windows nightly build to one laptop and had no problems getting it up and running. Today, I tried to do the same with another laptop and it appeared to install correctly (i.e. the launcher shortcut got created and I see the splash screen when I open it), but nothing ever happens after the splash screen disappears (i.e. no Slicer main window appears and I don’t see any kind of error message or anything).  Both laptops are running Windows 10 and have run earlier versions of Slicer without trouble.  I was switching to 4.11 to be able to use scipy.</p>
<p>One thing I noticed, the download file yesterday was titled Slicer-4.11.0-2019-08-30-win-amd64.exe.  Today, the download button today says “Built 2019-8-31”, but is named the same (Slicer-4.11.0-2019-08-30-win-amd64.exe).  I assumed that was just because there weren’t any new changes incorporated on 8-31. If that was the case, then I used the exact same installer file on each laptop.</p>
<p>Without an error message, I’m not sure how to provide more information. If there is a log file I should find and share, let me know.  Thanks.</p>

---

## Post #2 by @jamesobutler (2019-08-31 15:48 UTC)

<p>Recently there are pop ups when starting a new nightly about upgrading the Slicer Dicom Database. If there aren’t any dialogs being hidden behind other windows that you have open, then try deleting your Slicer Dicom Database directory which I believe is in the user documents location and restarting Slicer.</p>

---

## Post #3 by @cpinter (2019-08-31 23:04 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> I think this is not the problem, because the check does not happen at startup, but only when you try opening the DICOM browser.</p>
<p>Log files can be found at<br>
c:\Users[User]\AppData\Local\Temp\Slicer\</p>

---

## Post #4 by @jamesobutler (2019-09-01 00:34 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I could be wrong but I remember getting pop ups about upgrading the Dicom Database and I don’t remember going into the Dicom Browser. I actually never use it(but had an old one) so that’s why I thought it was weird when it popped up for me.</p>

---

## Post #5 by @lassoan (2019-09-01 03:04 UTC)

<p>This popup appears on startup (when you have a DICOM database created with Slicer-4.10), without switching to DICOM module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4f36f2310c5924a3f571cea8f774e80194d8b97.png" data-download-href="/uploads/short-url/yWW3AYfBSzKjJOCHj0WvR5mMrtB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4f36f2310c5924a3f571cea8f774e80194d8b97.png" alt="image" data-base62-sha1="yWW3AYfBSzKjJOCHj0WvR5mMrtB" width="690" height="175" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1002×255 13.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> Is this an issue? Also, I think your most recent improvements (that allows selection of different database folder for different Slicer versions) are not yet available in current Slicer Preview Release.</p>

---

## Post #6 by @mikebind (2019-09-01 15:17 UTC)

<p>Yes, I got this popup the first time and chose to create a new empty database in a new folder. After doing so, I moved on to other tasks for a few minutes, then noticed that Slicer had never opened.  When I tried launching it again I saw the splash screen, was not prompted to do anything about the dicom database, and again nothing happened after the splash screen disappeared.</p>

---
