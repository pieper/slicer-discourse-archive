# Using Webserver DicomWeb interface with OHIF (CORS enabled)

**Topic ID**: 39736
**Date**: 2024-10-17
**URL**: https://discourse.slicer.org/t/using-webserver-dicomweb-interface-with-ohif-cors-enabled/39736

---

## Post #1 by @Kynetyk (2024-10-17 03:15 UTC)

<p>Hello!</p>
<p>I just found out the WebServer extension in Slicer and discovered that it provided a DicomWeb interface to the dicom database.</p>
<p>I would like to use it with OHIF (3.8.3, running locally for now), without the need to setup a reverse proxy. I enabled the CORS option, however I can’t seem to get it to work. The dicom-client of OHIF will send preflight requests which will just hang on the slicer webserver, since OPTIONS requests are dismissed. Browser will then just hang waiting for the preflight response.</p>
<p>Preflights are sent when trying to fetch the <code>/studies/{...}/series</code> and <code>/studies/{...}/metadata</code> routes.</p>
<p>relevant line : <a href="https://github.com/Slicer/Slicer/blob/ba3a9fdc04c9f4fc47cad331f9160b6d7a0beded/Modules/Scripted/WebServer/WebServer.py#L422" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Modules/Scripted/WebServer/WebServer.py at ba3a9fdc04c9f4fc47cad331f9160b6d7a0beded · Slicer/Slicer · GitHub</a></p>
<p>I was wondering if my setup was wrong, or this use case is not implemented.<br>
I’m on Windows (WSL2) with Slicer 5.6.2. Here’s my datasource config in OHIF if it’s any help</p>
<pre data-code-wrap="json"><code class="lang-json">    {
      friendlyName: 'Slicer 3D',
      namespace: '@ohif/extension-default.dataSourcesModule.dicomweb',
      sourceName: 'slicer',
      configuration: {
        name: 'Slicer',
        wadoUriRoot: 'http://localhost:2016/dicom',
        qidoRoot: 'http://localhost:2016/dicom',
        wadoRoot: 'http://localhost:2016/dicom',
        qidoSupportsIncludeField: true,
        imageRendering: 'wadouri',
        thumbnailRendering: 'wadouri',
        enableStudyLazyLoad: true,
        supportsFuzzyMatching: true,
      },
    },
</code></pre>

---

## Post #2 by @lassoan (2024-10-17 03:27 UTC)

<p>I’m not sure if you are aware that Slicer already comes with a preconfigured OHIF viewer that you can launch by a few clicks. I’ve just tested it now and everything works well.</p>
<p>You can start the DICOMweb server in Slicer and launch OHIF viewer by starting the Slicer web server with DICOMweb API and static pages enabled, opening the static pages in a web browser, and clicking on the “DICOM database browser” link. No need to download or configure OHIF (unless you want a different version than what already comes with Slicer):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b70ac1f8c9c13bf35098f57c11566f34d3691ac.jpeg" data-download-href="/uploads/short-url/3UKi32eApjm2rN5G5MFCxtv14p6.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b70ac1f8c9c13bf35098f57c11566f34d3691ac_2_690x374.jpeg" alt="image" data-base62-sha1="3UKi32eApjm2rN5G5MFCxtv14p6" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b70ac1f8c9c13bf35098f57c11566f34d3691ac_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b70ac1f8c9c13bf35098f57c11566f34d3691ac_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b70ac1f8c9c13bf35098f57c11566f34d3691ac_2_1380x748.jpeg 2x" data-dominant-color="626266"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1043 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Just make sure to give enough time (several minutes) for OHIF to start if you have lots of data sets in your DICOM database.</p>
<p>You can find the server configuration that Slicer uses here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/ba3a9fdc04c9f4fc47cad331f9160b6d7a0beded/Modules/Scripted/WebServer/Resources/docroot/browse.html">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/ba3a9fdc04c9f4fc47cad331f9160b6d7a0beded/Modules/Scripted/WebServer/Resources/docroot/browse.html" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/ba3a9fdc04c9f4fc47cad331f9160b6d7a0beded/Modules/Scripted/WebServer/Resources/docroot/browse.html" target="_blank" rel="noopener">Slicer/Slicer/blob/ba3a9fdc04c9f4fc47cad331f9160b6d7a0beded/Modules/Scripted/WebServer/Resources/docroot/browse.html</a></h4>


      <pre><code class="lang-html">&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;

