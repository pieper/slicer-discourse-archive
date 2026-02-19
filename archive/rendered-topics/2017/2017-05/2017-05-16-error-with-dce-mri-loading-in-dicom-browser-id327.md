---
topic_id: 327
title: "Error With Dce Mri Loading In Dicom Browser"
date: 2017-05-16
url: https://discourse.slicer.org/t/327
---

# ERROR with DCE MRI loading in DICOM Browser

**Topic ID**: 327
**Date**: 2017-05-16
**URL**: https://discourse.slicer.org/t/error-with-dce-mri-loading-in-dicom-browser/327

---

## Post #1 by @kirezgik (2017-05-16 17:23 UTC)

<p>Operating system: Microsoft Windows 7 Enterprise<br>
Slicer version: Slicer 4.7.0<br>
Expected behavior: Loading DCE MRI DICOM data using DICOM Browser or MultiVolume Importer<br>
Actual behavior: 	I have someT1 axial contrasted MRI image datasets. I imported them and can see in DICOM Browser series but it gives an error when I try to load. I used the DICOM browser,MultiVolume importer, also DATA load options to load the images, but none of them works. Also I have some DCE MRI images, but the software crashes whenever I try to load those DCE folders, which contain 1400 DICOM files in each.<br>
I`d apprecite your help.<br>
Thanks,<br>
Ezgi</p>

---

## Post #2 by @lassoan (2017-05-16 17:38 UTC)

<p>Use the latest nightly version.</p>
<p>To fix the crash when you load a large series, increase the amount of memory by either installing more physical memory in your computer or <a href="https://answers.microsoft.com/en-us/windows/forum/windows_7-performance/setting-up-proper-virtual-memory-windows-7-ult/8b6be428-faa1-4a72-8866-0ddc28a559de">increase virtual memory size</a> to 10x larger than the size of your data set.</p>
<p>Let us know if you still have problems.</p>

---

## Post #3 by @fedorov (2017-05-16 18:18 UTC)

<p>To the best of my knowledge, the only way to load a DCE MRI series as a dynamic 4-d series is to import it first into DICOM Browser, and then load using MultiVolumeImporter plugin.</p>
<p>After you import, when you click “Advanced” option and examine that DCE series in the DICOM Browser, do you see any loadables recognized as MultiVoumes?</p>

---

## Post #4 by @kirezgik (2017-05-16 20:10 UTC)

<p>Thanks for your quick replies.</p>
<p>The DCE data size is only 38 MB. I imported it first into <code>DICOM browser</code> and then loaded using <code>MultiVolumeImporter</code> plugin. The first image below shows when I import and examine it with <code>Advanced</code>option. And the second image shows when I load it.</p>
<p>As I realized that is a DWI volume file, even though it is saved as DCE volume file. So afterwards I tried to import it using <code>Diffusion-Weighted DICOM Import(DWI Convert)</code> plugin but it gives the error you can see in the third image(text only) below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e868234df28bb105e75e02bdc303fa210dae97d2.png" data-download-href="/uploads/short-url/x9XT1RY0Gg8URqPM3hiQUyixEyu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e868234df28bb105e75e02bdc303fa210dae97d2_2_690x417.png" alt="image" data-base62-sha1="x9XT1RY0Gg8URqPM3hiQUyixEyu" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e868234df28bb105e75e02bdc303fa210dae97d2_2_690x417.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e868234df28bb105e75e02bdc303fa210dae97d2_2_1035x625.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e868234df28bb105e75e02bdc303fa210dae97d2_2_1380x834.png 2x" data-dominant-color="E9EAEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1386×839 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/a7c481e3cad3ad17c9457ed6834ef2aaa1e1fc51.jpg" data-download-href="/uploads/short-url/nW8KFkXA5onJWvZ1BVK4clAu6PL.jpg?dl=1" title="MultiVolumeImporter plugin_imageview.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a7c481e3cad3ad17c9457ed6834ef2aaa1e1fc51_2_690x413.jpg" width="690" height="413" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a7c481e3cad3ad17c9457ed6834ef2aaa1e1fc51_2_690x413.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a7c481e3cad3ad17c9457ed6834ef2aaa1e1fc51_2_1035x619.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a7c481e3cad3ad17c9457ed6834ef2aaa1e1fc51_2_1380x826.jpg 2x" data-dominant-color="797980"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MultiVolumeImporter plugin_imageview.jpg</span><span class="informations">1724×1033 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>  </p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e759a3e1de6dd5b05bbb24c1413258c76d8702a8.png" data-download-href="/uploads/short-url/x0ClCWOIUS8j4j00OOqXGmpGvI4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e759a3e1de6dd5b05bbb24c1413258c76d8702a8.png" alt="image" data-base62-sha1="x0ClCWOIUS8j4j00OOqXGmpGvI4" width="523" height="500" data-dominant-color="F8F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">583×557 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2017-05-16 20:30 UTC)

<p>Disable the DICOMDiffusionVolumePlugin and try to load the series again.</p>

---

## Post #6 by @lassoan (2017-05-16 20:38 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> Volumes are getting misclassified as DWI volumes too frequently. Could you move the diffusion plugin to the diffusion extension? Let me know if there is any technical difficulty with that or you need help.</p>

---

## Post #7 by @kirezgik (2017-05-16 22:29 UTC)

<p>Disabling the DICOMDiffusionVolumePlugin did not help, either. What are the other causes that could be related with this issue?</p>

---

## Post #8 by @lassoan (2017-05-17 01:13 UTC)

<p>Unfortunately, DICOM storage of both DWI and DCE volumes are implemented in different ways by each vendor. Probably yours is just another variant. To make sure Slicer can load it properly, we would need at least one sample data set, preferably a phantom scan (if you don’t have that, then an anonymized patient data set may work, too).</p>

---

## Post #9 by @fedorov (2017-05-17 02:23 UTC)

<p>I am a bit unclear what you are trying to achieve.</p>
<p>You said it is loaded as a multivolume using the corresponding plugins, is this correct? If yes, you can then use multi volume explorer plugin to look at the b-value signal curves, and you can use DWModeling module [1] from the SlicerProstate extension to fit different diffusion models to the data. What do you want to do with the data?</p>
<p>[1] <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DWModeling">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DWModeling</a></p>

---

## Post #10 by @kirezgik (2017-05-17 23:31 UTC)

<p>Sure I can send you a sample data set.<br>
It is loaded as a multivolume but the axial image can not be scrolled, it shows only 1 image. And sagittal and coronal images look like a streak, as you can see in the image above I sent to here before. What we want to do with the data is to do the quantitative analysis and measure parameters like transfer constant and fractional value using DCE MRI.</p>

---

## Post #11 by @fedorov (2017-05-18 13:58 UTC)

<p>Thanks for the clarification. Indeed, I don’t see an easy way to debug this issue without a sample dataset.</p>
<p>Make sure you deidentify the data before sharing it.</p>

---

## Post #12 by @kirezgik (2017-05-18 15:35 UTC)

<p>Hope this helps to solve the issue.<br>
Thanks.</p>
<p><a href="https://mdacc.box.com/s/bj5p5nwm1bycldey1vr4n1or8jygk8aq" class="onebox" target="_blank" rel="nofollow noopener">https://mdacc.box.com/s/bj5p5nwm1bycldey1vr4n1or8jygk8aq</a></p>

---

## Post #13 by @lassoan (2017-05-18 19:50 UTC)

<p>I got the message “The item you are trying to access has either been deleted or unavailable to you”. But it’s more important for <a class="mention" href="/u/fedorov">@Fedorov</a> to get it, so if he downloaded it successfully then it should be enough for now.</p>

---

## Post #14 by @fedorov (2017-05-18 20:52 UTC)

<p>After a followup with <a class="mention" href="/u/kirezgik">@kirezgik</a>, I confirm I was able to download the dataset, and reproduce the problem. It is not something obvious to me, so I can’t fix it quickly. I will update this thread when I had time to investigate. Thank you for sharing the sample dataset!</p>

---

## Post #15 by @fedorov (2017-05-18 21:15 UTC)

<aside class="quote no-group" data-username="kirezgik" data-post="10" data-topic="327">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kirezgik/48/202_2.png" class="avatar"> kirezgik:</div>
<blockquote>
<p>It is loaded as a multivolume but the axial image can not be scrolled, it shows only 1 image.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/kirezgik">@kirezgik</a> just to clarify - for the data that you sent to me, I am not able to load it as a multivolume at all (see error popup below). Can you confirm the behavior is the same on your end? I want to make sure I am debugging the same issue that you experience. Perhaps there are two issues I need to investigate, but I can only reproduce this one.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b4bb91addd7ee035af42a498f26e7785e85882a.png" alt="image" data-base62-sha1="d1DGvX85rMKFicGGClvfrS7Ix0m" width="429" height="157"></p>

---

## Post #16 by @kirezgik (2017-05-18 21:20 UTC)

<p>Yes it behaves the same and this error pops up when I use DICOM browser to load.  But I could import and visualize the data using MultiVolume Importer plugin.</p>

---

## Post #17 by @fedorov (2017-05-18 21:33 UTC)

<p>Ah, I see, thanks! I was confused, because you are referring to the MultiVolume Importer module. That module is intended to import multivolume data that is not in DICOM format (ie, when each individual volume is stored in a research format, such as NRRD). So the behavior you observe is expected (or, to be more precise, not unexpected). Thank you for the clarification.</p>

---

## Post #18 by @fedorov (2017-05-19 03:16 UTC)

<p>I spent some time looking into this problem, but did not find the solution yet.</p>
<p>The issue appears to be not in MultiVolume related code, but in loading individual time frames of the DCE series. The multivolume frames are separated by TriggerTime in this dataset. If I take just the instances of the first frame, they fail to load as a Scalar Volume. The ScalarVolume plugin does not report any warnings and confirms that spacing between slices is consistent within the machine error. Here are the values for ImagePositionPatient:</p>
<pre><code class="lang-auto">(0020,0032) DS [-20\15\-5.559591]                       #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\-4.250905]                       #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\-2.942219]                       #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\-1.633533]                       #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\-0.3248464]                      #  18, 3 ImagePositionPatient
(0020,0032) DS [-20\15\0.9838399]                       #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\2.292526]                        #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\3.601213]                        #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\4.909899]                        #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\6.218585]                        #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\7.527271]                        #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\8.835958]                        #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\10.14464]                        #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\11.45333]                        #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\12.76202]                        #  16, 3 ImagePositionPatient
(0020,0032) DS [-20\15\14.0707]                         #  14, 3 ImagePositionPatient
</code></pre>
<p>However, loading of the scalar volume fails at the archetype level at this line: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L298">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L298</a></p>
<p>With this error in the error log: “A spacing of 0 is not allowed: Spacing is [0.3125, 0.3125, 0]”. I can’t understand why it comes up as 0 in the archetype reader!</p>
<p><a class="mention" href="/u/pieper">@pieper</a> can you take a look into this?</p>

---

## Post #19 by @pieper (2017-05-19 14:28 UTC)

<p>On a debug build this data crashes in an assert in GDCM.  This indicates there’s something pretty wrong with the data and probably the 0 spacing is a side effect.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/600b5b9370522db2b977e580de4dea18ba76c928.png" data-download-href="/uploads/short-url/dHEaBbcTX5H2O9eBd7tS5fMBvLi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/600b5b9370522db2b977e580de4dea18ba76c928_2_690x379.png" alt="image" data-base62-sha1="dHEaBbcTX5H2O9eBd7tS5fMBvLi" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/600b5b9370522db2b977e580de4dea18ba76c928_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/600b5b9370522db2b977e580de4dea18ba76c928_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/600b5b9370522db2b977e580de4dea18ba76c928_2_1380x758.png 2x" data-dominant-color="EAEAE8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1614×887 387 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @fedorov (2017-05-19 15:10 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thanks! Do you know which tag it is failing to read?</p>
<p>No idea how after all those years it didn’t occur to me to run a validator on this dataset! It seems that this dataset may have been generated on a preclinical system, and those are notorious for their non-compliance to the standard.</p>
<p>Indeed, <a href="http://www.dclunie.com/dicom3tools/dciodvfy.html">dciodvfy</a> gives a lot of errors.</p>
<pre><code class="lang-auto">(0x0019,0x108d)  ?  - Warning - Unrecognized tag - assuming explicit value representation OK
Error - Pixel Aspect Ratio may not be present when it has a ratio of 1:1 - values are 31\31
Warning - Value dubious for this VR - (0x0008,0x1060) PN Name of Physician(s) Reading Study  PN [0] = &lt;saif&gt; - Retired Person Name form
Warning - Value dubious for this VR - (0x0008,0x1070) PN Operators' Name  PN [0] = &lt;saif&gt; - Retired Person Name form
Error - Value invalid for this VR - (0x0010,0x0030) DA Patient's Birth Date  DA [0] = &lt;00010101&gt; - Character invalid for this VR = '0' (0x30)
Error - Dicom dataset contains invalid data values for Value Representations
MRImage
Warning - is only permitted to be empty when actually unknown; should be absent (not empty) if an unpaired body part, and have a value if a paired body part - attribute &lt;Laterality&gt;
Error - May not be present when Pixel Spacing is present - attribute &lt;PixelAspectRatio&gt;
Error - A value is required for value 3 in MR Images - attribute &lt;ImageType&gt;
Error - Attribute present when condition unsatisfied (which may not be present otherwise) Type 2C Conditional Element=&lt;InversionTime&gt; Module=&lt;MRImage&gt;
Error - Attribute present when condition unsatisfied (which may not be present otherwise) Type 2C Conditional Element=&lt;TriggerTime&gt; Module=&lt;MRImage&gt;
</code></pre>
<p>Even after I manually cleaned up most of the issues, to make dciodvfy complain about the following only</p>
<pre><code class="lang-auto">MRImage
Warning - is only permitted to be empty when actually unknown; should be absent (not empty) if an unpaired body part, and have a value if a paired body part - attribute &lt;Laterality&gt;
</code></pre>
<p>I am still not able to load it as a scalar volume into Slicer!</p>

---

## Post #22 by @kirezgik (2017-05-19 15:39 UTC)

<p>Thank you all <a class="mention" href="/u/fedorov">@fedorov</a>, <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for your helps.  In the meanwhile, I have realized that not only DCE but also other sequences, like T1 FS+C, for this case can not be loaded into Slicer. But i can display the images in a different software.<br>
The dataset have been generated on a preclinical system, as you figured, so I will contact with someone who generated the data and get more detailed information about it.</p>

---

## Post #23 by @pieper (2017-05-19 15:48 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> yes, the tag it complains about is LossyImageCompression,<br>
0x0028,0x2110.  But the value looks okay to me (“00”) and since this isn’t<br>
one that that dciodvfy complains about so I suspect the actual issue is<br>
something else.</p>

---

## Post #24 by @fedorov (2017-05-19 15:56 UTC)

<p>Works just fine in OsiriX!</p>
<p><a class="mention" href="/u/kirezgik">@kirezgik</a> yes, you should report that the data generated by the system is not standard-compliant, please do that, but I don’t expect a quick fix.</p>
<p>Since it works in OsiriX, it must be possible to figure out how to make it work in Slicer, it’s just a matter of resources. I don’t have a lot of time to spend on this today.</p>
<p>Do you know if I can make your dataset public? We could share it with the ITK/GDCM developers, since the problem is outside of Slicer really (but Slicer should rightfully take the full blame for the dataset not loading!)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea19a1633c0b1f2e02269d0e75ba32c8de5528a2.png" data-download-href="/uploads/short-url/xoWDK24bEFaLP0MVXUAWOT1gkxA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea19a1633c0b1f2e02269d0e75ba32c8de5528a2_2_690x290.png" alt="image" data-base62-sha1="xoWDK24bEFaLP0MVXUAWOT1gkxA" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea19a1633c0b1f2e02269d0e75ba32c8de5528a2_2_690x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea19a1633c0b1f2e02269d0e75ba32c8de5528a2_2_1035x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea19a1633c0b1f2e02269d0e75ba32c8de5528a2.png 2x" data-dominant-color="404341"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1253×528 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #25 by @lassoan (2017-05-19 16:07 UTC)

<p>Is it possible that the image is compressed?</p>
<p>You may also try to run Slicer’s DICOM patcher on it (although it does not contain fixes related to the specific errors that are reported).</p>

---

## Post #26 by @pieper (2017-05-19 16:10 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> - I agree, this is certainly fixable with some time and effort.<br>
It would be good to see if we can replicate the issue in pure ITK.</p>

---

## Post #27 by @pieper (2017-05-19 16:29 UTC)

<p>I tried the DICOMPatcher and it didn’t solve the issue.</p>

---

## Post #28 by @kirezgik (2017-05-19 22:28 UTC)

<p>I<code>ve just shared the</code>anonymized` data set with you to share it with the ITK/GDCM developers. Hope it helps.</p>

