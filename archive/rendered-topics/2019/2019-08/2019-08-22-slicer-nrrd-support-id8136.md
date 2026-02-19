---
topic_id: 8136
title: "Slicer Nrrd Support"
date: 2019-08-22
url: https://discourse.slicer.org/t/8136
---

# Slicer NRRD support

**Topic ID**: 8136
**Date**: 2019-08-22
**URL**: https://discourse.slicer.org/t/slicer-nrrd-support/8136

---

## Post #1 by @Chris_Rorden (2019-08-22 22:26 UTC)

<p>I am having trouble loading some NRRD files into slicer. Here is a <a href="https://drive.google.com/open?id=1bhsCIHqGYm4DXXpHMQAu5fh1GeORoX7U" rel="noopener nofollow ugc">link</a> to three images: ok.nhdr loads fine, ok2.nii.gz loads fine, bad.nhdr does not load in Slicer 4.10.2 on MacOS. All of these images load fine in MRIcroGL and ImageJ.</p>
<p>The Slicer error log reports:</p>
<blockquote>
<p>UpdateFromFile: Unsupported number of components (only 1 allowed): 2</p>
<p>ReadData: Cannot read file as a volume of type DiffusionTensorVolume[fullName = /Users/chris/Desktop/bad.nhdr]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 1 files.<br>
File reader used the archetype file name of /Users/chris/Desktop/bad.nhdr [reader 0th file name = /Users/chris/Desktop/bad.nhdr]<br>
FileFormatError</p>
<p>ReadData: MRMLVolumeNode does not match file kind</p>
<p>ReadData: Failed to instantiate a file reader</p>
<p>ReadData: Cannot read file as a volume of type Volume[fullName = /Users/chris/Desktop/bad.nhdr]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 1 files.<br>
File reader used the archetype file name of /Users/chris/Desktop/bad.nhdr [reader 0th file name = /Users/chris/Desktop/bad.nhdr]<br>
FileFormatError</p>
</blockquote>

---

## Post #2 by @lassoan (2019-08-23 04:04 UTC)

<p>It seems that the volume has 2 components. Slicer core can load single-component volumes as scalar, 3-component volumes as RGB, 9-component volumes as tensor. You can load 2-component volume as a volume sequence: install Sequences extension and in “Add data” dialog choose “Volume sequence” in Description column.</p>

---

## Post #3 by @Chris_Rorden (2019-08-23 12:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> you are correct. Slicer does not load 2-volume NRRD files, though it can load 2-volume NIfTI files. I can understand this for tools that use a photometric interpretation for data - e.g. if there is only one component treat it as scalar grayscale, if there are two component generate and error, if there are three component treat it as Red/Green/Blue. However, it does not make sense when each channel is treated as a scalar volume - which is how Slicer treats 1 volume and 3 volume NRRDs. I do think the current behavior will frustrate users, and the error message does not do a good job of clarifying the solution.</p>
<p>Here is a <a href="https://drive.google.com/file/d/1VUeZ5vHjJJp7XLE63NJX1PZ7aaJ6WSeK/view?usp=sharing" rel="nofollow noopener">link</a> to the same volume saved as NIfTI (.hdr/.img) and NRRD (.nhdr/.img; note image files are shared by both NIfTI and NRRD so literally identical data), with separate images storing 1, 2 or 3 volumes. As you predicted, slicer loads all NIfTI images correctly but fails for the two volume NRRD.</p>

---

## Post #4 by @pieper (2019-08-23 13:01 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> what’s the use case for a 2 component nrrd?  Is it a time series or something else?  How would you expect it to load?</p>

---

## Post #5 by @Chris_Rorden (2019-08-23 14:54 UTC)

<p>It should be treated just like the 1 and 3 volume NRRD files in slicer: as a scalar image (in this case with two volumes), and the same as the 2 volume NIfTI. At the moment, dragging and dropping a multi-volume NIfTI or NRRD just displays the <a href="https://discourse.slicer.org/t/how-to-load-4d-images-in-slicer-fmri-or-asl-datasets/1157">first volume </a> of the series, but it seems odd that a 2-volume NRRD is treated differently than the 1 and 3-volume files. Ideally, it would be great if all the volumes are loaded and the user could choose which volume is displayed, just like ImageJ, FSLeyes and MRIcroGL. Rapidly cycling through raw DWI and fMRI volumes is useful for detecting head movements, reconstructor errors, etc.</p>
<p>Here is a <a href="https://discourse.slicer.org/t/how-to-load-4d-images-in-slicer-fmri-or-asl-datasets/1157">link</a> to minimal dataset of 1/2/3 volume image in NRRD and NHDR.</p>

