---
topic_id: 14218
title: "Show Patient Comments Field In Dicom Browser"
date: 2020-10-24
url: https://discourse.slicer.org/t/14218
---

# Show patient comments field in DICOM browser

**Topic ID**: 14218
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/show-patient-comments-field-in-dicom-browser/14218

---

## Post #1 by @l.znaniecki (2020-10-24 05:13 UTC)

<p>HI there,</p>
<p>I have a lot of DICOMs imported form OSIRIX, and a lot of those studies have been commented in OSIRIX (I don’t mean a report was created, I mean on a list in OSIRIX there is a column named comment, and you can put there a word, or two).</p>
<p>Question - is there a way to visualise such comment in Slicer, make a column in list view of DICOMs, etc? This info is stored in DICOM files.</p>
<p>Regards,<br>
Lukasz</p>

---

## Post #2 by @lassoan (2020-10-24 14:33 UTC)

<p>It is highly unlikely that Osirix modifies the <em>original</em> DICOM images. You can check if the comment is included in <em>exported</em> images by importing them into Slicer and checking metadata content (by right-clicking on the the image in Slicer DICOM browser and choosing “View metadata”).</p>
<p>If comments are not exported to DICOM files then you can read it from the DICOM database of Osirix. Many years ago they used sqlite database for this (maybe the still do), which can be easily read in Python.</p>

---

## Post #3 by @l.znaniecki (2020-10-24 16:30 UTC)

<p>That is true, such field is not present in DICOM when I use “view metadata”. How can access is in SQLite? Can you suggest me this Python script?</p>
<p>Regards,<br>
Lukasz</p>

---

## Post #4 by @lassoan (2020-10-24 17:16 UTC)

<p>To explore what tables are in the database and implent the query you need, you can use viewers, such as <a href="https://sqlitebrowser.org/">https://sqlitebrowser.org/</a></p>
<p>Then, you can write the Python script that gets and the information you need. There are many Python Sqlite tutorials, for example <a href="https://www.tutorialspoint.com/sqlite/sqlite_python.htm">https://www.tutorialspoint.com/sqlite/sqlite_python.htm</a>. We can help if you are not sure how to use the retrieved information in Slicer.</p>

---

## Post #5 by @l.znaniecki (2020-10-26 12:21 UTC)

<p>OK, thank you. I get that.</p>
<p>Another thing -  I very much miss PatienComments column in 4.11.<br>
This is how it looks in your manual regarding v. 4.10.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d400e00d48684e3d9f0c2cac9565a301e2ba0985.png" data-download-href="/uploads/short-url/uft67YjAV1FRNpu90CTO7iRY8a9.png?dl=1" title="DICOM_Screenshot-1_1204-11-17-10-36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d400e00d48684e3d9f0c2cac9565a301e2ba0985_2_690x432.png" alt="DICOM_Screenshot-1_1204-11-17-10-36" data-base62-sha1="uft67YjAV1FRNpu90CTO7iRY8a9" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d400e00d48684e3d9f0c2cac9565a301e2ba0985_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d400e00d48684e3d9f0c2cac9565a301e2ba0985_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d400e00d48684e3d9f0c2cac9565a301e2ba0985.png 2x" data-dominant-color="E2E3EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DICOM_Screenshot-1_1204-11-17-10-36</span><span class="informations">1335×836 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But it is not visible in 4.11. Can I retrieve the column somehow?</p>
<p>Regards,<br>
Lukasz</p>

---

## Post #6 by @lassoan (2020-10-26 20:04 UTC)