&lt;head&gt;
	&lt;meta charset="utf-8" /&gt;

	&lt;meta name="description" content="3D Slicer DICOM Database displayed using OHIF Viewer" /&gt;
	&lt;meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1,maximum-scale=1,user-scalable=no" /&gt;
	&lt;meta name="theme-color" content="#000000" /&gt;
	&lt;meta http-equiv="cleartype" content="on" /&gt;
	&lt;meta name="MobileOptimized" content="320" /&gt;
	&lt;meta name="HandheldFriendly" content="True" /&gt;
	&lt;meta name="apple-mobile-web-app-capable" content="yes" /&gt;

	&lt;!-- WEB FONTS --&gt;
	&lt;link href="https://fonts.googleapis.com/css?family=Sanchez" rel="stylesheet" /&gt;

	&lt;title&gt;3D Slicer DICOM Database&lt;/title&gt;
&lt;/head&gt;

</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/ba3a9fdc04c9f4fc47cad331f9160b6d7a0beded/Modules/Scripted/WebServer/Resources/docroot/browse.html" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Kynetyk (2024-10-17 13:31 UTC)

<p>Hi Andras,<br>
Ah nice! I didn’t know that.</p>
<p>However in my case I wanted to use Slicer as a dicomweb server only, since we have our own custom OHIF extensions and modes that we are developing. (I’m looking for a dicomweb solution that’s easy to install locally, if any comes to mind)</p>
<p>In case of the built-in OHIF, the dicom-web client doesn’t send preflight requests since the viewer is served from the same host as the dicomweb server (<a href="http://localhost:2016" rel="noopener nofollow ugc">http://localhost:2016</a>).</p>
<p>Without an OPTIONS request handler, I’m not sure how the “Enable CORS” option would work… I’ll try to add that request handler, and if it solves the issue I can open a PR.</p>

---

## Post #4 by @pieper (2024-10-17 13:48 UTC)

<p>It should be easy enough to add OPTIONS support to the Slicer WebServer module.  It would be great if you could add it.</p>
<aside class="quote no-group" data-username="Kynetyk" data-post="3" data-topic="39736">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kynetyk/48/78245_2.png" class="avatar"> Kynetyk:</div>
<blockquote>
<p>I’m looking for a dicomweb solution that’s easy to install locally, if any comes to mind</p>
</blockquote>
</aside>
<p>Slicer’s dicom database and dicomweb server may handle some practical use cases, but it’s not really tested on huge data.  I’ve used maybe a few thousand studies.</p>
<p>Some of us also worked on this approach with a more scalable database.  I’ve been told by some users that it’s actually working well in a high-volume production environment.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/dcmjs-org/dicomweb-server">
  <header class="source">

      <a href="https://github.com/dcmjs-org/dicomweb-server" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/c75d5011ef142c7013cab0106dff0038/dcmjs-org/dicomweb-server" class="thumbnail">

  <h3><a href="https://github.com/dcmjs-org/dicomweb-server" target="_blank" rel="noopener">GitHub - dcmjs-org/dicomweb-server: Lightweight DICOMweb Server with CouchDB</a></h3>

    <p><span class="github-repo-description">Lightweight DICOMweb Server with CouchDB</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Kynetyk (2024-10-17 16:31 UTC)

<p>Thanks for the link Steve, I’ll keep that project in mind for high volume of data!</p>
<p>In my immediate situation, I was rather looking for something like a small daemon to could expose through dicomweb the content of a dicom folder with perhaps at most a couple of hundred series. Something like <a href="https://github.com/RadicalImaging/static-dicomweb" class="inline-onebox" rel="noopener nofollow ugc">GitHub - RadicalImaging/Static-DICOMWeb</a> but with a tiny GUI and an installer. The goal here is to have end users test-run our OHIF extensions without the need to setup Orthanc or a server. In that sense, Slicer seems like a good solution.</p>
<p>Regarding CORS, after adding the OPTIONS handler, things seems to work out! I’ve open a PR here <a href="https://github.com/Slicer/Slicer/pull/7998" class="inline-onebox" rel="noopener nofollow ugc">BUG: add missing OPTIONS request handler when CORS enabled by Gabsha · Pull Request #7998 · Slicer/Slicer · GitHub</a></p>

---