---

## Post #6 by @lassoan (2019-08-23 16:00 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="5" data-topic="8136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>it seems odd that a 2-volume NRRD is treated differently than the 1 and 3-volume files</p>
</blockquote>
</aside>
<p>I guess the reason is that some file formats don’t give a clue how to interpret dimensions (for example, .mhd) and so ITK and/or Slicer was not prepared to use descriptions in file formats that do specify dimensions. This could be improved for sure, probably by promoting Volume Sequences a bit more. We plan to bundle Sequences in default Slicer installations in Slicer5 and we could probably load non-scalar/RGB/tensor volumes as volume sequences.</p>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="5" data-topic="8136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>Ideally, it would be great if all the volumes are loaded and the user could choose which volume is displayed, just like ImageJ, FSLeyes and MRIcroGL. Rapidly cycling through raw DWI and fMRI volumes is useful for detecting head movements, reconstructor errors, etc.</p>
</blockquote>
</aside>
<p>I think this is all available if you load the file as a volume sequence. You can go prev/next frame, play/pause using toolbar buttons or pressing <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Left arrow</kbd>/<kbd>Right arrow</kbd>. You can browse multiple sequences separately or in sync, perform motion compensation (using Sequence Registration), etc.</p>

---

## Post #7 by @Chris_Rorden (2019-08-23 18:14 UTC)

<p>Perhaps ITK and Slicer could be enhanced to leverage the <a href="http://teem.sourceforge.net/nrrd/format.html#kinds" rel="nofollow noopener">kinds</a> field.</p>
<p>As an aside, dcm2niix always converts DICOM to NRRD <code>kinds: space space space list</code>, but perhaps it should be enhanced so that <code>list</code> is used for DWI data and <code>time</code> is used for ASL, fMRI, etc. This would hint that one could interpolate volumes along time, where this would not be appropriate for sequentially stored DWI directions. Perhaps <a class="mention" href="/u/tbillah">@tbillah</a> could comment on this proposal.</p>

---

## Post #8 by @lassoan (2019-08-23 18:44 UTC)

<p>Sequences extension uses <code>kinds</code> field, too, but always writes “list” for the vector dimension (and uses <code>labels</code> and <code>units</code> fields to store actual name and unit of the dimension), as we did not want to deviate from what ITK and most other packages do. If tools start to use <code>kinds</code> field properly then we can update Slicer to do the same.</p>

---

## Post #9 by @pieper (2019-08-23 20:29 UTC)

<p>I agree with the goal of improving the semantics of the files so that software can automatically do something more useful.  There are definitely cases in the Slicer (and ITK) codebase where some kind of heuristic is the only option.</p>
<p>Using the <code>kinds</code> field in nrrd is good and it would be great to see it respected more broadly.</p>
<p>On the other extreme we (as in me, <a class="mention" href="/u/fedorov">@fedorov</a>, etc)  are also continuing to work on encoding complex data types in dicom to be even more explicit about the meanings.  For example, <a>parametric maps</a> can explicitly encode the values at each pixel, but also the quantity measured and the units in which it is measured.  They can also include references to the data from which they were derived in addition to the usual patient/study metadata.</p>

---

## Post #10 by @fedorov (2019-08-26 15:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="8136" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems that the volume has 2 components. Slicer core can load single-component volumes as scalar, 3-component volumes as RGB, 9-component volumes as tensor. You can load 2-component volume as a volume sequence: install Sequences extension and in “Add data” dialog choose “Volume sequence” in Description column.</p>
</blockquote>
</aside>
<p>Slicer can also load NRRD with any number of components, including 2, as a multivolume, but the header must match the (un-documented) expectations of the multivolume reader. It is mostly intended to read back multivolumes saved by Slicer.</p>

---

## Post #11 by @Chris_Rorden (2019-08-26 16:52 UTC)

