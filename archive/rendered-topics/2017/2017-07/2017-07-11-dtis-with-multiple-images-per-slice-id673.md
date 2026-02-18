# DTIs with multiple images per slice

**Topic ID**: 673
**Date**: 2017-07-11
**URL**: https://discourse.slicer.org/t/dtis-with-multiple-images-per-slice/673

---

## Post #1 by @snaughton (2017-07-11 21:23 UTC)

<p>Hello,<br>
I am having an issue where the DTIs that I have received from our imaging core are captured in such a way that there are multiple images per each slice.  In other words when I open the file I will see the first slice several times captured as an FA value, then Trace of DTI, then A0 image, then Trace weighted image, DTI components, and all of the various eigenvector values.  Then each of the following slices will follow this same pattern.</p>
<p>This makes is difficult to scroll through and analyze only one of these values.  Is there a way I can sort the slices to only view one parameter at a time?  Better yet, is there a way to transform this file set into something that would resemble the files in the DTI tutorials?</p>

---

## Post #2 by @ihnorton (2017-07-12 00:35 UTC)

<p>Please provide more information. What type of scanner? What file format do the files arrive in? Can you get access to the raw DICOM if they aren’t already? How do you import?</p>
<p>Taking a guess, it sounds like the files are being either loaded or converted without respect to file sorting. You may have different options depending on answers to the questions above.</p>
<p>As for extraction, if certain types of images are at consistent offsets then the easiest extraction method is to use python and select strided slices. Copy those into a new volume. Getting diffusion parameters may be trickier depending again on above questions.</p>

---

## Post #3 by @ihnorton (2017-07-12 01:04 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="673">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>easiest extraction method is to use python</p>
</blockquote>
</aside>
<p>e.g see this thread:</p>
<aside class="quote quote-modified" data-post="1" data-topic="658">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/6de8d8/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/creating-volume-from-numpy/658">Creating Volume from Numpy</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi all, 
I have slicer version 4.7.0-2017-07-07 r26146 installed. 
I am trying to convert a numpy 3d array into a new volume. I tried the following as listed in the nightly documentation: 



resultVolumeNode = getNode(‘fixed’) 
resultVtkArray = vtk.util.numpy_support.numpy_to_vtk(a, deep=True, array_type=vtk.VTK_SHORT) 
resultVolumeNode.GetImageData().SetScalars(resultVtkArray) 



I’m running into a couple of issues. 


numpy_to_vtk only seems to support 1 or 2d arrays. What is your recommende…
  </blockquote>
</aside>


---

## Post #4 by @snaughton (2017-07-12 14:41 UTC)

<p>The scans are done a Bruker scanner (7.0T 20cm bore BioSpec MRI spectrometer).  I receive the files in DICOM format (I believe they are generated through the paravision software).  I can import the DICOM files directly using the the ‘Load DICOM Data’ option but the axes do not line up and the images are crooked.   If I convert to .Nrrd using image J, then the axes will line up evenly and the images are properly oriented when I import to slicer.   The guy from our MRI core gave me a macro to sort the images in imageJ and recommended doing my analysis manually through imageJ, but I was hoping to find a way to do it using slicer.</p>

---

## Post #5 by @ihnorton (2017-07-12 15:42 UTC)

<p>Ok, sorting the images in to separate folders would be a good start. If you pre-sort into separate folders before loading, it should be possible to get rid of the jumbled single volume. If you are able to load and split in ImageJ, you might be able to save as NRRD using e.g. BioFormats or one of the other plugins with NRRD support (but those probably don’t know about DWI metadata).</p>
<p>If ImageJ doesn’t provide folder sorting, then other options include <a href="https://dicomsort.com/">this</a> and <a href="https://github.com/pieper/dicomsort">this</a> (same name, both Python, but different projects).</p>
<p>As for actually interpreting the data as diffusion, you will need a way to extract the gradient information. Some comments:</p>
<ul>
<li>
<p>I don’t know what “Bruker diffusion DICOM” looks like. If you are <em>really lucky</em>, then Bruker is using the standard diffusion tags, and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DWIConverter">DWIConvert</a> may just work – once you sort the files appropriately. (sample data would be very helpful if you are able to provide any. we got some sample data from someone else in June, but it did not appear to have any DWI metadata).</p>
</li>
<li>
<p>The most popular NiFTI DWI conversion tool, <a href="https://www.nitrc.org/projects/dcm2nii/">dcm2nii</a>, can apparently read Bruker 2dseq style files with diffusion information, but I don’t know if it supports Bruker DICOM (again dependent on the tags).</p>
</li>
<li>
<p><a href="http://dsi-studio.labsolver.org/Manual/Parse-DICOM">DSI-Studio</a> apparently also has some Bruker support (2dseq again?) but my vague recollection is that their interpretation of NiFTI DWI differs a little bit from the “FSL NiFTI DWI” that dcm2nii and compatible tools create/expect.</p>
</li>
</ul>
<p>Hopefully something here is helpful to get started. If you do have shareable sample data I can take a quick look and maybe point you further along.</p>

---

## Post #6 by @pieper (2017-07-12 16:06 UTC)

<p>Another one to consider is dicom2nifti, which <a class="mention" href="/u/fedorov">@fedorov</a> recently pointed out.  It appears to support some diffusion.  Let us know what ends up working best for you.</p>
<p><a href="https://github.com/icometrix/dicom2nifti">https://github.com/icometrix/dicom2nifti</a></p>

---

## Post #7 by @snaughton (2017-07-13 16:36 UTC)

<p>Thanks for the suggestions guys.  Using the macro I was provided I am able to separate the different parameters then export them as individual NRDD files.   Will it be of any use to have these all as separate files?  Currently I have 22 different NRRD files for the same brain giving me  FA, Intensity, Tensor Trace, Tensor component XX ect.  All of these files  I can open in slicer and they look pretty good in terms of the orientation and all of the axes line up correctly.</p>
<p>I was not able to get anything useful using DWIConvert, dcm2nii, or DSI-Studio.  I will try dicom2nifti once I find a good python compiler.</p>
<p>Any suggestions as to how I might be able to collate these 22 nrrd files into a single file?</p>

---
