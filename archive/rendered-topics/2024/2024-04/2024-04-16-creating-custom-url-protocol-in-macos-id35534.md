---
topic_id: 35534
title: "Creating Custom Url Protocol In Macos"
date: 2024-04-16
url: https://discourse.slicer.org/t/35534
---

# Creating Custom URL protocol in macOS

**Topic ID**: 35534
**Date**: 2024-04-16
**URL**: https://discourse.slicer.org/t/creating-custom-url-protocol-in-macos/35534

---

## Post #1 by @Gil (2024-04-16 14:02 UTC)

<p>Operating system: macOS<br>
Slicer version: 5.6.2</p>
<p>Expected behavior: based on the developer guide to launch Slicer directly from browser, it will be based on custom url protocol.  This is done automatically in the Windows installer and can be set up on other operating systems manually.</p>
<p>when trying to create that custom URL protocol in MacOS, it require changing the Info.plist file.</p>
<p>after doing so, it is expected that the custom URL protocol will work.</p>
<p>Actual behavior:<br>
when trying to open slicer through the URL, the URL is recognized, but the 3D Slicer won’t open because the macOS is recognizing the altered Info.plist as - /Applications/Slicer.app: invalid Info.plist (plist or signature have been modified)</p>
<p>meaning, that there is invalidation of the signature in the macOS of the 3D Slicer.</p>
<p>Is there a way to solve it?</p>
<p>In general what I am trying to do is create a link that will open the 3D Slicer with a specific DICOM folder based on a path specified in that link. I tried to simplify it for now to simply open the 3D Slicer.</p>

---

## Post #2 by @pieper (2024-04-16 17:53 UTC)

<p>Did you try the version in the IDC Browser extension?  I understood it is working on all platforms.</p>
<p><a href="https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/Launch3DslicerViaClickableUrlsForViewingIdcDataViaSliceridcbrowserAndIdcIndex/">https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/Launch3DslicerViaClickableUrlsForViewingIdcDataViaSliceridcbrowserAndIdcIndex/</a></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/ImagingDataCommons/SlicerIDCBrowser">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/ImagingDataCommons/SlicerIDCBrowser" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/6ed23f1b8b7b8e5b59b47c4cf8f685fc70b95551a37083a84d32eb0391e90716/ImagingDataCommons/SlicerIDCBrowser" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/ImagingDataCommons/SlicerIDCBrowser" target="_blank" rel="noopener">GitHub - ImagingDataCommons/SlicerIDCBrowser: A 3D Slicer extension to...</a></h3>

  <p>A 3D Slicer extension to support access to the content of NCI Imaging Data Commons - ImagingDataCommons/SlicerIDCBrowser</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @vkt1414 (2024-04-16 20:07 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> for the reference!</p>
<p>Hi <a class="mention" href="/u/gil">@Gil</a>,</p>
<p>Here’s how I tackled it. I needed to create a new app and that app launches slicer whenever a custom protocol is detected.</p>
<p><a href="https://github.com/vkt1414/SlicerIDCBrowser/blob/add-slicer-idc-viewer/IDCBrowser/IDCViewer.py" rel="noopener nofollow ugc">SlicerIDCBrowser/IDCBrowser/IDCViewer.py at add-slicer-idc-viewer · vkt1414/SlicerIDCBrowser (github.com)</a></p>
<p>happy to answer anything with in my reach!</p>

---

## Post #4 by @Gil (2024-04-17 06:06 UTC)

<p>Thank you so much for your help!</p>
<p>I’ll try to play around with it a bit today and see if it solves it.</p>

---
