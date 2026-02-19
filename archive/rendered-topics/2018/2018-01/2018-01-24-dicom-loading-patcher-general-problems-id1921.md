---
topic_id: 1921
title: "Dicom Loading Patcher General Problems"
date: 2018-01-24
url: https://discourse.slicer.org/t/1921
---

# DICOM loading, patcher, general problems. 

**Topic ID**: 1921
**Date**: 2018-01-24
**URL**: https://discourse.slicer.org/t/dicom-loading-patcher-general-problems/1921

---

## Post #1 by @MSilent (2018-01-24 12:41 UTC)

<p>I have previously successfully patched DICOM data into slicer.  Currently, after deleting and reinstalling the data I can now no longer successfully patch it.  It doesn’t write to a DICOM folder, it writes it to a pa000 folder.  That doesn’t load properly into the program.</p>
<p>If I use a data set that it can see, I click LOAD (from the DICOM/import) and nothing happens at all.  As I’ve used this data before I know it is okay generally.</p>

---

## Post #2 by @lassoan (2018-01-24 13:54 UTC)

<p>Which Slicer version do you use?<br>
Can you send the application log of a DICOM patching and import? (available in menu: Help / Report a bug)</p>

---

## Post #3 by @MSilent (2018-01-24 14:34 UTC)

<p>[DEBUG][Qt] 24.01.2018 14:28:19 [] (unknown:0) - Session start time …: 2018-01-24 14:28:19<br>
[DEBUG][Qt] 24.01.2018 14:28:19 [] (unknown:0) - Session start time …: 2018-01-24 14:28:19<br>
[DEBUG][Qt] 24.01.2018 14:28:19 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) win-amd64 - installed<br>
[DEBUG][Qt] 24.01.2018 14:28:19 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) win-amd64 - installed<br>
[DEBUG][Qt] 24.01.2018 14:28:19 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 24.01.2018 14:28:19 [] (unknown:0) - Memory …: 3981 MB physical, 8845 MB virtual<br>
[DEBUG][Qt] 24.01.2018 14:28:19 [] (unknown:0) - CPU …: AuthenticAMD AMD A9-9420 RADEON R5, 5 COMPUTE CORES 2C+3G   , 2 cores, 1 logical processors<br>
[DEBUG][Qt] 24.01.2018 14:28:19 [] (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 24.01.2018 14:28:19 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 24.01.2018 14:28:19 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 24.01.2018 14:29:32 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\<a href="http://cmd.py:719" rel="nofollow noopener">cmd.py:719</a>) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 24.01.2018 14:29:35 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\<a href="http://cmd.py:719" rel="nofollow noopener">cmd.py:719</a>) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 24.01.2018 14:29:54 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 24.01.2018 14:29:54 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 24.01.2018 14:29:59 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 24.01.2018 14:29:59 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Python] 24.01.2018 14:29:59 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 24.01.2018 14:28:48 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 24.01.2018 14:28:48 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 24.01.2018 14:29:42 [] (unknown:0) - Number of instantiated modules: 135<br>
[DEBUG][Qt] 24.01.2018 14:30:00 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 24.01.2018 14:30:00 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 24.01.2018 14:30:00 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 24.01.2018 14:30:00 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Python] 24.01.2018 14:30:32 [Python] (C:\Program Files\Slicer 4.8.1\bin\Python\slicer\<a href="http://util.py:942" rel="nofollow noopener">util.py:942</a>) - DICOM Database will be stored in</p>
<p>C:\Users\pg13t\OneDrive\Documents\SlicerDICOMDatabase</p>
<p>Use the Local Database button in the DICOM Browser to pick a different location.<br>
[DEBUG][Qt] 24.01.2018 14:30:31 [] (unknown:0) - Switch to module:  “DICOM”<br>
[INFO][Stream] 24.01.2018 14:30:32 [] (unknown:0) - DICOM Database will be stored in<br>
[INFO][Stream] 24.01.2018 14:30:32 [] (unknown:0) -<br>
[INFO][Stream] 24.01.2018 14:30:32 [] (unknown:0) - C:\Users\pg13t\OneDrive\Documents\SlicerDICOMDatabase<br>
[INFO][Stream] 24.01.2018 14:30:32 [] (unknown:0) -<br>
[INFO][Stream] 24.01.2018 14:30:32 [] (unknown:0) - Use the Local Database button in the DICOM Browser to pick a different location.<br>
[CRITICAL][Stream] 24.01.2018 14:32:18 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 24.01.2018 14:32:18 [] (unknown:0) -   File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\<a href="http://DICOMWidgets.py" rel="nofollow noopener">DICOMWidgets.py</a>”, line 766, in loadCheckedLoadables<br>
[CRITICAL][Stream] 24.01.2018 14:32:18 [] (unknown:0) -     self.examineForLoading()<br>
[CRITICAL][Stream] 24.01.2018 14:32:18 [] (unknown:0) -   File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\<a href="http://DICOMWidgets.py" rel="nofollow noopener">DICOMWidgets.py</a>”, line 677, in examineForLoading<br>
[CRITICAL][Stream] 24.01.2018 14:32:18 [] (unknown:0) -     self.loadablesByPlugin, loadEnabled = self.getLoadablesFromFileLists(self.fileLists)<br>
[CRITICAL][Stream] 24.01.2018 14:32:18 [] (unknown:0) - TypeError: ‘NoneType’ object is not iterable<br>
[DEBUG][Qt] 24.01.2018 14:33:00 [] (unknown:0) - Switch to module:  “”</p>

---

## Post #4 by @lassoan (2018-01-24 15:22 UTC)

