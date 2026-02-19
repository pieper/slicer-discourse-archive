---
topic_id: 30872
title: "Save Patients Id In A List From Database With Python"
date: 2023-07-29
url: https://discourse.slicer.org/t/30872
---

# Save patients ID in a list from Database with Python

**Topic ID**: 30872
**Date**: 2023-07-29
**URL**: https://discourse.slicer.org/t/save-patients-id-in-a-list-from-database-with-python/30872

---

## Post #1 by @LisaAlborghetti (2023-07-29 17:16 UTC)

<p>Hi everyone,<br>
I’m quite a new entry in the Slicer world. I’m trying to use a python script for batch conversion of structures to .vtk but I face some problems. The first issue I would like to solve is this: I loaded two test patients files and it seems they are correcly imported in the Database, but then when I use slicer.dicomDatabase.patients() I get a list of integers instead of patients IDs and subsequently I get some errors, trying to call the patients in other parts of the code. Here is a simple example:</p>
<pre><code class="lang-auto">from DICOMLib import DICOMUtils

input_folder = '/Users/lisaalborghetti/Desktop/Patients/dicom'

DICOMUtils.openTemporaryDatabase()

DICOMUtils.importDicom(input_folder)

all_patients = slicer.dicomDatabase.patients()

print("Patient list: ", all_patients)

patient_names = {}

# Loop through the patient IDs and extract patient names

for patient_id in all_patients:
  patient_name = slicer.dicomDatabase.fileValue(patient_id, '0010,0010')
  patient_names[patient_id] = patient_name

for patient_id, patient_name in patient_names.items():
  print(f"Patient ID: {patient_id}, Patient Name: {patient_name}")
</code></pre>
<p>This is what I see in 3Dslicer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/386be3c1eff8a17b55a527958773ece04f4f934c.png" data-download-href="/uploads/short-url/837TeFNwrvkPq7WiE1Kx3OLMhQ0.png?dl=1" title="Screenshot 2023-07-29 at 19.10.10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/386be3c1eff8a17b55a527958773ece04f4f934c_2_690x63.png" alt="Screenshot 2023-07-29 at 19.10.10" data-base62-sha1="837TeFNwrvkPq7WiE1Kx3OLMhQ0" width="690" height="63" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/386be3c1eff8a17b55a527958773ece04f4f934c_2_690x63.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/386be3c1eff8a17b55a527958773ece04f4f934c_2_1035x94.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/386be3c1eff8a17b55a527958773ece04f4f934c_2_1380x126.png 2x" data-dominant-color="E8E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-07-29 at 19.10.10</span><span class="informations">1402×130 14.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And this the terminal output:<br>
Patient list:  (‘1’, ‘2’)<br>
Could not load  “1”<br>
DCMTK says:  No such file or directory<br>
File 1 could not be initialized.<br>
Could not load  “2”<br>
DCMTK says:  No such file or directory<br>
File 2 could not be initialized.<br>
Patient ID: 1, Patient Name:<br>
Patient ID: 2, Patient Name:</p>
<p>Am I doing something wrong?<br>
Thank you!</p>
<p>Lisa</p>

---

## Post #2 by @pieper (2023-07-29 17:55 UTC)

<p>Hi -</p>
<p>Since <code>PatientID</code> is assigned by the institution and they are not globally unique, Slicer assigns these integer local ids that are unique within the database.</p>
<p>The <code>slicer.dicomDatabase.fileValue</code> takes a path to a dicom instance file as an argument, hence the error message and the result of <code>None</code>.</p>
<p>To get from a Patient, who may have multiple studies, each of which with multiple series, and each of those with multiple instances, you can drill down with logic like in this example:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#iterate-through-dicom-series" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#iterate-through-dicom-series</a></p>

---

## Post #3 by @LisaAlborghetti (2023-07-31 13:37 UTC)

<p>Thanks a lot Steve, that was helpful!</p>

---
