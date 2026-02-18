# Loosing 4th dimension after segmentation 

**Topic ID**: 29881
**Date**: 2023-06-06
**URL**: https://discourse.slicer.org/t/loosing-4th-dimension-after-segmentation/29881

---

## Post #1 by @chopraamhk (2023-06-06 23:06 UTC)

<p>Hi,</p>
<p>My original nifti file is having 4dimensions , i.e., ( 196, 240, 100, 1). I have done segmentation in 3d slicer using 2 labels, and after saving the segmented file, it is giving me output as 3d. My new dimensions are (196, 240, 100) but my time dimension has vanished. I have used reference volume option as while before exporting but it didnt give me my output. I would request you to help.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2023-06-06 23:15 UTC)

<p>NIFTI file format is causing lot of trouble, as its specification contains lots of unnecesary complexity (redundancies and ambiguities). Therefore we are not keen on spending time with it, which means nobody ventured to implement support for 4D NIFTI files (except for displacement fields). Therefore, if you export a segmentation into NIFTI format from Slicer, the output will always be a 3D file.</p>
<p>One possible solution is to write the segmentation to NRRD file format and then read it and then write in NIFTI format. You can implement this in a few lines in Python using pynrrd and nibabel packages.</p>
<p>If your input NIFTI file has size of (196, 240, 100, 1) then it means that it is actually a 3D image. Why is it important to save as a 4D image if the 4th dimension is singular?</p>

---

## Post #3 by @chopraamhk (2023-06-08 12:17 UTC)

<p>Thank you for your reply. I have converted my dicom images initially to nifti using dcm2niix. Later, I am doing segmentation and doing it manually using 3d slicer. I need time information because I am using a python code which checks the quality of Nifti files with respect to time and, later, calculates the area. Either i am not doing segmentation properly or I need to follow some other approach to convert 1. dicom to nifti and, later, 2. nifti to segmented nifti.</p>
<p>For now, i will convert my dicom to nrrd file (as you suggested) and later, will convert it to nifti and try it in different cases. I will check if it gives me time information as well.  (My dicom images does have time information)</p>

---

## Post #4 by @chopraamhk (2023-06-12 14:10 UTC)

<p>my converted 100 dicom images to nifti has header -</p>
<p>sizeof_hdr      : 348<br>
data_type       : b’’<br>
db_name         : b’’<br>
extents         : 0<br>
session_error   : 0<br>
regular         : b’r’<br>
dim_info        : 57<br>
dim             : [  4 240 196   1 100   1   1   1]<br>
intent_p1       : 0.0<br>
intent_p2       : 0.0<br>
intent_p3       : 0.0<br>
intent_code     : none<br>
datatype        : int16<br>
bitpix          : 16<br>
slice_start     : 0<br>
pixdim          : [-1.         1.5833334  1.5833334  6.         0.028      0.<br>
0.         0.       ]<br>
vox_offset      : 0.0<br>
scl_slope       : nan<br>
scl_inter       : nan<br>
slice_end       : 0<br>
slice_code      : unknown<br>
xyzt_units      : 10<br>
cal_max         : 0.0<br>
cal_min         : 0.0<br>
slice_duration  : 0.0<br>
toffset         : 0.0<br>
glmax           : 0<br>
glmin           : 0<br>
descrip         : b’TE=1.2;Time=103829.298;phase=1’<br>
aux_file        : b’RR 872 +/- 61; 9 heartb’<br>
qform_code      : scanner<br>
sform_code      : scanner<br>
quatern_b       : 0.0<br>
quatern_c       : 1.0<br>
quatern_d       : 0.0<br>
qoffset_x       : 191.80186<br>
qoffset_y       : -134.34802<br>
qoffset_z       : 43.5763<br>
srow_x          : [ -1.5833334   0.         -0.        191.80186  ]<br>
srow_y          : [  -0.           1.5833334   -0.        -134.34802  ]<br>
srow_z          : [ 0.      0.      6.     43.5763]<br>
intent_name     : b’’<br>
magic           : b’n+1’</p>
<p>whereas my segmentation file doesn’t have time stamp<br>
sizeof_hdr      : 348<br>
data_type       : b’’<br>
db_name         : b’’<br>
extents         : 0<br>
session_error   : 0<br>
regular         : b’r’<br>
dim_info        : 0<br>
dim             : [  4 240 196   1 100   1   1   1]<br>
intent_p1       : 0.0<br>
intent_p2       : 0.0<br>
intent_p3       : 0.0<br>
intent_code     : none<br>
datatype        : uint16<br>
bitpix          : 16<br>
slice_start     : 0<br>
pixdim          : [-1.         1.5833334  1.5833334  6.         0.028      0.<br>
0.         0.       ]<br>
vox_offset      : 0.0<br>
scl_slope       : nan<br>
scl_inter       : nan<br>
slice_end       : 0<br>
slice_code      : unknown<br>
xyzt_units      : 2<br>
cal_max         : 0.0<br>
cal_min         : 0.0<br>
slice_duration  : 0.0<br>
toffset         : 0.0<br>
glmax           : 0<br>
glmin           : 0<br>
descrip         : b’’<br>
aux_file        : b’’<br>
qform_code      : scanner<br>
sform_code      : scanner<br>
quatern_b       : -0.0<br>
quatern_c       : 1.0<br>
quatern_d       : 0.0<br>
qoffset_x       : 191.80186<br>
qoffset_y       : -134.34802<br>
qoffset_z       : 43.5763<br>
srow_x          : [ -1.5833334  -0.          0.        191.80186  ]<br>
srow_y          : [  -0.           1.5833334   -0.        -134.34802  ]<br>
srow_z          : [ 0.      0.      6.     43.5763]<br>
intent_name     : b’’<br>
magic           : b’n+1’</p>
<p>Could you please suggest me how can i get the time stamp and i believe i am loosing some other informattion here as well…</p>

---

## Post #5 by @chopraamhk (2023-06-12 14:13 UTC)

<p>and by converting dicom to nrrd :</p>
<p>OrderedDict([(‘type’, ‘unsigned short’), (‘dimension’, 3), (‘space’, ‘left-posterior-superior’), (‘sizes’, array([240, 196, 100])), (‘space directions’, array([[1.58333337, 0.        , 0.        ],<br>
[0.        , 1.58333337, 0.        ],<br>
[0.        , 0.        , 1.        ]])), (‘kinds’, [‘domain’, ‘domain’, ‘domain’]), (‘endian’, ‘little’), (‘encoding’, ‘gzip’), (‘space origin’, array([-191.80186367, -174.40197062,   43.57630157]))])</p>
<p>i am not getting the required information.</p>

---
