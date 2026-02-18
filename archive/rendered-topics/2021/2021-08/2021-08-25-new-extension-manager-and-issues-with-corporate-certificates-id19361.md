# New extension manager and issues with corporate certificates

**Topic ID**: 19361
**Date**: 2021-08-25
**URL**: https://discourse.slicer.org/t/new-extension-manager-and-issues-with-corporate-certificates/19361

---

## Post #1 by @muratmaga (2021-08-25 18:39 UTC)

<p>Today I downloaded a new preview version, and tried to install MoniaLabel and SlicerMorph on my work computers, and encountered this error:</p>
<pre><code class="lang-auto">
Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/BreastImplantAnalyzer.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/CleverSeg.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e1/CornerAnnotationIcon.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b7/CurveMakerIcon.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/9/92/DSC_logo_Resized.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/ErodeDilateLabelIcon.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/1/16/FilmDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/f1/GelDosimetry_Logo_128x128.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/GraphCutSegment.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/GyroGuide.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/e/e5/QuickToolsLogo.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/f/f6/IntensitySegmenterIcon.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/5/56/LAScarSegmenter.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/0/08/LongitudinalPETCTLogo.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/index.php/File:ModelClipIcon.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/4/43/Slicer4ExtensionModelToModelDistance.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2e/OpenCAD.PNG'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/ac/PAAlogo-small.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/21/PerkTutorLogo.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/b1/DPetBrainQuantification.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/a/a7/Portplacement_icon.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/d/d6/ResectionPlannerLogo.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://viewvc.slicer.org/viewvc.cgi/Slicer4/trunk/Extensions/Testing/SNRMeasurement/SNRMeasurement.png?revision=21745&amp;view=co'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.na-mic.org/Wiki/images/a/ad/Spharm-pdm-icon.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/b/ba/SegAidedRegSquareFocus128.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/5/5b/Slicer-Wasp.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/SlicerDMRI/slicerdmri.github.io/master/images/DMRI_3D_SLICER-icon.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://raw.githubusercontent.com/QIICR/SlicerDevelopmentToolbox/master/Resources/Icons/SlicerDevelopmentToolbox.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/f/ff/SlicerHeart_Logo_128x128.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/2b/SlicerIGTLogo.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.example.com/Slicer/Extensions/SlicerNetstim.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/8/87/SlicerProstate_Logo_1.0_128x128.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/2/29/SlicerRT_Logo_3.0_128x128.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/w/images/6/6b/RadiomicsExtension.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/6/64/SlicerToKiwiExporterLogo.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.nitrc.org/project/screenshot.php?group_id=196&amp;screenshot_id=269'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/cd/SwissSkullStripper.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://slicer.org/slicerWiki/images/3/32/T1_Mapping_Logo_Resized.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/9/92/TCIABrowser_logo.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://www.slicer.org/slicerWiki/images/c/c2/VolumeClipLogo.png'. This content should also be served over HTTPS.

Mixed Content: The page at 'https://extensions.slicer.org/catalog/All/30133/win?q=' was loaded over HTTPS, but requested an insecure image 'http://wiki.slicer.org/slicerWiki/images/5/59/MpReviewLogo.png'. This content should also be served over HTTPS.

Retrieving extension metadata [ extensionId: 61260e2b342a877cb3b8d73e]

Retrieving extension files [ extensionId: 61260e2b342a877cb3b8d73e ]

Downloading extension [ item_id: 61260e2b342a877cb3b8d73e, file_id: 61260e2b342a877cb3b8d745]

