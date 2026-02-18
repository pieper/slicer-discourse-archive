# DICOM patient name not showing in database module

**Topic ID**: 34368
**Date**: 2024-02-16
**URL**: https://discourse.slicer.org/t/dicom-patient-name-not-showing-in-database-module/34368

---

## Post #1 by @Michael_Allen (2024-02-16 16:49 UTC)

<p>Hello, at some point in recent updates the patient name field in the dicom browser has stopped displaying the name. If I right click and view metadata, the name is still there. If I search for the name in the browser, slicer shows me the patient scans, but no name is present in the column. The other fields, ID, DOB, sex still populate fine. Any ideas what’s going on here?</p>
<p>Using 5.6.1 but it wasn’t working with 5.5 either.<br>
MacOS 12.7</p>

---

## Post #2 by @pieper (2024-02-16 16:51 UTC)

<p>Can you reproduce this with public data or share data for which this happens?</p>

---

## Post #3 by @Michael_Allen (2024-02-17 04:12 UTC)

<p>I don’t know of any public downloads that have Name metadata, if you have a link to any I would check it out. I’d prefer not to share any of my patient data.</p>

---

## Post #4 by @pieper (2024-02-17 15:07 UTC)

<p>There’s a lot of freely available dicom data with (anonymized) name strings.  For example here: <a href="https://portal.imaging.datacommons.cancer.gov/">https://portal.imaging.datacommons.cancer.gov/</a>, but at many other sites too.</p>

---

## Post #5 by @Michael_Allen (2024-02-17 23:53 UTC)

<p>Yep, sure enough loading a public dataset loads the name. All my data loads up fine in Horos, displaying the patient name. I deleted an existing older patient dataset, whose name was displayed fine, and re added it. The name no longer appears in the field.</p>
<p>I don’t think it’s a problem with the data, it’s the Slicer DICOM browser not displaying it. If I load a CT series, in the loaded data window it displays the patient name just fine.</p>

---

## Post #6 by @pieper (2024-02-18 15:55 UTC)

<p>If you think it’s not something specific to your data, can you describe the sequence of steps that leads to the name being missing?  If I understand correctly you say the name was there, but then it’s missing if you delete and re-add the same data?</p>
<p>There is some logic to map dicom header values to display names and maybe it gets out of sync with this operation.</p>

---

## Post #7 by @Michael_Allen (2024-02-18 22:19 UTC)

<p>Hi Steve, thank you for your help on this.</p>
<p>Previously, what I would do is just add (or drag a folder) a patient CT DICOM, and it would display Name, ID, birth date, sex as expected. Some time this fall, I updated to 5.5 and then 5.6, and since then when I load new patient data in the same way, the patient name column is empty. The previously added patients still display the name properly. I deleted one of these properly displayed patients, then re-added it and the name column is now blank.</p>
<p>I can right click and read the metadata and the name is there in field 0010,0010. I can search the name in the browser search bar, and the correct patient shows up though the name column is blank. Slicer is reading the name, it’s just not showing it in the browser patient column.</p>

---

## Post #8 by @pieper (2024-02-19 14:45 UTC)

<p>Okay, thanks.  Maybe you can help us narrow down what is happening and whether it’s something to do with the change of versions or whether it’s inherent with 5.6.1 and/or if certain dicom files trigger it or not.</p>
<p>What I tried is this:</p>
<ul>
<li>Launch 5.6.1</li>
<li>Set the dicom database directory to a newly created folder</li>
<li>drag and drop a dicom directory (patient name appears and data loads)</li>
<li>Delete patient from database</li>
<li>drag and drop directory again (patient name appears and data still loads).</li>
</ul>
<p>Are you able to replicate this?  How is your scenario different?</p>

---

## Post #9 by @jamesobutler (2024-02-19 16:32 UTC)

<p>Seems reminiscent of a previous reported issue where the user deleted all files associated with the Slicer dicom database and re-created it.</p>
<aside class="quote" data-post="13" data-topic="33228">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/3da27b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/problems-in-version-5-6-0/33228/13">Problems in version 5.6.0</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I resolved that problem when I deleted all the files (ctkDICOMTagCache.sql, ctkDICOM.sql) in dicom database. 
Maybe some old files in dicom database were not deleted when I uninstall the slicer. 
Sorry to bother you and thanks for your answer!
  </blockquote>
</aside>

<p>Does the patient name have any non-ASCII characters (non-English special characters)?</p>

---

## Post #10 by @Michael_Allen (2024-02-19 22:26 UTC)

