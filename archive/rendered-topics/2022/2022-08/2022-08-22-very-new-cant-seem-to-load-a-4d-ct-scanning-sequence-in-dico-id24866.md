# Very new, Can't seem to load a 4D CT scanning sequence in DICOM format

**Topic ID**: 24866
**Date**: 2022-08-22
**URL**: https://discourse.slicer.org/t/very-new-cant-seem-to-load-a-4d-ct-scanning-sequence-in-dicom-format/24866

---

## Post #1 by @MrTomatosoup (2022-08-22 14:58 UTC)

<p>Hi all,</p>
<p>as said in the title, I am very new to Slicer and its applications. I want to analyze a series of 4-dimensional CT-scans (xyzt). I have the files in DICOM format. It seems I have the same problem as posted in <a href="https://discourse.slicer.org/t/newbie-struggling-with-dicom-multivolume-and-sequences/22134">this post</a> before, however I can not seem to fix it.</p>
<p>My files have been handed over in different frames, where each folder is 1 frame, consisting of a number of .dcm files</p>
<p>These are my steps:</p>
<ol>
<li>Add data through the Add DICOM Data module</li>
<li>Select folder containing the “frame sub-folders”</li>
<li>Check advanced button</li>
<li>Check the plugins. I have tried multiple combinations, with and without MultiVolumeImporterPlugin, with and without DICOMVolumeSequencePlugin, etc.</li>
</ol>
<p>From here on, when I click “Examine”, I only get entries in the advanced tab when I check the DICOMScalarVolumePlugin. There is no ‘MultiVolume’ Entry.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/143ed01d28abadccf0e4bab36481f33d969785fe.png" data-download-href="/uploads/short-url/2T67MvByC7NRt1cdkCjeg51lrIy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/143ed01d28abadccf0e4bab36481f33d969785fe.png" alt="image" data-base62-sha1="2T67MvByC7NRt1cdkCjeg51lrIy" width="690" height="287" data-dominant-color="38434C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">877×365 21.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I don’t check the ScalarVolumePlugin, it shows nothing</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a3e3adca49469a3c611d8114952254c755447b.png" data-download-href="/uploads/short-url/wLutgIeUPFQSN0HU70tt5BdvFR9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a3e3adca49469a3c611d8114952254c755447b.png" alt="image" data-base62-sha1="wLutgIeUPFQSN0HU70tt5BdvFR9" width="690" height="329" data-dominant-color="374F64"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">830×396 18.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have also tried this with both Volume Sequence and Multi-volume selected in settings under preferred multi-volume import format.</p>
<p>Do you guys have any tips on how to get this to work?</p>
<p>Sadly, I can’t share my database.</p>
<p>Thanks for any advice on the topic!</p>

---

## Post #2 by @pieper (2022-08-22 16:16 UTC)

<p>Unfortunately when you are doing advanced processing on data you can’t share it’s hard to get the help you need.  Your best be here is to get to know the dicom headers used to define frames and <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMImageSequencePlugin.py">read the code</a> to see how the parsing is done.  You can use the metadata viewer (from right click menu on any item in the browser).  You can also look at the DICOM Patcher module for ideas if you need to patch the files.</p>

---

## Post #3 by @mikebind (2022-08-22 17:41 UTC)

<p>I agree with the approach <a class="mention" href="/u/pieper">@pieper</a> suggests.  However, I want to offer a correction of where to look at the code.  DICOMImageSequencePlugin <em>sounds like</em> the right place to be looking, but isn’t (it handles 2D image sequences like ultrasound).  Sequences of 3D image volumes are loaded from DICOM using MultiVolumeImporterPlugin, and the code for that is here: <a href="https://github.com/fedorov/MultiVolumeImporter/blob/master/MultiVolumeImporterPlugin.py" class="inline-onebox" rel="noopener nofollow ugc">MultiVolumeImporter/MultiVolumeImporterPlugin.py at master · fedorov/MultiVolumeImporter · GitHub</a>.  You can look at what DICOM tags the MultiVolumeImporterPlugin looks at to decide if a set of DICOM files can be imported as a image volume Sequence, and then also look through the values in your DICOM headers to figure out why they are not being recognized as appropriate for import as a Sequence. Two likely possibilities are that the DICOM headers in your images are incorrect in some way (there are a lot of malformed DICOM files out there!) or, alternatively, your files are fine and the MultiVolumeImporterPlugin needs a new heuristic added to catch the type of files you have and correctly organize them.</p>

---

## Post #4 by @pieper (2022-08-22 19:50 UTC)

<p>thanks for the clarification <a class="mention" href="/u/mikebind">@mikebind</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
