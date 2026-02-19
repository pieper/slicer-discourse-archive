---
topic_id: 19026
title: "Stable Public Pacs Test Server"
date: 2021-08-02
url: https://discourse.slicer.org/t/19026
---

# Stable public PACS test server?

**Topic ID**: 19026
**Date**: 2021-08-02
**URL**: https://discourse.slicer.org/t/stable-public-pacs-test-server/19026

---

## Post #1 by @rbumm (2021-08-02 13:14 UTC)

<p>Can anyone recommend a stable public PACS test server with a permanent CT or MRI (for reading)  included?<br>
Thank you.</p>

---

## Post #2 by @pieper (2021-08-02 14:33 UTC)

<p>Unfortunately there aren’t any that I know of.  The problem is that it costs computer, network, and administration resources to maintain a stable server and nobody has committed to that.  Even the dicom standards committee and radiology societies haven’t stepped up to offer a stable testing implementation, which is a shame because it makes it hard to test dicom software.</p>
<p>The default one in the dicom module, <a href="http://dicomserver.co.uk">dicomserver.co.uk</a>, which I see you were using too has been up for many years now and has been a valuable contribution to the community but I think it’s a “best efforts” policy and the server and the contents are not assured to be stable.</p>
<p>I’ve been trying to convince Amazon and/or Google to host something a public archive with a wide range of valid (and invalid) dicom data and dicom networking protocols (dimse and web) but there’s nothing yet that I know of.</p>

---

## Post #3 by @pieper (2021-08-02 14:37 UTC)

<p>I should add that for our testing our <a href="https://github.com/dcmjs-org/dicomweb-client/blob/master/test/test.js">javascript dicom networking client</a> we <a href="https://github.com/dcmjs-org/dicomweb-client/blob/master/test.sh">set up dcm4chee running in docker</a> which is workable for continuous integration scenarios but probably not good for slicer testing.</p>

---

## Post #4 by @lassoan (2021-08-02 15:21 UTC)

<p>For testing, you can also use <a href="https://support.dcmtk.org/docs/dcmqrscp.html">DCMTK’s Query/Retrieve Service Class Provider</a>. See <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/JRC2013Vis.py">JRC2013Vis.py</a> as an example of using this server in an automated test.</p>
<p>Of course an enterprise-level server has many essential features that simpler DICOM servers typically don’t implement. DICOM actually does not even specify essential features, such as how to delete data sets or rename a patient, or provide solutions for fine-grained access access control. These are defined in higher-level protocols, such as <a href="https://www.hl7.org/fhir/">HL7/FHIR</a>. See for example the <a href="https://dcm4che.atlassian.net/wiki/spaces/ee2/pages/2555933/Services+MBeans">list of services provided by dcm4che</a>.</p>
<p>If you want to set up DICOM server on public internet for hosting non-public data then I would recommend to let a professional service provider (a hospital or a reliable cloud computing company) to manage it. It is not just about technical ability to set up and operating the server, but taking full responsibility for it. Large companies employ many experts in setting up and managing secure information systems, and they still buy liability insurance to cover the costs incurred by inevitable hacks and information leaks.</p>

---

## Post #5 by @rbumm (2021-08-02 15:38 UTC)

<p>Thank you, Steve and  Andras - the question was just related to have a default when a user presses “Load public PACS access data”  in the (possibly upcoming) PACS Connector extension. A default setting, which reliably works on the first try on a normal internet connection with a permanently available public CT dataset, which I could provide resp which we already have.</p>

---

## Post #6 by @rbumm (2021-08-02 15:46 UTC)

<p>Maybe we should set up one for  testing purposes, read only</p>

---

## Post #7 by @pieper (2021-08-02 19:02 UTC)

<p>Yes, that could be useful for test data.  For testing real pacs integration there are a lot of dimse-level messages we’d ideally want to test (storing to the pacs, storage commit confirmation, etc).  Realistically we’ve found that researchers don’t have access and shouldn’t be messing with the pacs anyway in most cases so it’s not been the highest priority for Slicer’s use cases.</p>
<p>In terms of reference data for testing here are some more notes:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/dicomzoo">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/dicomzoo" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/fc46e3f5482bcb5dc88c244de97656f77703f0fad98fc4921c78fce9384a0e56/pieper/dicomzoo" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/dicomzoo" target="_blank" rel="noopener">GitHub - pieper/dicomzoo: DICOM data for testing and tutorials</a></h3>

  <p>DICOM data for testing and tutorials. Contribute to pieper/dicomzoo development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also here are some more notes about using the dcmtk tools for testing:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/master/Applications/Testing/Cpp/ctkDICOMApplicationTest1.cpp#L30-L58">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/master/Applications/Testing/Cpp/ctkDICOMApplicationTest1.cpp#L30-L58" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Applications/Testing/Cpp/ctkDICOMApplicationTest1.cpp#L30-L58" target="_blank" rel="noopener">commontk/CTK/blob/master/Applications/Testing/Cpp/ctkDICOMApplicationTest1.cpp#L30-L58</a></h4>



  <pre class="onebox">    <code class="lang-cpp">
      <ol class="start lines" start="30" style="counter-reset: li-counter 29 ;">
          <li>//</li>
          <li>//  This test performs a full dicom store, query, and retrieve.</li>
          <li>//</li>
          <li>//  To recreate the parts, from the CTK-superbuild directory, run:</li>
          <li>//</li>
          <li>//</li>
          <li>//  ./CMakeExternals/Install/bin/dcmqrscp -c ./CTK-build/Testing/Temporary/dcmqrscp.cfg -d -v</li>
          <li>//</li>
          <li>//  ./CMakeExternals/Install/bin/storescu -aec CTK_AE -aet CTK_AE localhost 11112 ./CMakeExternals/Source/CTKData/Data/DICOM/MRHEAD/*.IMA</li>
          <li>//</li>
          <li>//  ./CMakeExternals/Install/bin/findscu -aet CTK_AE -aec COMMONTK -P -k 0010,0010=\* localhost 11112 patqry.dcm</li>
          <li>//</li>
          <li>//  ./CTK-build/bin/ctkDICOMQuery /tmp/test.db CTK_AE CTK_AE localhost 11112</li>
          <li>//</li>
          <li>//</li>
          <li>//  ./CTK-build/bin/ctkDICOMRetrieve 1.2.840.113619.2.135.3596.6358736.5118.1115807980.182  /tmp/hoot CTK_AE 11113 CTK_AE localhost 11112 CTK_CLIENT_AE</li>
          <li>//</li>
          <li>//  As invoked by ctest:</li>
          <li>//</li>
          <li>//  % ./CTK-build/bin/CTKApplicationCppTests ctkDICOMApplicationTest1 \</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/master/Applications/Testing/Cpp/ctkDICOMApplicationTest1.cpp#L30-L58" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
