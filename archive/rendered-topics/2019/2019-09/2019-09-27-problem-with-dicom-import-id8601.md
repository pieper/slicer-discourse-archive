---
topic_id: 8601
title: "Problem With Dicom Import"
date: 2019-09-27
url: https://discourse.slicer.org/t/8601
---

# Problem with DICOM import

**Topic ID**: 8601
**Date**: 2019-09-27
**URL**: https://discourse.slicer.org/t/problem-with-dicom-import/8601

---

## Post #1 by @AMM (2019-09-27 22:20 UTC)

<p>Hello,</p>
<p>I already read questions about this problem, but for me nothing worked.<br>
I used to use 3D slicer with DICOM files without problem. After 2 or 3 months without using it, yesterday I tried and it doesn’t work (for the same DICOM files…).</p>
<p>I updated the Slicer version (it is now 4.10.2) and I am working with LINUX (CentOS Linux 7).</p>
<p>I try to import DICOM series and I receive the same error I saw for lots of people:<br>
“Slicer has caught an internal error.<br>
You may be able to continue from this point, but results are undefined.<br>
Suggested action is to save your work and restart.<br>
If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="nofollow noopener">http://slicer.org</a><br>
The message detail is:<br>
Exception thrown in event: Calling methods on uninitialized ctkDICOMItem”</p>
<ul>
<li>I changed directory (with a shorter one) and same error;</li>
<li>I used DICOM patcher and another error:<br>
" DICOM patching started…<br>
Unexpected error: ‘module’ object has no attribute ‘UID’"</li>
</ul>
<p>I am using original clinical DICOM files, I didn’t change anything, it works with other softwares and I already opened them with Slicer before without problems…</p>
<p>Can someone help me please?</p>
<p>Thank you in advance!!</p>

---

## Post #3 by @lassoan (2019-09-27 22:29 UTC)

<p>Try to create a new empty folder in writeable location, choose that as DICOM database folder, and re-import your DICOM files. If you still have issues, follow suggestions on the DICOM FAQ page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---

## Post #4 by @pieper (2019-09-27 22:37 UTC)

<p>Hmm, that’s odd - maybe try the ideas in <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" rel="nofollow noopener">DICOM FAQ</a>?  How about <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings#Settings_file_location" rel="nofollow noopener">deleting the settings</a>?</p>

---

## Post #5 by @AMM (2019-09-30 10:05 UTC)

<p>Thank you.</p>
<p>I did what you said (<a class="mention" href="/u/lassoan">@lassoan</a> ) and now I don’t see the error message anymore. BUT when I try to import DICOM data…</p>
<p>“Directory import completed.<br>
0 New Patients<br>
0 New Studies<br>
0 New Series<br>
0 New Instances”</p>
<p>I already delete the .*ini files as in “deleting the settings” (<a class="mention" href="/u/pieper">@pieper</a>)  and the same thing happens…</p>
<p>Any more ideas how to fix this??<br>
Thank you again!</p>

---

## Post #6 by @AMM (2019-09-30 10:22 UTC)

<p>I just saw that as soon as I open Slicer, although the interface appears “normally”, at command line I have the message<br>
“Switch to module:  “Welcome”<br>
There was an error during execution of the statement:  " CREATE TABLE ‘SchemaInfo’ ( ‘Version’ VARCHAR(1024) NOT NULL );”<br>
Error message:  “disk I/O error Unable to fetch row”<br>
"<br>
Could this be the reason? What does it mean and what can I do to fix it?</p>
<p>Thank you!!</p>

---

## Post #7 by @pieper (2019-09-30 12:19 UTC)

<p>There’s something wrong with your dicom database file.  Perhaps you don’t have permissions (you are using linux. so maybe you ran as root when the database was created - just guessing here).  In any case maybe try creating a new user account to start fresh.</p>

---
