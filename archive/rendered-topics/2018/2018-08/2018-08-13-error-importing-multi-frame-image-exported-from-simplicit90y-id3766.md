# Error importing multi frame image exported from Simplicit90Y (Mirada)

**Topic ID**: 3766
**Date**: 2018-08-13
**URL**: https://discourse.slicer.org/t/error-importing-multi-frame-image-exported-from-simplicit90y-mirada/3766

---

## Post #1 by @Sandor_Konya (2018-08-13 19:23 UTC)

<p>Operating system: Windows 10,  64bit<br>
Slicer version: 4.8.1<br>
Expected behavior: load multiframe image data as (labeled) volume data (dose distribution and VOI)<br>
Actual behavior: In the DICOM browser under advanced tab shows by examining that it is a Scalar Volume, and it warns that “Multi frame image. If slice orientation or spacing is non uniform, then the image may be displayed incorrectly. Use with caution. Reference image does not contain geometric information. Please use caution”</p>
<p>The above mentioned multiframe image data were exported from Simplicit90Y™  (Mirada). Below is the Metadata.<br>
The Pixeldata should represent Dose Distribution and VOIs.</p>
<p><a>Capture|459x499</a></p>
<p>Any chance that i’ll b able to import these VOI’s and Dosis distributions onto my CT-scan and create Volume-Dosis Histograms?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2018-08-14 04:50 UTC)

<p>Normally segmentations are saved to DICOM as segmentation objects or RT structure sets (and can be loaded if you install Reporting and SlicerRT extensions). Is there an option to save into these standard formats?</p>
<p>4D volume import has been greatly improved after Slicer 4.8.1 was released, so if you don’t have any other export option then you can try that. You may also try loading by enabling “Advanced” option, clicking Examine, and choosing different loadables in the list at the bottom.</p>

---

## Post #3 by @Sandor_Konya (2018-08-14 16:51 UTC)

<p>Hi there,</p>
<p>thank you for the answer,<br>
sadly i have no more chance to export / save the datasets, but i’ll try with SlcerRT and Reporting and with the different loadables.<br>
I’ll let you know how it goes!</p>

---

## Post #4 by @fedorov (2018-08-14 17:22 UTC)

<p>I think the issue here could be imperfect support of multiframe DICOM objects in Slicer.</p>
<p><a class="mention" href="/u/sandor_konya">@Sandor_Konya</a> what happens after you try to load the series, despite the warnings? Do you have a CT series corresponding to that labeled volume dataset? That way you could confirm that Slicer accurately interpreted image geometry.</p>
<p>You could also consider using <a href="http://plastimatch.org/plastimatch.html">plastimatch convert</a> or <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a> to convert that DICOM series into NRRD or NIfTI format, and then load those into Slicer. I believe those tools are more robust than Slicer in interpreting DICOM multiframe objects (with the exception of DICOM segmentation object, but it is unlikely that is the object you have).</p>
<p>Of course, if you have a de-identified dataset that you could share, we could look into investigating the issue in more detail.</p>

---

## Post #5 by @Sandor_Konya (2018-08-25 14:00 UTC)

<p>Hi there,<br>
I installed the extensions advised, but still no success in loading the series.</p>
<p>If i load them despite warnings i get following (the load warnig is overlayed on the advaned mode tab)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e8abe5466767a07770dea80b1b34559cc26ae52.jpeg" data-download-href="/uploads/short-url/mCwHcIhB71cvUnwnRS0pruRsh8K.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e8abe5466767a07770dea80b1b34559cc26ae52_2_690x114.jpeg" alt="Capture" data-base62-sha1="mCwHcIhB71cvUnwnRS0pruRsh8K" width="690" height="114" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e8abe5466767a07770dea80b1b34559cc26ae52_2_690x114.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e8abe5466767a07770dea80b1b34559cc26ae52_2_1035x171.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e8abe5466767a07770dea80b1b34559cc26ae52_2_1380x228.jpeg 2x" data-dominant-color="EDEEEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1507×249 68.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
and only get 2 of them loaded in the data tree (theones that are displayed w/o warning in the background)</p>
<p>I’ll try to convert them with plastimatch converter and dcm2niix though.</p>
<p>I suppose that the files in the folder should contain information about the transformation of the datasets ( CT series and a SPECT matched with ridig body transformation) and the segmentation results to.</p>

