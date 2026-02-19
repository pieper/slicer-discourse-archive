---
topic_id: 25864
title: "Create Volume Node From Dcm List"
date: 2022-10-24
url: https://discourse.slicer.org/t/25864
---

# Create volume node from dcm list

**Topic ID**: 25864
**Date**: 2022-10-24
**URL**: https://discourse.slicer.org/t/create-volume-node-from-dcm-list/25864

---

## Post #1 by @bserrano (2022-10-24 15:11 UTC)

<p>Hi,</p>
<p>I want to automatically create a volume node from a list of dcm files,  without having to “import” the files into Slicer, because the list is already in Slicer as a variable.</p>
<p>Is there a way to do it?</p>
<p>Thanks,</p>

---

## Post #2 by @pieper (2022-10-24 15:21 UTC)

<p>There are lots of special cases with dicom, but if you know the files form a volume this code is what the DICOM module uses under the hood.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L359-L368">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L359-L368" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L359-L368" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L359-L368</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="359" style="counter-reset: li-counter 358 ;">
          <li>def loadFilesWithArchetype(self, files, name):</li>
          <li>    """Load files in the traditional Slicer manner</li>
          <li>    using the volume logic helper class</li>
          <li>    and the vtkITK archetype helper code</li>
          <li>    """</li>
          <li>    fileList = vtk.vtkStringArray()</li>
          <li>    for f in files:</li>
          <li>        fileList.InsertNextValue(f)</li>
          <li>    volumesLogic = slicer.modules.volumes.logic()</li>
          <li>    return volumesLogic.AddArchetypeScalarVolume(files[0], name, 0, fileList)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @bserrano (2022-10-24 15:32 UTC)

<p>Thanks, what is “files” in the code?. I tried to use it but it expects a string.<br>
With:</p>
<pre><code class="lang-auto">fileList.InsertNextValue(myList[0])
</code></pre>
<p>I’m getting</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: InsertNextValue argument 1: string is required
</code></pre>
<p>The elements of my list have all the information about each slide.<br>
For example, myList[0] looks like:</p>
<pre><code class="lang-auto">Dataset.file_meta -------------------------------
(0002, 0000) File Meta Information Group Length  UL: 254
(0002, 0001) File Meta Information Version       OB: b'\x00\x01'
(0002, 0002) Media Storage SOP Class UID         UI: CT Image Storage
(0002, 0003) Media Storage SOP Instance UID      UI: 1.2.826.0.1.3680043.2.1125.1.52460637011028086951598878742235975
(0002, 0010) Transfer Syntax UID                 UI: Implicit VR Little Endian
(0002, 0012) Implementation Class UID            UI: 1.2.826.0.1.3680043.2.1143.107.104.103.115.3.0.5.111.124.113
(0002, 0013) Implementation Version Name         SH: 'GDCM 3.0.5'
(0002, 0016) Source Application Entity Title     AE: 'GDCM/ITK 5.1.2'
-------------------------------------------------
(0008, 0008) Image Type                          CS: ['ORIGINAL', 'PRIMARY', 'AXIAL']
(0008, 0016) SOP Class UID                       UI: CT Image Storage
(0008, 0018) SOP Instance UID                    UI: 1.2.826.0.1.3680043.2.1125.1.52460637011028086951598878742235975
(0008, 0020) Study Date                          DA: '20221024'
(0008, 0021) Series Date                         DA: '20221024'
(0008, 0023) Content Date                        DA: '20221024'
(0008, 0030) Study Time                          TM: '163518'
(0008, 0031) Series Time                         TM: '163518'
(0008, 0033) Content Time                        TM: '163518'
(0008, 0050) Accession Number                    SH: ''
(0008, 0060) Modality                            CS: 'CT'
(0008, 0070) Manufacturer                        LO: 'Unknown manufacturer'
(0008, 0090) Referring Physician's Name          PN: ''
(0008, 103e) Series Description                  LO: 'No series description'
(0008, 1090) Manufacturer's Model Name           LO: 'Unknown model'
(0010, 0010) Patient's Name                      PN: 'Anonymous'
(0010, 0020) Patient ID                          LO: 'IWXMOF'
(0010, 0030) Patient's Birth Date                DA: ''
(0010, 0040) Patient's Sex                       CS: ''
(0018, 0050) Slice Thickness                     DS: "0.625"
(0018, 5100) Patient Position                    CS: 'HFS'
(0020, 000d) Study Instance UID                  UI: 1.2.826.0.1.3680043.2.1125.1.82509780281950280869767406646856996
(0020, 000e) Series Instance UID                 UI: 1.2.826.0.1.3680043.2.1125.1.52499705098477734239230221067465548
(0020, 0010) Study ID                            SH: 'SLICER10001'
(0020, 0011) Series Number                       IS: "1"
(0020, 0013) Instance Number                     IS: "1"
(0020, 0032) Image Position (Patient)            DS: [105.671, 11.5634, -222.079]
(0020, 0037) Image Orientation (Patient)         DS: [-1, 0, 0, 0, -1, 0]
(0020, 0052) Frame of Reference UID              UI: 1.2.826.0.1.3680043.2.1125.1.45959135399399872453735019046048235
(0020, 1040) Position Reference Indicator        LO: ''
(0028, 0002) Samples per Pixel                   US: 1
(0028, 0004) Photometric Interpretation          CS: 'MONOCHROME2'
(0028, 0010) Rows                                US: 400
(0028, 0011) Columns                             US: 400
(0028, 0030) Pixel Spacing                       DS: [.3730469942, .3730469942]
(0028, 0100) Bits Allocated                      US: 16
(0028, 0101) Bits Stored                         US: 16
(0028, 0102) High Bit                            US: 15
(0028, 0103) Pixel Representation                US: 1
(0028, 1050) Window Center                       DS: "100.0"
(0028, 1051) Window Width                        DS: "800.0"
(0028, 1052) Rescale Intercept                   DS: "0.0"
(0028, 1053) Rescale Slope                       DS: "1.0"
(0028, 1054) Rescale Type                        LO: 'HU'
(7fe0, 0010) Pixel Data                          OW: Array of 320000 elements
</code></pre>

---

## Post #4 by @pieper (2022-10-24 20:39 UTC)

<p>The <code>files</code> argument would be a list of file system paths to binary (“part 10”) dicom datasets.</p>
<p>Are you saying you have a list of pydicom dataset instances instead?  As things stand now you would need to write these out to temp files and then load them.  Realistically this should be very fast, but if you really need performance you could also look into assembling the volume directly with numpy (but there are many special cases to consider so the result will be highly context dependent, as in knowing in advance what the file contain).</p>

---
