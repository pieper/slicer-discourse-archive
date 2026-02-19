---
topic_id: 34813
title: "Unspecified Error Opening Python Generated Dicom File In 3D"
date: 2024-03-10
url: https://discourse.slicer.org/t/34813
---

# Unspecified Error Opening Python-Generated DICOM File in 3D Slicer

**Topic ID**: 34813
**Date**: 2024-03-10
**URL**: https://discourse.slicer.org/t/unspecified-error-opening-python-generated-dicom-file-in-3d-slicer/34813

---

## Post #1 by @rcapozza (2024-03-10 17:48 UTC)

<p>Hello,</p>
<p>I’ve created a DICOM file using a Python script that processes a pixel array. This file opens without any issues in applications like Fiji and ezDICOM, indicating that the data is intact and correctly formatted according to the DICOM standard.</p>
<p>However, when I attempt to open this same file in 3D Slicer, I encounter an unspecified error, which prevents me from viewing or working with the file in that environment. This issue seems to be specific to 3D Slicer, as other DICOM-compatible software can read the file without any problems.</p>
<p>I’m seeking assistance or insights from anyone who might have faced similar challenges or has expertise in DICOM file compatibility with 3D Slicer. While I’m unable to attach the file here directly, I’m willing to share it privately if that helps in diagnosing the issue.</p>
<p>Python script:</p>
<pre><code class="lang-auto">import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom import uid

def save_dicom(image_dens, patName, patId):

    file_meta = FileMetaDataset()
    file_meta.MediaStorageSOPClassUID = uid.PYDICOM_IMPLEMENTATION_UID
    file_meta.MediaStorageSOPInstanceUID = uid.generate_uid()
    file_meta.ImplementationClassUID = uid.PYDICOM_IMPLEMENTATION_UID

    ds = Dataset()
    ds.file_meta = file_meta
    ds.is_little_endian = True
    ds.is_implicit_VR = True


    ds.PatientName = patName
    ds.PatientID = str(patId)


    ds.Modality = 'CT'
    ds.SeriesInstanceUID = uid.generate_uid()
    ds.StudyInstanceUID = uid.generate_uid()
    ds.FrameOfReferenceUID = uid.generate_uid()


    ds.StudyDate = '20240101'
    ds.StudyTime = '120000'


    ds.Rows = image_dens.shape[0]
    ds.Columns = image_dens.shape[1]


    ds.PixelRepresentation = 1
    ds.BitsStored = 16
    ds.BitsAllocated = 16
    ds.SamplesPerPixel = 1
    ds.HighBit = 15
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.PixelData = image_dens.tobytes()



    ds.save_as("output.dcm")
</code></pre>
<p>Thank you very much for your time and help.</p>

---

## Post #2 by @pieper (2024-03-10 18:40 UTC)

<p>You should check the error log.</p>
<p>It looks like you don’t have ImagePositionPatient or ImageOrientationPatient so file can’t be interpreted as 3D.  There may be other issues - you can search for dciodvfy to get more feedback on how to make sure your data is conformant.</p>

---
