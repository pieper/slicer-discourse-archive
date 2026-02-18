# Where to set "Move Storage port" in ctkDICOMRetrieve?

**Topic ID**: 18915
**Date**: 2021-07-25
**URL**: https://discourse.slicer.org/t/where-to-set-move-storage-port-in-ctkdicomretrieve/18915

---

## Post #1 by @rbumm (2021-07-25 10:56 UTC)

<p>I am having problems implementing this code snippet for automatic data retrieval in our hospital network:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#query-and-retrieve-data-from-a-pacs-using-classic-dimse-dicom-networking" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#query-and-retrieve-data-from-a-pacs-using-classic-dimse-dicom-networking</a></p>
<p>The code works well on my private laptop in a public network.</p>
<p>In the hospital I need to be able to set, besides the MoveDestinationAETitle,  the StoragePort as in Slicers DICOM Query/Retrieve dialog here (11112)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0b987f842e15792cee71ec7ab32bc519c5f5385.png" alt="image" data-base62-sha1="w40s1tExXBsIBqfi6Nv1Uit7FkN" width="377" height="74"></p>
<p>The query works from the dialog window in hospital (using our local PACS access data), but access negotiations fail from the snippet. I think it is because the StoragePort needs to be defined in the python code  because the PACS is configured to write to 11112</p>
<p>Any ideas ? Thank you !</p>

---

## Post #2 by @pieper (2021-07-25 19:28 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a>  -</p>
<p>Perhaps you have the same issue as discussed in this thread?  <a class="mention" href="/u/amy_morton">@Amy_Morton</a> also links to some documentation that helped explain the various requirements.</p>
<aside class="quote" data-post="1" data-topic="13754">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amy_morton/48/67318_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/configuration-of-the-3d-slicer-dicom-listener-to-hospital-ct/13754">Configuration of the 3D Slicer DICOM Listener to Hospital CT</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Win 10 
Slicer version: 4.10.2 
Expected behavior: a dialog with accessible port configurations 
Actual behavior: none found 
Beyond the ‘Start Listener’ button in the DICOM module, I cannot configure the listener such that datasets can be pushed to my PC from the the hospital CT scanner (same LAN).
  </blockquote>
</aside>


---

## Post #3 by @rbumm (2021-07-28 16:29 UTC)

<p>Hi guys,</p>
<p>it turned out that setting the “Move Storage Port” is not necessary but it was required to use setCallingAETitle, setCalledAETitle, setHost, setPort in the <code>dicomRetrieve </code> class to make this work with our GEPACS.</p>
<p>So I changed the code from the repository (<a class="mention" href="/u/lassoan">@lassoan</a> maybe update?) to:</p>
<pre><code class="lang-auto"># Query
dicomQuery = ctk.ctkDICOMQuery()
dicomQuery.callingAETitle = "SLICER"
dicomQuery.calledAETitle = "ANYAE"
dicomQuery.host = "dicomserver.co.uk"
dicomQuery.port = 11112
dicomQuery.preferCGET = True
dicomQuery.filters = {"Name":"Anon", "Modalities":"MR"}
# temporary in-memory database for storing query results
tempDb = ctk.ctkDICOMDatabase()
tempDb.openDatabase("")
dicomQuery.query(tempDb)

# Retrieve
dicomRetrieve = ctk.ctkDICOMRetrieve()
dicomRetrieve.setCallingAETitle(dicomQuery.callingAETitle)
dicomRetrieve.setCalledAETitle(dicomQuery.calledAETitle)
dicomRetrieve.setHost(dicomQuery.host)
dicomRetrieve.setPort(dicomQuery.port)
dicomRetrieve.setMoveDestinationAETitle("SLICER") 
dicomRetrieve.setDatabase(slicer.dicomDatabase)
for study in dicomQuery.studyInstanceUIDQueried:
  print(f"ctkDICOMRetrieveTest2: Retrieving {study}")
  slicer.app.processEvents()
  if dicomQuery.preferCGET:
    success = dicomRetrieve.getStudy(study)
  else:
    success = dicomRetrieve.moveStudy(study)
  print(f"  - {'success' if success else 'failed'}")
slicer.dicomDatabase.updateDisplayedFields()´´´
</code></pre>
<p>and now this code works in the hospital setting.</p>
<p>On the dicomQuery side, a dicomQuery.setCallingAETitle seems not yet to be exposed to python and results in an error message.</p>

---

## Post #4 by @pieper (2021-07-28 21:22 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="3" data-topic="18915">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>On the dicomQuery side, a dicomQuery.setCallingAETitle seems not yet to be exposed to python and results in an error message.</p>
</blockquote>
</aside>
<p>Thanks for pointing out this inconsistency.  The preferred way would be to use <code>dicomRetrieve.callingAETitle = dicomQuery.callingAETitle</code> since both classes have those values exposed as properties, but only <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMRetrieve.h">ctkDICOMRetrieve</a> exposes the Q_INVOKABLE versions.  Probably at this point we should add Q_INVOKABLE to the corresponding methods in <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMQuery.h">ctkDICOMQuery</a> for consistency, but properties are usually better to use if where they exist.</p>

---

## Post #6 by @lassoan (2021-08-01 12:08 UTC)

<p>The script repository does not need an update, there was just a copy-paste error in definition of the calledAETitle property in CTK:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/commontk/CTK/pull/988/commits/949607ea154f9f73468782bfdd5bad7a3aff9f3f">
  <header class="source">

      <a href="https://github.com/commontk/CTK/pull/988/commits/949607ea154f9f73468782bfdd5bad7a3aff9f3f" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/pull/988" target="_blank" rel="noopener">BUG: Fix ctkDICOMRetrieve::calledAETitle property setting method</a>
    </h4>

    <div class="branches">
      <code>commontk:master</code> ← <code>lassoan:fix-dicomquery</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-01" data-time="12:06:46" data-timezone="UTC">12:06PM - 01 Aug 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/commontk/CTK/pull/988/files" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixed copy-paste error.</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
