---
topic_id: 43320
title: "Slicer Wont Create A New Database If The Path Contains A Spa"
date: 2025-06-11
url: https://discourse.slicer.org/t/43320
---

# Slicer won't create a new database if the path contains a space

**Topic ID**: 43320
**Date**: 2025-06-11
**URL**: https://discourse.slicer.org/t/slicer-wont-create-a-new-database-if-the-path-contains-a-space/43320

---

## Post #1 by @sconrad (2025-06-11 15:59 UTC)

<p>When trying to create a DB in which the path contains a folder with a space in the name results in an error message: "Failed to create new database in folder “C:\Users\Folder with space\SlicerDICOMDatabase”. Changing the path in which all folders have no space is successful.</p>
<p>Also, if the database is created elsewhere and moved into the folder, it fails to import DICOM files.</p>

---

## Post #2 by @muratmaga (2025-06-11 16:37 UTC)

<p>You might want to report this on the Slicer repo (<a href="https://github.com/Slicer/Slicer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a>)</p>
<p>but in general it is always a good practice not to have space in folder or file names to avoid these issues.</p>

---

## Post #3 by @pieper (2025-06-11 20:54 UTC)

<p>I just tried on mac with space in database name path and also a space in the data path and both worked fine.  Maybe others can try on other platforms?  It should be the same everywhere.</p>
<p>Note also the database contains absolute paths to the files.  It works for me to move the database to a path with spaces.</p>

---

## Post #4 by @sconrad (2025-06-11 21:55 UTC)

<p>Thanks for the tip. I’ll report it on the repo.</p>
<p>Microsoft Windows set up my local account on one of my workstations to be my full name with a space in it. When I use One Drive on that computer is when the problem occurs. I am planning to migrate my account to a new account having a name without a space.</p>
<p>As to you point out on best practice of having no spaces, I agree that it has been a custom since it was a requirement of past OS versions (I’ve been writing code since 1969). But in modern OS versions spaces are quite common and the software would ideally be able to handle them.</p>
<p>I appreciate your time and input.</p>
<p>Steven Conrad, MD PhD</p>

---

## Post #5 by @pieper (2025-06-11 22:36 UTC)

<p>There have been other problems reported for OneDrive (e.g. <a href="https://discourse.slicer.org/t/windows-unable-to-import-dicom-files-that-are-in-a-onedrive-backed-up-folder/36153" class="inline-onebox">Windows: Unable to import DICOM files that are in a OneDrive-backed up folder</a>).  Best to use a local drive and if needed copy to OneDrive with the OS.</p>

---

## Post #6 by @jamesobutler (2025-06-12 00:06 UTC)

<p><a class="mention" href="/u/sconrad">@sconrad</a> I am running Windows 11 23H2 and was successful creating a new DICOM database in a path that contains a space.</p>
<ol>
<li>I launched Slicer 5.8.1</li>
<li>I went to Edit-&gt;Application Settings</li>
<li>Selected the “DICOM” left side panel in settings</li>
<li>Clicked the “Database location” button and chose a new directory at “C:/My Folder With A Space”</li>
<li>I restarted Slicer 5.8.1.</li>
<li>I went into the DICOM module and imported a new DICOM file and successfully loaded it into the Slicer scene.</li>
</ol>
<p>What version of Slicer and specific steps did you observe when it failed? Were you upgrading the Slicer DICOM database or creating a brand new empty one?</p>

---

## Post #7 by @sconrad (2025-06-12 01:10 UTC)

<p>I’m using 5.8.1. My error occurred on Windows 10 while attempting to use a synchronized OneDrive folder for the database and/or the DICOM import directory. Given the previous replies that OneDrive may be the culprit, or possibly Windows 10, I installed Slicer on a Windows 11 workstation and was able to successfully create a database and import files from directories containing spaces on OneDrive. Tomorrow I will test the Windows 10 machine again on a non-OneDrive folder and determine if it is OneDrive on Windows 10, or some issue with my installation with Windows 10 itself.</p>
<p>Thanks for the replies, and I’ll report what i find tomorrow.</p>

---

## Post #8 by @muratmaga (2025-06-12 04:45 UTC)

<aside class="quote no-group" data-username="sconrad" data-post="7" data-topic="43320">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ed8c4c/48.png" class="avatar"> sconrad:</div>
<blockquote>
<p>OneDrive folder for the database and/or the DICOM import directory.</p>
</blockquote>
</aside>
<p>Most likely culprit.</p>
<aside class="quote no-group" data-username="sconrad" data-post="4" data-topic="43320">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ed8c4c/48.png" class="avatar"> sconrad:</div>
<blockquote>
<p>But in modern OS versions spaces are quite common and the software would ideally be able to handle them.</p>
</blockquote>
</aside>
<p>The issue is not just the OS, but every part of the software chain needs to handle this. I complex program like Slicer is like a layered cake, consisting of hundreds of libraries across three major operating systems and their versions. It only takes one combination of option not to support this for things to break.</p>
<p>For example in my field, my colleagues have a tendency use the full genetic knockout nomenclature as a file name to identify a sample. Unfortunately, <a href="https://www.informatics.jax.org/mgihome/nomen/gene.shtml#navsma" rel="noopener nofollow ugc">nomenclature  contains  special characters like !, *, (), / and others</a>. While it is possible to use to create filenames like that in modern operating systems (with use of proper escape characters of double quotes), whether they will be handled correctly within Slicer is a complete different story.</p>

---

## Post #9 by @lassoan (2025-06-13 00:52 UTC)

<p>Please use latest Slicer Stable Release (currently 5.8.1). It should have no problem with spaces in paths. Have you set the folder name using the GUI (or you set it via command-line arguments or by modifying Slicer.ini file, …)? Is the folder writeable?</p>
<p>The DICOM database folder is created by SQLite database. It relies on sophisticated file locking APIs to ensure database integrity when multiple applications perform concurrent read/write operations. Virtual file systems (such as mapped network drives, Google drive, OneDrive, etc.) may not be able to fully emulate these complex file locking behaviors (some features are not implemented, some may not work reliably, and some cannot be implemented due to inherent speed and reliability limitations of network communication). Therefore, I would recommend to use local file system for DICOM database index storage, especially while you are building the database. If you want to share data between several users or need to process huge amount of data on your computer and you don’t have space for local storage then there are many solutions for these in Slicer, but that would be a separate discussion.</p>
<p>Special characters can be a problem on Windows, for operations that require passing paths via command-line arguments (such as DICOM export), depending on what code page is set in your system. There is a <a href="https://github.com/commontk/AppLauncher/pull/127">fix that should take care of the last special-characters-related problem that we know of</a>, it just has not been merged yet.</p>

---

## Post #10 by @sconrad (2025-06-16 03:27 UTC)

<p>I have determined that the issue seems to be related to using OneDrive on Windows 10. I was able to use paths with spaces on a local drive, but not on a locally-synchronized OneDrive folder. Since my user name had a space, my only option is to create a new account without a space in the user name.</p>
<p>On a different workstation with Windows 11, I was able to use paths with spaces on my OneDrive folder.</p>
<p>Thanks for all of the support, and apologies for any delays in replying to this thread.</p>

---
