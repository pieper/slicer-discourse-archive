# How To Calculate The SUV

**Topic ID**: 16831
**Date**: 2021-03-29
**URL**: https://discourse.slicer.org/t/how-to-calculate-the-suv/16831

---

## Post #1 by @akmal871026 (2021-03-29 20:22 UTC)

<p>Operating system: windows<br>
Slicer version: 4.13<br>
Expected behavior: can calculate the value SUV in y segmentation.<br>
Actual behavior:<br>
Hi, I have contour volume in PET image. I want to know about the SUV. I used the Pet Standard Uptake Value Computation. But failed. The error like below</p>
<p><em>PET Standard Uptake Value Computation standard error:</em></p>
<p><em>WARNING: In D:\D\P\Slicer-0-build\ITK\Modules\IO\GDCM\src\itkGDCMSeriesFileNames.cxx, line 100</em></p>
<p><em>GDCMSeriesFileNames (000002139BB38070): No Series were found</em></p>

---

## Post #2 by @pieper (2021-03-30 13:21 UTC)

<p>Try the latest stable release (4.11) for PET images and install the PET related extensions.  Several are not working yet for 4.13.  Also be sure the PET images have all the needed dicom header tags.</p>

---

## Post #3 by @akmal871026 (2021-03-31 20:10 UTC)

<p>I have installed all the PET extensions. But still failed.</p>
<p>Anyone knows this error when I reload all my data set? Could not load: 3: PET WB 3D AC as a Scalar Volume</p>

---

## Post #4 by @Liu_Lance (2022-04-06 18:27 UTC)

<p>hi Thanks,<br>
Could you tell what are all the needed dicom header tags? I load the scalar volume, I want to convert that PET scan to the SUV value</p>

---

## Post #5 by @akmal871026 (2022-04-06 18:35 UTC)

<p>Yes sure…whatsapp me 60143321631</p>

---

## Post #6 by @issakomi (2022-04-07 00:51 UTC)

<blockquote>
<p>Could you tell what are all the needed dicom header tags?</p>
</blockquote>
<p>S. <a href="https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)" rel="noopener nofollow ugc">QIBA FDG-PET/CT Standardized Uptake Value (SUV) Technical Subcommittee</a></p>
<p>Specially<br>
<a href="https://qibawiki.rsna.org/images/8/86/SUV_vendorneutral_pseudocode_20180626_DAC.pdf" rel="noopener nofollow ugc">Vendor-neutral pseudo-code for SUV calculation</a><br>
<a href="https://qibawiki.rsna.org/images/6/62/SUV_vendorneutral_pseudocode_happypathonly_20180626_DAC.pdf" rel="noopener nofollow ugc">Vendor-neutral pseudo-code for SUV calculation - extracted “happy path only”</a></p>

---

## Post #7 by @mikbuch (2023-03-24 14:51 UTC)

<p>If anyone else will be having this error, please refer to my answer in the other thread: <a href="https://discourse.slicer.org/t/pet-standard-uptake-value-computation/7491/4" class="inline-onebox">PET Standard Uptake Value Computation - #4 by mikbuch</a></p>

---