Failed downloading: https://slicer-packages.kitware.com/api/v1/file/61260e2b342a877cb3b8d745/download
</code></pre>
<p>This happens both on Linux and WIndows. If I copy and paste the referenced URL to the web browser in the same computer, I can download the file 30133-win-amd64-SlicerMorph-gitf70c039-2021-08-20.zip without an issue.</p>
<p>I suspect this is because our institution uses self-signed certificates in their corporate network. While, the regular OS (browsers and other operations) work fine, somehow this is not getting propagated to the Slicer. Is there a solution for this? Our IT admins consider this as Slicer’s problem, since on the same computer I can get to the specified URL without the error.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #2 by @jcfr (2021-09-02 16:59 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><code>Mixed Content</code></p>
</blockquote>
</aside>
<p>This is because some of the extension icons are server over http.</p>
<p>This will be fixed in the next few weeks.</p>
<p>To help with this, we already developed a Jupyter notebook to identify and check which extensions have issues. The next step will be to harden the notebook and integrate the code into the <a href="https://github.com/Slicer/ExtensionsIndex/pull/1788">Slicer/ExtensionsIndex</a> continuous integration.</p>
<p>For reference, see <a href="https://github.com/jcfr/jupyter-notebooks/blob/master/45_slicer_extensions_index_check_metadata_urls.ipynb">https://github.com/jcfr/jupyter-notebooks/blob/master/45_slicer_extensions_index_check_metadata_urls.ipynb</a></p>

---

## Post #3 by @lassoan (2021-09-02 18:00 UTC)

<p>There is also an automatic URL check <a href="https://github.com/Slicer/ExtensionsIndex/pull/1788/files">implemented in the ExtensionsIndex repository</a> - it just has not been merged yet (it can be used locally, though).</p>
<p>But these http/https warning are not related to the failed download, because I see these warnings on my computer, too, but the download does not fail.</p>

---

## Post #4 by @muratmaga (2021-09-03 16:16 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> is there an update on this? Package download is still failing for me without any detailed error.</p>
<p>This is all there is in the log</p>
<pre><code class="lang-auto">Retrieving extension metadata [ extensionId: 61260e2b342a877cb3b8d73e]

Retrieving extension files [ extensionId: 61260e2b342a877cb3b8d73e ]

Downloading extension [ item_id: 61260e2b342a877cb3b8d73e, file_id: 61260e2b342a877cb3b8d745]

Failed downloading: https://slicer-packages.kitware.com/api/v1/file/61260e2b342a877cb3b8d745/download
</code></pre>
<p>Here is the screenshot that I shows I can get to the same package via wget on the same laptop.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38d2bb14666e7f10710633d0eddca393e201b40f.png" data-download-href="/uploads/short-url/86Ge4qIdVuH7oX4cW4NkX8Vu8az.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d2bb14666e7f10710633d0eddca393e201b40f_2_690x375.png" alt="image" data-base62-sha1="86Ge4qIdVuH7oX4cW4NkX8Vu8az" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d2bb14666e7f10710633d0eddca393e201b40f_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d2bb14666e7f10710633d0eddca393e201b40f_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38d2bb14666e7f10710633d0eddca393e201b40f_2_1380x750.png 2x" data-dominant-color="0C0CFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1663×905 51.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2021-09-10 17:56 UTC)

<p>With todays preview, I tried again and still cannot download packages at office (fine at home).</p>
<pre><code class="lang-auto">Retrieving extension metadata [ extensionId: 613b26b1342a877cb3bee817]

Retrieving extension files [ extensionId: 613b26b1342a877cb3bee817 ]

Downloading extension [ item_id: 613b26b1342a877cb3bee817, file_id: 613b26b1342a877cb3bee81e]

Failed downloading: https://slicer-packages.kitware.com/api/v1/file/613b26b1342a877cb3bee81e/download
</code></pre>

---

## Post #6 by @lassoan (2021-09-10 18:53 UTC)

<p>Can you download the files using Python, in Slicer’s Python environment (using wget, curl, requests,…)?</p>

---

## Post #7 by @muratmaga (2021-09-10 19:06 UTC)

<p>This seems to work. At least it is finding the filename correct, I do not know how to write</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import wget
&gt;&gt;&gt; url = "https://slicer-packages.kitware.com/api/v1/file/613b26b1342a877cb3bee81e/download"
&gt;&gt;&gt; filename = wget.download(url)
&gt;&gt;&gt; filename
'30168-win-amd64-SlicerMorph-gitf70c039-2021-08-20.zip'
</code></pre>

---

## Post #8 by @lassoan (2021-09-10 19:22 UTC)

<p>OK, this is useful information (the file is saved in the current working directory).</p>
<p>Does the download work using Qt with the code snippet below?</p>
<pre><code class="lang-python">url = qt.QUrl("https://slicer-packages.kitware.com/api/v1/file/613b26b1342a877cb3bee81e/download")
request = qt.QNetworkRequest(url)
manager = qt.QNetworkAccessManager()
reply = manager.get(request)

