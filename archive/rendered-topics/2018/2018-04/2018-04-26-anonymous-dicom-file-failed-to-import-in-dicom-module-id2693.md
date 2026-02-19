---
topic_id: 2693
title: "Anonymous Dicom File Failed To Import In Dicom Module"
date: 2018-04-26
url: https://discourse.slicer.org/t/2693
---

# Anonymous Dicom file failed to import in Dicom module

**Topic ID**: 2693
**Date**: 2018-04-26
**URL**: https://discourse.slicer.org/t/anonymous-dicom-file-failed-to-import-in-dicom-module/2693

---

## Post #1 by @anandmulay3 (2018-04-26 07:24 UTC)

<p>i have a series of anonymous dicom files, when i try to import it; dicom module shows loading process but after it patient , study,series data shows 0(zero) value.so i cant load that series successfully.<br>
there is any different way to load anonymous series or any limitations on dicom series.<br>
(i have also tried to patch the series , which is also failed to patch)</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2018-04-26 15:36 UTC)

<p>Please follow the steps described <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">here</a> and let us know if you need further help.</p>

---

## Post #3 by @anandmulay3 (2018-04-30 08:21 UTC)

<p>Can you please tell me the thing actually slicer looks into series to catch the data or series info which helps it to identify the series as a volume data and loads it successfully( i mean as an anonymous series which dicom tag is important to load the series successfully) , so i can keep that thing while converting my series to anonymous.</p>

---

## Post #4 by @pieper (2018-04-30 12:30 UTC)

<p>Anonymization of DICOM data is a complex topic - you should try to use a standard tool like CTP or DicomCleaner (linked from the FAQ posted earlier) and the needed context is likely to be preserved.</p>
<p>If you want to know what header fields Slicer uses, you can <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L16">start here with the code</a> but there’s a lot of detail and we rely on many packages (ITK, CTK, DCMTK, GDCM…).</p>

---

## Post #5 by @lassoan (2018-04-30 13:05 UTC)

<aside class="quote no-group" data-username="anandmulay3" data-post="3" data-topic="2693">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"> anandmulay3:</div>
<blockquote>
<p>slicer looks into series to catch the data or series info which helps it to identify the series as a volume data and loads it successfully</p>
</blockquote>
</aside>
<p>When you create DICOM series, it is important to comply to DICOM standard to set all mandatory fields and not just fulfill one particular application’s requirements. Unfortunately, it is very difficult to decipher from the DICOM standard what fields are those, as there are many conditions and often even medical device manufacturers make mistakes (for example non-clinical, micro-CT, cone-beam CT devices are notoriously bad). That’s why I is recommended to use those standard anonymization tools that <a class="mention" href="/u/pieper">@pieper</a> described above.</p>

---

## Post #6 by @anandmulay3 (2018-04-30 13:33 UTC)

<p>thanks <a class="mention" href="/u/lassoan">@lassoan</a> And <a class="mention" href="/u/pieper">@pieper</a><br>
I’ll look into this.</p>

---

## Post #7 by @anandmulay3 (2018-05-04 12:07 UTC)

<p>Hello Andras i have looked into this series , the thing is when i try to import the series after loading the series this window showup<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac715bdcffe1c5336c0c942097a8c193d6fd8efa.png" alt="Capture" data-base62-sha1="oBuZHduov0oM1jxYRc4p1sgd1xw" width="192" height="159"></p>
<p>and in python interactor it shows: - Imported a DICOM directory, checking for extensions</p>
<p>and after trying to patch this series in DICOMPatcher following erros message :</p>
<pre><code>Traceback (most recent call last):
  File "C:/Program Files/Slicer 4.9.0/lib/Slicer-4.9/qt-scripted-modules/DICOMPatcher.py", line 154, in onPatchButton
    self.logic.patchDicomDir(self.inputDirSelector.currentPath, self.outputDirSelector.currentPath)
  File "C:/Program Files/Slicer 4.9.0/lib/Slicer-4.9/qt-scripted-modules/DICOMPatcher.py", line 577, in patchDicomDir
    dicom.write_file(patchedFilePath, ds)
  File "C:\Program Files\Slicer 4.9.0\lib\Python\Lib\site-packages\dicom\filewriter.py", line 356, in write_file
    write_dataset(fp, dataset)
  File "C:\Program Files\Slicer 4.9.0\lib\Python\Lib\site-packages\dicom\filewriter.py", line 200, in write_dataset
    write_data_element(fp, dataset[tag], dataset_encoding)
  File "C:\Program Files\Slicer 4.9.0\lib\Python\Lib\contextlib.py", line 35, in __exit__
    self.gen.throw(type, value, traceback)
  File "C:\Program Files\Slicer 4.9.0\lib\Python\Lib\site-packages\dicom\tagtools.py", line 21, in tag_in_exception
    raise type(e)(err)
Traceback (most recent call last):
  File "C:/Program Files/Slicer 4.9.0/lib/Slicer-4.9/qt-scripted-modules/DICOMPatcher.py", line 159, in onPatchButton
    traceback.print_exc()
  File "C:/Program Files/Slicer 4.9.0/lib/Python/Lib\traceback.py", line 233, in print_exc
    print_exception(etype, value, tb, limit, file)
  File "C:/Program Files/Slicer 4.9.0/lib/Python/Lib\traceback.py", line 128, in print_exception
    _print(file, line, '')
  File "C:/Program Files/Slicer 4.9.0/lib/Python/Lib\traceback.py", line 13, in _print
    file.write(str+terminator)
TypeError: argument 1 must be string without null bytes, not str![Capture|192x159]
</code></pre>
<p>Does it any kind of bug in Dicom or DICOMPatcher module.</p>

---

## Post #8 by @lassoan (2018-05-04 16:42 UTC)

<aside class="quote no-group" data-username="anandmulay3" data-post="7" data-topic="2693">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"> anandmulay3:</div>
<blockquote>
<p>argument 1 must be string without null bytes, not str![Capture|192x159]</p>
</blockquote>
</aside>
<p>It seems there is an invalid tag in the DICOM file. It is probably a string with the value of “[Capture|192x159]” which is incorrectly zero-terminated. If you have access to the software that created the DICOM tag then probably you can fix it by not writing the terminating <code>\0</code> character to the DICOM file.</p>

---
