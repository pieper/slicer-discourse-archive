# Segmented 3D model looks weird (TIFF to DICOM to STL)

**Topic ID**: 34277
**Date**: 2024-02-13
**URL**: https://discourse.slicer.org/t/segmented-3d-model-looks-weird-tiff-to-dicom-to-stl/34277

---

## Post #1 by @Minji_Yu (2024-02-13 03:05 UTC)

<p>Hi,</p>
<p>I load the dicom files of glove CT scan for my research and did segmentation process by setting threshold. However, 3D model looks weird and doesn’t look like glove. Is there anyone can help solve this issue? Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f41f0179f08ac9295ba29d9757468f3afc3c7689.jpeg" data-download-href="/uploads/short-url/yPAVNUr8PYcrGYorajv6BIqts2B.jpeg?dl=1" title="volume rendering" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f41f0179f08ac9295ba29d9757468f3afc3c7689_2_690x459.jpeg" alt="volume rendering" data-base62-sha1="yPAVNUr8PYcrGYorajv6BIqts2B" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f41f0179f08ac9295ba29d9757468f3afc3c7689_2_690x459.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f41f0179f08ac9295ba29d9757468f3afc3c7689_2_1035x688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f41f0179f08ac9295ba29d9757468f3afc3c7689_2_1380x918.jpeg 2x" data-dominant-color="6A7576"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume rendering</span><span class="informations">1385×923 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
DICOM files: <a href="https://drive.google.com/file/d/1RmEPqyqAwxfaquyCBO96VzwEvAsGaAWL/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">Glove 1_DICOM_Patcher.zip - Google Drive</a><br>
3D Slicer files: <a href="https://drive.google.com/file/d/1YxfdLne_faZtqzqRbrqSVxpccNJXElNf/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">Process - DICOM to STL.zip - Google Drive</a></p>

---

## Post #2 by @lassoan (2024-02-13 03:09 UTC)

<p>This is a sinogram (time sequence of cone-beam CT projection images), not a 3D volume. You can reconstruct a 3D volume from projection images using filtered backprojection or similar algorithms if you knownthe exact projection geometry and pose of the source and detector for every frame. Slicer does not have a module for this but instead you can try RTK image reconstruction toolkit.</p>

---

## Post #3 by @Minji_Yu (2024-02-13 05:35 UTC)

<p>Dear Andras,</p>
<p>Thank you so much for your reply. I attached the full raw files from Micro CT Scanner.</p>
<ol>
<li>Could you please advise if there is any files that is more appropriate for this reconstruction using 3D Slicer?</li>
<li>Based on your advice, I am trying to integrate RTK into 3D Slice - Could you advise how I can use RTK in 3D Slice?</li>
<li>Are there any documents/videos that I can refer to for the process about “You can reconstruct a 3D volume from projection images using filtered backprojection or similar algorithms if you knownthe exact projection geometry and pose of the source and detector for every frame.”? It was my first time doing CT scan and I am not sure what info from attached folder and what process needed for this.</li>
</ol>
<p>Full Raw Files: <a href="https://drive.google.com/file/d/1-yJTe4HRXms5-jw-HmI4a7uoxk6uhW2G/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1-yJTe4HRXms5-jw-HmI4a7uoxk6uhW2G/view?usp=sharing</a></p>
<p>I sincerely appreciate your help.</p>
<p>Best,<br>
Minji</p>
<p>2024년 2월 12일 (월) 오후 9:09, Andras Lasso via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt;님이 작성:</p>

---

## Post #4 by @muratmaga (2024-02-13 06:53 UTC)

<aside class="quote no-group" data-username="Minji_Yu" data-post="3" data-topic="34277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/minji_yu/48/69310_2.png" class="avatar"> Minji_Yu:</div>
<blockquote>
<p>Could you please advise if there is any files that is more appropriate for this reconstruction using 3D Slicer?</p>
</blockquote>
</aside>
<p>Files that would be suitable to be used with Slicer should have been under the subfolder called Reconstruction, which is empty. I would ask the lab/person who gave you this dataset to provide you with the reconstruction.</p>
<aside class="quote no-group" data-username="Minji_Yu" data-post="3" data-topic="34277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/minji_yu/48/69310_2.png" class="avatar"> Minji_Yu:</div>
<blockquote>
<p>Based on your advice, I am trying to integrate RTK into 3D Slice - Could you advise how I can use RTK in 3D Slice?</p>
</blockquote>
</aside>
<p>RTK is an independent application, that has nothing to do with Slicer. You need to build it from the source and then experiment with the settings.</p>
<p>You may also want to try out the python based TomoPy from the Argonne Labs. It might be less challenging to get it going then RTK. <a href="https://tomopy.readthedocs.io/en/latest/about.html" class="inline-onebox">About — TomoPy a7bd9a0b37c2b1d88e305b1eca37440e5120ba62 documentation</a>. However, I havent used either of these tools, so dont know how they compare to each other.</p>
<p>Getting reconstructions out of sinograms require certain information about the acqusition geometry as well i believe. Therefore people usually use the reconstruction software provided by the vendor with the system. That’s why reaching the people who created the scan in the first place might be your simplest solution.</p>

