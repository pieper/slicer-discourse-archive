# Import of registration DICOM files

**Topic ID**: 368
**Date**: 2017-05-24
**URL**: https://discourse.slicer.org/t/import-of-registration-dicom-files/368

---

## Post #1 by @edumeilan (2017-05-24 11:44 UTC)

<p>Operating system: Windows 7 Profesional 64 bits<br>
Slicer version: 4.6.2</p>
<p>Hi everyone,</p>
<p>I’m trying to use a DICOM registration object but I can’t even load it. I made a registration (in fact, two of them; one is rigid and the other one deformable) using Varian Eclipse module and I want to use this transformation for other purposes. What I really want right now is to change the format to a vector field or something like that.<br>
If I try to import this object with the DICOM module it says “Could not load x as a scalar volume”. If I try to load it as data it doesn’t give me any message but it doesn’t load it.</p>
<p>Is there any way I could import a registration in DICOM format?</p>
<p>Thank you very much,</p>
<p>Best regards,</p>
<p>Edu</p>

---

## Post #2 by @lassoan (2017-05-24 11:44 UTC)

<p>Use the latest nightly version of Slicer and install SlicerRT extension.</p>

---

## Post #3 by @edumeilan (2017-05-24 11:59 UTC)

<p>Thank you very much! I’ll try as soon as I can</p>

---

## Post #4 by @edumeilan (2017-05-29 08:55 UTC)