<p><a href="/u/fedorov">fedorov</a> cans you provide a sample header with these undocumented features or briefly discuss them. That way I could update dcm2niix to support this. Below is the current NRRD header created for a <a href="https://github.com/neurolabusc/dcm_qa/tree/master/In/Orientation/ax/axasc35" rel="nofollow noopener">simple DICOM 2-volume dataset</a>.</p>
<pre><code>NRRD0005
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
# dcm2niix v1.0.20190808 NRRD export transforms by Tashrif Billah
type: int16
dimension: 4
space: right-anterior-superior
sizes: 64 64 35 2
thicknesses:  NaN  NaN 3 NaN
endian: little
encoding: gzip
data file: 2vol_ax_asc_35sl_20140310133834_6.raw.gz
space units: "mm" "mm" "mm"
space origin: (104,-58.6843,-84.798)
space directions: (-3.25,3.25e-16,0) (3.25e-16,3.23099,0.350998) (-3.88798e-17,-0.388798,3.57894) none
centerings: cell cell cell ???
kinds: space space space list
DICOM_0008_0060_Modality:=MR
DICOM_0008_0070_Manufacturer:=SIEMENS
DICOM_0008_1090_ManufacturerModelName:=TrioTim
DICOM_0018_0022_ScanOptions:=FS
DICOM_0018_0023_MRAcquisitionType:=2D
DICOM_0018_0080_RepetitionTime:=3000
DICOM_0018_0081_EchoTime:=30
DICOM_0018_0083_NumberOfAverages:=1
DICOM_0018_0087_MagneticFieldStrength:=3
DICOM_0018_1020_SoftwareVersions:=syngo_MR_B17
DICOM_0018_1314_FlipAngle:=76</code></pre>

---

## Post #12 by @lassoan (2019-08-26 17:15 UTC)

<p>Slicer should not require custom tags to read a 4D volume, so I would not recommend to modify dcm2niix.</p>
<p>The plan is that Sequences will replace multivolume infrastructure in Slicer but it will require at least several months to bring Sequences into Slicer core. If we need an solution sooner then we can remove the special tag requirements in multivolume importer.</p>

---

## Post #13 by @fedorov (2019-08-27 00:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="8136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer should not require custom tags to read a 4D volume, so I would not recommend to modify dcm2niix.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I don’t know what you mean by the first part (those custom tags describe semantics of the volume, and replicate some of the attributes from the DICOM header - I am not sure there is a “standard” NRRD or NIfTI way to do this, since dcm2niix saves some of those into a separate JSON file for BIDS), but I agree it is not a good idea to modify dcm2niix to write custom attributes that are only readable by the multivolume reader in Slicer.</p>

---

## Post #14 by @lassoan (2019-08-27 01:13 UTC)

<p>There are standard fields for axis kind, measurement unit, etc., so multi-volume modules should not <em>require</em> presence of any custom fields to load a 4D volume as multi-volume node.</p>
<p>I agree that additional custom fields would be useful (e.g., to store frame time vector) and agreeing in a standard list of fields between dcm2niix and Slicer could simplify DICOM import. However, I’m not sure how to implement this. Should this be a small private business between dcm2niix and Slicer (and hope that others will follow) or we should try to involve medical image computing and scipy community? There are many people who would be interested in consolidation in file formats and tools (see for example <a href="https://discourse.itk.org/t/images-in-physical-space-in-python/2124/25" rel="nofollow noopener">this</a> discussion and <a href="https://discourse.itk.org/t/add-a-parallel-compression-method-to-nrrd-and-or-metaimage/696/28" rel="nofollow noopener">this</a>), but nobody has promised to allocate resources or offer to write a grant application.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a>, can improving research file formats and tools be part of your NCI Imaging Data Commons project, or it can only use DICOM?</p>

---

## Post #15 by @fedorov (2019-08-28 01:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="8136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a>, can improving research file formats and tools be part of your NCI Imaging Data Commons project, or it can only use DICOM?</p>
</blockquote>
</aside>
<p>No, this is not in the scope. We may need to revisit it, who knows, but at least our declared plan is to use DICOM for all data, both images and image-derived.</p>

---

## Post #16 by @fedorov (2019-08-29 16:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="8136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There are standard fields for axis kind, measurement unit, etc., so multi-volume modules should not <em>require</em> presence of any custom fields to load a 4D volume as multi-volume node.</p>
</blockquote>
</aside>
<p>Note that multivolumes, as produced by the multivolume plugin, will often have irregular spacing in the 4th dimension (e.g., for various types of MR acquisitions). Is that something that is supported by NRRD?</p>

---

