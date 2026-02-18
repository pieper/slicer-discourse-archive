# SlicerRT not compatible with nightly

**Topic ID**: 6504
**Date**: 2019-04-15
**URL**: https://discourse.slicer.org/t/slicerrt-not-compatible-with-nightly/6504

---

## Post #1 by @Alex_Vergara (2019-04-15 15:20 UTC)

<p>When installing SlicerRT it says</p>
<p>File “/Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/BatchStructureSetConversion.py”, line 233<br>
except Exception, e:<br>
^<br>
SyntaxError: invalid syntax</p>

---

## Post #2 by @cpinter (2019-04-15 15:25 UTC)

<p>Thanks for the report! We are in transition to Python3, which is not a trivial task, so it might take a while until everything is functional again.</p>
<p>I’ll fix this asap though. And please keep reporting anything new that comes up!</p>

---

## Post #3 by @jcfr (2019-04-15 15:38 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I will submit a PR on SlicerRT with a first round of updates.</p>

---

## Post #4 by @Alex_Vergara (2019-04-15 15:39 UTC)

<p>Traceback (most recent call last):<br>
File “/Users/alex/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMWidgets.py”, line 730, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examineForImport(fileLists)<br>
File “/Users/alex/Applications/Slicer.app/Contents/Extensions-28138/SlicerRT/lib/Slicer-4.11/qt-scripted-modules/DicomRtImportExportPlugin.py”, line 43, in examineForImport<br>
for loadableIndex in xrange(0,loadablesCollection.GetNumberOfItems()):<br>
NameError: name ‘xrange’ is not defined<br>
Warning: Plugin failed: DicomRtImportExportPlugin</p>
<p>See python console for error message.<br>
DICOM Plugin failed: name ‘xrange’ is not defined</p>

---

## Post #5 by @cpinter (2019-04-15 15:41 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I’m working on it right now</p>
<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> Please stand by with more error reports until I have committed the first fixes</p>

---

## Post #6 by @Alex_Vergara (2019-04-15 15:42 UTC)

<p>the last error was not on loading but when trying to import a DICOMRT</p>

---

## Post #7 by @jcfr (2019-04-15 15:53 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="6504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p><a class="mention" href="/u/jcfr">@jcfr</a> I’m working on it right now</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/cpinter">@cpinter</a> and I just synced offline and Csaba will continue his effort and i will help as needed later.</p>

---

## Post #8 by @cpinter (2019-04-16 13:39 UTC)

<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> SlicerRT works in the latest nightly. There is one more error coming from Slicer core when you load an RTImage, but otherwise it seems to works well. I’ll still do some tests to make sure, but I think the main functions should be fine now. Thanks for the report!</p>

---
