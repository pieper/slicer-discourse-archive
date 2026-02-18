# Split multiframe dicom to series dicom code problem

**Topic ID**: 45374
**Date**: 2025-12-05
**URL**: https://discourse.slicer.org/t/split-multiframe-dicom-to-series-dicom-code-problem/45374

---

## Post #1 by @Berk_Gezgin (2025-12-05 13:03 UTC)

<p>Hello<br>
I wrote the following code. My goal here is to slice a single DICOM file and establish a standard. However, the sliced DICOM does not appear the same as the original DICOM in the slicer program. The positions and spacings look different. What is the reason for this?<br>
Thanks in advance for your answer.</p>
<pre data-code-wrap="python"><code class="lang-python">import pydicom
import os
import numpy as np
from pydicom.uid import generate_uid

def calculate_geometry(ds):
    shared_fg = ds.SharedFunctionalGroupsSequence[0]
    pixel_measures_shared = shared_fg.PixelMeasuresSequence[0]
    spacing_x = float(pixel_measures_shared.PixelSpacing[0])
    spacing_y = float(pixel_measures_shared.PixelSpacing[1])

    per_frame = ds.PerFrameFunctionalGroupsSequence

    ipp1 = np.array(per_frame[0].PlanePositionSequence[0].ImagePositionPatient, dtype=float)
    ipp2 = np.array(per_frame[1].PlanePositionSequence[0].ImagePositionPatient, dtype=float)
    diff_vector = ipp2 - ipp1

    iop = np.array(per_frame[0].PlaneOrientationSequence[0].ImageOrientationPatient, dtype=float)
    row_cos = iop[:3]
    col_cos = iop[3:]
    slice_normal = np.cross(row_cos, col_cos)
    slice_normal = slice_normal / np.linalg.norm(slice_normal)

    spacing_between_slices = abs(np.dot(diff_vector, slice_normal))

    slice_thickness = spacing_between_slices

    if hasattr(per_frame[0], "PixelMeasuresSequence"):
        pm = per_frame[0].PixelMeasuresSequence[0]
        if hasattr(pm, "SliceThickness"):
            slice_thickness = float(pm.SliceThickness)
        if hasattr(pm, "SpacingBetweenSlices"):
            spacing_between_slices = float(pm.SpacingBetweenSlices)

    return spacing_x, spacing_y, slice_thickness, spacing_between_slices


