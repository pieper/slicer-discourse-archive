# Show 3D reconstruction rendered by Slicer in a web browser

**Topic ID**: 24045
**Date**: 2022-06-25
**URL**: https://discourse.slicer.org/t/show-3d-reconstruction-rendered-by-slicer-in-a-web-browser/24045

---

## Post #1 by @zhang_ming (2022-06-25 13:03 UTC)

<p>I have my Slicer app run background on WIN10 , How can I activate Slicer app to show 3D reconstruction by a message sends from browser</p>
<p>I would donate 200$  to Slicer for soving this problems, because it puzzled me a very long time.</p>

---

## Post #2 by @zhang_ming (2022-06-25 14:04 UTC)

<aside class="quote no-group" data-username="zhang_ming" data-post="1" data-topic="24045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhang_ming/48/15790_2.png" class="avatar"> zhang_ming:</div>
<blockquote>
<p>I would donate 200$ to Slicer for soving this problems, because it puzzled me a very long ti</p>
</blockquote>
</aside>
<p>this problem means a lot to me , any one can solve this , I would pay for solution &gt; 200 $</p>

---

## Post #3 by @pieper (2022-06-25 14:43 UTC)

<p>Customization is required, but basically you can activate Slicer’s WebServer and connect to it from a browser by accessing the localhost port.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html?highlight=webserver" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html?highlight=webserver</a></p>

---

## Post #4 by @zhang_ming (2022-06-26 00:32 UTC)

<p>message  from web-app PACS/HIS, with a chrome plugin, was sent  to windows app  like <em>“”" kview:////info=studyuid=1.2.826.0.1.3680043.2.461.13073401.3329453282#userid=9999#pacssvrip=172.16.0.59#pacssvrport=7008#pacssvrip1=#pacssvrport1=#security=1 “”"</em>,  I wander if I can modify message to activate Slicer to get 3D reconstruction like this,  thank you very much</p>

---

## Post #5 by @lassoan (2022-06-26 00:52 UTC)

<p>Yes, this should be no problem at all.</p>
<ol>
<li>You need to <a href="https://github.com/shotgunsoftware/developer.shotgunsoftware.com/blob/master/docs/en/action-menu-items/custom-browser-protocols.md">associate <code>kview://</code> protocol with Slicer</a> in your operating system. Then when you click on the link the operating system will automatically launch Slicer.</li>
<li>When Slicer is launched with a URL then the Slicer application object emits the <code>urlReceived</code> signal that your custom script can interpret (similarly <a href="https://github.com/Slicer/Slicer/blob/5794e16fd72035310301e545c345c372e38facdf/Modules/Scripted/DICOM/DICOM.py#L111">how it is done in DICOM module</a>), for example it can retrieve the selected study based on the information in the URL, render the image, and make it available via the WebServer API.</li>
</ol>
<p>I hope someone will show up here who can put this all together for you.</p>

---

## Post #7 by @zhang_ming (2022-06-26 02:44 UTC)

<p>thank you for answering. In our hospital, we use chrome browser to read dicom pic, and we can put a button on html , direct to Slicer, by sending message “https:// protocol with Slicer”? can any one help me for remote controll? I would pay for the help. this means a lot to our hospital.</p>

---

## Post #8 by @zhang_ming (2022-06-26 06:09 UTC)

<p>thank you, but I can’t find WebServer module in 3D Slicaer , my version is 5.0.2</p>

---

## Post #9 by @zhang_ming (2022-06-26 06:18 UTC)

<p>thank you , I foud the version 5.10 is ok</p>

---

## Post #11 by @lassoan (2022-06-26 15:44 UTC)

<p><code>https</code> protocol is associated with your web browser (so if you open an <code>https</code> URL then the operating system launches the default web browser; and if you click the link in the web browser then of course it will just open the link within the browser). Therefore, you need to use a custom protocol, such as <code>slicer</code> and the URL would look something like this:</p>
<pre><code>slicer://viewer/?studyUID=2.16.840.1.113669.632.20.121711.10000158860&amp;access_token=k0zR6WAPpNbVguQ8gGUHp6&amp;dicomweb_endpoint=http%3A%2F%2Fdemo.kheops.online%2Fapi&amp;dicomweb_uri_endpoint=%20http%3A%2F%2Fdemo.kheops.online%2Fapi%2Fwado
</code></pre>

