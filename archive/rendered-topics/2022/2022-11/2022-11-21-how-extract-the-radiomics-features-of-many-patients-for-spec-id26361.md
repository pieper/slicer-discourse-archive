# How extract the radiomics features of many patients for specific region of interests by using python interactor instead of manually one by one patient?

**Topic ID**: 26361
**Date**: 2022-11-21
**URL**: https://discourse.slicer.org/t/how-extract-the-radiomics-features-of-many-patients-for-specific-region-of-interests-by-using-python-interactor-instead-of-manually-one-by-one-patient/26361

---

## Post #1 by @NAVEED_ASHRAF (2022-11-21 20:31 UTC)

<p>How extract the radiomics features of many patients for specific region of interests by using python interactor instead of manually one by one patient?</p>

---

## Post #2 by @rbumm (2022-11-22 15:51 UTC)

<p>Once you have installed SlicerRadiomics → pyradiomics should be available in Python Interactor.<br>
You could then write a Python script and call the radiomics featureextractor on different data sets like it is <a href="https://pyradiomics.readthedocs.io/en/latest/usage.html#interactive-use">shown here</a>. You would probably do that from a loop.</p>
<p>In case you have a working example, please post it here.</p>

---

## Post #3 by @NAVEED_ASHRAF (2022-11-23 10:56 UTC)

<p>Dear<br>
Sir, I am facing the problem in the section of ‘setting up data’.Can you help me ?</p>
<p>regards<br>
Naveed ashraf</p>

---

## Post #4 by @rbumm (2022-11-23 20:19 UTC)

<p><a class="mention" href="/u/naveed_ashraf">@NAVEED_ASHRAF</a> that is too vague.<br>
Please specify what the problem is and what does not work.</p>
<p>Could you not just load your patients one by one and run SlicerRadiomics manually on each of the datasets?</p>

---

## Post #5 by @NAVEED_ASHRAF (2023-01-16 08:09 UTC)

<p>Hi Dear Sir,<br>
I want to export radiomics features of many patients at once time.For example if we have a dicom file (data) of 10 patients in 3D slicer then we want to use python code to automatically export 107 features of each patient at once a time . Instead of manually exporting the 107 radiomics features of each patient separately we want to export all radiomics features of all patients at once a time.please recommend or give us a script which will perform this operation.</p>

---

## Post #6 by @rbumm (2023-01-16 10:42 UTC)

<p>You can load DICOM data into 3D Slicer from a folder <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder">like shown here</a>.</p>
<p>Probably need to find a programmer or learn to</p>
<ul>
<li>call this code</li>
<li>segment your region of interest</li>
<li>export the radiomics features of that region</li>
</ul>
<p>from a loop.</p>
<p>Please understand that we can not provide fully scripted solutions in this forum.</p>

---

## Post #7 by @Vin_S (2024-06-04 20:41 UTC)

<p>Hi, I was wondering if you knew how to overcome <a href="https://discourse.slicer.org/t/module-slicerradiomics-reported-an-error/31122">this error</a> that I had run into with accessing the SlicerRadiomics Logic class</p>

---