---

## Post #5 by @Minji_Yu (2024-02-15 19:48 UTC)

<p>Hi I found .vgi and .vol under my Recon folder. Could you advise how I can open this in 3D slicer? I saw another posts talking about nhdr or python code that I can try, but not sure how to do with my files.</p>
<p>Link: <a>https://drive.google.com/drive/folders/1yF75Nrx339yAXrl11uc1qHsFqCqbgohU?usp=sharing</a><br>
Thank you</p>

---

## Post #6 by @muratmaga (2024-02-15 20:04 UTC)

<p>If you had the PCR file (the reconstruction file), you could have tried our GEVolImport module in SlicerMorph. However, vgi file is only there to import the saved .VOL file into VGStudioMax.</p>
<p>You can try to open the VGII file in a text editor, and see the dimensions and data type of the images saved in the VOL file, and from there you can create NHDR to import the file into Slicer.</p>

---

## Post #7 by @Minji_Yu (2024-02-15 20:16 UTC)

<p>Thanks, I actually try to create NHDR file but I don’t have a good understanding on how to create nhdr data. Could you please advise?</p>
<p>2024년 2월 15일 (목) 오후 2:04, Murat Maga via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt;님이 작성:</p>

---

## Post #8 by @muratmaga (2024-02-15 21:06 UTC)

<aside class="quote no-group quote-modified" data-username="Minji_Yu" data-post="5" data-topic="34277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/minji_yu/48/69310_2.png" class="avatar"> Minji_Yu:</div>
<blockquote>
<p><a href="https://drive.google.com/drive/folders/1yF75Nrx339yAXrl11uc1qHsFqCqbgohU?usp=sharing" class="inline-onebox">KP_240211_Sand_1_01_Recon - Google Drive</a></p>
</blockquote>
</aside>
<p>copy and paste this in a file called <strong>KP_240211_Sand_1.nhdr</strong> and drag and drop to slicer.</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: float
dimension: 3
space: left-posterior-superior
sizes: 1389 1477 1999
space directions: (0.113428, 0.0, 0.0) (0.0, 0.113428, 0.0) (0.0, 0.0, 0.113428)
kinds: domain domain domain
endian: little
encoding: raw
space origin: (0.0, 0.0, 0.0)
data file: KP_240211_Sand_1.vol
</code></pre>
<p>You can use this as a template for other scans like that the important sections from the VGI file are fields called:<br>
size<br>
datatype<br>
resolution</p>

---

## Post #9 by @Minji_Yu (2024-02-15 21:11 UTC)

