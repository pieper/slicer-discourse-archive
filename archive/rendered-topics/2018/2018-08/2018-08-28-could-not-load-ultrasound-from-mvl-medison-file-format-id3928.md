# Could not load ultrasound from .mvl (Medison) file format

**Topic ID**: 3928
**Date**: 2018-08-28
**URL**: https://discourse.slicer.org/t/could-not-load-ultrasound-from-mvl-medison-file-format/3928

---

## Post #1 by @Agustin_Gudino (2018-08-28 17:40 UTC)

<p>Hello!</p>
<p>“Could not load:  - as a 48 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume”</p>
<p>Just received that error trying to load the DICOM information from an ecography. 3D/4D data in “.mvl” (Medison Volume) format.</p>
<p>Anyone can help, new to the software here.</p>
<p>Best Regards and thanks in advance</p>
<p>Operating system: MACOSX HIGH SIERRA<br>
Slicer version:  4.8.1<br>
Expected behavior:  load dicom ecography<br>
Actual behavior: Could not load:  - as a 48 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume</p>

---

## Post #2 by @fedorov (2018-08-28 20:16 UTC)

<p>Please review the following articles from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ">Slicer FAQ</a> and let us know the result:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#When_I_click_on_.22Load_selection_to_slicer.22_I_get_an_error_message_.22Could_not_load_..._as_a_scalar_volume.22">When I click on “Load selection to slicer” I get an error message “Could not load … as a scalar volume”</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser">I try to import a directory of DICOM files, but nothing shows up in the browser</a></li>
</ul>

---

## Post #3 by @lassoan (2018-08-28 21:38 UTC)

<p><a href="https://github.com/SlicerHeart/SlicerHeart">SlicerHeart extension</a> has 3D/4D ultrasound importers for Philips and GE systems.</p>
<p>As far as I know Medison MVL format is a closed, proprietary format, not even DICOM. If sufficient number of input files are available then probably the format can be reverse-engineered (as it was done by <a href="http://www.tomovision.com/products/format_image.html">TomoVision</a> developers), but it would take a couple of weeks of work, which would require dedicated funding.</p>
<p>I would recommend trying the followings:</p>
<ul>
<li>Check if you can export to Cartesian DICOM file format and then try to import it as <a class="mention" href="/u/fedorov">@fedorov</a> recommended above. If you don’t find an option like that then ask your Medison representative about what export options are available.</li>
<li>Try import using TomoVision. If import works, contact TomoVision developers, asking for image export in NRRD format.</li>
</ul>
<p>It is important to make ultrasound manufacturers aware that they are hurting researchers by using closed, proprietary file formats. When you buy a new ultrasound system make sure you buy one that can export images in a format that can be freely accessed - preferably in DICOM format.</p>

---

## Post #4 by @Agustin_Gudino (2018-08-28 21:40 UTC)

<p>I guess I figured out that there was a lot of files inside the directory and that lead me to open files individually…sorry for my lack of knowledge…learning over this.</p>
<p>The thing is that I opened a single file and the R view shows it ok…but the Y and G shows what it should be other dimensions views but they are really shrinked…<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f81aa1f5d65f76193f9c90f53c873caf3fe4270.png" data-download-href="/uploads/short-url/ktw5a677Pktg7tb2OUEE5ayrrrO.png?dl=1" title="pol6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f81aa1f5d65f76193f9c90f53c873caf3fe4270_2_553x500.png" alt="pol6" data-base62-sha1="ktw5a677Pktg7tb2OUEE5ayrrrO" width="553" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f81aa1f5d65f76193f9c90f53c873caf3fe4270_2_553x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f81aa1f5d65f76193f9c90f53c873caf3fe4270_2_829x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f81aa1f5d65f76193f9c90f53c873caf3fe4270_2_1106x1000.png 2x" data-dominant-color="455768"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pol6</span><span class="informations">1472×1330 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I it does not create the 3d mesh correctly…any suggestion?</p>

---

## Post #5 by @lassoan (2018-08-28 21:46 UTC)

<p>The pictures above show just secondary captures (screenshots). Probably the 3D image information is stored in private DICOM fields in the same files. If you can share anonymized data sets then we can have a look at them to confirm.</p>

---

