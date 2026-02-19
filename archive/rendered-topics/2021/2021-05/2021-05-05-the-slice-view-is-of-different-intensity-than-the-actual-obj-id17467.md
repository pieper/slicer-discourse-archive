---
topic_id: 17467
title: "The Slice View Is Of Different Intensity Than The Actual Obj"
date: 2021-05-05
url: https://discourse.slicer.org/t/17467
---

# The Slice view is of different intensity than the actual object

**Topic ID**: 17467
**Date**: 2021-05-05
**URL**: https://discourse.slicer.org/t/the-slice-view-is-of-different-intensity-than-the-actual-object/17467

---

## Post #1 by @pranaysingh (2021-05-05 12:29 UTC)

<p>Operating system: Linux Centos<br>
Slicer version: 4.11<br>
Expected behavior: I am trying to view the tooth. The 3D slicer loads the slice views with the intensity shown in the first image. As you can see the slice images for R, G and Y loaded in 3D slicer shows a unexpected black(dark) shaded region at the corner regions of the tooth.<br>
Actual behavior: The same set of dicom files loaded with other softwares such as Matlab or Dicom Browser on same OS loads the slices with accurate intensity across the whole tooth as shown in the second, third and fourth image, with white(bright) color corners. It is also to be noted that every other region of slice, loaded with any software including 3d Slicer has matching intensity, for example, areas in the background, central gray region of the tooth and the region at the middle.</p>
<p>I wanted to understand why is there an intensity difference in 3D slicer and that too only at the specified area, which is the boundary region, and everything else is looking fine.<br>
I would highly appreciate if someone could guide or point to something that I might change or tweak in any of the module to load my images with correct intensity in 3D slicer as well.</p>
<p>Thanks,<br>
Pranay<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/180e288e88b6c0ef3c2b97f6c83907b54f5fb2a4.png" alt="3Dslicer_image" data-base62-sha1="3qNNcvqQsMvlWyGnbaBNeCTQtpi" width="558" height="259"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17ba89fa2723286875a24956b786bc496fb0141d.png" alt="matlab_image1" data-base62-sha1="3nUDF6WGHfdS3O3dMMiz9fNaTQ9" width="401" height="373"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4c2e1f08fd295f06dfd79143d6a0dfdc258cb10.png" alt="matlab_image2" data-base62-sha1="pN5tG1XfCcOQqTmFOPBybDxOt56" width="535" height="478"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/561d63e29e93f5998b5f061079afccc0f8c2b95e.png" alt="matlab_image3" data-base62-sha1="chO1TI1wj2taqza42LSKPXQKsYS" width="517" height="441"></p>

---

## Post #2 by @pieper (2021-05-05 13:57 UTC)

<p>Where does the data come from, what format is it in, and what method do you use to load it in Slicer?</p>

---

## Post #3 by @mikebind (2021-05-05 18:30 UTC)

<p>That looks like an overflow or data type error.  If you load a image data as signed integers when they are supposed to be unsigned integers this kind of error can happen. For example, an unsigned 8-bit voxel can store values 0-255 (0 to 2^8-1), whereas a signed 8-bit voxel stores values -128 to 127 (-2^7 to 2^7-1).  The way it’s set up, values 0 to 127 are represented the same way whether the representation is signed or unsigned, so any gray values in that range look the same even if you use the wrong interpretation.  However, the representation for unsigned 128 is the same as the representation -128 (I think) for the signed version (because the leading bit is interpreted as indicating the sign instead of indicating a larger value).  The representation for unsigned representation 129 would then be -127, and so forth. So, voxel values which are greater than a threshold of 127 would suddenly look black because they would be interpreted as negative values. For 16-bit voxels, the threshold would be 32,767 (2^15-1, values greater than this become negative numbers when interpreted as signed).</p>
<p>I’ve seen things like this happen before with CT images with sharpening filters or metal artifacts which pushed some voxel values above the normal range of values and very dense areas turned black because the imaging software assumed signed integers and the values were actually supposed to be interpreted as unsigned integers.</p>
<p>This problem could arise by 1) the file you are loading from being ambiguous about whether values are signed or unsigned, or 2) because the loading software makes the wrong assumption, or 3) because the wrong values were stored originally because of a calculation overflow error.   In the first case, Slicer would need an adjustment to a heuristic or input from you to do the right thing; In the second case, Slicer might have a bug in interpreting a properly specified input or the input might not be properly specified (and the other software you use makes a beneficial assumption for your case).  In the third case, Slicer is doing the correct thing, and you need to fix your data (which is easy, just add 32,768 to any negative number and store as 16 bit unsigned instead of 16 bit signed).</p>