---

## Post #29 by @fedorov (2017-05-21 03:43 UTC)

<p>I reproduced the problem using pure ITK (the version that is used by Slicer).</p>
<p>The repo to reproduce the problem is here: <a href="https://github.com/fedorov/itk-gdcm-dcmtk-readers">https://github.com/fedorov/itk-gdcm-dcmtk-readers</a></p>
<p>GDCM reader fails with the same error as in Slicer:</p>
<pre><code class="lang-auto">Exception thrown while reading the series

itk::ExceptionObject (0x7ff2538696d8)
Location: "virtual void itk::ImageBase&lt;3&gt;::ComputeIndexToPhysicalPointMatrices() [VImageDimension = 3]"
File: /Users/fedorov/local/builds/Slicer4-Release/ITKv4/Modules/Core/Common/include/itkImageBase.hxx
Line: 187
Description: itk::ERROR: Image(0x7ff253873c90): A spacing of 0 is not allowed: Spacing is [0.3125, 0.3125, 0]
</code></pre>
<p>DCMTK reader works just fine, and results in a volume with slice thickness 1.3, as expected.</p>
<p>I will follow up with the ITK folks, but this experience, once again, begs the question - why do we rely in ITK and Slicer on GDCM and not on DCMTK?</p>

---

## Post #30 by @fedorov (2017-05-21 04:10 UTC)

