---
topic_id: 319
title: "Dicom Browser How To Distinguish Series In The List"
date: 2017-05-16
url: https://discourse.slicer.org/t/319
---

# DICOM Browser: How to distinguish series in the list?

**Topic ID**: 319
**Date**: 2017-05-16
**URL**: https://discourse.slicer.org/t/dicom-browser-how-to-distinguish-series-in-the-list/319

---

## Post #1 by @jondo (2017-05-16 10:45 UTC)

<p>Hello,<br>
I have received DICOM data from an external partner. After importing the files, the DICOM browser lists a lot of series, but they all look exactly the same in the series list. I can only distinguish them by opening the metadata window and looking at the file path. (The patient info is the same, and the study info only differs by the StudyTime, which contains an uninterpretable value, probably filled in by anonymization software.)</p>
<p>It would be very useful for me to have this file path as additional column in the series list. Is this possible?</p>

---

## Post #2 by @lassoan (2017-05-16 13:03 UTC)

<p>Usually a DICOM series is stored in hundreds of files, with random file names, often spread across in several directories, so they are not a good indication of content. For the rare occasion when filenames are useful, you have the metadata browser.</p>
<p>I agree that more useful information could be shown in the series list. Do you see any other field in the metadata browser that would better indicate what’s in the series?</p>

---

## Post #3 by @jondo (2017-05-16 14:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="319">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you see any other field in the metadata browser that would better indicate what’s in the series?</p>
</blockquote>
</aside>
<p>The data has the modality <code>RTIMAGE</code>, and each series comes from just one file. I see a field <code>GantryAngle</code> with useful content.</p>

---

## Post #4 by @lassoan (2017-05-16 15:08 UTC)

<p>For RTIMAGE the best is to install SlicerRT, load all the RTIMAGEs and use the Data modul (Subject hierarchy view) to browse the data.</p>
<p>We’ll keep in mind to make the series list more customizable. I’ve added a ticket to track this: <a href="http://na-mic.org/Mantis/view.php?id=4373">http://na-mic.org/Mantis/view.php?id=4373</a></p>

---

## Post #5 by @jondo (2017-05-22 06:48 UTC)

<p>Thank you for the hint and the ticket. Unfortunately, I could not load the RTIMAGES:</p>
<p>The Slicer-2017-05-06 Nightly with SlicerRT gave me<br>
<code>Could not load: Unknown - as DWI Volume as a Diffusion Volume</code>,<br>
and Slicer <s>3.6.2</s> 4.6.2 with SlicerRT said<br>
<code>Could not load: 0: RTIMAGE: 744483668-0 as a RT</code>.</p>
<p>However, I don’t currently need to solve this, because my project has moved into a different direction.</p>

---

## Post #6 by @cpinter (2017-05-22 15:12 UTC)

<p>I thought SlicerRT is only available for Slicer 4.0 and above, but in any case, those versions are at least 5-6 years old, and many features - including RTIMAGE reading - is not present yet.</p>
<p>As for the new nightly, the message you get is not from SlicerRT, but from another DICOM plugin, which suggests that SlicerRT is not properly installed, or maybe there are some other issues related to the DICOM plugins. Can you load dose volumes correctly? (meaning that it appears with a rainbow color palette, and is shown as dose volume in subject hierarchy)</p>
<p>If you can share those DICOM files with us (preferably anonymized), then I can take a look.</p>

---

## Post #7 by @jondo (2017-05-23 06:31 UTC)

<p>Sorry for my misleading typo: I meant Slicer 4.6.2 (and fixed that now).</p>
<p>As a Slicer newbie, I don’t know anything about the ‘dose volumes’ you mention. However, some RTSTRUCT file loads fine in both Slicer versions, so SlicerRT seems to be installed correctly. (It is the only installed extension.)</p>
<p>Unfortunately, my project does not currently allow to find out whether I can share the files.</p>

---

## Post #8 by @cpinter (2017-05-23 13:35 UTC)

<p>If RTSS is loaded correctly, then SlicerRT is correctly deployed indeed. Unfortunately without at least one RTIMAGE file I cannot find out why it fails to load. Can you share the log after the failed load? You can find it in the menu Help / Report a bug.</p>
<p>FYI, as RTIMAGE is a radiation therapy image modality, and RT involves irradiation with a planned dose, the 3D dose distribution needs to be calculated and evaluated. This is what dose volume is.</p>

---
