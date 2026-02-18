# Minimum header information for loading DICOM into same series

**Topic ID**: 6355
**Date**: 2019-04-01
**URL**: https://discourse.slicer.org/t/minimum-header-information-for-loading-dicom-into-same-series/6355

---

## Post #1 by @d4mir (2019-04-01 16:48 UTC)

<p>Hi,</p>
<p>I have a generally blank dicom header, (attached to images).<br>
I’m wondering what is the minimum number of fields to have to pull a set of images (135 different ones them) into the same series.</p>
<p>When I import them into slicer they attempt to go to separate series</p>
<p>Heres sample fields</p>
<p>struct with fields:</p>
<pre><code>                                   Filename: '/Users/d/Documents/Images/im0090.dcm'
                                FileModDate: '26-Mar-2019 12:16:12'
                                   FileSize: 1865690
                                     Format: 'DICOM'
                              FormatVersion: 3
                                      Width: 1110
                                     Height: 560
                                   BitDepth: 8
                                  ColorType: 'truecolor'
             FileMetaInformationGroupLength: 208
                 FileMetaInformationVersion: [2×1 uint8]
                    MediaStorageSOPClassUID: '1.2.840.10008.5.1.4.1.1.7'
                 MediaStorageSOPInstanceUID: '1.3.6.1.4.1.9590.100.1.2.288704759709434390630648630132056272210'
                          TransferSyntaxUID: '1.2.840.10008.1.2'
                     ImplementationClassUID: '1.3.6.1.4.1.9590.100.1.3.100.9.4'
                  ImplementationVersionName: 'MATLAB IPT 9.4'
                                SOPClassUID: '1.2.840.10008.5.1.4.1.1.7'
                             SOPInstanceUID: '1.3.6.1.4.1.9590.100.1.2.288704759709434390630648630132056272210'
                                  StudyDate: ''
                                ContentDate: '20190326'
                                  StudyTime: ''
                                ContentTime: '121612.416500'
                            AccessionNumber: ''
                                   Modality: 'OT'
                             ConversionType: 'WSD'
                     ReferringPhysicianName: [1×1 struct]
                                PatientName: [1×1 struct]
                                  PatientID: ''
                           PatientBirthDate: ''
                                 PatientSex: ''
         SecondaryCaptureDeviceManufacturer: 'MathWorks'
SecondaryCaptureDeviceManufacturerModelName: 'MATLAB'
                           StudyInstanceUID: '1.3.6.1.4.1.9590.100.1.2.234207437404492933027473378421527667084'
                          SeriesInstanceUID: '1.3.6.1.4.1.9590.100.1.2.244984412904515044829263492910100970731'
                                    StudyID: ''
                               SeriesNumber: []
                             InstanceNumber: []
                         PatientOrientation: ''
                            SamplesPerPixel: 3
                  PhotometricInterpretation: 'RGB'
                        PlanarConfiguration: 0
                                       Rows: 560
                                    Columns: 1110
                              BitsAllocated: 8
                                 BitsStored: 8
                                    HighBit: 7
                        PixelRepresentation: 0h2.SecondaryCaptureDeviceManufacturer, h2.SecondaryCaptureDeviceManufacturerModelName, h2.StudyInstanceUID, h2.SeriesInstanceUID, h2.StudyID, h2.SeriesNumber, h2.InstanceNumber, h2.PatientOrientation, h2.SamplesPerPixel, h2.PhotometricInterpretation, h2.PlanarConfiguration, h2.Rows, h2.Columns, h2.BitsAllocated, h2.BitsStored, h2.HighBit</code></pre>

---

## Post #2 by @pieper (2019-04-02 13:22 UTC)

<p>If you want to load as a scalar volume you probably need at least the tags linked below.  Also if you want them in the same series, the instances all need the same SeriesInstanceUID (and StudyInstanceUID) but unique values for InstanceUID.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L27-L45" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L27-L45" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L27-L45</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="27" style="counter-reset: li-counter 26 ;">
<li>self.tags['sopClassUID'] = "0008,0016"</li>
<li>self.tags['seriesDescription'] = "0008,103e"</li>
<li>self.tags['seriesUID'] = "0020,000E"</li>
<li>self.tags['seriesNumber'] = "0020,0011"</li>
<li>self.tags['position'] = "0020,0032"</li>
<li>self.tags['orientation'] = "0020,0037"</li>
<li>self.tags['pixelData'] = "7fe0,0010"</li>
<li>self.tags['seriesInstanceUID'] = "0020,000E"</li>
<li>self.tags['contentTime'] = "0008,0033"</li>
<li>self.tags['triggerTime'] = "0018,1060"</li>
<li>self.tags['diffusionGradientOrientation'] = "0018,9089"</li>
<li>self.tags['imageOrientationPatient'] = "0020,0037"</li>
<li>self.tags['numberOfFrames'] = "0028,0008"</li>
<li>self.tags['instanceUID'] = "0008,0018"</li>
<li>self.tags['windowCenter'] = "0028,1050"</li>
<li>self.tags['windowWidth'] = "0028,1051"</li>
<li>self.tags['classUID'] = "0008,0016"</li>
<li>self.tags['rows'] = "0028,0010"</li>
<li>self.tags['columns'] = "0028,0011"</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