## Post #6 by @Paroxistico (2019-01-27 15:14 UTC)

<p>Hi everyone. I’m in the same boat. The USS machine I used was a Samsung UGEO_HM70A. Tried with Tomovision Babysliceo(demo) and I could see the baby and edit everything but it’s quite expensive for a couple of mvl files I want to edit/use.</p>
<p>If anyone is working on these kind of files (mvl), feel free to get all of them from my dropbox. All of them are anonimyzed and exported as 3d volume, default mode.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/azdck7h9e7b71dq/AACiHg-m-XPOhj2vs2_CFGK5a?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/azdck7h9e7b71dq/AACiHg-m-XPOhj2vs2_CFGK5a?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/azdck7h9e7b71dq/AACiHg-m-XPOhj2vs2_CFGK5a?dl=0" target="_blank" rel="noopener nofollow ugc">Mvl</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Grretings from Spain</p>

---

## Post #7 by @lassoan (2019-01-27 16:30 UTC)

<p>Thanks for sharing the data. It is easy to load these images once you know the image geometry (pixel start position and x y z size and spacing) just by creating a .nhdr header file for it. The geometry values can be determined by trial and error. <a href="https://na-mic.github.io/ProjectWeek/PW30_2019_GranCanaria/Projects/RawImageGuess/">One of the projects for the Slicer project week</a> (that starts tomorrow) will be about automating this process - your data sets will be perfect test data for this.</p>
<p>For example, you can load one of your data sets by creating a “DAN 1_0000.nhdr” file in the same folder with the content below and then loading the .nhdr file into Slicer:</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: unsigned char
dimension: 3
space: left-posterior-superior
sizes: 376 124 158
space directions: (-0.30,0,0) (0,-0.60,0) (0,0,0.90)
kinds: domain domain domain
endian: little
encoding: raw
space origin: (0,0,0)
byte skip: 620919
data file: DAN 1_0000.mvl
</code></pre>
<p>After applying masking (to remove some reflections that would occlude the face), casting to double, and applying anisotropic filtering, you get this volume rendering result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98d3ac54995b58d86f06d06fdd11c8706142e356.jpeg" data-download-href="/uploads/short-url/lNY59IPN6N5beDlKyYBKgy2Mpvg.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98d3ac54995b58d86f06d06fdd11c8706142e356_2_558x500.jpeg" alt="image" data-base62-sha1="lNY59IPN6N5beDlKyYBKgy2Mpvg" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98d3ac54995b58d86f06d06fdd11c8706142e356_2_558x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98d3ac54995b58d86f06d06fdd11c8706142e356_2_837x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98d3ac54995b58d86f06d06fdd11c8706142e356_2_1116x1000.jpeg 2x" data-dominant-color="3B3A3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1379×1234 313 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here is the link to the complete <a href="https://1drv.ms/u/s!Arm_AFxB9yqHtuR-017KI3_m1NuYPA">Slicer scene</a> of the imported and processed image.</p>

---

## Post #8 by @Paroxistico (2019-01-27 20:25 UTC)

<p>Hi again</p>
<p>Thank you so much for your explanation and I’m really glad that you found useful these data sets for the Slicer project week.</p>
<p>On the other hand I tried doing myself following your steps and using the same file and when I import or drag the nhdr file I created I’m still getting 3 black screens. Do I need any specific extension? I tried importing as a volume, sequence of volumes, etc without success.</p>
<p>Regards</p>

---

## Post #9 by @lassoan (2019-01-27 22:19 UTC)

<p>Create the nhdr in the same folder as the .mvl file. If the image does not load correctly then please post the application log (menu: Help / Report a bug).</p>

---

## Post #10 by @Paroxistico (2019-01-29 10:19 UTC)