def extract_multiframe_to_series(input_path, output_dir):
    ds = pydicom.dcmread(input_path)
    os.makedirs(output_dir, exist_ok=True)

    frames = int(ds.NumberOfFrames)
    pixel_array = ds.pixel_array

    sx, sy, slice_thickness, spacing_between = calculate_geometry(ds)

    new_series_uid = generate_uid()
    frame_of_reference_uid = ds.FrameOfReferenceUID 

    print(f"Detected voxel size: {sx:.4f} × {sy:.4f} × {spacing_between:.4f} mm")
    print(f"Total frames: {frames}")
    print(f"New SeriesInstanceUID: {new_series_uid}")

    per_frame = ds.PerFrameFunctionalGroupsSequence

    for i in range(frames):
        frame_fg = per_frame[i]

        iop = frame_fg.PlaneOrientationSequence[0].ImageOrientationPatient
        ipp = frame_fg.PlanePositionSequence[0].ImagePositionPatient

        frame_pixels = pixel_array[i]

        new_ds = pydicom.Dataset()

        new_ds.file_meta = pydicom.Dataset()
        new_ds.file_meta.TransferSyntaxUID = ds.file_meta.TransferSyntaxUID
        new_ds.file_meta.MediaStorageSOPClassUID = ds.SOPClassUID
        new_ds.file_meta.MediaStorageSOPInstanceUID = generate_uid()
        new_ds.file_meta.ImplementationClassUID = pydicom.uid.PYDICOM_IMPLEMENTATION_UID

        new_ds.PatientName = ds.get("PatientName", "Anonymous")
        new_ds.PatientID = ds.get("PatientID", "ID")
        new_ds.PatientBirthDate = getattr(ds, "PatientBirthDate", "")
        new_ds.PatientSex = getattr(ds, "PatientSex", "")

        new_ds.StudyInstanceUID = ds.StudyInstanceUID
        new_ds.StudyDate = getattr(ds, "StudyDate", "")
        new_ds.StudyTime = getattr(ds, "StudyTime", "")
        new_ds.StudyDescription = getattr(ds, "StudyDescription", "")

        new_ds.SeriesInstanceUID = new_series_uid
        new_ds.SeriesNumber = 1001
        new_ds.SeriesDescription = f"{getattr(ds, 'SeriesDescription', 'Tomosynthesis')} - Split"
        new_ds.Modality = ds.Modality

        new_ds.SOPClassUID = ds.SOPClassUID
        new_ds.SOPInstanceUID = generate_uid()
        new_ds.InstanceNumber = i + 1

        new_ds.ImageOrientationPatient = iop
        new_ds.ImagePositionPatient = ipp
        new_ds.FrameOfReferenceUID = frame_of_reference_uid

        new_ds.Rows = ds.Rows
        new_ds.Columns = ds.Columns
        new_ds.PixelSpacing = [str(sx), str(sy)]
        new_ds.SliceThickness = str(slice_thickness)
        new_ds.SpacingBetweenSlices = str(spacing_between)

        new_ds.SamplesPerPixel = ds.SamplesPerPixel
        new_ds.PhotometricInterpretation = ds.PhotometricInterpretation
        new_ds.BitsAllocated = ds.BitsAllocated
        new_ds.BitsStored = ds.BitsStored
        new_ds.HighBit = ds.HighBit
        new_ds.PixelRepresentation = ds.PixelRepresentation

        if "WindowCenter" in ds:
            new_ds.WindowCenter = ds.WindowCenter
            new_ds.WindowWidth = ds.WindowWidth
        if "WindowCenterWidthExplanation" in ds:
            new_ds.WindowCenterWidthExplanation = ds.WindowCenterWidthExplanation

        new_ds.PixelData = frame_pixels.tobytes()

        out_path = os.path.join(output_dir, f"{i+1:04d}.dcm")
        pydicom.dcmwrite(out_path, new_ds)

if __name__ == "__main__":
    extract_multiframe_to_series(r"tomo.dcm", r"DICOM_SPLIT")
</code></pre>
<p>The metadata for the first slice of the series DICOM appears as follows.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05dcd489e4164f9a85141895da000a43b17e7f08.png" data-download-href="/uploads/short-url/PRvRzkejdELikOwdeednd4fFck.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dcd489e4164f9a85141895da000a43b17e7f08_2_690x276.png" alt="image" data-base62-sha1="PRvRzkejdELikOwdeednd4fFck" width="690" height="276" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dcd489e4164f9a85141895da000a43b17e7f08_2_690x276.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dcd489e4164f9a85141895da000a43b17e7f08_2_1035x414.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dcd489e4164f9a85141895da000a43b17e7f08_2_1380x552.png 2x" data-dominant-color="262626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1438×576 42 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-12-05 13:40 UTC)

<p>It’s hard to say from a quick look at your code.  It would be great if you could share the full reproducible example, including the source image data.  Creating single-frame instances from multi-frames should be well-defined but I’m not aware of any worked out examples, so your code could be an example for future reference.</p>
<p>What you can do to test is import the multi-frame into Slicer and then re-export it and it should give you single-frames that you can compare.</p>

---

## Post #3 by @Berk_Gezgin (2025-12-05 13:51 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="45374">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>What you can do to test is import the multi-frame into Slicer and then re-export it and it should give you single-frames that you can compare.</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9de89c076d072931974b48af5bb477dbab98fc5e.png" data-download-href="/uploads/short-url/mwVkeE3NyroQ2Xj8kXZDbOldjtA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9de89c076d072931974b48af5bb477dbab98fc5e.png" alt="image" data-base62-sha1="mwVkeE3NyroQ2Xj8kXZDbOldjtA" width="690" height="207" data-dominant-color="262626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">803×242 7.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
For example, the meta data of the DICOM series I created here had a pixel spacing of 0.6. However, when exported from Slicer, it became 1.1.<br>
My goal is to split the frames into their original 1:1 format when a single DICOM arrives and capture a single standard.</p>

---

## Post #4 by @pieper (2025-12-05 14:38 UTC)

<p>If you can share a deidentified example dataset that illustrates the problem people should be able to help.  Otherwise it’s not realistic to ask people to read your code an help you debug.</p>

---
