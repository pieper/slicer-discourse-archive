---
topic_id: 15693
title: "Load Dicom Data Via Networking With Python Script"
date: 2021-01-27
url: https://discourse.slicer.org/t/15693
---

# Load DICOM data via "networking" with python script?

**Topic ID**: 15693
**Date**: 2021-01-27
**URL**: https://discourse.slicer.org/t/load-dicom-data-via-networking-with-python-script/15693

---

## Post #1 by @rbumm (2021-01-27 12:17 UTC)

<p>Hi,</p>
<p>what would be the recommended way to realize DICOM network access via python script? We would need to load all CT scans of a patient (defined by patient ID) of a certain time period into Slicers DICOM database,  then process data later. DICOM networking via GUI works well here.</p>
<p>Thanks and best regards<br>
Rudolf</p>

---

## Post #2 by @pieper (2021-01-27 14:05 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a> -</p>
<p>I’m guessing you mean traditional dicom networking (a.k.a. “DIMSE”) since that is the very common standard, compared to the newer DICOMweb standard (if your PACS or VNA supports DICOMweb that’s cleaner).</p>
<p>For DIMSE, Slicer uses a combination of C++ and python.  The CFIND, CMOVE type transactions are in <a href="https://github.com/commontk/CTK/tree/master/Libs/DICOM/Core">CTK</a> C++ but should all be exposed and usable in python.  For the listener (CSTORE SCP) we use the dcmtk command line <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMProcesses.py">executable in a separate process</a> in python.</p>
<p>If your PACS supports CGET, you are probably best to use <a href="https://support.dcmtk.org/docs-dcmrt/getscu.html">getscu</a> into a temp directory and then load into the database.  Let us know if you need more pointers.</p>

---

## Post #3 by @rbumm (2021-01-27 16:03 UTC)

<p>Thank you Steve.</p>
<p>To be able to pull from our GE-PACS, we needed to</p>
<ul>
<li>specify Calling AETitle</li>
<li>specify the StorageAETitle</li>
<li>specify three port adresses</li>
<li>the 4100 port</li>
<li>
<strong>disable</strong> CGET</li>
</ul>
<p>in slicers DICOM Query/Receive. This works reliably.<br>
So probably getscu is not the appropriate script option?</p>

---

## Post #4 by @pieper (2021-01-27 19:52 UTC)

<p>Right, if you can’t use CGET then you need to be running the Slicer listener and then do the CFIND to get the list of instances and CMOVE to tell them to be transferred to Slicer’s listener.  This can be done using dcmtk command line tools but that might not be cleanest.</p>
<p>It’s been been about a decade since we did all that code, but I’m pretty sure everything you need is exposed in python if you use the ctkDICOMQuery and ctkDICOMRetrieve classes.  These are what the GUI uses under the hood and it looks like all the methods are exposed.  The ctk doxygen is down, but if you look in the header files you’ll find what you need.</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/commontk/CTK/tree/master/Libs/DICOM/Core" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars.githubusercontent.com/u/300358?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/commontk/CTK/tree/master/Libs/DICOM/Core" target="_blank" rel="noopener">commontk/CTK</a></h3>

<p><a href="https://github.com/commontk/CTK/tree/master/Libs/DICOM/Core" target="_blank" rel="noopener">master/Libs/DICOM/Core</a></p>

  <p><span class="label1">A set of common support code for medical imaging, surgical navigation, and related purposes.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>And you can see how they are used by the widget code - it should just be a matter of using the same API from python.  Hope that helps!</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMQueryRetrieveWidget.cpp#L151-L395" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMQueryRetrieveWidget.cpp#L151-L395" target="_blank" rel="noopener">commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMQueryRetrieveWidget.cpp#L151-L395</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="151" style="counter-reset: li-counter 150 ;">
