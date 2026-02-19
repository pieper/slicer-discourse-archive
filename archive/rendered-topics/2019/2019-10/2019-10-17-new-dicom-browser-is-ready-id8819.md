---
topic_id: 8819
title: "New Dicom Browser Is Ready"
date: 2019-10-17
url: https://discourse.slicer.org/t/8819
---

# New DICOM browser is ready

**Topic ID**: 8819
**Date**: 2019-10-17
**URL**: https://discourse.slicer.org/t/new-dicom-browser-is-ready/8819

---

## Post #1 by @lassoan (2019-10-17 18:52 UTC)

<p>We have completely reworked the DICOM browser in Slicer to make it more responsive and display more relevant information.</p>
<p>Highlights:</p>
<ul>
<li>DICOM import runs in the background: application GUI is not blocked anymore and continuous, detailed progress information is shown while data is being imported</li>
<li>DICOM import speed is greatly improved: for example, time to import 10 TCIA patients decreased from 46 sec to 7 seconds.</li>
<li>DICOM patient/study/series can be loaded by double-clicking on the it</li>
<li>Added new displayed fields: such date added (makes it easy to find newly added images), number of studies/series/images, number of frames and frame size</li>
<li>Improved data columns display: fit column widths to content, set default sorting</li>
<li>DICOM database version upgrade is not enforced when updating Slicer (user can choose between upgrade or creating a new database at a new location)</li>
</ul>
<p>Developer features:</p>
<ul>
<li>Made it configurable which columns are displayed in the browser, in what order, what format (stored in database <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/Resources/dicom-schema.sql">ColumnDisplayProperties table</a>)</li>
<li>Moved many DICOM features into CTK (export to file system, DICOM metadata display, etc.)</li>
<li>Separated DICOM widget from logic: DICOM database is now owned by Slicer application using a shared pointer. This allows DICOM import and loading without using GUI classes (without instantiating DICOM browser widget). See example in DICOMUtils.loadSeriesByUID.</li>
<li>DICOM database object is always created (even if no valid DICOM database location is specified) when the application is started. If no valid DICOM database location is specified then the database will not be open.</li>
<li>Made recent activity widget selection trigger selection of the series in DICOM browser</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb1d5f8759df6a60d186fe8ac57251197992558d.png" data-download-href="/uploads/short-url/xxV8vCyiSOLDL2X43uo2FkVcBNH.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb1d5f8759df6a60d186fe8ac57251197992558d_2_690x321.png" alt="image" data-base62-sha1="xxV8vCyiSOLDL2X43uo2FkVcBNH" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb1d5f8759df6a60d186fe8ac57251197992558d_2_690x321.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb1d5f8759df6a60d186fe8ac57251197992558d_2_1035x481.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb1d5f8759df6a60d186fe8ac57251197992558d_2_1380x642.png 2x" data-dominant-color="E5E0E6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2234×1041 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The new browser is available in latest Slicer Preview Release. Any comments and suggestions are welcome.</p>

---

## Post #2 by @Amine (2019-10-17 19:24 UTC)

<p>Is it possible to configure the series choosing frame to display columns for specific metadata? Or another way to quickly access a pre-saved metadata list?<br>
Specifically thinking about Gantry tilt, pixel spacing, slice thickness</p>

---

## Post #3 by @lassoan (2019-10-17 20:01 UTC)

<aside class="quote no-group" data-username="Amine" data-post="2" data-topic="8819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>Is it possible to configure the series choosing frame to display columns for specific metadata?</p>
</blockquote>
</aside>
<p>Yes, you can add more displayed columns by editing the database schema and register custom ctkDICOMDisplayedFieldGeneratorAbstractRule classes in the DICOM database’s DisplayedFieldGenerator to fill those columns with values. This requires rebuilding of Slicer, so if you have specific fields that many users would potentially wan to see then we can add these rules to the application. Users then can use any SQLite file editor to change ColumnDisplayProperties table in the database to set what fields they want to see and what order.</p>
<aside class="quote no-group" data-username="Amine" data-post="2" data-topic="8819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>Or another way to quickly access a pre-saved metadata list?</p>
</blockquote>
</aside>
<p>You can see all DICOM metadata of an item by right-clicking and choosing “View DICOM metadata”. There is free-text (and regexp) search, so you can find all fields that you are interested in very quickly.</p>

---

## Post #4 by @Amine (2019-10-17 20:22 UTC)

<p>Thanks for your answer,</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="8819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>if you have specific fields that many users would potentially wan to see then we can add these rules to the application</p>
</blockquote>
</aside>
<p>I guess pixel spacing (0028:0030) slice thickness (0018:0050) and (a bit less importantly) gantry tilt (0018:1120) might be nice additions for many users.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="8819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is free-text (and regexp) search, so you can find all fields that you are interested in very quickly.</p>
</blockquote>
</aside>
<p>This works for individual checks but there is often a need to quickly check a set of metadata entries, i sometimes use microdicom (a free dicom viewer) just for its functionality of saving a list of favorite metadata and quickly browse them for multiple series.</p>

---

## Post #5 by @lassoan (2019-10-17 20:53 UTC)

<aside class="quote no-group" data-username="Amine" data-post="4" data-topic="8819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>slice thickness</p>
</blockquote>
</aside>
<p>Value of slice thickness field is rarely useful. This field does not specify image geometry and often missing. Slice spacing can only be determined by inspecting slice positions, which is a quite expensive operation. However, slice spacing information is often included in the series description.</p>
<p>Pixel spacing and gantry tilt could be added quite easily.</p>

---

## Post #6 by @awarru (2019-11-07 15:40 UTC)

<p>I am having difficulty using the new DICOM browser because the column width cannot be adjusted in the main display window.  This makes it inconvenient when I need to expand fields like ‘Date added’ to ensure I’m looking at the right files.  Is there a way to fix this currently?</p>

---

## Post #7 by @lassoan (2019-11-07 15:57 UTC)

<p>Only very narrow column widths are set automatically. You can change “Date added” column width by drag-and-dropping the <em>right</em> side of the column (left side of the column would resize the previous column, which is locked, because it is a narrow column that can be reliably sized automatically).</p>

---

## Post #8 by @awarru (2019-11-07 16:02 UTC)

<p>Thank you so much for fixing this problem for me, it’s been a very annoying hang up using the new Slicer<br>
This is very unintuitive behaviour and watching the left edge of the column move as I drag on the right edge feels incorrect.  That being said, I appreciate your help.</p>

---

## Post #9 by @lassoan (2019-11-07 16:13 UTC)

<p>This works exactly the same way as in Excel and most other software that displays tables: column width is always adjusted by drag-and-dropping the right side of the column. I agree that it is tricky to adjust the rightmost column because you need to drag outside the table, but nobody else has come up with a more intuitive solution.</p>

---

## Post #10 by @awarru (2019-11-07 16:19 UTC)

<p>Certainly true, it is correct to adjust from the right side of the column.  The unintuitive part (and what Excel does <strong>not</strong> do) is that the left side of the column is what actually moves when dragging on the right side.</p>

---

## Post #11 by @lassoan (2019-11-07 17:44 UTC)

<p>The left side of the column moves because the table is set to fill all the available space without scrolling (Excel just extends the table area and requires you to scroll). I agree that it is unexpected but I cannot think of a better behavior (without requiring scrolling and the user adjusting several column widths manually).</p>

---

## Post #12 by @dominicrushforth (2019-12-12 12:20 UTC)

<p>I like the new dicom database, but my users have come back to me with something that seems to be a bit of a bugbear for them. Every time the database loads the resizable columns are too small so they have to double click on the right side of the column for ‘date added’ and ‘patient ID’ in order to see the contents. Could these columns auto resize when the database is opened? Or when the selected data is changed?</p>
<p>Also, if you use it on a smaller 19" monitor you cannot see the right hand side of the right most column so can’t resize it. This is not a major issue for us as all of our systems have at least one widscreen monitor but it has the potential to cause confusion.</p>
<p>I did try changing the default column widths in the ColumnDisplayProperties table mentioned above, but couldn’t find it in my installed version. I presume this is something you have to change before making your own build? It might be nice if the database could be personalised without having to do your own build but I am aware that this might not be as easy as it sounds!</p>

---

## Post #13 by @lassoan (2019-12-12 14:25 UTC)

<p>Thank you for the feedback. The rightmost column contains the last insertion date, which is a rather long field (full date and time). We chose to not automatically resize the column because usually the actual time does not matter but you just want to use it for sorting (showing most recent at the top or bottom).</p>
<p>You can experiment with various settings by editing <code>ColumnDisplayProperties</code> table in <code>ctkDICOM.sql</code> file in SQLite file editor (I use <a href="https://sqlitebrowser.org/">SQLite browser</a>) or using <code>slicer.dicomDatabase.setFormatForField</code> method. If you don’t find the table then make sure you have created/updated the database with a recent Slicer Preview Release. For example, run this in Slicer’s Python console to make “Date added” field fully displayed in Patients table:</p>
<pre><code class="lang-python">slicer.dicomDatabase.setFormatForField('Patients', 'InsertTimestamp', '{"sort": "descending", "resizeMode":"resizeToContents"}')
slicer.dicomDatabase.schemaUpdated()
</code></pre>
<p>You can find further methods to customize displayed fields <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDatabase.h#L329-L350">here</a> (show/hide, change order, rename, etc.). You can make these changes permanent on a computer, for all installed Slicer versions, by adding such lines to your application startup file (<code>.slicerrc.py</code> - see in application settings).</p>
<p>If you find that insertion date&amp;time column should be always fully displayed and most other users agree then we can change the schema. If preference depends on user and environment (e.g., preferable to show in full on large monitors) then we should probably address this by making customization easier for users.</p>

---
