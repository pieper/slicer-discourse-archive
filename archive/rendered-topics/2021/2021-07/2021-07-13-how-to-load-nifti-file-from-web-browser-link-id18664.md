# How to load nifti file from web browser link?

**Topic ID**: 18664
**Date**: 2021-07-13
**URL**: https://discourse.slicer.org/t/how-to-load-nifti-file-from-web-browser-link/18664

---

## Post #1 by @ASH (2021-07-13 12:44 UTC)

<p>Hi there,<br>
I have a nifti file (xxx.nii.gz) and can open it in 3D slicer with drag and drop the file to the app.<br>
I watched the video (<a href="https://www.youtube.com/watch?v=60_hzSlptWY" class="inline-onebox" rel="noopener nofollow ugc">Using 3D Slicer with cloud DICOMweb databases - YouTube</a>) and found a DICOM can be opened from web browser lnk. Now, I want to load a nifti file in 3D slicer just like that. Is it possible?</p>
<p>I noticed a link looks like <code>slicer://viewer?studyUID=xxx&amp;access_token=xxx&amp;dicomweb_endpoint=httpsxxx&amp;dicomweb_uri_endpoint=httpsxxx</code>, but couldn’t find a document what value should be passed for each argment.</p>

---

## Post #2 by @lassoan (2021-07-13 16:14 UTC)

<p>This is easily doable. All you need to do is to create a small Python scripted module that handles this URL. You can generate the skeleton of the module using Extension Wizard and then you would only keep the module class that would set up the callback function <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L52">as it is done in the DICOM module</a>.</p>
<p>Your callback function could be something like this (you can copy-paste this code into the Python console to test it):</p>
<pre><code class="lang-python">def reportProgress(message, level, sampleDataLogic):
    # Print progress in the console
    print("Loading... {0}%".format(sampleDataLogic.downloadPercent))
    # Abort download if cancel is clicked in progress bar
    progressWindow = sampleDataLogic.progressWindow
    if progressWindow.wasCanceled:
        raise Exception("download aborted")
    # Update progress window
    progressWindow.show()
    progressWindow.activateWindow()
    progressWindow.setValue(int(sampleDataLogic.downloadPercent))
    progressWindow.setLabelText("Downloading...")
    # Process events to allow screen to refresh
    slicer.app.processEvents()

def onURLReceived(urlString):
    """Process DICOM view requests. Example:
    urlString="slicer://viewer/?download=https%3A%2F%2Fgithub.com%2Frbumm%2FSlicerLungCTAnalyzer%2Freleases%2Fdownload%2FSampleData%2FLungCTAnalyzerChestCT.nrrd"
    """
    url = qt.QUrl(urlString)
    if url.authority().lower() != "viewer":
        return
    query = qt.QUrlQuery(url)
    queryMap = {}
    for key, value in query.queryItems(qt.QUrl.FullyDecoded):
        queryMap[key] = qt.QUrl.fromPercentEncoding(value)
    if not "download" in queryMap:
        return
    downloadUrl = qt.QUrl(queryMap["download"])
    nodeName, ext = os.path.splitext(os.path.basename(downloadUrl.path()))
    import uuid
    # Generate random filename to avoid reusing/overwriting older downloaded files that may have the same name
    filename = f"{nodeName}-{uuid.uuid4().hex}{ext}"
    print(filename)
    try:
        progressWindow = slicer.util.createProgressDialog()
        import SampleData
        sampleDataLogic = SampleData.SampleDataLogic()
        sampleDataLogic.progressWindow = progressWindow
        sampleDataLogic.logMessage = lambda message, level=None, sampleDataLogic=sampleDataLogic: reportProgress(message, level, sampleDataLogic)
        loadedNodes = sampleDataLogic.downloadFromURL(nodeNames=nodeName, fileNames=filename, uris=downloadUrl.toString())
    finally:
        progressWindow.close()
