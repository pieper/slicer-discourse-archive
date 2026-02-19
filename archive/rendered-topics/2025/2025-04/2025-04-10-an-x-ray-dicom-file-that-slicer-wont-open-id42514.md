---
topic_id: 42514
title: "An X Ray Dicom File That Slicer Wont Open"
date: 2025-04-10
url: https://discourse.slicer.org/t/42514
---

# An X-Ray DICOM file that Slicer won't open

**Topic ID**: 42514
**Date**: 2025-04-10
**URL**: https://discourse.slicer.org/t/an-x-ray-dicom-file-that-slicer-wont-open/42514

---

## Post #1 by @shai-ikko (2025-04-10 08:34 UTC)

<p>Hello,</p>
<p>I have a series of X-Ray files which Slicer refuses to open. I can open them in other DICOM viewers, and I can do some processing in tools like <code>pydicom</code> or the <code>dcm*</code> and <code>gdcm*</code> CLI suites.</p>
<p>This seems a lot like <a href="https://discourse.slicer.org/t/seeking-help-could-not-load-as-a-scalar-volume-error-opening-dicom-x-ray-files-bone-ml-and-ap-views-with-3d-slicer/33443" class="inline-onebox">Seeking Help: "Could not load as a Scalar Volume" Error Opening DICOM X-ray Files (Bone, ML, and AP Views) with 3D Slicer</a> but there is no resolution in that discussion.</p>
<p>The files are loaded successfully into the DICOM database, but fail to load as volumes.</p>
<p>I first get <code>Image spacing may need to be calibrated for accurate size measurements.</code>  warnings, and then <code>Could not load: 2: XA SCOPY [2] as a Image sequence</code> for all files except the first, and <code>Could not load: 1: XA SCOPY - 16 frames Volume Sequence by AcquisitionTime as a MultiVolume</code> for the first. The log includes a series of</p>
<pre><code class="lang-auto">[Python] Could not read scalar volume using GDCM approach.  Error is: FileFormatError
[VTK] vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /tmp/Pig X ray March 17 2025/run_1.dcm. ITK exception info: error in unknown:  Could not create IO object for reading file /tmp/Pig X ray March 17 2025/run_1.dcm
[VTK]   Tried to create one of the following:
[VTK]     BMPImageIO
[VTK]     BioRadImageIO
[VTK]     DCMTKImageIO
[VTK]     GDCMImageIO
[VTK]     GiplImageIO
[VTK]     JPEGImageIO
[VTK]     LSMImageIO
[VTK]     MGHImageIO
[VTK]     MINCImageIO
[VTK]     MRCImageIO
[VTK]     MetaImageIO
[VTK]     NiftiImageIO
[VTK]     NrrdImageIO
[VTK]     PNGImageIO
[VTK]     ScancoImageIO
[VTK]     StimulateImageIO
[VTK]     TIFFImageIO
[VTK]     VTKImageIO
[VTK]     MRMLIDImageIO
[VTK]     Bruker2dseqImageIO
[VTK]     GE4ImageIO
[VTK]     GE5ImageIO
[VTK]     HDF5ImageIO
[VTK]     JPEG2000ImageIO
[VTK]   You probably failed to set a file suffix, or
[VTK]     set the suffix to an unsupported type.
[VTK] Algorithm vtkITKArchetypeImageSeriesScalarReader (0x7415440) returned failure for request: vtkInformation (0xa83f7c0)
[VTK]   Debug: Off
[VTK]   Modified Time: 223493
[VTK]   Reference Count: 1
[VTK]   Registered Events: (none)
[VTK]   Request: REQUEST_INFORMATION
[VTK]   ALGORITHM_AFTER_FORWARD: 1
[VTK]   FORWARD_DIRECTION: 0
</code></pre>
<p>There are also a few instances of</p>
<pre><code class="lang-auto">DICOM plugin failed to load '16: XA SCOPY [16]' as a 'Image sequence'.
Traceback (most recent call last):
  File ".../Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/DICOMLib/DICOMUtils.py", line 812, in loadLoadables
    loadSuccess = plugin.load(loadable)
  File ".../Slicer-5.6.2-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMImageSequencePlugin.py", line 357, in load
    imageData, ijkToRas = self.loadImageData(filePath, loadable.grayscale, tempFrameVolume)
  File ".../Slicer-5.6.2-linux-amd64/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMImageSequencePlugin.py", line 235, in loadImageData
    f"Could not read image {loadable.name} from file {filePath}. Error is: {errorString}")
NameError: name 'loadable' is not defined
</code></pre>
<p>(this seems to be a bug in the error-handling code, and I haven’t checked if it is fixed in later releases)</p>
<p>Since, as I said, several tools can read and process these files, I tried to manipulate them a little (in particular, add PixelSpacing, remove the Cyrillic encoding since all the texts are in ASCII anyway, using pydicom; change the image representation to JPEG using <code>gdcmconv</code>). This changed nothing.</p>
<p>I want to attach the first of these files (no need for anonymization, the image is of a pig), but the forum seems to only allow conventional image files.</p>

---

## Post #2 by @shai-ikko (2025-04-10 13:27 UTC)

<p>Well. You can get the file from <a href="https://drive.google.com/file/d/10Vnxs1VqPYiuQ5xPLVN_zKD4Ne4E4IQx/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">run_1.dcm - Google Drive</a></p>
<p>Please let me know if there’s any more data I can provide.</p>

---

## Post #3 by @muratmaga (2025-04-10 15:00 UTC)

<p>It generates a lot of errors and warnings, but it seems to load for me with 5.8.1. I just dragged into Slicer, go through the DICOM module warnings, and then hit examine and load.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/add472bb64c474b3f06f493ee17526474d3fa6f6.jpeg" data-download-href="/uploads/short-url/oNLLLMX8ECGILiLulc3KTIeZDts.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/add472bb64c474b3f06f493ee17526474d3fa6f6_2_690x494.jpeg" alt="image" data-base62-sha1="oNLLLMX8ECGILiLulc3KTIeZDts" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/add472bb64c474b3f06f493ee17526474d3fa6f6_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/add472bb64c474b3f06f493ee17526474d3fa6f6_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/add472bb64c474b3f06f493ee17526474d3fa6f6_2_1380x988.jpeg 2x" data-dominant-color="CAC7C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1569×1124 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @shai-ikko (2025-04-14 08:56 UTC)

<p>Indeed. I was on 5.6.2, and 5.8.1 does manage.</p>
<p>Thanks!</p>

---