<p>Both are in the same folder. Here is the log.</p>
<details>
<summary>
Logs</summary>
<pre>
[DEBUG][Qt] 29.01.2019 11:13:24 [] (unknown:0) - Session start time .......: 2019-01-29 11:13:24
[DEBUG][Qt] 29.01.2019 11:13:24 [] (unknown:0) - Slicer version ...........: 4.10.1 (revision 27931) win-amd64 - installed release
[DEBUG][Qt] 29.01.2019 11:13:24 [] (unknown:0) - Operating system .........: Windows /  Professional /  (Build 9200) - 64-bit
[DEBUG][Qt] 29.01.2019 11:13:24 [] (unknown:0) - Memory ...................: 16331 MB physical, 18763 MB virtual
[DEBUG][Qt] 29.01.2019 11:13:24 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 5 1600X Six-Core Processor           , 12 cores, 12 logical processors
[DEBUG][Qt] 29.01.2019 11:13:24 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 29.01.2019 11:13:24 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 29.01.2019 11:13:24 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 29.01.2019 11:13:24 [] (unknown:0) - Additional module paths ..: C:/Users/chinl/AppData/Roaming/NA-MIC/Extensions-27931/DCMQI/lib/Slicer-4.10/cli-modules, C:/Users/chinl/AppData/Roaming/NA-MIC/Extensions-27931/SlicerDMRI/lib/Slicer-4.10/cli-modules, C:/Users/chinl/AppData/Roaming/NA-MIC/Extensions-27931/SlicerDMRI/lib/Slicer-4.10/qt-loadable-modules, C:/Users/chinl/AppData/Roaming/NA-MIC/Extensions-27931/SlicerDMRI/lib/Slicer-4.10/qt-scripted-modules, C:/Users/chinl/AppData/Roaming/NA-MIC/Extensions-27931/SlicerHeart/lib/Slicer-4.10/qt-loadable-modules, C:/Users/chinl/AppData/Roaming/NA-MIC/Extensions-27931/SlicerHeart/lib/Slicer-4.10/qt-scripted-modules, C:/Users/chinl/AppData/Roaming/NA-MIC/Extensions-27931/Sequences/lib/Slicer-4.10/qt-loadable-modules, C:/Users/chinl/AppData/Roaming/NA-MIC/Extensions-27931/Sequences/lib/Slicer-4.10/qt-scripted-modules, C:/Users/chinl/AppData/Roaming/NA-MIC/Extensions-27931/SlicerITKUltrasound/lib/Slicer-4.10/cli-modules
[DEBUG][Python] 29.01.2019 11:13:25 [Python] (D:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 29.01.2019 11:13:26 [Python] (D:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 29.01.2019 11:13:26 [Python] (D:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 29.01.2019 11:13:26 [] (unknown:0) - Switch to module:  "Welcome"
[INFO][Stream] 29.01.2019 11:13:41 [] (unknown:0) - starting storescp process
[INFO][Stream] 29.01.2019 11:13:41 [] (unknown:0) - (u'Starting D:/Program Files/Slicer 4.10.1/bin/../bin\\storescp.exe with ', ['11112', '--accept-all', '--output-directory', u'C:/Users/chinl/OneDrive/Documentos\\SlicerDICOMDatabase/incoming', '--exec-sync', '--exec-on-reception', u'D:/Program Files/Slicer 4.10.1/bin/../bin\\dcmdump.exe --load-short --print-short --print-filename --search PatientName "C:/Users/chinl/OneDrive/Documentos\\SlicerDICOMDatabase/incoming/#f"'])
[INFO][Stream] 29.01.2019 11:13:41 [] (unknown:0) - process D:/Program Files/Slicer 4.10.1/bin/../bin\storescp.exe now in state Starting
[INFO][Stream] 29.01.2019 11:13:41 [] (unknown:0) - process D:/Program Files/Slicer 4.10.1/bin/../bin\storescp.exe now in state Running
[ERROR][VTK] 29.01.2019 11:15:07 [vtkITKArchetypeDiffusionTensorImageReaderFile (0000017CB56A6170): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/DAN 1_0000.nhdr. ITK exception info: error in unknown: itk::ERROR: NrrdImageIO(0000017CBB0781C0)] (D:\D\S\Slicer-4101\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:622) - ReadImageInformation: Error reading D:/DAN 1_0000.nhdr:
[nrrd] nrrdLoad: trouble reading "D:/DAN 1_0000.nhdr"
[nrrd] nrrdRead: trouble
[nrrd] _nrrdRead: trouble reading NRRD file
[nrrd] _nrrdFormatNRRD_read: hit end of header, but no "data file" given
[ERROR][VTK] 29.01.2019 11:15:07 [vtkCompositeDataPipeline (0000017CBAD2EB40)] (D:\D\S\Slicer-4101-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(0000017CB56A6170) returned failure for request: vtkInformation (0000017CBB2D35E0)
  Debug: Off
  Modified Time: 301563
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 29.01.2019 11:15:07 [vtkITKArchetypeImageSeriesVectorReaderSeries (0000017CB56A52F0): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/DAN 1_0000.nhdr. ITK exception info: error in unknown: itk::ERROR: NrrdImageIO(0000017CBB075470)] (D:\D\S\Slicer-4101\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:622) - ReadImageInformation: Error reading D:/DAN 1_0000.nhdr:
[nrrd] nrrdLoad: trouble reading "D:/DAN 1_0000.nhdr"
[nrrd] nrrdRead: trouble
[nrrd] _nrrdRead: trouble reading NRRD file
[nrrd] _nrrdFormatNRRD_read: hit end of header, but no "data file" given
[ERROR][VTK] 29.01.2019 11:15:07 [vtkCompositeDataPipeline (0000017CBAD2FEF0)] (D:\D\S\Slicer-4101-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries(0000017CB56A52F0) returned failure for request: vtkInformation (0000017CBB2CFB70)
  Debug: Off
  Modified Time: 303052
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 29.01.2019 11:15:07 [vtkITKArchetypeImageSeriesVectorReaderFile (0000017CB56A5690): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/DAN 1_0000.nhdr. ITK exception info: error in unknown: itk::ERROR: NrrdImageIO(0000017CBB076280)] (D:\D\S\Slicer-4101\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:622) - ReadImageInformation: Error reading D:/DAN 1_0000.nhdr:
[nrrd] nrrdLoad: trouble reading "D:/DAN 1_0000.nhdr"
[nrrd] nrrdRead: trouble
[nrrd] _nrrdRead: trouble reading NRRD file
[nrrd] _nrrdFormatNRRD_read: hit end of header, but no "data file" given
[ERROR][VTK] 29.01.2019 11:15:07 [vtkCompositeDataPipeline (0000017CBAD2FA40)] (D:\D\S\Slicer-4101-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesVectorReaderFile(0000017CB56A5690) returned failure for request: vtkInformation (0000017CBB2D5070)
  Debug: Off
  Modified Time: 303147
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 29.01.2019 11:15:07 [vtkITKArchetypeImageSeriesScalarReader (0000017CB56A6510): vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open D:/DAN 1_0000.nhdr. ITK exception info: error in unknown: itk::ERROR: NrrdImageIO(0000017CBB0779F0)] (D:\D\S\Slicer-4101\Libs\vtkITK\vtkITKArchetypeImageSeriesReader.cxx:622) - ReadImageInformation: Error reading D:/DAN 1_0000.nhdr:
[nrrd] nrrdLoad: trouble reading "D:/DAN 1_0000.nhdr"
[nrrd] nrrdRead: trouble
[nrrd] _nrrdRead: trouble reading NRRD file
[nrrd] _nrrdFormatNRRD_read: hit end of header, but no "data file" given
[ERROR][VTK] 29.01.2019 11:15:07 [vtkCompositeDataPipeline (0000017CBAD2FD10)] (D:\D\S\Slicer-4101-build\VTK\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(0000017CB56A6510) returned failure for request: vtkInformation (0000017CBB2D25F0)
  Debug: Off
  Modified Time: 303930
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_INFORMATION
  FORWARD_DIRECTION: 0
  ALGORITHM_AFTER_FORWARD: 1
[ERROR][VTK] 29.01.2019 11:15:07 [vtkMRMLNRRDStorageNode (0000017CB98F0F30)] (D:\D\S\Slicer-4101\Libs\MRML\Core\vtkMRMLNRRDStorageNode.cxx:189) - ReadData: This is not a nrrd file
[ERROR][VTK] 29.01.2019 11:15:07 [vtkMRMLVolumeArchetypeStorageNode (0000017CB8E0B5B0)] (D:\D\S\Slicer-4101\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:379) - ReadData: Cannot read file as a volume of type DiffusionTensorVolume[fullName = D:/DAN 1_0000.nhdr]
	Number of files listed in the node = 0.
	File reader says it was able to read 1 files.
	File reader used the archetype file name of D:/DAN 1_0000.nhdr [reader 0th file name = D:/DAN 1_0000.nhdr]
FileFormatError
[ERROR][VTK] 29.01.2019 11:15:07 [vtkMRMLNRRDStorageNode (0000017CB98F6F40)] (D:\D\S\Slicer-4101\Libs\MRML\Core\vtkMRMLNRRDStorageNode.cxx:189) - ReadData: This is not a nrrd file
[ERROR][VTK] 29.01.2019 11:15:07 [vtkMRMLVolumeArchetypeStorageNode (0000017CB8E0B5B0)] (D:\D\S\Slicer-4101\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:315) - ReadData: Failed to instantiate a file reader
[ERROR][VTK] 29.01.2019 11:15:07 [vtkMRMLVolumeArchetypeStorageNode (0000017CB8E0C690)] (D:\D\S\Slicer-4101\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:379) - ReadData: Cannot read file as a volume of type Volume[fullName = D:/DAN 1_0000.nhdr]
	Number of files listed in the node = 0.
	File reader says it was able to read 1 files.
	File reader used the archetype file name of D:/DAN 1_0000.nhdr [reader 0th file name = D:/DAN 1_0000.nhdr]
FileFormatError
</pre>
</details>

---

## Post #11 by @lassoan (2019-01-30 01:42 UTC)

<p>It seems that the file that you created is not valid (maybe end-of-line character is not what is expected or a new-line is missing from the end of the file, etc). You can download a working header file from here: <a href="https://1drv.ms/u/s!Arm_AFxB9yqHtuR5XyPS9kbrOrCPIA" rel="nofollow noopener">https://1drv.ms/u/s!Arm_AFxB9yqHtuR5XyPS9kbrOrCPIA</a></p>

---

## Post #12 by @Paroxistico (2019-01-30 09:33 UTC)

<p>Thanks for your answer. Stupid thing, but just adding a new empty line after the name of the mvl file <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=6" title=":thinking:" class="emoji" alt=":thinking:"></p>

---

## Post #13 by @e36alpine (2019-02-05 13:39 UTC)

<p>I followed along with your instructions to create the .nhdr file which I can now at least get the .mvl file from our Samsung RS85 loaded in as a volume.  Question is what’s the easiest way to figure out the proper pixel start position and x y z size and spacing?  I’ve tried just randomly changing the image spacing and origin with no success.  Just see a bunch of white lines and dots.  Any help is appreciated.  Thanks!</p>

---

## Post #14 by @lassoan (2019-02-05 14:13 UTC)

<p>A module was developed last week at the Slicer project week for finding out image dimensions: <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess" rel="nofollow noopener">https://github.com/acetylsalicyl/SlicerRawImageGuess</a></p>
<p>The module could be improved to generate a .mhd header from the determined values.</p>
<p><a class="mention" href="/u/nagy.attila">@nagy.attila</a></p>

---

## Post #15 by @e36alpine (2019-02-06 18:13 UTC)

<p>Is there a trick to getting that extension loaded?  I downloaded the rawimageguessmaster.zip and tried loading it in the extension manager.  I keep getting an error:<br>
No extension description found in archive ‘C:/Users/en12283/Downloads/SlicerRawImageGuess-master.zip’</p>
<p>I also extracted the files and tried that and it’s still not working.  I’m sure I’m doing something wrong.  Thanks again!</p>

---

## Post #16 by @lassoan (2019-02-06 21:47 UTC)

<p>See instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Community-contributed_modules" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Community-contributed_modules</a></p>
<p><a class="mention" href="/u/nagy.attila">@nagy.attila</a> Would you mind clean up and document the module and submit to the extension index so that people can more easily access it?</p>

---

## Post #17 by @Paroxistico (2019-02-17 11:15 UTC)

<p><a class="mention" href="/u/e36alpine">@e36alpine</a> following the instructions is quite easy. You have to extract that zip wherever you want, and add the folders where every py file is from slicer/application settings/modules/aditional module paths. Restart slicer and that is.</p>

---

## Post #18 by @Paroxistico (2019-02-27 17:34 UTC)

<p>By the way, I need some help using this module… How can we open mvl files with this module? I mean, when I load with this module ie the uss I’ve uploaded previously I get nothing on the screen even playing with the sliders and setting the same parameters of the nrrd file created. A couple of weeks ago I remembered I could see the images without touching any setting but know is impossible. I tried reinstalling everything again without success.</p>

---

## Post #19 by @Chemaelite (2019-10-29 04:11 UTC)

<p>Hi Lassoan<br>
Andras Lasso, is there any extension of 3D SLICER to read the .mvl file at present</p>

---

## Post #20 by @lassoan (2019-10-29 12:00 UTC)

<p>Slicer currently cannot automatically load Samsung .mvl ultrasound files. Request your Samsung representative to provide you with an option to save images in DICOM or other open standard data format; or release specification of their proprietary file format.</p>
<p>However, you can still use <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">https://github.com/acetylsalicyl/SlicerRawImageGuess</a> extension to manually determine the image size and load the image.</p>

---

## Post #21 by @Chemaelite (2019-10-29 14:07 UTC)

<p>thank you very much for the answer i will be aware of your recommendations</p>

---

## Post #22 by @lassoan (2019-10-29 15:56 UTC)

<p>I’ve updated SlicerRawImageGuess to work with latest Slicer Preview Release (it should be available in the main repository very soon). Until then you can use the extension with Slicer-4.10.2. Here is an example of parameter settings that you can start from:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce704ca3b13f6714538c252862e3adb45905b221.jpeg" data-download-href="/uploads/short-url/tseXtcmaU1NxhUGD3fANGQP6FwZ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce704ca3b13f6714538c252862e3adb45905b221_2_690x494.jpeg" alt="image" data-base62-sha1="tseXtcmaU1NxhUGD3fANGQP6FwZ" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce704ca3b13f6714538c252862e3adb45905b221_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce704ca3b13f6714538c252862e3adb45905b221_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce704ca3b13f6714538c252862e3adb45905b221.jpeg 2x" data-dominant-color="918F90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1358×974 390 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #23 by @Chemaelite (2019-11-01 12:56 UTC)

<p>Andras Lasso, Thank you very much for your response, I am Obstetrician Gynecologist. I am very interested in this 3D technology for the benefit of my patients. You can study better alterations that fetuses have to be able to operate them. That’s why I’m interested in 3D image quality. Keep me updated on progress and updates. Thank you very very much.</p>

---

## Post #24 by @lassoan (2019-11-21 16:24 UTC)

<p>Update: RawImageGuess extension is available in the extension manager now and there is a video showing how to use it to load Samsung .mvl files: <a href="https://discourse.slicer.org/t/new-extension-rawimageguess-for-loading-of-images-from-unrecognized-file-format/9219" class="inline-onebox">New extension: RawImageGuess - for loading of images from unrecognized file format</a></p>

---

## Post #25 by @Erik-D-Mueller (2019-11-21 18:34 UTC)

<p>If someone has example source files to work from, I would be happy to start trying to reverse engineer the next most common 3d-sonogram file format.</p>

---

## Post #26 by @lassoan (2019-11-21 18:51 UTC)

<p>I think there is measurable interest in loading Samsung mvl files. The image is stored uncompressed, so the main challenge is to figure out how to determine where the image starts, where the extents and spacing information is stored. There is a link in a <a href="https://discourse.slicer.org/t/could-not-load-ultrasound-from-mvl-medison-file-format/3928/6">post above</a> to a few example data sets. If you figure out the format and create a reader in Python or C++ then we can integrate it as a file reader in Slicer (so the file can be loaded by drag-and-dropping to the application window).</p>

---

## Post #27 by @lassoan (2020-07-09 19:08 UTC)

<p>FYI, RawImageGuess module can now also load 4D movies from Samsung MVL files - see example here:</p>
<aside class="quote quote-modified" data-post="12" data-topic="12452">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/sonoace-dicom-files-loading-error/12452/12">Samsung SonoAce 4D ultrasound mvl file loading</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve also found a 4D sequence in the file (you can read it with <a href="https://1drv.ms/u/s!Arm_AFxB9yqHu70Ow3KQa3Lt5hNJIQ?e=z0tLjv">Movie4D.seq.nhdr</a> header): 
[SlicerCapture]
  </blockquote>
</aside>


---
