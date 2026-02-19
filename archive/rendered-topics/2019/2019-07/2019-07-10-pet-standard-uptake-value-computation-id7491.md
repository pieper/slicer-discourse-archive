---
topic_id: 7491
title: "Pet Standard Uptake Value Computation"
date: 2019-07-10
url: https://discourse.slicer.org/t/7491
---

# PET Standard Uptake Value Computation

**Topic ID**: 7491
**Date**: 2019-07-10
**URL**: https://discourse.slicer.org/t/pet-standard-uptake-value-computation/7491

---

## Post #1 by @qimo601 (2019-07-10 03:17 UTC)

<p>Hi,everyone.<br>
I have a question about the calculation formulas of SUV for PET, when i use the moudle " PETStandardUptakeValueComputation" and extension “PET DICOM”<br>
As we know, the Suv formula is as follows<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51414bbac094f875eb563dbf113fd9ef51db4a8e.png" alt="%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190710094712" data-base62-sha1="bAOznYbHntU1ARDKy6ALUk39qSG" width="628" height="292"></p>
<p><strong>But I don’t know what’s the scan start time?Is it the Series Time or the Acquisition Time?</strong><br>
<strong>And their SUV results are different.</strong></p>
<p>(0008,0031) TM 153348 # Series Time<br>
(0008,0032) TM 154644.500000 # Acquisition Time<br>
(0010,1030) DS 100.788 # Patient’s Weight<br>
(0018,1072) TM 142110.000000 # Radiopharmaceutical Start Time<br>
(0018,1074) DS 552410034.17969 # Radionuclide Total Dose<br>
(0018,1075) DS 6586.2 # Radionuclide Half Life</p>
<p>Thank you very much.<br>
qimo</p>

---

## Post #2 by @mikbuch (2023-02-18 22:44 UTC)

<p>Up for this question</p>

---

## Post #3 by @issakomi (2023-02-18 22:50 UTC)

<p>S. <a href="https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)" class="inline-onebox" rel="noopener nofollow ugc">Standardized Uptake Value (SUV) - QIBA Wiki</a></p>

---

## Post #4 by @mikbuch (2023-03-24 14:50 UTC)

<p>Thank you <a class="mention" href="/u/issakomi">@issakomi</a> for the reference. I am still in the process of trying to implement the activity concentration to SUV conversion algorithm.</p>
<p>Meanwhile, with this presentation: <a href="https://www.na-mic.org/w/img_auth.php/c/ca/RSNA2011_QI.pdf" rel="noopener nofollow ugc">https://www.na-mic.org/w/img_auth.php/c/ca/RSNA2011_QI.pdf</a> , I was finally able to get the <code>PET Standard Update Value Computation</code> module to work.</p>
<p>There were to issues I was dealing with:</p>
<p>(1) I didn’t know how to convert segment to LabelMapVolume (the “VOI” from the linked presentation). I managed to do it using this option:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe3d644642fcdcb22a8d7f78700d4b6e68a8cf5f.png" data-download-href="/uploads/short-url/Ah6O8fF6igDaCO6LrezJEIpgl8b.png?dl=1" title="Screenshot 2023-03-24 at 15.34.48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe3d644642fcdcb22a8d7f78700d4b6e68a8cf5f_2_222x500.png" alt="Screenshot 2023-03-24 at 15.34.48" data-base62-sha1="Ah6O8fF6igDaCO6LrezJEIpgl8b" width="222" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe3d644642fcdcb22a8d7f78700d4b6e68a8cf5f_2_222x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe3d644642fcdcb22a8d7f78700d4b6e68a8cf5f_2_333x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe3d644642fcdcb22a8d7f78700d4b6e68a8cf5f_2_444x1000.png 2x" data-dominant-color="EBECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-24 at 15.34.48</span><span class="informations">1254×2812 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(2) Initially, I have not understood the documentation correctly:</p>
<blockquote>
<ul>
<li>Input PET Volume (<em>PETVolume</em>): Input PET volume for SUVbw computation <strong>(must be the same volume as pointed to by the DICOM path!)</strong>.</li>
</ul>
</blockquote>
<p>Source: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/petstandarduptakevaluecomputation.html" class="inline-onebox" rel="noopener nofollow ugc">PET Standard Uptake Value Computation — 3D Slicer documentation</a></p>
<p>It means, that you have to select the proper <strong>subdirectory</strong> within the DICOM directory with your data.</p>
<p>I.e., in my case it was the “0003” subdirectory:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc2bfda503643075b2eeeb0a5da9fed7c56b4ee1.png" data-download-href="/uploads/short-url/qQE0SXmf7pCiDdf1dWlsCtZQeU9.png?dl=1" title="Screenshot 2023-03-24 at 15.38.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc2bfda503643075b2eeeb0a5da9fed7c56b4ee1_2_690x422.png" alt="Screenshot 2023-03-24 at 15.38.27" data-base62-sha1="qQE0SXmf7pCiDdf1dWlsCtZQeU9" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc2bfda503643075b2eeeb0a5da9fed7c56b4ee1_2_690x422.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc2bfda503643075b2eeeb0a5da9fed7c56b4ee1_2_1035x633.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc2bfda503643075b2eeeb0a5da9fed7c56b4ee1_2_1380x844.png 2x" data-dominant-color="F4F6F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-24 at 15.38.27</span><span class="informations">2664×1632 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If some upper-level directory was selected, i.e., the directory containing all the data (from the CD), or the “DCMS” directory, then I was getting the following error:</p>
<pre><code class="lang-auto">PET Standard Uptake Value Computation standard error:

