---
topic_id: 11450
title: "How To For A Really Newbie Having A Mri Cdrom"
date: 2020-05-07
url: https://discourse.slicer.org/t/11450
---

# "How to" for a really newbie having a MRI CDRom?

**Topic ID**: 11450
**Date**: 2020-05-07
**URL**: https://discourse.slicer.org/t/how-to-for-a-really-newbie-having-a-mri-cdrom/11450

---

## Post #1 by @janolap1 (2020-05-07 18:27 UTC)

<p>Operating system: Win10<br>
Slicer version: 4.10.2<br>
Expected behavior: Obtaining 3D model of my head<br>
Actual behavior: Seeing images but not sure the good way</p>
<p>Hi, I’m really new to 3D Slicer and all of those MRI stuff.<br>
I’m french, so you can contact me in this language if you want.</p>
<p>I’ve got a recent MRI of a head on a CD-ROM.<br>
The directory structure of the CD-ROM is shown below :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42f2e560ae4577c1694e20e26ad3ea1f8182b530.png" alt="image" data-base62-sha1="9yfUKzYqu1Or02W2WjkYYBaCZCU" width="640" height="484"><br>
As you can see, there is no file extension. But the files are DICOM files from an Optima MR360 (as seen in a hexadecimal version of one of a DICOM files).</p>
<p>I’m trying to load those files in Slicer 3D.</p>
<p><strong>First question :</strong> Can I load all the SE1, SE2, SE3, SE4, … SE8 folders, or should I load only one ?</p>
<p>When loading just one file by dragging and dropping the first file, it’s ok :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c435ce301996f8598d5b679b6753c59071268d3f.png" data-download-href="/uploads/short-url/rZKRqJ7lOgXlaOMVzHqFvok34Z1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c435ce301996f8598d5b679b6753c59071268d3f_2_690x403.png" alt="image" data-base62-sha1="rZKRqJ7lOgXlaOMVzHqFvok34Z1" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c435ce301996f8598d5b679b6753c59071268d3f_2_690x403.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c435ce301996f8598d5b679b6753c59071268d3f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c435ce301996f8598d5b679b6753c59071268d3f.png 2x" data-dominant-color="F1F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">897×524 62 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I choose the “Show options” and deselect “Single file”, then I press OK.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0c844271e018981413f8965f378ae05ada698ba.png" data-download-href="/uploads/short-url/rvqK32OT0fRmGguLAS0u42X1CEa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0c844271e018981413f8965f378ae05ada698ba.png" alt="image" data-base62-sha1="rvqK32OT0fRmGguLAS0u42X1CEa" width="690" height="190" data-dominant-color="F8F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">743×205 7.88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I choose the “Volumes” module, and display “Volume information”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c03ee82b75e40fb0ff72b3c000aa8cf549a6cf3b.png" data-download-href="/uploads/short-url/rqGs0AvaRKZxyGubAkIEVMMSHoL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c03ee82b75e40fb0ff72b3c000aa8cf549a6cf3b.png" alt="image" data-base62-sha1="rqGs0AvaRKZxyGubAkIEVMMSHoL" width="541" height="500" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">607×560 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<strong>Second question :</strong> Do I need to chance something on this “Volumes” module ?</p>
<p>I try next to use the “Vector to scalar” module, but I really don’t know if it’s necessary, or what to do (the input vector volume dropdown list is empty).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e32a89236efed725652342ff0fc78737e170ca5d.png" alt="image" data-base62-sha1="wpBw7AhBwOi0HvwBSCzJapDSHp3" width="622" height="380"></p>
<p>If I choose the “Volume rendering” module, and playing with “Preset” dropdown list, I obtain (after clicking on the closed eye next to “Volume :” label) a king of 3D, but that’s not a head…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f034372846f4698af80ce112436de1b0caede1e7.png" data-download-href="/uploads/short-url/ygWsLESUz8q8rqqoVtUR6ymW91R.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f034372846f4698af80ce112436de1b0caede1e7_2_690x171.png" alt="image" data-base62-sha1="ygWsLESUz8q8rqqoVtUR6ymW91R" width="690" height="171" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f034372846f4698af80ce112436de1b0caede1e7_2_690x171.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f034372846f4698af80ce112436de1b0caede1e7_2_1035x256.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f034372846f4698af80ce112436de1b0caede1e7.png 2x" data-dominant-color="A1A0A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1359×338 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Question 3 :</strong> Can you help me to have a good result with the CDRom datas ?</p>
<p>Cordially</p>
<p>Janolap1</p>

---

## Post #2 by @cpinter (2020-05-07 18:41 UTC)

<p>What you have is DICOM data, so you will need to import it (the folder PA1) to the DICOM database using the DICOM browser and load from there.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#Data_import_and_loading" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#Data_import_and_loading</a></p>

---

## Post #3 by @janolap1 (2020-05-07 20:23 UTC)

<p>Thank you <a class="mention" href="/u/cpinter">@cpinter</a> !<br>
I think there is a issue with the DICOM Browser.<br>
I don’t know where is the option to “Show DICOM browser”.</p>
<p>And when I read the error windows, there is a critical error when launching the DICOM module :</p>
<pre><code>Traceback (most recent call last):
File "C:/Program Files/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOM.py", line 360, in setup
self.detailsPopup = self.getSavedDICOMDetailsWidgetType()()
File "C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 1015, in __init__
super(DICOMDetailsWindow, self).__init__(dicomBrowser, parent)
File "C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 984, in __init__
DICOMDetailsBase.__init__(self, dicomBrowser)
File "C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 93, in __init__
self.promptForDatabaseDirectory()
File "C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 540, in promptForDatabaseDirectory
os.makedirs(databaseDirectory)
File "C:/Program Files/Slicer 4.10.2/bin/../lib/Python/Lib\os.py", line 157, in makedirs
mkdir(name, mode)
WindowsError: [Error 2] Le fichier sp�cifi� est introuvable: u'C:/Users/jean/Documents\\SlicerDICOMDatabase'
Traceback (most recent call last):
File "C:/Program Files/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOM.py", line 301, in enter
self.onOpenDetailsPopup()
File "C:/Program Files/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOM.py", line 401, in onOpenDetailsPopup
if not isinstance(self.detailsPopup, self.getSavedDICOMDetailsWidgetType()):
AttributeError: DICOMWidget instance has no attribute 'detailsPopup'
Traceback (most recent call last):
File "C:/Program Files/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOM.py", line 234, in dropEvent
dicomWidget.detailsPopup.dicomBrowser.importDirectories(self.directoriesToAdd)
AttributeError: DICOMWidget instance has no attribute 'detailsPopup'
</code></pre>
<p>I think I have a bug ? isn’t it ?</p>
<p>Can you help me once again ?</p>
<p>Thank you</p>
<p>janolap1</p>

---

## Post #4 by @lassoan (2020-05-07 22:08 UTC)

<p>I would recommend to try with latest Slicer Preview Release, as it contains fixes for many common issues with the DICOM browser.</p>

---

## Post #5 by @janolap1 (2020-05-11 12:03 UTC)

<p>Thank you !<br>
No problem with the preview release.</p>

---
