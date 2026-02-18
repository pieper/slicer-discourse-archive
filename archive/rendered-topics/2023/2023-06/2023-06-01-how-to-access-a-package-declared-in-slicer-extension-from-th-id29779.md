# How to access a package declared in Slicer extension from the python console?

**Topic ID**: 29779
**Date**: 2023-06-01
**URL**: https://discourse.slicer.org/t/how-to-access-a-package-declared-in-slicer-extension-from-the-python-console/29779

---

## Post #1 by @fedorov (2023-06-01 17:53 UTC)

<p>I have a python package declared within the extension, and I can import it directly when accessing from the extension code. How can I import that extension in the Slicer python console?</p>
<p>I’ve done this before, I know it is possible, but I cannot find it in the hierarchies of <code>slicer.modules.*</code> etc.</p>

---

## Post #2 by @rbumm (2023-06-01 19:25 UTC)

<p>Do you mean something like this?</p>
<pre><code class="lang-auto">self.showStatusMessage(' Importing lungmask AI ...')
try:
    import lungmask
except ModuleNotFoundError:
    self.showStatusMessage(' Installing lungmask AI ...')
    lungmaskPackage = "https://github.com/JoHof/lungmask/archive/master.zip"
    slicer.util.pip_install(lungmaskPackage)
    import lungmask

</code></pre>

---

## Post #3 by @fedorov (2023-06-01 20:05 UTC)

<p>With the help of <a class="mention" href="/u/deepakrishnaswamy">@DeepaKrishnaswamy</a> I figured this out.</p>
<p>To be more specific, I wanted to import this package:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/QIICR/TCIABrowser/blob/master/TCIABrowser/TCIABrowserLib/TCIAClient.py">
  <header class="source">

      <a href="https://github.com/QIICR/TCIABrowser/blob/master/TCIABrowser/TCIABrowserLib/TCIAClient.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/TCIABrowser/blob/master/TCIABrowser/TCIABrowserLib/TCIAClient.py" target="_blank" rel="noopener">QIICR/TCIABrowser/blob/master/TCIABrowser/TCIABrowserLib/TCIAClient.py</a></h4>


      <pre><code class="lang-py">import json, string
import urllib.request, urllib.parse, urllib.error
import urllib.parse
#import TCIABrowserLib

#
# Refer https://wiki.cancerimagingarchive.net/display/Public/REST+API+Usage+Guide for complete list of API
#
class TCIAClient:
    GET_IMAGE = "getImage"
    GET_MANUFACTURER_VALUES = "getManufacturerValues"
    GET_MODALITY_VALUES = "getModalityValues"
    GET_COLLECTION_VALUES = "getCollectionValues"
    GET_BODY_PART_VALUES = "getBodyPartValues"
    GET_PATIENT_STUDY = "getPatientStudy"
    GET_SERIES = "getSeries"
    GET_SERIES_SIZE = "getSeriesSize"
    GET_PATIENT = "getPatient"

    # use Slicer API key by default
</code></pre>



  This file has been truncated. <a href="https://github.com/QIICR/TCIABrowser/blob/master/TCIABrowser/TCIABrowserLib/TCIAClient.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Which is part of this extension:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/QIICR/TCIABrowser">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/QIICR/TCIABrowser" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/c2d7b78628db4c88e182e96b16da15255da24b082393b3837b1e843455c5d909/QIICR/TCIABrowser" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/QIICR/TCIABrowser" target="_blank" rel="noopener">GitHub - QIICR/TCIABrowser: 3D Slicer module for browsing and downloading...</a></h3>

  <p>3D Slicer module for browsing and downloading medical imaging collections from The Cancer Imaging Archive (TCIA). - GitHub - QIICR/TCIABrowser: 3D Slicer module for browsing and downloading medical...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Which is very simple once you know how to do it. I hope I will remember it for the next time!</p>
<pre><code class="lang-python">from TCIABrowser import TCIAClient
</code></pre>

---
