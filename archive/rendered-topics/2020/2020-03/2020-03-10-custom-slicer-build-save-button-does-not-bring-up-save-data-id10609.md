# Custom Slicer build - Save button does not bring up "Save Data" widget, does not load NRRD files

**Topic ID**: 10609
**Date**: 2020-03-10
**URL**: https://discourse.slicer.org/t/custom-slicer-build-save-button-does-not-bring-up-save-data-widget-does-not-load-nrrd-files/10609

---

## Post #1 by @aptirumalai (2020-03-10 07:32 UTC)

<p>I am working with a custom Slicer based application that Kitware helped us develop 2 years ago.</p>
<p>I built our custom Slicer-based application on one laptop. But the application does not behave correctly on this laptop. It will not load NRRD files or FCSV files. However, it is able to load a DICOM series and display it correctly. Another peculiarity is that when I click the “Save” button, it just brings up a standard Windows save dialog - not the Qt “Save Data” widget.</p>
<p>As a test, I created an installer for this application on this laptop. (It is something Kitware provided too). When I installed it on a different laptop using this installed .exe file, everything works normally - NRRD and FCSV files load properly, the Save button brings up the expected “Save Data” widget.</p>
<p>I have attached screenshots of the dialog boxes that pop up on the two laptops.</p>
<p>I am baffled. Any idea what is going on here?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e0dbabf97528a98c4561475bb27a7e30454a134.png" data-download-href="/uploads/short-url/6zpnuBiSRAjAmqZQD3GbqwwNia8.png?dl=1" title="SaveSceneandUnsavedData1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e0dbabf97528a98c4561475bb27a7e30454a134_2_690x432.png" alt="SaveSceneandUnsavedData1" data-base62-sha1="6zpnuBiSRAjAmqZQD3GbqwwNia8" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e0dbabf97528a98c4561475bb27a7e30454a134_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e0dbabf97528a98c4561475bb27a7e30454a134.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e0dbabf97528a98c4561475bb27a7e30454a134.png 2x" data-dominant-color="B8BCBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SaveSceneandUnsavedData1</span><span class="informations">918×575 39.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-03-10 15:37 UTC)

<p>Probably a custom module overrides default save and load data behavior.</p>

---

## Post #3 by @aptirumalai (2020-03-10 17:54 UTC)

<p>When I created a .exe installer on the laptop where I am seeing this issue - and then use that installer to install the same application on a different laptop, it behaves normally on the second laptop. That is what is baffling me.</p>
<p>I could try stepping through the code in Visual Studio - to trace what is happening when I click the “Save” button. Which files should I set breakpoints at? I think it is under:<br>
Slicer-build/Base/QTGUI/moc_qSlicerSaveDataDialog_p.cxx. Is this correct?</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2020-03-10 17:57 UTC)

<p>Probably you have a custom module/extension installed on the laptop where you see this issue. Check if anything is listed under “Additional module paths” (in Application settings / Modules).</p>

---

## Post #5 by @aptirumalai (2020-03-10 18:43 UTC)

<p>I checked Application Settings. The “Additional module paths” is empty.</p>
<p>I sent the installer over to our client. They were able to install it and it works normally on their side. So the issue is specific to this one laptop where I built the application and created the installer.</p>
<p>Any other suggestions? Will stepping through the code shed some light? What files are involved when the Save button is clicked?</p>

---

## Post #6 by @aptirumalai (2020-03-11 17:59 UTC)

