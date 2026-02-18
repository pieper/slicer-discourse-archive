# E: PatientName (0010,0010) violates VR definition in PatientModule but actual value is correct

**Topic ID**: 3737
**Date**: 2018-08-12
**URL**: https://discourse.slicer.org/t/e-patientname-0010-0010-violates-vr-definition-in-patientmodule-but-actual-value-is-correct/3737

---

## Post #1 by @jcfr (2018-08-12 07:57 UTC)

<p>The discussion below initially took place here: <a href="https://github.com/QIICR/dcmqi/issues/348">https://github.com/QIICR/dcmqi/issues/348</a>.</p>
<p><i>From <span class="mention">@mmromero</span> on Tue Aug 07 2018 13:03:44 GMT+0000 (UTC)</i><br><br>Dear developers,</p>
<p>I am trying to create the structure report of a white matter hyper-intensity lesion segmentation with your docker container but no matter the Patient’s Name I always get the same error (see below). The actual value is “N2D_PATIENT”, but also tried with “xxx xxx” with the same result.</p>
<p>I can share the data with you, just let me know if you need it and I upload it.</p>
<p>Thank you very much.<br>
Miguel.</p>
<pre><code class="lang-auto">docker run -v /Users/miguel/Workspace/RAPIDS/SR/dcmqi_test:/tmp/dcmqi qiicr/dcmqi itkimage2segimage --inputDICOMDirectory /tmp/dcmqi/input_data --inputMetadata /tmp/dcmqi/wmh_segmentation.json --inputImageList /tmp/dcmqi/output_nifti/18991230_000000nifti2dicom044s001a001.nii.gz --outputDICOM /tmp/dcmqi/wmh_segmentation.dcm
dcmqi repository URL: git@github.com:QIICR/dcmqi.git revision: 72869c3 tag: latest-2-g72869c3
Searching recursively /tmp/dcmqi/input_data for DICOM files
Input image size: [240, 240, 48]
W: PatientName (0010,0010) violates VR definition in PatientModule
W: PatientSex (0010,0040) violates VR definition in PatientModule
W: AccessionNumber (0008,0050) violates VR definition in GeneralStudyModule
W: InstitutionName (0008,0080) violates VR definition in GeneralEquipmentModule
W: PatientAge (0010,1010) violates VR definition in PatientStudyModule
W: PositionReferenceIndicator (0020,1040) absent in FrameOfReferenceModule (type 2)
Directions: 0.997303 -0.0502721 -0.0534678
-0.0229997 -0.905936 0.422789
0.0696929 0.42042 0.904649

Processing input label Image (0x1889550)
  RTTI typeinfo:   itk::Image&lt;short, 3u&gt;
  Reference Count: 3
  Modified Time: 184
  Debug: Off
  Object Name: 
  Observers: 
    none
  Source: (none)
  Source output name: (none)
  Release Data: Off
  Data Released: False
  Global Release Data: Off
  PipelineMTime: 48
  UpdateMTime: 183
  RealTimeStamp: 0 seconds 
  LargestPossibleRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [240, 240, 48]
  BufferedRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [240, 240, 48]
  RequestedRegion: 
    Dimension: 3
    Index: [0, 0, 0]
    Size: [240, 240, 48]
  Spacing: [0.958333, 0.958333, 3]
  Origin: [-107.096, 80.3152, -82.9768]
  Direction: 
0.997303 -0.0502721 -0.0534678
-0.0229997 -0.905936 0.422789
0.0696929 0.42042 0.904649

  IndexToPointMatrix: 
0.955749 -0.0481774 -0.160403
-0.0220414 -0.868189 1.26837
0.066789 0.402902 2.71395

  PointToIndexMatrix: 
1.04066 -0.0239997 0.072723
-0.0524578 -0.945325 0.438699
-0.0178226 0.14093 0.30155

  Inverse Direction: 
