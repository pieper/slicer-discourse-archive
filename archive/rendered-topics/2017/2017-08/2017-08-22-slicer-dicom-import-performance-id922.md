---
topic_id: 922
title: "Slicer Dicom Import Performance"
date: 2017-08-22
url: https://discourse.slicer.org/t/922
---

# Slicer DICOM import performance

**Topic ID**: 922
**Date**: 2017-08-22
**URL**: https://discourse.slicer.org/t/slicer-dicom-import-performance/922

---

## Post #1 by @fedorov (2017-08-22 21:49 UTC)

<p>Today I tried MITK, and I noticed that DICOM import operation is order of magnitude faster there than in Slicer.</p>
<p>I tested this specific dataset: <a href="https://bit.ly/QIN-HN-137">https://bit.ly/QIN-HN-137</a> on the same Linux system with the latest MITK package (2016.11) and the latest Slicer nightly. In MITK import of this dataset takes seconds, and in Slicer it is over 20 seconds. Considering both platforms are using the common set of components from CTK, is this behavior expected?</p>

---

## Post #2 by @lassoan (2017-08-22 21:53 UTC)

<p>Does it have a DICOMDIR file? (download from the link is really slow…)<br>
Is the import slower if you delete the DICOMDIR file?</p>

---

## Post #3 by @fedorov (2017-08-22 21:55 UTC)

<p>No, there is no DICOMDIR file.</p>

---

## Post #4 by @fedorov (2017-08-22 21:59 UTC)

<p>I forgot to mention - I chose “Add Link” option in Slicer while importing the dataset.</p>

---

## Post #5 by @pieper (2017-08-22 22:35 UTC)

<p>Yes, we should profile this.  I suspect it’s either the tagCache using sqlite inefficiently or unneeded updates of the widget, but it would be good to know and fix.</p>

---

## Post #6 by @fedorov (2017-08-22 22:45 UTC)

<p>I logged an issue <a href="https://issues.slicer.org/view.php?id=4420">https://issues.slicer.org/view.php?id=4420</a></p>

---

## Post #7 by @jcfr (2017-08-23 03:40 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> It takes 11 seconds to import the complete folder. Considering my hard drive is very efficient  (SSD NVME) … I would expect it to be faster.</p>

---

## Post #8 by @fedorov (2017-08-23 03:55 UTC)

<p>Both for mitk and Slicer?</p>
<p>Anyway, I reported the time comparison on the same Linux box.</p>

---

## Post #9 by @jcfr (2017-08-23 03:57 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Both for mitk and Slicer?</p>
</blockquote>
</aside>
<p>Only Slicer, 11 seconds is to slow. I am profiling and experimenting with few approaches.</p>

---

## Post #10 by @jcfr (2017-08-23 04:06 UTC)

<p>I instrumented CTK to report some timing.</p>
<pre><code class="lang-auto">"DICOM indexer has successfully processed 556 files [8.12s]"
</code></pre>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/commontk/CTK/pull/739" target="_blank">github.com/commontk/CTK</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/pull/739" target="_blank">ENH: Update ctkDICOMIndexer to report indexing time in seconds</a>
    </h4>

    <div class="branches">
      <code>commontk:master</code> ← <code>jcfr:dicom-report-indexing-time</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2017-08-23" data-time="04:06:09" data-timezone="UTC">04:06AM - 23 Aug 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 15 additions and 0 deletions">
        <a href="https://github.com/commontk/CTK/pull/739/files" target="_blank">
          <span class="added">+15</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #11 by @jcfr (2017-08-23 05:25 UTC)

