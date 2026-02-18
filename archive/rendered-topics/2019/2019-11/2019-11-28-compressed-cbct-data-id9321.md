# Compressed CBCT Data

**Topic ID**: 9321
**Date**: 2019-11-28
**URL**: https://discourse.slicer.org/t/compressed-cbct-data/9321

---

## Post #1 by @manjula (2019-11-28 11:22 UTC)

<p>I was today using CBCT data exported as dcm multiframe images of patients.<br>
I used 3D Slicer to import the .dcm file and when it was importing it gave a warning  in advance mode saying " Multi-frame image. If slice orientation or spaicing is non-uniform then the image may be displayed incorretly. Use with caution"<br>
And after importing anyway when i use volume rendering to visualize the bones,  i realized the rendered image is scaled or compressed or skewed i dont know what exactly but  “not proper”.</p>
<p>So i went back and used gdcmconv to uncompressed the .dcm file and used the uncompressed dcm file in the 3D slicer. Then the volume rendering was accurate.</p>
<p>Why is this ? Is there a way of properly importing the compressed cbct data  directly to 3D Slicer without using gdcmconv and cli ?</p>
<p>I cannot share the screenshots due to i did not seek permission from the patient to use the data in public.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2019-11-28 12:31 UTC)

<p>This information is not enough to even guess what could have gone wrong. Follow instructions in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">DICOM FAQ</a> and if it doesn’t solve the problems then let us know.</p>

---

## Post #3 by @manjula (2019-11-28 12:34 UTC)

<p>Thank you for the quick reply Prof Iassoan.  I will go through it and let you know and come back with more details.</p>
<p>And just now i figure out there is a x3 time scaling added when i uncompressed the dcm with gdcmconv command when i measured the distances.</p>
<p>Is there a way to scale it back or something is horrible wrong from the onset ?</p>

---

## Post #4 by @manjula (2019-11-28 12:50 UTC)

<p>Thank you Prof <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>The <em>DICOM Patcher</em>  module corrected the problem including the scaling problem i had.</p>
<p>Also just out of interest i tried the volume --&gt; spacing and when i gave same spacing value again i think the problem settled because  image spacing in volume information section was 0.3, 0.3 and 1.0 mm so when i changed everything to 0.3 mm it again seems it was working.</p>
<p>Thank you</p>

---

## Post #5 by @pieper (2019-11-28 16:12 UTC)

<p><a class="mention" href="/u/manjula">@manjula</a> - I’m glad you were very attentive to the spacing issues in the data and were able to find a workable solution.  To help make this process more robust, please scan a phantom with known dimensions using the scanner in question and share the data for testing.</p>

---

## Post #6 by @lassoan (2019-11-28 17:12 UTC)

