# Unable to load DICOM segmentation

**Topic ID**: 22947
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/unable-to-load-dicom-segmentation/22947

---

## Post #1 by @koeglfryderyk (2022-04-13 19:36 UTC)

<p>Operating system: Mac M1Pro macOS 12.3.1<br>
Slicer version: 4.13.0-2022-04-12 (also tested on 2022-04-04)<br>
Expected behaviour: Load DICOM segmentation<br>
Actual behaviour: Unable to load - error message</p>
<p>I’m trying to load a DICOM segmentation. I looked through other similar posts, but they didn’t help me.</p>
<p>Unfortunately I cannot share the file. I think the main error is this but I couldn’t figure out what to do next:</p>
<pre><code class="lang-auto">Convert DICOM Segmentation Image into ITK image(s) standard error:
E: No conversion from RLE Lossless to uncompressed transfer syntax possible!
</code></pre>
<p>Here is the entire error log (with detailed logging for DICOM enabled):</p>
<pre><code class="lang-auto">Examine for import using DICOMEnhancedUSVolumePlugin
Examine for import using DICOMGeAbusPlugin
Examine for import using DICOMImageSequencePlugin
Examine for import using DICOMPETSUVPlugin
Examine for import using DICOMParametricMapPlugin
DICOMParametricMapPluginClass : Using cached files
DICOMParametricMapPluginClass : Using cached files
Examine for import using DICOMRWVMPlugin
Examine for import using DICOMScalarVolumePlugin
Examine for import using DICOMSegmentationPlugin
DICOMSegmentationPluginClass : Using cached files
Examine for import using DICOMSlicerDataBundlePlugin
Examine for import using DICOMTID1500Plugin
DICOMTID1500PluginClass : Using cached files
DICOMTID1500PluginClass : Using cached files
Examine for import using DICOMVolumeSequencePlugin
Examine for import using Dcm2niixPlugin
['/Applications/Slicer.app/Contents/Extensions-30779/SlicerDcm2nii/lib/Slicer-4.13/qt-scripted-modules/Resources/bin/dcm2niix', '-n', '-1', '-s', 'y', '-f', '%p_%t_%s', '-i', 'y', '-o', '/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmp0cbs01az', '/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmp0cbs01az/input-dicom-files.txt']
Error: Compressed image stored as 38 fragments: decompress with gdcmconv, Osirix, dcmdjpeg or dcmjp2k /Users/fryderykkogl/Data/DICOM from Brainlab/find_seg/34099514/52880560
Chris Rorden's dcm2niiX version v1.0.20220412  (JP2:OpenJPEG) (JP-LS:CharLS) Clang10.0.0 x86-64 (64-bit MacOS)
Found 1 files in '/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmp0cbs01az/input-dicom-files.txt'
Found 1 DICOM file(s)
Image Decompression is new: please validate conversions
No valid DICOM images were found
DICOM Plugin failed: 'CalledProcessError' object has no attribute 'message'
Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-30779/SlicerDcm2nii/lib/Slicer-4.13/qt-scripted-modules/Dcm2niixPlugin.py", line 119, in examineFiles
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/Extensions-30779/SlicerDcm2nii/lib/Slicer-4.13/qt-scripted-modules/Resources/bin/dcm2niix', '-n', '-1', '-s', 'y', '-f', '%p_%t_%s', '-i', 'y', '-o', '/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmp0cbs01az', '/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmp0cbs01az/input-dicom-files.txt']' returned non-zero exit status 2.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules/DICOMLib/DICOMUtils.py", line 748, in getLoadablesFromFileLists
    loadablesByPlugin[plugin] = plugin.examine(fileLists)
  File "/Applications/Slicer.app/Contents/Extensions-30779/SlicerDcm2nii/lib/Slicer-4.13/qt-scripted-modules/Dcm2niixPlugin.py", line 29, in examine
    loadables += self.examineFiles(files)
  File "/Applications/Slicer.app/Contents/Extensions-30779/SlicerDcm2nii/lib/Slicer-4.13/qt-scripted-modules/Dcm2niixPlugin.py", line 121, in examineFiles
    logging.debug("Failed to examine files using dcm2niix: {0}".format(e.message))