---

## Post #4 by @pranaysingh (2021-05-06 10:29 UTC)

<p>Hi, Thanks for the reply.<br>
The data is CT scan of our samples that was performed by a local lab in India.<br>
The format is Dicom. I loaded it in Slicer using GUI as…<br>
Module &gt; DICOM &gt; Import Dicom files &gt; then I imported the dicom directory from my system.<br>
To load it, I used, Module &gt; DICOM &gt; Show Dicom database &gt; then clicked on above imported database and click load tab.<br>
That’s the same way the documentation teaches.<br>
Then I can view all my slices as usual, or do volume rendering and everything. But couldn’t fix the problem stated in the question.</p>
<p>If there’s something wrong with the way to load or any further information required, kindly let me know.</p>
<p>Thanks,<br>
Pranay</p>

---

## Post #5 by @pranaysingh (2021-05-06 10:44 UTC)

<p>Hi, Thank you so much for replying back.</p>
<p>I gave a thought about the possibilities you suggested, indeed it could be one of the problems you mentioned. Thanks for shedding the light on that. I would like to mention a few more things:<br>
I was analyzing the slices in numpy array to see the pixel values, I couldn’t find any negative values in the array, suggesting that the values are unsigned.<br>
Also, when I analyzed the pixel values of same slice, exported via matlab, I noticed that there was a difference, For example, for gray region in the middle, in the matlab image, a pixel that has the intensity value of around say, 150. The same pixel in the image exported by 3D slicer will have the intensity of 150-127(=23) at that very location.</p>
<p>What could probably serve as a great convenience for me is, if there’s a way in 3D slicer where I can specify the data type(signed or unsigned) while loading the dicom files. If there’s an assumption made by the 3D slicer itself, I would like to override that assumption by explicitly specifying the correct data type. I couldn’t find any settings for that. If it’s there It would be lot helpful if you could point out the module.<br>
Even if there’s any additional observation you could make by above points, I would love to hear.</p>
<p>Thanks,<br>
Pranay</p>

---

## Post #6 by @mikebind (2021-05-06 15:32 UTC)

<p>If you have a data set which shows this issue without patient information (either a non-patient scan or a patient scan where all identifying information has been removed) that you can share, that would be helpful for figuring out what exactly is happening.</p>

---

## Post #7 by @pranaysingh (2021-05-07 09:26 UTC)

<p>Sure, Iike I can share a couple of my DICOM files, if you load in 3D slicer, you would be able to view the Axial view of the tooth as I posted in the screenshot in the question, with black colored corners. I hope that serves the purpose, let me know for the additionals.</p>
<p>here are they -<br>
<a href="https://drive.google.com/drive/folders/1EnEGzXneSd4remUXUkFI0yBFHdWZl0Bw?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1EnEGzXneSd4remUXUkFI0yBFHdWZl0Bw?usp=sharing</a></p>
<p>Thanks,<br>
Pranay</p>

---

## Post #8 by @pranaysingh (2021-05-07 14:02 UTC)

