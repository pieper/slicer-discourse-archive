# DICOM to Voxel(python) - Landmark Placement Issue for DL Dataset

**Topic ID**: 44366
**Date**: 2025-09-05
**URL**: https://discourse.slicer.org/t/dicom-to-voxel-python-landmark-placement-issue-for-dl-dataset/44366

---

## Post #1 by @nik_47 (2025-09-05 17:45 UTC)

<p>Hey everyone!</p>
<p>I’m currently working on a project to prepare a dataset for a deep learning model. The main goal is to train a neural network to detect specific landmarks on 3D MRIs. I’m using Slicer 3D to create landmark annotations in a markup JSON format, and then I’m trying to write some Python code to read both the DICOM images and the annotations.</p>
<p>I’m using this MRI gallery as a test dataset: <a href="https://www.magnetomworld.siemens-healthineers.com/korean-dicom-image-gallery" rel="noopener nofollow ugc">https://www.magnetomworld.siemens-healthineers.com/korean-dicom-image-gallery</a></p>
<p>My process involves loading the DICOM series into a 3D NumPy array and then reading the landmark coordinates from the JSON file. The tricky part is transforming the patient-space coordinates from the JSON into the voxel-space of my NumPy array. I wrote some code/vibecode to handle this transformation using DICOM tags such as <strong><code>ImagePositionPatient</code></strong>, <strong><code>ImageOrientationPatient</code></strong>, and <strong><code>PixelSpacing</code></strong>. Then, I use <strong><code>pyvista</code></strong> to visualize the 3D volume and the landmarks to check if the conversion is correct.</p>
<p>Unfortunately, the algorithm I’ve created doesn’t seem to be placing the landmarks in the correct locations on the 3D image. The points are off, and I’m not sure if the issue lies in how I’m handling the DICOM metadata or if there’s a problem with my transformation matrix.</p>
<p>Has anyone dealt with this kind of coordinate conversion before? Any guidance or tips on where I might be going wrong would be greatly appreciated! I’m really excited about getting this dataset ready for training. Thanks a lot!</p>
<p>Below you will find my python code, and the obtained results.</p>
<pre><code class="lang-auto">import os
import glob
import json

import pydicom
import numpy as np
import pyvista as pv
from skimage import measure


def load_dicom_series(path):
    dicom_files = sorted(glob.glob(os.path.join(path, '*.dcm')), key=lambda x: int(pydicom.dcmread(x).InstanceNumber))
    datasets = [pydicom.dcmread(f) for f in dicom_files]

    if len (datasets) &gt; 1:
        volume = np.stack([ds.pixel_array for ds in datasets], axis=-1)
    else:
        volume = datasets[0].pixel_array
    return datasets, volume


def load_markups_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    points = np.array([cp['position'] for cp in data['markups'][0]['controlPoints']])
    return points


def get_value_tag(ds, tag):
    def has_shared(ds): return hasattr(ds, 'SharedFunctionalGroupsSequence')
    def has_perframe(ds): return hasattr(ds, 'PerFrameFunctionalGroupsSequence')

    if tag == 'PixelSpacing':
        if has_perframe(ds):
            return [float(ds.PerFrameFunctionalGroupsSequence[0].PixelMeasuresSequence[0].PixelSpacing[i]) for i in (0, 1)]
        if has_shared(ds):
            return [float(ds.SharedFunctionalGroupsSequence[0].PixelMeasuresSequence[0].PixelSpacing[i]) for i in (0, 1)]
        return [float(ds.PixelSpacing[i]) for i in (0, 1)]

    if tag == 'SliceThickness':
        if has_perframe(ds):
            return float(ds.PerFrameFunctionalGroupsSequence[0].PixelMeasuresSequence[0].SliceThickness)
        if has_shared(ds):
            return float(ds.SharedFunctionalGroupsSequence[0].PixelMeasuresSequence[0].SliceThickness)
        return float(ds.SliceThickness)

    if tag == 'ImageOrientationPatient':
        if has_perframe(ds):
            return np.array(ds.PerFrameFunctionalGroupsSequence[0].PlaneOrientationSequence[0].ImageOrientationPatient, float)
        if has_shared(ds):
            return np.array(ds.SharedFunctionalGroupsSequence[0].PlaneOrientationSequence[0].ImageOrientationPatient, float)
        return np.array(ds.ImageOrientationPatient, float)

    if tag == 'ImagePositionPatient':
        if has_perframe(ds):
            return np.array(ds.PerFrameFunctionalGroupsSequence[0].PlanePositionSequence[0].ImagePositionPatient, float)
        if has_shared(ds):
            return np.array(ds.SharedFunctionalGroupsSequence[0].PlanePositionSequence[0].ImagePositionPatient, float)
        return np.array(ds.ImagePositionPatient, float)