<p>Thanks, the log was helpful. Could you try disabling MultiVolumeImporterPlugin and DICOMSlicerDataBundlePlugin and try again? (check Advanced, uncheck MultiVolumeImporterPlugin and DICOMSlicerDataBundlePlugin checkboxes, click Examine, then click Load)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/916754f9524fbee8571b508f236087e41eee7f2d.png" data-download-href="/uploads/short-url/kKiCuyAaBH57tt3zPG0cydEd6tn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/916754f9524fbee8571b508f236087e41eee7f2d.png" alt="image" data-base62-sha1="kKiCuyAaBH57tt3zPG0cydEd6tn" width="690" height="146" data-dominant-color="F6F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">845×180 9.29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If loading is not successful then please send the logs again.</p>

---

## Post #5 by @MSilent (2018-01-24 15:29 UTC)

<p>[DEBUG][Qt] 24.01.2018 15:26:55 [] (unknown:0) - Session start time …: 2018-01-24 15:26:55<br>
[DEBUG][Qt] 24.01.2018 15:26:55 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) win-amd64 - installed<br>
[DEBUG][Qt] 24.01.2018 15:26:55 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 24.01.2018 15:26:55 [] (unknown:0) - Memory …: 3981 MB physical, 8845 MB virtual<br>
[DEBUG][Qt] 24.01.2018 15:26:55 [] (unknown:0) - CPU …: AuthenticAMD AMD A9-9420 RADEON R5, 5 COMPUTE CORES 2C+3G   , 2 cores, 1 logical processors<br>
[DEBUG][Qt] 24.01.2018 15:26:55 [] (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 24.01.2018 15:26:55 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 24.01.2018 15:26:55 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 24.01.2018 15:27:09 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\<a href="http://cmd.py:719" rel="nofollow noopener">cmd.py:719</a>) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 24.01.2018 15:27:11 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\<a href="http://cmd.py:719" rel="nofollow noopener">cmd.py:719</a>) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 24.01.2018 15:27:17 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 24.01.2018 15:27:20 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 24.01.2018 15:27:20 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\<a href="http://AbstractScriptedSubjectHierarchyPlugin.py:36" rel="nofollow noopener">AbstractScriptedSubjectHierarchyPlugin.py:36</a>) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 24.01.2018 15:26:57 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 24.01.2018 15:27:14 [] (unknown:0) - Number of instantiated modules: 135<br>
[DEBUG][Qt] 24.01.2018 15:27:21 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 24.01.2018 15:27:21 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 24.01.2018 15:28:01 [] (unknown:0) - Switch to module:  “DICOM”<br>
[CRITICAL][Stream] 24.01.2018 15:28:23 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 24.01.2018 15:28:23 [] (unknown:0) -   File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\<a href="http://DICOMWidgets.py" rel="nofollow noopener">DICOMWidgets.py</a>”, line 766, in loadCheckedLoadables<br>
[CRITICAL][Stream] 24.01.2018 15:28:23 [] (unknown:0) -     self.examineForLoading()<br>
[CRITICAL][Stream] 24.01.2018 15:28:23 [] (unknown:0) -   File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\<a href="http://DICOMWidgets.py" rel="nofollow noopener">DICOMWidgets.py</a>”, line 677, in examineForLoading<br>
[CRITICAL][Stream] 24.01.2018 15:28:23 [] (unknown:0) -     self.loadablesByPlugin, loadEnabled = self.getLoadablesFromFileLists(self.fileLists)<br>
[CRITICAL][Stream] 24.01.2018 15:28:23 [] (unknown:0) - TypeError: ‘NoneType’ object is not iterable</p>

---

## Post #6 by @lassoan (2018-01-24 15:37 UTC)

<p>OK. It seems that your files cannot be interpreted as scalar volumes. The problem is most likely caused by invalid file content, which is most likely related to what you reported in this post: <a href="https://discourse.slicer.org/t/importing-data-from-patcher/1922">Importing data from patcher</a>. Let’s continue the discussion there.</p>

---

## Post #7 by @MSilent (2018-01-24 15:39 UTC)

<p>OK.  I’ll move over to that post.</p>

---

## Post #8 by @MSilent (2018-03-02 12:43 UTC)

<p>Update.   After reading through lots of discussions, I tried drag and drop on the original data.  It worked perfectly.  The load data from DICOM button is the problem.  Hence I thought the data needed patching, which sent me off on a rabbit trail.</p>
<p>So I don’t know if there is an error generally on the DICOM module, but at least now I know how to do it, it’s easy.</p>

---

## Post #9 by @lassoan (2018-03-05 16:23 UTC)

<aside class="quote no-group" data-username="MSilent" data-post="8" data-topic="1921">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/eb8c5e/48.png" class="avatar"> MSilent:</div>
<blockquote>
<p>I tried drag and drop on the original data.  It worked perfectly.</p>
</blockquote>
</aside>
<p>If you don’t go through the DICOM module then ITK’s DICOM reader is used directly. That only supports loading of images and many important checks are bypassed. If you are lucky then the result may be usable, but I would always recommend using DICOM module (and if there are errors then fix DICOM module, DICOM patcher, or the generator of the DICOM data set).</p>

---

## Post #10 by @MSilent (2018-03-05 17:09 UTC)

<p>How would I fix the DICOM module, or patcher? I spent months trying so many different things, and this has been the only route to success.<br>
The resulting image looks good, and the model was great.</p>

---

## Post #11 by @lassoan (2018-03-05 17:20 UTC)

<p>There is no single recipe for fixing things. Have you shared the problematic image with us?</p>

---
