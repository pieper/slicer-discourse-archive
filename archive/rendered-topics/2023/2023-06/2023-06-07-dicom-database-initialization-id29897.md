---
topic_id: 29897
title: "Dicom Database Initialization"
date: 2023-06-07
url: https://discourse.slicer.org/t/29897
---

# DICOM database initialization

**Topic ID**: 29897
**Date**: 2023-06-07
**URL**: https://discourse.slicer.org/t/dicom-database-initialization/29897

---

## Post #1 by @Nadya_Shusharina (2023-06-07 13:12 UTC)

<p>Hi!</p>
<p>I am starting Slicer in a Docker container. I need to initialize Slicer DICOM database prior to executing the module I am working on. How to initialize the db in a script rather than manually clicking “Create new database” in DICOM module GUI?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2023-06-07 14:44 UTC)

<p>Hi <a class="mention" href="/u/nadya_shusharina">@Nadya_Shusharina</a>  -  See <a href="https://discourse.slicer.org/t/persist-new-server-in-dicom-query-servers-list/27227">this thread</a> with <a class="mention" href="/u/paula_moreno">@Paula_Moreno</a> for information about creating a settings file for server connectsions.  Setting up the database should be similar.  We also worked on this <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerHub/">last project week</a> and as I recall we ran into a language localization issue with the docker directory path, but otherwise I think it was working.</p>

---

## Post #3 by @Nadya_Shusharina (2023-06-07 15:38 UTC)

<p>Thank you, Steve.</p>
<p>Looking at that thread,  I made a workaround by manually initializing the database in the running container and added  the empty ctkDICOM.sql and ctkDICOMTagCache.sql into the Dockerfile:</p>
<pre><code class="lang-auto">RUN mkdir -p /home/slicer/Documents/SlicerDICOMDatabase
COPY files/SlicerDICOMDatabase/ctkDICOM.sql /home/slicer/Documents/SlicerDICOMDatabase
COPY files/SlicerDICOMDatabase/ctkDICOMTagCache.sql /home/slicer/Documents/SlicerDICOMDatabase
</code></pre>
<p>It would be cleaner to have Slicer create the .sql files every time the container starts.</p>

---

## Post #4 by @pieper (2023-06-07 15:50 UTC)

<p>I haven’t looked at that initialization code in a while, but I thought it used to create a database when you initialized the browser, so it might be enough to run <code>selectModule("DICOM")</code> in python at startup.  But you can probably also find a way to initialize a the database and set <code>slicer.dicomDatabase</code> on the fly.</p>

---

## Post #5 by @Nadya_Shusharina (2023-06-07 16:09 UTC)

<p>In Slicer 5.0.2 without the database, running slicer.util.selectModule(‘DICOM’) in GUI python interactor presents two buttons, “Create new database” and “Select database folder”. The db is not created unless the button is pressed.</p>
<p>In command line,<br>
<code>Slicer --python-code "slicer.util.selectModule('DICOM');" --testing</code><br>
prints a message but does not create the sql files:<br>
<code>Database folder does not contain ctkDICOM.sql file: /opt/slicer</code></p>

---

## Post #6 by @pieper (2023-06-07 18:10 UTC)

<p>The feature is implemented in CTK, so you should be able to call this method:<br>
<code>ctk.ctkDICOMBrowser().createNewDatabaseDirectory()</code></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L510-L589">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L510-L589" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L510-L589" target="_blank" rel="noopener">commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L510-L589</a></h4>



    <pre class="onebox"><code class="lang-cpp">
      <ol class="start lines" start="510" style="counter-reset: li-counter 509 ;">
          <li>void ctkDICOMBrowser::createNewDatabaseDirectory()</li>
          <li>{</li>
          <li>  Q_D(ctkDICOMBrowser);</li>
          <li>
          </li>
<li>  // Use the current database folder as a basis for the new name</li>
          <li>  QString baseFolder = this-&gt;databaseDirectory();</li>
          <li>  if (baseFolder.isEmpty())</li>
          <li>  {</li>
          <li>    baseFolder = d-&gt;DefaultDatabaseDirectory;</li>
          <li>  }</li>
          <li>  else</li>
          <li>  {</li>
          <li>    // only use existing folder name as a basis if it is empty or</li>
          <li>    // a valid database</li>
          <li>    if (!QDir(baseFolder).isEmpty())</li>
          <li>    {</li>
          <li>      QString databaseFileName = QDir(baseFolder).filePath("ctkDICOM.sql");</li>
          <li>      if (!QFile(databaseFileName).exists())</li>
          <li>      {</li>
          <li>        // current folder is a non-empty and not a DICOM database folder</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L510-L589" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @Nadya_Shusharina (2023-06-07 18:38 UTC)

<p>It “almost” worked: CTK initializes the database in $HOME/ctkDICOM-database while Slicer expects $HOME/Documents/SlicerDICOMDatabase. How to create it in the right place?</p>

---

## Post #8 by @pieper (2023-06-07 19:15 UTC)

<p>You can do something like this:</p>
<pre><code class="lang-auto">dicomBrowser = ctk.ctkDICOMBrowser()
dicomBrowser.databaseDirectory = "/tmp/x"
dicomBrowser.createNewDatabaseDirectory()
</code></pre>

---

## Post #9 by @Nadya_Shusharina (2023-06-07 19:36 UTC)

<p>It works. The portable way to form the database directory is</p>
<pre><code class="lang-auto">import os
documentsLocation = qt.QStandardPaths.DocumentsLocation
documents = qt.QStandardPaths.writableLocation(documentsLocation)
databaseDirectory = os.path.join(documents, slicer.app.applicationName + "DICOMDatabase")
dicomBrowser = ctk.ctkDICOMBrowser()
dicomBrowser.databaseDirectory = databaseDirectory
dicomBrowser.createNewDatabaseDirectory()
</code></pre>
<p>Adapted from <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOM/DICOM.py" class="inline-onebox" rel="noopener nofollow ugc">Slicer/DICOM.py at main · Slicer/Slicer · GitHub</a></p>
<p>Of note, this snippet does not work using <code>Slicer --testing --python-script initDICOMdb.py</code> because app.applicationName becomes Slicer-tmp rather than Slicer. It works wihtout --testing, and in .slicerrc.py</p>

---
