# OpenDose3D: DICOMError - Attribute 'acquisition' is empty (Siemens SPECT-CT)

**Topic ID**: 41392
**Date**: 2025-01-31
**URL**: https://discourse.slicer.org/t/opendose3d-dicomerror-attribute-acquisition-is-empty-siemens-spect-ct/41392

---

## Post #1 by @Angie_Tatiana_Marin (2025-01-31 05:12 UTC)

<p>Hello everyone,</p>
<p>I am using <strong>3D Slicer 5.6.2</strong> with the <strong>OpenDose3D</strong> module to process SPECT-CT images from a <strong>Siemens scanner</strong> for quantitative imaging with <strong>Lu-177, Tc-99m, and I-131</strong>. However, I am encountering the following error:<br>
<strong>Logic.errors.DICOMError: Attribute ‘acquisition’ is empty</strong></p>
<p>However, when I inspect the DICOM metadata (using Slicer’s DICOM browser), the relevant tags are present:</p>
<ul>
<li><code>(0008,0020) Study Date: 20240813</code></li>
<li><code>(0008,0022) Acquisition Date: 20240813</code></li>
<li><code>(0008,0030) Study Time: 180138.383000</code></li>
<li><code>(0008,0032) Acquisition Time: 183453.468508</code></li>
</ul>
<p>It seems that OpenDose3D does not recognize the <code>AcquisitionDate</code> and <code>AcquisitionTime</code> values, even though they are correctly stored in the DICOM headers.<br>
I am running <strong>Windows 10</strong> and using the latest OpenDose3D extension.</p>
<p>Has anyone encountered a similar issue with Siemens DICOM files? Any advice would be greatly appreciated. Thanks!</p>
<p><a>Uploading: dicomtags.jpg…</a><br>
<a>Uploading: error.jpg…</a></p>

---

## Post #2 by @Alex_Vergara (2025-01-31 13:07 UTC)

<p>Please create an issue here <a href="https://gitlab.com/opendose/opendose3d/-/issues" rel="noopener nofollow ugc">Issues · OpenDose / SlicerOpenDose3D · GitLab</a></p>

---

## Post #3 by @fragosoj (2025-01-31 14:19 UTC)

<p>OpenDose3D should work smoothly if the Acquisition Date is stored.</p>
<p>Could you please check that <strong>all</strong> your images have the Acquisition Date and modality correctly stored?</p>

---

## Post #4 by @akmal871026 (2025-02-09 07:47 UTC)

<p>Dear <a class="mention" href="/u/angie_tatiana_marin">@Angie_Tatiana_Marin</a> ,</p>
<p>Actually, the DICOM attribute from SIEMENS are quite tricky. Some of the parameter for example acquisition time and date, they address with the different name.</p>
<p>I my experience, the “number of angular” is represents the “projection angle” something like that. You have to check particularly.</p>

---

## Post #5 by @Angie_Tatiana_Marin (2025-02-10 02:39 UTC)

<p>Hello, I already checked the dicomtags of the images, and they all have the information. I don’t know how to solve this.<br>
How can it be corrected?</p>
<p>Thank you</p>

---

## Post #6 by @akmal871026 (2025-02-24 01:19 UTC)

<p>Dear <a class="mention" href="/u/angie_tatiana_marin">@Angie_Tatiana_Marin</a> , try look up at “<strong>MRML node information</strong>”</p>

---
