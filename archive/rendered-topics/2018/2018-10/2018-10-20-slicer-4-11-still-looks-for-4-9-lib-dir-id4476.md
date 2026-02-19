---
topic_id: 4476
title: "Slicer 4 11 Still Looks For 4 9 Lib Dir"
date: 2018-10-20
url: https://discourse.slicer.org/t/4476
---

# Slicer 4.11 still looks for 4.9 lib dir

**Topic ID**: 4476
**Date**: 2018-10-20
**URL**: https://discourse.slicer.org/t/slicer-4-11-still-looks-for-4-9-lib-dir/4476

---

## Post #1 by @chir.set (2018-10-20 16:48 UTC)

<p>Built Slicer from git on Arch Linux. It does not start with Slicer executable. I have to set LD_LIBRARY_PATH to &lt;install_path&gt;/lib/Slicer-4.11 for it to run. Then the title bar still shows 4.9.0, while the about box shows 4.11.</p>
<p>On start, stdout shows</p>
<blockquote>
<p>…<br>
File “/home/user/programs/Slicer/bin/…/lib/Slicer-4.9/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 6, in <br>
import DICOMLib<br>
File “/home/user/programs/Slicer/lib/Slicer-4.9/qt-scripted-modules/DICOMLib/<strong>init</strong>.py”, line 4, in <br>
from DICOMWidgets import *<br>
File “/home/user/programs/Slicer/lib/Slicer-4.9/qt-scripted-modules/DICOMLib/DICOMWidgets.py”, line 8, in <br>
from ctk import ctkDICOMObjectListWidget, ctkDICOMDatabase, ctkDICOMIndexer, ctkDICOMBrowser, ctkPopupWidget, ctkExpandButton<br>
ImportError: cannot import name ctkDICOMObjectListWidget<br>
loadSourceAsModule - Failed to load file “/home/user/programs/Slicer/bin/…/lib/Slicer-4.9/qt-scripted-modules/MultiVolumeImporterPlugin.py”  as module “MultiVolumeImporterPlugin” !<br>
…</p>
</blockquote>
<p>That’s not a clean build, and I can’t test all functionalities. But the above stdout presumes that many modules won’t work. Is some tuning of cmake files required on your part ? Or should I delete all CTKAppLauncher* files and rebuild ? Or anything else ?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2018-10-20 17:29 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="4476">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>That’s not a clean build</p>
</blockquote>
</aside>
<p>You need to do a completely clear build when major or minor version of the application is changed.</p>

---

## Post #3 by @chir.set (2018-10-21 06:14 UTC)

<p>Yep, Slicer works as usual with a clean build. Thanks.</p>

---