<p>Also, this is metadata information given by 3D slicer</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Tag</th>
<th>Attribute</th>
<th>Value</th>
<th>VR</th>
<th>Length</th>
</tr>
</thead>
<tbody>
<tr>
<td>[0008,0005]</td>
<td>SpecificCharacterSet</td>
<td>ISO_IR 100</td>
<td>CS</td>
<td>10</td>
</tr>
<tr>
<td>[0008,0016]</td>
<td>SOPClassUID</td>
<td>1.2.840.10008.5.1.4.1.1.7</td>
<td>UI</td>
<td>26</td>
</tr>
<tr>
<td>[0008,0018]</td>
<td>SOPInstanceUID</td>
<td>2.25.296958948774992279876467636149074931855</td>
<td>UI</td>
<td>44</td>
</tr>
<tr>
<td>[0008,0021]</td>
<td>SeriesDate</td>
<td>20210122</td>
<td>DA</td>
<td>8</td>
</tr>
<tr>
<td>[0008,0031]</td>
<td>SeriesTime</td>
<td>153256</td>
<td>TM</td>
<td>6</td>
</tr>
<tr>
<td>[0008,103e]</td>
<td>SeriesDescription</td>
<td></td>
<td>LO</td>
<td>0</td>
</tr>
<tr>
<td>[0010,0010]</td>
<td>PatientName</td>
<td>Unspecified Patient</td>
<td>PN</td>
<td>20</td>
</tr>
<tr>
<td>[0010,0020]</td>
<td>PatientID</td>
<td>2.25.277744876348196707507775220078483990376</td>
<td>LO</td>
<td>44</td>
</tr>
<tr>
<td>[0020,000d]</td>
<td>StudyInstanceUID</td>
<td>1.2.276.0.7230010.3.1.2.568124770.6912.1611309776.784</td>
<td>UI</td>
<td>54</td>
</tr>
<tr>
<td>[0020,000e]</td>
<td>SeriesInstanceUID</td>
<td>2.25.42204707247853066808077597454226435009</td>
<td>UI</td>
<td>44</td>
</tr>
<tr>
<td>[0020,0011]</td>
<td>SeriesNumber</td>
<td>1</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0020,0013]</td>
<td>InstanceNumber</td>
<td>1</td>
<td>IS</td>
<td>2</td>
</tr>
<tr>
<td>[0020,0032]</td>
<td>ImagePositionPatient</td>
<td>[3] -7.591317, -54.826260, -8.552629</td>
<td>DS</td>
<td>30</td>
</tr>
<tr>
<td>[0020,0037]</td>
<td>ImageOrientationPatient</td>
<td>[6] 1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000</td>
<td>DS</td>
<td>54</td>
</tr>
<tr>
<td>[0028,0002]</td>
<td>SamplesPerPixel</td>
<td>1</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0004]</td>
<td>PhotometricInterpretation</td>
<td>MONOCHROME2</td>
<td>CS</td>
<td>12</td>
</tr>
<tr>
<td>[0028,0010]</td>
<td>Rows</td>
<td>1024</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0011]</td>
<td>Columns</td>
<td>1000</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0030]</td>
<td>PixelSpacing</td>
<td>[2] 0.015527, 0.015527</td>
<td>DS</td>
<td>18</td>
</tr>
<tr>
<td>[0028,0100]</td>
<td>BitsAllocated</td>
<td>16</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0101]</td>
<td>BitsStored</td>
<td>15</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0102]</td>
<td>HighBit</td>
<td>14</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,0103]</td>
<td>PixelRepresentation</td>
<td>0</td>
<td>US</td>
<td>2</td>
</tr>
<tr>
<td>[0028,1050]</td>
<td>WindowCenter</td>
<td>29157</td>
<td>DS</td>
<td>6</td>
</tr>
<tr>
<td>[0028,1051]</td>
<td>WindowWidth</td>
<td>58314</td>
<td>DS</td>
<td>6</td>
</tr>
<tr>
<td>[0028,1052]</td>
<td>RescaleIntercept</td>
<td>0.000</td>
<td>DS</td>
<td>6</td>
</tr>
<tr>
<td>[0028,1053]</td>
<td>RescaleSlope</td>
<td>1.000</td>
<td>DS</td>
<td>6</td>
</tr>
<tr>
<td>[7fe0,0010]</td>
<td>PixelData</td>
<td>0000</td>
<td>OW</td>
<td>2048000</td>
</tr>
</tbody>
</table>
</div>

