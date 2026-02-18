# Generate NRRD header from DICOM header

**Topic ID**: 33453
**Date**: 2023-12-19
**URL**: https://discourse.slicer.org/t/generate-nrrd-header-from-dicom-header/33453

---

## Post #1 by @Lin_Li (2023-12-19 03:22 UTC)

<p>I already read .npy file from a LPS coordinate system DICOM folder and generate a .npy mask. When I want to generate the .nrrd header from the DICOM header, and I got confused about the results.</p>
<p>For the dicom header, I read:<br>
(0018, 0050) Slice Thickness                     DS: ‘1.1000000238419’<br>
(0028, 0030) Pixel Spacing                       DS: [0.80357140302658, 0.80357140302658]<br>
(0020, 0032) Image Position (Patient)            DS: [-191.80030483817, -176.12590213898, 86.606538507263]<br>
(0020, 0037) Image Orientation (Patient)         DS: [0.9993283937409, -2.051034E-10, 0.036643709737, 2.049657E-10, 1, 7.5158E-12]</p>
<p>To generate space directions in NRRD, I generate the z space directions by cross product, with the reference of <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" rel="noopener nofollow ugc">Slicer Coordinate System</a>.</p>
<p>origin = dicom_data.ImagePositionPatient<br>
x_spacing, y_spacing = dicom_data.PixelSpacing<br>
z_spacing = dicom_data.SliceThickness</p>
<p>direction_x = np.array(dicom_data.ImageOrientationPatient[:3])<br>
direction_y = np.array(dicom_data.ImageOrientationPatient[3:])<br>
direction_z = np.cross(direction_x, direction_y)</p>
<p>space_direction_x = direction_x * x_spacing<br>
space_direction_y = direction_y * y_spacing<br>
space_direction_z = direction_z * z_spacing<br>
space_directions = np.stack((space_direction_x, space_direction_y, space_direction_z)).tolist()</p>
<p>The generated space_directions is:<br>
array([[ 9.99328394e-01, -2.05103400e-10,  3.66437097e-02],<br>
[ 2.04965700e-10,  1.00000000e+00,  7.51580000e-12],<br>
[-4.03080807e-02, -5.35973205e-17,  1.09926123e+00]])</p>
<p>Looks like the z spacing is positive. But the second slice is DICOM folder has smaller z origin value. Is that possible? Actually I tried to manually draw a segmentation in Slicer and Slicer generate the same NRRD header with same Spacing Directions. And the segmentation I generated can be properly showed in Slicer.</p>
<p>So I’m wondering why the DICOM z spacing (space directions[2][2]) is positive but the second slice origin is smaller than the first slice? And is my code generating NRRD header from LPS DICOM can be applied to all situations? Thanks.</p>

---