def get_dicom_metadata(dicom_datasets):
    if not dicom_datasets:
        return np.array([]), {}, np.identity(4)

    first_slice = dicom_datasets[0]

    # --- Sorting by InstanceNumber (fallback) ---
    if hasattr(first_slice, 'ImagePositionPatient'):
        dicom_datasets.sort(key=lambda s: float(get_value_tag(s, tag='ImagePositionPatient')[2]))
    else:
        dicom_datasets.sort(key=lambda s: int(s.InstanceNumber))

    # --- Extract metadata from first slice ---
    pixel_spacing = get_value_tag(first_slice, tag='PixelSpacing')
    slice_thickness = get_value_tag(first_slice, tag='SliceThickness')
    orientation = get_value_tag(first_slice, tag='ImageOrientationPatient')
    position = get_value_tag(first_slice, tag='ImagePositionPatient')

    # --- Compute normal ---
    row = orientation[:3]
    col = orientation[3:]
    normal = np.cross(row, col)
    normal = normal / np.linalg.norm(normal)

    print("normal:", normal)
    print("Sorting slices by ImagePositionPatient before sort", position)

    # --- Sort slices robustly along the normal ---
    dicom_datasets.sort(key=lambda s: np.dot(get_value_tag(s, tag='ImagePositionPatient'), normal))

    pixel_spacing = get_value_tag(dicom_datasets[0], tag='PixelSpacing')
    slice_thickness = get_value_tag(dicom_datasets[0], tag='SliceThickness')
    orientation = get_value_tag(dicom_datasets[0], tag='ImageOrientationPatient')
    position = get_value_tag(dicom_datasets[0], tag='ImagePositionPatient')  # update after sorting

    ipps = np.array([get_value_tag(d, tag='ImagePositionPatient') for d in dicom_datasets])

    print("Sorting slices by ImagePositionPatient after sort", position)

    distances = np.diff(ipps @ normal)
    print("Mean Δ along normal:", distances.mean())
    return pixel_spacing, slice_thickness, orientation, position


def get_dicom_transform(datasets):

    pixel_spacing, slice_thickness, orientation, position = get_dicom_metadata(datasets)
    
    print(f"Pixel Spacing: {pixel_spacing}")
    print(f"Slice Thickness (from tag): {slice_thickness}") # This is for info, we won't use it directly for spacing
    print(f"Position (First Slice): {position}")
    print(f"Orientation: {orientation}")

    # Get the ImagePositionPatient for all slices
    ipps = np.array([get_value_tag(d, 'ImagePositionPatient') for d in datasets])
    
    # Calculate the vector that defines the third axis (slice progression)
    # The most robust method is to use the difference between the positions
    # of the first and last slices and divide by the number of steps.
    # This handles cases where spacing might be slightly irregular.
    if len(ipps) &gt; 1:
        slice_vector = (ipps[-1] - ipps[0]) / (len(ipps) - 1)
    else:
        # Fallback for single-slice volume: use the cross product and SliceThickness
        row_vec_unscaled = orientation[:3]
        col_vec_unscaled = orientation[3:]
        slice_vector = np.cross(row_vec_unscaled, col_vec_unscaled) * slice_thickness
    print("Slice Vector (unit):", slice_vector)

    print(f"Calculated Slice Vector (Direction &amp; Spacing): {slice_vector}")
    
    # DICOM orientation: first 3 values = row direction, next 3 = column direction
    row_vec = orientation[:3]
    col_vec = orientation[3:]
    
    # Build the 4x4 transformation matrix
    transform = np.eye(4)
    
    # The first three columns are the basis vectors for the voxel grid (i, j, k)
    # scaled by the pixel/slice spacing.
    transform[:3, 0] = np.array(row_vec) * pixel_spacing[0]  # X-axis (Voxel i -&gt; Patient)
    transform[:3, 1] = np.array(col_vec) * pixel_spacing[1]  # Y-axis (Voxel j -&gt; Patient)
    transform[:3, 2] = slice_vector                          # Z-axis (Voxel k -&gt; Patient)
    
    # The fourth column is the origin of the voxel grid in patient coordinates
    # (the position of the center of the first voxel).
    transform[:3, 3] = position
    
    return transform


