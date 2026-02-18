# Easy way to display the metadata of a CT

**Topic ID**: 41220
**Date**: 2025-01-22
**URL**: https://discourse.slicer.org/t/easy-way-to-display-the-metadata-of-a-ct/41220

---

## Post #1 by @Matteboo (2025-01-22 14:16 UTC)

<p>Hello,</p>
<p>I’m working on cases transfered by an hospital. The case contains multiple CT. When I load the CT they are ordered by the series number. I want to order them by acquisition time to make it easier to understand the chronological order of the operation.</p>
<p>Does anybody knows how to do it ?</p>

---

## Post #2 by @Matteboo (2025-01-23 13:13 UTC)

<p>Here is a code snippet to load  all the series from a patient in chronological order and add the aquisition time in the volume name</p>
<pre><code class="lang-auto">import slicer
from DICOMLib import DICOMUtils

def load_and_sort_images_by_patient_name(patient_name):
    """
    Loads images of a patient from the 3D Slicer DICOM database,
    sorts them by acquisition time, and loads them in order.

    :param patient_name: Name of the patient  to search for.
    """
    # Get the DICOM database
    dicom_database = slicer.dicomDatabase

    if not dicom_database.isOpen:
        print("The DICOM database is not open.")
        return

    # Search for patients matching the given name
    patient_ids = dicom_database.patients()
    matched_patient_ids = [
        pid for pid in patient_ids
        if patient_name.lower() in dicom_database.displayedNameForPatient(pid).lower()
    ]

    if not matched_patient_ids:
        print(f"No patient found with the name: {patient_name}")
        return

    print(f"Patients found: {', '.join([dicom_database.displayedNameForPatient(pid) for pid in matched_patient_ids])}")

    # Iterate over each matching patient
    for patient_id in matched_patient_ids:
        print(f"Loading series for patient: {dicom_database.displayedNameForPatient(patient_id)}")

        # Get the studies for this patient
        study_ids = dicom_database.studiesForPatient(patient_id)

        # Retrieve all series for each study
        series_list = []
        for study_id in study_ids:
            series_ids = dicom_database.seriesForStudy(study_id)
            for series_id in series_ids:
                # Retrieve metadata for sorting
                filename = dicom_database.filesForSeries(series_id)[0]
                acquisition_time_string = slicer.dicomDatabase.fileValue(filename, "0008,0032")
                acquisition_time = int(acquisition_time_string[0:4])  
                series_list.append({
                    "series_id": series_id,
                    "acquisition_time": acquisition_time or "999999",  # Use a default value if the time is missing
                })

        # Sort the series by ascending acquisition time
        series_list.sort(key=lambda x: x["acquisition_time"])

        # Load the sorted series
        for series in series_list:
            try:
                print(f"Loading series {series['series_id']} with acquisition time {series['acquisition_time']}")
                load_output = DICOMUtils.loadSeriesByUID([series["series_id"]])
                if type(load_output) == str:
                    volumeNode = slicer.mrmlScene.GetNodeByID(load_output)
                    old_name = volumeNode.GetName()
                    L = len(str(series['acquisition_time']))
                    new_name = old_name + " " + str(series['acquisition_time'])[max(L-4, 0):L-2] + "h" + str(series['acquisition_time'])[L-2:L]
                    volumeNode.SetName(new_name)
                else:
                    for volumeid in load_output:
                        volumeNode = slicer.mrmlScene.GetNodeByID(volumeid)
                        old_name = volumeNode.GetName()
                        L = len(str(series['acquisition_time']))
                        new_name = old_name + " " + str(series['acquisition_time'])[max(L-4, 0):L-2] + "h" + str(series['acquisition_time'])[L-2:L]
                        volumeNode.SetName(new_name)
                    
            except Exception as e:
                print(f"Error while loading series {series['series_id']}: {e}")


# Example usage
# Replace "Patient_name_001" with the name of the patient
patient_name = "Patient_name_001"
load_and_sort_images_by_patient_name(patient_name)


all_volumes = slicer.util.getNodesByClass("vtkMRMLVolumeNode")
for volume_node in all_volumes:
    slicer.modules.volumes.logic().ApplyVolumeDisplayPreset(volume_node.GetVolumeDisplayNode(), "CT_ABDOMEN")


</code></pre>

---