---

## Post #6 by @lassoan (2018-08-25 22:44 UTC)

<p>It is also possible that frames are missing or the acquisition has variable number of frames. If you use a recent night build, then the MultiVolume importer writes thr reasons why it rejects loading of the data set into the Slicer application log. It would be useful if you could copy the log messages here. You can find the logs in menu: Help / Report a bug.</p>

---

## Post #7 by @Sandor_Konya (2018-08-26 12:53 UTC)

<p>Here is the log excerpt, I cropped a bit, hope that helps:</p>
<blockquote>
<p>[INFO][Stream] 26.08.2018 14:35:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading with imageIOName: GDCM<br>
[…]<br>
Description: itk::ERROR: ImageSeriesReader(000001DB887C4390)] (D:\D\P\Slicer-0\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:264) - Size mismatch! The size of  [path]/WK_V2/IM1.DCM is [892, 892, 17] and does not match the required size [892, 892, 1] from file [path]/WK_V2/IM1.DCM<br>
[ERROR][VTK] 26.08.2018 14:35:19 [vtkCompositeDataPipeline (000001DB88874530)] (D:\D\P\Slicer-0-build\VTKv9\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(000001DB87F624A0) returned failure for request: vtkInformation (000001DB88256120)<br>
Debug: Off<br>
Modified Time: 371028<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_DATA<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FROM_OUTPUT_PORT: 0<br>
[CRITICAL][Stream] 26.08.2018 14:35:19 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Could not read scalar volume using GDCM approach.  Error is: FileFormatError</p>
</blockquote>
<p>and then again:</p>
<blockquote>
<p>[ERROR][VTK] 26.08.2018 14:35:20 [vtkITKArchetypeImageSeriesScalarReader (000001DB87F62100): Exception from vtkITK MegaMacro:<br>
[…]<br>
Description: itk::ERROR: ImageSeriesReader(000001DB887C33D0)] (D:\D\P\Slicer-0\Libs\vtkITK\vtkITKArchetypeImageSeriesScalarReader.cxx:264) - Size mismatch! The size of  [path]/WK_V2/IM1.DCM is [892, 892, 17] and does not match the required size [892, 892, 1] from file [path]/WK_V2/IM1.DCM<br>
[ERROR][VTK] 26.08.2018 14:35:20 [vtkCompositeDataPipeline (000001DB88872230)] (D:\D\P\Slicer-0-build\VTKv9\Common\ExecutionModel\vtkExecutive.cxx:782) - Algorithm vtkITKArchetypeImageSeriesScalarReader(000001DB87F62100) returned failure for request: vtkInformation (000001DB88878800)<br>
[…]<br>
[CRITICAL][Stream] 26.08.2018 14:35:20 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Could not read scalar volume using DCMTK approach.  Error is: FileFormatError</p>
</blockquote>

---

## Post #8 by @lassoan (2018-08-26 13:24 UTC)

<p>Could you upload the complete log (only remove patient information from the log - patient name, ID, etc)? If it is too large then you can upload to <a href="http://pastebin.com">pastebin.com</a>, dropbox, onedrive, or gdrive and post the link.</p>

---

## Post #9 by @fedorov (2018-08-26 15:18 UTC)

<p>I would first try with dcm2niix.</p>

---

## Post #10 by @lassoan (2018-08-26 16:27 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="9" data-topic="3766" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I would first try with dcm2niix</p>
</blockquote>
</aside>
<p>Is dcm2niix that good? If so, then we could use it in the MultiVolume importer in Slicer.</p>

---

## Post #11 by @fedorov (2018-08-26 21:04 UTC)

<p>Well, first, I do not see in this thread any reason why that specific dataset would be handled by the multivolume plugin. It is probably just a couple of scalar volumes saved as enhanced multiframe objects, and I did have problems with multiframe objects in the past using Slicer. But maybe I missed something. I also know that the MF parser in ITK (at least the one that is based on DCMTK) doesn’t have a function to sort individual frames of a MF instance geometrically, which tells something about MF support robustness.</p>
<p>Regarding integration of dcm2niix, it would make sense to first consider this not in the context of multivolume, but for parsing scalar volumes. Multivolume plugin does not parse or load scalar volumes by itself, it delegates that task to the scalar volume plugin. To make an educated decision of whether it makes sense to consider integrating dcm2niix into Slicer, I would want to see some meaningful comparison of different tools to demonstrate its superiority to alternatives. I do not have resources to work on such at the moment.</p>
<p>In this particular situation, I just thought it is most practical to take a converter that is specifically designed for the task, and try it on the dataset.</p>

---

## Post #12 by @lassoan (2018-08-27 03:52 UTC)

<p>Thanks for the explanation, I have been following multiple discussions and it seems I missed the point that these are just simple 3D volumes in multi-frame format and you are right that for this it is not necessary to use MultiVolume infrastructure</p>
<p>If Slicer has problems reading this file then most probably ITK’s DICOM image reader should be improved to better support DICOM files that contains multiple frames.</p>
<p><a class="mention" href="/u/thewtex">@thewtex</a> Can you comment on this? Has DICOM multi-frame image support been improved recently? Do you need sample data sets to investigate or you are already aware that there are some limitations?</p>

---

## Post #13 by @thewtex (2018-08-27 04:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If Slicer has problems reading this file then most probably ITK’s DICOM image reader should be improved to better support DICOM files that contains multiple frames.</p>
<p><a class="mention" href="/u/thewtex">@thewtex</a> Can you comment on this? Has DICOM multi-frame image support been improved recently? Do you need sample data sets to investigate or you are already aware that there are some limitations?</p>
</blockquote>
</aside>
<p>Are you certain the issue is in the ITK DICOM image reader?</p>

---

## Post #14 by @lassoan (2018-08-27 05:11 UTC)

<aside class="quote no-group" data-username="thewtex" data-post="13" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/thewtex/48/32_2.png" class="avatar"> thewtex:</div>
<blockquote>
<p>Are you certain the issue is in the ITK DICOM image reader?</p>
</blockquote>
</aside>
<p>I don’t have the data set but I’ve tried loading <a>3D.dcm sample</a> just now.</p>
<p>I’ve found that passing the file directly to the ITK reader (by drag-and-dropping the file to Slicer window and loading using ITK series reader) worked. So, ITK can load the multi-frame volume.</p>
<p>Loading the volume through Slicer’s DICOM scalar volume plugin failed with the same error as in the log above (<code>Size mismatch! The size of  .../3D.dcm is [275, 176, 164] and does not match the required size [275, 176, 1] from file .../3D.dcm</code>).</p>
<p><strong>So, it seems that this loading error is due to how Slicer uses the ITK image series reader and it has to be fixed in Slicer. Until the fix is ready, multi-frame volumes can be loaded by using “Add data” function (without DICOM module).</strong></p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> mentioned some other limitations of multi-frame image support in ITK - see above:</p>
<aside class="quote no-group" data-username="fedorov" data-post="11" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I also know that the MF parser in ITK (at least the one that is based on DCMTK) doesn’t have a function to sort individual frames of a MF instance geometrically</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/thewtex">@thewtex</a> Do you know if this is this still the case? Even with the GDCM-based reader? Do you know about any other limitations related to multi-frame files?</p>

---

## Post #15 by @pieper (2018-08-27 12:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>So, it seems that this loading error is due to how Slicer uses the ITK image series reader and it has to be fixed in Slicer. Until the fix is ready, multi-frame volumes can be loaded by using “Add data” function (without DICOM module).</p>
</blockquote>
</aside>
<p>This is definitely something that can debugged - by default the DICOMScalarVolumePlugin should be using the same code path as the Add Dialog, with the ability to force the use of other readers, as described in the thread linked below.</p>
<aside class="quote quote-modified" data-post="1" data-topic="354">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-dicom-scalar-volume-plugin-relies-on-old-gdcm-why-do-we-not-use-dcmtk/354">Slicer DICOM Scalar volume plugin relies on (old) GDCM: why do we not use DCMTK?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    This question came up several times, and I would like to document the answer - why do we rely on GDCM series reader in this code: <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkITK/vtkITKArchetypeImageSeriesScalarReader.cxx#L96">https://github.com/Slicer/Slicer/blob/master/Libs/vtkITK/vtkITKArchetypeImageSeriesScalarReader.cxx#L96</a> 
Arguably, this is one of the most important pieces of Slicer, since absolutely every user wants their DICOM series to be loaded correctly. We should really strive for the scalar volume loader to be very robust! 
This example can be used to demonstrate the GDCM read…
  </blockquote>
</aside>


---

## Post #16 by @pieper (2018-08-27 12:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Loading the volume through Slicer’s DICOM scalar volume plugin failed with the same error as in the log above ( <code>Size mismatch! The size of .../3D.dcm is [275, 176, 164] and does not match the required size [275, 176, 1] from file .../3D.dcm</code> ).</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> under what circumstances did you get that error?  I just loaded the 3D.dcm file through the dicom module on a linux system with a nightly build from August 4th.  I had no problems no matter what reader approach (GDCM or DCMTK or Archetype all match the Add Data result).</p>

---

## Post #17 by @lassoan (2018-08-27 13:36 UTC)

<aside class="quote no-group" data-username="pieper" data-post="16" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>under what circumstances did you get that error?</p>
</blockquote>
</aside>
<p>In that <a>sample data folder</a> there are 4 files. If you import all of them into the DICOM database then you’ll see the error.</p>
<p>It is an interesting twist in the story. DICOM reading fails because 3 of the 4 series has the same series instance uid, therefore the DICOM reader tries to read them as one series, but in fact they are completely independent volumes.</p>
<p>For me it seems to be a violation of he DICOM standard that multiple volumes have the same series instance UID, but it is interesting that both this data set and most likely the Mirada Simplicity generated data set suffers from the same issue.</p>

---

## Post #18 by @lassoan (2018-08-27 13:43 UTC)

<p><a class="mention" href="/u/sandor_konya">@Sandor_Konya</a> Could you please check if you enable “Allow loading subseries by time” option (in menu: Application settings / DICOM), then go to DICOM module, enable “Advanced” option (in lower-right corner), click “Examine”, then you see multiple series with different contentTime in the list at the bottom?</p>
<p>If you check each loadable (with different contentTime, unchecked by default) and click “Load” then are the volumes loaded correctly?</p>
<p>Can you share the data set? (preferably use phantom data set; if patient data set then make it is anonymized)</p>

---

## Post #19 by @fedorov (2018-08-27 13:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>multiple volumes have the same series instance UID, but it is interesting that both this data set and most likely the Mirada Simplicity generated data set suffers from the same issue.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/sandor_konya">@Sandor_Konya</a> did you do anything with those files prior to loading into Slicer? Did you apply any anonymization on Mirada or using any other tools, or you are confident those files are exactly as they were created by Mirada?</p>
<p>Assignment of non-unique UIDs seems like a very serious non-compliance issue for a clinical product.</p>

---

## Post #20 by @pieper (2018-08-27 14:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For me it seems to be a violation of he DICOM standard that multiple volumes have the same series instance UID, but it is interesting that both this data set and most likely the Mirada Simplicity generated data set suffers from the same issue.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="fedorov" data-post="19" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Assignment of non-unique UIDs seems like a very serious non-compliance issue for a clinical product.</p>
</blockquote>
</aside>
<p>Hmm…  Any 4D sequence acquired on one modality would have multiple volumes in one series (and therefore be a multivolume).  But if these files are not from the same equipment or modality then they shouldn’t be in the same Series.  In this case I guess the labels and dose are from different equipment from the original images so yes, a violation.</p>
<p>Some obligatory links to the Standard below…</p>
<p><a href="http://dicom.nema.org/medical/dicom/current/output/html/part01.html" class="onebox" target="_blank" rel="noopener">http://dicom.nema.org/medical/dicom/current/output/html/part01.html</a></p>
<blockquote>
<p>This information model is a simplification of the real world concepts and activities of medical imaging; for acquisition modalities, a Study is approximately equivalent to an ordered procedure, and a Series is approximately equivalent to a performed data acquisition protocol element. In other domains, such as Radiotherapy, the Study and Series are less clearly related to real world entities or activities, but are still required for consistency.</p>
</blockquote>
<p>and</p>
<p><a href="http://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.1.2.3" class="onebox" target="_blank" rel="noopener">http://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.1.2.3</a></p>
<blockquote>
<p>A.1.2.3 Series IE</p>
<p>The Series IE defines the Attributes that are used to group Composite Instances into distinct logical sets. Each Series is associated with exactly one Study.</p>
<p>The following criteria group Composite Instances into a specific Series:</p>
<ol>
<li>
<p>All Composite Instances within a Series must be of the same modality</p>
</li>
<li>
<p>Each Series may be associated with exactly one Frame of Reference IE, and if so associated all Composite Instances within the Series shall be spatially or temporally related to each other</p>
</li>
<li>
<p>All Composite Instances within the Series shall be created by the same equipment; therefore, each Series is associated with exactly one Equipment IE</p>
</li>
<li>
<p>All Composite Instances within a Series shall have the same Series information</p>
</li>
</ol>
</blockquote>

---

## Post #21 by @thewtex (2018-08-27 14:38 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="14" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<blockquote>
<p>I also know that the MF parser in ITK (at least the one that is based on DCMTK) doesn’t have a function to sort individual frames of a MF instance geometrically</p>
</blockquote>
<p><a class="mention" href="/u/thewtex">@thewtex</a> Do you know if this is this still the case? Even with the GDCM-based reader? Do you know about any other limitations related to multi-frame files?</p>
</blockquote>
</aside>
<p>Multi-frame series work well in ITK as far as I am aware.</p>
<p>There were a few recent improvements for some exceptional image geometries:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/commit/8d093d5600113f94b0d635184efc14161035ce81#diff-832dee3fd0bcc47414150e32a4a64337">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/8d093d5600113f94b0d635184efc14161035ce81#diff-832dee3fd0bcc47414150e32a4a64337" target="_blank" rel="noopener nofollow ugc">github.com/InsightSoftwareConsortium/ITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/8d093d5600113f94b0d635184efc14161035ce81" target="_blank" rel="noopener nofollow ugc">ENH: compute spacing using n-1 instead 2-1 in ImageSeriesReader</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2018-08-03" data-time="19:26:51" data-timezone="UTC">07:26PM - 03 Aug 18 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/dzenanz" target="_blank" rel="noopener nofollow ugc">
          <img alt="dzenanz" src="https://avatars.githubusercontent.com/u/1792121?v=4" class="onebox-avatar-inline" width="20" height="20">
          dzenanz
        </a>
      </div>

      <div class="lines" title="changed 1 files with 87 additions and 115 deletions">
        <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/8d093d5600113f94b0d635184efc14161035ce81" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+87</span>
          <span class="removed">-115</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Use first and last slice for computing the spacing,
instead of second and first <span class="show-more-container"><a href="https://github.com/InsightSoftwareConsortium/ITK/commit/8d093d5600113f94b0d635184efc14161035ce81" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">- it is more numerically stable.
Also simplify GenerateOutputInformation method somewhat.

Change-Id: Id8076ae195e6d145d8a9051a94276ded172904d5</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubcommit" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/commit/23436a04c978d176b32775e97d2701d96d6d2dd6#diff-832dee3fd0bcc47414150e32a4a64337">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/23436a04c978d176b32775e97d2701d96d6d2dd6#diff-832dee3fd0bcc47414150e32a4a64337" target="_blank" rel="noopener nofollow ugc">github.com/InsightSoftwareConsortium/ITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/23436a04c978d176b32775e97d2701d96d6d2dd6" target="_blank" rel="noopener nofollow ugc">ENH: fix reading of oblique image series</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2018-08-03" data-time="21:04:19" data-timezone="UTC">09:04PM - 03 Aug 18 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/dzenanz" target="_blank" rel="noopener nofollow ugc">
          <img alt="dzenanz" src="https://avatars.githubusercontent.com/u/1792121?v=4" class="onebox-avatar-inline" width="20" height="20">
          dzenanz
        </a>
      </div>

      <div class="lines" title="changed 2 files with 30 additions and 7 deletions">
        <a href="https://github.com/InsightSoftwareConsortium/ITK/commit/23436a04c978d176b32775e97d2701d96d6d2dd6" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+30</span>
          <span class="removed">-7</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">ImageSeriesReader can read non-orthogonal direction cosines.
This is controlled <span class="show-more-container"><a href="https://github.com/InsightSoftwareConsortium/ITK/commit/23436a04c978d176b32775e97d2701d96d6d2dd6" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">by ForceOrthogonalDirectionOff();
That calculates the third axis from difference in positions
of last and first slice (usually from DICOM's image position patient tag).

Change-Id: I3774b4a8e022ba4581d8d63f0f5cadf0ccfd8615</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If there is an image geometry / series type that exists and is known to not read correctly, then we should look into fixing it. However, performing geometry checks for the sake of geometry checks can have performance downsides that dramatically impact user experience. We do not want the experience of loading DICOM files to be painfully slow.</p>

---

## Post #22 by @lassoan (2018-08-27 15:22 UTC)

<p><a class="mention" href="/u/thewtex">@thewtex</a> Thanks for the information, this all sounds promising. Unfortunately, even clinical device manufacturers misuse the DICOM standard in every possible way, so consistency checks are necessary for safety-critical applications. Performance of course is important, too - maybe that can be addressed by making some checks optional.</p>

---

## Post #23 by @fedorov (2018-08-27 19:19 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> can you tell us if the reader sorts the individual frames of a multiframe object geometrically, since you worked on that part recently?</p>
<p>I can’t think of a use case when it makes sense to not sort image slices geometrically while reconstructing the volume. What is the alternative - to keep the fingers crossed?</p>

---

## Post #24 by @pieper (2018-08-27 19:58 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="23" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I can’t think of a use case when it makes sense to not sort image slices geometrically while reconstructing the volume. What is the alternative - to keep the fingers crossed?</p>
</blockquote>
</aside>
<p>I’ll note that the issue of non-geometrically sorted frames in a multiframe document comes up for data created from converters that read and concatenate the frames read from disk that is, for example, sorted by filenames or directory (inode) order.  I suspect the reason sorting isn’t usually needed is that modalities would typically output sorted frames.</p>
<p>The ‘defensive programming’ thing to approach would be to have both (1) the converter sort the frames to work with systems that typically only see sorted frames and (2) the reader sort the frames to handle converters or modalities that don’t provide sorted frames.</p>
<p>Of course, sorting correctly can require heuristics or further user input so there’s no 100% solution for these issues.</p>

---

## Post #25 by @fedorov (2018-08-27 20:14 UTC)

<aside class="quote no-group" data-username="pieper" data-post="24" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I suspect the reason sorting isn’t usually needed is that modalities would typically output sorted frames.</p>
</blockquote>
</aside>
<p>I just don’t know how accurate that statement is. Following the same reasoning, one might not sort geometrically non-multiframe series and instead rely on InstanceNumber or some other assumption (or wait - is this what ITK has been doing already for reading non-multiframe series, and Slicer sorts them outside of ITK because of that?).</p>
<p>I agree that disabling sorting makes sense, once the user established that the specific equipment produces sorted frames, and no sorting is necessary. But I still don’t think that by default it should be disabled.</p>

---

## Post #26 by @fedorov (2018-08-27 20:29 UTC)

<p>I also think it is time to split this topic - I am afraid we veered off the topic and might have lost the user and the actual problem they wanted to get resolved.</p>

---

## Post #27 by @pieper (2018-08-27 20:33 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> I didn’t suggest <em>not</em> sorting frames, just explaining why the issue probably hasn’t come up much in practice.  In my (admittedly very limited) experience I’ve only ever seen non-sorted frames come from converters.</p>

---

## Post #28 by @fedorov (2018-08-27 20:40 UTC)

<p>I agree. In my (even more limited) experience, I have never encountered multi-frame series produced by the clinical applications I worked with. I think it is hard to get a grasp of how important it is with very limited adoption of multiframe by modalities.</p>
<p>Also, it is not clear if sorting is disabled, or it is just not implemented (as it has not been implemented for non-multiframe series).</p>

---

## Post #29 by @pieper (2018-08-27 20:55 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="28" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Also, it is not clear if sorting is disabled, or it is just not implemented (as it has not been implemented for non-multiframe series).</p>
</blockquote>
</aside>
<p>I don’t think it’s disabled on purpose, I think it’s just a very different code path.</p>

---

## Post #30 by @thewtex (2018-08-28 17:12 UTC)

<p>In ITK, the <code>itk::ImageSeriesReader</code> processes in a series of images. These images should already be sorted. They can be sorted with any desirable strategy beforehand.</p>
<p>For example, ITK provides <a href="https://itk.org/Doxygen/html/classitk_1_1DCMTKSeriesFileNames.html" rel="noopener nofollow ugc">itk::DCMTKSeriesFileNames</a>, which is a nice default. This works by:</p>
<blockquote>
<p>This class generates a sequence of files whose filenames points to a DICOM file. The ordering is based on the following strategy: Read all images in the directory (assuming there is only one study/serie)</p>
<ol>
<li>Extract Image Orientation &amp; Image Position from DICOM images, and then calculate the ordering based on the 3D coordinate of the slice</li>
<li>If for some reason this information is not found or failed, another strategy is used: the ordering is based on ‘Image Number’</li>
<li>If this strategy also failed, then the filenames are ordered by lexicographical order.</li>
</ol>
<p>If multiple volumes are being grouped as a single series for your dicom objects, you may want to try calling -&gt;SetUseSeriesDetails(true) prior to calling SetDirectory().</p>
</blockquote>
<p>Slicer could also use a more complicated or different strategy, too.</p>
<p>If the images have already been sorted by the time they are ready to be passed to the <code>itk::ImageFileReader</code>, then I do not think they should be sorted again. This is an opportunity for conflicting behavior and it negatively impacts performance. While some of the best DICOM support around can be found in Slicer, a common criticism is that it is too slow for users – we should try to improve this <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"> .</p>

---

## Post #31 by @lassoan (2018-08-28 17:51 UTC)

<aside class="quote no-group" data-username="thewtex" data-post="30" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/thewtex/48/32_2.png" class="avatar"> thewtex:</div>
<blockquote>
<p>Slicer, a common criticism is that it is too slow for users</p>
</blockquote>
</aside>
<p>Slicer needs to handle more than just images. Some of the data objects cross-reference other objects (by DICOM UIDs), which can be loaded in any order or may be missing - to resolve all these we need to maintain a database. We also need to handle ambiguities in how to interpret a data set. Often there are many interpretations, some of them are most likely to be correct than others, but you cannot choose the most likely solution until you investigated all options. Database building, reading, testing hypotheses about best interpretation, etc. take time - probably magnitudes more time than consistency checks or sorting of frames. If we lock things down (e.g., disable DICOM plugins that you are sure you won’t need; load files without DICOM database import) then we get better performance, but by default we prioritize flexibility over performance.</p>
<p>Still, Slicer’s current DICOM import and loading speed currently is about at the level of industry standard. It was noticeable slower about half year or year ago, but we then successfully identified and fixed some performance bottlenecks.</p>
<p>Of course, things can be improved further. However, instead of shaving a few percent off from raw DICOM image reading times, we plan to focus on reducing “time to first image” by showing thumbnails, using DICOMDIR files, etc. in the DICOM browser.</p>

---

## Post #32 by @Sandor_Konya (2018-08-28 18:59 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> You were right, after changing the settings i see all of the loadables in a list, each having different content time in the advanced tab.<br>
It loads the content, but not correclty, the slices are displayed as the image data matrix had a wrong datashape (can’t explain better) but see pic below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fd97102d3e35bc872846163729cdee840331419.png" data-download-href="/uploads/short-url/bonAlP0FzYYIPhIldZBMgQufsjD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd97102d3e35bc872846163729cdee840331419_2_585x500.png" alt="image" data-base62-sha1="bonAlP0FzYYIPhIldZBMgQufsjD" width="585" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd97102d3e35bc872846163729cdee840331419_2_585x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd97102d3e35bc872846163729cdee840331419_2_877x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4fd97102d3e35bc872846163729cdee840331419_2_1170x1000.png 2x" data-dominant-color="343440"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2144×1830 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ll make an anonimised data set and upload it soon.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a><br>
I haven’t modified any of the files, i left them in the structure as it was exported from the software.</p>
<aside class="quote no-group" data-username="fedorov" data-post="26" data-topic="3766" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I also think it is time to split this topic - I am afraid we veered off the topic and might have lost the user and the actual problem they wanted to get resolved.</p>
</blockquote>
</aside>
<p>… not THIS user <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---

## Post #34 by @pieper (2018-08-28 19:28 UTC)

<aside class="quote no-group" data-username="thewtex" data-post="30" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/thewtex/48/32_2.png" class="avatar"> thewtex:</div>
<blockquote>
<p>For example, ITK provides <a href="https://itk.org/Doxygen/html/classitk_1_1DCMTKSeriesFileNames.html">itk::DCMTKSeriesFileNames</a>, which is a nice default. This works by:</p>
</blockquote>
</aside>
<p>Yes, exactly - this is a nice heuristic for sorting files, but what <a class="mention" href="/u/fedorov">@fedorov</a> mentioned is the case where you have a multiframe object in a single file, but the individual frames are not geometrically sorted.  It’s a valid point that the standard allows many different frame orderings so the same kind of sorting heuristics could/should be applied to soft the frames as they are to files.</p>

---

## Post #35 by @fedorov (2018-08-28 19:59 UTC)

<aside class="quote no-group" data-username="Sandor_Konya" data-post="32" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/58956e/48.png" class="avatar"> Sandor_Konya:</div>
<blockquote>
<p>It loads the content, but not correclty</p>
</blockquote>
</aside>
<p>I know I will sound as a broken record … but is the result of conversion with <code>dcm2niix</code> and <code>plastimatch convert</code> any different?</p>
<aside class="quote no-group" data-username="Sandor_Konya" data-post="32" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/58956e/48.png" class="avatar"> Sandor_Konya:</div>
<blockquote>
<p>… not THIS user <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="thewtex" data-post="30" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/thewtex/48/32_2.png" class="avatar"> thewtex:</div>
<blockquote>
<p>For example, ITK provides <a href="https://itk.org/Doxygen/html/classitk_1_1DCMTKSeriesFileNames.html">itk::DCMTKSeriesFileNames </a>, which is a nice default.</p>
</blockquote>
</aside>
<p>I don’t know if this is a new development, or if it was not considered for use in Slicer in the past for any reason, but if it works as stated, it should be considered to replace the sorting implemented in the Slicer scalar volume DICOM plugin then.</p>

---

## Post #36 by @pieper (2018-08-28 20:44 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="35" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I don’t know if this is a new development</p>
</blockquote>
</aside>
<p>I believe this is basically the same code that has been in itkGDCMSeriesFileNames from the very early days, which Slicer <a href="https://github.com/Slicer/Slicer/blob/4c0b0b15276aedc0e12d77e2227536426979d773/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx">does use</a>.  As <a class="mention" href="/u/thewtex">@thewtex</a> says, this code requires that all the files be in one directory and that the directory contain only one series.  This simply does not match the way many people have their data.  Very often multiple series are in the same directory.  And also very often (such as a DICOM exported CD or DVD) the files that make up a series are spread out across subdirectories.</p>
<p>The DICOMScalarVolumePlugin (and others) use the database and heuristics to create loadable chunks that correspond to the data that Slicer will be able to digest and then gives the user options about which are passed to ITK for loading.</p>
<p>It is worthwhile to try improving ITK’s implementation to relax some of the constraints and handle more scenarios, but it’s fairly big job and several previous efforts haven’t worked out too well, which is why there is still the legacy GDCM reader path in parallel with the newer but differently incomplete DCMTK path in ITK and exposed in Slicer.</p>
<p>If you look at the /<a href="https://github.com/Slicer/Slicer/tree/4c0b0b15276aedc0e12d77e2227536426979d773/Libs/vtkITK">vtkITKArchetype</a>* classes in Slicer you’ll see that a lot of the code involves instantiating the ITK readers across all the range of possible image types that might be discovered from parsing a dicom series, but even this (very large) set doesn’t handle all the other cases that one might want to load from a dicom study (like SEG, PM, or various types of timeseries images).</p>
<p>One more point: the whole code base could obviously benefit from a fresh start, but as has been noted many times in the past, we don’t have any way to really test a new implementation.  The existing implementation was developed to read data that we don’t have access to (and we never will have because much of it private patient data or was otherwise not public).</p>

---

## Post #37 by @lassoan (2020-05-17 02:39 UTC)

<p>A post was split to a new topic: <a href="/t/diffusion-volume-loading/11583">Diffusion volume loading</a></p>

---

## Post #38 by @Anonymous007 (2023-05-17 13:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="3766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>by drag-and-dropping the file to Slicer window and loading using ITK series reader</p>
</blockquote>
</aside>
<p>How to load using ITK Series reader?</p>

---

## Post #39 by @lassoan (2023-05-17 18:16 UTC)

<p>If you drag-and-drop a single file to the Slicer application window and you are <em>not</em> in DICOM module then the ITK series reader is used for reading the DICOM file. This method is not recommended and may result in incorrect loading of the DICOM data set.</p>

---