while (not reply.isFinished()):
    slicer.app.processEvents()

localFile = qt.QFile("c:/tmp/downloaded2.zip")
localFile.open(qt.QIODevice.WriteOnly)
localFile.write(reply.readAll());
localFile.close()

print(f"HTTP response code: {reply.attribute(qt.QNetworkRequest.HttpStatusCodeAttribute)}")
print(f"Error code: {reply.error()}")
</code></pre>

---

## Post #9 by @muratmaga (2021-09-10 19:29 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="8" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">url = qt.QUrl("https://slicer-packages.kitware.com/api/v1/file/613b26b1342a877cb3bee81e/download")
request = qt.QNetworkRequest(url)
manager = qt.QNetworkAccessManager()
reply = manager.get(request)

localFile = qt.QFile("c:/tmp/downloaded.zip")
localFile.open(qt.QIODevice.WriteOnly)
localFile.write(reply.readAll());
localFile.close()
</code></pre>
</blockquote>
</aside>
<p>There is now a downloaded.zip file in c:/tmp but it is 0 bytes.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; localFile = qt.QFile("c:/temp/downloaded.zip")
&gt;&gt;&gt; localFile.open(qt.QIODevice.WriteOnly)
True
&gt;&gt;&gt; localFile.write(reply.readAll());
0
&gt;&gt;&gt; localFile.close()
</code></pre>

---

## Post #10 by @lassoan (2021-09-10 19:33 UTC)

<p>Sorry, I forgot to say that you need to wait for the request to complete before you read out the result. I’ve updated the code above to wait so that you don’t need to wait manually. Try again with the updated code snippet.</p>

---

## Post #11 by @muratmaga (2021-09-10 19:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">url = qt.QUrl("https://slicer-packages.kitware.com/api/v1/file/613b26b1342a877cb3bee81e/download")
request = qt.QNetworkRequest(url)
manager = qt.QNetworkAccessManager()
reply = manager.get(request)

while (not reply.isFinished()):
    slicer.app.processEvents()

localFile = qt.QFile("c:/tmp/downloaded2.zip")
localFile.open(qt.QIODevice.WriteOnly)
localFile.write(reply.readAll());
localFile.close()

print(f"HTTP response code: {reply.attribute(qt.QNetworkRequest.HttpStatusCodeAttribute)}")
print(f"Error code: {reply.error()}")
</code></pre>
</blockquote>
</aside>
<p>Still 0.</p>
<pre><code class="lang-auto">
&gt;&gt;&gt; url = qt.QUrl("https://slicer-packages.kitware.com/api/v1/file/613b26b1342a877cb3bee81e/download")
&gt;&gt;&gt; request = qt.QNetworkRequest(url)
&gt;&gt;&gt; manager = qt.QNetworkAccessManager()
&gt;&gt;&gt; reply = manager.get(request)
&gt;&gt;&gt;
&gt;&gt;&gt; while (not reply.isFinished()):
... slicer.app.processEvents()
...
&gt;&gt;&gt; localFile = qt.QFile("c:/temp/downloaded2.zip")
&gt;&gt;&gt; localFile.open(qt.QIODevice.WriteOnly)
True
&gt;&gt;&gt; localFile.write(reply.readAll());
0
&gt;&gt;&gt; localFile.close()
&gt;&gt;&gt;
&gt;&gt;&gt; print(f"HTTP response code: {reply.attribute(qt.QNetworkRequest.HttpStatusCodeAttribute)}")
HTTP response code: None
&gt;&gt;&gt; print(f"Error code: {reply.error()}")
Error code: 6
&gt;&gt;&gt;
</code></pre>

---

## Post #12 by @lassoan (2021-09-10 19:37 UTC)

<p>Great, you’ve managed to reproduce the problem!</p>
<p>What is the output of <code>reply.errorString()</code>?</p>

---

## Post #13 by @muratmaga (2021-09-10 19:37 UTC)

<p>‘SSL handshake failed’</p>

---

