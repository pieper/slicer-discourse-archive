---
topic_id: 31221
title: "Could Not Load Series As A Scalar Volume"
date: 2023-08-18
url: https://discourse.slicer.org/t/31221
---

# Could not load series as a scalar volume

**Topic ID**: 31221
**Date**: 2023-08-18
**URL**: https://discourse.slicer.org/t/could-not-load-series-as-a-scalar-volume/31221

---

## Post #1 by @lvdw (2023-08-18 14:13 UTC)

<p>Operating system: Mac OS<br>
Slicer version: 5.2.2<br>
Expected behavior: Load DICOM series as a scalar volume<br>
Actual behavior: Does’nt load anything</p>
<p>So I have a MRI DWI dicom series for which a mask was created (saved as a DICOM series) using HOROS, so I only have these exported series, not the original ones. They seem to load without any problem in Horos. I would like to load the series and the mask in slicer, but it keeps throwing errors. From previous posts that were comparable I tried to install the extensions SlicerDMRI and SlicerDcm2nii but it doesn’t solve the problem, just adds more lines of failed attempts to the error. I tried loading it outside the DCM reader, this was unsuccessful. I tried the DICOM patcher, didn’t work.</p>
<p>The error as a pop-up: Could not load: 100: FU DWI as a Scalar Volume</p>
<p>And in the python console:<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-31382/SlicerDcm2nii/lib/Slicer-5.2/qt-scripted-modules/Dcm2niixPlugin.py”, line 119, in examineFiles<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/Extensions-31382/SlicerDcm2nii/lib/Slicer-5.2/qt-scripted-modules/Resources/bin/dcm2niix’, ‘-n’, ‘-1’, ‘-s’, ‘y’, ‘-f’, ‘%p_%t_%s’, ‘-i’, ‘y’, ‘-o’, ‘/private/var/folders/4q/3ch44qxj07x_zvqj8yp635nc0000gn/T/Slicer-username/tmp5vfeq8vm’, ‘/private/var/folders/4q/3ch44qxj07x_zvqj8yp635nc0000gn/T/Slicer-username/tmp5vfeq8vm/input-dicom-files.txt’]’ returned non-zero exit status 1.</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-5.2/qt-scripted-modules/DICOMLib/DICOMUtils.py”, line 748, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
File “/Applications/Slicer.app/Contents/Extensions-31382/SlicerDcm2nii/lib/Slicer-5.2/qt-scripted-modules/Dcm2niixPlugin.py”, line 29, in examine<br>
loadables += self.examineFiles(files)<br>
File “/Applications/Slicer.app/Contents/Extensions-31382/SlicerDcm2nii/lib/Slicer-5.2/qt-scripted-modules/Dcm2niixPlugin.py”, line 121, in examineFiles<br>
logging.debug(“Failed to examine files using dcm2niix: {0}”.format(e.message))<br>
AttributeError: ‘CalledProcessError’ object has no attribute ‘message’<br>
[Python] DICOM Plugin failed: ‘CalledProcessError’ object has no attribute ‘message’<br>
[VTK] Unhandled PixelFormat: SamplesPerPixel    :1<br>
[VTK] BitsAllocated      :15<br>
[VTK] BitsStored         :15<br>
[VTK] HighBit            :14<br>
[VTK] PixelRepresentation:1<br>
[VTK] ScalarType found   :UNKNOWN<br>
[VTK] Algorithm vtkITKArchetypeImageSeriesScalarReader(0x7fccd2f0fe30) returned failure for request: vtkInformation (0x6000037c2d80)<br>
[VTK]   Debug: Off<br>
[VTK]   Modified Time: 238615<br>
[VTK]   Reference Count: 1<br>
[VTK]   Registered Events: (none)<br>
[VTK]   Request: REQUEST_INFORMATION<br>
[VTK]   ALGORITHM_AFTER_FORWARD: 1<br>
[VTK]   FORWARD_DIRECTION: 0<br>
[Python] Could not read scalar volume using GDCM approach.  Error is: FileFormatError<br>
[VTK] Unhandled PixelFormat: SamplesPerPixel    :1<br>
[VTK] BitsAllocated      :15<br>
[VTK] BitsStored         :15<br>
[VTK] HighBit            :14<br>
[VTK] PixelRepresentation:1<br>
[VTK] ScalarType found   :UNKNOWN<br>
[VTK] Algorithm vtkITKArchetypeImageSeriesScalarReader(0x7fcd155b3680) returned failure for request: vtkInformation (0x6000034f8f00)<br>
[VTK]   Debug: Off<br>
[VTK]   Modified Time: 238710<br>
[VTK]   Reference Count: 1<br>
[VTK]   Registered Events: (none)<br>
[VTK]   Request: REQUEST_INFORMATION<br>
[VTK]   ALGORITHM_AFTER_FORWARD: 1<br>
[VTK]   FORWARD_DIRECTION: 0<br>
[Python] Could not read scalar volume using DCMTK approach.  Error is: FileFormatError<br>
[Python] Could not load: 100: FU DWI as a Scalar Volume</p>
<p>The metadata:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>[0008,0005]</th>
<th>SpecificCharacterSet</th>
<th>ISO_IR 100</th>
<th>CS</th>
<th>10</th>
</tr>
</thead>
<tbody>
<tr>
<td>[0008,0008]</td>
<td>ImageType</td>
<td>ORIGINAL</td>
<td>CS</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0016]</td>
<td>SOPClassUID</td>
<td>1.2.840.10008.5.1.4.1.1.4</td>
<td>UI</td>
<td>26</td>
</tr>
<tr>
<td>[0008,0018]</td>
<td>SOPInstanceUID</td>
<td>1.2.826.0.1.3680043.8.498.38959781551086868487592517682093160443</td>
<td>UI</td>
<td>64</td>
</tr>
<tr>
<td>[0008,0020]</td>
<td>StudyDate</td>
<td>20010101</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0021]</td>
<td>SeriesDate</td>
<td>20010101</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0022]</td>
<td>AcquisitionDate</td>
<td>20010101</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0030]</td>
<td>StudyTime</td>
<td>120000</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0031]</td>
<td>SeriesTime</td>
<td>120000</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0032]</td>
<td>AcquisitionTime</td>
<td>120000</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0050]</td>
<td>AccessionNumber</td>
<td>0</td>
<td>SH</td>
<td>2</td>
</tr>
<tr>
<td>[0008,0060]</td>
<td>Modality</td>
<td>MR</td>
<td>CS</td>
<td>2</td>
</tr>
<tr>
<td>[0008,0070]</td>
<td>Manufacturer</td>
<td>StrokeCenter</td>
<td>LO</td>
<td>20</td>
</tr>
<tr>
<td>[0008,1030]</td>
<td>StudyDescription</td>
<td>FU DWI</td>
<td>LO</td>
<td>6</td>
</tr>
<tr>
<td>[0008,103e]</td>
<td>SeriesDescription</td>
<td>FU DWI</td>
<td>LO</td>
<td>6</td>
</tr>
<tr>
<td>[0010,0010]</td>
<td>PatientName</td>
<td>UHL071</td>
<td>PN</td>
<td>6</td>
</tr>
<tr>
<td>[0010,0020]</td>
<td>PatientID</td>
<td>UHL071</td>
<td>LO</td>
<td>6</td>
</tr>
<tr>
<td>[0010,0030]</td>
<td>PatientBirthDate</td>
<td>20010101</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0010,0040]</td>
<td>PatientSex</td>
<td>M</td>
<td>CS</td>
<td>2</td>
</tr>
<tr>
<td>[0018,0020]</td>
<td>ScanningSequence</td>
<td>RM</td>
<td>CS</td>
<td>2</td>
</tr>
<tr>
<td>[0018,0021]</td>
<td>SequenceVariant</td>
<td>NONE</td>
<td>CS</td>
<td>4</td>
</tr>
<tr>
<td>[0018,0050]</td>
<td>SliceThickness</td>
<td></td>
<td>DS</td>
<td>0</td>
</tr>
<tr>
<td>[0018,5100]</td>
<td>PatientPosition</td>
<td>HFS</td>
<td>CS</td>
<td>4</td>
</tr>
<tr>
<td>[0020,000d]</td>
<td>StudyInstanceUID</td>
<td>1.2.826.0.1.3680043.8.498.55099949773984100432982975104017035658</td>
<td>UI</td>
<td>64</td>
</tr>
<tr>
<td>[0020,000e]</td>
<td>SeriesInstanceUID</td>
<td>1.2.826.0.1.3680043.8.498.75684090443619204850010177854450728722</td>
<td>UI</td>
<td>64</td>
</tr>
<tr>
<td>[0020,0011]</td>
<td>SeriesNumber</td>
<td>100</td>
<td>IS</td>
<td>4</td>
</tr>
<tr>
<td>[0020,0013]</td>
<td>InstanceNumber</td>
<td>38</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0020,0032]</td>
<td>ImagePositionPatient</td>
<td>[3] -100.0, -100.0, 14.0</td>
<td>DS</td>
<td>18</td>
</tr>
<tr>
<td>[0020,0037]</td>
<td>ImageOrientationPatient</td>
<td>[6] 1.0, 0.0, 0.0, 0.0, 1.0, 0.0</td>
<td>DS</td>
<td>24</td>
</tr>
<tr>
<td>[0020,0052]</td>
<td>FrameOfReferenceUID</td>
<td>1.2.826.0.1.3680043.8.498.25150985547740653771167800120409132909</td>
<td>UI</td>
<td>64</td>
</tr>
<tr>
<td>[0028,0002]</td>
<td>SamplesPerPixel</td>
<td>1</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0004]</td>
<td>PhotometricInterpretation</td>
<td>MONOCHROME2</td>
<td>CS</td>
<td>12</td>
</tr>
<tr>
<td>[0028,0010]</td>
<td>Rows</td>
<td>512</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0011]</td>
<td>Columns</td>
<td>512</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0030]</td>
<td>PixelSpacing</td>
<td>[2] 0.44726562, 0.44726562</td>
<td>DS</td>
<td>22</td>
</tr>
<tr>
<td>[0028,0100]</td>
<td>BitsAllocated</td>
<td>15</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0101]</td>
<td>BitsStored</td>
<td>15</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0102]</td>
<td>HighBit</td>
<td>16</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0103]</td>
<td>PixelRepresentation</td>
<td>1</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,1052]</td>
<td>RescaleIntercept</td>
<td>0.0</td>
<td>DS</td>
<td>4</td>
</tr>
<tr>
<td>[0028,1053]</td>
<td>RescaleSlope</td>
<td>1.0</td>
<td>DS</td>
<td>4</td>
</tr>
<tr>
<td>[7fe0,0010]</td>
<td>PixelData</td>
<td>0000</td>
<td>OW</td>
<td>524288</td>
</tr>
</tbody>
</table>
</div><p>I have an entire dataset with this same problem. Any suggestions?</p>

