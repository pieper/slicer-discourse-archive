---
topic_id: 1142
title: "Slicer Nightly Build Crash Loading Dicoms"
date: 2017-09-28
url: https://discourse.slicer.org/t/1142
---

# Slicer Nightly Build Crash loading DICOMs

**Topic ID**: 1142
**Date**: 2017-09-28
**URL**: https://discourse.slicer.org/t/slicer-nightly-build-crash-loading-dicoms/1142

---

## Post #1 by @juangdiosa (2017-09-28 17:36 UTC)

<p>Hi everybody</p>
<p>I tried to load my DICOMs in the Nightly version but slicer crashed, It is so strange because those DICOMs files I could load without problems in the stable version. I tried load those files on windows and linux versions and after the following message slicer close.<br>
“Warnings detected during load. Examine data in advance mode for details. Load anyway?”. Acording to Advance models - Reference image in series does not contain geometry information please use caution-.</p>
<p>I tried with advance mode, DICOM Module, DICOM Patcher Module  and deleting all DICOM data and reload again. Are there another alternative in order to load my files?. My Idea is to use Editor Segmentation module and reduce the processing time.</p>
<p>thanks a lot<br>
are there another alternative in order to load my files?. My Idea is to use Editor Segmentation module and reduce the processing time.</p>
<p>thanks a lot</p>

---

## Post #2 by @pieper (2017-09-28 18:30 UTC)

<p>Hi -</p>
<p>That’s odd, thanks for reporting the issue.  A few things have changed between the 4.6 release and the current nightly but I wouldn’t have thought it would impact loading data.</p>
<p>A few troubleshooting ideas:</p>
<ul>
<li>
<p>Do you see anything in the error log? (Try the menu Help-&gt;Report a Bug).  If there’s no patient identifiable information you could send me the info.</p>
</li>
<li>
<p>When you are in Advanced mode of the browser is the selected reader Scalar Volume?  Are there other readers offered?</p>
</li>
<li>
<p>Can you load the data using the File-&gt;Add Data menu?  Typically if you select one of the dicom files and uncheck the “Single File” option you might get the data to load.</p>
</li>
<li>
<p>If you know anything else that might make this data “weird” compared to data that does load in the Nightly slicer please let us know.  Or even better if you have sharable data that triggers the behavior that would be best.</p>
</li>
<li>
<p>Of course if your main goal is just to use the Segment Editor you could just save the files from 4.6 in nrrd format and load those in the Nightly.</p>
</li>
</ul>
<p>-Steve</p>

---

## Post #3 by @juangdiosa (2017-10-05 16:01 UTC)

<p>Hi Steve. Thanks for your help.</p>
<p>According to error log, slicer has a critical error for two reasons: firstly  "could not read scalar volumen using GDCM: Error is FileFormatError. Secondly “Reference image in series does not contain geometry information”.</p>
<p>When I am in advanced mode the reader scalar volume is selected by default, I cannot change to other reader or maybe I do not how to do it.</p>
<p>I could load my DICOMs loading by Data menu  and used the Segment Editor without problems.</p>
<p>Here you can access to the data in order to identify the triggers. <a href="https://drive.google.com/drive/folders/0B91rlquiQ2OkT1d4ZGRJLVhhV2s?usp=sharing" rel="nofollow noopener">https://drive.google.com/drive/folders/0B91rlquiQ2OkT1d4ZGRJLVhhV2s?usp=sharing</a></p>
<p>regards</p>

---

## Post #4 by @lassoan (2017-10-05 18:19 UTC)

<p>I could reproduce the crash. There is something wrong with one of the images (probably the file is corrupted). GDCM handles the error gracefully (reports an error and quits), but DCMTK crashes. It may be this issue: <a href="https://issues.itk.org/jira/browse/ITK-3570">https://issues.itk.org/jira/browse/ITK-3570</a></p>
<p>To avoid the crash, switch to Advanced mode, click Examine, and uncheck all items (prevent from loading) that has warnings.</p>
<p>Maybe if <code>Warnings detected during load. Examine data in Advanced mode for details. Load anyway?</code> popup is displayed and  user clicks <code>OK</code>  then we should not load those series that have warnings? <a class="mention" href="/u/pieper">@pieper</a> What do you think?</p>

---

## Post #5 by @pieper (2017-10-05 18:43 UTC)

