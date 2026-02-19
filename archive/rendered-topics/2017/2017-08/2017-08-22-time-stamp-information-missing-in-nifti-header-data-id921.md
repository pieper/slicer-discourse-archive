---
topic_id: 921
title: "Time Stamp Information Missing In Nifti Header Data"
date: 2017-08-22
url: https://discourse.slicer.org/t/921
---

# Time Stamp information missing in NifTI header data

**Topic ID**: 921
**Date**: 2017-08-22
**URL**: https://discourse.slicer.org/t/time-stamp-information-missing-in-nifti-header-data/921

---

## Post #1 by @Diana_Anthony (2017-08-22 20:15 UTC)

<p>Operating system: Windows 10, 64 bit<br>
Slicer version: 3D Slicer 4.6.2</p>
<p>I am working with Philips cardiac ultrasound scans and would like to gain information about interesting slices from using their .nii header and reading this information using MATLAB. For the most part, I have what I need, except any information about time stamps.</p>
<p>Here is a sample of what the header looks like from the .nii file I save from Slicer.</p>
<pre><code class="lang-auto">           SizeofHdr: 348
            DataType: 2
              DbName: '                  '
             Extents: 0
        SessionError: 0
             Regular: 'r'
             DimInfo: ' '
          Dimensions: [240 176 208 1 1 1 1]
         headerbswap: 0
            IntentP1: 0
            IntentP2: 0
            IntentP3: 0
          IntentCode: 0
         datatypestr: 'UNKNOWN'
            bitvoxel: 0
         DataTypeStr: 'UINT8'
            BitVoxel: 8
              Bitpix: 8
          SliceStart: 0
     PixelDimensions: [7×1 double]
           VoxOffset: 352
        RescaleSlope: 1
    RescaleIntercept: 0
            SliceEnd: 0
           SliceCode: ' '
           XyztUnits: 2
       xyzt_unitsstr: 'UNKNOWN'
        XyztUnitsStr: 'MM'
              CalMax: 0
              CalMin: 0
      Slice_duration: 0
             Toffset: 0
               Glmax: 0
               Glmin: 0
             Descrip: '                                                                                '
             AuxFile: '                        '
           QformCode: 2
           SformCode: 1
            QuaternB: 0
            QuaternC: 0
            QuaternD: 0
            QoffsetX: 0
            QoffsetY: 0
            QoffsetZ: 0
               SrowX: [4×1 double]
               SrowY: [4×1 double]
               SrowZ: [4×1 double]
          IntentName: '                '
               Magic: 'n+1 '
</code></pre>
<p>It seems like a lot of information is missing, or perhaps I am not exporting the right file from Slicer or not reading this data correctly, is there any way from Slicer to get time information from the slices for a cardiac cycle?</p>
<p>Thanks for any help!</p>

---

## Post #2 by @lassoan (2017-08-22 21:23 UTC)

<p>How did you create the .nii file from the ultrasound scans?</p>

---

## Post #3 by @Diana_Anthony (2017-08-23 07:18 UTC)

<p>I loaded the dicom Philips file and used the patcher to convert to an<br>
.nrrd, opened that file as a Volume Sequence, and then saved individual<br>
frames as .nii files.</p>

---

## Post #4 by @lassoan (2017-08-23 15:44 UTC)

<p>Nifty file format is most commonly used for neuro imaging and not particularly well suited for 4D data. I would recommend to load the 4D nrrd file directly into Matlab: it is easier to handle a single file and also you have access to metadata, such as frame rate. You can use the nrrd file reader/writer available in Slicer MatlabBridge: <a href="https://subversion.assembla.com/svn/slicerrt/trunk/MatlabBridge/src/MatlabCommander/commandserver/">https://subversion.assembla.com/svn/slicerrt/trunk/MatlabBridge/src/MatlabCommander/commandserver/</a></p>

---

## Post #5 by @fedorov (2017-08-23 19:04 UTC)

<p>As aside, apparently, it is not uncommon in the neuro community to use nifti for 4d data, and there is a special clause in the nifti standard about describing the 4th dimension. To support the users, in general, it would be nice to be able to load that kind of data. Someone asked me a while ago to add support of this type of data to MultiVolumeImporter, but I never made time to work on it…</p>

---

## Post #6 by @lassoan (2017-08-23 21:09 UTC)

<p>NRRD has a nice framework for specifying higher-dimensionality data - not just 4D, so for example it can store time sequence of RGB color or tensor volumes. It can store what kind of axes you have (time, space, etc), there are also a number of per-axis metadata fields, etc. all part of the standard for many years. It’s not perfect (for example, it would be great to have sparse/non-uniform axes), but it is quite flexible and generic.</p>
<p>My impression with nifti is that the format is still plagued with image orientation inconsistencies. I would just let the neuroimaging community to figure this out, standardize their tools, make higher-dimensional data support properly part of nifti (not just a special clause, not just 4D), etc. and re-evaluate the situation in a few years.</p>
<p>I agree that for neuro applications it would be nice to support 4D nifti (and we should implement it at some point), but for other/general use, such as 4D ultrasound, NRRD should work just as well, or better.</p>

---

## Post #7 by @lassoan (2017-08-23 21:31 UTC)

<p><a class="mention" href="/u/diana_anthony">@Diana_Anthony</a>, to answer In the saved .nrrd file you have these fields:</p>
<pre>
labels: "time" "" "" ""
units: "s" "" "" "" 
axis 0 index type:=numeric
axis 0 index values:=0.000 0.142 0.284 0.426 0.568 0.710 0.852 0.994 1.136 1.278 1.420 1.562 1.704 
</pre>
<p>The <code>axis 0 index values</code> field contains timestamp for each frame, in seconds.</p>

---