</code></pre>
<p>To test, run this in the Python console (to download this sample nrrd file: <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/releases/download/SampleData/LungCTAnalyzerChestCT.nrrd">https://github.com/rbumm/SlicerLungCTAnalyzer/releases/download/SampleData/LungCTAnalyzerChestCT.nrrd</a>)</p>
<pre><code class="lang-python">onURLReceived("slicer://viewer/?download=https%3A%2F%2Fgithub.com%2Frbumm%2FSlicerLungCTAnalyzer%2Freleases%2Fdownload%2FSampleData%2FLungCTAnalyzerChestCT.nrrd")
</code></pre>
<p>You can of course tune the URL format, add checksum (SampleData module can automatically cache downloaded data sets to avoid repeated downloads if the checksum value matches), etc.</p>

---

## Post #3 by @ASH (2021-07-14 03:19 UTC)

<p>Thanks for the reply. Some parts are not clear to me as I’m new to 3D slicer and python. Appreaciate if you could help me bit more.</p>
<p>Firstly, I followed “Creating Extensions” section in the below page to create an extension/module named “loadRemoteFile”:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ExtensionWizard" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/ExtensionWizard</a></p>
<p>I added <code>slicer.app.connect("urlReceived(QString)", self.onURLReceived)</code> line and the script you mentioned above in loadRemoteFile.py. Then loaded the module from “Module finder” (It should be loaded automatically anyway as I checked ‘Add selected module to search paths’ when creaed extension). No error occurs at this point. However, if I run "onURLReceived(“slicer…” in Python interactor, get an error “NameError: name ‘onURLReceived’ is not defined”. What am I missing?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8734e2d260f2a3c1da750d6cfe69e5020d690b1.png" data-download-href="/uploads/short-url/o2bfQM8XtFNTLc6xnKDHMcXLGZb.png?dl=1" title="Annotate-a-local-image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8734e2d260f2a3c1da750d6cfe69e5020d690b1_2_690x397.png" alt="Annotate-a-local-image" data-base62-sha1="o2bfQM8XtFNTLc6xnKDHMcXLGZb" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8734e2d260f2a3c1da750d6cfe69e5020d690b1_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8734e2d260f2a3c1da750d6cfe69e5020d690b1_2_1035x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8734e2d260f2a3c1da750d6cfe69e5020d690b1_2_1380x794.png 2x" data-dominant-color="908F97"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Annotate-a-local-image</span><span class="informations">1455×839 56.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, I would like to know the way to pass the module I created to somebody. Give the whole contents of loadRemoteFile folder then users load it from Extension wizard-&gt;Select extension?</p>

---

## Post #4 by @lassoan (2021-07-14 03:34 UTC)

<p><code>onURLReceived</code> function is not found in the Python console if you don’t copy it into the Python console.</p>
<p>To test your module, you can launch <code>Slicer.exe</code> with the URL as the only command-line argument:</p>
<pre><code>Slicer.exe slicer://viewer/?download=https%3A%2F%2Fgithub.com%2Frbumm%2FSlicerLungCTAnalyzer%2Freleases%2Fdownload%2FSampleData%2FLungCTAnalyzerChestCT.nrrd
</code></pre>
<p>To test if the custom URL association is set up correctly, you can open a command terminal in Windows and execute this:</p>
<pre><code>start slicer://viewer/?download=https%3A%2F%2Fgithub.com%2Frbumm%2FSlicerLungCTAnalyzer%2Freleases%2Fdownload%2FSampleData%2FLungCTAnalyzerChestCT.nrrd`
</code></pre>
<aside class="quote no-group" data-username="ASH" data-post="3" data-topic="18664">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash/48/11599_2.png" class="avatar"> ASH:</div>
<blockquote>
<p>Also, I would like to know the way to pass the module I created to somebody.</p>
</blockquote>
</aside>
<p>Probably the easiest is to copy your module files to the <code>lib\Slicer-4.13\qt-scripted-modules</code> folder in the Slicer installation.</p>

---

## Post #5 by @ASH (2021-07-14 06:01 UTC)

<p>mmm… I’m still struggling. 3D slicer won’t complain anything if open up normally, however open up with “Slicer.exe slicer://…” or “start slicer://…” gets “Missing dicomweb_endpoint” error. Sounds like the module is not loaded correctly.</p>
<pre><code class="lang-auto">DICOM module received URL: slicer://viewer/?download=https%3A%2F%2Fgithub.com%2Frbumm%2FSlicerLungCTAnalyzer%2Freleases%2Fdownload%2FSampleData%2FLungCTAnalyzerChestCT.nrrd
Missing dicomweb_endpoint
</code></pre>
<p>The app complains if I insert something meaningless text in loadRemoteFile.py intentionally, so apparently the app is reading the py file.<br>
I share the py file below. Could you check if anything wrong please?<br>
I commented out <code>slicer.app.connect("startupCompleted()", registerSampleData)</code> at line 35.<br>
“slicer.app.connect” is in line 36 followed by reportProgress and onURLReceived functions.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1j6WRLAt7vdaa4kzYYyyFG3XBPUa_73ZG/view">
  <header class="source">

      <a href="https://drive.google.com/file/d/1j6WRLAt7vdaa4kzYYyyFG3XBPUa_73ZG/view" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1j6WRLAt7vdaa4kzYYyyFG3XBPUa_73ZG/view" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1j6WRLAt7vdaa4kzYYyyFG3XBPUa_73ZG/view" target="_blank" rel="noopener nofollow ugc">loadRemoteFile.py</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @ASH (2021-07-14 12:39 UTC)

<p>I also tried to put “slicer.app.connect()”, “reportProgress()” and “onURLReceived()” functions just under the “def setup(self):” line like the example you mentioned - still same error.</p>

---

## Post #7 by @lassoan (2021-07-14 14:00 UTC)

<p>You have forgot to add the <code>self</code> argument to the reporting function when you made it a class member. I’ve made a few simplifications and uploaded a complete working example here:</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/534298ee567000a37b3cb89de01750b8">
  <header class="source">

      <a href="https://gist.github.com/lassoan/534298ee567000a37b3cb89de01750b8" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/534298ee567000a37b3cb89de01750b8" target="_blank" rel="noopener">https://gist.github.com/lassoan/534298ee567000a37b3cb89de01750b8</a></h4>

  <h5>LoadRemoteFile.py</h5>
  <pre><code class="Python">The example was moved to Sandbox extension so that users can more easily install it:

https://github.com/PerkLab/SlicerSandbox/blob/master/LoadRemoteFile/LoadRemoteFile.py

More information: https://github.com/PerkLab/SlicerSandbox/blob/master/README.md#loadremotefile</code></pre>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34513f8646eabef9a132617a9948ae36667a1f85.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34513f8646eabef9a132617a9948ae36667a1f85.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34513f8646eabef9a132617a9948ae36667a1f85.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #8 by @ASH (2021-07-15 04:41 UTC)

<p>It is working finally! Thank you so much for your support lassoan!</p>
<p>Steps:<br>
Put LoadRemoteFile.py in <code>lib\Slicer-4.13\qt-scripted-modules</code> folder<br>
Load module from module finder<br>
Open 3d slicer from slice:// link on browser</p>
<p>I noticed the error “Missing dicomweb_endpoint”, but guess it’s safe to ignore.</p>

---

## Post #9 by @lassoan (2021-07-15 04:54 UTC)

<aside class="quote no-group" data-username="ASH" data-post="8" data-topic="18664">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash/48/11599_2.png" class="avatar"> ASH:</div>
<blockquote>
<p>I noticed the error “Missing dicomweb_endpoint”, but guess it’s safe to ignore.</p>
</blockquote>
</aside>
<p>Yes that’s logged by the DICOM module, as it notices that the application is started with a <code>slicer://</code> URL but the link does not point to a DICOMweb server. It is not an actual error, it is safe to ignore it. I’ll change it to a debug-level message.</p>

---

## Post #10 by @OLIVERFCHEN (2021-10-31 10:31 UTC)

<p>Hi, I followed the above tutorial but still can’t work.</p>
<ol>
<li>Put LoadRemoteFile.py in <code>lib\Slicer-4.13\qt-scripted-modules</code> folder</li>
<li>Load module from module finder --in Modules finder “load Remote File” – Switch to module.</li>
<li>In Chrome input url: slicer://viewer/?download=https%3A%2F%<a href="http://2Fgithub.com" rel="noopener nofollow ugc">2Fgithub.com</a>%2Frbumm%2FSlicerLungCTAnalyzer%2Freleases%2Fdownload%2FSampleData%2FLungCTAnalyzerChestCT.nrrd</li>
</ol>
<p>nothing happened.</p>

---

## Post #11 by @muratmaga (2021-11-01 00:54 UTC)

<p>İf the script doesnt work for you, there is an <code>importfromUrl</code> module in Slicermorph extension.</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImportFromURL">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImportFromURL" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImportFromURL" target="_blank" rel="noopener nofollow ugc">SlicerMorph/Docs/ImportFromURL at master · SlicerMorph/SlicerMorph</a></h3>

  <p><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImportFromURL" target="_blank" rel="noopener nofollow ugc">master/Docs/ImportFromURL</a></p>

  <p><span class="label1">Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #12 by @lassoan (2021-11-01 04:16 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> the question is about how to open an image in 3D Slicer by simply clicking on a link in a web browser (user do not have to launch Slicer manually and copy-paste a URL).</p>
<aside class="quote no-group" data-username="OLIVERFCHEN" data-post="10" data-topic="18664">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oliverfchen/48/13069_2.png" class="avatar"> OLIVERFCHEN:</div>
<blockquote>
<p>I followed the above tutorial but still can’t work.</p>
</blockquote>
</aside>
<p>Most likely you have not associated the <code>slicer://</code> custom browser protocol with the Slicer application. I’ve added more detailed instructions to the top of the <a href="https://gist.github.com/lassoan/534298ee567000a37b3cb89de01750b8">example module</a>. I’ve just tested this module with the latest Slicer Preview Release on Windows and it worked well.</p>

---

## Post #13 by @OLIVERFCHEN (2021-11-02 01:27 UTC)

<p>Thank you for the reply. I reinstalled the latest slicer 4.13.0 and now it worked.<br>
However, when I download url from DCM4CHEE retrieve link,<br>
slicer://viewer/?download=http://192.168.8.113:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.276.0.7230010.3.1.4.3928906.148.15392368.470/series/1.2.276.0.7230010.3.1.4.39968906.148.1539239634.469<br>
It errors out.<br>
So is it only support nrrd file not dcm?</p>

---

## Post #14 by @lassoan (2021-11-02 03:27 UTC)

<p>Opening a file via DICOMweb is much simpler, as it is a built-in feature of Slicer’s DICOM module (no need to install a custom module). You need to use the <code>slicer://viewer/...</code> URL as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/gui.html#launch-slicer-directly-from-a-web-browser">here</a>.</p>

---

## Post #15 by @OLIVERFCHEN (2021-11-02 03:57 UTC)

<p>Thank you, but please bear with me, I still can’t work out.</p>
<p>slicer://viewer/?download=http://192.168.8.113:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.276.0.7230010.3.1.4.3929968906.148.1539239668.470</p>
<p>it did not work, with loading… 0% then<br>
TypeError: reportProgress() takes 2 positional arguments but 3 were given</p>
<p>or if<br>
slicer://viewer/?studyUID=1.2.276.0.7230010.3.1.4.1726399104.1960.1540283292.820<br>
&amp;dicomweb_endpoint=http://192.168.8.113:8080/dcm4chee-arc/aets/DCM4CHEE/rs<br>
&amp;dicomweb_uri_endpoint=http://192.168.8.113:8080/dcm4chee-arc/aets/DCM4CHEE/rs/studies/1.2.276.0.7230010.3.1.4.1726399104.1960.1540283292.820</p>
<p>i got : NameError: name ‘progressCallback’ is not defined</p>

---

## Post #16 by @lassoan (2021-11-02 05:36 UTC)

<p>There was an untested code branch (when access token was not specified) that caused the error above. I’ve <a href="https://github.com/Slicer/Slicer/commit/1c513e68183ea2a83b85ad75f43aadb2a2c5a952">fixed it now</a>, you can apply the code change to the same file in your Slicer installation.</p>

---

## Post #17 by @OLIVERFCHEN (2021-11-02 10:25 UTC)

<p>Yes, that fixed problem. Thanks.</p>

---

## Post #18 by @lassoan (2021-11-02 13:08 UTC)

<p>Great, thanks for the update!</p>
<p>DICOMweb downloads can take a while and we currently only update progress report once for each series. It would be great if you could add more detailed progress reporting to the script in Modules/Scripted/DICOMLib/DICOMUtils.py.</p>

---

## Post #19 by @OLIVERFCHEN (2021-11-03 00:11 UTC)

<p>Is this part? I love to do it if you can give me more information.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5aea8bdfa345d5336abeb34ca6050b07700f5e67.png" data-download-href="/uploads/short-url/cYhu6OH4rYSWDL7QNJk6dI96m3R.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5aea8bdfa345d5336abeb34ca6050b07700f5e67.png" alt="image" data-base62-sha1="cYhu6OH4rYSWDL7QNJk6dI96m3R" width="690" height="106" data-dominant-color="333436"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">927×143 15.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It only shows 0% then jump to 100%, for <em>len(seriesInstanceUIDs)</em> if <em>seriesInstanceUIDs</em> only one then length always 1. So in this <em>for</em> loop, it will not show the values between 0-100.<br>
The script you mentioned in Modules/Scripted/DICOMLib/DICOMUtils.py, is it a different file?</p>
<p>Also, is that possible to detect whether the slicer already opened before downloading? So that windows will not open slicer multiple instances.</p>

---

## Post #20 by @lassoan (2021-11-03 17:55 UTC)

<aside class="quote no-group" data-username="OLIVERFCHEN" data-post="19" data-topic="18664">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oliverfchen/48/13069_2.png" class="avatar"> OLIVERFCHEN:</div>
<blockquote>
<p>It only shows 0% then jump to 100%, for <em>len(seriesInstanceUIDs)</em> if <em>seriesInstanceUIDs</em> only one then length always 1.</p>
</blockquote>
</aside>
<p>I’ve had a look at the progress reporting and found an easy way to do make it more granular (using the <code>iter_series</code> method that was added not too long ago). I’ve also improved error reporting and currently working on selecting the imported series in the DICOM browser. I plan to submit a pull request with these improvements today or tomorrow.</p>
<aside class="quote no-group" data-username="OLIVERFCHEN" data-post="19" data-topic="18664">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oliverfchen/48/13069_2.png" class="avatar"> OLIVERFCHEN:</div>
<blockquote>
<p>is that possible to detect whether the slicer already opened before downloading? So that windows will not open slicer multiple instances.</p>
</blockquote>
</aside>
<p>While there are some operating system level support for singleton applications, there is nothing available on all supported platforms. A nice solution would be to implement a very lightweight launcher application (it could be implemented in Python) that starts Slicer with an extra script. The extra script would create a HTTP server (similarly to how it is done <a href="https://github.com/pieper/SlicerWeb/blob/master/WebServer/WebServer.py">here</a>) which would listen for HTTP requests. For now the only request that it would need to handle is opening of a URL. After Slicer is started, the launcher application would then send an HTTP request with the URL. The launcher application would always check if the HTTP request is responded and if it is then it would not launch Slicer again, it would just send the new URL to the running Slicer to open.</p>
<p>Since this would not be a high-speed operation, communication with a running Slicer instance could be performed via files. For example, we could have an “incoming” folder within the Slicer install folder that Slicer would monitor and if it detected a new file then it would get the URL from that. However, the HTTP request would be a bit more elegant and versatile (e.g., it could be used more easily in a container or from JavaScript applications).</p>
<p><a class="mention" href="/u/pieper">@pieper</a> What do you think? I know that we could just use SlicerWeb extension as is, but it seems more like a prototyping extension, contains lots of hardcoded, project-specific, experimental things and so it is quite complex. We could probably implement URL opening in 20-30 line of code and it could be part of Slicer core, so it could be used easily in various scenarios. For example SimpleITK notebooks use an environment variable to specify a viewer application. Specifying Slicer directly would mean that for opening each image, users need to wait for Slicer startup, which just takes too long. Specifying the launcher application as viewer would allow opening an image in Slicer very quickly.</p>

---

## Post #21 by @pieper (2021-11-03 18:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="18664">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> What do you think? I know that we could just use SlicerWeb extension as is, but it seems more like a prototyping extension, contains lots of hardcoded, project-specific, experimental things and so it is quite complex.</p>
</blockquote>
</aside>
<p>Yes, the SlicerWeb project has a lot of experimental parts and is not complete.  I’ve been thinking for quite a while that it should be refactored and simplified.  That said it does work well and could be the basis for this ‘singleton app’ feature and others.  It probably looks more complex than it really is because I was trying to figure out how it needed to work while developing this version.  The actual core is not that big and most of the rest would be better as plugins.</p>

---

## Post #22 by @lassoan (2021-11-03 19:38 UTC)

<p>Considering that “singleton app” is a core feature, needed in many use cases, it would be much better to have it in the Slicer core.</p>
<p>What do you think about bringing base classes and maybe some stable request handlers (such as opening of an URL) to the Slicer core and leave the experimental and project-specific features in SlicerWeb and other extensions?</p>
<p>Or we could clean up Slicer Web and move out experimental things to other extension(s).</p>

---

## Post #23 by @pieper (2021-11-03 19:53 UTC)

<p>Yes, there’s a very small set of code in SlicerWeb that would enable the essential functionality.  I agree it would be better in the core than in an extension so that people could rely on it being available.  Let me try look into that and try a PR.  It’s really just the one <code>WebServer</code> scripted module.</p>

---

## Post #24 by @lassoan (2021-11-03 20:02 UTC)

<p>Sounds great!</p>
<p>We could consider adding two request handlers to the Slicer core: one for opening an URL and another one for executing Python command and return the output. By default the server would be disabled, so it would not be a security risk.</p>

---

## Post #25 by @pieper (2021-11-03 20:22 UTC)

<p>Yes, I already have a <code>repl</code> endpoint in the web server that accepts python code and returns the result.  The first time the request is received the user gets a dialog to accept or not (along with an ‘always accept’ checkbox).  We may want to make a separate preference for allowing this endpoint since it seems more risky than some of the others (but it’s super powerful too!).</p>
<p>It is definitely important to consider security implications before using this.  I also recently added a <code>certfile</code> option to support https.</p>

---

## Post #26 by @lassoan (2021-11-04 19:48 UTC)

<p><a class="mention" href="/u/oliverfchen">@OLIVERFCHEN</a></p>
<p>I’ve pushed the DICOMweb import enhancements, which will be available in the Slicer Preview Release from tomorrow. Improvements include:</p>
<ul>
<li>fine-grained progress reporting during downloading of each series (not just when a series download is completed)</li>
<li>avoid re-downloading of content already in the local DICOM database</li>
<li>select loaded content in the DICOM browser when import is finished</li>
<li>improved error handling (errors are displayed in a popup window)</li>
</ul>
<p>While <a class="mention" href="/u/pieper">@pieper</a> takes care of moving core parts of the web server to the Slicer core, you can already write a Python script that starts Slicer (if not started already) and uses the <a href="https://github.com/pieper/SlicerWeb/">SlicerWeb extension</a> to make it load an image via a web request.</p>

---

## Post #27 by @OLIVERFCHEN (2021-11-10 13:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
I download the newest slicer 4.13.0-2021-11-9, I tested using the URL to open the slicer, but it took much longer time than before to download the data. Wonder if this is only me?<br>
Confirmed when the file already existed in the slicer, it will not download again.</p>

---

## Post #28 by @lassoan (2021-11-10 16:15 UTC)

<p>Good catch, thanks for reporting this. The download time got increased by the combination of detailed logging and increased progress reporting. On a test case, download time increased from 150sec to 244sec. I’ve updated the importer to only report warnings and errors during series download, which cut the download time to 68sec.</p>
<p>The <a href="https://github.com/Slicer/Slicer/commit/a4d51a19f2ce0a553a2b4cc9fa8bade0781df568">fix</a> will be included in the Slicer Preview Releases from tomorrow but you can apply the change to your local installation now (just modification of a single .py file).</p>

---

## Post #29 by @OLIVERFCHEN (2021-11-18 01:42 UTC)

<p>I’ve been waiting for the update about the “singleton app”, any news?</p>

---

## Post #30 by @lassoan (2021-11-18 03:52 UTC)

<p>The pull request to integrate the WebServer module into Slicer core is still under review:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5999">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5999" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5999" target="_blank" rel="noopener">ENH: add WebServer module</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>pieper:add-webserver</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-05" data-time="21:25:19" data-timezone="UTC">09:25PM - 05 Nov 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="3 commits changed 14 files with 2760 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5999/files" target="_blank" rel="noopener">
          <span class="added">+2760</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Code imported from Steve Pieper's development repository.

https://github.com/<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5999" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">pieper/SlicerWeb</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You don’t need to wait for this to be merged. You can get the WebServer module files from that branch and copy them into your <code>&lt;SlicerInstallFolder&gt;lib\Slicer-4.13\qt-scripted-modules</code> folder then start Slicer and open the WebServer module. It starts the web server automatically. Instead of the GUI, you can also start Slicer and start the WebServer module from the command line.</p>
<p>After this, you can make Slicer open a file by sending a command via Slicer’s REST API. For example, you can open a file by running these few lines from any Python environment:</p>
<pre><code class="lang-python">import requests
import sys
filename=sys.argv[-1].replace('\\','/')
port = 2016
requests.post(url=f'http://localhost:{port}/slicer/repl', data='slicer.app.loadFiles([\''+filename+'\'])', timeout=15)
</code></pre>
<p>You can use Slicer’s Python interpreter to run this (unlike the full Slicer application, it starts up in a second) by copying the above script into a new <code>ShowInSlicer</code> folder: <code>&lt;SlicerInstallFolder&gt;/bin/Python/ShowInSlicer/__main__.py</code> (this creates a Python module that can be referred to by name instead of a full path). After this, you can execute this command in the terminal:</p>
<pre><code class="lang-auto">PythonSlicer.exe -m ShowInSlicer c:\tmp\CTChest.nrrd
</code></pre>
<p>It will open the specified file in the running Slicer instance.</p>
<p>After the WebServer module will be integrated into the Slicer core, I’ll add a Python script like the one above to the Slicer core, so it will not be necessary to mess with copying files. It could also make sense to add detection of the server to the script: if the server is not running then the script could start Slicer.</p>

---

## Post #31 by @kmordhwaj (2023-01-19 09:28 UTC)

<p>Can we upload more than 50 nifti files at a time with a link or can we upload a folder of these much nifti files through script in 3d slicer?</p>

---

## Post #32 by @pieper (2023-01-19 16:47 UTC)

<p>Yes, you can do this.</p>

---

## Post #33 by @kmordhwaj (2023-01-20 04:31 UTC)

<p>How to do that <a class="mention" href="/u/pieper">@pieper</a> ? Is there is any script available? or we just need to pass a link with the prams which have the downloadable folder of these much files. Because I think we can’t pass it in link as folder is not considered as downloadable file.<br>
please help.</p>

---

## Post #34 by @pieper (2023-01-20 12:57 UTC)

<p>The scripts <a class="mention" href="/u/lassoan">@lassoan</a> posted just above your post gives the formula, just repeat it for all your volumes.  One note: the WebServer module is now is the Slicer release, so no need for special installation.  Also the <code>repl</code> endpoint has been renamed <code>exec</code>.  What this <code>exec</code> endpoint allows is for external programs (e.g. python or shell scripts) to invoke the execution of python code in the Slicer application just as if it had been typed in the python console of the application or initiated by other GUI actions in the application.  It’s a very powerful feature so you should be able to accomplish whatever you are trying to do.</p>
<p>If this isn’t clear, please post what specifically you are trying to accomplish and what tools you are using and maybe we can make more concrete suggestions.</p>

---

## Post #35 by @kmordhwaj (2023-01-20 13:02 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> . I will give it a try.</p>

---

## Post #36 by @lassoan (2023-01-20 13:27 UTC)

<p>There have been even more improvements since this thread was started: you can use the <a href="https://pypi.org/project/slicerio/0.1.8/">slicerio Python</a> package to conveniently open an image in Slicer bya simple Python call. slicerio launches Slicer with web server interface enabled and opens the file.</p>
<p>For example, after installing slicerio Python package, run this in any local Python environment to open an image in Slicer:</p>
<pre><code class="lang-auto">import slicerio.server
slicerio.server.file_load("https://github.com/rbumm/SlicerLungCTAnalyzer/releases/download/SampleData/LungCTAnalyzerChestCT.nrrd", slicer_executable="path/to/Slicer.exe")
</code></pre>
<p>See more information and examples <a href="https://github.com/lassoan/slicerio#view-files-in-3d-slicer">here</a>.</p>

---

## Post #37 by @kmordhwaj (2023-01-20 13:32 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. It is a great updated feature. But this is for a one file, can I open slicer 3d with a link which contains a folder of the files? Like how we are importing a single file or a directory in 3d slicer.</p>

---

## Post #38 by @lassoan (2023-01-20 13:37 UTC)

<p>What is your end goal? Quickly view the 50 files one by one? Or view more (or all) at once?</p>
<p>Are those files in a local directory or a web server somewhere? If you show them one by one, how do you decide on the order?</p>
<p>Does the user need to do anything with them? For example, view one by one and approve or flag each? Maybe edit some segmentation results and submit the revised segmentation to a server?</p>

---

## Post #39 by @kmordhwaj (2023-01-20 13:46 UTC)

<p>Thanks for replying <a class="mention" href="/u/lassoan">@lassoan</a> , My folder which contains 50 NIFTI files is in my local repository. I mean in my app in cloud as .zip file.<br>
when user click “label in slicer” then it will download zip and the zip will be extracted and will be in local downloads folder. (so can say the folder is in local directory).<br>
There is a feature in the 3d slicer where I can take a file or a directory so I am trying to open 3d slicer and the directory should load.<br>
I can open and place a file by cli command in subprocess, but giving error while putting folder in path.</p>
<p>The user want to label it and edit it to get obj file.</p>

---

## Post #40 by @lassoan (2023-01-20 14:24 UTC)

<p>This use case is often implemented by simply sharing a dropbox or onedrive folder. The user drag-and-drops an image into the Slicer application window, segments it, and saves the result. Since segmentation typically takes tens of minutes, the 10-20 second task of loading and saving data usually does not justify doing any Python scripting to speed up things.</p>
<p>A more modern approach is to use MONAILabel for this. You can start a single MONAILabel server and many users can connect to it using the MONAILabel extension in 3D Slicer. MONAILabel automatically provides an image by a single click; the user can then segment the image (optionally MONAILabel may provide a default AI segmentation) and finally the user uploads the segmentation result by a single click.</p>

---

## Post #41 by @kmordhwaj (2023-02-13 12:04 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I followed these conversations. Upto Chat <span class="hashtag">#7</span>, I am successfully opening the mentioned .nrrd file in your example from that link. But when I am sending a downloadable .nrrd file from AWS S3 bucket, the url had some tokens, So it is not loading the file in Slicer 3D. And I am facing same error as discussed by <a class="mention" href="/u/oliverfchen">@OLIVERFCHEN</a> in Chat <span class="hashtag">#14</span>, its in 0%, and given that positional argument related error. I followed the next chats. And your fix in Chat <span class="hashtag">#15</span> is already there in that Dicom util file. Please help.</p>

---

## Post #42 by @lassoan (2023-02-13 15:00 UTC)

<p>Could you please provide an example URL that you would expect to work but it doesn’t?</p>

---

## Post #44 by @lassoan (2023-02-13 17:12 UTC)

<p>It was all good, you just forgot to <a href="https://www.urlencoder.io/">URL-encode</a> the URL, so the script interpreted the URL parameters as additional query parameters for Slicer.</p>
<p>I’ve made some improvements to the LoadRemoteFile module (it can now open multiple volumes and segmentations and show them in 3D) and moved it to the Sandbox extension, so that users can easily install it by a few clicks.</p>
<p>How to use:</p>
<ul>
<li>Install latest version of Sandbox extension (on 2023-02-14 or later)</li>
<li>Construct an URL as explained <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/README.md#loadremotefile">here</a> and open the URL in a web browser. For example, copy these URLs to the web browser’s address bar to open them in Slicer:
<ul>
<li>LungCTAnalyzerChestCT image: <code>slicer://viewer/?download=https%3A%2F%2Fgithub.com%2Frbumm%2FSlicerLungCTAnalyzer%2Freleases%2Fdownload%2FSampleData%2FLungCTAnalyzerChestCT.nrrd</code>
</li>
<li>LungCTAnalyzerChestCT image + segmentation: <code>slicer://viewer/?show3d=true&amp;segmentation=https%3A%2F%2Fgithub.com%2Frbumm%2FSlicerLungCTAnalyzer%2Freleases%2Fdownload%2FSampleData%2FLungCTAnalyzerMaskSegmentation.seg.nrrd&amp;image=https%3A%2F%2Fgithub.com%2Frbumm%2FSlicerLungCTAnalyzer%2Freleases%2Fdownload%2FSampleData%2FLungCTAnalyzerChestCT.nrrd</code>
</li>
</ul>
</li>
</ul>

---

## Post #45 by @kmordhwaj (2023-02-14 05:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, Installed Sandbox extension but it had installed (2022-12-31) version. It is not even loading the example nrrd file.<br>
I followed the updated LoadRemoteFile.py and placed it in qt-scripted-modules folder.<br>
Now file is not downloading my encoded file (but downloading the provided .nrrd file in example). It is just giving 0% in pop-up and in log also 3 times. Then after giving error while trying to remove the file (os.remove()) as the file is not downloaded.<br>
Please help Sir.</p>

---

## Post #46 by @kmordhwaj (2023-02-14 06:59 UTC)

<p>Sorry Sorry. Thanks Sir. It’s working. With that segmentation key.</p>

---

## Post #47 by @kmordhwaj (2023-02-16 14:14 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, Sandbox extension is now installing still version 2022-12-31. Can you please tell me how to install the latest(2023-02-14 or later) ?</p>
<p>Oh. Okay. Its installed by default version 2022-12-31. But when checked for update, Its giving version 2023-02-14 available.</p>

---

## Post #48 by @lassoan (2023-02-16 14:29 UTC)

<p>See how to update an extension <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#update-extensions">here</a>.</p>
<p>Update from Extensions Manager is available for latest Slicer Stable Release.</p>
<p>If you use a Slicer Preview Release then you don’t get extension updates but you need to install a more recent Slicer Preview Release.</p>

---

## Post #49 by @kmordhwaj (2023-02-16 19:31 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , There is a bug in LoadRemoteFile.py . The encoded URI is not properly decoding here in the code. Each time the log in slicer is showing “//////” inside the URI instead of “%F%F%F” after decoding. So my file is not uploading in the slicer.</p>
<p>I had crosschecked the file by <a href="https://www.urlencoder.io/" rel="noopener nofollow ugc">encoding</a> an <a href="https://www.urldecoder.io/" rel="noopener nofollow ugc">decoding</a> the encoded file.<br>
It is giving the actual downloadable file.</p>

---

## Post #50 by @lassoan (2023-02-16 19:39 UTC)

<p>Please provide a complete example that reproduces the issue.</p>

---

## Post #52 by @lassoan (2023-02-16 20:04 UTC)

<p>Thanks, the url was decoded twice. Fixed now.</p>

---

## Post #54 by @Likitha_Shetty (2024-01-03 11:22 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> I am able to load a NIFTI file from the terminal using the  <code>open -a "Slicer" --args</code> command. But not from the web browser. I am on a macOS so I understand I need to manually associate the “slicer://” custom URL protocol to the 3D Slicer application. I have appended the Info.plist file of the Application with the following</p>
<pre><code class="lang-auto">&lt;key&gt;CFBundleIdentifier&lt;/key&gt;
&lt;string&gt;viewer&lt;/string&gt;
&lt;key&gt;CFBundleURLTypes&lt;/key&gt;
&lt;array&gt;
&lt;dict&gt;
&lt;key&gt;CFBundleURLName&lt;/key&gt;
&lt;string&gt;slicer&lt;/string&gt;
&lt;key&gt;CFBundleURLSchemes&lt;/key&gt;
&lt;array&gt;
&lt;string&gt;slicer&lt;/string&gt;
&lt;/array&gt;
&lt;/dict&gt;
&lt;/array&gt;
</code></pre>
<p>Is there anything else i should do for the web browser link to work? Really appreciate your help.</p>

---

## Post #55 by @lassoan (2024-01-06 04:38 UTC)

<p>It looks good.</p>
<p>I’m not sure about the <code>viewer</code> (it must be unique, so something like <code>org.slicer.slicer</code> could be more appropriate) and you may need to double-click on the bundle to register this URL handler - see this page for some more details:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://web.archive.org/web/20200618072827/https://support.shotgunsoftware.com/hc/en-us/articles/219031308-Launching-Applications-Using-Custom-Browser-Protocols">
  <header class="source">
      <img src="https://web.archive.org/web/20200618072827im_/https://theme.zdassets.com/theme_assets/7538/b0cb3f20a70e215b2704195b7e61c32c51d79598.png" class="site-icon" width="16" height="16">

      <a href="https://web.archive.org/web/20200618072827/https://support.shotgunsoftware.com/hc/en-us/articles/219031308-Launching-Applications-Using-Custom-Browser-Protocols" target="_blank" rel="noopener">Shotgun Support</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:139/20;"><img src="https://web.archive.org/web/20200618072827im_/https://theme.zdassets.com/theme_assets/7538/a9cf7888439f8fcfada3710e4cfca2ffc9d569c6.png" class="thumbnail" width="139" height="20"></div>

<h3><a href="https://web.archive.org/web/20200618072827/https://support.shotgunsoftware.com/hc/en-us/articles/219031308-Launching-Applications-Using-Custom-Browser-Protocols" target="_blank" rel="noopener">Launching applications using custom browser protocols</a></h3>

  <p>Contents

Registering a protocol

Registering a protocol on Windows
Registering a protocol on OSX
Registering a protocol on Linux




A very practical version of an Action Menu Item (AMI) is a vari...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It is also possible that this only works for signed applications (Slicer Stable Releases), or you may need to move the application folder somewhere or restart the computer <a href="https://apple.stackexchange.com/a/51416">for the OS to pick up the plist file</a>.</p>
<p>Note that we will work on registration of custom URL handlers for Slicer for Windows/Linux/macOS during the upcoming project week - see <a href="https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/Launch3DslicerViaClickableUrlsForViewingIdcDataViaSliceridcbrowserAndIdcIndex/" class="inline-onebox">Project Description | NA-MIC Project Weeks</a><br>
It would be nice to have some successful test of this working before the event, so if you have any updates (either that it’s working or you have some errors) then please share.</p>

---

## Post #56 by @Likitha_Shetty (2024-01-08 17:28 UTC)

<p>Thanks so much for responding.</p>
<p>I made the following updates as per your suggestion</p>
<ol>
<li>Update <code>viewer</code> to <code>org.slicer.slicer</code></li>
<li>Double click on the bundle</li>
</ol>
<p>I ensured the other items from the article were in place too but I still couldn’t open a NIFTI image from the browser. Note that I tried this with the latest preview release of the 3D slicer i.e. 5.7.0</p>
<p>When I tried to use the latest stable release i.e. 5.6.1, it failed to load the image even from the terminal as the modification of the Info.plist file led to the app crashing.</p>

---

## Post #57 by @vkt1414 (2024-01-31 07:27 UTC)

<p>Hi <a class="mention" href="/u/likitha_shetty">@Likitha_Shetty</a>, stumbled upon this again as I wanted to read <a class="mention" href="/u/lassoan">@lassoan</a> suggestions again. I got slicer:// protocol registration to work on macOS.<br>
Here’s the shell script that will do the registration.<br>
<a href="https://gist.github.com/vkt1414/1319c5b4794480e8953187cf76093a7b" rel="noopener nofollow ugc">macOSregistration (github.com)</a></p>
<p>Here’s how I extend <a class="mention" href="/u/lassoan">@lassoan</a> initial work, and integrate the above shell script to run with in slicer env, to register slicer:// protocol on Linux and Mac, download data from IDC and load to a scene. The below link may or may not be persistent as it will eventually live under ImagingDataCommons. But we do plan to contribute the registration process on Linux and MacOS in coming weeks or months to Slicer directly as we refine the behavior when a user has multiple versions of slicer.</p>
<p><a href="https://github.com/vkt1414/SlicerIDCBrowser/blob/add-slicer-idc-viewer/IDCBrowser/IDCViewer.py" rel="noopener nofollow ugc">SlicerIDCBrowser/IDCBrowser/IDCViewer.py at add-slicer-idc-viewer · vkt1414/SlicerIDCBrowser (github.com)</a></p>
<p>I’m still very new to slicer dev but happy to help if anything is with in my reach.</p>

---