<p>In Slicer-4.11, you can configure the name, visibility, formatting, and order of DICOM browser columns as shown in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_table_columns_in_DICOM_browser">script repository</a>.</p>
<p>We made patient comments hidden by default because it is almost never used in clinical practice, but you can make it visible by typing this into the Python console (you only need to do this once, as column display properties are stored persistently in the database):</p>
<pre><code class="lang-python">dicomBrowser = slicer.modules.dicom.widgetRepresentation().self().browserWidget.dicomBrowser
dicomDatabase = dicomBrowser.database()
dicomDatabase.setVisibilityForField('Patients', 'PatientsComments', True)
dicomDatabase.setWeightForField('Patients', 'PatientsComments', 8)
dicomDatabase.closeDatabase()
dicomDatabase.openDatabase(dicomBrowser.database().databaseFilename)
</code></pre>

---

## Post #7 by @l.znaniecki (2020-10-26 21:34 UTC)

<p>OK, Thanks.</p>
<p>Now I see comments column, but how can I actually comment the examination in there? Or can I only read what is contained in “PatientComments” in DICOM?</p>
<p>Regards,<br>
Lukasz</p>

---

## Post #8 by @lassoan (2020-10-26 21:41 UTC)

<p>Content of the comment field is set from the DICOM file. If you want to modify the field then you need to modify the DICOM file and re-index the file.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> I know that you have worked on something similar in custom projects. Are field editing features planned to be added to Slicer core as well?</p>
<p><a class="mention" href="/u/l.znaniecki">@l.znaniecki</a> Can you tell a bit more about your use case? Why would you like to change these DICOM fields? To fix mistakes in fields, make it easier to find data sets or build patient cohorts, …?</p>

---

## Post #9 by @l.znaniecki (2020-10-26 22:01 UTC)

<p>Good question.</p>
<p>To build patient cohorts, and then, to easily find data sets.</p>
<p>Is there a way to customize Slicer in that direction? (I feel yes, there is, based on your question to <a class="mention" href="/u/cpinter">@cpinter</a> <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"> )</p>
<p>Regards,<br>
Lukasz</p>

---

## Post #10 by @lassoan (2020-10-27 02:30 UTC)

<p>We will probably make some field editing possible for fixing errors (e.g., typo in patient name) or adding missing information.</p>
<p>However, field editing would interfere with cohort building, as after any modification of a DICOM file (if the DICOM files might be accessed by an external system) you need to generate new UIDs, refer to the old instances, and preferably also notify connected information systems that the old version of the data set is now obsolete and share the updated version. Instead, typically cohorts are built by compiling information from the DICOM header and other non-imaging sources into spreadsheets or other specialized cohort building tools (you can add comments or any extra information there), then exporting minimal, anonymized data set for analysis (often this is not even in DICOM format anymore, but in nrrd or other research file formats).</p>

---

## Post #11 by @l.znaniecki (2020-10-27 07:08 UTC)

<p>OK, thank you for this answer.</p>
<p>So I would probably need:</p>
<ol>
<li>build a repository of anonymized DICOMs (PACS?)</li>
<li>have a separate tool to connect those DICOMs with cohort building toll (what tool would you suggest?) - by patient ID for example?</li>
<li>have a tool to export selected packets (based on some comments) of DICOMs from PACS to nrrd and import them to Slicer - scripts?</li>
</ol>
<p>I would greatly appreciate your help to establish an efficient tool to work on hundreds of CT DICOMs.</p>
<p>Thanks,<br>
Regards,<br>
Łukasz</p>

---

## Post #12 by @cpinter (2020-10-27 11:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="14218">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I know that you have worked on something similar in custom projects. Are field editing features planned to be added to Slicer core as well?</p>
</blockquote>
</aside>
<p>We implemented editing capabilities in a Slicer custom app that uses DCMTK’s dcmodify tool and sets the changed fields such as patient comments. However, we haven’t gotten as far as re-generating UIDs and referencing the old dataset etc. The DICOM database in that particular case is completely controlled by the workstation and there is no chance that someone has accessed the old dataset externally, so this feature has been delayed. This is the main reason we haven’t integrated it into Slicer. The other reason is that the UI the custom app uses for editing is not the DICOM table view.</p>

---