0.997303 -0.0229997 0.0696929
-0.0502721 -0.905936 0.42042
-0.0534678 0.422789 0.904649

  PixelContainer: 
    ImportImageContainer (0x1884ec0)
      RTTI typeinfo:   itk::ImportImageContainer&lt;unsigned long, short&gt;
      Reference Count: 1
      Modified Time: 180
      Debug: Off
      Object Name: 
      Observers: 
        none
      Pointer: 0x7f569bb8a010
      Container manages memory: true
      Size: 2764800
      Capacity: 2764800

Found 2 label(s)
Skipping label 0
Processing label 1
Total non-empty slices that will be encoded in SEG for label 1 is 48
 (inclusive from 0 to 48)
E: PatientName (0010,0010) violates VR definition in PatientModule
FATAL ERROR: Writing of the SEG dataset failed! Please report the problem to the developers, ideally accompanied by a de-identified dataset allowing to reproduce the problem!
```&lt;br /&gt;&lt;br /&gt;&lt;i&gt;Copied from original issue: https://github.com/QIICR/dcmqi/issues/348&lt;/i&gt;</code></pre>

---

## Post #2 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/pieper">@pieper</a> on Tue Aug 07 2018 14:02:38 GMT+0000 (UTC)</i><br><br>Hi <span class="mention">@mmromero</span> -</p>
<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>
<p>I’d try encoding the PatientName as a PN (person name) VR according to the standard:</p>
<p><a>ftp://dicom.nema.org/MEDICAL/Dicom/current/output/chtml/part05/sect_6.2.html</a></p>
<p>If it’s still not working, can you post your wmh_segmentation.json file?</p>
<p>-Steve</p>

---

## Post #3 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <span class="mention">@mmromero</span> on Tue Aug 07 2018 14:08:53 GMT+0000 (UTC)</i><br><br>Dear Steve,</p>
<p>Thank you for the quick answer, I checked the VR PN format but I didn’t see how a name of one word without special characters couldn’t match it. I will check again, just to be sure.</p>
<p>I am running a test of dcmqi, for that I used the following wmh_segmentation.json:</p>
<pre><code class="lang-auto">{
  "ContentCreatorName": "Miguel",
  "ClinicalTrialSeriesID": "Session1",
  "ClinicalTrialTimePointID": "1",
  "SeriesDescription": "WMH Segmentation",
  "SeriesNumber": "300",
  "InstanceNumber": "1",
  "BodyPartExamined": "Brain",
  "segmentAttributes": [
    [
      {
        "labelID": 1,
        "SegmentDescription": "WMH",
        "SegmentAlgorithmType": "AUTOMATIC",
        "SegmentAlgorithmName": "IBBM Algorithm",
        "AnatomicRegionSequence": {
          "CodeValue": "T-A0100",
          "CodingSchemeDesignator": "SRT",
          "CodeMeaning": "Brain"
        },
        "SegmentedPropertyCategoryCodeSequence": {
          "CodeValue": "T-D0050",
          "CodingSchemeDesignator": "SRT",
          "CodeMeaning": "Tissue"
        },
        "recommendedDisplayRGBValue": [
          237,
          5,
          5
        ],
        "SegmentedPropertyTypeCodeSequence": {
          "CodeValue": "T-D0050",
          "CodingSchemeDesignator": "SRT",
          "CodeMeaning": "Tissue"
        }
      }
    ]
  ],
  "ContentLabel": "SEGMENTATION",
  "ContentDescription": "Image segmentation",
  "ClinicalTrialCoordinatingCenterName": "dcmqi"
}
</code></pre>
<p>Thank you,<br>
Miguel.</p>

---

## Post #4 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/pieper">@pieper</a> on Tue Aug 07 2018 14:59:08 GMT+0000 (UTC)</i><br><br>First glance that looks okay - I guess if you post the full dataset to dropbox or similar we could have a closer look (assuming no identifying patient info of course).</p>

---

## Post #5 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <span class="mention">@mmromero</span> on Tue Aug 07 2018 15:38:46 GMT+0000 (UTC)</i><br><br>Sure, you can download it from here: <a href="https://gigamove.rz.rwth-aachen.de/d/id/KfEouv7ymsysW9">https://gigamove.rz.rwth-aachen.de/d/id/KfEouv7ymsysW9</a></p>

---

## Post #6 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/fedorov">@fedorov</a> on Tue Aug 07 2018 15:53:55 GMT+0000 (UTC)</i><br><br>dciodvfy reports a number of errors for that dataset, I wonder if this causes the conversion problem too. Looks like you created that series with ITK, is this correct? If yes, what version did you use?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14525a3045e75f2676d45f139fb194994ca62dba.png" data-download-href="/uploads/short-url/2TLZhos8CMiIcO7s52bgT85Lbku.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14525a3045e75f2676d45f139fb194994ca62dba.png" alt="image" data-base62-sha1="2TLZhos8CMiIcO7s52bgT85Lbku" width="690" height="327" data-dominant-color="1E1F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">949×450 89.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <span class="mention">@mmromero</span> on Tue Aug 07 2018 16:01:22 GMT+0000 (UTC)</i><br><br>Hi <a class="mention" href="/u/fedorov">@fedorov</a>. I created the dicoms from a nifti file using the <a href="http://www.bio.dist.unige.it/projects/national/n2d">nifti2dicom</a> tool as follows:</p>
<pre><code class="lang-auto">nifti2dicom_macos_0.4.3-0r1 -i INPUT -o OUTPUT --studyid rapidstest --studyinstanceuid 1.2.826.0.1.3680043.2.1143.9925161747653993333667655489998915347 --patientage 33 --patientsex M --patientweight 85 --patientdob 19841101 --studydate 20180516 --seriesnumber 1 -a 1
</code></pre>
<p>The ITK version is 4.8.2.</p>
<p>If you think this is the problem I will populate all the fields with my values instead of using the default ones. The problem is that I only have the niftis for these data and I need to use the dicoms.</p>
<p>Thank you very much.</p>

---

## Post #8 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/fedorov">@fedorov</a> on Tue Aug 07 2018 16:16:46 GMT+0000 (UTC)</i><br><br>Interesting. I have not seen that tool before, and indeed it is a good question - what tool we could recommend to create a DICOM image series from non-DICOM image … I don’t have a ready answer!</p>
<p>I am not sure it will help if you just not use the default values. It looks like it might be writing trailing characters that are not consistent with the standard, and I do not know how to confirm or fix this. I would need to dig into the standard more to see if I can figure it out. But if the issue is in your converter, I can’t think of an alternative to suggest! … <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #9 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/pieper">@pieper</a> on Tue Aug 07 2018 16:48:30 GMT+0000 (UTC)</i><br><br>Of course you can use Slicer to convert your files to dicom - either with a<br>
command line module (that you could script) or with the GUI.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/CreateDICOMSeries" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/CreateDICOMSeries</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export</a></p>
<p>On Tue, Aug 7, 2018 at 12:16 PM, Andrey Fedorov <a href="mailto:notifications@github.com">notifications@github.com</a><br>
wrote:</p>
<blockquote>
<p>Interesting. I have not seen that tool before, and indeed it is a good<br>
question - what tool we could recommend to create DICOM from non-DICOM …<br>
I don’t have a ready answer!</p>
<p>I am not sure it will help if you just not use the default values. It<br>
looks like it might be writing trailing characters that are not consistent<br>
with the standard, and I do not know how to confirm or fix this. I would<br>
need to dig into the standard more to see if I can figure it out. But if<br>
the issue is in your converter, I can’t think of an alternative to suggest!<br>
… <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>—<br>
You are receiving this because you commented.<br>
Reply to this email directly, view it on GitHub<br>
<a href="https://github.com/QIICR/dcmqi/issues/348#issuecomment-411114675">https://github.com/QIICR/dcmqi/issues/348#issuecomment-411114675</a>, or mute<br>
the thread<br>
<a href="https://github.com/notifications/unsubscribe-auth/AAHsfUlhDpqvyfHDsErRSG6xq8o2ABVAks5uOb1vgaJpZM4VyHiq">https://github.com/notifications/unsubscribe-auth/AAHsfUlhDpqvyfHDsErRSG6xq8o2ABVAks5uOb1vgaJpZM4VyHiq</a><br>
.</p>
</blockquote>

---

## Post #10 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/fedorov">@fedorov</a> on Tue Aug 07 2018 16:54:18 GMT+0000 (UTC)</i><br><br>&gt; you can use Slicer to convert your files to dicom</p>
<p>… but that will mean the output will always be CT, and you cannot import metadata from another DICOM object as the tool you mentioned advertises it can do.</p>

---

## Post #11 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/pieper">@pieper</a> on Tue Aug 07 2018 17:01:29 GMT+0000 (UTC)</i><br><br>Actually I think if you imported the other data and then put your volume in the subject hiearchy node with the imported data then the exported data dicom files would inherit the study information.</p>
<p>The point about the exported dicom having a CT modality is valid - that’s been a ‘feature’ of the CreateDICOMSeries module since the beginning but if that’s the only objection and there’s no other good tool, then making the modality into a command line argument would be a simple fix.</p>
<p>Perhaps <a class="mention" href="/u/cpinter">@cpinter</a> or <a class="mention" href="/u/lassoan">@lassoan</a> have other suggestions?</p>

---

## Post #12 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/fedorov">@fedorov</a> on Tue Aug 07 2018 17:03:45 GMT+0000 (UTC)</i><br><br>&gt; making the modality into a command line argument would be a simple fix</p>
<p>I don’t think it would be that simple. The tool would need to know what attributes are required by individual IODs, and be able to import those from the input reference instances. I think implementing that in a meaningful way will require a non-trivial effort.</p>
<p>Do we know of any other tool that can take a non-DICOM image and make a DICOM out of it?</p>

---

## Post #13 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/pieper">@pieper</a> on Tue Aug 07 2018 17:07:38 GMT+0000 (UTC)</i><br><br>That’s my point - of course it’s complicated to make everything perfect, but if all you need to do is help people in <span class="mention">@mmromero</span>’s situation then there may not be any better tool.  Plus improving the DICOM export from Slicer, even if imperfect, might still be useful.</p>
<p>Of course the other way to do it is to just write a program that generates the DICOM you wanted - e.g. with dcmtk, pydicom, or other method.</p>

---

## Post #14 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/fedorov">@fedorov</a> on Tue Aug 07 2018 17:30:24 GMT+0000 (UTC)</i><br><br>Yes, I completely agree. I am just wondering if there is another ready-to-go tool that could help here.</p>

---

## Post #15 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/pieper">@pieper</a> on Tue Aug 07 2018 17:46:48 GMT+0000 (UTC)</i><br><br>Depending on how much data there is to convert and how variable it is, one brute force method is to use dcmdump and dump2dcm along with a script that slices up the volumes and does string replaces on the dump file.  Not elegant but at least you know that if you start with a valid file of the type you are trying to create you will have the right dicom tags.  This is not an elegant approach but it may be easier than learning how to do the same thing in dcmtk.</p>

---

## Post #16 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/lassoan">@lassoan</a> on Tue Aug 07 2018 18:58:44 GMT+0000 (UTC)</i><br><br>You can specify any modality when you export an image from Slicer. In the DICOM export dialog, change <em>Modality</em> tag in <em>Edit DICOM tags</em> section.</p>
<p>In Data module, create subject and study, drag-and-drop the series (volume node) under the study, and right-click on the series to export it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2424445fa484efee4f5ae754b232b89e4f8cc852.png" data-download-href="/uploads/short-url/59ITeg2umEcfIcjHbMJYqk9HYhc.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2424445fa484efee4f5ae754b232b89e4f8cc852_2_313x500.png" alt="image" data-base62-sha1="59ITeg2umEcfIcjHbMJYqk9HYhc" width="313" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2424445fa484efee4f5ae754b232b89e4f8cc852_2_313x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2424445fa484efee4f5ae754b232b89e4f8cc852_2_469x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2424445fa484efee4f5ae754b232b89e4f8cc852.png 2x" data-dominant-color="EBF0F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">568×907 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The DICOM export dialog is opened where several fields can be modified and then exported to DICOM file:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc25ae190c0bd944a90ed0925496d63d29edc9a4.png" data-download-href="/uploads/short-url/vpvLUagVj86mwE2PAIq2RE9zmU4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc25ae190c0bd944a90ed0925496d63d29edc9a4_2_657x500.png" alt="image" data-base62-sha1="vpvLUagVj86mwE2PAIq2RE9zmU4" width="657" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc25ae190c0bd944a90ed0925496d63d29edc9a4_2_657x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc25ae190c0bd944a90ed0925496d63d29edc9a4_2_985x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc25ae190c0bd944a90ed0925496d63d29edc9a4_2_1314x1000.png 2x" data-dominant-color="F4F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1322×1006 34.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can use dcmodify to change individual tags in a DICOM file, but it is not very convenient, because it is a command-line tool and you also need to write a short script that iterates through all files of a series to change modality of a volume.</p>

---

## Post #17 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <span class="mention">@mmromero</span> on Wed Aug 08 2018 10:38:57 GMT+0000 (UTC)</i><br><br>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>, exporting dicoms from Slicer works. I managed to generate the segmentation report. Also <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/fedorov">@fedorov</a>, thank you for quick answer and support.</p>

---

## Post #18 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/pieper">@pieper</a> on Wed Aug 08 2018 12:14:14 GMT+0000 (UTC)</i><br><br>Thanks <span class="mention">@mmromero</span> for reporting and following up!</p>

---

## Post #19 by @jcfr (2018-08-12 07:57 UTC)

<p><i>From <a class="mention" href="/u/fedorov">@fedorov</a> on Wed Aug 08 2018 15:57:07 GMT+0000 (UTC)</i><br><br><a class="mention" href="/u/lassoan">@lassoan</a> thank you for the details!</p>
<p><span class="mention">@mmromero</span> glad the issue is resolved for you, and thank you for pointing us to the other tool you used. I was not aware of it.</p>
<p>If/when I figure out what was the issue with the output it produces, I will see if I can make a PR to fix the issue, since that tool looks more comprehensive than Slicer in customizing the output, and can be used in batch mode, which makes it unique - I don’t know of something comparable. Meanwhile, I took note of the issue in <a href="https://github.com/biolab-unige/nifti2dicom/issues/33">https://github.com/biolab-unige/nifti2dicom/issues/33</a>.</p>

---

## Post #20 by @jcfr (2018-08-12 07:58 UTC)

<p><i>From <a class="mention" href="/u/lassoan">@lassoan</a> on Wed Aug 08 2018 21:49:08 GMT+0000 (UTC)</i><br><br>You can use all Slicer features in batch mode, without GUI. If you ever need help in figuring out how to access a particular feature then ask on the Slicer forum.</p>
<p>“nifti2dicom” has a very narrow scope - it can only export a single 3D image volume. DICOM storage is much more than this. You may need to export segmentation objects, RT structure sets, registration objects, structured reports, complete studies with references between series, etc. Slicer can all do all this, using an extensible, plugin-based DICOM export infrastructure. It’s far from perfect, but it’s being continuously improved.</p>

---

## Post #21 by @jcfr (2018-08-12 07:58 UTC)

<p><i>From <a class="mention" href="/u/pieper">@pieper</a> on Wed Aug 08 2018 22:03:18 GMT+0000 (UTC)</i><br><br>Andrey and I did this script to go from dicom to nrrd - it could definitely be generalize.  Maybe we want to add some example going to dicom for various common types.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/QIICR/dcmheat/blob/master/docker/SlicerConvert.py" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/dcmheat/blob/master/docker/SlicerConvert.py" target="_blank">QIICR/dcmheat/blob/master/docker/SlicerConvert.py</a></h4>
<pre><code class="lang-py">import os
import sys

def setDICOMReaderApproach(approach):
    import DICOMScalarVolumePlugin
    approaches = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass.readerApproaches()
    if approach not in approaches:
        raise ValueError("Unknown dicom approach: %s\nValid options are: %s" % (approach, approaches))
    approachIndex = approaches.index(approach)
    settings = qt.QSettings()
    settings.setValue('DICOM/ScalarVolume/ReaderApproach', approachIndex)


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--dcmtk", help="use dcmtk to parse dicom (exclusive with --gdcm)", action="store_true")
parser.add_argument("--gdcm", help="use dcmtk to parse dicom (exclusive with --dcmtk)", action="store_true")
parser.add_argument("--no-quit", help="For debugging, don't exit Slicer after converting", action="store_true")
parser.add_argument("--input", help="Input DICOM directory")
parser.add_argument("--output", help="Output directory")
</code></pre>

  This file has been truncated. <a href="https://github.com/QIICR/dcmheat/blob/master/docker/SlicerConvert.py" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #22 by @jcfr (2018-08-12 07:58 UTC)

<p><i>From <a class="mention" href="/u/fedorov">@fedorov</a> on Wed Aug 08 2018 22:06:27 GMT+0000 (UTC)</i><br><br>Andras, I agree with you, but scripting Slicer functionality in python, and running the result in batch mode has a very big startup overhead, and is associated with other inconveniences, such as tricks that need to be done for headless mode, large package size, platform-specific launcher issues. It might be a lot more convenient for users to use command line tools that are designed for the specific task (when they are available!) instead of learning how to write Slicer scripts, and then figuring other issues.</p>
<p>I am all for Slicer, as you know, but for example using Slicer for batch conversion of DICOM from command line is extremely slow and not convenient, so for that task I would rather use plastimatch, dcm2niix, or dicom2nifti, which are all maintained, and do the job well and much more efficiently.</p>
<p>In this particular case, indeed, if nifti2dicom is not supported (there has not been much activity, and I am not sure about the quality of the code), Slicer might be the only option.</p>

---

## Post #23 by @jcfr (2018-08-12 07:58 UTC)

<p><i>From <a class="mention" href="/u/lassoan">@lassoan</a> on Wed Aug 08 2018 23:10:16 GMT+0000 (UTC)</i><br><br>I believe that having so many simple, rigid, single-purpose dicomToX tools is bad, because these tools hide issues (by making random assumptions and ignore various potential problems) and cause fragmentation in the research community. It would be better to establish one common DICOM import/export tool framework that many people can use, customize, and extend.</p>
<p>I agree with your list of limitations above (although maybe the recently completed PythonSlicer interpreter solved some of these issues). This common DICOM converter framework does not have to be Slicer-based. However, it should be general, customizable, and extensible, similarly to Slicer’s DICOM import/export infrastructure.</p>

---

## Post #24 by @jcfr (2018-08-12 07:58 UTC)

<p><i>From <a class="mention" href="/u/pieper">@pieper</a> on Wed Aug 08 2018 23:18:16 GMT+0000 (UTC)</i><br><br>It would be great to factor out the code in slicer so that it could be used in other scenarios in addition to the slicer gui.  We already do this for things like the diffusion plugin that uses DWIConvert under the hood or QuantitativeReporting that uses dcmqi.</p>
<p>Regarding your other points Andrey, while they are generally true I don’t see things like package size or startup time as limiting factors.  Converting files like this is not a real time activity and if you have a large number of dicom files to convert slicer is the least of your disk space concerns.   No reason to prematurely optimize something like this.</p>

---

## Post #25 by @jcfr (2018-08-12 07:58 UTC)

<p><i>From <a class="mention" href="/u/jcfr">@jcfr</a> on Wed Aug 08 2018 23:18:50 GMT+0000 (UTC)</i><br><br>&gt; , and running the result in batch mode has a very big startup overhead,</p>
<p>We need to address this.  (the first step was to lazily load CLIs which was implemented before 4.8.1, now when a specific module is request for batch processing, we need to improve the dependency management and load only the needed dependencies)</p>
<blockquote>
<p>and is associated with other inconveniences, such as tricks that need to be done for headless mode,</p>
</blockquote>
<p>That is currently a problem indeed.</p>
<ul>
<li>for VTK rendering, compiling with mesa offscreen rendering backend would help. Ideally, this should be dynamic and not a compile option.</li>
<li>for Qt GUI … this is definitively more tricky was a lot of module do not cleanly separate Widget from logic.</li>
</ul>
<p>Now, I think that putting effort into having a well maintained docker image supporting this (we could even have one based of “nvidia-docker”) would address 80% of the batch processing use case.</p>
<blockquote>
<p>large package size</p>
</blockquote>
<p>Removing EMSegment, BRAINSTools and SimpleITK for the core should help.</p>
<blockquote>
<p>platform-specific launcher issues.</p>
</blockquote>
<p>Do you have more details ?  (if that helps, the PythonSlicer launcher can now be used on all platform including installed macOS)</p>

---

## Post #26 by @jcfr (2018-08-12 07:58 UTC)

<p><i>From <a class="mention" href="/u/pieper">@pieper</a> on Thu Aug 09 2018 00:19:58 GMT+0000 (UTC)</i><br><br>&gt; Now, I think that putting effort into having a well maintained docker image supporting this (we could even have one based of “nvidia-docker”) would address 80% of the batch processing use case.</p>
<p>If it gets the job done I’m okay with a docker based solution, but of course that’s the opposite of lightweight.</p>
<p>I would lean toward trying to make sure all the dicom conversion code is logic-only and could be imported without pulling vtkRendering or Qt into the python interpreter (PythonSlicer for now, ultimately a regular python).</p>
<p>Also, thinking about the actual workflow of converting a large set of nii files to dicom, I’d personally want to do a lot of QC checking because so many things could be inconsistent in the nifti files.  So what I’d probably do is start with the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator">CaseIterator</a>  and create a custom scripted module to call the dicom export into an organized directory hierarchy (and also into the Slicer dicom database).</p>

---

## Post #27 by @jcfr (2018-08-12 07:58 UTC)

<p><i>From <a class="mention" href="/u/fedorov">@fedorov</a> on Thu Aug 09 2018 18:37:43 GMT+0000 (UTC)</i><br><br>Great discussion, would be even better if we could have it in-person!</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<blockquote>
<p>having so many simple, rigid, single-purpose dicomToX tools is bad, because these tools hide issues (by making random assumptions and ignore various potential problems) and cause fragmentation in the research community. It would be better to establish one common DICOM import/export tool framework that many people can use, customize, and extend.</p>
</blockquote>
<p>First, I disagree that a general statement like this is accurate. Any tool has issues, and (at least for an outsider) makes random assumptions, and Slicer is no exception, but many of the converters have been around for quite a long time, and are quite robust (arguably, more robust than Slicer!) in dealing with various problems. I think non-Slicer converters from DICOM have larger user base, and may be more reliable just because more people tried and broke them before (e.g., most likely <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a> has a much larger user base than <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DWIConverter">Slicer DWConverter</a>).</p>
<p>Second, fragmentation is inevitable, since research community by definition has different interests and focus areas. But that is good! I do not believe in monolithic tools that solve all problems for everyone. Would it be better to establish one common tool? Maybe. But I don’t see how it can be done practically. I wonder if there is any example where something like this has been done successfully in the research community.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<blockquote>
<blockquote>
<p>platform-specific launcher issues.<br>
Do you have more details ? (if that helps, the PythonSlicer launcher can now be used on all platform including installed macOS)</p>
</blockquote>
</blockquote>
<p>The lack of console output on Windows is a big one for me, and based on many discussions over the past years.</p>
<p><a class="mention" href="/u/pieper">@pieper</a></p>
<blockquote>
<p>Regarding your other points Andrey, while they are generally true I don’t see things like package size or startup time as limiting factors. Converting files like this is not a real time activity and if you have a large number of dicom files to convert slicer is the least of your disk space concerns. No reason to prematurely optimize something like this.</p>
</blockquote>
<p>I think package size is an issue for someone composing a docker image. I think it is common for folks to try to minimize that, and this converter (~1Gb for Slicer?) would be just a small piece of it. For me,  bottom line is using Slicer for converting DICOM in batch mode is cumbersome, but more importantly - we don’t know how robust it is compared to other conversion tools (I am talking here about “from DICOM” pathway). What we do know is that the DICOM IO components of ITK need more love, we also know that for sure “assumptions were made” by people who are no longer around to maintain that code, and we also know that we do not have a robust regression testing for DICOM conversion in Slicer. So all things considered, I am leaning much more towards recommending the converters listed in <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/DICOMVolumeReconstruction/">the project I started last January</a>. Unfortunately, it’s been difficult to make time to continue with that project. If and when we establish some technical capability to compare converters across the board on a versatile dataset, that might be the first step towards educated decision making and harmonization of tools.</p>

---

## Post #28 by @jcfr (2018-08-12 07:58 UTC)

<p><i>From <a class="mention" href="/u/lassoan">@lassoan</a> on Thu Aug 09 2018 20:46:31 GMT+0000 (UTC)</i><br><br>&gt; Any tool has issues, and (at least for an outsider) makes random assumptions</p>
<p>I agree. My point is that based sharing solutions to common problems lowers the development and maintenance workload in the long term (more time is saved than the overhead of coordination between different groups). If you just let everybody do what feels convenient, the easy 90% of the code is reimplemented many times, and the difficult 10% has partial implementation in random toolkits. Eventually, a few well-designed, full-featured solutions emerge as winners, but this process can be accelerated with some conscious effort.</p>
<blockquote>
<p>I do not believe in monolithic tools that solve all problems for everyone</p>
</blockquote>
<p>I agree, monolithic tools are not well suited for this. The problem exactly is that various groups maintain their own monolithic tools, with zero modularity and potential for reuse or customization. Instead, we should have a small common framework that many groups are using and contributing to - with shared infrastructure components (such as tilted gantry, variable image slice spacing, patient name, etc. management) and application-specific plugins (that can handle import/export of a particular DICOM IOD).</p>
<blockquote>
<p>The lack of console output on Windows is a big one for me</p>
</blockquote>
<p>We’ve fixed CTK to have a full-featured interaction Python console, even on Windows. It works really well! However, these developments have not been merged yet . <a class="mention" href="/u/jcfr">@jcfr</a> could you please merge the <a href="https://github.com/commontk/AppLauncher/pulls">pull requests</a> and update Slicer master?</p>

---

## Post #29 by @jcfr (2018-08-12 08:04 UTC)

<p>6 posts were split to a new topic: <a href="/t/migrating-github-issue-to-discourse/3738">Migrating GitHub issue to discourse</a></p>

---

## Post #31 by @jcfr (2018-08-12 07:58 UTC)

<p><i>From <a class="mention" href="/u/fedorov">@fedorov</a> on Sat Aug 11 2018 19:04:53 GMT+0000 (UTC)</i><br><br>As I discovered while working on something else, <a href="http://plastimatch.org/plastimatch.html">plastimatch convert</a> has a function to create DICOM series from an ITK volume. Looks like it only outputs CT, but it provides options to populate metadata from an existing DICOM dataset.</p>

---
