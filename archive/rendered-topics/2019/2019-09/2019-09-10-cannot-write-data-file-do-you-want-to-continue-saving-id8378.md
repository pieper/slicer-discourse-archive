---
topic_id: 8378
title: "Cannot Write Data File Do You Want To Continue Saving"
date: 2019-09-10
url: https://discourse.slicer.org/t/8378
---

# "Cannot write data file... Do you want to continue Saving?"

**Topic ID**: 8378
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/cannot-write-data-file-do-you-want-to-continue-saving/8378

---

## Post #1 by @NoahwithFish (2019-09-10 21:47 UTC)

<p>Hi All,</p>
<p>I am having some issues saving my work in Slicer 4.10.2. After uploading a tiff stack, I adjust the image spacing in the Volume module according to the CT scanner settings, and then immediately try to save it as an .nrrd onto the desktop, but I get this error message pop-up:</p>
<p>“Cannot write data file: C:/Users/… Do you want to continue saving?”</p>
<p>I then open up the “log messages” and the error I’m getting is:</p>
<p>itk::ExceptionObject (00000001F39233D0)</p>
<p>Location: “unknown”</p>
<p>File: D:\D\S\Slicer-4102-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx</p>
<p>Line: 1123</p>
<p>Description: itk::ERROR: NrrdImageIO(0000014637F6A1D0): Write: Error writing C:/Users/Ashley-Ross Lab/Desktop/TempWriteTerrestrial_Fish_24/Terrestrial_Fish_24.8um_2k__rec2526.nrrd:</p>
<p>[nrrd] nrrdSave:</p>
<p>[nrrd] nrrdWrite: trouble</p>
<p>[nrrd] _nrrdWrite:</p>
<p>[nrrd] _nrrdFormatNRRD_write: couldn’t write gzip data</p>
<p>[nrrd] _nrrdEncodingGzip_write: expected to write 17839464000 bytes, but only wrote 21790720</p>
<p>[nrrd] _nrrdGzWrite: failed to write to file</p>
<p>[nrrd] _nrrdGzWrite: failed to write to file</p>
<p>UpdateFileList: Failed to write ‘C:/Users/Ashley-Ross Lab/Desktop/TempWriteTerrestrial_Fish_24/Terrestrial_Fish_24.8um_2k__rec2526.nrrd’.</p>
<p>itk::ExceptionObject (00000001F3923770)</p>
<p>Location: “unknown”</p>
<p>File: D:\D\S\Slicer-4102-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx</p>
<p>Line: 1123</p>
<p>Description: itk::ERROR: NrrdImageIO(0000014637F6A1D0): Write: Error writing C:/Users/Ashley-Ross Lab/Desktop/Terrestrial_Fish_24.8um_2k__rec2526.nrrd:</p>
<p>[nrrd] nrrdSave:</p>
<p>[nrrd] nrrdWrite: trouble</p>
<p>[nrrd] _nrrdWrite:</p>
<p>[nrrd] _nrrdFormatNRRD_write: couldn’t write gzip data</p>
<p>[nrrd] _nrrdEncodingGzip_write: expected to write 17839464000 bytes, but only wrote 851968</p>
<p>[nrrd] _nrrdGzWrite: failed to write to file</p>
<p>[nrrd] _nrrdGzWrite: failed to write to file</p>
<p>Does anybody know how to reserve this issue so that I can save my scans as an .nrrd and actually work on it/segment it from there?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2019-09-10 22:02 UTC)

<aside class="quote no-group" data-username="NoahwithFish" data-post="1" data-topic="8378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c2a13f/48.png" class="avatar"> NoahwithFish:</div>
<blockquote>
<p>[nrrd] _nrrdEncodingGzip_write: expected to write 17839464000 bytes, but only wrote 21790720</p>
</blockquote>
</aside>
<p>Hi Noah -</p>
<p>The message indicates you might be running out of disk space - are you able to save on another drive or maybe test with a subset of your input files?</p>
<p>-Steve</p>

