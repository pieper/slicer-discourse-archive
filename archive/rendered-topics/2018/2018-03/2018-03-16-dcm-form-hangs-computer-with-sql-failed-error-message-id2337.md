# DCM form, hangs computer with SQL Failed error message

**Topic ID**: 2337
**Date**: 2018-03-16
**URL**: https://discourse.slicer.org/t/dcm-form-hangs-computer-with-sql-failed-error-message/2337

---

## Post #1 by @JohnK (2018-03-16 16:51 UTC)

<p>Using Slicer 4.9, Windows 7 64bit</p>
<p>I  have a major error occurring on my DCM form when it initially shows (no button clicks yet). My entire computer hangs and not even Task Manager shows up so I can stop the slicer process / App</p>
<p>"SQL Failed<br>
Bad SQL: SELECT value FROM TagCache WHERE SOPInstanceUID = :SOPInstanceUID AND Tag = :Tag</p>
<p>error text: disk I/O error unable to fetch row. "</p>
<p>I suspect the error comes from not allowing the system to background events, but this is pretty serious. Any suggestions?</p>

---

## Post #2 by @lassoan (2018-03-16 17:14 UTC)

<p>If the whole system hangs then most likely it is indeed a disk error. If your local disk is not acting up otherwise, then it is probably due to an inaccessible network drive. To fix that, make all the mapped network drive accessible, or remove those that are inaccessible.</p>

---

## Post #3 by @JohnK (2018-03-16 17:24 UTC)

<p>All disks /net drive appear to function normally otherwise. I suspect the DICOM listener is acting up (it never worked in the first place). Is there a way to turn off the listener in SLICER without using the DCM form?</p>

---

## Post #4 by @lassoan (2018-03-16 17:45 UTC)

<p>Can you try to open a file selector dialog in Slicer? It would be important to know if those hang, too.</p>
<p>You can edit all application settings in Slicer.ini and Slicer-NNNN.ini files in your user profile folder (AppData/Roaming/NA-MIC/… or something like that). You can also start Slicer with default settings by running <code>Slicer.exe --disable-settings</code>.</p>

---

## Post #5 by @JohnK (2018-03-16 17:55 UTC)

<p>Yes, choosing files to add works fine.<br>
This gets me back to the point that Slicer does not crash my computer:<br>
-copied the database to a new folder</p>
<ul>
<li>in the slicer.ini file remove any fields from<br>
StoragePort=<br>
ServerNodeCount=<br>
CallingAETitle=<br>
StorageAETitle=</li>
</ul>
<p>So I suspect my database was corrupt ( will just restart from scratch) or the DICOM listener was hanging up.<br>
Either way that part of the 3Dslicer code is absolutely evil since it does not allow you to shut down its process!</p>
<p>Thanks so much for your help.</p>

---
