---
topic_id: 28291
title: "Error Downloading Liver Ct Sample Image"
date: 2023-03-10
url: https://discourse.slicer.org/t/28291
---

# Error downloading Liver CT sample image

**Topic ID**: 28291
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/error-downloading-liver-ct-sample-image/28291

---

## Post #1 by @Amirmahdimech (2023-03-10 20:19 UTC)

<p>Hi guys<br>
I’m using Slicer 5.2.2 and for some reason it cannot download Liver CT sample data which is built-in.<br>
Does anybody know how I can download the sample data online?<br>
regards</p>

---

## Post #2 by @lassoan (2023-03-11 06:59 UTC)

<p>What is the error message in the Python console?</p>

---

## Post #3 by @Amirmahdimech (2023-03-11 15:59 UTC)

<p>It says “failed to download from repository”.<br>
I’ve downloaded previous versions(4.0.2 and 4.1) and tried to download the sample data and it was successful, but since I need Liver’s sample data which is only present in 5.0 and after versions, I have to somehow download it and load it into Slicer.</p>

---

## Post #4 by @lassoan (2023-03-11 16:00 UTC)

<p>Please copy here the application log (menu: Help / Report a bug) for a bit more details. Thank you.</p>

---

## Post #5 by @Amirmahdimech (2023-03-11 16:20 UTC)

<p>Here the error<br>
"Status: Idle</p>
<p>Requesting download CTLiver.nrrd from <a href="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/e16eae0ae6fefa858c5c11e58f0f1bb81834d81b7102e021571056324ef6f37e" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/e16eae0ae6fefa858c5c11e58f0f1bb81834d81b7102e021571056324ef6f37e</a> …</p>
<p>Download failed:</p>
<p>Download failed (attempt 1 of 3)…</p>
<p>Requesting download CTLiver.nrrd from <a href="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/e16eae0ae6fefa858c5c11e58f0f1bb81834d81b7102e021571056324ef6f37e" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/e16eae0ae6fefa858c5c11e58f0f1bb81834d81b7102e021571056324ef6f37e</a> …</p>
<p>Download failed:</p>
<p>Download failed (attempt 2 of 3)…</p>
<p>Requesting download CTLiver.nrrd from <a href="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/e16eae0ae6fefa858c5c11e58f0f1bb81834d81b7102e021571056324ef6f37e" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/e16eae0ae6fefa858c5c11e58f0f1bb81834d81b7102e021571056324ef6f37e</a> …</p>
<p>Download failed:</p>
<p>Download failed (attempt 3 of 3)…"</p>

---

## Post #6 by @Amirmahdimech (2023-03-11 16:22 UTC)