---

## Post #3 by @lassoan (2019-09-11 00:52 UTC)

<p>17839464000 bytes is about 18GB. Is your volume really that big? Was it loaded successfully? How many slices do you have? How large is one slice? Is it a color or grayscale image?</p>

---

## Post #4 by @muratmaga (2019-09-11 04:08 UTC)

<p><a class="mention" href="/u/noahwithfish">@NoahwithFish</a></p>
<p>If these are 2kx2kx2k scans of fishes (in tiff format and I happen to know that data type is 16bit from that particular mCT, and indeed all grayscale, and not multichannel), they are would be about 16-18GB. So looks like you successfully imported the full stack. After making sure you have enough space on the drive you are trying to save, disable the compression (remember to expand the save as option). Gzip compression of such data would take quite a while and may or may not be related to your problem.</p>

---

## Post #5 by @NoahwithFish (2019-09-11 12:44 UTC)

<p>Yes, something like that. Each slice is 7.18 MB. It’s a large uCT scan. It seemed like it loaded successfully, with 2,370 slices. I believe it’s grayscale.</p>

---

## Post #6 by @NoahwithFish (2019-09-11 22:13 UTC)

<p>Well, this solved part of the issue. Using an empty drive (D), into which I downloaded Slicer 4.11.0, instead of the full drive © allowed me to save the stack as an nrrd. However, this wouldn’t let me save cropped volumes. For instance, if I cropped a volume and named it “Fish 1”, Slicer would not let me save that volume once it’s cropped, and instead gives me this error:</p>
<p>Weirdly, if I saved it under “Create new volume” and use the name it creates, like “Terrestrial_Fish cropped”, it allows me to save that. When I open that, though, it’s not the cropped volume but the full volume. <img src="https://emoji.discourse-cdn.com/twitter/upside_down_face.png?v=9" title=":upside_down_face:" class="emoji" alt=":upside_down_face:"> If I try to save the cropped volumes on their own, such as “Archerfish.nrrd”, I still get this error message:</p>
<p>“cannot write ImageDate, it’s NULL”</p>
<p>Do you have any suggestions on how to fish that?</p>
<p>Just before that error message is a warning:<br>
“ShellExecute ‘file:///C:/Users/Ashley-Ross Lab/.slicerrc.py’ failed (error 31)”</p>
<p>That’s where the Application startup script seems to be located, but it won’t let me change that. It seems like there may not be enough memory to even run this startup script in C drive, even though I downloaded the program in D drive, and have all working files in D drive.  Do you have an idea what’s going on with that?</p>

---

## Post #7 by @muratmaga (2019-09-11 22:50 UTC)

<p>I am not exactly sure what’s going on from the description.</p>
<p>First, you want to check whether Crop Volume worked as it is intended. There is a tab called Volume Information in the crop volume that will show what the dimension of the input volume is, and what would be the output volume dimensions. You can cross-refer this to the volume information reported under the volumes after the cropping operation is completed.</p>
<p>Once you are certain crop volume indeed worked correctly (i.e., input and output volume dimensions are NOT the same), go to Data module rename your “-cropped” volume to a simple name and try saving it as nrrd without compressing.</p>
<p>A lot of the typical saving errors people face are related to using non-ascii characters in file name, paths or trying to write a folder that they don’t have permission to write. If still doesn’t work, please send the full log.</p>

---

## Post #8 by @NoahwithFish (2019-09-12 15:46 UTC)

<p>It was a memory issue. Even though I was saving into an empty drive, the computer’s working memory was in a drive that was full, so it wouldn’t allow saving of anything. I cleared some space in that drive and now everything works well. Thanks!</p>

---

## Post #9 by @muratmaga (2019-09-12 15:47 UTC)

<p>Happy to hear that. When you are working with such large volumes, you have to be cognizant of the both physical  memory (RAM)  and disk space requirements.</p>

---