<p>I guess it’s a Dolphin CBCT scanner. Developers of this device thought that slice thickness tag could be used to define image geometry, which is of course incorrect.</p>
<p>This is the rule in DICOM patcher that fixes it:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/324ad88c817cc77186a1736a2846a48b06e7a9ae/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L308" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/324ad88c817cc77186a1736a2846a48b06e7a9ae/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L308" target="_blank">Slicer/Slicer/blob/324ad88c817cc77186a1736a2846a48b06e7a9ae/Modules/Scripted/DICOMPatcher/DICOMPatcher.py#L308</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="298" style="counter-reset: li-counter 297 ;">
<li>import pydicom</li>
<li>
</li>
<li>if not hasattr(ds,'NumberOfFrames'):</li>
<li>  return</li>
<li>numberOfFrames = ds.NumberOfFrames</li>
<li>if numberOfFrames &lt;= 1:</li>
<li>  return</li>
<li>
</li>
<li># Multi-frame sequence, we may need to add slice positions</li>
<li>
</li>
<li class="selected"># Error in Dolphin 3D CBCT scanners, they store multiple frames but they keep using CTImageStorage as storage class</li>
<li>if ds.SOPClassUID == '1.2.840.10008.5.1.4.1.1.2': # Computed Tomography Image IOD</li>
<li>  ds.SOPClassUID = '1.2.840.10008.5.1.4.1.1.2.1' # Enhanced CT Image IOD</li>
<li>
</li>
<li>sliceStartPosition = ds.ImagePositionPatient if hasattr(ds,'ImagePositionPatient') else [0,0,0]</li>
<li>sliceAxes = ds.ImageOrientationPatient if hasattr(ds,'ImagePositionPatient') else [1,0,0,0,1,0]</li>
<li>x = sliceAxes[:3]</li>
<li>y = sliceAxes[3:]</li>
<li>z = [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]] # cross(x,y)</li>
<li>sliceSpacing = ds.SliceThickness if hasattr(ds,'SliceThickness') else 1.0</li>
<li>pixelSpacing = ds.PixelSpacing if hasattr(ds,'PixelSpacing') else [1.0, 1.0]</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #7 by @manjula (2019-11-28 17:54 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>It is a i-CAT KAVO dental CBCT. I will try to scan a phantom with that but it is not my scanner. It belong to colleague of mine and he send me this for a test run with 3D Slicer for a project we are planning for. I am not sure but i will try.</p>
<p>thanks</p>

---

## Post #8 by @pieper (2019-11-28 18:24 UTC)

<p>Sounds good.  Perhaps you can explain to your colleague that the scanner needs to be calibrated/tested to ensure accurate measurements.  In any case best of luck.</p>

---

## Post #9 by @lassoan (2019-11-28 18:55 UTC)

<p>Does the image come directly from the scanner or it has been processed by some software? Maybe the problem is not in the Dolphin software (in previous sample images that I got, Dolphin was in the manufacturer tag, but maybe it was just used for processing).</p>
<p>If it is straight from the scanner then the scanner manufacturer should be made aware of their probable non-conformance with the DICOM standard.</p>
<p>If you can provide a sample scan of a phantom then we can give you more specific information about which required DICOM tags are missing from their images.</p>

---

## Post #10 by @manjula (2019-11-29 08:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="9321">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>n-conf</p>
</blockquote>
</aside>
<p>I will tell him next week when i meet him.</p>
<p>Is the metdata is of any use ?  because It is already available !</p>

---

## Post #11 by @lassoan (2019-11-29 13:53 UTC)

<p>Yes, metadata is useful, could you copy-paste it here? (make sure you don’t remove any tags just replace values that contain personal information by ***).</p>

---

## Post #12 by @manjula (2019-11-29 19:47 UTC)