## Post #14 by @lassoan (2021-09-10 19:44 UTC)

<p>Perfect! Now you have everything to debug this problem and find how to fix the SSL configuration to make the handshake happen (by fixing the root cause of the error or making the error ignored). See all the configuration options in the <a href="https://doc.qt.io/qt-5/qnetworkaccessmanager.html">network access manager</a> and the <a href="https://doc.qt.io/qt-5/qnetworkrequest.html">network request</a>.</p>

---

## Post #15 by @pieper (2021-09-10 21:13 UTC)

<p>Can anyone else replicate this issue or suggest what might be the solution?  It sounds like this is something to do with the institutional firewall and <a href="https://doc.qt.io/qt-5/qsslconfiguration.html">SSL certificate management</a>.</p>

---

## Post #16 by @muratmaga (2021-09-10 21:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="19361" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Perfect! Now you have everything to debug this problem and find how to fix the SSL configuration to make the handshake happen (by fixing the root cause of the error or making the error ignored). See all the configuration options in the <a href="https://doc.qt.io/qt-5/qnetworkaccessmanager.html">network access manager </a> and the <a href="https://doc.qt.io/qt-5/qnetworkrequest.html">network request </a>.</p>
</blockquote>
</aside>
<p>I won’t know where to start with those.</p>
<p>However, as Steve pointed out I think this is most likely related to certificate. On the same computers, when I install the windows Git, if I do not choose to trust the windows certificate store, git would fail with the same error. A more detailed description of this is here (see the first answer): <a href="https://stackoverflow.com/questions/16668508/how-do-i-configure-git-to-trust-certificates-from-the-windows-certificate-store" class="inline-onebox">How do I configure Git to trust certificates from the Windows Certificate Store? - Stack Overflow</a></p>
<p>Is there a way to test this option for Slicer as well?</p>

---

## Post #17 by @muratmaga (2021-09-10 21:32 UTC)

<aside class="quote no-group" data-username="pieper" data-post="15" data-topic="19361" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Can anyone else replicate this issue or suggest what might be the solution? It sounds like this is something to do with the institutional firewall and <a href="https://doc.qt.io/qt-5/qsslconfiguration.html">SSL certificate management </a>.</p>
</blockquote>
</aside>
<p>Yes, I really appreciate if any Slicer users behind corporate firewalls with self-signed certificates can try this and see if this happens to others as well.</p>

---

## Post #18 by @lassoan (2021-09-10 22:27 UTC)

<blockquote>
<p>I won’t know where to start with those.</p>
</blockquote>
<p>Just Google <code>qt linux "SSL handshake failed"</code> and try all the solutions that people recommend. It should be easy to disable verification, but it would be much nicer if you found out where Python gets the certificates from and make Qt find those, too. But maybe Python (wget) just does not verify the certificates by default.</p>
<p>You may be able to add your self-signed certificate to the certificate file in share\Slicer-4.13\Slicer.crt. See more information <a href="https://github.com/Slicer/Slicer/tree/master/Base/QTCore/Resources/Certs">here</a>.</p>

---

## Post #19 by @muratmaga (2021-09-10 22:56 UTC)

<p>OK. Will try those but looking at this example from your link, I am getting this error</p>
<pre><code class="lang-auto"> w = slicer.qSlicerWebWidget()
 w.show()
 v = w.webView()
 v.setUrl(qt.QUrl("https://www.eff.org/https-everywhere"))
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: QWebEngineView has no attribute named 'setUrl'
</code></pre>

---

## Post #20 by @lassoan (2021-09-10 23:42 UTC)

<p>We have a very good, simple way to reproduce the error, just stick to that for now (the qSlicerWebWidget  contains a full web browser, i.e., an entire operating system, so that could complicate things).</p>
<p>Just check what is needed to make the simple download code snippet work.</p>
<p>For example, check if <a href="https://stackoverflow.com/a/26016487/12370111">disabling verification</a> fixes the issue. If it does, then that could be a simple, universal workaround that we could expose, if needed (and if we don’t find a safer solution).</p>
<p>Another idea to try: <a href="https://www.qtcentre.org/threads/18762-QNetworkAccessManager-quot-SSL-handshake-failed-quot?p=92768#post92768">select different protocol</a>.</p>

