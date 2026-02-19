---
topic_id: 13281
title: "Slicer 3D Dicom Import Issues With Pydicom Dicom Files"
date: 2020-09-01
url: https://discourse.slicer.org/t/13281
---

# Slicer 3D DICOM Import Issues with pydicom DICOM files

**Topic ID**: 13281
**Date**: 2020-09-01
**URL**: https://discourse.slicer.org/t/slicer-3d-dicom-import-issues-with-pydicom-dicom-files/13281

---

## Post #1 by @jdp (2020-09-01 16:23 UTC)

<p>I am trying to develop a DICOM file from scratch (using pydicom) that can be imported into slicer 3D. This DICOM from scratch can be read by other programs with no issue. Although the DICOM I can generate has a Patient Name, Patient ID, etc. - slicer doesn’t show in the DICOM database.</p>
<p>To further highlight the issue, in the pydicom code (below) I have “ds” as the dicom data that I’m trying to create and “ds_in” as the read in data of the original dicom. If I set ds=ds_in (committed out currently in code below) and make modifications then the pydicom can be read by slicer (not too surprising). Furthermore, if I delete all unwanted dicom tags (so just the specific dicoms I’m manually writing from ds_in to ds in the code current are present), the dicom file still has no issue as long as I set ds=ds_in after “file_meta = FileMetaDataset()”. It is the minute that I comment out ds=ds_in but try to pass in the ds_in tags directly to the ds tags on a tag by tag bases then that file does not work. In other words, if I manually try to force each and every ds_in file meta dataset from the ds_in to the ds variable, I have an issue.</p>
<p>It seems the “file_meta = FileMetaDataset()” is key here in which manually rewriting it, i.e., setting the ds_in tags to the ds file_meta tag group, is not the same as copying the file meta dataset from the original dicom? I am also making sure I’m being consistent with my image datatype - you can see I set my modified image to a uint16 at the end.</p>
<p>Are there any suggestions or example codes to write a basic dicom from scratch with pydicom that is Slicer 3D compatible?</p>
<pre><code class="lang-python">import pydicom
from pydicom.dataset import FileDataset, FileMetaDataset

ds_in = pydicom.dcmread(ReadPath1)

#
file_meta = FileMetaDataset()
file_meta.FileMetaInformationGroupLength = ds_in.file_meta.FileMetaInformationGroupLength
file_meta.FileMetaInformationVersion     = ds_in.file_meta.FileMetaInformationVersion #b'\x01\x00'
file_meta.MediaStorageSOPClassUID        = ds_in.file_meta.MediaStorageSOPClassUID
file_meta.MediaStorageSOPInstanceUID     = ds_in.file_meta.MediaStorageSOPInstanceUID
file_meta.TransferSyntaxUID              = ds_in.file_meta.TransferSyntaxUID
file_meta.ImplementationClassUID         = ds_in.file_meta.ImplementationClassUID #pydicom.uid.UID(pydicom.uid.PYDICOM_IMPLEMENTATION_UID) #ds_in.file_meta.ImplementationClassUID
file_meta.ImplementationVersionName      = ds_in.file_meta.ImplementationVersionName #pydicom.uid.UID(pydicom.uid.PYDICOM_IMPLEMENTATION_UID).name

FileName_TMP = tempfile.NamedTemporaryFile(suffix='.dcm').name
ds = FileDataset(FileName_TMP, {}, file_meta=file_meta, preamble=b"\0" * 128)

# # Works if I set ds to equal ds_in
# ds_in.remove_private_tags()
# ds = ds_in

ds.StudyInstanceUID          = ds_in.StudyInstanceUID
ds.SeriesInstanceUID         = ds_in.SeriesInstanceUID
ds.SamplesPerPixel           = ds_in.SamplesPerPixel
ds.PhotometricInterpretation = ds_in.PhotometricInterpretation
ds.BitsStored                = ds_in.BitsStored
ds.BitsAllocated             = ds_in.BitsAllocated
ds.HighBit                   = ds_in.HighBit
ds.PixelRepresentation       = ds_in.PixelRepresentation
ds.Rows                      = ds_in.Rows
ds.Columns                   = ds_in.Columns
ds.PixelSpacing              = ds_in.PixelSpacing
ds.InstanceNumber            = ds_in.InstanceNumber
ds.SliceThickness = 2
ds.SpacingBetweenSlices = 15