<p>OK i deleted all the patients, changed the database folder, and then re added all the patients. They are now showing up with the name. In the browser the last, first name is separated by a comma. Looking at the metadata name tag they are separated by a ^. It seems somehow during the update there was an issue with the database, and deleting and changing to a new database seems to have solved the problem. I did not need to delete any of the files like in the link posted above.</p>

---

## Post #11 by @pieper (2024-02-19 22:37 UTC)

<p>Thanks for reporting and investigating.  We are always trying to improve things and sometimes there can be some hiccups along the way.</p>

---

## Post #12 by @cpinter (2024-02-20 09:45 UTC)

<p>Just for the record, the name is displayed with a comma instead of the DICOM-style ^ because we have special display fields and “rules” that generate these fields, so that the raw DICOM information is more human readable. It is almost impossible to debug this on a non-developer computer (meaning no access to CTK debug build), but I’m glad that using a brand new database solved the issue. There has been a version increment recently in the DICOM database schema, maybe there was an issue with the update process.</p>

---

## Post #13 by @mvergnat (2025-01-29 10:13 UTC)

<p>Dear 3d slicer colleagues,</p>
<p>Unfortunately, I encounter the same problem as Michael Allen, at the beginning of the post:</p>
<p>patient name field in the dicom browser has stopped displaying the name.</p>
<p>It was good working with 5.6.2</p>
<p>then</p>
<p>I did Slicer version Update,</p>
<p>Now using 5.8.0 r33216 / d20ee94</p>
<p>PC windows 10</p>
<p>The Slicer asked me to update DICOM database, I did it,</p>
<p>And now, no name anymore.</p>
<p>Of course (same problem), the names are in the system (for example, <strong>If I right click and view metadata, the name is still there</strong>), BUT they are not displayed in the Field:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bb9d393671e8d8bb595c72740d04feeee881029.png" data-download-href="/uploads/short-url/aNTWnILMpZ5cxHlR45q9IzToJf3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bb9d393671e8d8bb595c72740d04feeee881029_2_690x387.png" alt="image" data-base62-sha1="aNTWnILMpZ5cxHlR45q9IzToJf3" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bb9d393671e8d8bb595c72740d04feeee881029_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bb9d393671e8d8bb595c72740d04feeee881029.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bb9d393671e8d8bb595c72740d04feeee881029.png 2x" data-dominant-color="EFECF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">945×531 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have 40 dicoms here, reload everything will be bad.</p>
<p>EVEN, I uploaded a new DICOM, and it has also no name displayed, so reload does not solve problem.</p>
<p>I did not find the answer to this problem in the posts.</p>
<p>Thx for help!!</p>
<p>cheers</p>

---

## Post #14 by @pieper (2025-01-29 21:31 UTC)

<p>Did you try deleting the tag cache, as described earlier in this thread?</p>

---

## Post #15 by @mvergnat (2025-01-30 09:06 UTC)

<p>Dear Steve,<br>
<strong>MANY thx for your quick answer!!</strong><br>
So…<br>
I had to use my brain…it hurts…</p>
<p>I followed your instruction:<br>
" * Launch 5.6.1 [<em>I used my 5.8.0 r33216 / d20ee94</em>]</p>
<ul>
<li>Set the dicom database directory to a newly created folder</li>
<li>drag and drop a dicom directory<br>
-&gt;i<em>t worked</em>: patient name appears and data loads"<br>
when I come back on my initial dicom database, name still missing.</li>
</ul>
<p>would you advice that I have to rebuild my entire 40 patients database and drag and drop all 40 patients again???<br>
if yes, it would be very painful (<strong>unless there is an easy way to reload it…but I need intruction like for a 4y old boy…I am pretty much incompetent</strong>).</p>
<p>as comment, when I switch to “show experiemntal database” display…<br>
all the name are here!!! but not with the classic display (frustration…!)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d201378eb07445064d14b262417504d8eb6fac49.png" data-download-href="/uploads/short-url/tXMSkiRu7DDoTWaL44jXjogGJf3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d201378eb07445064d14b262417504d8eb6fac49_2_690x388.png" alt="image" data-base62-sha1="tXMSkiRu7DDoTWaL44jXjogGJf3" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d201378eb07445064d14b262417504d8eb6fac49_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d201378eb07445064d14b262417504d8eb6fac49_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d201378eb07445064d14b262417504d8eb6fac49_2_1380x776.png 2x" data-dominant-color="F0F0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>MANY THX FOR HELP!!!<br>
mathieu</p>

---

## Post #16 by @pieper (2025-01-30 21:19 UTC)

<p>If all your dicom data is in subfolders of a single top folder you can just drag and drop the top level and slicer will import it all.  Otherwise maybe you can multiselect and get all the dicom folders in a few steps.</p>

---