def patient_to_voxel_coords(points, transform):
    # Convert patient (LPS) coordinates to voxel indices
    inv_transform = np.linalg.inv(transform)
    points_h = np.hstack([points, np.ones((points.shape[0], 1))])
    voxel_coords = (inv_transform @ points_h.T).T[:, :3]
    voxel_coords = np.clip(voxel_coords, 0, np.inf)  # later clip to volume shape
    return voxel_coords


def read_plot_3d(dicom_dir, json_file=None):
    if not json_file:
        json_file = os.path.join(dicom_dir, 'OC_1.mrk.json')

    datasets, volume = load_dicom_series(dicom_dir)
    transform = get_dicom_transform(datasets)
    print("DICOM to Patient Transform:\n", transform)
    markup_points_patient = load_markups_json(json_file)
    print("Markup points (patient coords):", markup_points_patient)
    markup_points_voxel = patient_to_voxel_coords(markup_points_patient, transform)
    markup_points_voxel = np.round(markup_points_voxel).astype(float)
    print("Markup points (voxel coords):", markup_points_voxel)

    threshold = 30
    verts, faces, _, _ = measure.marching_cubes(volume, threshold)  # (y, x, z) order
    mesh_verts = verts.copy()
    mesh_verts[:, [0, 1]] = mesh_verts[:, [1, 0]]  # Swap y and x for PyVista
    pyvista_faces = np.c_[np.full(faces.shape[0], 3, dtype=np.int64), faces].flatten()
    mesh = pv.PolyData(mesh_verts, pyvista_faces)
    plotter = pv.Plotter(window_size=[600, 600])
    plotter.add_mesh(mesh, color='lightblue', opacity=1, show_edges=False)
    # Markup points: already in correct voxel coordinates
    points = pv.PolyData(markup_points_voxel)
    plotter.add_points(points, color='red', render_points_as_spheres=True, point_size=15, label='Markups')
    plotter.show_grid()
    plotter.show()

  
read_plot_3d('data/single_object_sample', 'data/single_object_sample/OC.mrk.json')
</code></pre>
<p>Markups in Slicer 3d<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddcd87e658b7bc7563abc945aab2b0c5f339e93c.jpeg" data-download-href="/uploads/short-url/vE9RRG2I28pkAzYEOsG8KZ22kB6.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddcd87e658b7bc7563abc945aab2b0c5f339e93c_2_434x500.jpeg" alt="Screenshot" data-base62-sha1="vE9RRG2I28pkAzYEOsG8KZ22kB6" width="434" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddcd87e658b7bc7563abc945aab2b0c5f339e93c_2_434x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddcd87e658b7bc7563abc945aab2b0c5f339e93c_2_651x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddcd87e658b7bc7563abc945aab2b0c5f339e93c_2_868x1000.jpeg 2x" data-dominant-color="333137"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1624×1870 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Attempt to recreate in python<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26e51c3ab1a2dabe8dec512e67e90404510e0d07.jpeg" data-download-href="/uploads/short-url/5y50DQYzxZ6mCYZfe9Q5OGiIYn5.jpeg?dl=1" title="Screenshot 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26e51c3ab1a2dabe8dec512e67e90404510e0d07_2_505x500.jpeg" alt="Screenshot 2" data-base62-sha1="5y50DQYzxZ6mCYZfe9Q5OGiIYn5" width="505" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26e51c3ab1a2dabe8dec512e67e90404510e0d07_2_505x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26e51c3ab1a2dabe8dec512e67e90404510e0d07_2_757x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26e51c3ab1a2dabe8dec512e67e90404510e0d07_2_1010x1000.jpeg 2x" data-dominant-color="E4E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2</span><span class="informations">1242×1228 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-09-05 18:12 UTC)

