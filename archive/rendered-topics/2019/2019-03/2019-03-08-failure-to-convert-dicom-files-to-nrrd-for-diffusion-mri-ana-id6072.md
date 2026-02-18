# Failure to convert DICOM files to Nrrd for Diffusion MRI Analysis

**Topic ID**: 6072
**Date**: 2019-03-08
**URL**: https://discourse.slicer.org/t/failure-to-convert-dicom-files-to-nrrd-for-diffusion-mri-analysis/6072

---

## Post #1 by @Bebo (2019-03-08 12:11 UTC)

<p>Hello every one,<br>
I’m a new 3D slicer user (4.10.1 version), I intend to convert DCM files to Nrrd  for the purpose of diffusion MRI analysis (the public data come from the Visual Human Project).<br>
However I have this error message:<br>
Diffusion-weighted DICOM Import (DWIConvert) standard error:<br>
<strong>Error: no DICOMfiles found in inputDirectory: D:/Modélisation_tête/GRANDIN_TETE_HUMAINE/2 - Datas/4 - 3D Slicer/Intput_directory/st000/se000</strong><br>
<strong>Unable to create converter!</strong><br>
I tried to use the lastest build version (4.11) but no DWI volume set was created and that version doesn’t have DWI converter extension yet…<br>
I also tried to use the “patch” option or to copy/paste the data into another folder as I could read in previous posts but it didn’t work neither<br>
Can someone help me please ??</p>

---

## Post #2 by @cpinter (2019-03-08 14:28 UTC)

<p>The DICOM importer and database are known to have problems with special characters in the paths. Please try to move the data to a path that only has ascii characters, and make sure your databsae is in such a folder as well.</p>

---

## Post #3 by @jaygummers (2019-03-08 15:18 UTC)

<p>Yes, I have also faced the similar issue with special characters in the database. However, I couldn’t fix it even after moving the DB into the same folder. <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=6" title=":confused:" class="emoji" alt=":confused:"></p>

---

## Post #4 by @cpinter (2019-03-08 15:46 UTC)

<p>Have you reported this problem?<br>
It’s possible that not just the database but the files were also in folders with paths containing spaces and/or non-ascii characters.</p>

---

## Post #5 by @Bebo (2019-03-12 09:00 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I did as you said I changed the path with only ascii characters path but now I have another error message:</p>
<p><strong>Diffusion-weighted DICOM Import (DWIConvert) standard error:</strong></p>
<p><strong>Exception extracting gradient vectors</strong><br>
<strong>itk::ExceptionObject (00000000002FB410)</strong><br>
<strong>Location: "unknown"</strong><br>
<strong>File: D:\D\S\Slicer-4101-build\ITK\Modules\IO\DCMTK\src\itkDCMTKFileReader.cxx</strong><br>
<strong>Line: 577</strong><br>
<strong>Description: itk::ERROR: Cant find tag 18 9089</strong><br>
I googled the message error but wasn’t conclusive…</p>

---

## Post #6 by @pieper (2019-03-12 11:11 UTC)

<p>Have a look at this dicussion of dcm2niix as an alternative:</p>
<aside class="quote" data-post="1" data-topic="5407">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/convert-single-files-into-one-nii/5407">Convert single files into one .nii</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I have multiple single .ima files. These contain single slices info. 
What I want to achieve is to merge all these into one .nii file. 
What is the best way to do that? 
Thanks
  </blockquote>
</aside>


---

## Post #7 by @Bebo (2019-03-20 13:44 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>  thank you for your answer,<br>
However even if did manage to reconstruct the geometry and the convertion, I did not have the b-vector and b-value files critical for the diffusion MRI analysis is that normal ?</p>

---

## Post #8 by @pieper (2019-03-20 20:26 UTC)

<p><a class="mention" href="/u/bebo">@bebo</a> looking back, it seems you are trying to work with the visible human data, but I don’t believe there is any DWI acquisition, so no, you wouldn’t be able do diffusion analysis.</p>

---

## Post #9 by @Bebo (2019-03-21 07:48 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thank you for answer.<br>
Indeed, I googled it and it seems that there’s no DWI acquisition… which explains all my troubles… Any way Thank you !!</p>

---