AttributeError: 'CalledProcessError' object has no attribute 'message'
DICOM Plugin failed: 'CalledProcessError' object has no attribute 'message'
Examine for import using DicomRtImportExportPlugin
Examine for import using DicomSroImportExportPlugin
Examine for import using MultiVolumeImporterPlugin
MultiVolumeImporterPlugin: examine
MultiVolumeImporterPlugin: found 0 multivolumes!
MultiVolumeImporterPlugin: examineMultiseries
MultiVolumeImporterPlugin: found 0 multivolumes!
MultiVolumeImporterPlugin: found 0 loadables in 1 files in 0.0sec.
Examine for import using DICOMEnhancedUSVolumePlugin
Examine for import using DICOMGeAbusPlugin
Examine for import using DICOMImageSequencePlugin
Only one or few different trigger times found ({''}) - assuming this series is not a cine MRI
Examine for import using DICOMPETSUVPlugin
Examine for import using DICOMParametricMapPlugin
DICOMParametricMapPluginClass : Using cached files
DICOMParametricMapPluginClass : Using cached files
Examine for import using DICOMRWVMPlugin
Examine for import using DICOMScalarVolumePlugin
Examine for import using DICOMSegmentationPlugin
DICOMSegmentationPluginClass : Using cached files
DICOMSegmentationPluginClass : Using cached files
Examine for import using DICOMSlicerDataBundlePlugin
Examine for import using DICOMTID1500Plugin
DICOMTID1500PluginClass : Using cached files
DICOMTID1500PluginClass : Using cached files
Examine for import using DICOMVolumeSequencePlugin
Examine for import using Dcm2niixPlugin
['/Applications/Slicer.app/Contents/Extensions-30779/SlicerDcm2nii/lib/Slicer-4.13/qt-scripted-modules/Resources/bin/dcm2niix', '-n', '-1', '-s', 'y', '-f', '%p_%t_%s', '-i', 'y', '-o', '/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmp1o_j9tu0', '/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmp1o_j9tu0/input-dicom-files.txt']
Chris Rorden's dcm2niiX version v1.0.20220412  (JP2:OpenJPEG) (JP-LS:CharLS) Clang10.0.0 x86-64 (64-bit MacOS)
Found 192 files in '/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmp1o_j9tu0/input-dicom-files.txt'
Found 192 DICOM file(s)
Image Decompression is new: please validate conversions
	1565661178	/private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/tmp1o_j9tu0/3D_AX_T1_Nav_20181204111057_18
 /Users/fryderykkogl/Data/DICOM from Brainlab/find_seg/34099514/26278310
Conversion required 0.891678 seconds (0.891671 for core code).
Examine for import using DicomRtImportExportPlugin
Examine for import using DicomSroImportExportPlugin
Examine for import using MultiVolumeImporterPlugin
MultiVolumeImporterPlugin: examine
MultiVolumeImporterPlugin: found 1 multivolumes!
MultiVolumeImporterPlugin: examineMultiseries
MultiVolumeImporterPlugin: found 0 multivolumes!
MultiVolumeImporterPlugin: found 0 loadables in 192 files in 0.1sec.
DICOM SEG load()
in load(): uid = 1.2.276.0.20.1.4.35.923849970726.192.1544626175.288056.0
SEG2NRRD did not complete successfully, unable to load DICOM Segmentation
Cleaning up temporarily created directory /private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/QIICR/SEG/2022-04-13_152424/1.2.276.0.20.1.4.35.923849970726.192.1544626175.288056.0
Could not load: Objects as a DICOMSegmentation
Found CommandLine Module, target is  /Applications/Slicer.app/Contents/Extensions-30779/DCMQI/lib/Slicer-4.13/cli-modules/segimage2itkimage
ModuleType: CommandLineModule
Convert DICOM Segmentation Image into ITK image(s) command line: 

/Applications/Slicer.app/Contents/Extensions-30779/DCMQI/lib/Slicer-4.13/cli-modules/segimage2itkimage --inputDICOM /Users/fryderykkogl/Data/DICOM from Brainlab/find_seg/34099514/52880560 --outputDirectory /private/var/folders/sj/w4lgym6n0qx3j46fzwdrv3x80000gn/T/Slicer-fryderykkogl/QIICR/SEG/2022-04-13_152424/1.2.276.0.20.1.4.35.923849970726.192.1544626175.288056.0 --outputType nrrd 

Convert DICOM Segmentation Image into ITK image(s) standard output:

dcmqi repository URL: https://github.com/QIICR/dcmqi.git revision: a3c9e4a tag: latest

Convert DICOM Segmentation Image into ITK image(s) standard error:

E: No conversion from RLE Lossless to uncompressed transfer syntax possible!
ERROR: Failed to load segmentation dataset! Cannot decompress
Fatal error encountered.



Convert DICOM Segmentation Image into ITK image(s) completed with errors