---

## Post #9 by @mikebind (2021-05-07 18:03 UTC)

<p>Thanks for sharing.  I can confirm that I see that same phenomenon as you where the densest areas inappropriately show up with low pixel values.  The images you shared are clearly not directly off the scanner and appear to have been processed using DCMTK, perhaps because that is how you anonymized them?  When I look at these files with non-Slicer DICOM readers, they show the same problem as shown in Slicer, is that the case for you also?</p>
<p>However, where I expected that the dark areas would have large negative pixel values (high unsigned voxel values being reinterpreted as large negative signed voxel values), I instead see small positive voxel values.  I still think it’s highly likely that the problem is related to misinterpreted binary values somewhere in the processing chain, but I’m not sure how much more I’ll be able to help you.  This is supported by the highest pixel values in the images being exactly 32767, implying that the adjacent dark areas are probably values that crossed the 2^16 threshold and were misinterpreted.</p>
<p>I think you are looking in the right areas to get this figured out.  I would examine the DICOM header for the original files and see if there is anything which changes or is illuminating in the BitsAllocated, BitsStored, HighBit, PixelRepresentation, RescaleIntercept, or RescaleSlope fields. Slicer won’t change the header at all on import, so you can safely do the examination in Slicer. If MATLAB is your other tool, Slicer’s DICOM processing is usually better than MATLAB’s, so there is definitely a chance that Slicer is respecting the DICOM header in a way that MATLAB is not, and there is a problem or inconsistency in the original DICOM file. You might also try another DICOM tool to take a look at the original images (MicroDicom viewer on Windows or Osirix on Mac) and see how they look there.</p>
<p>Good luck going forward!</p>

---

## Post #10 by @pranaysingh (2021-05-07 18:40 UTC)

<p>Thaks alot Mike, that’s really helpful analysis.</p>
<aside class="quote no-group" data-username="mikebind" data-post="9" data-topic="17467">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>When I look at these files with non-Slicer DICOM readers, they show the same problem as shown in Slicer, is that the case for you also?</p>
</blockquote>
</aside>
<p>I used 2 softwares, matlab and Dicom browser, but I didn’t see the problem there as shown in 3d slicer. I have posted matlab’s output in the question.<br>
I am curious to know which software did you use where you found the same problem as shown by 3D slicer.</p>
<p>I was thinking of trying 2 methods for my problem, first was to try loading the dicom files in another format, like first converting the Dicom files into .nrrd format. It’s just one of the many formats supported by 3d slicer to load the data, then I will load the nrrd files to see if the problem still exists.<br>
The second approach would be yet another file format supported by 3D slicer, which is ‘raw volume’ format (.raw), according to the documentation, it requires manual setting of header parameters. I am hoping i can manually supply the right parameters about the data via this approach.</p>
<p>Thanks alot for narrowing down my suspicion about the problem. I will see if above mentioned things work out.</p>
<p>Best,<br>
Pranay</p>

---

## Post #11 by @mikebind (2021-05-08 00:07 UTC)

