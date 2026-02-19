---
topic_id: 41107
title: "How To Align Nifti Files With Original Dicom Files"
date: 2025-01-16
url: https://discourse.slicer.org/t/41107
---

# How to align NIfTI files with original DICOM files?

**Topic ID**: 41107
**Date**: 2025-01-16
**URL**: https://discourse.slicer.org/t/how-to-align-nifti-files-with-original-dicom-files/41107

---

## Post #1 by @oi_o (2025-01-16 02:17 UTC)

<p>I encountered an issue while trying to align NIfTI files (segmentation results from TotalSegmentator) with the original DICOM files in Jupyter Notebook. Despite my efforts to construct an appropriate affine matrix for the DICOM data, the axes do not align as expected.</p>
<p>Here’s the workflow I followed:</p>
<p><strong>I sorted the DICOM files based on InstanceNumber:</strong></p>
<pre><code class="lang-auto">dicom_files = sorted(
    [os.path.join(dcm_folder, f) for f in os.listdir(dcm_folder) if f.endswith('.dcm')],
    key=lambda x: pydicom.dcmread(x).InstanceNumber
)
</code></pre>
<p><strong>Using the DICOM metadata, I constructed an affine matrix:</strong></p>
<pre><code class="lang-auto">ds1 = pydicom.dcmread(dicom_files[0])
ds2 = pydicom.dcmread(dicom_files[1])

a = np.array(ds1.ImageOrientationPatient[:3])
b = np.array(ds1.ImageOrientationPatient[3:])
slice_diff = (np.array(ds1.ImagePositionPatient) - np.array(ds2.ImagePositionPatient)) / (
    ds1.InstanceNumber - ds2.InstanceNumber
)
c = slice_diff / np.sum(slice_diff**2) ** 0.5

matrix = np.zeros((4, 4))
matrix[3, 3] = 1
matrix[:3, 0] = b
matrix[:3, 1] = a
matrix[:3, 2] = c
affine_matrix = matrix
</code></pre>
<p><strong>I computed the transformation between the NIfTI and DICOM orientations using <code>nib.orientations.ornt_transform</code></strong></p>
<pre><code class="lang-auto">transform_ornt = nib.orientations.ornt_transform(start_ornt, end_ornt)
</code></pre>
<p><strong>I applied the computed transformation to the NIfTI data:</strong></p>
<pre><code class="lang-auto">reoriented_nifti = nib.orientations.apply_orientation(nii_data, transform_ornt)
</code></pre>
<p>Despite these steps, the alignment of the NIfTI and DICOM files is still incorrect. It seems like the axes are not properly aligned.</p>
<p><strong>What I tried:</strong></p>
<ul>
<li>I tested several cases with different orientations and found that axes could flip in all three directions under certain conditions.</li>
<li>When viewing the files in 3D Slicer or ITK-Snap, the alignment looks almost correct but has slight offsets.</li>
<li>I inspected the NIfTI transformation matrix in ITK-Snap (via Image Layer <code>Inspector -&gt; Info -&gt; Reorient -&gt; Voxel to World Matrix</code>) and found that the NIfTI affine matrix appears correct.</li>
<li>However, in the DICOM files, certain axes sometimes seem flipped.</li>
<li>I also tried simpleITK  <code>SetDirection</code> for aligning, but it seems not work.</li>
</ul>
<p><strong>My Questions:</strong></p>
<ul>
<li>Is there an issue with how I constructed the affine matrix for the DICOM files?</li>
<li>Should I handle the orientation of the DICOM files differently due to their non-fixed orientations?</li>
<li>Why does the NIfTI file display correctly in 3D Slicer/ITK-Snap but not when visualized in my Jupyter Notebook workflow?</li>
<li>Are there any known pitfalls in using nib.orientations.ornt_transform or apply_orientation that I might have overlooked?</li>
<li>What is the best way to ensure that the NIfTI and DICOM files align perfectly, considering the frequent axis flips in the DICOM files?</li>
</ul>
<p>Any insights, suggestions, or alternative workflows to address this alignment issue would be greatly appreciated. Thank you!</p>

