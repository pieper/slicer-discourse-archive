# Trying to load RTStruct dicom file but tool crashes

**Topic ID**: 13177
**Date**: 2020-08-26
**URL**: https://discourse.slicer.org/t/trying-to-load-rtstruct-dicom-file-but-tool-crashes/13177

---

## Post #1 by @Gabriel_T (2020-08-26 13:20 UTC)

<p>Hi All,</p>
<p>I have a binary segmentation mask which I converted to nifti format and using the original dicom files I converted that to an RTStruct dicom file.</p>
<p>But when I try to load the RTStruct file it crashes the tool. I tried to load it by dragging and dropping the folder containing the dicom files and the RTstruct file, when I do so it asks me if I want to load the RTstruct or some other referenced dataset <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34de1a5385f6882ba4302f6968984c46f906ba24.png" data-download-href="/uploads/short-url/7xGGg3DkY8ouCVzr4J9XHNJ0Wq0.png?dl=1" title="slicer3derr" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/34de1a5385f6882ba4302f6968984c46f906ba24_2_690x479.png" alt="slicer3derr" data-base62-sha1="7xGGg3DkY8ouCVzr4J9XHNJ0Wq0" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/34de1a5385f6882ba4302f6968984c46f906ba24_2_690x479.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/34de1a5385f6882ba4302f6968984c46f906ba24_2_1035x718.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/34de1a5385f6882ba4302f6968984c46f906ba24_2_1380x958.png 2x" data-dominant-color="EDF0F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer3derr</span><span class="informations">2255×1568 422 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I select the RTStruct option, it tries to load it but then the software crashes when the progress bar is at 50%</p>

---

## Post #2 by @Sunderlandkyl (2020-08-26 13:31 UTC)

<p>I can take a look at it. Can you upload the RTSTRUCT somewhere and send me a message with a link to it?</p>

---

## Post #3 by @cpinter (2020-08-26 13:36 UTC)

<p><a class="mention" href="/u/gabriel_t">@Gabriel_T</a> I see from the screenshot that you probably use a not so recent version. Can you please try the latest nightly? (<a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> please hold until this is confirmed).<br>
Thanks!</p>

---

## Post #4 by @Gabriel_T (2020-08-31 00:40 UTC)

<p>Thanks for the response, I tried out the latest preview build , now it doesnt crash, but slicer3d still isnt loading anything.</p>

---

## Post #5 by @cpinter (2020-08-31 08:07 UTC)

<aside class="quote no-group" data-username="Gabriel_T" data-post="4" data-topic="13177">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gabriel_t/48/4222_2.png" class="avatar"> Gabriel_T:</div>
<blockquote>
<p>slicer3d still isnt loading anything.</p>
</blockquote>
</aside>
<p>If you provide more information we might be able to help. What do you do exactly? What do you expect to happen? What happens instead? An error log is also useful. Thank you.</p>

---

## Post #6 by @Gabriel_T (2020-08-31 14:39 UTC)

<p>Thanks for the response.</p>
<p>I had generated a segmentation mask in the form of a numpy array, I was trying to load this segmentation mask in Slicer3D so I converted the numpy array to an RTStruct file. I’m not sure if I constructed the right RTStruct file or what may be wrong with it. Please can you advice ? I was trying to load the generated segmentation masks onto slicer3D for editing and viewing.</p>

---

## Post #7 by @cpinter (2020-08-31 14:46 UTC)

<p>So the one thing I now know is that you exported an RT structure set using Slicer and tried to load it.</p>
<p>Then what happens? Please describe the <em>exact steps</em> you take before you encounter the problem you mentioned. Also as I said please include an error log. Thanks!</p>

---

## Post #8 by @Gabriel_T (2020-08-31 14:55 UTC)

<p>Steps taken -<br>
Dragged folder containing dicom files and RTStruct file to Slicer<br>
It loads the folder in, then in Dicom Database I select the Series with RTSTRUCT Modality. When I do so it loads nothing, all I see are empty axial, coronal, saggital images (black images).<br>
Here is the error log -</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\gabri\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-29\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMBrowser.py”, line 221, in timerCallback<br>
self.promptForExtensions()<br>
File “C:\Users\gabri\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-29\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMBrowser.py”, line 226, in promptForExtensions<br>
extensionsToOffer = self.checkForExtensions()<br>
File “C:\Users\gabri\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-29\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMBrowser.py”, line 289, in checkForExtensions<br>
instance0 = slicer.dicomDatabase.filesForSeries(series)[0]<br>
IndexError: tuple index out of range</p>

---

## Post #9 by @cpinter (2020-08-31 15:09 UTC)

<p>Thank you for the details!</p>
<p>When you exported the dataset it also exported an anatomical volume alongside the RTSS. If you try to load the whole study with both series, do you still have the same problem?</p>

---

## Post #10 by @Gabriel_T (2020-08-31 15:17 UTC)