<p>I used <a href="https://www.microdicom.com/" rel="noopener nofollow ugc">https://www.microdicom.com/</a> as the outside DICOM viewer, where your uploaded anonymized image looked like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b37f85a41701d2a0ea1c6b58e043b1d81d548408.png" data-download-href="/uploads/short-url/pBUGhglVsjw9CCgcIAAmvMJ5TUQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b37f85a41701d2a0ea1c6b58e043b1d81d548408_2_690x387.png" alt="image" data-base62-sha1="pBUGhglVsjw9CCgcIAAmvMJ5TUQ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b37f85a41701d2a0ea1c6b58e043b1d81d548408_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b37f85a41701d2a0ea1c6b58e043b1d81d548408_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b37f85a41701d2a0ea1c6b58e043b1d81d548408.png 2x" data-dominant-color="9A9C9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1311×737 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I just tried the same image using MATLAB’s dicomread(), and it shows in MATLAB like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33eabff2b2b211f378482fc4de9eb4c31bbe45b3.jpeg" data-download-href="/uploads/short-url/7phiBDri29E9w6Xg1y1EVD9sSQP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33eabff2b2b211f378482fc4de9eb4c31bbe45b3_2_497x500.jpeg" alt="image" data-base62-sha1="7phiBDri29E9w6Xg1y1EVD9sSQP" width="497" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33eabff2b2b211f378482fc4de9eb4c31bbe45b3_2_497x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33eabff2b2b211f378482fc4de9eb4c31bbe45b3_2_745x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33eabff2b2b211f378482fc4de9eb4c31bbe45b3_2_994x1000.jpeg 2x" data-dominant-color="505050"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1073×1079 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer’s “Volumes” module shows the “Scalar Type” of this image as “unsigned short”, which is the same as 16 bit unsigned integer. MATLAB shows the loaded image data type as “uint16”, which is also 16 bit unsigned integer. However, comparing the exact same voxel (755, 414) in each gives, 11919 in Slicer and 43995 in MATLAB. I’m a bit baffled by this.</p>
<p>OK, here’s a theory: The DICOM header says that 16 bits are allocated per pixel, but that only 15 bits actually store image information (and that the high bit is bit 14, which I think means that the 15th bit is related to the sign).  However, I think MATLAB is ignoring this, and reading each pixel as a 16bit number.  It must be, because the largest 15 bit number is 32767 (2^15-1), and 43995 is larger than this.  Slicer, on the other hand, is ignoring the value in the 16th bit (which is what the DICOM standard says should be done) and only reading the remaining 15 (or 14, I’m not sure which because the 15th bit for 43995 would be 0). If I try dropping the 16th bit from the binary representation for 43995, I get 11227, which is pretty close to the values in Slicer, but not an exact match. Wait, just remembered that MATLAB indexing is 1-based, and Slicer indexing is 0-based, so the matching voxel index for (755, 414) in MATLAB would be (754, 413) in Slicer!  And there, the voxel value is 11227, exactly 2^16 less than 43995!  So, I think this must be what’s going on.</p>
<p>To summarize:</p>
<ul>
<li>The DICOM header is incorrect
<ul>
<li>While it says that there are only 15 bits of image data in each pixel, there are in fact 16 bits of image data</li>
</ul>
</li>
<li>MATLAB very likely ignores this in the DICOM header, just reading that 16 bits are allocated to each pixel value, and then loading the pixel data as 16 bit unsigned integers</li>
<li>Slicer, following the DICOM standard, ignores the 16th bit as the header indicates it should</li>
</ul>
<p>I think the correct fix for you is to fix the DICOM headers of your images so that BitsStored is 16 and the HighBit is 15 (it looks to me in DICOM reference info that the HighBit is now always supposed to be one less than BitsStored).  I think then they will load correctly in both Slicer and MATLAB.</p>

---

## Post #12 by @pranaysingh (2021-05-08 15:34 UTC)

<p>Hi Mike,</p>
<p>I would like to say a huge thanks to you for generously guiding me to the solution.<br>
I looked at the meta and understood the point you raised, finally as what you suggested I corrected the dicom header using pydicom and saved it again.<br>
Loaded the corrected dicom files in 3D slicer and the problem was fixed finally.</p>
<p>Thanks alot for that.  <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=9" title=":grin:" class="emoji" alt=":grin:"><br>
Regards,<br>
Pranay</p>

---

## Post #13 by @mikebind (2021-05-08 15:50 UTC)

<p>Great!  I’m glad we figured it out and it’s working for you now.</p>
<p>Best wishes,<br>
Mike</p>

---