<p>I used the Visual Studio Debugger to trace what is going on. This is what I traced when I clicked the “Data” button in our custom Slicer build. The standard FileDialog pops up instead of the Slicer Data Widget. This is another of the issues I have with our custom build - similar to what happens when I click the “Save” button. I discovered the the Slicer code does indeed bring up the standard dialogs in some cases of failure.</p>
<p>The issue comes from …\Slicer\Base\QTGUI\qSlicerIOManager.cc<br>
bool qSlicerIOManager::openDialog(qSlicerIO::IOFileType fileType,…)<br>
{<br>
bool deleteDialog = false;<br>
if (properties[“objectName”].toString().isEmpty())<br>
{<br>
QString name = d-&gt;createUniqueDialogName(fileType, action, properties);<br>
properties[“objectName”] = name;<br>
}<br>
qSlicerFileDialog* dialog = d-&gt;findDialog(fileType, action);<br>
if (dialog == 0)<br>
{<br>
deleteDialog = true;<br>
qSlicerStandardFileDialog* standardDialog =<br>
new qSlicerStandardFileDialog(this);<br>
…</p>
<p>So the issue arises from the findDialog() method. On the laptop where I am having this issue, findDialog() returns NULL causing the standardDialog to pop up instead? I do not know why yet - but thought I would share it with you hoping for answers. I am not familiar with Qt.</p>

---

## Post #7 by @lassoan (2020-03-11 18:16 UTC)

<p>Nice work, just continue along these lines. Step into findDialog, see what fileType you get, what qSlicerFileDialog classes are registered, etc. The default save dialog is qSlicerSaveDataDialog, registered in qSlicerDataModule. If that is not found then it is either not registered or later removed or overridden by another one. Even a scripted module can override the default save dialog (look for “FileDialog” in all .py files).</p>

---

## Post #8 by @aptirumalai (2020-03-12 18:24 UTC)

<p>I continued debugging. On the laptop where the code works, I noticed the following:<br>
“…/Slicer-build/lib/Slicer-4.5/qt-scripted-modules/DICOM.py”<br>
registerDialog: Read   “DICOM Directory”<br>
…<br>
“…/Slicer-build/lib/Slicer-4.5/qt-scripted-modules/DICOMSlicerDataBundlePlugin.py”<br>
registerDialog: Read   “NoFile”<br>
registerDialog: Write  “NoFile”</p>
<p>So after the DICOMSlicerDataBundlePlugin.py module is processed, “NoFile” gets registered (for both Read and Write).</p>
<p>On the laptop where it fails, “NoFile” does not get registered. The only registered dialogs are “DICOM Directory” and “ModelFile” (added when Editor.py is processed)</p>
<p>So when I click the “Data” button, it looks for the “NoFile” dialog but does not find it. So it pops up the default dialog.</p>
<p>I can dig further. But I thought I would check if you had a quick answer or suggestion. Could be the Antivirus software preventing something from being loaded? I have Traps running and it has been blocking certain modules.</p>
<p>Thanks so much.</p>

---

## Post #9 by @lassoan (2020-03-12 18:58 UTC)

<aside class="quote no-group" data-username="aptirumalai" data-post="8" data-topic="10609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aptirumalai/48/6198_2.png" class="avatar"> aptirumalai:</div>
<blockquote>
<p>So after the DICOMSlicerDataBundlePlugin.py module is processed, “NoFile” gets registered (for both Read and Write).</p>
</blockquote>
</aside>
<p>Probably you have a stray .py or .pyc file somewhere that registers this NoFile (scene) read/write plugins. Maybe it is the DICOMSlicerDataBundlePlugin. Try to delete that file and see if you still get the extra dialog registrations.</p>
<aside class="quote no-group" data-username="aptirumalai" data-post="8" data-topic="10609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aptirumalai/48/6198_2.png" class="avatar"> aptirumalai:</div>
<blockquote>
<p>“…/Slicer-build/lib/Slicer-4.5/qt-scripted-modules/DICOM.py”<br>
registerDialog: Read “DICOM Directory”</p>
</blockquote>
</aside>
<p>Do you really use Slicer-4.5??? That would be very, very old.</p>

---

## Post #10 by @aptirumalai (2020-03-12 19:18 UTC)

<blockquote>
<blockquote>
<p>Probably you have a stray .py or .pyc file somewhere that registers this NoFile (scene) read/write &gt;&gt;plugins. Maybe it is the DICOMSlicerDataBundlePlugin. Try to delete that file and see if you still get &gt;&gt; the extra dialog registrations.<br>
Oh. I was under the impression that it is the “NoFile” registration that makes it work. This is what I thought I observed. On the laptop where it does work, “NoFile” is registered along with “Dicom Directory” and “Model File”. Am I mistaken?</p>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<p>Do you really use Slicer-4.5??? That would be very, very old.<br>
Yes it is OLD. This application was built with Kitware’s help (JC and others) in 2016. It was customized to work with Visual Studio 2013 and QT4.8.7. We are not actively working on it. Just in support mode at this time for a client. I do need to follow up with JC as the app will no longer build without manual hacks. The build process was fine last year - the last time I successfully built it was Feb. 2019.</p>
</blockquote>
</blockquote>

---

## Post #11 by @lassoan (2020-03-12 19:31 UTC)

<aside class="quote no-group" data-username="aptirumalai" data-post="10" data-topic="10609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aptirumalai/48/6198_2.png" class="avatar"> aptirumalai:</div>
<blockquote>
<p>Oh. I was under the impression that it is the “NoFile” registration that makes it work.</p>
</blockquote>
</aside>
<p>NoFile is the scene save dialog. Normally you have only one plugin that registers as NoFile: the standard save dialog. It seems that you have another one, which registers itself as NoFile, replacing the standard save dialog.</p>

---
