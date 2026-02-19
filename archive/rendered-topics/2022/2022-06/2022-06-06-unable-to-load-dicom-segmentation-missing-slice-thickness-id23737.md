---
topic_id: 23737
title: "Unable To Load Dicom Segmentation Missing Slice Thickness"
date: 2022-06-06
url: https://discourse.slicer.org/t/23737
---

# Unable to load DICOM segmentation - missing slice thickness

**Topic ID**: 23737
**Date**: 2022-06-06
**URL**: https://discourse.slicer.org/t/unable-to-load-dicom-segmentation-missing-slice-thickness/23737

---

## Post #1 by @koeglfryderyk (2022-06-06 15:58 UTC)

<p>I’m unable to load a DICOM segmentation.</p>
<p>The segmentation was created by the Brainlab Curve navigation system in the AMIGO suite.<br>
I unfortunately cannot share the file.</p>
<p>Tested on the latest preview version (version 5.1.0, revision 30987, built 2022-06-02) and the stable release.</p>
<p>I was tempted to ignore this and just assume that the file was faulty, but:</p>
<ul>
<li>this was the case for more than one file</li>
<li>I could open the segmentation with other software (<a href="https://www.imfusion.com/resources/download" rel="noopener nofollow ugc">ImFusion Suite Demo Version</a> to be specific)</li>
</ul>
<p>This is the full error log (detailed logging enabled):</p>
<blockquote>
<p>Examine for import using DICOMEnhancedUSVolumePlugin<br>
Examine for import using DICOMGeAbusPlugin<br>
Examine for import using DICOMImageSequencePlugin<br>
Examine for import using DICOMPETSUVPlugin<br>
Examine for import using DICOMParametricMapPlugin<br>
DICOMParametricMapPluginClass : Caching files<br>
DICOMParametricMapPluginClass : Using cached files<br>
Examine for import using DICOMRWVMPlugin<br>
Examine for import using DICOMScalarVolumePlugin<br>
Examine for import using DICOMSegmentationPlugin<br>
DICOMSegmentationPluginClass : Caching files<br>
DICOM SEG modality found<br>
Examine for import using DICOMSlicerDataBundlePlugin<br>
Examine for import using DICOMTID1500Plugin<br>
DICOMTID1500PluginClass : Caching files<br>
DICOMTID1500PluginClass : Using cached files<br>
Examine for import using DICOMVolumeSequencePlugin<br>
Examine for import using Dcm2niixPlugin<br>
[‘/Applications/Slicer.app/Contents/Extensions-30987/SlicerDcm2nii/lib/Slicer-5.1/qt-scripted-modules/Resources/bin/dcm2niix’, ‘-n’, ‘-1’, ‘-s’, ‘y’, ‘-f’, ‘%p_%t_%s’, ‘-i’, ‘y’, ‘-o’, ‘/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmpearfjf5v’, ‘/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmpearfjf5v/input-dicom-files.txt’]<br>
Chris Rorden’s dcm2niiX version v1.0.20220505 (JP2:OpenJPEG) (JP-LS:CharLS) Clang10.0.0 x86-64 (64-bit MacOS)<br>
Found 1 files in ‘/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmpearfjf5v/input-dicom-files.txt’<br>
Found 1 DICOM file(s)<br>
Ignoring derived image(s) of series 82 /Users/fryderykkogl/Data/DICOM from Brainlab/p3_how/99398381/43232200_decompressed<br>
Conversion required 0.002901 seconds (0.002893 for core code).<br>
Examine for import using DicomRtImportExportPlugin<br>
Examine for import using DicomSroImportExportPlugin<br>
Examine for import using MultiVolumeImporterPlugin<br>
MultiVolumeImporterPlugin: examine<br>
MultiVolumeImporterPlugin: found 0 multivolumes!<br>
MultiVolumeImporterPlugin: examineMultiseries<br>
MultiVolumeImporterPlugin: found 0 multivolumes!<br>
MultiVolumeImporterPlugin: found 0 loadables in 1 files in 0.0sec.<br>
DICOM SEG load()<br>
in load(): uid = 1.2.276.0.20.1.4.72.550353941687.11068.1606854664.323220.0<br>
SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
Cleaning up temporarily created directory /private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/QIICR/SEG/2022-06-06_115042/1.2.276.0.20.1.4.72.550353941687.11068.1606854664.323220.0<br>
Could not load: Objects as a DICOMSegmentation<br>
Found CommandLine Module, target is /Applications/Slicer.app/Contents/Extensions-30987/DCMQI/lib/Slicer-5.1/cli-modules/segimage2itkimage<br>
ModuleType: CommandLineModule<br>
Convert DICOM Segmentation Image into ITK image(s) command line:<br>
/Applications/Slicer.app/Contents/Extensions-30987/DCMQI/lib/Slicer-5.1/cli-modules/segimage2itkimage --inputDICOM /Users/fryderykkogl/Data/DICOM from Brainlab/p3_how/99398381/43232200_decompressed --outputDirectory /private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/QIICR/SEG/2022-06-06_115042/1.2.276.0.20.1.4.72.550353941687.11068.1606854664.323220.0 --outputType nrrd<br>
Convert DICOM Segmentation Image into ITK image(s) standard output:<br>
dcmqi repository URL: <a href="https://github.com/QIICR/dcmqi.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - QIICR/dcmqi: dcmqi (DICOM for Quantitative Imaging) is a free, open source C++ library for conversion between imaging research formats and the standard DICOM representation for image analysis results</a> revision: e25cb30 tag: latest<br>
Row direction: 1 4.897e-12 -0<br>
Col direction: -4.897e-12 1 0<br>
Z direction: 0 0 1<br>
Total frames: 287<br>
Total frames with unique IPP: 287<br>
Total overlapping frames: 0<br>
Origin: [-141.62, -167.528, -39.7066]<br>
Convert DICOM Segmentation Image into ITK image(s) standard error:<br>
ERROR: No sufficient information to derive slice spacing! Unable to interpret the data.<br>
Fatal error encountered.<br>
Convert DICOM Segmentation Image into ITK image(s) completed with errors<br>
SEG2NRRD did not complete successfully, unable to load DICOM Segmentation<br>
Could not load: Objects as a DICOMSegmentation</p>
</blockquote>