<p>Hi!<br>
I’ve been trying to download the slicerRT extension, but I have some<br>
problems when doing from my institution. Is there any posibility of<br>
downloading from the web and not from the extension manager? I could then<br>
install it from the file. I’ve benn looking in several webs (<br>
<a href="http://slicer.kitware.com/midas3" rel="nofollow noopener">http://slicer.kitware.com/midas3</a>, <a href="https://github.com/SlicerRt/SlicerRT" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT</a>…)<br>
but I can’t find any zip, tar or similar file to download. Could you help<br>
me, please?</p>
<p>Sorry for disturbing you.<br>
Best regards,</p>
<p>Edu</p>

---

## Post #5 by @lassoan (2017-05-29 12:51 UTC)

<p>See detailed instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_download_an_extension_package.3F">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#How_to_manually_download_an_extension_package.3F</a></p>

---

## Post #6 by @stephan (2018-09-21 14:03 UTC)

<p>Hi everybody,<br>
I have the same issue as the OP, but I have installed the latest SlicerRT version (0.18.0). Slicer is 4.9. nightly 2018-09-10.<br>
I have two DICOM registration objects, exported from MIM 6.8.3.<br>
The rigid registration registers a CT to an MRI, and the deformable one registers a CT to a follow-up CT (accounting for animal growth in between).<br>
They import into the DICOM database nicely, but when I try to load either registration object, a warning is triggered by the Scalar Volume Reader: “Reference image in series does not contain geometry information. Please use caution.”<br>
When I proceed with “load anyway”, an error is thrown “Could not load 0: Image registration as a scalar volume”<br>
When I uncheck the DICOMScalarVolumePlugin reader and leave only the DicomRtImportExportPlugin checked in the DICOM browser, no warning is triggered but nothing is loaded either.</p>
<p>Any hints at what I am missing are greatly appreciated.</p>
<p>Thank you<br>
Stephan</p>

---

## Post #7 by @cpinter (2018-09-21 14:27 UTC)

<p>This warning is rarely a cause for concern. The threshold for giving this warning is very low, so you can usually ignore it I think.</p>
<p>FYI I’m not sure how well deformable SROs are handler right now, but we’ll work on it soon in SlicerRT.</p>

---

## Post #8 by @fedorov (2018-09-21 14:34 UTC)

<p>I think the issue is that ScalarVolumePlugin should not even examine the registration object. If it loads correctly when you uncheck ScalarVolumePlugin, I would not worry about anything else. ScalarVolumePlugin needs to be fixed to ignore this IOD.</p>

---

## Post #9 by @stephan (2018-09-21 14:39 UTC)

<p>Thank you for the swift reply.<br>
It works now.<br>
For the record: For some reason, DicomSroPlugin was unchecked from the beginning in my DICOM browser.<br>
And after getting the ScalarVolume warning for the first time, i unchecked all other handlers as well, except for DicomRtImportExport (which I thought would handle REGs), not being aware of that the SroPlugin is the one I would actually need. Only after Csaba referred to “deformable SROs” I realized that this acronym must stand for registration objects. Since I re-activated the DicomSrcoPlugin handler, everything works fine without warnings and with the registrations showing up in the scene hierarchy.</p>
<p>Thank you all for your great work with Slicer.<br>
Stephan</p>

---

## Post #10 by @fedorov (2018-09-21 15:05 UTC)

<aside class="quote no-group" data-username="stephan" data-post="9" data-topic="368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>Only after Csaba referred to “deformable SROs” I realized that this acronym must stand for registration objects.</p>
</blockquote>
</aside>
<p>I have to admit, I do not know what “SRO” stands for (in this context)!</p>

---

## Post #11 by @cpinter (2018-09-21 15:06 UTC)

<p>DICOM Spatial Registration Object</p>

---

## Post #12 by @cpinter (2018-09-21 15:08 UTC)

<aside class="quote no-group" data-username="stephan" data-post="9" data-topic="368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>DicomSroPlugin was unchecked from the beginning</p>
</blockquote>
</aside>
<p>This is strange. I’ll look into this.</p>
<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>ScalarVolumePlugin needs to be fixed to ignore this IOD.</p>
</blockquote>
</aside>
<p>I’m not sure if the warning was thrown from the SRO. It gets thrown many times from valid scalar volumes as well. However in general it wouldn’t hurt making it ignore special IOD types.</p>

---

## Post #13 by @pieper (2018-09-21 16:06 UTC)

<p>If the plugin recognizes the SOPClass then it should return a very high confidence so that it is selected by default.  The ScalarVolume plugin returns medium confidence for for pretty much anything so that it can be the catch-all for anything not recognized by specialized readers.  So in this case it’s the SRO plugin that should be fixed.</p>

---

## Post #14 by @cpinter (2018-09-21 16:27 UTC)

<p>The SRO plugin does the same, not sure what is there to fix. Again I think there is a misunderstanding and the ScalarVolume plugin actually never tries to load SRO and vice versa, SRO never tries to load a scalar volume, but there is a usual geometry warning for ScalarVolume plugin trying to load a scalar volume while everything is loaded as expected. <a class="mention" href="/u/stephan">@stephan</a> needs to confirm this, but if my hunch is right then we’re good.</p>

---

## Post #15 by @pieper (2018-09-21 17:03 UTC)

<p>Good - if both SRO and ScalarVolume plugins are enabled then SRO plugin should recognize the sop class and return highest priority and be selected for loading.</p>

---

## Post #16 by @stephan (2018-09-21 18:14 UTC)

<p>Yes, I think we are good here. The only scenario where a warning was displayed (and the import eventually failed if I clicked “load anyway”) was when the SRO plugin was inactive. It seems that the scalar plugin works as a sort of scavenger, trying to import any class which is not imported by some more specific plugin. As soon as I activated the checkbox for the SRO plugin, the scalar plugin threw no more warning messages.<br>
Sorry for all the confusion.</p>

---

## Post #17 by @pieper (2018-09-21 18:43 UTC)

<p>Thanks for checking and clearing this up.</p>
<aside class="quote no-group" data-username="stephan" data-post="16" data-topic="368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>It seems that the scalar plugin works as a sort of scavenger, trying to import any class which is not imported by some more specific plugin.</p>
</blockquote>
</aside>
<p>Yes, my rationale for that is that there are so many poorly formatted dicom files out there and so many heuristics and fixes that are hard-coded into the ITK/GDCM/DCMTK layers that we may as well give it a try instead of just giving up (or before giving up).</p>

---

## Post #18 by @lassoan (2018-09-23 02:34 UTC)

<p>Keeping scalar volume reader as a catch-all makes sense, but when scalar volume reader is used as a last resort, it could be nicer to show a more generic error message “Could not load 0: Image registration" (do not mention scalar volume) and maybe add some basic information (imaging modality, SOP class UID, etc.) that may be useful for debugging.</p>

---

## Post #19 by @hannahrhea (2018-12-17 20:30 UTC)

<p>I have a similar query. I want to import the DICOM registration objects, exported from MIM 6.8.7. The cooresponding DICOM images came in without any problems. However the registration objects did not and I got the following error. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df66eee76559b67f8e26fe602fd289947cc2a27d.png" alt="image" data-base62-sha1="vSj0zNCuxROzQFn2ZRP1T49bBgh" width="591" height="421"></p>
<p>Slicer has caught an internal error.</p>
<p>You may be able to continue from this point, but results are undefined.</p>
<p>Suggested action is to save your work and restart.</p>
<p>If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="noopener nofollow ugc">http://slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: d:\d\p\slicer-480-package\itkv4\modules\io\imagebase\include\itkImageFileReader.hxx:143:<br>
Could not create IO object for reading file C:/Users/hmthomas/Desktop/New folder/2016-08__Studies/FLARE005_9599-FLARE005_REG_2016-08-15_152550_CT.THERAPY.PLAN.RAD.ON_FDG.PET.fusion.pretx_n1__00000/2.16.840.1.114362.1.6.6.4.16526.10113205933.441938047.913.5384.dcm<br>
Tried to create one of the following:<br>
NiftiImageIO<br>
NrrdImageIO<br>
GiplImageIO<br>
JPEGImageIO<br>
GDCMImageIO<br>
BMPImageIO<br>
LSMImageIO<br>
PNGImageIO<br>
TIFFImageIO<br>
VTKImageIO<br>
StimulateImageIO<br>
BioRadImageIO<br>
MetaImageIO<br>
MRCImageIO<br>
MINCImageIO<br>
MGHImageIO<br>
MRMLIDImageIO<br>
HDF5ImageIO<br>
GE4ImageIO<br>
GE5ImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.</p>
<p>How can I resolve this problem?<br>
Thanks,<br>
Hannah</p>

---

## Post #20 by @lassoan (2018-12-17 22:02 UTC)

<p>You need to install SlicerRT extension and load DICOM data using DICOM module (drag-and-drop the parent folder to the application window and not individual files).</p>
<p>We are actively working on improving DICOM SRO import/export compatibility with mim. If you find any issues then let us know and if possible, share your data sets (make sure they do not contain patient information).</p>

---

## Post #21 by @labixin (2019-05-09 11:18 UTC)

<p>Hi everyone,<br>
I am now using Slicer 4.11.0 and I wonder if I could export deformable transform (to mim) using “DICOM Registration Export”. Besides, I have a (deformable) warp which was modified and I wonder if I can import to Slicer and then convert to DICOM format? The warp (.txt) is shown below. Your help is highly appreciated!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59807e4c1618e73a2ad84ab056b6cd394d210956.png" alt="warp" data-base62-sha1="cLLN13Z2eLRT1YhXjZ5LFoktgcm" width="401" height="240"><br>
Crayon</p>

---

## Post #22 by @cpinter (2019-05-09 13:36 UTC)

<p>Hi!</p>
<p>We’re expecting deformable SRO export to be available very soon, there is just a final piece missing from the implementation. You can track progress here: <a href="https://github.com/SlicerRt/SlicerRT/issues/41" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/issues/41</a><br>
Once you see that the ticket is closed, download a nightly Slicer, install SlicerRT and try exporting the deformable transform.</p>
<p>Thanks for the patience!</p>

---

## Post #23 by @labixin (2019-05-20 17:06 UTC)

<p>Hi,</p>
<p>Thanks for your reply. I have downloaded the most recently nightly Slicer (Slicer 4.11.0-2019-05-19) but I still can’t export the deformable transform (done in “General Registration (BRAINS)” module)? I have succeeded in exporting linear transform and got the SRO (.dcm) which I could import to mim software as REG. Is there any wrong with my Slicer version? Your help is highly appreciated.</p>
<p>Crayon</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28f3cdfd260677c8193ec57f12639334bbab7f1c.png" alt="01" data-base62-sha1="5QhrLzg5hwHVvQv7LTX51iVFY1C" width="501" height="441"></p>

---