---

## Post #22 by @muratmaga (2021-09-14 19:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You may be able to add your self-signed certificate to the certificate file in share\Slicer-4.13\Slicer.crt. See more information <a href="https://github.com/Slicer/Slicer/tree/master/Base/QTCore/Resources/Certs">here </a>.</p>
</blockquote>
</aside>
<p>Manually adding the certificates inside the Slicer.crt fixed the problem. I can now use the extension manager.</p>
<p>But where do we go from here? This is not a solution for us, just in our center there about 30-40 different installations of Slicer in dozens of computers (each user account needs to be fixed individually). There are many other clinical centers and researchers at SCH who use Slicer that will suffer from this.</p>
<p><a class="mention" href="/u/mikebind">@mikebind</a> <a class="mention" href="/u/ezgimercan">@ezgimercan</a>  do you encounter this certificate issue at your work computers? (try with a new installation)</p>

---

## Post #23 by @lassoan (2021-09-14 19:56 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="22" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>But where do we go from here? This is not a solution for us</p>
</blockquote>
</aside>
<p>Try to figure out why <code>wget</code> does not have this issue.</p>
<ul>
<li>Is it because curl can find the certificate on your system? Can you check where self-signed certificates are stored on your computer?</li>
<li>Maybe because curl uses the system OpenSSL? You can consult with <a class="mention" href="/u/jcfr">@jcfr</a>, currently evaluating building Slicer without bundling OpenSSL - see <a href="https://github.com/Slicer/Slicer/issues/5663">#5663</a>)</li>
<li>Is it because SSL verification is turned off? By default it should be enabled, but if your system has a special OpenSSL configuration and the user is not concerned about security then we could allow disabling SSL verification.</li>
</ul>
<aside class="quote no-group" data-username="muratmaga" data-post="22" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>do you encounter this certificate issue at your work computers? (try with a new installation)</p>
</blockquote>
</aside>
<p>Only about 1 of 10 Slicer downloads are on Linux, and they are expected to be able to deal with things like installing self-signed certificates. It would be important to know if this is an issue on Windows and macOS as well.</p>

---

## Post #24 by @muratmaga (2021-09-14 20:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="23" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Only about 1 of 10 Slicer downloads are on Linux, and they are expected to be able to deal with things like installing self-signed certificates. It would be important to know if this is an issue on Windows and macOS as well.</p>
</blockquote>
</aside>
<p>This happens on both windows and Linux computers that are connected to our network. We are primarily a windows shop, which is the concern. As you said, most Linux users are used to following these kinds of instructions, but quite concerning for windows.</p>
<p>Our windows desktops use a centralized image, in which I presume the certificates are baked. I can try to find path where those are, if that’s helpful.</p>

---

## Post #25 by @lassoan (2021-09-14 20:44 UTC)

<p>On Windows, there is a certificate store where you all the trusted certificates are saved to. It would be nice if you could check that Python <code>curl</code> and <code>requests</code> retrieve certificates from there (you can try that for example by temporarily removing your self-signed certification from the store).</p>
<p>By the way, I don’t understand how a large organization cannot afford to pay a few hundred dollars to get the certificate properly registered. This investigation already costs more than what they would need to pay for it. Doesn’t this untrusted certificate cause all kinds of issues for many other applications? How can you connect devices that do not allow installing self-signed certificates?</p>

---

## Post #26 by @muratmaga (2021-09-14 20:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>By the way, I don’t understand how a large organization cannot afford to pay a few hundred dollars to get the certificate properly registered. This investigation already costs more than what they would need to pay for it. Doesn’t this untrusted certificate cause all kinds of issues for many other applications? How can you connect devices that do not allow installing self-signed certificates?</p>
</blockquote>
</aside>
<p>I have no idea why they are not doing this, and I unfortunately i have no answer for it…</p>

---

## Post #27 by @mikebind (2021-09-14 21:24 UTC)

<p>I primarily work on my personal laptop, but I can confirm that I ran into the same problem on computers within the hospital corporate network, <a class="mention" href="/u/muratmaga">@muratmaga</a>.</p>

---