WARNING: In /Volumes/D/S/S-0-build/ITK/Modules/IO/GDCM/src/itkGDCMSeriesFileNames.cxx, line 100
GDCMSeriesFileNames (0x7f993a69e530): No Series were found

PET Standard Uptake Value Computation standard output:
list.SUVOutputStringFile = /private/var/folders/8j/8tw8x4sx49384vtn35xcpwn00000gr/T/Slicer-mbuch/36400_O1g87aQq7f.params

Done reading the file /private/var/folders/8j/8tw8x4sx49384vtn35xcpwn00000gr/T/Slicer-mbuch/DGEAA_vtkMRMLScalarVolumeNodeE.nrrd

Done reading the file /private/var/folders/8j/8tw8x4sx49384vtn35xcpwn00000gr/T/Slicer-mbuch/DGEAA_vtkMRMLLabelMapVolumeNodeB.nrrd
</code></pre>
<p>In fact, I think it is the same error <a class="mention" href="/u/akmal871026">@akmal871026</a> was getting (for the same reason): <a href="https://discourse.slicer.org/t/how-to-calculate-the-suv/16831" class="inline-onebox">How To Calculate The SUV</a></p>
<hr>
<p>Btw., <a class="mention" href="/u/issakomi">@issakomi</a> , maybe do you know where can I find a source code for the <code>PET Standard Update Value Computation</code> module, or for the <code>SUV Factor Calculator</code> module? (I am still getting errors with <code>SUV Factor Calculator</code>) – I would like to use this source code to see how the activity concentration to SUV conversion is implemented there.</p>

---

## Post #5 by @mikbuch (2023-03-24 15:11 UTC)

<p>I think I found the source code: <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/PETStandardUptakeValueComputation/PETStandardUptakeValueComputation.cxx" class="inline-onebox" rel="noopener nofollow ugc">Slicer/PETStandardUptakeValueComputation.cxx at main · Slicer/Slicer · GitHub</a></p>

---

## Post #6 by @lassoan (2023-03-26 13:42 UTC)

<p>It is great that you have been able to figure these out! It would not be hard to modernize this module to make it much more convenient to use:</p>
<ol>
<li>Allow using segmentation as input (without the need to manually export to labelmap volume) - for example, by temporarily creating a labelmap node for the computation</li>
<li>Allow using a volume node as input (without the need to manually select some DICOM folders) - because the volume node contains DICOM UIDs that can be used to look up the filenames or any additional required DICOM fields</li>
</ol>
<p>Would you be interested in working on this? We can help you with getting started.</p>

---