<p>I think you will have far less trouble if you use slicer to convert your landmark coordinates to IJK coordinates, which you can then use in your training module. here is an example by Copilot using MRHead as an example:</p>
<pre><code class="lang-auto">import numpy as np

# Get the volume node
volumeNode = getNode('MRHead')

# Define the RAS coordinates
ras_coords = [10.855, 41.146, 9.356, 1]  # Homogeneous coordinates (add 1)

# Get the RAS to IJK transformation matrix
ras_to_ijk_matrix = vtk.vtkMatrix4x4()
volumeNode.GetRASToIJKMatrix(ras_to_ijk_matrix)

# Convert to numpy array for easier manipulation
ras_to_ijk_np = np.array([[ras_to_ijk_matrix.GetElement(i, j) for j in range(4)] for i in range(4)])

# Multiply RAS coordinates by the transformation matrix
ijk_coords_homogeneous = ras_to_ijk_np @ ras_coords

# Extract IJK coordinates (drop the homogeneous component)
ijk_coords = ijk_coords_homogeneous[:3]

# Round to nearest integer voxel indices
ijk_coords_rounded = [int(round(c)) for c in ijk_coords]

print("IJK coordinates:", ijk_coords_rounded)

</code></pre>

---

## Post #3 by @nik_47 (2025-09-05 19:59 UTC)

<p>Thanks a lot for the suggestion! I used your approach and successfully got the IJK coordinates for my landmarks.</p>
<p>Here’s the interesting part: The IJK coordinates from your Slicer method are exactly the same as the ones my Python script calculates. This confirms that my coordinate transformation logic is correct.</p>
<p>While this works perfectly for the <code>MRHead</code> example, it still doesn’t correctly place the landmarks on the images from Siemens Healthineers gallery. I checked the coordinates for a point like the tip of the nose on <code>MRHead</code> ([2.661, 123.840, -39.934, 1]), and my script correctly plots it. Since my script’s IJK coordinates match Slicer’s, it seems the issue isn’t in my coordinate conversion logic itself.</p>
<p>This leads to a new question: Why does the method work for <code>MRHead</code> but not for the other DICOM images? Is there something fundamentally different about how the gallery images are structured? Or, if the IJK coordinates are correct, is it possible I need an additional transformation when plotting the points on the image itself? It feels like my script might not be capable of generalizing to all DICOM types. Any ideas on what we might be missing?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2e0037ec391653490d881865fbf072119a5e66f.jpeg" data-download-href="/uploads/short-url/wn1R208vvFzme6meIM3Wxllivr9.jpeg?dl=1" title="Screenshot 2025-09-05 at 22.57.58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2e0037ec391653490d881865fbf072119a5e66f_2_473x375.jpeg" alt="Screenshot 2025-09-05 at 22.57.58" data-base62-sha1="wn1R208vvFzme6meIM3Wxllivr9" width="473" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2e0037ec391653490d881865fbf072119a5e66f_2_473x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2e0037ec391653490d881865fbf072119a5e66f_2_709x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2e0037ec391653490d881865fbf072119a5e66f_2_946x750.jpeg 2x" data-dominant-color="979798"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-09-05 at 22.57.58</span><span class="informations">1920×1519 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca6289660c90ba23421b76e0e4a4996c856c597f.jpeg" data-download-href="/uploads/short-url/sSnyU2rygep9ll13I9UEZixidwb.jpeg?dl=1" title="Screenshot 2025-09-05 at 22.58.50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca6289660c90ba23421b76e0e4a4996c856c597f_2_371x500.jpeg" alt="Screenshot 2025-09-05 at 22.58.50" data-base62-sha1="sSnyU2rygep9ll13I9UEZixidwb" width="371" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca6289660c90ba23421b76e0e4a4996c856c597f_2_371x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca6289660c90ba23421b76e0e4a4996c856c597f_2_556x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca6289660c90ba23421b76e0e4a4996c856c597f_2_742x1000.jpeg 2x" data-dominant-color="DEE3E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-09-05 at 22.58.50</span><span class="informations">1522×2046 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
