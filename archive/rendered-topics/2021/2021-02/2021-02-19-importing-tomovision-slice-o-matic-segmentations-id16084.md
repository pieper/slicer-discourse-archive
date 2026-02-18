# Importing Tomovision Slice-O-Matic segmentations

**Topic ID**: 16084
**Date**: 2021-02-19
**URL**: https://discourse.slicer.org/t/importing-tomovision-slice-o-matic-segmentations/16084

---

## Post #1 by @Justin (2021-02-19 13:38 UTC)

<p>Dear all,</p>
<p>My group has been using Tomovision Slice-O-Matic to create segmentations on CT-scans to get cross-sectional areas. I myself am using Slicer 3D for this and would like to use the segmentations created by others from Slice-O-Matic.</p>
<p>Slice-O-Matic creates a .tag file that contains the segmentation and this files is linked to a dicom file.<br>
The contents of this TAG file is described here: <a href="https://www.tomovision.com/SliceO_Help/index.htm?context=700" class="inline-onebox" rel="noopener nofollow ugc">SliceOmatic 5.0</a><br>
It says the file is composed of a header and the image data. The image data is output as a binary format that is loosely based on the " university of Waterloo IM format"</p>
<p>Unfortunately, the normal import option (or add data) does not work for these kinds of files, so I would like to find another way to import these files.</p>
<p>I tried opening them in notepad++ or ImageJ to see if I could access this binary data to maybe convert this somehow to another format, but unfortunately I am not sufficiently knowledgeable on this subject to create a converter or to view the output somehow.</p>
<p>Is there anyone who has experience with this type of file format and is able to help me convert the tag files so that I can work with it in slicer?</p>
<p>Please find a link to a .dcm and corresponding .tag file (using anonymized data) in the link below</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://prod-cdn.wetransfer.net/packs/media/images/favicon-a34a7465.ico" class="site-icon" width="16" height="16">
      <a href="https://wetransfer.com/downloads/724a08b869ac4ffb6057113f99ada6f120210219132621/eede61" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://prod-cdn.wetransfer.net/packs/media/images/wt-facebook-9db47080.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://wetransfer.com/downloads/724a08b869ac4ffb6057113f99ada6f120210219132621/eede61" target="_blank" rel="noopener nofollow ugc">1.2.826.0.1.3680043.9.6827.2654999522103593432286634944139815071-no-value-for-Se...</a></h3>

<p>2 files sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thanks so much in advance for your help!</p>
<p>Best, Justin</p>

---

## Post #2 by @pieper (2021-02-19 15:28 UTC)

<p>It looks like there’s all the info you need, so just creating a .nhdr file the points to the .tag should make it basically loadable.</p>
<p>The nrrd format is <a href="http://teem.sourceforge.net/nrrd/format.html">described here</a>.  What I would suggest is starting with the dicom, creating a segmentation, saving it as .nhdr, and then editing the .nhdr <a href="http://teem.sourceforge.net/nrrd/format.html#detached">data file</a> field to point to the tag file.  It might’ ‘just work’ or there may be other fields to tweak.</p>

---

## Post #3 by @Justin (2021-02-19 21:49 UTC)

<p>Hi Steve,</p>
<p>Thanks for your suggestion!</p>
<p>I’ve tried to do as you said, so create a segmentation and export as .nhdr<br>
After opening the .nhdr file and changing the data file to point to the tag file I don’t get the expected result (if I add the .nhdr file to the scene nothing is added)</p>
<p>I also tried deleting the header information in the .tag file to see whether this is the problem but this doesn’t fix the problem.</p>
<p>What I notice is that the dummy segmentation is 3 kb (that I’ve created to change the header), the .dcm file is 254 kb and the .tag file is 257 kb. So it looks as if the .tag file contains the segmentation and the whole dicom image. Could that be possible?</p>
<p>Best, Justin</p>

---

## Post #4 by @pieper (2021-02-19 21:54 UTC)

<p>Yes, from what you posted the tag file should be the same size as the dicom since it is the same dimensions and datatype.</p>
<p>Probably there’s an error reported in the log file when you load the nhdr that will give you more info.</p>
<p>You might also use this extension to help narrow things down: <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess" class="inline-onebox">GitHub - acetylsalicyl/SlicerRawImageGuess</a></p>

---

## Post #5 by @Justin (2021-02-19 22:12 UTC)

<p>Thanks! This is the error message I get:</p>
<p>Read: Error reading D:/Slicer/Test nhdr/Segmentation-Segment_1-label.nhdr:<br>
[nrrd] nrrdLoad: trouble reading “D:/Slicer/Test nhdr/Segmentation-Segment_1-label.nhdr”<br>
[nrrd] nrrdRead: trouble<br>
[nrrd] _nrrdRead: trouble reading NRRD file<br>
[nrrd] _nrrdFormatNRRD_read:<br>
[nrrd] _nrrdEncodingGzip_read: expected 524288 bytes but received 262142</p>
<p>Algorithm vtkITKArchetypeImageSeriesScalarReader(000001B5C041FC80) returned failure for request: vtkInformation (000001B5C2C937E0)<br>
Debug: Off<br>
Modified Time: 736173<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_DATA<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FROM_OUTPUT_PORT: 0</p>
<p>ReadDataInternal: Cannot read file as a volume of type LabelMapVolume[fullName = D:/Slicer/Test nhdr/Segmentation-Segment_1-label.nhdr]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 1 files.<br>
File reader used the archetype file name of D:/Slicer/Test nhdr/Segmentation-Segment_1-label.nhdr [reader 0th file name = D:/Slicer/Test nhdr/Segmentation-Segment_1-label.nhdr]<br>
FileFormatError</p>
<p>I’ve also tried using the Raw Image Guess.<br>
When I set it to 8bit image, of dimensions 512x512 (CT-size) then the image turns white, however I cannot see the segmentations that are supposed to be there.</p>
<p>Edit: I also notice that when I open the ‘dummy segmentation’ file in Notepad++ it reads length 524.288 and the .tag file (with the header info removed) reads length 262.144. So this I can confirm from the  error message.</p>
<p>The expected width en height of the image should be 512x512, as I can read this from the header of the .tag file.</p>