---

## Post #13 by @zhang_ming (2022-06-27 08:18 UTC)

<p>I find another way to solve the problem, WebServer is ok, and use ‘localhost:2016/slicer/exec’ post to exec python with the operation I need. but I have not find the way to get dicom by patient name and studyId, could you please tell me how to exec this operation by python scripts, not just paste a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder" rel="noopener nofollow ugc">script_repo</a>, to judge all kind of opeartions, thank you very much!</p>
<p>Specially, post  /slicer/exec, how can I make the Volume Rendering opeartion executed automatically?</p>

---

## Post #14 by @pieper (2022-06-27 19:32 UTC)

<p>You can send any slicer python code (e.g. any of the code from the script repository or other python code) to the slicer/exec endpoint.  This makes it very powerful, so be sure you have total control over what gets posted there (you may wish to wrap this in a security layer like a proxy).</p>
<p>But assuming you have that under control, then from what I can tell from your earlier posts you would need to take the information from the posted URL, like the study uid and pacs info, probably together with other pre-defined info like the pacs ip address, and download the study on to the local disk and import it through the dicom database.  From there you can load and render using the rest of the slicer api.  It’s not a huge job but there’s some programming you need to learn.</p>

---

## Post #15 by @zhang_ming (2022-06-28 00:42 UTC)

<p>Thank you for replying me in detail sincerely, and I am coing python to your open source program. sorry to disturbe again for some questions while in programing I found .</p>
<ol>
<li>can Web Server start automatically in .slicerrc.py by python code (I have reading you code in webserver.py, and I have no idea )</li>
<li>add node from dicom database, using function "  DICOMUtils.loadByInstanceUID(insUid) " failed with the error code " DICOM Plugin failed: tuple index out of range ", deatiled info added in below.</li>
<li>can only just display 3d view full screen with rendering tools, not other frame or view is need</li>
</ol>
<p>error info:<br>
File “H:\Program Files (x86)\Slicer 5.1.0-2022-06-21\lib\Slicer-5.1\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 744, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examineForImport(fileLists)<br>
File “H:/Program Files (x86)/Slicer 5.1.0-2022-06-21/bin/…/lib/Slicer-5.1/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 151, in examineForImport<br>
loadablesForFiles = self.examineFiles(files)<br>
File “H:/Program Files (x86)/Slicer 5.1.0-2022-06-21/bin/…/lib/Slicer-5.1/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 175, in examineFiles<br>
seriesUID = slicer.dicomDatabase.fileValue(files[0],self.tags[‘seriesUID’])<br>
IndexError: tuple index out of range<br>
DICOM Plugin failed: tuple index out of range<br>
Traceback (most recent call last):<br>
File “H:\Program Files (x86)\Slicer 5.1.0-2022-06-21\lib\Slicer-5.1\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 748, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
File “H:/Program Files (x86)/Slicer 5.1.0-2022-06-21/bin/…/lib/Slicer-5.1/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 119, in examine<br>
loadables += self.examineFilesIPPAcqTime(files)<br>
File “H:/Program Files (x86)/Slicer 5.1.0-2022-06-21/bin/…/lib/Slicer-5.1/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 357, in examineFilesIPPAcqTime<br>
desc = slicer.dicomDatabase.fileValue(files[0],self.tags[‘seriesDescription’]) # SeriesDescription<br>
IndexError: tuple index out of range<br>
DICOM Plugin failed: tuple index out of range<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “H:\Program Files (x86)\Slicer 5.1.0-2022-06-21\lib\Slicer-5.1\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 263, in loadByInstanceUID<br>
return loadLoadables(filteredLoadablesByPlugin)<br>
File “H:\Program Files (x86)\Slicer 5.1.0-2022-06-21\lib\Slicer-5.1\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 770, in loadLoadables<br>
if loadable.selected:<br>
AttributeError: ‘NoneType’ object has no attribute ‘selected’</p>