<p>By commenting out this line, import time is reduced by a factor 2.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/1f3eba2282b892cc0603cb29d31f7949459944f0/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L428" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/1f3eba2282b892cc0603cb29d31f7949459944f0/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L428" target="_blank" rel="nofollow noopener">commontk/CTK/blob/1f3eba2282b892cc0603cb29d31f7949459944f0/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L428</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="418" style="counter-reset: li-counter 417 ;">
<li>{</li>
<li>Q_D(ctkDICOMBrowser);</li>
<li>return d-&gt;dicomTableManager;</li>
<li>}</li>
<li>
</li>
<li>//----------------------------------------------------------------------------</li>
<li>void ctkDICOMBrowser::onFileIndexed(const QString&amp; filePath)</li>
<li>{</li>
<li>// Update the progress dialog when the file name changes</li>
<li>// - also allows for cancel button</li>
<li class="selected">QCoreApplication::instance()-&gt;processEvents();</li>
<li>qDebug() &lt;&lt; "Indexing \n\n\n\n" &lt;&lt; filePath &lt;&lt;"\n\n\n";</li>
<li>
</li>
<li>}</li>
<li>
</li>
<li>//----------------------------------------------------------------------------</li>
<li>void ctkDICOMBrowser::openImportDialog()</li>
<li>{</li>
<li>Q_D(ctkDICOMBrowser);</li>
<li>
</li>
<li>d-&gt;ImportDialog-&gt;show();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<pre><code class="lang-auto">"DICOM indexer has successfully processed 556 files [3.39s]"
</code></pre>

---

## Post #12 by @lassoan (2017-08-23 13:17 UTC)

<p>That is a significant improvement!</p>
<p>It would be useful to keep the possibility of cancelling the import, so instead of removing the line, we could add a check which would only allow processing of events if at least a few seconds has passed since the last processing.</p>

---

## Post #13 by @fedorov (2017-08-23 13:26 UTC)

<p>I agree, improvement of factor of 2 is great. If we could get to factor of 10 to be on par with CTK (and probably much closer to OsiriX), this would be perfect!</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> thank you for investigating this issue! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #14 by @jcfr (2017-08-23 17:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>so instead of removing the line, we could add a check which would only allow processing of events if at least a few seconds has passed since the last processing.</p>
</blockquote>
</aside>
<p>I was able to successfully close the dialog without that line on both Qt4 and Qt5 on Linux. Can someone try on windows ?</p>
<p>This line was added back in 2013 … it doesn’t seem to be useful anymore</p>
<blockquote>
<p>If we could get to factor of 10 to be on par with CTK</p>
</blockquote>
<p>For reference, MITK is not doing anything is special with CTKDICOM:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/MITK/MITK/blob/cf6879c304025341d6e99c2aa13f6ee7f700dba0/Modules/DicomUI/src/QmitkDicomLocalStorageWidget.cpp#L67-L81">
  <header class="source">

      <a href="https://github.com/MITK/MITK/blob/cf6879c304025341d6e99c2aa13f6ee7f700dba0/Modules/DicomUI/src/QmitkDicomLocalStorageWidget.cpp#L67-L81" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/MITK/MITK/blob/cf6879c304025341d6e99c2aa13f6ee7f700dba0/Modules/DicomUI/src/QmitkDicomLocalStorageWidget.cpp#L67-L81" target="_blank" rel="noopener">MITK/MITK/blob/cf6879c304025341d6e99c2aa13f6ee7f700dba0/Modules/DicomUI/src/QmitkDicomLocalStorageWidget.cpp#L67-L81</a></h4>



    <pre class="onebox"><code class="lang-cpp">
      <ol class="start lines" start="67" style="counter-reset: li-counter 66 ;">
          <li>void QmitkDicomLocalStorageWidget::OnStartDicomImport(const QString &amp;dicomData)</li>
          <li>{</li>
          <li>  if (m_LocalDatabase-&gt;isOpen())</li>
          <li>  {</li>
          <li>    m_LocalIndexer-&gt;addDirectory(*m_LocalDatabase, dicomData, m_LocalDatabase-&gt;databaseDirectory());</li>
          <li>  }</li>
          <li>}</li>
          <li></li>
          <li>void QmitkDicomLocalStorageWidget::OnStartDicomImport(const QStringList &amp;dicomData)</li>
          <li>{</li>
          <li>  if (m_LocalDatabase-&gt;isOpen())</li>
          <li>  {</li>
          <li>    m_LocalIndexer-&gt;addListOfFiles(*m_LocalDatabase, dicomData, m_LocalDatabase-&gt;databaseDirectory());</li>
          <li>  }</li>
          <li>}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #15 by @pieper (2017-08-23 17:58 UTC)

<p>I did some profiling and about 50% of the time is spent in precacheTags, which is the part of the code that allows DICOMPlugins to save header values that they want to have fast access to in the future.  This is being done as an sqlite transaction per-dicom object, but maybe there is a more efficient way to do this.  Perhaps the tags can be stored in memory and then pushed to the database in one transaction when the parsing is finished (ideally the database transaction would be done in the background, but I don’t think that’s possible with sqlite).</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDatabase.cpp#L1262-L1286" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDatabase.cpp#L1262-L1286" target="_blank" rel="nofollow noopener">commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDatabase.cpp#L1262-L1286</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="1262" style="counter-reset: li-counter 1261 ;">
<li>
</li>
<li>//------------------------------------------------------------------------------</li>
<li>const QStringList ctkDICOMDatabase::tagsToPrecache()</li>
<li>{</li>
<li>Q_D(ctkDICOMDatabase);</li>
<li>return d-&gt;TagsToPrecache;</li>
<li>}</li>
<li>
</li>
<li>//------------------------------------------------------------------------------</li>
<li>bool ctkDICOMDatabasePrivate::openTagCacheDatabase()</li>
<li>{</li>
<li>// try to open the database if it's not already open</li>
<li>if ( this-&gt;TagCacheDatabase.isOpen() )</li>
<li>  {</li>
<li>  return true;</li>
<li>  }</li>
<li>this-&gt;TagCacheDatabase = QSqlDatabase::addDatabase(</li>
<li>      "QSQLITE", this-&gt;Database.connectionName() + "TagCache");</li>
<li>this-&gt;TagCacheDatabase.setDatabaseName(this-&gt;TagCacheDatabaseFilename);</li>
<li>if ( !this-&gt;TagCacheDatabase.open() )</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDatabase.cpp#L1262-L1286" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #16 by @lassoan (2017-08-23 21:21 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="14" data-topic="922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>lassoan:</p>
<p>so instead of removing the line, we could add a check which would only allow processing of events if at least a few seconds has passed since the last processing.</p>
<p>I was able to successfully close the dialog without that line on both Qt4 and Qt5 on Linux. Can someone try on windows ?</p>
</blockquote>
</aside>
<p>I’ll try this on Windows with Qt4.</p>

---

## Post #17 by @jcfr (2017-08-24 02:34 UTC)

<p>Here is the latest PR: <a href="https://github.com/commontk/CTK/pull/740">https://github.com/commontk/CTK/pull/740</a></p>
<p>With this commit, I managed to go from 3.3s to 2.9s.</p>
<p><a href="https://github.com/commontk/CTK/pull/740/commits/1e92bdcb4fc829823d7ae65bfbdbb39ace748557" class="onebox" target="_blank">https://github.com/commontk/CTK/pull/740/commits/1e92bdcb4fc829823d7ae65bfbdbb39ace748557</a></p>

---

## Post #18 by @lassoan (2017-08-24 16:38 UTC)

<p>The changes work without problems on Windows with Qt4.</p>
<p>I’ve made some speed measurements on loading 6 CTs:</p>
<ul>
<li>With patched CTK of this PR: DICOM indexer has successfully processed 1554 files [255.59s]</li>
<li>If I comment out this-&gt;precacheTags(sopInstanceUID) call in ctkDICOMDatabase: DICOM indexer has successfully processed 1554 files [9.78s] !!!</li>
</ul>
<p>There are some good tips on improving SQLite insert speed:<br>
<aside class="onebox stackexchange">
  <header class="source">
      <a href="https://stackoverflow.com/questions/1711631/improve-insert-per-second-performance-of-sqlite" target="_blank">stackoverflow.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/203690/mike-willekes" target="_blank">
    <img alt="Mike Willekes" src="https://www.gravatar.com/avatar/bc7f81a3f1fe45bede6ebb302e60338a?s=128&amp;d=identicon&amp;r=PG" class="thumbnail onebox-avatar" width="128" height="128">
  </a>
<h4>
  <a href="https://stackoverflow.com/questions/1711631/improve-insert-per-second-performance-of-sqlite" target="_blank">Improve INSERT-per-second performance of SQLite</a>
</h4>

<div class="tags">
  <strong>c, performance, sqlite, optimization</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/203690/mike-willekes" target="_blank">
    Mike Willekes
  </a>
  on <a href="https://stackoverflow.com/questions/1711631/improve-insert-per-second-performance-of-sqlite" target="_blank">10:16PM - 10 Nov 09 UTC</a>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
It seems that the most significant improvement (to 85 inserts/sec to 23000 inserts/sec) by using transactions.</p>
<p>After some investigation I’ve found a bug in how transactions is set up for inserting tagcache values. Actually, a transaction is created for the DICOM patient database and not for tag cache!</p>
<p><strong>This change inctkDICOMDatabasePrivate::precacheTags decreases import time from 255 sec to 19 sec!</strong></p>
<p>Before:</p>
<pre>  this-&gt;beginTransaction();
  q-&gt;cacheTags(sopInstanceUIDs, tags, values);
  this-&gt;endTransaction();
</pre>
<p>After:</p>
<pre>  QSqlQuery transaction(this-&gt;TagCacheDatabase);
  transaction.prepare("BEGIN TRANSACTION");
  transaction.exec();
  q-&gt;cacheTags(sopInstanceUIDs, tags, values);
  QSqlQuery transaction2(this-&gt;TagCacheDatabase);
  transaction2.prepare("END TRANSACTION");
  transaction2.exec();
</pre>
<p>Probably if we start/end the transaction for all files at once then it would further improve the speed.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Could you add this to your branch and test if using this change you get a significant speed improvement, too?</p>

---

## Post #19 by @fedorov (2017-08-24 16:52 UTC)

<p>This sounds really great!</p>
<p>I can test after Friday.</p>

---

## Post #20 by @jcfr (2017-08-24 17:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you add this to your branch and test if using this change you get a significant speed improvement, too?</p>
</blockquote>
</aside>
<p>With this change in place, I get the following stats:</p>
<pre><code class="lang-auto">"DICOM indexer has successfully processed 556 files [2.12s]"
</code></pre>

---

## Post #21 by @lassoan (2017-08-24 17:57 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Very good, thanks for testing. Do you have time to implement this properly in your branch?<br>
At least we should create beginTagCacheTransaction() / endTagCacheTransaction() methods. Maybe also update the code to do all tag cache updates in one transaction per directory or per import session - if it makes things much faster. To test, you might use a slower computer or larger data set (e.g., from <a href="http://www.cancerimagingarchive.net/">http://www.cancerimagingarchive.net/</a>), as your few-second import times are already very good.</p>

---

## Post #22 by @jcfr (2017-08-24 18:25 UTC)

<p>Makes sense.</p>
<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you have time to implement this properly in your branch?</p>
</blockquote>
</aside>
<p>I do not have the bandwidth to address this. In the mean time, I integrated the topic and will  update Slicer.</p>

---

## Post #23 by @lassoan (2017-08-24 19:45 UTC)

<p>Thank you. I’ll follow up with another pull request if I find that further optimization of transactions make a significant impact.</p>

---

## Post #24 by @GiulioBen (2019-08-05 11:54 UTC)

<p>I imported more or less 60 MR multislice images with about 1000 400x400px slices for a total of 10 Gpx and it took 2 hours.<br>
Is it normal? Is it not?</p>
<p>Thank you.</p>

---

## Post #25 by @lassoan (2019-08-05 14:00 UTC)

<p>A CT volume is imported and loaded from DICOM files in about 10-20 seconds on an average computer (using Slicer or most other medical imaging software). Since size of this data set is equivalent to about 600 CT volumes, 120 minutes may be normal.</p>
<p>Since the size of this data set is extreme, your computer will need to have extreme specifications if you want to have good performance. You would need at least 32GB physical RAM but preferably 128GB if you want to manipulate the volume. You would also benefit from fast SSD storage.</p>
<p>You can access the data 1-2 magnitudes faster if you store the data in nrrd format. Make sure you disable compression.</p>
<p>What would you like to do with this data set?</p>

---