<p>Thanks. I just tried but Slicer didn’t activate ‘Load Files’ button with this error message…</p>
<p>[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>[Qt] libpng warning: iCCP: known incorrect sRGB profile</p>
<p>Traceback (most recent call last):</p>
<p>File “C:/Users/ectym/AppData/Local/<a href="http://slicer.org/Slicer" rel="noopener nofollow ugc">slicer.org/Slicer</a> 5.6.1/<a href="http://slicer.org/Extensions-32438/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ImageStacks.py" rel="noopener nofollow ugc">slicer.org/Extensions-32438/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ImageStacks.py</a>”, line 364, in populateFromArchetype</p>
<p>self.setFilePaths(filePaths)</p>
<p>File “C:/Users/ectym/AppData/Local/<a href="http://slicer.org/Slicer" rel="noopener nofollow ugc">slicer.org/Slicer</a> 5.6.1/<a href="http://slicer.org/Extensions-32438/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ImageStacks.py" rel="noopener nofollow ugc">slicer.org/Extensions-32438/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ImageStacks.py</a>”, line 306, in setFilePaths</p>
<p>self.logic.filePaths = filePaths</p>
<p>File “C:/Users/ectym/AppData/Local/<a href="http://slicer.org/Slicer" rel="noopener nofollow ugc">slicer.org/Slicer</a> 5.6.1/<a href="http://slicer.org/Extensions-32438/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ImageStacks.py" rel="noopener nofollow ugc">slicer.org/Extensions-32438/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ImageStacks.py</a>”, line 591, in filePaths</p>
<p>reader.ReadImageInformation()</p>
<p>File “C:\Users\ectym\AppData\Local[slicer.org](<a href="http://slicer.org" rel="noopener nofollow ugc">http://slicer.org</a>)\Slicer 5.6.1\lib\Python\Lib\site-packages\SimpleITK\SimpleITK.py”, line 6253, in ReadImageInformation</p>
<p>return _SimpleITK.ImageFileReader_ReadImageInformation(self)</p>
<p>RuntimeError: Exception thrown in SimpleITK ImageFileReader_ReadImageInformation: D:\D\S\S-0-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx:292:</p>
<p>itk::ERROR: NrrdImageIO(0000022EABFF62F0): ReadImageInformation: Error reading C:/Users/ectym/Desktop/recon/KP_240211_Sand_1.nhdr:</p>
<p>[nrrd] nrrdLoad: trouble reading “C:/Users/ectym/Desktop/recon/KP_240211_Sand_1.nhdr”</p>
<p>[nrrd] nrrdRead: trouble</p>
<p>[nrrd] _nrrdRead: trouble reading NRRD file</p>
<p>[nrrd] _nrrdFormatNRRD_read: hit end of header, but no “data file” given</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4872d99b1fc0843960174b25090b4bdaaef5f2e9.png" data-download-href="/uploads/short-url/akUrsypc0fQaAHMR36aPljSaOMh.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4872d99b1fc0843960174b25090b4bdaaef5f2e9.png" data-base62-sha1="akUrsypc0fQaAHMR36aPljSaOMh" alt="image.png" width="421" height="500" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">435×516 14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>2024년 2월 15일 (목) 오후 3:06, Murat Maga via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt;님이 작성:</p>

---

## Post #10 by @muratmaga (2024-02-15 21:17 UTC)

<p><a class="mention" href="/u/minji_yu">@Minji_Yu</a> I think you have SlicerMorph installed. In that case it suggest to load the NHDR as an imagestack. Please choose “Any Data” option and retry. Also make sure that VOL file is in the same folder as your NHDR file.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, can we stop the ImageStack’s behavior to treat NRRD/NHDR to automatically try to open with ImageStacks. It is a corner use case, and it will confuse people. For people who need to stream large NRRD to benefit from ImageStacks, they should navigate the module and use the file selector from there.</p>

---

## Post #11 by @lassoan (2024-02-15 22:06 UTC)

<p>You can choose the list of file extensions that ImageStacks accepts for drag-and-drop here: <a href="https://github.com/SlicerMorph/SlicerMorph/blob/1ece7a402999f7f7b2d25937a29adc58ccfddfaa/ImageStacks/ImageStacks.py#L472" class="inline-onebox">SlicerMorph/ImageStacks/ImageStacks.py at 1ece7a402999f7f7b2d25937a29adc58ccfddfaa · SlicerMorph/SlicerMorph · GitHub</a></p>
<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="34277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It is a corner use case</p>
</blockquote>
</aside>
<p>If we want people to switch from tiff stacks to nrrd then this will be a very common, important use case, because most high-resolution data sets will be too big for an average laptop to handle.</p>
<p>ImageStacks should be improved to ensure there is no user confusion. The custom ImageStacks filedialog could be also bypassed for compressed files (until compression is implemented) and for files below a certain size (e.g., less than 1/10 of system RAM).</p>
<p>The long-term solution may be to use something that is a bit more sophisticated than NRRD, because for good performance and storage efficiency we need multiresolution, random access, and patch-based compression. These are all available in OME-NGFF, which has recently become <a href="https://github.com/InsightSoftwareConsortium/ITKIOOMEZarrNGFF">supported in ITK</a>, so we should be able to use it in Slicer.</p>

---

## Post #12 by @muratmaga (2024-02-15 23:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="34277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The long-term solution may be to use something that is a bit more sophisticated than NRRD, because for good performance and storage efficiency we need multiresolution, random access, and patch-based compression. These are all available in OME-NGFF, which has recently become <a href="https://github.com/InsightSoftwareConsortium/ITKIOOMEZarrNGFF">supported in ITK</a>, so we should be able to use it in Slicer.</p>
</blockquote>
</aside>
<p>I agree, when I mean corner case I mean for the time being. For big data, we do consider switching to OME-NGFF, or give an option of saving in that format, provided that we can build the multiscale pyramids during the import time and include in the format. So until then, probably NRRD is what we need to stick with.</p>

---