<p>ITK issue reported: <a href="https://issues.itk.org/jira/browse/ITK-3546">https://issues.itk.org/jira/browse/ITK-3546</a></p>
<p>Sample dataset shared by <a class="mention" href="/u/kirezgik">@kirezgik</a> uploaded here: <a href="https://github.com/fedorov/itk-gdcm-dcmtk-readers/releases/download/gdcm_fails/GDCM_fails.zip">https://github.com/fedorov/itk-gdcm-dcmtk-readers/releases/download/gdcm_fails/GDCM_fails.zip</a></p>
<p>CC: <a class="mention" href="/u/thewtex">@thewtex</a></p>

---

## Post #31 by @fedorov (2017-05-25 13:46 UTC)

<p><a class="mention" href="/u/kirezgik">@kirezgik</a> are you able to build Slicer from source, or you only use the downloaded binaries?</p>
<p>I have a modified version of code that works for your dataset, but other people have concerns about integrating that solution into the main application, so I need to work on another approach.</p>

---

## Post #32 by @kirezgik (2017-05-26 16:35 UTC)

<p>I only use the downloaded binaries. But if building from source helps, we might try to do that.</p>

---

## Post #33 by @fedorov (2017-05-29 13:49 UTC)

<p><a class="mention" href="/u/kirezgik">@kirezgik</a> I feel sorry to ask you to build it, since it might be easier for me to implement this feature in the extension, than for you to build Slicer. I think it is too much trouble for you. I am not sure if I can get to it this week, but if not then next week for sure.</p>