<li>void ctkDICOMQueryRetrieveWidget::query()</li><li>{</li><li>  Q_D(ctkDICOMQueryRetrieveWidget);</li><li></li><li>  d-&gt;RetrieveButton-&gt;setEnabled(false);</li><li></li><li>  if (!d-&gt;QueryResultDatabase.isOpen())</li><li>  {</li><li>    // create a database in memory to hold query results</li><li>    try</li><li>    {</li><li>      d-&gt;QueryResultDatabase.openDatabase(":memory:");</li><li>    }</li><li>    catch (std::exception e)</li><li>    {</li><li>      logger.error("Database error: " + d-&gt;QueryResultDatabase.lastError());</li><li>      d-&gt;QueryResultDatabase.closeDatabase();</li><li>      return;</li><li>    }</li><li>  }</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMQueryRetrieveWidget.cpp#L151-L395" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @rbumm (2021-02-02 12:57 UTC)

<p>Thank you Steve.</p>
<p>In my DICOM retrieval extension</p>
<code>
import ctk
<p>…</p>
<p>query = ctk.ctkDICOMQuery</p>
<p>query.setCalledAETitle(“SLICER”)</p>
<p>query.setHost(“SRVXXX”)</p>
<p>query.setPort(1234)</p>
<p>query.setPreferCGET(False)</p>
<p>QMap&lt;QString,QVariant&gt; filters</p>
<p>filters[“ID”] = QString(studyID)</p>
<p>query.setFilters(filters)</p>
</code>
<p>results in</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/152d7397a38d84c0de6b2a1723f50ea2f8965d9e.png" alt="image" data-base62-sha1="31lpbXVApKNANeDtd5A6z3UcqzY" width="457" height="95"></p>
<p>Am I missing anything here ?</p>
<p>Thanks &amp; best regards<br>
Rudolf</p>

---

## Post #6 by @lassoan (2021-02-02 13:10 UTC)

<p><code>ctkDICOMQuery</code> is a Qt class and <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMQuery.h#L42-L46"><code>calledAETitle</code> is a property</a>, which can be read/written in Python by its name (without <code>set...</code> prefix). See more information about how to translate C++ to Python <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#doxygen-style-documentation">here</a>.</p>

---

## Post #7 by @rbumm (2021-02-02 19:22 UTC)

<p>Thanks Andras, but I am nowhere near it , sorry.</p>
<p>What I tried:</p>
<pre><code>query = ctk.ctkDICOMQuery
query.CalledAETitle = "SLICER"
query.Host = "SRVxxx"
query.Port = nnnn
query.PreferCGET= False
filters = {'Name':'', 'Study':'', 'Series':'', 'ID':'', 'Modalities':'', 'StartDate':'', 'EndDate':''}  
filters["ID"] = studyID 
query.Filters = filters
query.query(???)
</code></pre>
<p>Is the problem related to</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Why_can.27t_I_access_my_C.2B.2B_Qt_class_from_python" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Why_can.27t_I_access_my_C.2B.2B_Qt_class_from_python</a></p>
<p>maybe ?</p>

---

## Post #8 by @lassoan (2021-02-02 20:49 UTC)

<p>I’v added a complete working example to the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Query_and_retrieve_data_from_a_PACS_using_classic_DIMSE_DICOM_networking" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<p>I had to <a href="https://github.com/commontk/CTK/commit/f670e1d0e513bae9d08257b883aaf669f546053d">fix a few small issues in the ctkDICOMQuery</a> class Python wrapping, so you can use this code with Slicer Preview Release that you download tomorrow or later.</p>

---

## Post #9 by @rbumm (2021-02-02 21:11 UTC)

<p>Never ever saw such a great support anywhere.<br>
At least I was on the right track somehow <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Thank you Andras!!<br>
I will implement that and report back during the next days …</p>

---

## Post #10 by @lassoan (2021-02-02 22:16 UTC)

<p>It is nice to hear this. It would be great if you could write a few sentences about this good experience here:</p>
<aside class="onebox category-onebox" style="box-shadow: -5px 0px #92278F;">
  <article class="onebox-body category-onebox-body">
    <h3>
      <a class="badge-wrapper bullet" href="/c/community/success-stories/29">
          <span class="badge-category-bg" style="background-color: #92278F"></span>
        <span class="clear-badge"><span>Success stories</span></span>
      </a>
    </h3>
      <div>
        <span class="description">
          <p>This is the place where you can share how Slicer helped your work. Describe your project and how Slicer was useful in achieving your goal. Include reference to any publication(s) and if possible also add a few nice images or links to videos.</p>
        </span>
      </div>
  </article>
  <div class="clearfix"></div>
</aside>

<p>Having a list of success stories could help with getting grant funding for Slicer.</p>

---

## Post #11 by @rbumm (2021-02-03 10:16 UTC)

<p>Of course, Andras. Just done.</p>

---

## Post #12 by @rbumm (2021-02-04 11:52 UTC)

<p>I just tried the above mentioned code after installation of<br>
Slicer preview release 4.13.0 rev 29684 build 21-02-04</p>
<p>tempDb.open(’’)</p>
<p>throws the following error:</p>
<p>AttributeError: ctkDICOMDatabase has no attribute named ‘open’</p>

---

## Post #13 by @rbumm (2021-02-04 12:56 UTC)

<p>Looked into <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/ctkDICOMDatabase.h" class="inline-onebox" rel="noopener nofollow ugc">CTK/ctkDICOMDatabase.h at master · commontk/CTK · GitHub</a></p>
<p>and changed</p>
<p>tempDb.open(’’)</p>
<p>to</p>
<p><strong>tempDb.openDatabase(’’)</strong></p>
<p>DICOM Query and Receive works great now !</p>

---

## Post #14 by @rbumm (2021-02-05 16:46 UTC)

<p>During the implementation of <a class="mention" href="/u/lassoan">@lassoan</a> 's script example I face the following problem:<br>
The script works well with the public DICOM server, but does not work within the hospital setting. It returns a “failed” move operation upon retrieving the images.</p>
<p>The query itself seems to work fine and finds three CT series for a specific patient ID (which is correct)</p>
<p>All parameters are set exactly as I would do in the DICOM networking widget.</p>
<p>Is it possible that the function</p>
<p>dicomRetrieve.setMoveDestinationAETitle(“XXXXX”)</p>
<p>is not exposed yet?</p>
<p>I also tried</p>
<p>dicomRetrieve.moveDestinationAETitle = “XXXXX”</p>
<p>with no luck.</p>
<p>I need to set the retriever (“XXXXX”, the computer which makes the DICOM retrieve call) in the widget form field “Storage AETitle”, otherwise, the widget networking call would not work.</p>
<p>Second info:</p>
<p>I normally use it from the widget with CGET unchecked, but from the widget, it also works with CGET checked.</p>

---

## Post #15 by @pieper (2021-02-05 19:30 UTC)

<p>Debugging DIMSE networking is always a challenge.  Both sides need to be configured just right, but it sounds like you are close.</p>
<aside class="quote no-group" data-username="rbumm" data-post="14" data-topic="15693">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Is it possible that the function</p>
<p>dicomRetrieve.setMoveDestinationAETitle(“XXXXX”)</p>
<p>is not exposed yet?</p>
<p>I also tried</p>
<p>dicomRetrieve.moveDestinationAETitle = “XXXXX”</p>
<p>with no luck.</p>
</blockquote>
</aside>
<p>Hmm, these appear be exposed correctly and that should match what’s happening in the GUI implementation.</p>
<aside class="quote no-group" data-username="rbumm" data-post="14" data-topic="15693">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>I normally use it from the widget with CGET unchecked, but from the widget, it also works with CGET checked.</p>
</blockquote>
</aside>
<p>In this case then you could try using the <code>bool ctkDICOMRetrieve::getStudy(const QString&amp; studyInstanceUID)</code> or <code>bool getSeries( const QString&amp; studyInstanceUID,  const QString&amp; seriesInstanceUID )</code> methods?  If the PACS side supports it then this is less tricky to configure.</p>

---

## Post #16 by @rbumm (2021-02-06 08:11 UTC)

<p>This widget call works with query and retrieve:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7ca30040a4abf88d7977c8cc731a546c499b8b71.png" data-download-href="/uploads/short-url/hMAqVAZL5KD8KpWQJNPaJeSh3t7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7ca30040a4abf88d7977c8cc731a546c499b8b71.png" alt="image" data-base62-sha1="hMAqVAZL5KD8KpWQJNPaJeSh3t7" width="499" height="499" data-dominant-color="DCE7F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">829×829 36.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The next call works with query, but not with receive (I only changed the Storage AETitle to a wrong parameter):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2ba0d809ab35abae74de3a72ef5b6b7cf6d108b.png" data-download-href="/uploads/short-url/yDgaasZviBh5WniVIKid1keqqsb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2ba0d809ab35abae74de3a72ef5b6b7cf6d108b.png" alt="image" data-base62-sha1="yDgaasZviBh5WniVIKid1keqqsb" width="497" height="500" data-dominant-color="DDE8F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">838×842 37.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I get only a short popup and no DICOM download.</p>
<p>So retrieve works from the widget and setting the Storage AE Title correctly  is crucial.</p>

---

## Post #18 by @rbumm (2021-02-06 09:33 UTC)

<p>Then I run:</p>
<pre><code class="lang-auto"># Query
dicomQuery = ctk.ctkDICOMQuery()
dicomQuery.callingAETitle = "CKL1757"
dicomQuery.calledAETitle = "GPACS"
dicomQuery.host = "S078"
dicomQuery.port = 4001
dicomQuery.preferCGET = False
dicomQuery.filters = {'ID':'xxxxxxxxxx', 'Modalities':'CT'}    


# temporary in-memory database for storing query results
tempDb = ctk.ctkDICOMDatabase()
tempDb.openDatabase('')
dicomQuery.query(tempDb)

# Retrieve
dicomRetrieve = ctk.ctkDICOMRetrieve()
dicomRetrieve.callingAETitle = dicomQuery.callingAETitle
dicomRetrieve.calledAETitle = dicomQuery.calledAETitle
dicomRetrieve.host = dicomQuery.host
dicomRetrieve.port = dicomQuery.port
dicomRetrieve.moveDestinationAETitle = "CKL1757"
dicomRetrieve.setDatabase(slicer.dicomDatabase)


for study in dicomQuery.studyInstanceUIDQueried:
    print(f"ctkDICOMRetrieveTest: Retrieving &gt;{study}&lt;")
    slicer.app.processEvents()
    if dicomQuery.preferCGET:
        print(f"getting ...")
        success = dicomRetrieve.getStudy(study)
    else:
        print(f"moving ...")
        success = dicomRetrieve.moveStudy(study)
    print(f"  - {'success' if success else 'failed'}")

slicer.dicomDatabase.updateDisplayedFields()
</code></pre>
<p>and get three times "moving → “failed” for the three correctly detected CT datasets</p>
<p>Same happens if I set</p>
<p>dicomQuery.preferCGET = True</p>
<p>→ three times "getting → “failed” for the three correctly detected CT datasets</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10ca3d32967cb1fafa348800df22b0a6175c1127.png" data-download-href="/uploads/short-url/2owVWZeQeyafyh8rjrYqYF4RYft.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ca3d32967cb1fafa348800df22b0a6175c1127_2_394x500.png" alt="image" data-base62-sha1="2owVWZeQeyafyh8rjrYqYF4RYft" width="394" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ca3d32967cb1fafa348800df22b0a6175c1127_2_394x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ca3d32967cb1fafa348800df22b0a6175c1127_2_591x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10ca3d32967cb1fafa348800df22b0a6175c1127.png 2x" data-dominant-color="EBEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×852 36.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any idea what could be the difference between the widget call (working) and the script call (failed) ?</p>

---

## Post #19 by @lassoan (2021-02-06 14:13 UTC)

<p>The widget also sets how associations are handled, try to set that in your script:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/f670e1d0e513bae9d08257b883aaf669f546053d/Libs/DICOM/Widgets/ctkDICOMQueryRetrieveWidget.cpp#L299" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/f670e1d0e513bae9d08257b883aaf669f546053d/Libs/DICOM/Widgets/ctkDICOMQueryRetrieveWidget.cpp#L299" target="_blank" rel="noopener">commontk/CTK/blob/f670e1d0e513bae9d08257b883aaf669f546053d/Libs/DICOM/Widgets/ctkDICOMQueryRetrieveWidget.cpp#L299</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="289" style="counter-reset: li-counter 288 ;">
<li>  progress.setMinimumDuration(0);</li><li>  progress.setValue(0);</li><li>  progress.setMaximum(0);</li><li>  progress.setAutoClose(false);</li><li>  progress.show();</li><li>  }</li><li></li><li>QMap&lt;QString,QVariant&gt; serverParameters = d-&gt;ServerNodeWidget-&gt;parameters();</li><li>ctkDICOMRetrieve *retrieve = new ctkDICOMRetrieve;</li><li>// only start new association if connection parameters change</li><li class="selected">retrieve-&gt;setKeepAssociationOpen(true);</li><li>// pull from GUI</li><li>retrieve-&gt;setMoveDestinationAETitle( serverParameters["StorageAETitle"].toString() );</li><li></li><li>// do the rerieval for each selected series</li><li>// that is selected in the tree view</li><li>QStringList selectedSeriesUIDs = d-&gt;dicomTableManager-&gt;currentStudiesSelection();</li><li>foreach( QString studyUID, selectedSeriesUIDs )</li><li>  {</li><li>  std::cout&lt;&lt;studyUID.toUtf8().constData()&lt;&lt;std::endl;</li><li>  if(d-&gt;UseProgressDialog)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #20 by @rbumm (2021-02-06 16:41 UTC)

<p>Unfortunately, neither</p>
<p>dicomRetrieve.setKeepAssociationOpen(True)</p>
<p>nor</p>
<p>dicomRetrieve.keepAssociationOpen = True</p>
<p>changed anything …</p>

---

## Post #21 by @rbumm (2021-02-06 17:51 UTC)

<p>The observation with the widget is: Takes quite a long time interval until the popup “Got a move request” is displayed (20 s), then it is again quite slow but realiable to retieve the data.</p>
<p>With the script, the query takes place almost instantly, the failed retrieval requests print messages are within 3 s.<br>
I suspect a timing problem … if I could I would check logs on the server side, but I have no access myself  and it is extremely difficult to get hold of the PACS guy</p>

---

## Post #22 by @pieper (2021-02-06 18:34 UTC)

<p>Unfortunately this kind of thing almost always requires debugging logs from both sides, or even a network packet sniffer.  Keep bugging the PACS guy I guess.</p>
<p>In the meantime sometimes it’s easier to use dcmtk directly for debugging.  <a href="https://www.na-mic.org/wiki/CTSC:ARRA:Mockup">Here are some notes</a> about how to use the dcmtk command line utilities directly to do a a CFIND and you can also use the <code>movescu</code> command to initiate a CMOVE transfer.  Internally Slicer uses the <code>storescp</code> command so you can look in the task manager to see the command line arguments when you have the listener running.</p>

---

## Post #23 by @rbumm (2021-02-06 19:09 UTC)

<p>Thank you both!<br>
Which task manager should I look into? I am on Windows …</p>

---

## Post #24 by @pieper (2021-02-06 19:39 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="23" data-topic="15693">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Which task manager should I look into? I am on Windows …</p>
</blockquote>
</aside>
<p>It should be visible on the one you get with Control-Alt-Delete I have (<a href="https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer">Process Explorer</a> installed as my task manager so can’t check easily how to see the command line parameters in the default one but I’m pretty sure it’s possible).  Really all you will see is the port number that it is using, which is the one you set in the dialog, and the temp directory where images will be stored.  So maybe not all that important, but just more background info for debugging.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f47ac0356d4fa7fd8f6d4ed7e69ec4216d15a1da.jpeg" data-download-href="/uploads/short-url/ySLuHxCnpTGMEqpc0XAU8D8hd2i.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f47ac0356d4fa7fd8f6d4ed7e69ec4216d15a1da_2_690x136.jpeg" alt="image" data-base62-sha1="ySLuHxCnpTGMEqpc0XAU8D8hd2i" width="690" height="136" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f47ac0356d4fa7fd8f6d4ed7e69ec4216d15a1da_2_690x136.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f47ac0356d4fa7fd8f6d4ed7e69ec4216d15a1da.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f47ac0356d4fa7fd8f6d4ed7e69ec4216d15a1da.jpeg 2x" data-dominant-color="DBD9DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1003×199 69.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you see anything in the error log?  You could also try this to see status:</p>
<pre><code class="lang-auto">dicomRetrieve().connect("progress(QString)", print)
</code></pre>

---

## Post #25 by @rbumm (2021-02-07 09:27 UTC)

<aside class="quote no-group" data-username="pieper" data-post="24" data-topic="15693">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><code>dicomRetrieve().connect("progress(QString)", print)</code></p>
</blockquote>
</aside>
<p>Please explain  … where would that progress  print ?</p>

---

## Post #26 by @pieper (2021-02-07 17:16 UTC)

<p>If you are using the CGET option the code will emit progress as it goes through the steps and you can see which step fails.  It’s what you would see in the progress dialog in the GUI version of CGET.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/03bf84789d8c1f5ba7aeb8f6139d07e12ab94fd1/Libs/DICOM/Core/ctkDICOMRetrieve.cpp#L379-L500" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/03bf84789d8c1f5ba7aeb8f6139d07e12ab94fd1/Libs/DICOM/Core/ctkDICOMRetrieve.cpp#L379-L500" target="_blank" rel="noopener">commontk/CTK/blob/03bf84789d8c1f5ba7aeb8f6139d07e12ab94fd1/Libs/DICOM/Core/ctkDICOMRetrieve.cpp#L379-L500</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="379" style="counter-reset: li-counter 378 ;">
<li>bool ctkDICOMRetrievePrivate::get ( const QString&amp; studyInstanceUID,</li><li>                                         const QString&amp; seriesInstanceUID,</li><li>                                         const RetrieveType retrieveType )</li><li>{</li><li>  Q_Q(ctkDICOMRetrieve);</li><li></li><li>  DcmDataset *retrieveParameters = new DcmDataset();</li><li>  if (! this-&gt;initializeSCU(studyInstanceUID, seriesInstanceUID, retrieveType, retrieveParameters) )</li><li>    {</li><li>    delete retrieveParameters;</li><li>    return false;</li><li>    }</li><li></li><li>  // Issue request</li><li>  logger.debug ( "Sending Get Request" );</li><li>  emit q-&gt;progress("Sending Get Request");</li><li>  emit q-&gt;progress(0);</li><li>  OFList&lt;RetrieveResponse*&gt; responses;</li><li>  T_ASC_PresentationContextID presID = this-&gt;SCU.findPresentationContextID(</li><li>                                          UID_GETStudyRootQueryRetrieveInformationModel, </li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/03bf84789d8c1f5ba7aeb8f6139d07e12ab94fd1/Libs/DICOM/Core/ctkDICOMRetrieve.cpp#L379-L500" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #27 by @rbumm (2021-02-08 20:40 UTC)

<p>Had a few days of wrestling with our hospital internal PACS concerning the above-mentioned problems.<br>
Interestingly I made some progress (without the PACS guy):</p>
<p>First I installed my own private dcmtk from here:</p>
<p><a href="https://dicom.offis.de/dcmtk.php.en" class="onebox" target="_blank" rel="noopener nofollow ugc">https://dicom.offis.de/dcmtk.php.en</a></p>
<p>Then I needed to set the environment variable DCMDICTPATH to the full path of “dicom.dict” file in the installation, which contains a full list of DICOM tag and value types.</p>
<p>From cmd line and after many failed scripts I was able to get correct C-FIND queries from the GEPACS  by (all sensible information changed)</p>
<p>findscu -P -k 0008,0052=PATIENT -k PatientID=“9087653” -k PatientName -k StudyDate -k Modality -k StudyInstanceUID -aet CKS1234 -aec GEPACS SR7234 4100</p>
<p>and moved all PACS studies of the above-mentioned patient to my Slicer Server by</p>
<p>movescu -v --patient --move CKS1234 --port 11112 -od “C:\Users\xxxxxx\DICOM\Test” -k 0008,0052=PATIENT -k PatientID=“9087653”  -aet CKS1234 --call GEPACS SR7234 4100</p>
<p>Received about 2.8 GB of valid  data and was able to import and load that to Slicer.<br>
So principally it works, just not from python, this is just the beginning <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---