<p><a class="mention" href="/u/juangdiosa">@juangdiosa</a> thanks for providing the anonymized data for testing.</p>
<p>Another workaround would be to go into the Edit-&gt;Application Settings to the DICOM page and pick GCDM in the Reader Approach selection menu.  <a href="https://github.com/Slicer/Slicer/commit/28498540b42a10a2d017d5238a9556b51e92ac63#diff-5c81585867008dffacf021ea0c9d23d4">Before this change</a> only GCDM was tried, but we made the defalt behavior to try DCMTK if GDCM failed to load.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I think you are right.  The stack trace below is what I got on mac.  Looks like the same ITK issue you reported.</p>
<p>Regarding the dialog, it could make sense to have a third option where only data with no warnings is loaded, but this would complicate things and the warnings might be false positives sometimes.</p>
<p>I think it would be better to put effort into making sure ITK doesn’t crash or if that’s not easy then go back to using only GDCM as the default behavior.</p>
<pre>

Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   libsystem_platform.dylib      	0x00007fffda61dfd1 _platform_memmove$VARIANT$Ivybridge + 49
1   libITKIODCMTK-4.12.1.dylib    	0x00000001082f7ec9 itk::DCMTKImageIO::Read(void*) + 233
2   libvtkITK.dylib               	0x0000000106ad6a1a itk::ImageFileReader&lt;itk::Image, itk::DefaultConvertPixelTraits &gt;::GenerateData() + 474
3   libITKCommon-4.12.1.dylib     	0x000000010ad0e89f itk::ProcessObject::UpdateOutputData(itk::DataObject*) + 223
4   libvtkITK.dylib               	0x0000000106a98ae7 itk::ImageSeriesReader&lt;itk::Image &gt;::GenerateData() + 1399
5   libITKCommon-4.12.1.dylib     	0x000000010ad0e89f itk::ProcessObject::UpdateOutputData(itk::DataObject*) + 223
6   libvtkITK.dylib               	0x0000000106a91143 vtkITKArchetypeImageSeriesScalarReader::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 27747
7   libvtkCommon-7.1.1.dylib      	0x000000010f4197d2 vtkExecutive::CallAlgorithm(vtkInformation*, int, vtkInformationVector**, vtkInformationVector*) + 66
8   libvtkCommon-7.1.1.dylib      	0x000000010f4144bd vtkDemandDrivenPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 61
9   libvtkCommon-7.1.1.dylib      	0x000000010f40fcab vtkCompositeDataPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 107
10  libvtkCommon-7.1.1.dylib      	0x000000010f413c0b vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 1291
11  libvtkCommon-7.1.1.dylib      	0x000000010f42eeea vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*) + 762
12  libvtkCommon-7.1.1.dylib      	0x000000010f41424c vtkDemandDrivenPipeline::UpdateData(int) + 252
13  libvtkCommon-7.1.1.dylib      	0x000000010f42f37c vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector*) + 252

</pre>

---

## Post #6 by @fedorov (2017-10-05 20:36 UTC)

<p>Tangentially related to this issue, we experienced situation (not consistently reproducible) with Slicer crashing while in ITK/GDCM reader (at least that’s what it looked like from the trace)… <a class="mention" href="/u/che85">@che85</a> was working on this. It belongs to a separate discussion, but I just wanted to bring it up to loop Christian in.</p>

---

## Post #7 by @pieper (2017-10-06 15:13 UTC)

<p>I spent some more time debugging and looking through the ITK code and didn’t see an obvious fix to propose.</p>
<p>I’m thinking we should change the Slicer default reader back to only use GDCM but leave in place the option to enable DCMTK.</p>

---

## Post #8 by @lassoan (2017-10-07 04:57 UTC)

<p>I’ve checked the ITK code, too, and it seemed that the problem is caused by a design error, which is not obvious how should be fixed. I agree that instead of urging ITK developers we should just temporarily prevent automatic fallback to DCMTK. I’ve added an issue in Slicer bugtracker to track this: <a href="https://issues.slicer.org/view.php?id=4454">https://issues.slicer.org/view.php?id=4454</a></p>

---

## Post #9 by @fedorov (2017-10-09 16:26 UTC)

<p>Instead of disabling the fallback, we could also check for SamplesPerPixel in the input dataset, and not invoke the fallback if it is not 1.</p>

---

## Post #10 by @lassoan (2017-10-09 17:11 UTC)

<p>We would need to then parse each file twice: once just parse the header with GDCM IO or low-level DCMTK API to find out if we may try to parse it using DCMTK IO. Doable, but may be slow and some development work. Also, the fact that DCMTK IO is so fragile indicates that it is not used/tested well enough yet, so it may not be ready for real-world use.</p>

---

## Post #11 by @lassoan (2017-10-09 17:14 UTC)

<p><a class="mention" href="/u/thewtex">@thewtex</a> What do you think? Is ITK’s DCMTK IO ready for production use? Is there a chance somebody can fix the <a href="https://issues.itk.org/jira/browse/ITK-3570">crash</a> in time before the new stable version of Slicer (in about 2 weeks)?</p>

---

## Post #12 by @fedorov (2017-10-09 17:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="1142">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We would need to then parse each file twice</p>
</blockquote>
</aside>
<p>I meant to do this check in the DICOM python plugin code, before calling the DCMTK IO plugin. At that point, the dataset is already parsed, and it is just about checking another tag. I agree DCMTK IO is not used/tested well enough, but it does allow to load certain datasets that do not work with GDCM IO. And it will never become used/tested if we don’t use it…</p>

---

## Post #13 by @thewtex (2017-10-09 17:31 UTC)

<p>A number of fixes have been made to ITK / DCMTK recently. Francois is going to take a look at ITK-3570. We will bump up the priority on this issue.</p>

---

## Post #14 by @fbudin69500 (2017-10-11 21:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>: Can I add the image you attached to the ITK bug report to create a new test in ITK?</p>

---

## Post #15 by @lassoan (2017-10-12 05:03 UTC)

<p>Yes, you can add the image to the test suite.</p>

---

## Post #16 by @fbudin69500 (2017-10-17 20:11 UTC)

<p>I created a patch for ITK. Let me know if that solves your problem:<br>
<a href="http://review.source.kitware.com/#/c/22723/" class="onebox" target="_blank" rel="nofollow noopener">http://review.source.kitware.com/#/c/22723/</a></p>

---

## Post #17 by @jcfr (2017-10-18 06:35 UTC)

<p>Thanks to <a class="mention" href="/u/fbudin69500">@fbudin69500</a> who work on the <a href="http://review.source.kitware.com/#/c/22723/">ITK fix</a>, this is fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26486">r26486</a> .</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09790b3e36ecefc192c8dfb84e02d9dd9d9ca0ab.png" alt="Screenshot from 2017-10-18 02-20-54" data-base62-sha1="1lNDdQ1OMa8Hr3dgZjSQTrhyqN5" width="483" height="436"></p>

---