---

## Post #34 by @zp12132016 (2017-05-29 14:28 UTC)

<p>Hi Andrey,</p>
<p>Thanks very much for your fast reply, No problem, I can build it again.</p>
<p>Best regards</p>
<p>Zen</p>

---

## Post #35 by @fedorov (2017-05-29 14:42 UTC)

<p><a class="mention" href="/u/zp12132016">@zp12132016</a> this is the branch that contains the fix that should allow loading of the DCE dataset <a class="mention" href="/u/kirezgik">@kirezgik</a> shared earlier: <a href="https://github.com/fedorov/slicer/tree/dcmtk-for-scalar-volume">https://github.com/fedorov/slicer/tree/dcmtk-for-scalar-volume</a></p>

---

## Post #36 by @zp12132016 (2017-05-29 15:23 UTC)

<p>Hi Andrey,</p>
<p>Thanks for your active reply!</p>
<p>I am trying to built the slicer again, currently I am using slicer version 4.6.2 and Viusal studio 2013 desktop with update 5, Qt 4.8.7 and CMake 3.8.1</p>
<p>Do you think  I need to try different version of slicer?</p>
<p>For the branch you mentioned below, how to put it in build slicer?</p>
<p>Best regards</p>
<p>Zen</p>

---

## Post #37 by @fedorov (2017-05-29 15:52 UTC)

