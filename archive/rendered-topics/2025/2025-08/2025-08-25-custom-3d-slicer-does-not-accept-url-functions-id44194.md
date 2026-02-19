---
topic_id: 44194
title: "Custom 3D Slicer Does Not Accept Url Functions"
date: 2025-08-25
url: https://discourse.slicer.org/t/44194
---

# Custom 3D Slicer does not accept url functions

**Topic ID**: 44194
**Date**: 2025-08-25
**URL**: https://discourse.slicer.org/t/custom-3d-slicer-does-not-accept-url-functions/44194

---

## Post #1 by @nicofutur8 (2025-08-25 08:44 UTC)

<p>Hello everyone!</p>
<p>I’m testing a custom build of Slicer but, when I got into URLs functions (because I want to open slicer via browser with “slicer://”) it doesn’t seem to recognize them and nothing happens at all.</p>
<p>Could you help me figure out whats happening? I don’t know if i need to activate a flag or something in building phase.</p>
<p>Thanks in advance, Nico.</p>

---

## Post #2 by @lassoan (2025-08-25 18:45 UTC)

<p>The <code>slicer://</code> URL handler has to be registered at the operating system. The Windows installer registers it, but if you haven’t installed your custom application or you work on macOS or Linux then you need to register the URL handler yourself.</p>
<p>The IDC browser already registers custom URL handler for Slicer, so you can take the code from there:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/vkt1414/SlicerIDCBrowser/blob/add-slicer-idc-viewer/IDCBrowser/IDCViewer.py">
  <header class="source">

      <a href="https://github.com/vkt1414/SlicerIDCBrowser/blob/add-slicer-idc-viewer/IDCBrowser/IDCViewer.py" target="_blank" rel="noopener">github.com/vkt1414/SlicerIDCBrowser</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/vkt1414/SlicerIDCBrowser/blob/add-slicer-idc-viewer/IDCBrowser/IDCViewer.py" target="_blank" rel="noopener">IDCBrowser/IDCViewer.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/vkt1414/SlicerIDCBrowser/blob/add-slicer-idc-viewer/IDCBrowser/IDCViewer.py" rel="noopener"><code>add-slicer-idc-viewer</code></a>
</div>


      <pre><code class="lang-py">import json
import logging
import os
import platform
import unittest
from urllib.request import urlopen

import ctk
import pkg_resources
import qt
import slicer
import vtk
from packaging import version
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

# Register slicer url
def register_linux_slicer_url_protocol():
    if platform.system() == "Linux":
        # Check if the protocol is already registered
</code></pre>



  This file has been truncated. <a href="https://github.com/vkt1414/SlicerIDCBrowser/blob/add-slicer-idc-viewer/IDCBrowser/IDCViewer.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @nicofutur8 (2025-08-26 10:47 UTC)

<p>Hello Lasso! Thanks for the fast response.</p>
<p>I’ve already modified my windows register to open my custom App instead of the original one, and it opens when i called “slicer://” in a browser, but the problem is the url is not recognized and slicer does nothing but open itself.</p>
<p>I’m running my tests in Windows fyi.</p>

---

## Post #4 by @lassoan (2025-08-26 19:58 UTC)

<p>That’s good, then you just have to make sure that there is a module that recognizes the received URL. See for example how it is done in the DICOM module:</p>
<p>Make the DICOM module notified when the application receives a URL:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/Modules/Scripted/DICOM/DICOM.py#L54">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/Modules/Scripted/DICOM/DICOM.py#L54" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/Modules/Scripted/DICOM/DICOM.py#L54" target="_blank" rel="noopener">Modules/Scripted/DICOM/DICOM.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/Modules/Scripted/DICOM/DICOM.py#L54" rel="noopener"><code>284df9431</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="44" style="counter-reset: li-counter 43 ;">
          <li>    self.currentViewArrangement = 0</li>
          <li>    # This variable is set to true if we temporarily</li>
          <li>    # hide the data probe (and so we need to restore its visibility).</li>
          <li>    self.dataProbeHasBeenTemporarilyHidden = False</li>
          <li></li>
          <li>    self.postModuleDiscoveryTasksPerformed = False</li>
          <li></li>
          <li>def setup(self):</li>
          <li>    # Tasks to execute after the application has started up</li>
          <li>    slicer.app.connect("startupCompleted()", self.performPostModuleDiscoveryTasks)</li>
          <li class="selected">    slicer.app.connect("urlReceived(QString)", self.onURLReceived)</li>
          <li></li>
          <li>    pluginHandlerSingleton = slicer.qSlicerSubjectHierarchyPluginHandler.instance()</li>
          <li>    pluginHandlerSingleton.registerPlugin(slicer.qSlicerSubjectHierarchyDICOMPlugin())</li>
          <li></li>
          <li>    self.viewFactory = slicer.qSlicerSingletonViewFactory()</li>
          <li>    self.viewFactory.setTagName("dicombrowser")</li>
          <li>    if slicer.app.layoutManager() is not None:</li>
          <li>        slicer.app.layoutManager().registerViewFactory(self.viewFactory)</li>
          <li></li>
          <li>def performPostModuleDiscoveryTasks(self):</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The DICOM module recognizes URLs that start with <code>slicer://viewer/</code> and processes it by downloading from DICOMweb:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/Modules/Scripted/DICOM/DICOM.py#L111-L171">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/Modules/Scripted/DICOM/DICOM.py#L111-L171" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/Modules/Scripted/DICOM/DICOM.py#L111-L171" target="_blank" rel="noopener">Modules/Scripted/DICOM/DICOM.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/Modules/Scripted/DICOM/DICOM.py#L111-L171" rel="noopener"><code>284df9431</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="111" style="counter-reset: li-counter 110 ;">
          <li>def onURLReceived(self, urlString):</li>
          <li>    """Process DICOM view requests.</li>
          <li></li>
          <li>    Required query path: viewer/</li>
          <li>    Query parameters:</li>
          <li>      - studyUID: study instance UID (required)</li>
          <li>      - dicomweb_endpoint: DICOMweb server address (required)</li>
          <li>      - access_token: token for accessing the server (optional)</li>
          <li>      - bulk_retrieve: set to 0 for slower retrieve but better compatibility</li>
          <li>        with simple servers (optional, valid values are 0 and 1, default 1)</li>
          <li></li>
          <li>    Example 1 (server supports bulk retrieve):</li>
          <li></li>
          <li>    slicer://viewer/?studyUID=2.16.840.1.113669.632.20.121711.10000158860</li>
          <li>      &amp;access_token=k0zR6WAPpNbVguQ8gGUHp6</li>
          <li>      &amp;dicomweb_endpoint=http%3A%2F%2Fdemo.kheops.online%2Fapi</li>
          <li>      &amp;dicomweb_uri_endpoint=%20http%3A%2F%2Fdemo.kheops.online%2Fapi%2Fwado</li>
          <li></li>
          <li>    Example 2 (server does not support bulk retrieve):</li>
          <li></li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/284df9431ec0dd02db225494de9067898a6a43a4/Modules/Scripted/DICOM/DICOM.py#L111-L171" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>In your module, you can add the connection the same way and your module can process URLs that it recognizes.</p>

---

## Post #5 by @nicofutur8 (2025-11-14 10:03 UTC)

<p>Hello Lasso! Sorry for being late, but I have been resolving errors in my custom version which couldn’t let me build it at all.</p>
<p>I could build it yesterday for the first time in months, I also changed Windows registry from official 3DSlicer to my personal build. Now, when I try to open it with URL protocol, It shows me this sort of error:</p>
<p>”Ignore argument received via command-line (not a valid URL or existing local file):  “slicer://?action=visualize&amp;study_id=54&amp;token=27|CnCXjoEiRqWMa6J7SUZMKCNF4sEgDNXB6hAQCGQI018cd76f” “</p>
<p>I have run out of ideas so, could you give me a helping hand in this tricky situation?<br>
That would be awesome, thanks in advance.<br>
Nicolás</p>

---

## Post #6 by @lassoan (2025-11-14 20:28 UTC)

<p>According to the error message, the url syntax is invalid. Maybe you can fix the url by setting a valid path (have something between the <code>//</code> and the <code>?</code>) or maybe there are some extra quotes, etc.</p>

---