---

## Post #2 by @pieper (2022-06-06 16:28 UTC)

<p>Thanks for the report <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a>.  To make this reproducible can you please generate a sharable segmentation instance using phantom data?  There is a well-known issue with dicom segmentations being ambiguous if the slice thickness is not included so this is probably an issue that should be reported as an issue to Brainlab but it is also possible that there’s a workaround so that it isn’t a bottleneck for you. <a class="mention" href="/u/fedorov">@fedorov</a></p>

---

## Post #3 by @fedorov (2022-06-06 16:52 UTC)

<p>A workaround could potentially be to use <a href="https://support.dcmtk.org/docs/dcmodify.html">dcmodify</a> and patch the SEG instances by adding <code>SliceThickness</code> with the value taken from the corresponding MR series to <code>SharedFunctionalGroupsSequence[0] &gt; PixelMeasuresSequence[0] </code> (or you would need to create that sequence if it does not exist).</p>
<p>Of course, this assumes that SEG has the same geometry as the source MR series, which in the general case cannot be assumed.</p>
<p>Below is the example of the relevant part of a SEG series from BrainLab phantom study you shared with me earlier Fryderyk - the file should have something like this after you patch it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16415b3d60ab15e0f532999dd8dbb0e3b03babac.png" data-download-href="/uploads/short-url/3aSwQyKRtQ8y0kFLCunRmmSXquU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16415b3d60ab15e0f532999dd8dbb0e3b03babac.png" alt="image" data-base62-sha1="3aSwQyKRtQ8y0kFLCunRmmSXquU" width="690" height="249" data-dominant-color="393B44"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">881×319 67.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
