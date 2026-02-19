---
topic_id: 30058
title: "Sqlite3 Query In Python Returns Less Data Than What Appears"
date: 2023-06-15
url: https://discourse.slicer.org/t/30058
---

# SQLite3 query in Python returns less data than what appears in the Slicer DICOM module

**Topic ID**: 30058
**Date**: 2023-06-15
**URL**: https://discourse.slicer.org/t/sqlite3-query-in-python-returns-less-data-than-what-appears-in-the-slicer-dicom-module/30058

---

## Post #1 by @smsmt (2023-06-15 18:29 UTC)

<p>Hello everyone,</p>
<p>I am currently working on constructing a database of DICOM tags using 3D Slicer. I have imported DICOM image data of approximately 700 patients into the Slicer, which seems to have successfully processed all the files as the DICOM tags within the Slicer UI show data for all the patients.</p>
<p>To extract this data, I used the “ctkDICOM.sql” file that Slicer generated. This file is around 2GB in size, with an additional 20GB cache SQL file. When I attempt to parse the “ctkDICOM.sql” file using the sqlite3 module in Python, however, I find that data for around 200 patients seems to be missing.</p>
<p>Despite this, there doesn’t appear to be an issue with the original DICOM data, as all patient data is correctly displayed in the Slicer UI. I have double-checked the DICOM files, and they don’t seem to be the problem.</p>
<p>I was wondering if anyone could provide some guidance on this. Specifically, my goal is to generate a single SQL file using Slicer that contains all the DICOM tag information for these patients.</p>
<p>Any help or insights would be greatly appreciated!</p>
<p>Thank you in advance.</p>

---

## Post #2 by @pieper (2023-06-15 20:26 UTC)

<p>The dicom database is managed by <a href="https://github.com/commontk/CTK/tree/master/Libs/DICOM">the CTK code</a>, including the mapping from what’s in the database to what’s displayed on the screen, as generally described here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDisplayedFieldGenerator.h#L34-L49">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDisplayedFieldGenerator.h#L34-L49" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDisplayedFieldGenerator.h#L34-L49" target="_blank" rel="noopener">commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDisplayedFieldGenerator.h#L34-L49</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="34" style="counter-reset: li-counter 33 ;">
          <li>/// \ingroup DICOM_Core</li>
          <li>///</li>
          <li>/// \brief Generates displayable data fields from DICOM tags</li>
          <li>/// </li>
          <li>/// The \sa updateDisplayedFieldsForInstance function is called from the DICOM database when update of the</li>
          <li>/// displayed fields is needed.</li>
          <li>/// </li>
          <li>/// Displayed fields are determined by the rules, subclasses of ctkDICOMDisplayedFieldGeneratorAbstractRule.</li>
          <li>/// The rules need to be registered to take part of the generation. When updating the displayed fields,</li>
          <li>/// every rule defines the fields it is responsible for using the cached DICOM tags in the database.</li>
          <li>/// Tags can be requested to be cached in the rules from the getRequiredDICOMTags function. After the fields</li>
          <li>/// are defined in each rule, the results are merged together. The merging rules are also defined in the</li>
          <li>/// rule classes. Each field can requested to be merged with "expect same value", which uses the only</li>
          <li>/// non-empty value and throws a warning if conflicting values are encountered, or with "concatenate",</li>
          <li>/// which simply concatenates the displayed field values together.</li>
          <li>///</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>That should explain how the fields are generated.  But there’s no reason 200 patients should be missing from the database if they are displayed on the GUI (they should be the same).  Maybe try recreating the issue, perhaps with public data, and if you can let us know the steps and hopefully someone can help you troubleshoot.</p>

---

## Post #3 by @lassoan (2023-06-16 13:32 UTC)

<p><a href="https://www.sqlite.org/limits.html">SQlite3 sets default limits for query results</a>. It seems that with your select query you reached the default limit of 500 records. You can use the <a href="https://www.beekeeperstudio.io/blog/sqlite-limit"><code>LIMIT</code> clause</a> in your query to get all the records.</p>

---

## Post #4 by @smsmt (2023-06-16 18:16 UTC)

<p>Thanks Andras and Pieper for your thoughts. I’ve tried a few things already:</p>
<ol>
<li>I used a “LIMIT” command to see if there’s an issue with sqlite3, but that didn’t help.</li>
<li>I also opened the ctkDICOM.sql file using a tool called DB browser, but I still saw the same problem.</li>
</ol>
<p>I noticed that 200 patients are missing, but they’re not just at the end of the list. They’re missing randomly when I try to look at the data using the DB browser or Python. But, I can see them when I use the Slicer UI.<br>
Also, some data shows as ‘None’ when I look at it in the DB browser or Python, but it’s there when I use the Slicer UI.</p>
<p>So, my guess is that Slicer might be using cache file called ctkDICOMTagCache.sql to fill in the missing data and patients. That might be how Slicer manages to show all the data.</p>
<p>Now, I’m going to try moving the data to a new computer. I want to see if I still have the same problems with the ctkDICOM.sql generated file by Slicer and the missing data.</p>

---

## Post #5 by @lassoan (2023-06-16 18:58 UTC)

<p>You can ignore the tag cache file, that just stores some fields for faster access. Only <code>ctkDICOM.sql</code>  content matters. You can find the list of patients in <code>Patients</code> table.</p>
<p>Note that none of these files are part of the public Slicer API. If you can find a way to extract useful information from the sqlite files then that is fine for us, but we do not support this (because that would impose many limitations on how we can evolve the internal design in the future). The public API for the Slicer DICOM database is the <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDatabase.h">ctkDICOMDatabase</a> object that is accessible in Slicer Python environment as <code>slicer.dicomDatabase</code>.</p>

---