## Post #17 by @lassoan (2019-09-01 03:23 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="16" data-topic="8136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Note that multivolumes, as produced by the multivolume plugin, will often have irregular spacing in the 4th dimension (e.g., for various types of MR acquisitions). Is that something that is supported by NRRD?</p>
</blockquote>
</aside>
<p>Sadly, nrrd cannot store variable spaced data along any dimension in a standard way. You can have origin and spacing (start time and time between frames) but not arbitrary value for each frame.</p>
<p>Regardless, we should still be able to read/write nrrd files that does not have custom timestamps. If custom timestamps are found in a field then we could use those.</p>
<p>Nifti seems to have some <a href="https://nipy.org/nibabel/reference/nibabel.nifti1.html#nibabel.nifti1.Nifti1Header.get_slice_times">slice_times</a> field, but I’m not sure how standard it is.</p>

---

## Post #18 by @Chris_Rorden (2019-09-01 11:54 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> the NIfTI format was designed for MRI scans prior to the advent of multi-band. It describes the relative timing of the 2D slices that are stacked to form a 4D volume.</p>
<ul>
<li>The timing between volumes is always fixed (TR = pixdim[4]). This makes sense for MRI, as variable TR impacts the image contrast. However, I think <a class="mention" href="/u/fedorov">@fedorov</a> would like to describe variable times between volumes for the CT modality. This is a useful feature, but not supported by NIfTI.</li>
<li>The NIfTI format only describes ascending, descending, odd-first interleaved and even-first interleaved patterns of 2D slices. This is sufficient to allow slice time correction for single-band MRI. However, it can not describe multi-band sequences, e.g. with a 32-slice volume and MB=4, a total of 8 readouts are performed each with 4 aliased slices (though one could argue that MB allows very short TRs, so the slice-timing error is very small allowing the temporal derivative to soak up variability and allowing one to ignore slice time correction).</li>
<li>Tools like dcm2niix can create a <a href="https://bids.neuroimaging.io/bids_spec.pdf" rel="nofollow noopener">BIDS format</a> JSON text file with the <code>SliceTiming</code> tag that independently does describe the time of each slice in a volume. Therefore, this can describe multi band. However, it still does not provide a mechanism to describe variable time between the 3D volumes that compose a 4D series.</li>
</ul>
<p>Since the NIfTI format can not support variable timing between volumes, perhaps NRRD could be formally extended. It appears the Slicer has informally introduced the <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/MultiVolumeExplorer" rel="nofollow noopener">NRRD tag MultiVolume.FrameLabels</a>: <code>MultiVolume.FrameLabels:=0.0,4270.0,8541.0,12812.0,...</code>. If some scheme like this could be adopted as part of the NRRD specification, it could solve <a class="mention" href="/u/fedorov">@fedorov</a>’s issue (though I realize he is also advocating that DICOM might be a flexible format to handle this situation).</p>
<p>By the way, the full description of NIfTI slice timing support is <a href="https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h" rel="nofollow noopener">embedded in the NIfTI header</a>:</p>
<pre><code>slice_duration = If this is positive, AND if slice_dim is nonzero,
                 indicates the amount of time used to acquire 1 slice.
                 slice_duration*dim[slice_dim] can be less than pixdim[4]
                 with a clustered acquisition method, for example.

slice_code = If this is nonzero, AND if slice_dim is nonzero, AND
             if slice_duration is positive, indicates the timing
             pattern of the slice acquisition.  The following codes
             are defined:
               NIFTI_SLICE_SEQ_INC  == sequential increasing
               NIFTI_SLICE_SEQ_DEC  == sequential decreasing
               NIFTI_SLICE_ALT_INC  == alternating increasing
               NIFTI_SLICE_ALT_DEC  == alternating decreasing
               NIFTI_SLICE_ALT_INC2 == alternating increasing #2
               NIFTI_SLICE_ALT_DEC2 == alternating decreasing #2
{ slice_start } = Indicates the start and end of the slice acquisition
{ slice_end   } = pattern, when slice_code is nonzero.  These values
                are present to allow for the possible addition of
                "padded" slices at either end of the volume, which
                don't fit into the slice timing pattern.  If there
                are no padding slices, then slice_start=0 and
                slice_end=dim[slice_dim]-1 are the correct values.
                For these values to be meaningful, slice_start must
                be non-negative and slice_end must be greater than
                slice_start.  Otherwise, they should be ignored.
