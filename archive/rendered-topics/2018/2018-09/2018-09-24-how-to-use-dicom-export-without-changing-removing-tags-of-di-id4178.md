---
topic_id: 4178
title: "How To Use Dicom Export Without Changing Removing Tags Of Di"
date: 2018-09-24
url: https://discourse.slicer.org/t/4178
---

# How to use "DICOM Export" without changing/removing tags of DICOM?

**Topic ID**: 4178
**Date**: 2018-09-24
**URL**: https://discourse.slicer.org/t/how-to-use-dicom-export-without-changing-removing-tags-of-dicom/4178

---

## Post #1 by @shahrokh (2018-09-24 14:53 UTC)

<p>Hi<br>
Dear developers and users</p>
<p>After using “DICOM Export” for a series images of PET, I get dicom files that these tages (DICOM metadata) are changed or removed (Attributes as “Modality”, “<strong>PatientName</strong>”, “<strong>RescaleIntercept</strong>”, “<strong>RescaleSlope</strong>”, “<strong>RescaleType</strong>” and many other tags).</p>
<p>I can edit these tags using softwares such as “DicomBrowser”, but this is a very time consuming task and it’s not accurate. I think that 3DSlicer must be able to do it.</p>
<p>At now, my question:<br>
How can I use “DICOM Export” for one series images of PET processed without changing or removing non of original tags of DICOM?</p>
<p>Please guide me,<br>
Thanks a lot,<br>
Shahrokh</p>

---

## Post #2 by @cpinter (2018-09-24 16:11 UTC)

<p>Patient and study level tags can be preserved by exporting them from the same patient/study. Or if you export one and want to export more, then check the Save tags checkbox when exporting after editing these fields.</p>
<p>RescaleIntercent and slope are volume-specific tags that I don’t think the ScalarVolume exporter plugin can currently provide.</p>

---

## Post #3 by @fedorov (2018-09-25 02:28 UTC)

<p>You can open DICOM Browser, select the data you want to export, and click right mouse button to select the location on disk to export to.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8db459e3901d776587482ed2ec0989d3a92eca26.png" data-download-href="/uploads/short-url/kdzISslQzxvHRkR2hgYCMa00qgu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8db459e3901d776587482ed2ec0989d3a92eca26_2_690x236.png" alt="image" data-base62-sha1="kdzISslQzxvHRkR2hgYCMa00qgu" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8db459e3901d776587482ed2ec0989d3a92eca26_2_690x236.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8db459e3901d776587482ed2ec0989d3a92eca26_2_1035x354.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8db459e3901d776587482ed2ec0989d3a92eca26.png 2x" data-dominant-color="DDE4ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1348×462 49.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2018-09-25 13:17 UTC)

<p>Yes you can do this if your volume has not changed. But then why would you want to use Slicer for export if you already have it…</p>

---

## Post #5 by @fedorov (2018-09-25 13:45 UTC)

<p>I obviously don’t know what the user actually wants to do… But there are many situations where one might want to export from DICOM Browser, such as DICOM series was created by Slicer, need to export to move the file to another computer/dropbox/flashdrive. Sorry if my response only added confusion.</p>

---

## Post #6 by @cpinter (2018-09-25 13:59 UTC)

<p>Not at all, I just pointed out that what we can see in the DICOM browser is the original data. If we change it in any way, then we’ll need to go through the 1) subject hierarchy DICOM exporter or the 2) Create DICOM series module (which is a legacy module as far as I’m concerned, but it can still probably do things that the other one cannot).</p>

---

## Post #7 by @fedorov (2018-09-25 14:12 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="4178">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>what we can see in the DICOM browser is the original data</p>
</blockquote>
</aside>
<p>Yes, but with few exceptions. PETDICOM extension plugin transparently creates a new DICOM RWVM series that gets added to the DICOM DB, and so does QuantitativeReporting creating new SEG and SR series.</p>

---

## Post #8 by @shahrokh (2018-09-27 05:24 UTC)

<p>Dear Csaba and Andrey</p>
<p>Thanks a lot for your guidance. Sorry I did not give any feedback.<br>
I have to point out what I want to create three landmarks on PET/CT images and then export them to TPS for doing research.<br>
After adding the landmarks to both two series of PET/CT images, I do what Andrey pointed out. As you mentioned in your messages, this method does not apply changes in new DICOM series.<br>
I do this work (editing DICOM tags) using DicomBrowser.</p>
<p>It seems that Pydicom can do it, but when I want to install and use it in Python Interactor of 3DSlicer, I get the following error:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import pip<br>
pip.main([‘install’, ‘pydicom’])<br>
Requirement already satisfied: pydicom in ./Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages<br>
You are using pip version 9.0.1, however version 18.0 is available.<br>
You should consider upgrading via the ‘pip install --upgrade pip’ command.<br>
0<br>
import pydicom<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
ImportError: No module named pydicom</p>
</blockquote>
</blockquote>
</blockquote>
<p>I was looking for commands in Python and Slicer API smiliar to dicominfo (to edit tags) and dicomwrite.<br>
Please guide me if such commands/functions are available in Slicer API and python.</p>
<p>Please guide me.<br>
Shahrokh</p>

---

## Post #9 by @lassoan (2018-09-27 05:26 UTC)

<p>pydicom is already bundled with Slicer. Use <code>import dicom</code> (and not <code>import pydicom</code>).</p>

---

## Post #10 by @shahrokh (2018-09-27 05:38 UTC)

<p>Thanks a lot Andras.<br>
Where can I find tutorials about using <strong>dicom</strong> in 3DSlicer to edit tags and then write DICOM files?</p>

---

## Post #11 by @lassoan (2018-09-27 18:19 UTC)

<p>It’s a regular Python package, so there is no Slicer-specific tutorial, just check out their <a href="https://github.com/pydicom/pydicom">website</a> about how to use it.</p>

---

## Post #12 by @Dex2046 (2023-12-17 12:31 UTC)

<p>Hi, I met a quite similar problem, so may I know how to solve the problem?</p>

---