---

## Post #2 by @oi_o (2025-01-16 02:29 UTC)

<p>I have resolved this issue. The primary cause lies in the difference between the coordinate systems used by DICOM and NIfTI files. Almost all DICOM systems are based on the <strong>LPS (Left-Posterior-Superior)</strong> coordinate system, whereas NIfTI files use the <strong>RAS (Right-Anterior-Superior)</strong> coordinate system. Therefore, a transformation between LPS and RAS coordinates is required to align the affine matrices correctly.</p>
<p>The code for generating the transform matrix between different coordinate system should be:</p>
<pre><code class="lang-auto">def generate_coordinate_matrix(coord_system):
    """
    Generate a transformation matrix from the given coordinate system
    to the world coordinate system.
    :param coord_system: String representing the coordinate system (e.g., 'LSP', 'RAS', etc.)
    :return: 4x4 transformation matrix
    """
    if len(coord_system) != 3:
        raise ValueError("Coordinate system must have exactly 3 characters (e.g., 'RAS', 'LSP').")
    
    # Mapping from coordinate labels to axis directions
    axis_mapping = {
        'R': [1, 0, 0],   # Right (positive X)
        'L': [-1, 0, 0],  # Left (negative X)
        'A': [0, 1, 0],   # Anterior (positive Y)
        'P': [0, -1, 0],  # Posterior (negative Y)
        'S': [0, 0, 1],   # Superior (positive Z)
        'I': [0, 0, -1]   # Inferior (negative Z)
    }

    # Extract the directions for X, Y, Z
    x_axis = axis_mapping[coord_system[0]]
    y_axis = axis_mapping[coord_system[1]]
    z_axis = axis_mapping[coord_system[2]]

    # Ensure the coordinate system is valid 
    if not np.isclose(np.dot(x_axis, y_axis), 0) or not np.isclose(np.dot(x_axis, z_axis), 0) or not np.isclose(np.dot(y_axis, z_axis), 0):
        raise ValueError(f"Invalid coordinate system: {coord_system}. Axes must be orthogonal.")
    
    # Create the transformation matrix
    transform_matrix = np.eye(4)
    transform_matrix[:3, 0] = x_axis  # X axis
    transform_matrix[:3, 1] = y_axis  # Y axis
    transform_matrix[:3, 2] = z_axis  # Z axis

    return transform_matrix

def calculate_transform_matrix(source_coord, target_coord):
    """
    Calculate the transformation matrix to convert coordinates
    from source_coord to target_coord.
    :param source_coord: Source coordinate system (e.g., 'LSP')
    :param target_coord: Target coordinate system (e.g., 'RAS')
    :return: 4x4 transformation matrix
    """
    # Generate matrices for both systems
    source_to_world = generate_coordinate_matrix(source_coord)
    target_to_world = generate_coordinate_matrix(target_coord)

    # Calculate the transform from source to target
    transform_matrix = np.linalg.inv(target_to_world) @ source_to_world
    return transform_matrix