</code></pre>
<p>Personally, I think different formats fill different niches: NIfTI/NRRD are very simple and fast to parse. They lend themselves to datascientists and developers who want to tools that can quickly read and write tools with simple I/O. The DICOM format is very flexible, but extremely complex, compounded by the fact that different vendors have interpreted the standard differently. Ideally, it would be great if the DICOM standard could describe a “core” usage, similar to how one can use the legacy OpenGL or the streamlined “ES” and “Core” specifications. Since the “Core” features are a subset of the full specification, systems would be backward compatible. However, new enhanced files that followed the core pattern would be much faster to parse (in particular if group lengths were mandatory). Until such a time, DICOM is extremely flexible but unwieldy for many projects. While I respect <a class="mention" href="/u/fedorov">@Fedorov</a> and David Clunie’s <a href="http://qiicr.org/dicom4miccai/dicom4miccai2017.html" rel="nofollow noopener">feeling that DICOM should be THE medical imaging format</a>, I think the success of NIfTI and NRRD reflect a Darwinian selection. Different species have developed that are each adapted to their niche. If we really want to see wider adoption of DICOM in tools, we need to explore how DICOM can evolve to succeed in more environments (simplified core specification, core validator, etc.).</p>

---

## Post #19 by @fedorov (2019-09-02 16:45 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="18" data-topic="8136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>The timing between volumes is always fixed (TR = pixdim[4]). This makes sense for MRI, as variable TR impacts the image contrast. However, I think <a class="mention" href="/u/fedorov">@fedorov</a> would like to describe variable times between volumes for the CT modality. This is a useful feature, but not supported by NIfTI.</p>
</blockquote>
</aside>
<p>The motivation for multi-volume was actually just various flavors of MRI in the context of prostate imaging. DCE timing interval is fixed, but other applications for prostate imaging include various T1- and T2-mapping sequences (variable FA or TR), and DW trace images with unequally spaced b-values (e.g., see <a href="https://www.ncbi.nlm.nih.gov/pubmed/28718517" class="inline-onebox">Evaluation of fitting models for prostate tissue characterization using extended-range b-factor diffusion-weighted imaging - PubMed</a>). In multivolumes, from the start, the forth dimension was not intended to always correspond to time.</p>
<aside class="quote no-group quote-modified" data-username="Chris_Rorden" data-post="18" data-topic="8136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>The DICOM format is very flexible, but extremely complex, compounded by the fact that different vendors have interpreted the standard differently.<br>
[…]<br>
I think the success of NIfTI and NRRD reflect a Darwinian selection. Different species have developed that are each adapted to their niche.</p>
</blockquote>
</aside>
<p>I agree with many points, but I think once you want to step out of the boundaries defined by those formats, and introduce extra complexity, in particular - handling metadata (like the issue we are discussing here), the answer is not trivial. I am not aware of examples that use NRRD or NIfTI (or BIDS, for that matter) for large-scale data aggregation and metadata management.</p>
<p>The question becomes do we want to invest the time to further extend those formats, or explore how those situations can be handled in DICOM. Yes, vendors have different implementations and interpretations of DICOM, but why not try to establish best practices and open source DICOM conversion tools that we can iteratively refine? We have just a handful of established tools that normalize vendor-specific DICOM and output NRRD/NIfTI - why not explore how those tools can output multiframe DICOM in addition to the research format they output right now?</p>
<p>I agree at this point it is hard to make the case for using DICOM to solve this specific problem, since there are no converters that could “just do it”. But I would much rather explore how this problem can be solved using DICOM. And if we have more people who believe this approach is worth the time investment, we would much sooner be able to decide how suitable multiframe DICOM is for those tasks, how much effort it will take to implement it, and how to proceed with refining the standard along the lines you mentioned, Chris.</p>

---

## Post #20 by @Chris_Rorden (2019-09-02 18:28 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> I agree on all points. Tools that convert vendor-specific DICOMs to general NIfTI/NRRD could easily be adapted to generate a clean and simple DICOM. However, I think this effort would work best if there was a clear idea of what that flavor of DICOM would look like. People like you and David Clunie seem well positioned to do this. A clean specification and validation tool would allow developers of different tools to tune their conversions.</p>

---

## Post #21 by @lassoan (2019-09-02 20:40 UTC)

