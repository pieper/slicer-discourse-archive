---
topic_id: 27831
title: "Totalsegmenter Looks For A Non Existant Archve File"
date: 2023-02-15
url: https://discourse.slicer.org/t/27831
---

# TotalSegmenter looks for a non-existant archve file

**Topic ID**: 27831
**Date**: 2023-02-15
**URL**: https://discourse.slicer.org/t/totalsegmenter-looks-for-a-non-existant-archve-file/27831

---

## Post #1 by @GeneRisi (2023-02-15 18:11 UTC)

<p>When I try to run TotalSegmenter with the sample data ( in Slicer 5.3.0), I get this message</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\Gene\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-27\bin\Python\slicer\util.py”, line 2973, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/Gene/AppData/Local/NA-MIC/Slicer 5.3.0-2023-01-27/NA-MIC/Extensions-31549/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 255, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “C:/Users/Gene/AppData/Local/NA-MIC/Slicer 5.3.0-2023-01-27/NA-MIC/Extensions-31549/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 624, in setupPythonRequirements<br>
slicer.util.pip_install(self.totalSegmentatorPythonPackageDownloadUrl)<br>
File “C:\Users\Gene\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-27\bin\Python\slicer\util.py”, line 3586, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\Users\Gene\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-27\bin\Python\slicer\util.py”, line 3548, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\Gene\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-27\bin\Python\slicer\util.py”, line 3517, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command '[‘C:/Users/Gene/AppData/Local/NA-MIC/Slicer 5.3.0-2023-01-27/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, '<a href="https://github.com/wasserth/TotalSegmentator/archive/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a.zip'%5D'" rel="noopener nofollow ugc">https://github.com/wasserth/TotalSegmentator/archive/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a.zip’]’</a> returned non-zero exit status 1.</p>
<p>I found that the archive does not exist online. How can I fix this?</p>
<p>Thank you!</p>
<p>Gene Risi</p>

---

## Post #2 by @lassoan (2023-02-16 00:27 UTC)

<p>If the <a href="https://github.com/wasserth/TotalSegmentator/archive/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a.zip">https://github.com/wasserth/TotalSegmentator/archive/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a.zip</a> is not accessible for you then it means that you have a network connectivity problem.</p>
<p>If you want to get more details on why the installation fails, exit Slicer and launch this in a Windows Command Prompt:</p>
<p><code>"C:\Users\Gene\AppData\Local\NA-MIC\Slicer 5.3.0-2023-01-27\bin\PythonSlicer.EXE" -m pip install https://github.com/wasserth/TotalSegmentator/archive/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a.zip</code></p>

---

## Post #3 by @GeneRisi (2023-02-16 00:49 UTC)

<p>Thank you, Andras! That worked and now things are running <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @rbumm (2023-02-16 06:20 UTC)

<p>Where can we get the information about available GitHub archive files for this and other projects?</p>

---

## Post #5 by @lassoan (2023-02-16 12:18 UTC)

<p>Github accepts any branch name or commit hash as .zip file name.</p>

---

## Post #6 by @rbumm (2023-02-16 13:11 UTC)

<p>Sry, but where did you find the hash.zip? If I enter <code>https://github.com/wasserth/TotalSegmentator/archive/</code><br>
it does not show what zip files are available. Should we just use a commit hash?</p>

---

## Post #7 by @lassoan (2023-02-16 13:36 UTC)

<p>You can find commit hashes in the commit history.</p>

---