# Modify image
A = ds_in.pixel_array
from scipy import ndimage
Aavg = ndimage.gaussian_filter(A, 5)
Aedge = ndimage.filters.laplace(A)
A = Aavg + Aedge
A[A &gt; 1000] = 0
A = numpy.uint16(A)

ds.PixelData                 = A.tobytes()
ds.Modality                  = ds_in.Modality
ds.ImagePositionPatient      = ds_in.ImagePositionPatient
ds.ImageOrientationPatient   = ds_in.ImageOrientationPatient

ds.InstanceCreatorUID        = ds_in.InstanceCreatorUID
ds.SpecificCharacterSet      = ds_in.SpecificCharacterSet
ds.ContentDate               = ds_in.ContentDate
ds.ContentTime               = ds_in.ContentTime
ds.PatientName               = ds_in.PatientName
ds.PatientID                 = ds_in.PatientID

pydicom.dataset.validate_file_meta(ds.file_meta, enforce_standard=True)

ds.save_as(WritePath + '/' + WriteFile + '.dcm')
</code></pre>

---

## Post #2 by @pieper (2020-09-01 16:54 UTC)

<p>Did you look in the slicer error log?  I’d expect some diagnostic output.</p>

---

## Post #3 by @jdp (2020-09-01 17:00 UTC)

<p>The first error that pops up is listed as critical and states:</p>
<p>W: DcmItem: Non-standard VR ’ ’ (0a\00) encountered while parsing element (0008,0005), assuming 2 byte length field</p>
<p>W: DcmItem: Non-standard VR ‘IR’ (49\52) encountered while parsing element (5349,5f4f), assuming 4 byte length field</p>
<p>E: DcmElement: Unknown Tag &amp; Data (5349,5f4f) larger (536624) than remaining bytes in file</p>
<p>What is interesting is the element (0008,0005) shows as a VR of CS and a Size of 10 when I open it up with another viewer.</p>

---

## Post #4 by @jdp (2020-09-01 20:28 UTC)

<p>I did get an error (attached it above - not sure if I applied directly to you). However, I am now really stripping down the code (see below) and I’ve gotten the following read error. Any suggestions to get this to work as normal dicom viewers can read and display the image with no issue? Note the image is a randomized intensity image. The error is:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\jdp\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-20\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMBrowser.py”, line 212, in timerCallback<br>
self.promptForExtensions()<br>
File “C:\Users\jdp\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-20\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMBrowser.py”, line 217, in promptForExtensions<br>
extensionsToOffer = self.checkForExtensions()<br>
File “C:\Users\jdp\AppData\Local\NA-MIC\Slicer 4.11.0-2019-12-20\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMBrowser.py”, line 280, in checkForExtensions<br>
instance0 = slicer.dicomDatabase.filesForSeries(series)[0]<br>
IndexError: tuple index out of range</p>
<p>the stripped down code (using pydicom) is:</p>
<p>file_meta = FileMetaDataset()<br>
file_meta.FileMetaInformationGroupLength = int(192)<br>
file_meta.MediaStorageSOPClassUID        = pydicom.uid.generate_uid()<br>
file_meta.MediaStorageSOPInstanceUID     = pydicom.uid.generate_uid()<br>
file_meta.TransferSyntaxUID              = str(‘1.2.840.10008.1.2’) <span class="hashtag">#ds_in</span>.file_meta.TransferSyntaxUID</p>
<p>FileName_TMP = tempfile.NamedTemporaryFile(suffix=’.dcm’).name<br>
ds = FileDataset(FileName_TMP, {}, file_meta=file_meta, preamble=b"\0" * 128)</p>
<p>ds.StudyInstanceUID          = pydicom.uid.generate_uid()<br>
ds.SeriesInstanceUID         = pydicom.uid.generate_uid()<br>
ds.SamplesPerPixel           = int(1)<br>
ds.PhotometricInterpretation = str(‘MONOCHROME2’)<br>
ds.BitsStored                = int(16)<br>
ds.BitsAllocated             = int(16)<br>
ds.HighBit                   = int(15)<br>
ds.PixelRepresentation       = int(0)<br>
ds.Rows                      = int(512)<br>
ds.Columns                   = int(512)<br>
ds.PixelSpacing              = [float(.5), float(.5)]<br>
ds.InstanceNumber            = int(1)<br>
ds.SliceThickness            = int(4)<br>
ds.SpacingBetweenSlices      = int(5)</p>
<h1>Modify image</h1>
<p>A = numpy.uint((numpy.power(2, 16)-1) * numpy.random.rand(512, 512))</p>
<p>ds.PixelData                 = A.tobytes()<br>
ds.Modality                  = str(‘MR’)<br>
ds.ImagePositionPatient      = [float(.5), float(.5), float(.5)]<br>
ds.ImageOrientationPatient   = [float(0), float(0), float(1), float(0), float(0), float(-1)]</p>
<p>ds.InstanceCreatorUID        = pydicom.uid.generate_uid()<br>
ds.PatientName               = str(‘Cheese’)<br>
ds.PatientID                 = str(‘12345667’)</p>
<p>pydicom.dataset.validate_file_meta(ds.file_meta, enforce_standard=True)<br>
ds.save_as(WritePath + ‘/’ + WriteFile + ‘.dcm’)</p>

