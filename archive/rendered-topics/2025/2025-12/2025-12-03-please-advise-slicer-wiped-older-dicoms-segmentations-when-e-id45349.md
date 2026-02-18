# Please advise - Slicer wiped older dicoms/segmentations when editing other files 

**Topic ID**: 45349
**Date**: 2025-12-03
**URL**: https://discourse.slicer.org/t/please-advise-slicer-wiped-older-dicoms-segmentations-when-editing-other-files/45349

---

## Post #1 by @Sus_Mu (2025-12-03 13:36 UTC)

<p>I am working on a project with batches of segmentations.</p>
<p>Batch A (prepared in October) and Batch B (prepared in November) were saved on my computer, without meaningful backup through TimeMachine or iCloud. I also have a Batch C (prepared in October) and Batch D and E (prepared in April).</p>
<p>I went back to Batch A and made some small edits, saving as normal. However, I realized once I did this, that Slicer had deleted the dicoms and segmentations of Batch B, as well as batch D completely off my desktop, without a trace. There are complete subfolders which went missing out of folders because they were from Batch A. They are not in my trash, nor can I find them when using applications like Data Drill. Other folders, from Batch A and C were not affected.</p>
<p>Furthermore, when I open Slicer, it states that there is no longer a database file in the location that it expects, and recommends to create a new one. In the folder, there are two files (ctkDICOM.sql and ctkDICOMTagCache.sql), but as I understand, these cannot recover segmentation files.</p>
<p>This has never happened to me before when I went back to edit older files, and I don’t understand why suddenly this happened.</p>
<p>Can you please help me understand a few things:</p>
<ol>
<li>Are there files completely uncoverable?</li>
<li>Why did this happen?</li>
<li>How can I prevent this in the future?</li>
</ol>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2025-12-03 13:43 UTC)

<p>Slicer very rarely if ever removes any file from the user’s computer. It removes only temporary files that it created. It would never delete the ctkDICOM.sql file. Most likely the operating system deleted the files or they disappeared due to some other errors.</p>
<p>Maybe you saved data in temporary folders? macOS automatically wipes temporary folders after some time or when you are running low of free disk space. Do you still have the full path of the ctkDICOM.sql file that disappeared?</p>

---

## Post #3 by @Sus_Mu (2025-12-04 20:29 UTC)

<p>Hello,</p>
<p>Thank you very much for your quick response.</p>
<p>To clarify - the ctkDICOM.sql file is still present, but the .dcm and the .nrrd and the .mrml are all wiped from my computer. This is not an issue with disk space, as I have 200GB free.</p>
<p>Best,<br>
Susie</p>

---

## Post #4 by @pieper (2025-12-05 00:05 UTC)

<aside class="quote no-group" data-username="Sus_Mu" data-post="1" data-topic="45349">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sus_mu/48/81483_2.png" class="avatar"> Sus_Mu:</div>
<blockquote>
<p>Slicer had deleted the dicoms and segmentations of Batch B, as well as batch D completely off my desktop</p>
</blockquote>
</aside>
<p>This sounds very unfortunate, but as Andras said, this is very unlikely to have been done by Slicer.    There is really no code that goes through and deletes files from your disk.</p>
<p>Are you using a mac?  Sometimes if you save files to an iCloud drive, the files will “disappear” but are still on the iCloud and just need to be recalled to your local machine.  This “feature” is fairly annoying and recent, but you can control it via the mac settings.  I understand OneDrive on windows can do similar things, and newer Dropbox versions probably do as well on both platforms.</p>

---