<p>You will have to check out the branch I mentioned above from GitHub, and build Slicer from scratch. Looking at the instructions [1], your setup should work.</p>
<p>[1] <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows</a></p>

---

## Post #38 by @kirezgik (2017-06-02 20:15 UTC)

<p>Hi,<br>
We tried the instructions for setup, but can not unzip Cmake and Qt folders in common prerequisites.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a19299c6a28eab9019cb0c54410ac728b7a6f6fa.png" data-download-href="/uploads/short-url/n3kXINgdc0iwCxM4YlnDl0aJStA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a19299c6a28eab9019cb0c54410ac728b7a6f6fa_2_690x457.png" alt="image" data-base62-sha1="n3kXINgdc0iwCxM4YlnDl0aJStA" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a19299c6a28eab9019cb0c54410ac728b7a6f6fa_2_690x457.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a19299c6a28eab9019cb0c54410ac728b7a6f6fa.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a19299c6a28eab9019cb0c54410ac728b7a6f6fa.png 2x" data-dominant-color="EBEDF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1026×681 77.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99282dd6e959a19167ab7a77b4d3c0b8a374c354.png" data-download-href="/uploads/short-url/lQT8rCMedZKviWj6ijX6BadTmbW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99282dd6e959a19167ab7a77b4d3c0b8a374c354_2_690x426.png" alt="image" data-base62-sha1="lQT8rCMedZKviWj6ijX6BadTmbW" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99282dd6e959a19167ab7a77b4d3c0b8a374c354_2_690x426.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99282dd6e959a19167ab7a77b4d3c0b8a374c354.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99282dd6e959a19167ab7a77b4d3c0b8a374c354.png 2x" data-dominant-color="EBEEF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1020×630 73.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #39 by @lassoan (2017-06-02 20:35 UTC)

