# Brain resample module issue

**Topic ID**: 17046
**Date**: 2021-04-12
**URL**: https://discourse.slicer.org/t/brain-resample-module-issue/17046

---

## Post #1 by @Ludovic_Ferrer (2021-04-12 21:27 UTC)

<p>Hi everybody,<br>
I found a weird behaviour to brains resample module on some PET/CT images I have.<br>
Despite that PET/CT ScalarVolumesNodes are correctly displayed with correct informations as regards to the volume properties, the resample module raises an error:</p>
<blockquote>
<p>Resample Image (BRAINS) standard output:</p>
<p>WARNING: neither warpTransform nor deformationVolume are defined, so warpTransform is set as identity.</p>
<p>=====================================================</p>
<p>Input Volume: C:/Users/l-ferrer/AppData/Local/Temp/Slicer/BCHGA_vtkMRMLScalarVolumeNodeC.nrrd</p>
<p>Reference Volume: C:/Users/l-ferrer/AppData/Local/Temp/Slicer/BCHGA_vtkMRMLScalarVolumeNodeB.nrrd</p>
<p>Output Volume: C:/Users/l-ferrer/AppData/Local/Temp/Slicer/BCHGA_vtkMRMLScalarVolumeNodeD.nrrd</p>
<p>Pixel Type: short</p>
<p>Interpolation: Linear</p>
<p>Background Value: 0</p>
<p>Warp By Transform: Identity</p>
<p>=====================================================</p>
<p>******* HERE *******D:\D\S\Slicer-0-build\BRAINSTools\BRAINSResample\BRAINSResample.cxx 475</p>
<p>itk::ExceptionObject (000000024AB5D870)</p>
<p>Location: “unknown”</p>
<p>File: D:\D\S\Slicer-0-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx</p>
<p>Line: 290</p>
<p>Description: itk::ERROR: NrrdImageIO(000001C04F65A7E0): ReadImageInformation: Error reading C:/Users/l-ferrer/AppData/Local/Temp/Slicer/BCHGA_vtkMRMLScalarVolumeNodeC.nrrd:</p>
<p>[nrrd] nrrdLoad: trouble reading “C:/Users/l-ferrer/AppData/Local/Temp/Slicer/BCHGA_vtkMRMLScalarVolumeNodeC.nrrd”</p>
<p>[nrrd] nrrdRead: trouble</p>
<p>[nrrd] _nrrdRead: trouble reading NRRD file</p>
<p>[nrrd] _nrrdFormatNRRD_read: trouble parsing space directions info |(0,97656250000000022,0,0) (0,0,97656250000000022,0) (0,0,2)|</p>
<p>[nrrd] _nrrdReadNrrdParse_space_directions: trouble getting space vector 1 of 3</p>
<p>[nrrd] _nrrdSpaceVectorParse: space dimension is 3, but seem to have 4 coefficients</p>
</blockquote>
<p>Apparently, the PET/CT images I got haven’t 4 dimensions.<br>
I tried with 4.11.20200629 r29190, slicer 4.11.20200930 r29402, slicer 4.1120210226  r29738<br>
I also tried with different PET/CT images, same results</p>
<p>What is going wrong here ? That must be obvious but I am blind <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>
<p>Best regards<br>
Ludovic</p>

---

## Post #2 by @pieper (2021-04-12 22:25 UTC)

<aside class="quote no-group" data-username="Ludovic_Ferrer" data-post="1" data-topic="17046">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ludovic_ferrer/48/5018_2.png" class="avatar"> Ludovic_Ferrer:</div>
<blockquote>
<p>(0,97656250000000022,0,0)</p>
</blockquote>
</aside>
<p>It looks like perhaps your machine’s locale has been set to something that prints decimal numbers using the comma character instead of the period character, so you get what looks like four comma separated numbers instead of three.</p>
<p>We had this problem before in Slicer and worked hard to make sure we always used the <code>C</code> LOCALE setting.  I’m not sure how it crept back.  Looks like this is your local build and maybe you changed something?  Do regular Slicer binaries work?</p>

---

## Post #3 by @Ludovic_Ferrer (2021-04-13 05:15 UTC)

<p>Hi Steve,<br>
nice shot. I will look at your suggestion.<br>
A part from this issue, slicer seems to work correclty, but i didn’t thoroughfully search for such bug.<br>
I am working on windows 10 that my company is taking care of. So, I am not sure i will have too much user rights to investigate. Il let you know here the results of my search.<br>
thanks a lot.<br>
Best regards<br>
Ludovic</p>

---

## Post #4 by @Ludovic_Ferrer (2021-04-13 06:23 UTC)

<p>ok, your suggestion works. not sure i did the right way as i had to get into the windows registry <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
best regards<br>
ludovic</p>

---

## Post #5 by @pieper (2021-04-13 11:52 UTC)

<p>Thanks for the report and glad you got things working <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>We hope to improve Slicer’s ability to be localized without being subject to this kind of issue with some of the older libraries.</p>

---