## Post #28 by @jcfr (2021-09-14 22:07 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="22" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Manually adding the certificates inside the Slicer.crt fixed the problem.</p>
</blockquote>
</aside>
<p>Could you try using the updated <code>Slicer.crt</code> associated with <a href="https://github.com/Slicer/Slicer/pull/5855">https://github.com/Slicer/Slicer/pull/5855</a> ?</p>
<p>For reference, certificate bundle was re-generated following these instructions. See <a href="https://github.com/Slicer/Slicer/tree/master/Base/QTCore/Resources/Certs#readme">Base/QTCore/Resources/Certs#readme</a></p>
<p>Moving forward, I suggest we also add a weekly GitHub Actions workflow that would be automatically run the script and create a pull-request.</p>

---

## Post #29 by @muratmaga (2021-09-14 22:22 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="28" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Could you try using the updated <code>Slicer.crt</code> associated with <a href="https://github.com/Slicer/Slicer/pull/5855">https://github.com/Slicer/Slicer/pull/5855 </a> ?</p>
<p>For reference, certificate bundle was re-generated following these instructions. See <a href="https://github.com/Slicer/Slicer/tree/master/Base/QTCore/Resources/Certs#readme">Base/QTCore/Resources/Certs#readme</a></p>
</blockquote>
</aside>
<p>If you mean, I just replace the default Slicer.crt in today’s preview with this one, it didn’t work. (same issue with extension manager).</p>

---

## Post #30 by @pieper (2021-09-14 22:29 UTC)

<p>I believe Jc meant to download <a href="https://raw.githubusercontent.com/Slicer/Slicer/6fb5dcb4362756ccca2a88cc2009b5d1734bad9a/Base/QTCore/Resources/Certs/Slicer.crt">this one</a> and if it works then he’ll merge the PR and it will be in tomorrow’s preview.</p>

---

## Post #31 by @lassoan (2021-09-15 00:32 UTC)

<p>As far as I understand, the problem is that the certificate that <a class="mention" href="/u/muratmaga">@muratmaga</a>’s institution is using is not trusted (self-signed). This untrusted certificate has to be manually merged into the Slicer.crt file.</p>
<p>The interesting thing is that curl in the Slicer interpreter works. It would be nice to do the same what curl does.</p>

---

## Post #32 by @jcfr (2021-09-15 08:56 UTC)

<h3><a name="p-66311-updates-1" class="anchor" href="#p-66311-updates-1" aria-label="Heading link"></a>Updates</h3>
<p>Every Tuesday at 11.30am UTC (7.30am ET), a GitHub workflow will now be triggered to re-generate the <code>Slicer.crt</code> bundle and create a pull-request if has changed since the last run. See <a href="https://github.com/Slicer/Slicer/blob/master/.github/workflows/update-slicer-certificate-bundle.yml">update-slicer-certificate-bundle.yml</a></p>

---

## Post #33 by @muratmaga (2021-09-15 15:18 UTC)

<aside class="quote no-group" data-username="pieper" data-post="30" data-topic="19361" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I believe Jc meant to download <a href="https://raw.githubusercontent.com/Slicer/Slicer/6fb5dcb4362756ccca2a88cc2009b5d1734bad9a/Base/QTCore/Resources/Certs/Slicer.crt">this one </a> and if it works then he’ll merge the PR and it will be in tomorrow’s preview.</p>
</blockquote>
</aside>
<p>That’s what I did. Downloaded that crt file, overwrite the one preview version came with. Had no effect (errors persist). As Andras said the only mitigating solution we have right now is to copy and paste the root certificates in SLicer’s certificate. But since this needs to be done on per user basis, it is not much of a solution.</p>
<p>As also andras pointed out I do NOT encounter the SSL handshake error when I use <a href="https://discourse.slicer.org/t/new-extension-manager-and-issues-with-corporate-certificates/19361/7">wget inside the Slicer’s python environment</a>, but get the error if I try to access the file directly via <a href="https://discourse.slicer.org/t/new-extension-manager-and-issues-with-corporate-certificates/19361/11">QT</a>. So somehow wget is finding the correct certificates from the windows and but not  QT.</p>

---