---

## Post #2 by @lvdw (2023-08-18 14:43 UTC)

<p>I noticed the SliceThickness tag had None as value, so I set it to 3 (which I checked with ImagePositionPatient, but this didn’t solve the problem</p>

---

## Post #3 by @pieper (2023-08-18 16:00 UTC)

<p>Be sure to check the suggestions here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---

## Post #4 by @lvdw (2023-08-18 16:58 UTC)

<p>Thank you for the reply but I think I tried everything on that page already. Or was there something specific you would suggest based on the errors? The only thing I didn’t post already above that was in the error logs was this:</p>
<p>DICOMTID1500PluginClass : Using cached files</p>
<p>[‘/Applications/Slicer.app/Contents/Extensions-31382/SlicerDcm2nii/lib/Slicer-5.2/qt-scripted-modules/Resources/bin/dcm2niix’, ‘-n’, ‘-1’, ‘-s’, ‘y’, ‘-f’, ‘%p_%t_%s’, ‘-i’, ‘y’, ‘-o’, ‘/private/var/folders/4q/3ch44qxj07x_zvqj8yp635nc0000gn/T/Slicer-username/tmp2sdb7xa1’, ‘/private/var/folders/4q/3ch44qxj07x_zvqj8yp635nc0000gn/T/Slicer-username/tmp2sdb7xa1/input-dicom-files.txt’]</p>
<p>Compression will be faster with ‘pigz’ installed <a href="http://macappstore.org/pigz/" class="inline-onebox" rel="noopener nofollow ugc">Install pigz on Mac OSX - Mac App Store</a></p>
<p>Chris Rorden’s dcm2niiX version v1.0.20230210 (JP2:OpenJPEG) (JP-LS:CharLS) Clang10.0.0 x86-64 (64-bit MacOS)</p>
<p>Found 50 files in ‘/private/var/folders/4q/3ch44qxj07x_zvqj8yp635nc0000gn/T/Slicer-username/tmp2sdb7xa1/input-dicom-files.txt’</p>
<p>Found 50 DICOM file(s)</p>
<p>Unable to determine slice thickness: please check voxel size (was printed 50 times)</p>
<p>Warning: Unable to determine manufacturer (0008,0070), so conversion is not tuned for vendor.</p>
<p>Unsupported DICOM bit-depth 15 with 1 samples per pixel</p>
<p>But I’m not sure what I should do with this, if I search it I can’t find it. My apologies is a trivial problem or already answered problem but I’m rather new to slicer and can’t find the solution.</p>

---

## Post #5 by @lassoan (2023-08-18 20:31 UTC)

<aside class="quote no-group" data-username="lvdw" data-post="4" data-topic="31221">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/a6a055/48.png" class="avatar"> lvdw:</div>
<blockquote>
<p>Unsupported DICOM bit-depth 15 with 1 samples per pixel</p>
</blockquote>
</aside>
<p>This seems to be the issue that makes all three, commonly used, independently developed DICOM readers (GDCM, DCMTK, dcm2niix) fail to read the image.</p>
<p>Most likely that HOROS created an invalid image, but at least so “special” that none of the commmonly used DICOM toolkits support it. If you upload anonymized files somewhere and post the link here then we can have a look.</p>
<p>If you want to save a binary mask then currently, the most appropriate DICOM format for that is Segmentation information object. I would recommend to request HOROS developers to support this information object type and use that for saving your mask.</p>

---

## Post #6 by @lvdw (2023-08-21 12:01 UTC)

<p>If you would be willing to have a look at it that would be really helpful.<br>
You can find a test series here: <a href="https://www.dropbox.com/sh/2ikxa1ycp5im6z1/AABH336FTK_Zvr62_oNJZPxYa?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - test_dicom - Simplify your life</a></p>

---