---

## Post #5 by @pieper (2020-09-01 21:01 UTC)

<aside class="quote no-group" data-username="jdp" data-post="3" data-topic="13281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c6cbf5/48.png" class="avatar"> jdp:</div>
<blockquote>
<p>W: DcmItem: Non-standard VR ’ ’ (0a\00) encountered while parsing element (0008,0005), assuming 2 byte length field</p>
<p>W: DcmItem: Non-standard VR ‘IR’ (49\52) encountered while parsing element (5349,5f4f), assuming 4 byte length field</p>
<p>E: DcmElement: Unknown Tag &amp; Data (5349,5f4f) larger (536624) than remaining bytes in file</p>
</blockquote>
</aside>
<p>I would say these together are problematic.  I’d guess one of the assumptions has led to the wrong bytes being decoded as if they were group,element tags and length entries.</p>
<p>One option would be to get the <a href="http://dclunie.com/dicom3tools/dciodvfy.html">dciodvfy</a> tool and see what it reports.</p>

---

## Post #7 by @jdp (2020-09-01 22:38 UTC)

<p>I ran the tool you suggested for the stripped down pydicom DICOM and it says:</p>
<p>jdp$ ./dcentvfy NewDICOM.dcm<br>
Warning - Unrecognized SOP Class - - so cannot determine information entity of attributes within file &lt;NewDICOM.dcm&gt;</p>
<p>It seems because pydicom made this, the SOP isn’t recognized by the tool you suggested I use. I did have a slight error in the stripped down code with:<br>
file_meta.MediaStorageSOPClassUID = pydicom.uid.generate_uid()<br>
should have been:<br>
file_meta.MediaStorageSOPClassUID = str(‘1.2.840.10008.5.1.4.1.1.7’)</p>
<ul>
<li>but the error is happening after the correction (and the same issue is happening in slicer). Any other suggestions here as I’m at a loss at this point?</li>
</ul>

---

## Post #8 by @pieper (2020-09-02 13:31 UTC)

<aside class="quote no-group" data-username="jdp" data-post="4" data-topic="13281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c6cbf5/48.png" class="avatar"> jdp:</div>
<blockquote>
<p>file_meta.MediaStorageSOPClassUID = pydicom.uid.generate_uid()</p>
</blockquote>
</aside>
<p>This is probably the issue - SOPClassUIDs are a set of pre-defined constants that are part of the dicom standard but here you are assigning a random number so Slicer doesn’t know what to do with it.  Since you set the modality to MR you should use the MRImage.</p>
<p>If you are still having trouble you can try dcmdump from dcmtk and compare the values it shows to what you expect to see based on your pydicom code.</p>

---

## Post #9 by @jdp (2020-09-02 17:18 UTC)

<p>Your suggestion of using dcmdump was exactly what I needed to find my issue. I started making my pydicom code worse as I was trying to find the original issue. The SOP error you highlighted was a side error I put in as I was debugging by accident. I’ve now isolated my underlining issue and understand you need to embed the SOP and transfer syntax in both the meta and the general data sections of the pydicom write dicom code (furthermore the transfer syntax can be different between the meta and the general data). I apricate your patience and guidance, Steve.</p>

---