## Post #34 by @lassoan (2021-09-15 16:55 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="33" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>So somehow wget is finding the correct certificates from the windows and but not QT.</p>
</blockquote>
</aside>
<p>Have you confirmed that wget does not simply skip the SSL verification? Does wget fail if you temporarily remove the self-signed certificate from your system?</p>
<p>Have you checked if you disable SSL verification in the Qt request then it completes successfully?</p>
<p>Could you ask your IT admins about why don’t they get a proper certificate from a trusted authority? If there is a valid use case then it can justify investing Slicer development time into this; but if this is just a bad decision of a single organization then it does not make sense for Slicer developers to pay the price.</p>

---

## Post #35 by @muratmaga (2021-09-15 17:12 UTC)

<p>It is not easy to remove the certificates fro`</p>
<aside class="quote no-group" data-username="lassoan" data-post="34" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you confirmed that wget does not simply skip the SSL verification? Does wget fail if you temporarily remove the self-signed certificate from your system?</p>
</blockquote>
</aside>
<p>It is not easy to remove the certificates from these windows boxes as far as I can tell. In normal wget you have to explicitly specify to skip ssl via --no-check-certificate parameter. I am not how it is done in its python implementation, but will check.</p>
<aside class="quote no-group" data-username="lassoan" data-post="34" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you ask your IT admins about why don’t they get a proper certificate from a trusted authority? If there is a valid use case then it can justify investing Slicer development time into this; but if this is just a bad decision of a single organization then it does not make sense for Slicer developers to pay the price.</p>
</blockquote>
</aside>
<p>I agree and already reached out to the institutional security team that this is turning to be a big issue for us. However, whatever/why ever  they are doing is not impacting regular windows operation. So from their perspective this is also a corner case that they need to get more info to come up with a solution. It appears to be a combination of QT and Slicer build settings. The only other QT based application I used on these windows machines is Rstudio, and I have no issue getting https:// resources on them (no handshake error).</p>

---

## Post #36 by @lassoan (2021-09-15 18:08 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="35" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It is not easy to remove the certificates from these windows boxes as far as I can tell.</p>
</blockquote>
</aside>
<p>You can open the local machine certificate manager by hitting the windows key and typing <code>certlm.msc</code>. You can then find the self-signed certificate and disable all uses, restart the computer, and see if wget in python still works.</p>
<p>You can also <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/README.md#debuggingtools-extension-for-3d-slicer">run wget step by step in a Python debugger</a> to see what certificates it is using and from where it gets them.</p>

---

## Post #37 by @muratmaga (2023-01-05 20:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="36" data-topic="19361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>then</p>
</blockquote>
</aside>
<p>This is back for me, this time on a MacOS computer attached to the corporate network. The funny thing it was working fine until last week. When I try to download a sample file (like MRHead) I am getting certificate error.</p>
<p>When I used the test snipped above, I am getting error code 200, which says “Unknown Error”</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<pre><code class="lang-auto">url = qt.QUrl("https://slicer-packages.kitware.com/api/v1/file/613b26b1342a877cb3bee81e/download")

request = qt.QNetworkRequest(url)

manager = qt.QNetworkAccessManager()

reply = manager.get(request)

while (not reply.isFinished()):

slicer.app.processEvents()

localFile = qt.QFile("/Users/amaga/downloaded2.zip")

localFile.open(qt.QIODevice.WriteOnly)

localFile.write(reply.readAll());

localFile.close()

print(f"HTTP response code: {reply.attribute(qt.QNetworkRequest.HttpStatusCodeAttribute)}")

print(f"Error code: {reply.error()}")

HTTP response code: 200

Error code: 0

&gt;&gt;&gt;

&gt;&gt;&gt; reply.errorString()

'Unknown error'
</code></pre>
<p>Like before, this URL downloads fine from firefox or safari browsers on the same computer, attached to the same network.</p>

---

## Post #38 by @jcfr (2023-01-05 22:04 UTC)

<blockquote>
<p>certificate error</p>
</blockquote>
<p>Since the scheduled workflow <a href="https://github.com/Slicer/Slicer/actions/workflows/update-slicer-certificate-bundle.yml">Update Slicer.crt certificate bundle</a> didn’t lead to an update, we will need to further investigate.</p>

---
