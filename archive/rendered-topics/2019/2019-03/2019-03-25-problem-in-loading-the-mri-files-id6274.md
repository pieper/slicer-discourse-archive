---
topic_id: 6274
title: "Problem In Loading The Mri Files"
date: 2019-03-25
url: https://discourse.slicer.org/t/6274
---

# Problem in loading the MRI files

**Topic ID**: 6274
**Date**: 2019-03-25
**URL**: https://discourse.slicer.org/t/problem-in-loading-the-mri-files/6274

---

## Post #1 by @Valeria_di_Battista (2019-03-25 11:47 UTC)

<p>Good morning,<br>
I’m using the Slicer 4.11.0 version of the software to visualize and reconstruct Volume from MRI images of a breast tumor. Till yesterday I was able to load the DICOM file without any problem. Today i’m not able anymore to do it. I click on the DICOM module, I select the files I’m interested in and I click the load button. The software checks “DICOMScalarVolumePlugin”, “MultiVolumeImportPlugin” and “DICOMSlicerDataBundlePlugin”. It gives me some errors and it invites me to check the Python Console. It says this:</p>
<pre><code class="lang-auto">-----------------------------------------------------------------------------------
Geometric issues were found with 1 of the series. Please use caution.

Traceback (most recent call last):

File &amp;quot;C:\Program Files\Slicer 4.11.0-2019-03-24\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMWidgets.py&amp;quot;, line 732, in getLoadablesFromFileLists

loadablesByPlugin[plugin] = plugin.examine(fileLists)

File &amp;quot;C:/Program Files/Slicer 4.11.0-2019-03-24/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py&amp;quot;, line 106, in examine

loadables += self.examineFiles(files)

File &amp;quot;C:/Program Files/Slicer 4.11.0-2019-03-24/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py&amp;quot;, line 493, in examineFiles

mvNodes = self.initMultiVolumes(subseriesLists[key])

File &amp;quot;C:/Program Files/Slicer 4.11.0-2019-03-24/bin/../lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py&amp;quot;, line 885, in initMultiVolumes

mvNode.SetAttribute('MultiVolume.FrameFileList', frameFileListStr)

TypeError: SetAttribute argument 2: (unicode conversion error)

Warning: Plugin failed: MultiVolumeImporterPlugin

See python console for error message.

DICOM Plugin failed: SetAttribute argument 2: (unicode conversion error)

Warning in DICOM plugin Scalar Volume when examining loadable 601: dyn_eTHRIVE: Images are not equally spaced (a difference of 1 vs 0 in spacings was detected). If loaded image appears distorted, enable 'Acquisition geometry regularization' in Application settings / DICOM / DICOMScalarVolumePlugin. Please use caution.

DICOM plugin failed to load '601: dyn_eTHRIVE' as a 'Scalar Volume'.

Traceback (most recent call last):

File &amp;quot;C:\Program Files\Slicer 4.11.0-2019-03-24\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMWidgets.py&amp;quot;, line 862, in proceedWithReferencedLoadablesSelection

loadSuccess = plugin.load(loadable)

File &amp;quot;C:/Program Files/Slicer 4.11.0-2019-03-24/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py&amp;quot;, line 422, in load

volumeNode = self.loadFilesWithSeriesReader(&amp;quot;GDCM&amp;quot;, loadable.files, loadable.name)

File &amp;quot;C:/Program Files/Slicer 4.11.0-2019-03-24/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py&amp;quot;, line 299, in loadFilesWithSeriesReader

reader.SetArchetype(files[0]);

TypeError: SetArchetype argument 1: (unicode conversion error)

Could not load: 601: dyn_eTHRIVE as a Scalar Volume
------------------------------
</code></pre>
<p>What could I do? I tried to install older version too, but the problem is still there.</p>

---

## Post #2 by @pieper (2019-03-25 13:18 UTC)

<aside class="quote no-group" data-username="Valeria_di_Battista" data-post="1" data-topic="6274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/valeria_di_battista/48/3321_2.png" class="avatar"> Valeria_di_Battista:</div>
<blockquote>
<p>(unicode conversion error)</p>
</blockquote>
</aside>
<p>Looks like an issue with the characters used in the file path.  Can you try again with only ascii characters?</p>

---

## Post #3 by @Valeria_di_Battista (2019-03-25 13:59 UTC)

<p>Actually, yesterday I changed the name of the folder in which the DICOM images are saved. I tried to rename the folder with the previous name and I tried again to import and load the DICOM images. The problem still occurs.</p>
<p>In the error the program says this:<br>
“Images are not equally spaced (a difference of 1 vs 0 in spacings was detected)”</p>
<p>But i didn’t touch in any way the images. I don’t understand why the software doesn’t load the images anymore.</p>

---

## Post #4 by @pieper (2019-03-25 14:15 UTC)

<p>Probably you can select a new dicom database location and re-import using the ascii directory paths.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM</a></p>

---

## Post #5 by @Valeria_di_Battista (2019-03-25 15:47 UTC)

<p>I’m using anonymizated DICOM with the extension “.dcm” coming from an application crated with MATLAB. I tried so to use the original not anonymized file and with no extension. I tried to change location, too. It still doesn’t work.</p>

---

## Post #6 by @lassoan (2019-03-25 15:52 UTC)

<aside class="quote no-group" data-username="Valeria_di_Battista" data-post="5" data-topic="6274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/valeria_di_battista/48/3321_2.png" class="avatar"> Valeria_di_Battista:</div>
<blockquote>
<p>I’m using anonymizated DICOM with the extension “.dcm” coming from an application crated with MATLAB</p>
</blockquote>
</aside>
<p>There is a good chance that the anonymization process ruined the image by removing mandatory DICOM fields. You may be able to fix the data set by using Slicer’s “DICOM Patcher” module. If that does not help then you probably need to fix the anonymizer.</p>

---