<p>I have pasted two metdata sets.</p>
<p>Metdata Set 01</p>
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
<td>[3] ORIGINAL, PRIMARY, AXIAL</td>
<td>CS</td>
<td>22</td>
</tr>
<tr>
<td>[0008,0012]</td>
<td>InstanceCreationDate</td>
<td>20170629</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0013]</td>
<td>InstanceCreationTime</td>
<td>082742</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0014]</td>
<td>InstanceCreatorUID</td>
<td>99999</td>
<td>UI</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0016]</td>
<td>SOPClassUID</td>
<td>1.2.840.10008.5.1.4.1.1.2</td>
<td>UI</td>
<td>26</td>
</tr>
<tr>
<td>[0008,0018]</td>
<td>SOPInstanceUID</td>
<td>2.16.840.114421.80462.9552036653.9615108653</td>
<td>UI</td>
<td>44</td>
</tr>
<tr>
<td>[0008,0020]</td>
<td>StudyDate</td>
<td>20170629</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0021]</td>
<td>SeriesDate</td>
<td>20170629</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0022]</td>
<td>AcquisitionDate</td>
<td>20170629</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0023]</td>
<td>ContentDate</td>
<td>20170629</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0030]</td>
<td>StudyTime</td>
<td>082742</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0031]</td>
<td>SeriesTime</td>
<td>082742</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0032]</td>
<td>AcquisitionTime</td>
<td>082742</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0033]</td>
<td>ContentTime</td>
<td>082742</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0050]</td>
<td>AccessionNumber</td>
<td></td>
<td>SH</td>
<td>0</td>
</tr>
<tr>
<td>[0008,0060]</td>
<td>Modality</td>
<td>CT</td>
<td>CS</td>
<td>2</td>
</tr>
<tr>
<td>[0008,0070]</td>
<td>Manufacturer</td>
<td>Imaging Sciences International</td>
<td>LO</td>
<td>30</td>
</tr>
<tr>
<td>[0008,0080]</td>
<td>InstitutionName</td>
<td>Imaging Sciences International</td>
<td>LO</td>
<td>30</td>
</tr>
<tr>
<td>[0008,0081]</td>
<td>InstitutionAddress</td>
<td>Hatfield, PA</td>
<td>ST</td>
<td>12</td>
</tr>
<tr>
<td>[0008,0090]</td>
<td>ReferringPhysicianName</td>
<td></td>
<td>PN</td>
<td>0</td>
</tr>
<tr>
<td>[0008,1010]</td>
<td>StationName</td>
<td>RONTGEN</td>
<td>SH</td>
<td>8</td>
</tr>
<tr>
<td>[0008,103e]</td>
<td>SeriesDescription</td>
<td></td>
<td>LO</td>
<td>0</td>
</tr>
<tr>
<td>[0008,1050]</td>
<td>PerformingPhysicianName</td>
<td></td>
<td>PN</td>
<td>0</td>
</tr>
<tr>
<td>[0008,1070]</td>
<td>OperatorsName</td>
<td>rtg</td>
<td>PN</td>
<td>4</td>
</tr>
<tr>
<td>[0008,1090]</td>
<td>ManufacturerModelName</td>
<td>17-19</td>
<td>LO</td>
<td>6</td>
</tr>
<tr>
<td>[0009,0100]</td>
<td>Unknown Tag &amp; Data</td>
<td>9267</td>
<td>LO</td>
<td>4</td>
</tr>
<tr>
<td>[0009,0101]</td>
<td>Unknown Tag &amp; Data</td>
<td>1</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0010,0010]</td>
<td>PatientName</td>
<td>*************</td>
<td>PN</td>
<td>16</td>
</tr>
<tr>
<td>[0010,0020]</td>
<td>PatientID</td>
<td>**********</td>
<td>LO</td>
<td>10</td>
</tr>
<tr>
<td>[0010,0030]</td>
<td>PatientBirthDate</td>
<td>********</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0010,0040]</td>
<td>PatientSex</td>
<td>*</td>
<td>CS</td>
<td>2</td>
</tr>
<tr>
<td>[0010,2160]</td>
<td>EthnicGroup</td>
<td></td>
<td>SH</td>
<td>0</td>
</tr>
<tr>
<td>[0010,4000]</td>
<td>PatientComments</td>
<td></td>
<td>LT</td>
<td>0</td>
</tr>
<tr>
<td>[0018,0022]</td>
<td>ScanOptions</td>
<td>PORTRAIT</td>
<td>CS</td>
<td>8</td>
</tr>
<tr>
<td>[0018,0050]</td>
<td>SliceThickness</td>
<td>0.300</td>
<td>DS</td>
<td>6</td>
</tr>
<tr>
<td>[0018,0060]</td>
<td>KVP</td>
<td>120</td>
<td>DS</td>
<td>4</td>
</tr>
<tr>
<td>[0018,0090]</td>
<td>DataCollectionDiameter</td>
<td>170.00</td>
<td>DS</td>
<td>6</td>
</tr>
<tr>
<td>[0018,1000]</td>
<td>DeviceSerialNumber</td>
<td>ICU-080462</td>
<td>LO</td>
<td>10</td>
</tr>
<tr>
<td>[0018,1020]</td>
<td>SoftwareVersions</td>
<td>1.9.3.13</td>
<td>LO</td>
<td>8</td>
</tr>
<tr>
<td>[0018,1150]</td>
<td>ExposureTime</td>
<td>4</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0018,1151]</td>
<td>XRayTubeCurrent</td>
<td>5</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0018,5100]</td>
<td>PatientPosition</td>
<td></td>
<td>CS</td>
<td>0</td>
</tr>
<tr>
<td>[0019,1000]</td>
<td>Unknown Tag &amp; Data</td>
<td>ISI_ACQU_1</td>
<td>LO</td>
<td>10</td>
</tr>
<tr>
<td>[0019,1043]</td>
<td>Unknown Tag &amp; Data</td>
<td>1</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0019,1050]</td>
<td>Unknown Tag &amp; Data</td>
<td>64.3059095263</td>
<td>DS</td>
<td>14</td>
</tr>
<tr>
<td>[0019,1051]</td>
<td>Unknown Tag &amp; Data</td>
<td>73.0000000000</td>
<td>DS</td>
<td>14</td>
</tr>
<tr>
<td>[0019,2000]</td>
<td>Unknown Tag &amp; Data</td>
<td>Pan</td>
<td>EFOV</td>
<td>DAP</td>
</tr>
<tr>
<td>[0019,2001]</td>
<td>Unknown Tag &amp; Data</td>
<td>9deSGSZl+9BZr9jdo0hvGbDe+I4</td>
<td>LO</td>
<td>28</td>
</tr>
<tr>
<td>[0019,2002]</td>
<td>Unknown Tag &amp; Data</td>
<td>4.586000^0.138000^0.138000</td>
<td>ST</td>
<td>50</td>
</tr>
<tr>
<td>[0020,000d]</td>
<td>StudyInstanceUID</td>
<td>2.16.840.114421.80462.9552036462</td>
<td>UI</td>
<td>32</td>
</tr>
<tr>
<td>[0020,000e]</td>
<td>SeriesInstanceUID</td>
<td>2.16.840.114421.80462.9552036477.9583572477</td>
<td>UI</td>
<td>44</td>
</tr>
<tr>
<td>[0020,0010]</td>
<td>StudyID</td>
<td></td>
<td>SH</td>
<td>0</td>
</tr>
<tr>
<td>[0020,0011]</td>
<td>SeriesNumber</td>
<td>0</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0020,0012]</td>
<td>AcquisitionNumber</td>
<td>0</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0020,0013]</td>
<td>InstanceNumber</td>
<td>1</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0020,0032]</td>
<td>ImagePositionPatient</td>
<td>[3] -384.000, -384.000, 100.000</td>
<td>DS</td>
<td>26</td>
</tr>
<tr>
<td>[0020,0037]</td>
<td>ImageOrientationPatient</td>
<td>[6] 1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000</td>
<td>DS</td>
<td>54</td>
</tr>
<tr>
<td>[0020,0052]</td>
<td>FrameOfReferenceUID</td>
<td>2.16.840.114421.80462.9552036477.9583572477</td>
<td>UI</td>
<td>44</td>
</tr>
<tr>
<td>[0020,1040]</td>
<td>PositionReferenceIndicator</td>
<td></td>
<td>LO</td>
<td>0</td>
</tr>
<tr>
<td>[0020,1041]</td>
<td>SliceLocation</td>
<td>100.000</td>
<td>DS</td>
<td>8</td>
</tr>
<tr>
<td>[0021,1032]</td>
<td>Unknown Tag &amp; Data</td>
<td>18.537371</td>
<td>DS</td>
<td>10</td>
</tr>
<tr>
<td>[0021,1034]</td>
<td>Unknown Tag &amp; Data</td>
<td>8.883619</td>
<td>DS</td>
<td>8</td>
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
<td>[0028,0008]</td>
<td>NumberOfFrames</td>
<td>576</td>
<td>IS</td>
<td>4</td>
</tr>
<tr>
<td>[0028,0010]</td>
<td>Rows</td>
<td>768</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0011]</td>
<td>Columns</td>
<td>768</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0030]</td>
<td>PixelSpacing</td>
<td>[2] 0.300, 0.300</td>
<td>DS</td>
<td>12</td>
</tr>
<tr>
<td>[0028,0100]</td>
<td>BitsAllocated</td>
<td>16</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0101]</td>
<td>BitsStored</td>
<td>16</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0102]</td>
<td>HighBit</td>
<td>15</td>
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
<td>[0028,1050]</td>
<td>WindowCenter</td>
<td>1100</td>
<td>DS</td>
<td>4</td>
</tr>
<tr>
<td>[0028,1051]</td>
<td>WindowWidth</td>
<td>4500</td>
<td>DS</td>
<td>4</td>
</tr>
<tr>
<td>[0028,1052]</td>
<td>RescaleIntercept</td>
<td>0</td>
<td>DS</td>
<td>2</td>
</tr>
<tr>
<td>[0028,1053]</td>
<td>RescaleSlope</td>
<td>1</td>
<td>DS</td>
<td>2</td>
</tr>
<tr>
<td>[0032,4000]</td>
<td>RETIRED_StudyComments</td>
<td></td>
<td>LT</td>
<td>0</td>
</tr>
<tr>
<td>[7fe0,0010]</td>
<td>PixelData</td>
<td></td>
<td>OB</td>
<td>0</td>
</tr>
</tbody>
</table>
</div><p>MetData set 02</p>
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
<td>[3] ORIGINAL, PRIMARY, AXIAL</td>
<td>CS</td>
<td>22</td>
</tr>
<tr>
<td>[0008,0012]</td>
<td>InstanceCreationDate</td>
<td>20170914</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0013]</td>
<td>InstanceCreationTime</td>
<td>092126</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0014]</td>
<td>InstanceCreatorUID</td>
<td>99999</td>
<td>UI</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0016]</td>
<td>SOPClassUID</td>
<td>1.2.840.10008.5.1.4.1.1.2</td>
<td>UI</td>
<td>26</td>
</tr>
<tr>
<td>[0008,0018]</td>
<td>SOPInstanceUID</td>
<td>2.16.840.114421.80462.9558692675.9621764675</td>
<td>UI</td>
<td>44</td>
</tr>
<tr>
<td>[0008,0020]</td>
<td>StudyDate</td>
<td>20170914</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0021]</td>
<td>SeriesDate</td>
<td>20170914</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0022]</td>
<td>AcquisitionDate</td>
<td>20170914</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0023]</td>
<td>ContentDate</td>
<td>20170914</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0030]</td>
<td>StudyTime</td>
<td>092126</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0031]</td>
<td>SeriesTime</td>
<td>092126</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0032]</td>
<td>AcquisitionTime</td>
<td>092126</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0033]</td>
<td>ContentTime</td>
<td>092126</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,0050]</td>
<td>AccessionNumber</td>
<td></td>
<td>SH</td>
<td>0</td>
</tr>
<tr>
<td>[0008,0060]</td>
<td>Modality</td>
<td>CT</td>
<td>CS</td>
<td>2</td>
</tr>
<tr>
<td>[0008,0070]</td>
<td>Manufacturer</td>
<td>Imaging Sciences International</td>
<td>LO</td>
<td>30</td>
</tr>
<tr>
<td>[0008,0080]</td>
<td>InstitutionName</td>
<td>Imaging Sciences International</td>
<td>LO</td>
<td>30</td>
</tr>
<tr>
<td>[0008,0081]</td>
<td>InstitutionAddress</td>
<td>Hatfield, PA</td>
<td>ST</td>
<td>12</td>
</tr>
<tr>
<td>[0008,0090]</td>
<td>ReferringPhysicianName</td>
<td></td>
<td>PN</td>
<td>0</td>
</tr>
<tr>
<td>[0008,1010]</td>
<td>StationName</td>
<td>RONTGEN</td>
<td>SH</td>
<td>8</td>
</tr>
<tr>
<td>[0008,103e]</td>
<td>SeriesDescription</td>
<td></td>
<td>LO</td>
<td>0</td>
</tr>
<tr>
<td>[0008,1050]</td>
<td>PerformingPhysicianName</td>
<td></td>
<td>PN</td>
<td>0</td>
</tr>
<tr>
<td>[0008,1070]</td>
<td>OperatorsName</td>
<td>rtg</td>
<td>PN</td>
<td>4</td>
</tr>
<tr>
<td>[0008,1090]</td>
<td>ManufacturerModelName</td>
<td>17-19</td>
<td>LO</td>
<td>6</td>
</tr>
<tr>
<td>[0009,0100]</td>
<td>Unknown Tag &amp; Data</td>
<td>8809</td>
<td>LO</td>
<td>4</td>
</tr>
<tr>
<td>[0009,0101]</td>
<td>Unknown Tag &amp; Data</td>
<td>1</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0010,0010]</td>
<td>PatientName</td>
<td>********</td>
<td>PN</td>
<td>12</td>
</tr>
<tr>
<td>[0010,0020]</td>
<td>PatientID</td>
<td>********</td>
<td>LO</td>
<td>10</td>
</tr>
<tr>
<td>[0010,0030]</td>
<td>PatientBirthDate</td>
<td>********</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0010,0040]</td>
<td>PatientSex</td>
<td>*</td>
<td>CS</td>
<td>2</td>
</tr>
<tr>
<td>[0010,2160]</td>
<td>EthnicGroup</td>
<td></td>
<td>SH</td>
<td>0</td>
</tr>
<tr>
<td>[0010,4000]</td>
<td>PatientComments</td>
<td></td>
<td>LT</td>
<td>0</td>
</tr>
<tr>
<td>[0018,0022]</td>
<td>ScanOptions</td>
<td>PORTRAIT</td>
<td>CS</td>
<td>8</td>
</tr>
<tr>
<td>[0018,0050]</td>
<td>SliceThickness</td>
<td>0.300</td>
<td>DS</td>
<td>6</td>
</tr>
<tr>
<td>[0018,0060]</td>
<td>KVP</td>
<td>120</td>
<td>DS</td>
<td>4</td>
</tr>
<tr>
<td>[0018,0090]</td>
<td>DataCollectionDiameter</td>
<td>170.00</td>
<td>DS</td>
<td>6</td>
</tr>
<tr>
<td>[0018,1000]</td>
<td>DeviceSerialNumber</td>
<td>ICU-080462</td>
<td>LO</td>
<td>10</td>
</tr>
<tr>
<td>[0018,1020]</td>
<td>SoftwareVersions</td>
<td>1.9.3.13</td>
<td>LO</td>
<td>8</td>
</tr>
<tr>
<td>[0018,1150]</td>
<td>ExposureTime</td>
<td>4</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0018,1151]</td>
<td>XRayTubeCurrent</td>
<td>5</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0018,5100]</td>
<td>PatientPosition</td>
<td></td>
<td>CS</td>
<td>0</td>
</tr>
<tr>
<td>[0019,1000]</td>
<td>Unknown Tag &amp; Data</td>
<td>ISI_ACQU_1</td>
<td>LO</td>
<td>10</td>
</tr>
<tr>
<td>[0019,1043]</td>
<td>Unknown Tag &amp; Data</td>
<td>1</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0019,1050]</td>
<td>Unknown Tag &amp; Data</td>
<td>77.6498551190</td>
<td>DS</td>
<td>14</td>
</tr>
<tr>
<td>[0019,1051]</td>
<td>Unknown Tag &amp; Data</td>
<td>124.0000000000</td>
<td>DS</td>
<td>14</td>
</tr>
<tr>
<td>[0019,2000]</td>
<td>Unknown Tag &amp; Data</td>
<td>Pan</td>
<td>EFOV</td>
<td>DAP</td>
</tr>
<tr>
<td>[0019,2001]</td>
<td>Unknown Tag &amp; Data</td>
<td>o6fVI9wQoGd8/4ckK5VByBD58Sg</td>
<td>LO</td>
<td>28</td>
</tr>
<tr>
<td>[0019,2002]</td>
<td>Unknown Tag &amp; Data</td>
<td>4.586000^0.138000^0.138000^0.138000</td>
<td>ST</td>
<td>58</td>
</tr>
<tr>
<td>[0020,000d]</td>
<td>StudyInstanceUID</td>
<td>2.16.840.114421.80462.9558692486</td>
<td>UI</td>
<td>32</td>
</tr>
<tr>
<td>[0020,000e]</td>
<td>SeriesInstanceUID</td>
<td>2.16.840.114421.80462.9558692501.9590228501</td>
<td>UI</td>
<td>44</td>
</tr>
<tr>
<td>[0020,0010]</td>
<td>StudyID</td>
<td></td>
<td>SH</td>
<td>0</td>
</tr>
<tr>
<td>[0020,0011]</td>
<td>SeriesNumber</td>
<td>0</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0020,0012]</td>
<td>AcquisitionNumber</td>
<td>0</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0020,0013]</td>
<td>InstanceNumber</td>
<td>1</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0020,0032]</td>
<td>ImagePositionPatient</td>
<td>[3] -384.000, -384.000, 100.000</td>
<td>DS</td>
<td>26</td>
</tr>
<tr>
<td>[0020,0037]</td>
<td>ImageOrientationPatient</td>
<td>[6] 1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000</td>
<td>DS</td>
<td>54</td>
</tr>
<tr>
<td>[0020,0052]</td>
<td>FrameOfReferenceUID</td>
<td>2.16.840.114421.80462.9558692501.9590228501</td>
<td>UI</td>
<td>44</td>
</tr>
<tr>
<td>[0020,1040]</td>
<td>PositionReferenceIndicator</td>
<td></td>
<td>LO</td>
<td>0</td>
</tr>
<tr>
<td>[0020,1041]</td>
<td>SliceLocation</td>
<td>100.000</td>
<td>DS</td>
<td>8</td>
</tr>
<tr>
<td>[0021,1032]</td>
<td>Unknown Tag &amp; Data</td>
<td>18.537371</td>
<td>DS</td>
<td>10</td>
</tr>
<tr>
<td>[0021,1034]</td>
<td>Unknown Tag &amp; Data</td>
<td>8.883619</td>
<td>DS</td>
<td>8</td>
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
<td>[0028,0008]</td>
<td>NumberOfFrames</td>
<td>576</td>
<td>IS</td>
<td>4</td>
</tr>
<tr>
<td>[0028,0010]</td>
<td>Rows</td>
<td>768</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0011]</td>
<td>Columns</td>
<td>768</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0030]</td>
<td>PixelSpacing</td>
<td>[2] 0.300, 0.300</td>
<td>DS</td>
<td>12</td>
</tr>
<tr>
<td>[0028,0100]</td>
<td>BitsAllocated</td>
<td>16</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0101]</td>
<td>BitsStored</td>
<td>16</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0102]</td>
<td>HighBit</td>
<td>15</td>
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
<td>[0028,1050]</td>
<td>WindowCenter</td>
<td>1100</td>
<td>DS</td>
<td>4</td>
</tr>
<tr>
<td>[0028,1051]</td>
<td>WindowWidth</td>
<td>4500</td>
<td>DS</td>
<td>4</td>
</tr>
<tr>
<td>[0028,1052]</td>
<td>RescaleIntercept</td>
<td>0</td>
<td>DS</td>
<td>2</td>
</tr>
<tr>
<td>[0028,1053]</td>
<td>RescaleSlope</td>
<td>1</td>
<td>DS</td>
<td>2</td>
</tr>
<tr>
<td>[0032,4000]</td>
<td>RETIRED_StudyComments</td>
<td></td>
<td>LT</td>
<td>0</td>
</tr>
<tr>
<td>[7fe0,0010]</td>
<td>PixelData</td>
<td></td>
<td>OB</td>
<td>0</td>
</tr>
</tbody>
</table>
</div>