---

## Post #16 by @zhang_ming (2022-06-28 03:27 UTC)

<p>I found another question in WebServer<br>
if a patient has many studies, I want to load one of studies use study id as a node to watch, but  source file DICOMUtils.py did not  implement this. wish for your answering.</p>

---

## Post #17 by @lassoan (2022-06-28 03:45 UTC)

<p>If you load a DICOM study via DICOMweb then you can specify the study UID:</p>
<pre><code>slicer.app.openUrl("slicer://viewer/?studyUID=2.16.840.1.113669.632.20.121711.10000155501&amp;access_token=eyJhbGciO...SC1NR0GA&amp;dicomweb_endpoint=https%3A%2F%2Fdemo.kheops.online%2Fapi&amp;dicomweb_uri_endpoint=https%3A%2F%2Fdemo.kheops.online%2Fapi%2Fwado"
</code></pre>
<p>If you load from a folder then you can load a specific study or series, the same way as it is done in <code>loadPatientByUID</code>:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/23744ee0e374928b76dc4c1209faa07377bee518/Modules/Scripted/DICOMLib/DICOMUtils.py#L62-L79">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/23744ee0e374928b76dc4c1209faa07377bee518/Modules/Scripted/DICOMLib/DICOMUtils.py#L62-L79" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/23744ee0e374928b76dc4c1209faa07377bee518/Modules/Scripted/DICOMLib/DICOMUtils.py#L62-L79" target="_blank" rel="noopener">Slicer/Slicer/blob/23744ee0e374928b76dc4c1209faa07377bee518/Modules/Scripted/DICOMLib/DICOMUtils.py#L62-L79</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="62" style="counter-reset: li-counter 61 ;">
          <li>if not slicer.dicomDatabase.isOpen:</li>
          <li>    raise OSError('DICOM module or database cannot be accessed')</li>
          <li>
          </li>
<li>patientUIDstr = str(patientUID)</li>
          <li>if patientUIDstr not in slicer.dicomDatabase.patients():</li>
          <li>    raise OSError('No patient found with DICOM database UID %s' % patientUIDstr)</li>
          <li>
          </li>
<li># Select all series in selected patient</li>
          <li>studies = slicer.dicomDatabase.studiesForPatient(patientUIDstr)</li>
          <li>if len(studies) == 0:</li>
          <li>    raise OSError('No studies found in patient with DICOM database UID ' + patientUIDstr)</li>
          <li>
          </li>
<li>series = [slicer.dicomDatabase.seriesForStudy(study) for study in studies]</li>
          <li>seriesUIDs = [uid for uidList in series for uid in uidList]</li>
          <li>if len(seriesUIDs) == 0:</li>
          <li>    raise OSError('No series found in patient with DICOM database UID ' + patientUIDstr)</li>
          <li>
          </li>
<li>return loadSeriesByUID(seriesUIDs)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #18 by @zhang_ming (2022-06-28 05:50 UTC)

<p>I had read this code yet , does that mea I need to code this part ,and the push to you main repo? or will your team add this function in later version?</p>

---

## Post #19 by @zhang_ming (2022-06-28 05:50 UTC)

<p>I had read this code yet , does that mea I need to code this part ,and the push to you main repo? or will your team add this function in later version?</p>

---

## Post #20 by @pieper (2022-06-28 12:22 UTC)

<p>You can do everything you describe in your own code.  No need to add anything to our repository unless you develop some helper utilities that others might find useful.</p>
<p>You can look for slicerrc.py to find how to script the startup behavior of Slicer and can start/configure the WebServer module from there.  You can also program the dicom module to retrieve / load data and can customize the rendering.  <a class="mention" href="/u/lassoan">@lassoan</a> and I are busy this week with <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/">Project Week</a> and may not have time to provide details, but if you join Project Week you can find people to discuss your use case and help.</p>

---