<p>Do you have CMake running? Do you have any anti-virus software that may prevent extraction of executable files? Can you extract the files in your user directory or desktop?</p>

---

## Post #40 by @kirezgik (2017-06-06 17:31 UTC)

<p>We had CMake run and tried to extract the files in desktop but it gives these errors:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b0d4455960459e831ae1c1527c4f19e38bf36d4.png" data-download-href="/uploads/short-url/cZtSbXzyAuWsOGirBvEMKxl1Qi0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b0d4455960459e831ae1c1527c4f19e38bf36d4.png" alt="image" data-base62-sha1="cZtSbXzyAuWsOGirBvEMKxl1Qi0" width="590" height="500" data-dominant-color="F29E9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1051×890 45.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #41 by @fedorov (2017-06-07 15:30 UTC)

<p>We are moving forward with the implementation discussed in this thread: <a href="https://discourse.slicer.org/t/slicer-dicom-scalar-volume-plugin-relies-on-old-gdcm-why-do-we-not-use-dcmtk/354/15">Slicer DICOM Scalar volume plugin relies on (old) GDCM: why do we not use DCMTK?</a></p>
<p>We should hopefully have it in the application sometime soon. I will followup with <a class="mention" href="/u/pieper">@pieper</a> later this week. I think fixing this  problem of failing read of scalar volume in the Slicer application should be done no matter what.</p>