---

## Post #13 by @manjula (2019-12-02 20:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Jsut out of curiosity, did you manage to obtain any useful information from the metdata ?  or do I have to see the possibility of a phantom object scan  ?</p>

---

## Post #14 by @lassoan (2019-12-03 04:27 UTC)

<p>Sorry for the slow response, both <a class="mention" href="/u/pieper">@pieper</a> and I are quite busy at RSNA. I’ve checked the metadata and the problem is the following:</p>
<p>Slice position must be specified for each slice. However in the ISI i-CAT device, only one position is specified using <code>[0020,0032]	ImagePositionPatient</code> and probably the developers thought that by adding a <code>[0018,0050]	SliceThickness</code> tag will specify slice positions within the image. That is incorrect. Instead, values that are the same for all frames (image orientation, pixel spacing, etc.) should be specified in tag (5200,9229) and values that are different in each slice (such as fields position) should be specified in <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.16.html">tag (5200,9230)</a>. For example:</p>
<pre><code>(5200,9229) SQ (Sequence with undefined length #=1)     # u/l, 1 SharedFunctionalGroupsSequence
(0020,9116) SQ (Sequence with undefined length #=1)     # u/l, 1 PlaneOrientationSequence
    (0020,0037) DS [1.00000\0.00000\0.00000\0.00000\1.00000\0.00000] #  48, 6 ImageOrientationPatient
(0028,9110) SQ (Sequence with undefined length #=1)     # u/l, 1 PixelMeasuresSequence
    (0018,0050) DS [3.00000]                                #   8, 1 SliceThickness
    (0028,0030) DS [0.597656\0.597656]                      #  18, 2 PixelSpacing
...

(5200,9230) SQ (Sequence with undefined length #=54)    # u/l, 1 PerFrameFunctionalGroupsSequence
(0020,9113) SQ (Sequence with undefined length #=1)     # u/l, 1 PlanePositionSequence
    (0020,0032) DS [-94.7012\-312.701\-806.500]             #  26, 3 ImagePositionPatient
(0020,9113) SQ (Sequence with undefined length #=1)     # u/l, 1 PlanePositionSequence
    (0020,0032) DS [-94.7012\-312.701\-809.500]             #  26, 3 ImagePositionPatient
...</code></pre>

---

## Post #15 by @manjula (2019-12-03 13:17 UTC)

<p>Thank you for the information. It has been very useful.</p>
<p>Further, I have noticed that few CBCT’s that i have worked with in the past to import data in to 3D Slicer is having the same problem but did not knew what was wrong at the time but never with the conventional CT’s.</p>
<p>Are CBCT manufacturers are notoriously not compiling to DICOM format ? is this something non compliance is mainly a problem with CBCT manufacturers ?</p>

---

## Post #16 by @lassoan (2019-12-03 13:44 UTC)

<aside class="quote no-group" data-username="manjula" data-post="15" data-topic="9321">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Are CBCT manufacturers are notoriously not compiling to DICOM format ? is this something non compliance is mainly a problem with CBCT manufacturers ?</p>
</blockquote>
</aside>
<p>Yes, CBCT and microCT manufacturers often have DICOM compliance issues. Maybe they have fixed the problems in their current products but not released updates for the earlier models.</p>

---