---

## Post #6 by @pieper (2021-02-19 22:45 UTC)

<p>Looks like you are close.</p>
<blockquote>
<p>expected 524288 bytes but received 262142</p>
</blockquote>
<p>means that the .tag has bytes instead of shorts so you need to change the nhdr to match.</p>
<aside class="quote no-group" data-username="Justin" data-post="5" data-topic="16084">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/3ab097/48.png" class="avatar"> Justin:</div>
<blockquote>
<p>then the image turns white</p>
</blockquote>
</aside>
<p>You’ll want to load the converted file as a labelmap or segmentation.  Also you can mouse over the image and look in the DataProbe (lower left) to see the pixel values that have been read.</p>

---

## Post #7 by @lassoan (2021-02-19 22:47 UTC)

<p>If you use the .seg.nhdr extension then recent Slicer Releases (maybe only the preview release) will load the file by default as segmentation.</p>

---

## Post #8 by @lassoan (2021-02-20 04:01 UTC)

<p>We have recently added the possibility to easily create custom file readers in Python and I wanted to give it a try to see how well it works. The result: it works very well and now there is a <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/SliceOmaticImporter/SliceOmaticImporter.py">SliceOmatic tag file reader</a> available in Slicer (in Sandbox extension).</p>
<p>If you install Sandbox extension (in Examples category in the Extensions manager) then you can load the .tag file directly as a segmentation by simply drag-and-dropping the file to the application window.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6668184ed0d30bd10328f1bf5c694e27c44d7d7.png" data-download-href="/uploads/short-url/uAFNoeKIoOJllimvvZaMbCH1yDR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6668184ed0d30bd10328f1bf5c694e27c44d7d7.png" alt="image" data-base62-sha1="uAFNoeKIoOJllimvvZaMbCH1yDR" width="690" height="321" data-dominant-color="3D3D3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1122×523 19.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca58e4e3f20e443450bc18d9c4922abf69eb39cb.jpeg" data-download-href="/uploads/short-url/sS2U25jne5jcozaQ3TXH1hb3QnN.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca58e4e3f20e443450bc18d9c4922abf69eb39cb_2_419x499.jpeg" alt="image" data-base62-sha1="sS2U25jne5jcozaQ3TXH1hb3QnN" width="419" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca58e4e3f20e443450bc18d9c4922abf69eb39cb_2_419x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca58e4e3f20e443450bc18d9c4922abf69eb39cb.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca58e4e3f20e443450bc18d9c4922abf69eb39cb.jpeg 2x" data-dominant-color="494743"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">446×531 58.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I only tested it on a single slice and single segment, but it should work on 3D data with multiple segments as well.</p>

---

## Post #9 by @Justin (2021-02-20 11:42 UTC)

<p>I was finally able to use the Raw input guess method to generate a header for the .tag files after deleting the header information from the .tag file and convert to a segmentation (and as <a class="mention" href="/u/lassoan">@lassoan</a> advised also change the extension of the .nhdr to .seg.nhdr) but when I loaded the new header and the dicom file, the segmentation was not visible anymore.</p>
<p>The support for SliceOMatic tag import from the sandbox extension is amazing! I can just open the scan from the Dicom database, load in the segmentation by drag and drop and it falls into place nicely. Thanks so much for this extension!</p>

---

## Post #10 by @elpequeno (2023-12-05 10:26 UTC)

<p>This is amazing, thank you for this extension, it is very useful for me.</p>
<p>Sorry, if I missed it, but is there also a command line tool to do this? I have a folder of hundreds of images and segmentations in slice-o-matic .tag files and I would love to convert all of them to nrrd or nifti or something similar.</p>
<p>Thanks you for your help.</p>
<p>Best,<br>
André</p>

---

## Post #11 by @lassoan (2023-12-05 22:56 UTC)

<p>You can do all the conversion by a few lines of Python code. For each .tag file, you can <a href="https://github.com/PerkLab/SlicerSandbox/blob/94e2df06c4b2c890020b7d6bf0c55faa4b8ecf7e/ImportSliceOmatic/ImportSliceOmatic.py#L239">import the segmentation from .tag file using the sliceomatic reader</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file">export the segmentation using <code>exportNode</code> function</a>.</p>

---

## Post #12 by @elpequeno (2023-12-06 07:51 UTC)

<p>thank you so much for the quick response. After I wrote the question here I looked into this code. This helps a lot. I got a nice little script now to convert my files.<br>
Thank you!</p>

---
