---
topic_id: 38464
title: "Trouble Saving Fcsv File As Part Of Scene"
date: 2024-09-20
url: https://discourse.slicer.org/t/38464
---

# Trouble saving .fcsv file as part of scene

**Topic ID**: 38464
**Date**: 2024-09-20
**URL**: https://discourse.slicer.org/t/trouble-saving-fcsv-file-as-part-of-scene/38464

---

## Post #1 by @psychicpotato (2024-09-20 20:54 UTC)

<p>Hey all,</p>
<p>We’re currently experimenting with liver resection extensions in 3dSlicer, and have had some great progress using the <a href="https://github.com/ALive-research" rel="noopener nofollow ugc">SlicerLiver extension from the ALive group</a>.</p>
<p>A problem I’m having is saving scenes after setting up a resection plane - I believe the resection data is saved as a .fcsv file, and when I attempt to save the scene I have the follow message:</p>
<p>bool __cdecl qSlicerCoreIOManager::saveNodes(class QString,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLMessageCollection *,class vtkMRMLScene *) error: No writer found to write file “C:/Users/tvasurg001/Desktop/testAI/cases/081-090/081_7341961/test/LiverResection.fcsv” of type “LiverResectionFile”<br>
void __cdecl</p>
<p>qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save error: “Error: Cannot write data file: C:/Users/tvasurg001/Desktop/testAI/cases/081-090/081_7341961/test/LiverResection.fcsv.\n”</p>
<p>I’m trying to troubleshoot in finding a ‘writer’ for .fcsv file - is there an extension I should be importing to make this work?</p>
<p>This is with 3Dslicer 5.6.2, on a Windows 10 machine.</p>
<p>Thanks all!<br>
A</p>

---

## Post #2 by @lassoan (2024-09-20 20:55 UTC)

<p>You can only save point list as fcsv. You can save all markups as json.</p>

---

## Post #3 by @psychicpotato (2024-09-23 11:38 UTC)

<p>Thanks so much Andras. I’m just wondering if there’s anything I need for the fcsv saving to happen - the error message seems to suggest that I don’t have the appropriate ‘writer’ to write the file…</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2024-09-23 13:10 UTC)

<p>FCSV file format is a simple table-based, which cannot save the more complex data structures used by more recent markup nodes. If you are only interested in control point positions then you can export the control point coordinates to a table and save those in CSV format. Or you can create a new writer in Python that can save any data in any format you need.</p>
<p>What is your overall goal?</p>

---

## Post #5 by @psychicpotato (2024-09-23 13:14 UTC)

<p>Thanks Andras - sorry for being unclear, but I think all I’m aiming for is just to save the scene w/o errors <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
<p>The situation at the moment is the fcsv file can’t be saved, and as a result I can’t save the resection plane to the scene. I’ve tried saving the scene as a ‘bundle’, but it seems to always crash upon opening…</p>
<p>Thanks again!</p>

---

## Post #6 by @muratmaga (2024-09-23 15:58 UTC)

<aside class="quote no-group" data-username="psychicpotato" data-post="5" data-topic="38464">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/psychicpotato/48/8303_2.png" class="avatar"> psychicpotato:</div>
<blockquote>
<p>but I think all I’m aiming for is just to save the scene w/o errors <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>If this your goals, just change the file format for markups to mrk.json than during the save.</p>

---

## Post #7 by @muratmaga (2024-09-23 16:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="38464">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>FCSV file format is a simple table-based, which cannot save the more complex data structures used by more recent markup nodes.</p>
</blockquote>
</aside>
<p>I propose we remove the fcsv as file saving option for Markups, and make it available only as Export As subject hierarchy plug in for some amount of time. For people who need their data as tables, there is already an export option from the Markups module.</p>

---