SEG2NRRD did not complete successfully, unable to load DICOM Segmentation
Could not load: Objects as a DICOMSegmentation```</code></pre>

---

## Post #2 by @pieper (2022-04-13 19:43 UTC)

<p>Where did the SEG file come from?  Is it possible for you to generate a sharable file from that system? (e.g. of a phantom).</p>

---

## Post #3 by @pieper (2022-04-13 19:44 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="1" data-topic="22947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<pre><code class="lang-auto">Convert DICOM Segmentation Image into ITK image(s) standard error:
E: No conversion from RLE Lossless to uncompressed transfer syntax possible!
</code></pre>
</blockquote>
</aside>
<p>Also FYI this message means the data is in “Run Length Encoded” (RLE) so if there’s a chance to change to a different transfer syntax (on the source of the SEG) you could try that.</p>

---

## Post #4 by @koeglfryderyk (2022-04-13 19:44 UTC)

<p>It comes from the Brainlab Curve navigation system in the AMIGO suite.</p>
<p>I will try and generate a sharable file</p>

---

## Post #5 by @pieper (2022-04-13 19:45 UTC)

<p>Yes, good.  We should be able to make that work.</p>

---

## Post #6 by @lassoan (2022-04-13 20:54 UTC)

<p>We use DCMQI’s DICOM Segmentation Object converter. Developers of this tool, with close consultation with DICOM experts, concluded that it is not a good idea to use RLE encoding on top of bitpacking and so they do not support it, either for reading or writing. See some information <a href="https://discourse.slicer.org/t/dicom-rle-support-in-slicer/17656/5">here</a>.</p>
<p>If you remove the RLE transfer syntax from your DICOM C-store SCP configuration and send the segmentation from BrainLab again then you will get the segmentation in an uncompressed format.</p>

---

## Post #7 by @koeglfryderyk (2022-04-13 22:06 UTC)

<p>Ok, good to know.</p>
<p>Just to make sure that I understand this correctly - removing the RLE transfer syntax would have to be done on the Brainlab device before pulling the data?</p>
<p>And does this mean removing this DICOM tag completely, or changing it to something else?</p>

---

## Post #8 by @lassoan (2022-04-13 22:25 UTC)

<p>There is a transfer syntax negotiation between the C-STORE SCU (Brainlab) and C-STORE SCP (whatever DICOM store provider tool you use). The negotiation ends when a transfer syntax is found that the SCU can provide and the SCP can accept.</p>
<p>Therefore, you don’t need to touch anything in Brainlab DICOM configuration, just make sure you configure your SCP to not accept RLE for DICOM Segmentation Objects.</p>
<p>Do you receive the DICOM Segmentation Object using Slicer’s DICOM module (DICOM networking / Storage listener)? Or do you use DCMTK’s <code>storescp</code> tool directly? Either way, I would recommend to create a custom storescp.cfg file and remove the line that refers to RLE compression:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/Resources/DICOM/dcmtk/storescu-seg.cfg#L35">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/Resources/DICOM/dcmtk/storescu-seg.cfg#L35" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/Resources/DICOM/dcmtk/storescu-seg.cfg#L35" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/Resources/DICOM/dcmtk/storescu-seg.cfg#L35</a></h4>



    <pre class="onebox">      <code class="lang-cfg">
        <ol class="start lines" start="25" style="counter-reset: li-counter 24 ;">
            <li>TransferSyntax2 = BigEndianExplicit</li>
            <li>TransferSyntax3 = LittleEndianImplicit</li>
            <li>
            </li>
<li>[JPEGBaseline]</li>
            <li>TransferSyntax1 = JPEGBaseline</li>
            <li>
            </li>
<li>[JPEGLossless]</li>
            <li>TransferSyntax1 = JPEGLossless:Non-hierarchical-1stOrderPrediction</li>
            <li>
            </li>
<li>[RLE]</li>
            <li class="selected">TransferSyntax1 = RLELossless</li>
            <li>
            </li>
<li>[MPEG2]</li>
            <li>TransferSyntax1 = MPEG2MainProfile@MainLevel</li>
            <li>
            </li>
<li>[MPEG4]</li>
            <li>TransferSyntax1 = MPEG4HighProfile/Level4.1</li>
            <li>
            </li>
<li># ============================================================================</li>
            <li>[[PresentationContexts]]</li>
            <li># ============================================================================</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And make sure you have uncompressed transfer syntaxes:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/78073d283813d83d4152800a478be329e0b141f2/Modules/Scripted/DICOMLib/Resources/DICOM/dcmtk/storescu-seg.cfg#L24-L26">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/78073d283813d83d4152800a478be329e0b141f2/Modules/Scripted/DICOMLib/Resources/DICOM/dcmtk/storescu-seg.cfg#L24-L26" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/78073d283813d83d4152800a478be329e0b141f2/Modules/Scripted/DICOMLib/Resources/DICOM/dcmtk/storescu-seg.cfg#L24-L26" target="_blank" rel="noopener">Slicer/Slicer/blob/78073d283813d83d4152800a478be329e0b141f2/Modules/Scripted/DICOMLib/Resources/DICOM/dcmtk/storescu-seg.cfg#L24-L26</a></h4>



    <pre class="onebox">      <code class="lang-cfg">
        <ol class="start lines" start="24" style="counter-reset: li-counter 23 ;">
            <li>TransferSyntax1 = LittleEndianExplicit</li>
            <li>TransferSyntax2 = BigEndianExplicit</li>
            <li>TransferSyntax3 = LittleEndianImplicit</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It may worth checking if there is some configuration settings in Brainlab that would force sending DICOM Segmentation Object without RLE compression. If there is a setting for that then you could use it instead of changing your SCP’s DICOM configuration.</p>

---

## Post #9 by @koeglfryderyk (2022-04-13 22:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="22947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It may worth checking if there is some configuration settings in Brainlab that would force sending DICOM Segmentation Object without RLE compression. If there is a setting for that then you could use it instead of changing your SCP’s DICOM configuration.</p>
</blockquote>
</aside>
<p>I think this is the only option for me, because the only thing I am doing on the receiving side is attaching an external disk to the Brainlab device and then the Brainlab device moves/exports the DICOMs onto it</p>

---

## Post #10 by @pieper (2022-04-13 22:49 UTC)

<p>It would be good to check if Brainlab has a configuration option for saving bit packed or uncompressed seg.  In any case if this is common enough that a major vendor supports it then we should reconsider at least adding read support to dcmqi.  <a class="mention" href="/u/fedorov">@fedorov</a> what do you think?</p>

---

## Post #11 by @fedorov (2022-04-14 04:48 UTC)

<p>Maybe <a href="https://support.dcmtk.org/docs/dcmconv.html">dcmconv</a> can help here to go between transfer syntaxes? Should at least experiment with it.</p>

---

## Post #12 by @koeglfryderyk (2022-04-14 20:34 UTC)

<p>Thanks for the tip!<br>
dcmconv actually didn’t work, that was the error:</p>
<pre><code class="lang-auto">E: Pixel representation cannot be changed
F: no conversion to transfer syntax Little Endian Explicit possible!
</code></pre>
<p>But decoding with <a href="https://support.dcmtk.org/docs/dcmdrle.html" rel="noopener nofollow ugc">dcmdrle</a> worked.</p>
<p>Does it matters which output syntax I use? There were three and all of them worked (the same ones as mentioned above by <a class="mention" href="/u/lassoan">@lassoan</a>):</p>
<blockquote>
<p>write with explicit VR little endian (default)<br>
write with explicit VR big endian TS<br>
write with implicit VR little endian TS</p>
</blockquote>

---

## Post #13 by @pieper (2022-04-14 20:37 UTC)

<p>Glad that worked!  Probably that same <code>drle</code> feature of DCMTK could be added to dcmqi if someone wants to do a little C++ development.</p>
<p>I don’t think the output transfer syntax matters since most packages recognize any of them, but I would stick with explicit VR little endian.</p>

---

## Post #14 by @lassoan (2022-04-15 12:15 UTC)

<p>Little/big endian means if you need byte-swapping when decoding on a big/little endian system. Since most systems are little-endian it makes sense to use little endian.</p>
<p>Explicit VR means that value representation (data type) information is stored in the file, and so it does not have to be looked up in an external DICOM dictionary. Considering that the value representation takes only 2 bytes and it makes parsing simpler and more feasible for private tags, it makes sense to use explicit VR.</p>
<p>So, I agree with <a class="mention" href="/u/pieper">@pieper</a> that explicit VR little endian is a good default choice.</p>

---

## Post #15 by @fedorov (2022-04-15 15:05 UTC)

<p><a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> do you have a sample dataset with segmentation and matching MR image to share with me? We can check off this list with Tina, but I think I may already be listed on the IRB you are using for data collection.</p>

---

## Post #16 by @fedorov (2022-06-10 20:36 UTC)

<p>To follow up on this, Fryderyk shared a sample with me, and there was a bug in dcmqi that registered RLE codec <em>after</em> loading DICOM SEG, which was a problem, but it is now fixed. <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> we had some email exchange where I believe you mentioned the issues is now resolved in stable release, but could you please confirm here so we can close the thread?</p>

---