<p>If we defined nrrd metadata fields properly then we would end up with something very similar to the DICOM standard. So, it would make a lot of sense to avoid duplication of work and make DICOM standard usable instead.</p>
<p>The only fundamental problem I see is that DICOM only makes sense in the medical domain. We cannot collaborate on file IO libraries, plugins, or tools with the scientific computing community if we use DICOM. A hybrid approach like storing DICOM metadata in a generic file format could allow using DICOM while leveraging work of a much larger community. The generic file format could be nrrd or anything else that the majority of the scientific computing community widely uses and flexible enough to store DICOM metadata.</p>

---

## Post #22 by @fedorov (2019-09-02 20:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="8136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The only fundamental problem I see is that DICOM only makes sense in the medical domain. We cannot collaborate on file IO libraries, plugins, or tools with the scientific computing community if we use DICOM.</p>
</blockquote>
</aside>
<p>Can you elaborate on this point? What makes DICOM fundamentally not suitable for scientific computing community? I agree there are many issues with DICOM, but I don’t understand what makes it conceptually unfit.</p>

---

## Post #23 by @lassoan (2019-09-03 02:34 UTC)

<p>If you look at DICOM as a general-purpose data storage format, it is quite arbitrary and unnecessarily complex compared to what it offers.</p>
<p>Just one example. Have a look at the list of <a href="http://dicom.nema.org/medical/dicom/current/output/html/part05.html#sect_6.2" rel="nofollow noopener">value representations</a>:</p>
<ul>
<li>Time representations (Age String, Date, Date Time, Time): both range and resolution makes them inadequate for general usage.</li>
<li>String value representations (Long Text, Short Text, Unlimited Characters, Unlimited Text, Person Name): they are very similar, with some minor difference in limitations (length, allowed characters, etc). This complicates implementation, while not providing much in return. Having Person Name defined at this abstraction level is very arbitrary.</li>
<li>Numerical value representations: seemingly random selection of representations.</li>
</ul>
<p><a href="https://support.hdfgroup.org/HDF5/doc1.6/Datatypes.html" rel="nofollow noopener">HDF5</a> data representation model is similarly rich/complicated but it is consistently low-level and provides extremely high performance. NRRD does not provide much, but it is very simple, so it is very easy to implement.</p>

---

## Post #24 by @fedorov (2019-09-05 02:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="23" data-topic="8136">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you look at DICOM as a general-purpose data storage format, it is quite arbitrary and unnecessarily complex compared to what it offers</p>
</blockquote>
</aside>
<p>Speaking for myself, I find it impossible to grasp all the capabilities (especially, intended, but not adopted) of the standard and implications of various decisions made in the process of developing the DICOM standard. It is so broad, that very few have a complete picture, and probably no one has the context for why all the various, and often seemingly strange (if not wrong!) decisions were made.</p>
<p>I am afraid that any effort similar in scope started today (if successful in attracting attention from a diverse community of stakeholders with conflicting motivations and agendas and establishing as broad deployment base as DICOM) stands a pretty high chance of being judged in a similar fashion as above 30 years from now.</p>
<p>I agree that DICOM has not been designed as a general-purpose data storage format for the scientific community, and that it looks arbitrary and unnecessarily complex. But I hope and believe it can be more useful to the scientific community than it is now.</p>
<p>Sorry for the distraction from the topic of this conversation.</p>

---

## Post #25 by @lassoan (2019-09-05 16:31 UTC)

<p>I agree that it would be harder to get anything much better than DICOM for <em>clinical use</em> and relevant parts could be even useful for generic scientific computing.</p>
<p>The main problem is with DICOM’s file format. The file format is not designed to be optimal for anything, it just started as dumping DICOM network data stream to file - and remained just that. See comment in <a href="http://www.jpathinformatics.org/temp/JPatholInform10112-4386571_121105.pdf" rel="nofollow noopener">David Clunie’s recent paper</a>: <em>“There was no “file format” defined perse, although it had already become common practice to persist network data sets on disk.”</em>.</p>
<p>That’s why I think a hybrid approach - storing DICOM metadata in powerful general-purpose containers - could work well. It would make DICOM more widely accessible. We would only need to choose a suitable container (NRRD, HDF5, …?) and standardize the way how DICOM information is embedded.</p>
<p>David Clunie had similar conclusion in his paper, too, by proposing usage of “dual‑personality DICOM-TIFF files”. The only aspect I’m not convinced is that it is necessary to create files that are binary compatible with both DICOM and TIFF standards at the same time.</p>

---