---

## Post #42 by @fedorov (2017-06-17 01:50 UTC)

<p>You can monitor this pull request: <a href="https://github.com/Slicer/Slicer/pull/734">https://github.com/Slicer/Slicer/pull/734</a>. Once it is merged,  loading of your dataset should work in the nightly.</p>

---

## Post #43 by @fedorov (2017-06-25 11:27 UTC)

<p><a class="mention" href="/u/kirezgik">@kirezgik</a> the issue you identified should be fixed in today’s nightly of Slicer. At least I can say I am able to load the dataset you shared without problems.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/1eb56d1a223c1f9abc96fcc1b4c022302a684c1d.png" data-download-href="/uploads/short-url/4nF1Ji5p0reYbmPSTZLygzeYbyl.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1eb56d1a223c1f9abc96fcc1b4c022302a684c1d_2_648x499.png" width="648" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1eb56d1a223c1f9abc96fcc1b4c022302a684c1d_2_648x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1eb56d1a223c1f9abc96fcc1b4c022302a684c1d_2_972x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1eb56d1a223c1f9abc96fcc1b4c022302a684c1d_2_1296x998.png 2x" data-dominant-color="C4C4C3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1842×1420 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #44 by @kirezgik (2017-06-26 15:54 UTC)

<p>That`s great! Yes, it is working now. I am able to load the dataset and visualize it in all 3 planes as a dynamic view without problems.</p>
<p>Thank you <a class="mention" href="/u/fedorov">@fedorov</a> for all your help, and <a class="mention" href="/u/lassoan">@lassoan</a> , <a class="mention" href="/u/pieper">@pieper</a>! I appreciate your interest and hard work since the beginning of my support request.  I will update you about the implementation as I move forward with the analysis.</p>
<p>Best,<br>
Ezgi</p>

---

## Post #45 by @malaterre (2017-08-31 07:20 UTC)

<p>Dear <a class="mention" href="/u/kirezgik">@kirezgik</a> , I am one of the author of GDCM. I have been starring at your DICOM datasets and they seems to suffer from a rather large issue from a DICOM point of view. This is the first time I am seeing this from a DICOM DataSet in the wild. Could you please confirm that this data is coming from a real modality (not some kind of experimental project) ? If so I’d like to contact the vendor about their failure to follow the standard. Ideally I would need a copy of the original DataSet. Thanks.</p>

---

## Post #46 by @kirezgik (2017-09-13 16:19 UTC)

<p>Hi <a class="mention" href="/u/malaterre">@malaterre</a>, thanks for your interest about this topic. The data is coming from an experimental project, it is not a clinical data. What is the issue you realized? I can let the vendor know about it. Also I can share the original DataSet if you provide me your email. Thanks.</p>

---