</code></pre>
<p>Additionally, the third dimension in DICOM data requires special attention. Specifically, the direction vector for the slice axis may need a sign adjustment since the DICOM files are read in a sequential order. To ensure correctness, the DICOM files must be sorted by their <code>InstanceNumber</code>, and the slice spacing (position difference) between consecutive slices must be computed. Here’s the code snippet I used for this adjustment:</p>
<pre><code class="lang-auto">def compute_affine(dicom_files):
    dicom_files = sorted(dicom_files)
    
    ds = pydicom.dcmread(dicom_files[0])
    
    image_orientation = np.array(ds.ImageOrientationPatient) 
    #print(f'image_orientation: {image_orientation}')
    #print(f'image_position: {ds.ImagePositionPatient}')
    row_cosine = image_orientation[3:]
    col_cosine = image_orientation[:3]
    #col_cosine = image_orientation[:3]
    #row_cosine = image_orientation[3:]
    pixel_spacing = np.array(ds.PixelSpacing) 
    
    first_position = np.array(ds.ImagePositionPatient)  
    
    if len(dicom_files) &gt; 1:
        ds_next = pydicom.dcmread(dicom_files[1])
        second_position = np.array(ds_next.ImagePositionPatient)
        #print(f'first_instance_number: {ds.InstanceNumber}')
        #print(f'second_instance_number: {ds_next.InstanceNumber}')

        #print(f'first_position: {first_position}')
        #print(f'second_position: {second_position}')
        
        slice_direction = second_position - first_position
        #print(f'slice_direction before: {slice_direction}')
        slice_spacing = np.linalg.norm(slice_direction)
        slice_cosine = slice_direction / slice_spacing

    else:
        slice_cosine = np.cross(col_cosine,row_cosine)
        slice_spacing = 1.0
    
    #print(f'slice_spacing: {slice_spacing}')

    affine = np.eye(4)
    affine[:3, 0] = row_cosine * pixel_spacing[0]
    affine[:3, 1] = col_cosine * pixel_spacing[1]
    affine[:3, 2] = slice_cosine * slice_spacing* np.sign(ds_next.InstanceNumber-ds.InstanceNumber)
    affine[:3, 3] = first_position
    return affine
</code></pre>
<p>This code can return the correct Dicom affine matrix to <strong>LPS</strong>.</p>
<p>Another challenge was the discrepancy in orientation flipping when importing DICOM and NIfTI files directly into visualization tools like ITK-Snap and 3D Slicer. ITK-Snap sometimes displays incorrect flips for orientation, while 3D Slicer can accurately represent the directions. This inconsistency contributed to my confusion during the alignment process.</p>
<p>With these issues now resolved, the alignment works as expected. For additional reference, you can check out the code and workflow I used <a href="https://github.com/lzhang30/aligning_nifti2dicom_python" rel="noopener nofollow ugc">here</a>. If you notice any inaccuracies in my approach or suggestions for further improvements, I’d be glad to hear your thoughts.</p>

---

## Post #3 by @lassoan (2025-01-16 02:39 UTC)

<p>There are many equivalent, valid ways to reconstruct a 3D volume from a set of slices. For example, you are free to choose any corner of the voxel array as origin of the voxel coordinate system.</p>
<p>This is not a problem at all, as long as all the voxels are in correct location in physical coordinate system and you use imaging software that work in physical space, such as ITK or MONAI.</p>
<p>Some libraries (such as numpy and many scipy functions, and maybe your own code that you develop) ignore the image geometry (origin, spacing, axis directions). You can still use these libraries for image processing, but you may need to manually resample the input images before and after processing. Typically you need to resample all input images to make them have the same image geometry.  You may also need to resample them to have isotropic spacing. You can do this resampling in your own application (using ITK, MONAI, etc) or you can resample in Slicer by specifying a reference volume when you export the segmentation.</p>

---

## Post #4 by @oi_o (2025-01-16 03:26 UTC)

<p>Thank you for your detailed explanation. I realize that my misunderstanding stemmed from assuming that the coordinate systems of DICOM files and NIfTI files were identical, which led to the issue I encountered. My objective is to read segmentation data from a NIfTI file, slice it in the order of the DICOM slices, and save the results as PNG files. To achieve this, manualing alignment of the coordinate systems is necessary.</p>
<p>I appreciate your clarification regarding the importance of aligning the coordinate systems properly. I will explore suitable libraries, such as ITK or MONAI for the next steps in my work. Thank you again for your guidance.</p>

---

## Post #5 by @lassoan (2025-01-20 04:49 UTC)

<p>In general, once you reconstructed a 3D volume from a DICOM series, it does not matter how the data was organized in the source files. Your algorithm should work for a 3D volume that was put together from axial slices just as well as on a volume that consisted of sagittal slices.</p>
<p>It can be somewhat informative to show to the user the original slice orientation when reviewing the results (especially to radiologists who are the most comfortable when they look at native slices). But even then, it is useful to also show reformatted slices and 3D views as well. So, usually you can just work in 3D and let the user look at any views he is interested in.</p>

---