<p>When I loaded the whole study with both the CT modality and the RTStruct modality I still get empty images</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\gabri\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-29\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 675, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
File “C:/Users/gabri/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-29/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 112, in examine<br>
loadables += self.examineFilesIPPAcqTime(files)<br>
File “C:/Users/gabri/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-29/bin/…/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 343, in examineFilesIPPAcqTime<br>
desc = slicer.dicomDatabase.fileValue(files[0],self.tags[‘seriesDescription’]) # SeriesDescription<br>
IndexError: tuple index out of range<br>
DICOM Plugin failed: tuple index out of range</p>

---

## Post #11 by @cpinter (2020-08-31 15:23 UTC)

<p>Can you share this dataset with us so we can try?</p>

---

## Post #12 by @cpinter (2020-08-31 16:42 UTC)

<p>Thanks for sharing it! I was also not able to load the structure set. However I don’t see the error messages you pasted. What I receive are error logs such as</p>
<p><code>LoadContour: Contour sequence object item is invalid:  number of contour points is 51 therefore expected 153 values in contour data but only found 51</code></p>
<p>I did a segmentation on the CT you provided using Segment Editor, exported the result in DICOM-RT, and managed to load it back.</p>
<ol>
<li>Did you do the segmentation in Segment Editor?</li>
<li>What kind of structures did you segment? For example were they very small/thin?</li>
<li>How did you export the dataset?</li>
</ol>

---

## Post #13 by @lassoan (2020-08-31 19:41 UTC)

<p>Also note that if you use DICOM RT structure set because you just want to import planar contours, then you don’t need to go through DICOM. Instead, you can directly create planar contours segmentation representation using a simple Python script, as it is done in Slicer’s OsiriX segmentation importer (<a href="https://github.com/PerkLab/SlicerSandbox/tree/master/ImportOsirixROI">ImportOsirixROI module</a> in Sandbox extension).</p>
<p>By the way, using planar contours for representing 3D segmentation is not a good idea. There is just too much difficulty and uncertainty creating a 3D shape from cross-sections and it does not work for arbitrarily complex shapes.</p>

---

## Post #14 by @Gabriel_T (2020-08-31 22:59 UTC)

<p>I see those errors too, what could the reason be for expecting multiple of 3 values ?</p>
<ol>
<li>No the segmentation was generated through deep learning</li>
<li>Just the left ventricular wall, it was not small , it occupied about half the number of slices</li>
<li>The CT modality dicom files were directly from scanner, the RTStruct file I created using pydicom</li>
</ol>

---

## Post #15 by @lassoan (2020-08-31 23:59 UTC)

<aside class="quote no-group" data-username="Gabriel_T" data-post="14" data-topic="13177">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gabriel_t/48/4222_2.png" class="avatar"> Gabriel_T:</div>
<blockquote>
<p>I see those errors too, what could the reason be for expecting multiple of 3 values ?</p>
</blockquote>
</aside>
<p>You must have multiple of 3 values (each point is specified by 3 coordinates).</p>
<aside class="quote no-group" data-username="Gabriel_T" data-post="14" data-topic="13177">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gabriel_t/48/4222_2.png" class="avatar"> Gabriel_T:</div>
<blockquote>
<p>the segmentation was generated through deep learning</p>
</blockquote>
</aside>
<p>What is the output of the segmentation? Yes/no (or probability) for each voxel? If yes, then don’t bother with creating RTSTRUCT representation, but keep it as labelmap and save as DICOM Segmentation Object. Alternatively, you may choose to just save in a research format (nrrd or mha) and convert to DICOM in Slicer.</p>

---

## Post #16 by @cpinter (2020-09-01 07:56 UTC)

<aside class="quote no-group" data-username="Gabriel_T" data-post="14" data-topic="13177">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gabriel_t/48/4222_2.png" class="avatar"> Gabriel_T:</div>
<blockquote>
<p>No the segmentation was generated through deep learning</p>
</blockquote>
</aside>
<p>In this case the RTStruct file is probably not valid. As <a class="mention" href="/u/lassoan">@lassoan</a> says each point needs three coordinates, but apparently there is only one value. Maybe when you generated the values the coordinates were not separated. Consider this for example:</p>
<p><code>33.703125\-147.92120098039214\-193.0\33.36004901960784</code></p>
<p>Is it possible that the second and fourth values are actually three numbers that were not separated?</p>
<p>By the way, <a class="mention" href="/u/lassoan">@lassoan</a> is also right in that if you generate your segmentation with deep learning then you could use a much simpler format. RT structure set is an archaic format that introduces data loss because along one axis its resolution is very low, it does not handle holes or complex structures well, etc. You’d be better off using DICOM SEG, or nrrd.</p>

---

## Post #17 by @Gabriel_T (2020-09-01 15:25 UTC)

<p>Thanks for the suggestion, nrrd format works best for me, I was able to visualize the segmentations on slicer3d properly by importing the segmentation mask in .nrrd format as well as the dicom volume in the same .nrrd format</p>

---
