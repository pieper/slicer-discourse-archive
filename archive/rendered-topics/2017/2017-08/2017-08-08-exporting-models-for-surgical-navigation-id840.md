# Exporting models for surgical navigation

**Topic ID**: 840
**Date**: 2017-08-08
**URL**: https://discourse.slicer.org/t/exporting-models-for-surgical-navigation/840

---

## Post #1 by @drpreezy (2017-08-08 11:06 UTC)

<p>Operating system: WINDOWS<br>
Slicer version:4.6.2<br>
Expected behavior:<br>
First and foremost, thank you for the outstanding work with 3DSlicer, it has been very useful in my research.</p>
<p>I am currently taking DICOM data from CT scans, converting into STL to work with implants that (as you know) usually come in STL format. However, I am having some issues figuring out what is the most efficient way of then re-converting the “planned” surgery model into a DICOM. I have read some of the posts on the wiki/blogs that you guys have posted, but I am still a bit confused about how to define those optimal volumes. The goal of converting back to DICOM is to be able to display it on a surgical planning/navigation device. Is there any easy way to do this?</p>
<p>In a 2013 post (<a href="http://slicer-users-archive.65878.n3.nabble.com/STL-model-to-dicom-td4025720.html" rel="nofollow noopener">http://slicer-users-archive.65878.n3.nabble.com/STL-model-to-dicom-td4025720.html</a>) you referred to: <a href="https://www.slicer.org/wiki/Documentation/4.2/Modules/ModelToLabelMap" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.2/Modules/ModelToLabelMap</a></p>
<p>Any other leads I could use?</p>
<p>Many thanks,<br>
Best wishes,<br>
Actual behavior: STL to DICOM conversion is not always reliable using the method that I am using.</p>

---

## Post #2 by @lassoan (2017-08-08 12:05 UTC)

<p>What navigation system do you  use? How would you like your volumes to be exported: as RT structure sets, segmentation objects, or fake CT volumes?</p>
<p>Use the latest nightly version of Slicer and try to follow these instructions: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export</a></p>

---

## Post #3 by @pieper (2017-08-08 12:09 UTC)

<p>Also see this tutorial for information about how to bring existing stl files aa segmentations (that can be converted to/from surface and labelmap formats):</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation_for_3D_printing" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation_for_3D_printing</a></p>

---

## Post #4 by @drpreezy (2017-08-16 07:19 UTC)

<p>Hi Andras,</p>
<p>I am using Medtronic’s StealthStation7. The goal here would be to get the CT scan of the patient (DICOM) convert into STL (straightforward) and then use implants or play with the reconstructed CT to prepare for surgery. Once that is done I want to be able to re-upload the STL file as a DICOM to be able to Navigate the surgery. Hence, maybe fake CT volumes is the way to go?<br>
As of now, aside from the things that I mentioned, I also tried to upload a “black volume” made of 150-200slices approx, to load the stl, label to volume module, and after that I created the DICOM series. This doesn’t work great as when I load it into the StealthStation the results appear as white borders on a black screen… What do you reckon would be the best way to go given the overarching goal of planning surgeries using both the original CT image, STL from implant/prosthetic manufacturers and then wanting to export it as a DICOM?</p>
<p>Many thanks,<br>
Best wishes,</p>

---

## Post #5 by @drpreezy (2017-08-16 07:26 UTC)

<p>Hi Steve,</p>
<p>I checked out the tutorial. It is a very powerful tool, however, the result is exported as an STL file for 3D printing (which is the conventional way of doing things and what makes sense for 3D printing) <a href="https://www.youtube.com/watch?v=Uht6Fwtr9hE" rel="nofollow noopener">https://www.youtube.com/watch?v=Uht6Fwtr9hE</a></p>
<p>The issue I have comes from when I want to re-import the results into a navigation system (in my case Medtronic’s StealthStation) which doesn’t support STL files for navigation. It requires the use of DICOM to be able to navigate the surgery.<br>
Many thanks,<br>
Cheers,</p>

---

## Post #6 by @lassoan (2017-08-16 13:38 UTC)

<p>You could generate fake CTs and relatively easily create model from them on the StealthStation (using direct volume rendering or segmenting with simple tresholding). However, it would be just a workaround and you would still need to redo the trajectory planning and would be limited to what StealthStation can do.</p>
<p>For exploring new surgical navigation techniques, you may use Slicer in the operating room. Slicer can receive registration and real-time tool positions from StealthStation and display it in real-time. See this demo for an example: <a href="https://youtu.be/UHmv5u-sB5g">https://youtu.be/UHmv5u-sB5g</a> (left monitor is Slicer, right monitor is StealthStation). There is no visible time delay, no need for additional hardware, no need for repeating registration (Slicer retrieves patient registration automatically). Slicer can also retrieve the current planning image from the StealthStation, so you don’t need to set up DICOM networking or run around with USB sticks if you acquire real-time images with an O-arm and want to use that in Slicer.</p>
<p>Overall, if you use StealthStation and Slicer together then you can rely on a commercial navigation system (tracker, tools, patient registration, …) as usual, but in addition to that benefit from lots of advanced features and flexibility of Slicer - advanced registration, segmentation methods, image fusion with pre-operative or real-time intraoperative image registration (ultrasound, surface scans, optical spectroscopy, etc), display of custom tools, implants, interface with robotic devices, etc. See <a href="http://www.slicerigt.org">www.slicerigt.org</a> and <a href="http://www.plustoolkit.org">www.plustoolkit.org</a> for more details or check out our lab’s Youtube channel at <a href="https://www.youtube.com/user/perklabresearch">https://www.youtube.com/user/perklabresearch</a>. These tools are all freely available and used under IRB approval for several procedures.</p>

---

## Post #7 by @drpreezy (2017-08-17 06:41 UTC)

<p>Hi Andras,</p>
<p>Thank you for your detailed response. It was really helpful. I’ll try both approaches with a demo programmed surgery and see what works better given our pipeline of navigated surgical products and based on surgical needs. Very interesting work on augmented reality for musculoskeletal injections! Many thanks,</p>

---
