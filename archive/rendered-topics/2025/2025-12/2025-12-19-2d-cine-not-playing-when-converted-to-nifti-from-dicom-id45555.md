# 2D cine not playing when converted to nifti from dicom

**Topic ID**: 45555
**Date**: 2025-12-19
**URL**: https://discourse.slicer.org/t/2d-cine-not-playing-when-converted-to-nifti-from-dicom/45555

---

## Post #1 by @Nshehata (2025-12-19 12:48 UTC)

<p>Operating system: Linux also MacOS<br>
Slicer version: 5.8.1<br>
Expected behavior: Play button to be enabled when importing as DICOM<br>
Actual behavior: Play button disabled and fixed on one slice only</p>
<p>I thought maybe the problem was with the conversion. I tried several methods:</p>
<ol>
<li>dcm2niix in python</li>
<li>MRIcroGL</li>
<li><strong>In 3D Slicer:</strong>
<ol>
<li>Import dcm (plays perfectly fine)</li>
<li>Right-clicked and exported it as Nifti, save the nifti file.</li>
<li>close 3D slicer</li>
<li>Opened 3D slicer and imported the NIFTI file (play button disabled, showing one slice only).</li>
</ol>
</li>
</ol>
<p>My last attempt is saving each frame separately as nifti then merging them using fsl into one nifti file using the below code but same outcome still :’(</p>
<pre><code class="lang-auto">import os

import json
import SimpleITK as sitk
import numpy as np
import pydicom


def create_slicer_sequence_from_dicom(dicom_folder, output_mrb_folder):

"""

    Create ordered NIfTI frames from 2D cine DICOMs and

    extract temporal spacing from TriggerTime.

    """

os.makedirs(output_mrb_folder, exist_ok=True)


print(f"Reading DICOM files from: {dicom_folder}")


dicom_files = sorted([f for f in os.listdir(dicom_folder) if f.endswith(".dcm")])

if not dicom_files:

raise ValueError(f"No DICOM files found in {dicom_folder}")


print(f"Found {len(dicom_files)} DICOM files (timepoints)")




# -------------------------

# Read Trigger Times

# -------------------------

trigger_times = []

dicom_info = []


for f in dicom_files:

ds = pydicom.dcmread(

os.path.join(dicom_folder, f),

stop_before_pixels=True

        )


if "TriggerTime" not in ds:

raise RuntimeError(f"Missing TriggerTime in {f}")


trigger_time = float(ds.TriggerTime)

trigger_times.append(trigger_time)

dicom_info.append((f, trigger_time))


# Sort by TriggerTime (true temporal order)

dicom_info.sort(key=lambda x: x[1])

trigger_times = np.array([x[1] for x in dicom_info])



# Compute frame time (ms → s)

dt_ms = np.diff(trigger_times)

frame_time_ms = np.median(dt_ms)

pixdim4 = frame_time_ms / 1000.0

print(f"Estimated frame time: {frame_time_ms:.3f} ms")

print(f"pixdim4 = {pixdim4:.6f} seconds")




# Save pixdim4 for later use

with open(os.path.join(output_mrb_folder, "pixdim4.txt"), "w") as f:

f.write(f"{pixdim4}\n")


# -------------------------

# Write ordered NIfTI frames

# -------------------------

volumes_folder = os.path.join(output_mrb_folder, "volumes")

os.makedirs(volumes_folder, exist_ok=True)


volume_files = []


for i, (fname, _) in enumerate(dicom_info):

fpath = os.path.join(dicom_folder, fname)

img = sitk.ReadImage(fpath, sitk.sitkFloat32)




out_filename = f"frame_{i:03d}.nii.gz"

out_path = os.path.join(volumes_folder, out_filename)

sitk.WriteImage(img, out_path)




volume_files.append(out_filename)




if i % 10 == 0 or i == len(dicom_info) - 1:

print(f"  Processed {i+1}/{len(dicom_info)} frames")




print("✓ NIfTI frames written")




return output_mrb_folder





# --------------------

# Usage

# --------------------

dicom_folder = "path to dicom images"

output_folder = "path to/slicer_sequence"



create_slicer_sequence_from_dicom(dicom_folder, output_folder)


import os
import glob
import subprocess
import nibabel as nib

volumes_folder = "path to /slicer_sequence/volumes"
pixdim4_file = "path to /slicer_sequence/pixdim4.txt"

output_4d_cine = "./cine_4d.nii.gz"
output_4d_cine_fixed = ./cine_4d_with_tr.nii.gz"

# -------------------------
# Collect frames
# -------------------------
frame_files = sorted(glob.glob(os.path.join(volumes_folder, "frame_*.nii.gz")))
if not frame_files:
    raise RuntimeError("No NIfTI frames found")

print(f"Found {len(frame_files)} frames")

# -------------------------
# Merge with FSL
# -------------------------
cmd = ["fslmerge", "-t", output_4d_cine] + frame_files
print("Running:", " ".join(cmd))
subprocess.run(cmd, check=True)

# -------------------------
# Apply pixdim4
# -------------------------
with open(pixdim4_file) as f:
    pixdim4 = float(f.read().strip())

img = nib.load(output_4d_cine)
data = img.get_fdata()
affine = img.affine
hdr = img.header.copy()

hdr["pixdim"][4] = pixdim4

nib.save(
    nib.Nifti1Image(data, affine, hdr),
    output_4d_cine_fixed
)

print(f" 4D cine created with correct timing:")
print(f"   {output_4d_cine_fixed}")

</code></pre>

---
