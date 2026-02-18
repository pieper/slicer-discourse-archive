# Question about Editor and Labelstatistics Modules

**Topic ID**: 5008
**Date**: 2018-12-07
**URL**: https://discourse.slicer.org/t/question-about-editor-and-labelstatistics-modules/5008

---

## Post #1 by @otanit (2018-12-07 15:16 UTC)

<p>Operating system:WIndows 10<br>
Slicer version:Slicer version 4.10.0<br>
Expected behavior:<br>
Actual behavior:<br>
Dear the staff,</p>
<p>I am performing manual parcellation of prefrontal cortex of the brain and trying to measure volumes for the manually segmentated regions.<br>
Within this process, I have the following questions:</p>
<ol>
<li>How can I measure ICC volumes. When I used slicer 2, ICC volume could be calculated automatically for each of the cases for the MRI.</li>
<li>For manual parcellation, I want to draw lines along the brain sulcus as markers, and then make parcellation referring to the markers. However, I can’t cut the line when I draw lines. How do I draw more than one line on one slice? When I draw a line I can’t make an end-point to form the line and then begin a new start-point to draw another line. How do I draw multiple lines on one slice?</li>
<li>To my understanding, I can measure volume for the manually segmentated ROIs using Labelstatistics Module. Is it true?</li>
</ol>
<p>I would like to have your advice or help for the questions above.<br>
I appreciate any advice or siggestions.</p>
<p>Best wihes,<br>
TO</p>

---

## Post #2 by @cpinter (2018-12-07 17:42 UTC)

<p>Please use the Segment Editor module, the much improved successor of the legacy Editor module (which will be removed in 5.0). See tutorials here<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>

---

## Post #3 by @otanit (2018-12-10 08:19 UTC)

<p>Dear Dr. Csaba Pinter,</p>
<p>Thank you for your quick response and information.<br>
I could address most of my problems, however, how can I calculate the<br>
total intracranial contents (ICC) volume, which is yield by summing<br>
voxel volumes of gray and white matter and cerebrospinal fluid.<br>
I would like to know where I can find the manual or instruction for the<br>
question above.<br>
I appreciate your time and kind advice if possible.</p>
<p>Best wishies,<br>
TO</p>

---

## Post #4 by @cpinter (2018-12-10 15:42 UTC)

<p>I need to understand the segmentation workflow to answer this question. What segments do you have? You have three different segments that delineate the three structures that comprise the ICC? If so, then you can either create a new segment that is the union of the three (Logical operators effect), and use Segment Statistics on that, or use Segment Statistics as is, and add up the volume measurements of the three segments.</p>

---

## Post #5 by @otanit (2018-12-12 10:39 UTC)

<p>Dear Dr. Csaba Pinter,</p>
<p>I appreciate your time and kind response.<br>
I want to measure volumes for the following segments: whole brain gray<br>
matter, whole brain white matter and  whole cerebrospinal fluid.<br>
I would like to know how can I do it automatically.<br>
I’m sorry for inturrupting you, but I would like to know the modules or<br>
icons, which I should try.<br>
Again, I greatly appreciate your time and kind advice.</p>

---

## Post #6 by @cpinter (2018-12-12 13:28 UTC)

<p>Please try the Segment Statistics module and describe it in detail please what it is additionally that you’d like to achieve.</p>

---