## Post #7 by @mikbuch (2023-03-27 08:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , the modifications you mentioned would very helpful, indeed. I would also add a more general remark:</p>
<ol start="3">
<li>Explain (e.g., in the documentation), how “raw” PET-CT values - activity concentration - are converted into SUVs, i.e., how the conversion algorithm work (with a link to the implementation in Slicer 3D).</li>
</ol>
<p>Now it is not mentioned in the documentation, and there is no link to the RSNA’s wiki, nor to the scanner manufacturers documentation and manuals, and <a class="mention" href="/u/issakomi">@issakomi</a> has to provide the links on the forum each time someone asks about that <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I can give it a try with these modifications, but I’d start with some clarifications in the documentation, if you don’t mind. I tried to get to know where the sourcecode for the documentation is stored (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/petstandarduptakevaluecomputation.html" class="inline-onebox" rel="noopener nofollow ugc">PET Standard Uptake Value Computation — 3D Slicer documentation</a>) , but “Edit on GitHub” redirects to the “includes”. Then, based on this commit message: <a href="https://github.com/Slicer/Slicer/commit/b82b68f436b3b56b7dc125d8905cd8f5af86395b" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add automatically generated CLI module documentation · Slicer/Slicer@b82b68f · GitHub</a> I thought that the docs are somehow generated based on the XML files, e.g.: <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/PETStandardUptakeValueComputation/PETStandardUptakeValueComputation.xml" class="inline-onebox" rel="noopener nofollow ugc">Slicer/PETStandardUptakeValueComputation.xml at main · Slicer/Slicer · GitHub</a> , but it seems they are generated some other way. If you could give me a hint, a link to some Developer guide about how the docs are generated, I’d suggest some changes in a pull request.</p>

---

## Post #8 by @mikbuch (2023-04-19 22:50 UTC)

<p>I managed to re-implement the conversion algorithm. The process of getting to this result, including references to Slicer modules’ source code and RSNA’s documentation can be found in my post: <a href="https://www.mindyourdata.org/posts/calculating-suvmax-for-pet-ct-ge-scanner/" class="inline-onebox" rel="noopener nofollow ugc">Calculating SUVmax for GE’s PET/CT scanner – Mind Your Data</a>. Maybe someone will find it helpful.</p>
<p>Analyzing the Slicer’s implementation of the conversion algorithm, there is also a direct answer to <a class="mention" href="/u/qimo601">@qimo601</a> 's original question: scan start time is Series Time (0008,0031), see: <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx#L616-L657" class="inline-onebox" rel="noopener nofollow ugc">Slicer-PETDICOMExtension/SUVFactorCalculator.cxx at master · QIICR/Slicer-PETDICOMExtension · GitHub</a></p>
<hr>
<p>Interestingly, I am still unable to get exactly the same SUVmax results as GE’s Work Station for a given ROI. We are getting about 5% differences, and I have no idea yet what may be causing this.</p>

---

## Post #9 by @AGGDor (2023-11-12 07:20 UTC)

<p>Hi Mikołaj.</p>
<p>Thanks so much for looking at this. I’ve also struggled with the SUV calculations in Slicer which would ideally be updated to work with more vendor formats. The <a href="https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)" rel="noopener nofollow ugc">QIBA wiki</a> has been a useful resource.</p>
<p>With regards to the SUVmax differences you are seeing between Slicer and GE’s workstation, I can think of a few possibilities offhand: 1) error in formula/method (recheck, with reference to QIBA docs)?<br>
2) are the SUV’s normalised in the same way? e.g., body weight vs lean body weight.<br>
3) differences in the number of significant figures used by GE or Slicer when performing the calculations?<br>
4) differences in how GE and Slicer treat peripheral voxels at the VOI margin (I think some programs include these voxels, others exclude, some may split values - the reference manual may specify which)? Having said that, SUVmax should be pretty robust across packages, since voxel with highest counts is rarely peripheral, so would check formulas and normalisation method as first steps and maybe check SUVmax results from a few additional software packages?</p>
<p>Good luck.</p>

---

## Post #10 by @mikbuch (2024-01-18 23:48 UTC)

<p>Hi Alex,</p>
<p>My version for sure works, because it has been validated with GE Workstation. How exactly slicer calculates I cannot tell. As I mentioned earlier, I could try to determine that (and/or try to fix it), but I stumbled into some issues (maybe more of a technical nature, regarding Slicer development: <a href="https://discourse.slicer.org/t/pet-standard-uptake-value-computation/7491/7" class="inline-onebox">PET Standard Uptake Value Computation - #7 by mikbuch</a>) – I would need help first with these issues, to try to validate/fix Slicer’s SUV calculator.</p>

---

## Post #11 by @mikbuch (2024-01-20 01:56 UTC)

<p>The image <a href="/u/qimo601">qimo601</a> posted in his question (the very beginning of the current post) is no longer available (link broken). Below I paste the image for future reference:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51414bbac094f875eb563dbf113fd9ef51db4a8e.png" alt="pet_suv_formula" data-base62-sha1="bAOznYbHntU1ARDKy6ALUk39qSG" width="628" height="292"></p>
<p>A new source: <a href="https://www.radiantviewer.com/img/forum/pet_suv_formula.png" rel="noopener nofollow ugc">https://www.radiantviewer.com/img/forum/pet_suv_formula.png</a></p>

---
