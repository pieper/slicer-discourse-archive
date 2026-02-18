# Simple ITK ImageStacks Error

**Topic ID**: 20106
**Date**: 2021-10-11
**URL**: https://discourse.slicer.org/t/simple-itk-imagestacks-error/20106

---

## Post #1 by @Rosalee_Elting (2021-10-11 20:14 UTC)

<p>Os: Windows 10 Pro<br>
Slicer version: 4.11.20210226<br>
All extensions updated.</p>
<p>I am trying to load CT data slices using ImageStacks. I get the following error when I try any slices, and when I try to generate a preview and full resolution.</p>
<p>Loading failed: Exception thrown in SimpleITK ImageFileReader_Execute: D:\D\S\Slicer-1-build\ITK\Modules\IO\TIFF\src\itkTIFFImageIO.cxx:1408:<br>
itk::ERROR: itk::ERROR: TIFFImageIO(00000209510E01C0): Problem reading the row: 941</p>
<p>Slice error number does change based on which slice axis I try to load (X, Y or Z)</p>
<p>Thank you for any help!</p>

---

## Post #2 by @pieper (2021-10-11 22:53 UTC)

<p>That looks like a read error that would come from corrupted data.  Are the files readable with other applications?  If you can read them in another app, maybe try re-saving them and trying those in Slicer.  If you find a version that works elsewhere but not in Slicer please share an example for debugging.</p>

---

## Post #3 by @muratmaga (2021-10-11 23:16 UTC)

<p><a class="mention" href="/u/rosalee_elting">@Rosalee_Elting</a> if you can share the data, we can try to replicate the error.</p>
<p>And I am not also sure what you mean by</p>
<aside class="quote no-group" data-username="Rosalee_Elting" data-post="1" data-topic="20106">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosalee_elting/48/10138_2.png" class="avatar"> Rosalee_Elting:</div>
<blockquote>
<p>Slice error number does change based on which slice axis I try to load (X, Y or Z)</p>
</blockquote>
</aside>
<p>You should have just one sequence of slices…</p>

---

## Post #4 by @Rosalee_Elting (2021-10-12 16:02 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/pieper">@pieper</a> , thank you for the help! I’ve attached a link to a zipped file of the slices. When the person CT scanning our birds includes the slices, they have a X, Y and Z slices files. I’ve historically been able to load the X slices (of other birds) in ImageStacks, but now wonder if I’m missing something. Hopefully you can look at the data and see. Thanks, again! <a href="https://drive.google.com/file/d/1bYcSYtL_vdxjFTbywM181wq-vg13n_kT/view?usp=sharing" rel="noopener nofollow ugc">download link</a></p>

---

## Post #5 by @pieper (2021-10-12 17:59 UTC)

<p>Hi <a class="mention" href="/u/rosalee_elting">@Rosalee_Elting</a> - I tried downloading the google drive link but the zip file is invalid somehow.  Can you confirm the zipfile is valid on your end and maybe try re-uploading?  The issue may be due to the size of the zipfile so maybe you can see if you can replicate the issue with just one or two images?</p>

---

## Post #6 by @muratmaga (2021-10-12 18:32 UTC)

<aside class="quote no-group" data-username="Rosalee_Elting" data-post="4" data-topic="20106" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rosalee_elting/48/10138_2.png" class="avatar"> Rosalee_Elting:</div>
<blockquote>
<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/pieper">@pieper</a> , thank you for the help! I’ve attached a link to a zipped file of the slices. When the person CT scanning our birds includes the slices, they have a X, Y and Z slices files. I’ve historically been able to load the X slices (of other birds) in ImageStacks, but now wonder if I’m missing something. Hopefully you can look at the data and see. Thanks, again! <a href="https://drive.google.com/file/d/1bYcSYtL_vdxjFTbywM181wq-vg13n_kT/view?usp=sharing">download link </a></p>
</blockquote>
</aside>
<p>I donwnloaded and unzipped and used the X-slices folder, didn’t encounter any issues either loading the preview or full resolution dataset. There are many datasets in the zip file, is there a particular one you are facing the issue with?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62714db455e1c1cf3f3c0e7048b6ab29bb932865.jpeg" data-download-href="/uploads/short-url/e2RxInFBxL7TPHrfgX9LSbURl2t.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62714db455e1c1cf3f3c0e7048b6ab29bb932865_2_690x458.jpeg" alt="image" data-base62-sha1="e2RxInFBxL7TPHrfgX9LSbURl2t" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62714db455e1c1cf3f3c0e7048b6ab29bb932865_2_690x458.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62714db455e1c1cf3f3c0e7048b6ab29bb932865_2_1035x687.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62714db455e1c1cf3f3c0e7048b6ab29bb932865_2_1380x916.jpeg 2x" data-dominant-color="8F8E93"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1277 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Rosalee_Elting (2021-10-12 22:41 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> ! Looks great! This scan was taken with a 16.2um slice distance, I’m wondering if my changing the auto-populated values (0.264…mm) is where the error generated from. Coincidental or related, do you think?</p>

---

## Post #8 by @muratmaga (2021-10-12 22:50 UTC)

<p>You can manually update the voxel spacing at the ImageStacks. I simply used whatever the value tiff files reported (hence another reason not to use 2D formats like that).</p>
<p>Slice spacing shouldn’t cause an issue like that. Perhaps as <a class="mention" href="/u/pieper">@pieper</a> indicated one of your files were corrupted, thought I don’t know why you got that with other datasets. All I can say that ImageStacks working correctly with this dataset using the stable version of slicer.</p>

---

## Post #9 by @Rosalee_Elting (2021-10-14 15:48 UTC)

<p>Thank you for looking into it! I will check the files for corruption (they were transferred in a strange way, so that could be it). I appreciate you trying it on your machine and narrowing down the issue and that it isn’t ImageStacks. Can you direct me to a forum for preferred formats (non-tiff)? Thank you!</p>

---

## Post #10 by @muratmaga (2021-10-14 16:53 UTC)

<p>If the imaging lab gave you this, you will have to import it through the ImageStack, and when you are importing make sure you enter the correct voxel spacing values. After a successful import, you should save the resultant volume as NRRD so that you don’t have to keep importing and fixing the voxel spacing, everytime you want to work with this dataset.</p>
<p>There are a few other volumetric dataset options, but NRRD is the most flexible and supported by other open source biomedical visualization programs, so thats what we suggest.</p>

---

## Post #11 by @Rosalee_Elting (2021-10-14 17:44 UTC)

<p>Hi Murat,</p>
<p>Great! That is super helpful. I usually save the scene and only load the slices once to prevent mis-loading with the wrong voxels or other slice issues.</p>
<p>Thank you for the clarification!</p>

---