<pre><code class="lang-auto">[DEBUG][Qt] 11.03.2023 19:44:40 [] (unknown:0) - Session start time .......: 2023-03-11 19:44:40
[DEBUG][Qt] 11.03.2023 19:44:40 [] (unknown:0) - Slicer version ...........: 5.2.2 (revision 31382 / fb46bd1) win-amd64 - installed release
[DEBUG][Qt] 11.03.2023 19:44:40 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19044, Code Page 65001) - 64-bit
[DEBUG][Qt] 11.03.2023 19:44:40 [] (unknown:0) - Memory ...................: 8056 MB physical, 20344 MB virtual
[DEBUG][Qt] 11.03.2023 19:44:40 [] (unknown:0) - CPU ......................: GenuineIntel , 4 cores, 4 logical processors
[DEBUG][Qt] 11.03.2023 19:44:40 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 11.03.2023 19:44:40 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[WARNING][Qt] 11.03.2023 19:44:41 [] (unknown:0) - Could not get the INetworkConnection instance for the adapter GUID.
[DEBUG][Qt] 11.03.2023 19:44:41 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 11.03.2023 19:44:41 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 11.03.2023 19:44:41 [] (unknown:0) - Application path .........: C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin
[DEBUG][Qt] 11.03.2023 19:44:41 [] (unknown:0) - Additional module paths ..: NA-MIC/Extensions-31382/RawImageGuess/lib/Slicer-5.2/qt-scripted-modules
[DEBUG][Python] 11.03.2023 19:45:17 [Python] (C:\Users\SIGMA\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 11.03.2023 19:45:21 [Python] (C:\Users\SIGMA\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 11.03.2023 19:45:21 [Python] (C:\Users\SIGMA\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 11.03.2023 19:45:23 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 11.03.2023 19:45:50 [] (unknown:0) - Switch to module:  "SampleData"
[DEBUG][Python] 11.03.2023 19:45:50 [Python] (C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../lib/Slicer-5.2/qt-scripted-modules/SampleData.py:386) - &lt;p&gt;Status: &lt;i&gt;Idle&lt;/i&gt;&lt;/p&gt;
[DEBUG][Python] 11.03.2023 19:45:55 [Python] (C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../lib/Slicer-5.2/qt-scripted-modules/SampleData.py:386) - &lt;b&gt;Requesting download&lt;/b&gt; &lt;i&gt;CTLiver.nrrd&lt;/i&gt; from https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/e16eae0ae6fefa858c5c11e58f0f1bb81834d81b7102e021571056324ef6f37e ...
[ERROR][Python] 11.03.2023 19:47:31 [Python] (C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../lib/Slicer-5.2/qt-scripted-modules/SampleData.py:386) - &lt;font color="red"&gt;&lt;b&gt;	Download failed: &lt;urlopen error [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond&gt;&lt;/b&gt;&lt;/font&gt;
[ERROR][Python] 11.03.2023 19:47:31 [Python] (C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../lib/Slicer-5.2/qt-scripted-modules/SampleData.py:386) - &lt;font color="red"&gt;&lt;b&gt;Download failed (attempt 1 of 3)...&lt;/b&gt;&lt;/font&gt;
[DEBUG][Python] 11.03.2023 19:47:31 [Python] (C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../lib/Slicer-5.2/qt-scripted-modules/SampleData.py:386) - &lt;b&gt;Requesting download&lt;/b&gt; &lt;i&gt;CTLiver.nrrd&lt;/i&gt; from https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/e16eae0ae6fefa858c5c11e58f0f1bb81834d81b7102e021571056324ef6f37e ...
[ERROR][Python] 11.03.2023 19:48:10 [Python] (C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../lib/Slicer-5.2/qt-scripted-modules/SampleData.py:386) - &lt;font color="red"&gt;&lt;b&gt;	Download failed: &lt;urlopen error [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond&gt;&lt;/b&gt;&lt;/font&gt;
[ERROR][Python] 11.03.2023 19:48:10 [Python] (C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../lib/Slicer-5.2/qt-scripted-modules/SampleData.py:386) - &lt;font color="red"&gt;&lt;b&gt;Download failed (attempt 2 of 3)...&lt;/b&gt;&lt;/font&gt;
[DEBUG][Python] 11.03.2023 19:48:10 [Python] (C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../lib/Slicer-5.2/qt-scripted-modules/SampleData.py:386) - &lt;b&gt;Requesting download&lt;/b&gt; &lt;i&gt;CTLiver.nrrd&lt;/i&gt; from https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/e16eae0ae6fefa858c5c11e58f0f1bb81834d81b7102e021571056324ef6f37e ...
[ERROR][Python] 11.03.2023 19:48:40 [Python] (C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../lib/Slicer-5.2/qt-scripted-modules/SampleData.py:386) - &lt;font color="red"&gt;&lt;b&gt;	Download failed: &lt;urlopen error [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond&gt;&lt;/b&gt;&lt;/font&gt;
[ERROR][Python] 11.03.2023 19:48:40 [Python] (C:/Users/SIGMA/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../lib/Slicer-5.2/qt-scripted-modules/SampleData.py:386) - &lt;font color="red"&gt;&lt;b&gt;Download failed (attempt 3 of 3)...&lt;/b&gt;&lt;/font&gt;
</code></pre>

---

## Post #7 by @lassoan (2023-03-11 16:34 UTC)

<p>It seems that you are using a proxy server that does not let direct access to the server. You can specify proxy server for Python (see for example <a href="https://stackoverflow.com/questions/15820739/python-urlerror-urlopen-error-errno-10060">here</a>).</p>
<p>If that doesn’t work then you can download from the displayed URL using your web browser and rename the downloaded file to <code>liver.nrrd</code>.</p>

---

## Post #8 by @Amirmahdimech (2023-03-11 17:51 UTC)

<p>First time that I tried downloading the file, since it didn’t have a format assigned to it I gave up on it. But after I changed it’s name to liver.nrrd it worked!<br>
Thanks Andras</p>

---
