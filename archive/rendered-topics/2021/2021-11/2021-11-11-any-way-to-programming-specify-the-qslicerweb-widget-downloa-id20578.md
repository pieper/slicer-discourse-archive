# Any way to programming specify the qSlicerWeb Widget download file location?

**Topic ID**: 20578
**Date**: 2021-11-11
**URL**: https://discourse.slicer.org/t/any-way-to-programming-specify-the-qslicerweb-widget-download-file-location/20578

---

## Post #1 by @episodes (2021-11-11 13:07 UTC)

<p>Hi,<br>
I’m currently using the qSlicerWeb widget to build an embedded Dicom manage system based on the web.  I’m wondering if there’s any way to programming set the file download save folder by python? we have the custom script that needs to scan the file in a specific location.<br>
Thanks!</p>

---

## Post #2 by @lassoan (2021-11-11 13:19 UTC)

<p>You can configure all folders that Slicer uses in the application settings (Slicer.ini file). You can edit it by using the <code>qt.QSettings()</code> object. Paths can be relative path in the Slicer installation tree or an absolute path; shared between all Slicer instances or specific to one Slicer install tree.</p>
<p>We have implemented several features that allow serving a DICOM database from an internal or external web browser (on the same computer or from remote computers) or launch Slicer from the web browser (e.g., using Kheops or OHIF viewer). We are also adding a new module to the Slicer core within a week or so, which exposes Slicer as a web service (<a href="https://github.com/Slicer/Slicer/pull/5999" class="inline-onebox">ENH: add WebServer module by pieper · Pull Request #5999 · Slicer/Slicer · GitHub</a>).</p>
<p>Tell us a bit about the workflow that you are planning to implement (how the images are imported, how the user browses the data sets, what happens with created/modified data) and how (what framework do you use as a patient browser and viewer, how do you trigger launching Slicer and loading images, etc.) and we can give advice about how to take advantage of all the existing features.</p>

---

## Post #3 by @episodes (2021-11-13 06:06 UTC)

<p>Hi, lassoan,<br>
Thanks for your reply<br>
Our workflow requires using an embed browser running on the slicer end to allow the doctors to manage their images. The browser’s URL is set to a custom build web-based Dicom management system, pretty much like the <strong>kheops</strong> you did. but the different is all the operations need to be done using the embed browser in the slicer.<br>
for example <strong>import image</strong>, we want the user would be able to click a button (from the web-based Dicom management running at embed browser in slicer), the slicer will automatically download, opened and store the requested image file to our set location and close the browser window, without pop-ups asking the user to <strong>load</strong> or <strong>save as</strong> every time in order to simplify the doctor’s workflow.<br>
We need more controls of the qSlicerWeb widget. one of the challenges we faced is not much documentation about qSlicerWeb available, majority of the docs is the C++ one, I have tried one on the <a href="https://apidocs.slicer.org/v4.8/classqSlicerWebWidget.html" rel="noopener nofollow ugc">apidocs.slicer.org</a>  e.g. the <strong>onLinkClicked()</strong> seems not many of them are implemented on the python end.</p>
<blockquote>
<p>QObject::connect() signal ‘onLinkClicked’ does not exist on qSlicerWebWidget</p>
</blockquote>

---

## Post #4 by @lassoan (2021-11-13 13:54 UTC)

<p>Qt has removed its nice and simple webkit-based browser (QWebView) and added a huge, very complicated, but very powerful Chromium-based browser instead (QWebEngine). I loved the <code>onLinkClicked</code> signal in QWebView, but it does not exist anymore. You need to set up web sockets instead. See details in <a href="https://github.com/Slicer/Slicer/blob/master/Base/QTGUI/qSlicerWebWidget.cxx">qSlicerWebWidget implementation</a>.</p>
<p>See current documentation of the Slicer web widget <a href="https://apidocs.slicer.org/master/classqSlicerWebWidget.html">here</a>.</p>
<p>If you find Slicer’s built-in browser inconvenient then you can serve your web application from Slicer but open it in an external browser. You can communicate with Slicer using the REST API provided by the WebServer module.</p>
<aside class="quote no-group" data-username="episodes" data-post="3" data-topic="20578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/episodes/48/13082_2.png" class="avatar"> episodes:</div>
<blockquote>
<p>for example <strong>import image</strong> , we want the user would be able to click a button (from the web-based Dicom management running at embed browser in slicer), the slicer will automatically download, opened and store the requested image file to our set location and close the browser window, without pop-ups asking the user to <strong>load</strong> or <strong>save as</strong> every time in order to simplify the doctor’s workflow.</p>
</blockquote>
</aside>
<p>When you use Kheops (or you set up OHIF like that) then you can open the the selected study in Slicer without any popups (your browser asks first if you want to always ask before opening the custom URL in Slicer but if you choose not to ask again then there are no more popups) with a single click.</p>
<p>With a short Python script you can suppress scene saving confirmation popups and discard all changes or save all changes automatically.</p>
<hr>
<p>Thanks for the additional information about your workflow. It explains a few things, but not everything is clear yet.</p>
<ul>
<li>What do you mean by “web-based DICOM management system”? Do you want to just browse the patient/study/series list in the web browser or also view or even annotate and segment images in the browser?</li>
<li>Do you want to use your web-browser based DICOM browser because you prefer the appearance? Is there any particular functional limitation or other issue with Slicer’s DICOM browser or you just don’t like how it looks? Are there any other desktop applications (OsiriX, Weasis, …?) that have a DICOM browser that you think looks nicer and your users would accept?</li>
<li>Do you use the web-based DICOM browser only on the same computer where Slicer is running or users may connect to it from other computers?</li>
<li>Where do you store the data sets? In a DICOMweb database? Do you need to manage any non-DICOM data?</li>
</ul>

---

## Post #5 by @pieper (2021-11-13 17:54 UTC)

<p>As of <a href="https://github.com/Slicer/Slicer/commit/809c516fcdd91d26c5566dc4ddea8fe751f8362e">this commit</a> you can override the download behavior for the web widget so that Slicer handles it in whatever way you choose.</p>
<p>Also, when you are using the <code>qSlicerWebWidget</code> you have total bidirectional control via JavaScript and Python.  For example in SlicerMorph, this is used to <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/MorphoSourceBrowse/MorphoSourceBrowse.py#L115-L130">enter username and password</a> to the web page, but really anything is possible to control, like changing the contents of the links, adding new buttons etc.  The  js code can also control Slicer’s python environment using <code>window.slicerPython.evalPython()</code>.  See <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/WebEngine.py#L142-L225">the test code</a> for examples.</p>

---

## Post #6 by @episodes (2021-11-17 08:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>WebServer module</p>
</blockquote>
</aside>
<p>Hi lassoan,<br>
Thanks for your reply,</p>
<p>The “web-based DICOM management system” is just an online patient studies system running on the web and we’d like to do all the images related operations such as annotation and segmentation in the slicer and open with the selected images through a button on the web.</p>
<p>We attempted the restful API approach that you just recommend before, one biggest problem we encountered is it will open multiple instances of slicer application, we want to keep the slicer in singleton instance and if the doctors click another image link in the web, it doesn’t open another slicer, the old slicer should pop-ups a prompts asking the doctor whatever he would like to open and view another file before he saved.</p>

---

## Post #7 by @pieper (2021-11-17 20:32 UTC)

<p>From your description of the desired behavior I would say the same behavior could be accomplished using either the qSlicerWebWidget or the WebServer approach, but probably the widget is easier and has the advantage that the widget running the web app can be positioned by Slicer and even packed into the layout like the dicom browser is.</p>

---

## Post #8 by @lassoan (2021-11-18 13:36 UTC)

<aside class="quote no-group" data-username="episodes" data-post="6" data-topic="20578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/episodes/48/13082_2.png" class="avatar"> episodes:</div>
<blockquote>
<p>We attempted the restful API approach that you just recommend before, one biggest problem we encountered is it will open multiple instances of slicer application</p>
</blockquote>
</aside>
<p>See this thread on how to open a file in an already running Slicer instance using the new WebServer module:</p>
<aside class="quote quote-modified" data-post="30" data-topic="18664">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-load-nifti-file-from-web-browser-link/18664/30">How to load nifti file from web browser link?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    The pull request to integrate the WebServer module into Slicer core is still under review: 


You don’t need to wait for this to be merged. You can get the WebServer module files from that branch and copy them into your &lt;SlicerInstallFolder&gt;lib\Slicer-4.13\qt-scripted-modules folder then start Slicer and open the WebServer module. It starts the web server automatically. Instead of the GUI, you can also start Slicer and start the WebServer module from the command line. 
After this, you can make S…
  </blockquote>
</aside>

<p>Call <code>slicer.app.openUrl</code> instead of <code>slicer.addp.loadFiles([...])</code> in the last line of the code snippet to load from a DICOMweb URL instead of a local file.</p>

---

## Post #9 by @episodes (2021-11-23 12:15 UTC)

<p>Thanks<br>
It does work on my local machine, but the request seems to be blocked on the remote server by the browser’s <em>CORS</em> policy, is there any way to enable ‘Access-Control-Allow-Origin’, ‘*’ in the WebServer module for <strong>/slicer/repl</strong> ?</p>

---

## Post #10 by @pieper (2021-11-23 14:46 UTC)

<p>Good question - I haven’t tried CORS in the Slicer WebServer, but it should just be a matter of adding a header or two in the right place.  Typically I host the web app statically from the WebServer’s docroot so the repl requests are from the same origin.</p>

---
