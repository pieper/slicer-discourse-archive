# Windows: Unable to import DICOM files that are in a OneDrive-backed up folder

**Topic ID**: 36153
**Date**: 2024-05-14
**URL**: https://discourse.slicer.org/t/windows-unable-to-import-dicom-files-that-are-in-a-onedrive-backed-up-folder/36153

---

## Post #1 by @fedorov (2024-05-14 22:33 UTC)

<p>TL;DR: on Windows, do not use folders that are backed up by Microsoft OneDrive for DICOM images that you want to import into Slicer DICOMBrowser!</p>
<p><a class="mention" href="/u/vkt1414">@vkt1414</a> and I have been debugging an issue that we thought is a problem with our extension, but upon further investigation it turned out the issue was not in the extension. Logs showed that DCMTK failed to open the DICOM files our extension was downloading. Initially, I thought this is due to the presence of dots in the folder hierarchy, but <a class="mention" href="/u/pieper">@pieper</a> mentioned there were some recent OneDrive issues.</p>
<p>After that I discovered (since I do not use Windows very often) that OneDrive indeed was active on the computer where I did testing. Further, it had backup of my Desktop and Documents folders enabled, and that it was not possible to disable backup of those folders.</p>
<p>Upon disconnecting my computer from OneDrive, closing OneDrive, and moving my data folder to a different location, I was able to import the files without problems.</p>

---

## Post #2 by @pieper (2024-05-14 22:48 UTC)

<p>Thanks for the report <a class="mention" href="/u/fedorov">@fedorov</a>.</p>
<p>Have other windows users experienced this?  It’s odd that the files are visible to the indexer but not to the underlying dcmtk access method.  I wonder if a different windows-specific API is required.</p>
<p>This strikes me as a really bad regression in windows, since code since usually you can use code that’s decades old with no change in behavior.</p>

---

## Post #3 by @jamesobutler (2024-05-14 23:26 UTC)

<p>Were all the DICOM files being synced in the OneDrive location synced locally to disk (green) or were they actively trying to be download because it was just the cloud links?</p>
<p>Generally if I’m loading data such as NRRD into Slicer that only has the cloud link then it will begin downloading the file during the load process. This can result in the load process taking much longer than usual because it is downloading the source from the web first. The cloud only link is to allow saving local disk space while still being able to see all the files available in the cloud. Then it is download on demand when you try to open it.</p>

---

## Post #4 by @fedorov (2024-05-15 01:52 UTC)

<p>I just downloaded files using non-OneDrive means into a local folder that unbeknownst to me was synchronized by OneDrive. The most frustrating thing is that I didn’t even install OneDrive - either it is enabled by default when Windows is installed, or I checked some setting during install without thinking.</p>
<p>I can re-enable it and do some experiments later to nail down the details, if needed.</p>

---

## Post #5 by @cpinter (2024-05-15 07:57 UTC)

<p>I regularly import and use DICOM files synced by OneDrive (a business one but I don’t think it should matter), and haven’t had issues yet.</p>
<aside class="quote no-group" data-username="fedorov" data-post="1" data-topic="36153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Desktop and Documents folders enabled, and that it was not possible to disable backup of those folders</p>
</blockquote>
</aside>
<p>This is very strange. I don’t have those folders included in OneDrive sync (personal). It is something you can choose when first using it, and I find it very strange that you can’t opt out later.</p>
<p>The only thing that occurs to me is what <a class="mention" href="/u/jamesobutler">@jamesobutler</a> already described about the cloud-only file links. They start downloading when you first try to access them, and it works the same way for me with DICOM import. The only thing is that it is slower this way. There is a popup notification showing the progress when this happens.</p>

---

## Post #6 by @fedorov (2024-05-15 14:44 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="36153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>This is very strange.</p>
</blockquote>
</aside>
<p>I completely agree. I suspect that what might be happening is that the default setting on the sync is “remote only”, and as soon as the file is added to the folder, it is shoved to the cloud and does not exist locally for the purposes of Slicer readers.</p>
<p>I have not tested/investigated this - no time for now. But I know that this was the problem both for me and for <a class="mention" href="/u/vkt1414">@vkt1414</a>, so I thought I add this post as an alert in case it can help someone else. We spent at least several hours debugging this.</p>

---

## Post #7 by @pieper (2024-05-15 14:45 UTC)

<p>We saw something very similar with <a class="mention" href="/u/ron">@Ron</a> machine that I believe was due to dropbox not onedrive, but maybe it’s the same windows virtualizing method at the heart.</p>

---

## Post #8 by @jamesobutler (2024-05-15 17:08 UTC)

<p>Also something to be mindful of when OneDrive is set to “Back up important PC folders to OneDrive” that this results in new directories. So you will have 2 “Documents” locations that each have their own unique set of files.</p>
<ol>
<li>
<p>%USERPROFILE%\Documents (aka C:\Users\James\Documents)</p>
</li>
<li>
<p>C:\Users\James\OneDrive - OrgName\Documents</p>
</li>
</ol>
<p>1 is a local location while 2 is a location being synced to the cloud. The 2 location is what becomes linked to “Documents” in the quick access area on the left side of File Explorer.</p>

---

## Post #9 by @muratmaga (2024-05-15 17:15 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="36153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>OneDrive is set to “Back up important PC folders to OneDrive” that this results in new directories</p>
</blockquote>
</aside>
<p>At one point OneDrive also highjacked the user’s Desktop in the same way <a class="mention" href="/u/jamesobutler">@jamesobutler</a> described above. It throws all sorts of curveballs in terms of navigating files and performance. Cloud sync drives are often great, but for use with Slicer/SlicerMorph we advise against them, due to this path and performance issue.</p>

---
