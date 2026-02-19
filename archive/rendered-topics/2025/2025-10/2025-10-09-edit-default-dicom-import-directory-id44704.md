---
topic_id: 44704
title: "Edit Default Dicom Import Directory"
date: 2025-10-09
url: https://discourse.slicer.org/t/44704
---

# Edit default dicom import directory

**Topic ID**: 44704
**Date**: 2025-10-09
**URL**: https://discourse.slicer.org/t/edit-default-dicom-import-directory/44704

---

## Post #1 by @mvergnat (2025-10-09 08:55 UTC)

<p>hello to all 3dslicer fans!</p>
<p>I use slicer 5.8.1 on PC Windows 10 pro</p>
<p>I use “import dicom” very often.</p>
<p>unfortunately the “Import DICOM files from directory” window always open in the same folder:</p>
<p>C:\Users\7064654\AppData\Local\slicer.org\Slicer 5.8.1</p>
<p>I want to edit the default pathway into the other folder where I store all my dicoms.</p>
<p>Sure, I could create a shortcut, but I would like something more straightforward.</p>
<p>I looked on:</p>
<ul>
<li>3dslicer <strong>App Settings</strong> “General” or “Dicom”: no solution</li>
<li><strong>chatgpt</strong>: no good solution</li>
<li>3dslicer <strong>forums</strong>: no solution.</li>
</ul>
<p>Does anyone have an idea?</p>
<p>thanks for help!</p>
<p>mathieu</p>

---

## Post #2 by @cpinter (2025-10-09 09:14 UTC)

<p>In all the apps I develop, I store tha last used directory in application settings (QSettings, i.e. the Slicer.ini file). It would be quite easy to add this to the DICOM import.</p>

---

## Post #3 by @mvergnat (2025-10-09 09:32 UTC)

<p>dear csaba pinter,</p>
<p>many thx for answer!!</p>
<p>unfortunately, i m not sure i understand well:</p>
<p>you mean that i could create an app or modify (like python programming) an existing app? that is above my competences.</p>
<p>I asked if there was an easy way to do this in settings.</p>
<p>if there is no easy way, the shortcut inside the default folder is an easier way to achieve goal.</p>
<p>MANY THX indeed for your time! i appreciate!</p>
<p>mathieu</p>

---

## Post #4 by @cpinter (2025-10-09 13:39 UTC)

<p>What I said is that the developers could add this feature simply.</p>
<p>I don’t think there is any setting exposed for this.</p>

---

## Post #5 by @chir.set (2025-10-09 15:49 UTC)

<p>It could be that this directory shortcut available in the <code>Import DICOM</code> dialog box is handled by Qt itself.</p>
<p>On Linux, my Slicer startup script edits <code>$HOME/.config/QtProject.conf</code> to add a few directories to the shortcut key. Then the above mentioned dialog box shows the edited shortcuts.</p>
<p>But there’s a caveat. If just after starting Slicer, the <code>Add data/Choose file(s) to add</code> dialog box is raised, the shortcuts in that configuration file get overwritten to $HOME.</p>
<p>The workaround is good enough for me, your’s would be good enough for you. A general solution would be nice indeed, I have no idea if it’s Qt or application related.</p>

---

## Post #6 by @mikebind (2025-10-09 21:05 UTC)

<p>+1 for remembering a last-used import directory for DICOM import. That would be a nice quality of life improvement.</p>

---

## Post #7 by @pieper (2025-10-09 21:55 UTC)

<p>If someone is working on this, it would also be nice to remember the recently used dicom database locations too.</p>

---

## Post #8 by @cpinter (2025-11-11 14:41 UTC)

<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="44704">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>it would also be nice to remember the recently used dicom database locations too.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> What do you mean exactly? We already start navigating to select a new database from the location of the current one. Do you suggest opening a new dialog offering the last N database paths?</p>
<p>We just did the “saving the last imported DICOM directory” part, but this request needs clarification before we issue a PR. Thanks!</p>

---

## Post #9 by @pieper (2025-11-11 16:34 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a> - What I often do is create a ‘dicom database per project’.  For example, I get some data for multiple patients for research or I download a collection from IDC.  Then I’ll want to switch Slicer between databases to as I work on various projects.  Currently I use the directory browser to pick the dicom database folder for the project, but I need to remember and find the database directory manually.  It would be great if there were a list of recent directories stored in the settings and available in a pull aside menu of the dicom module to simplify this workflow.</p>

---

## Post #10 by @cpinter (2025-11-12 14:12 UTC)

<p>There is a PR for these two changes: <a href="https://github.com/Slicer/Slicer/pull/8843" class="inline-onebox">ENH: Last used DICOM import and 10 last used database directories are stored by xskere · Pull Request #8843 · Slicer/Slicer · GitHub</a></p>

---

## Post #11 by @xskere (2025-11-12 14:16 UTC)

<p>I hope the changes in the PR are what were on your mind!</p>

---
