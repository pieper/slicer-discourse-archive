---
topic_id: 7202
title: "Failing Tests Importerror No Module Named Elastix"
date: 2019-06-17
url: https://discourse.slicer.org/t/7202
---

# Failing Tests - ImportError: No module named Elastix

**Topic ID**: 7202
**Date**: 2019-06-17
**URL**: https://discourse.slicer.org/t/failing-tests-importerror-no-module-named-elastix/7202

---

## Post #1 by @jamesobutler (2019-06-17 14:27 UTC)

<p>There a couple extensions with failing tests for Slicer 4.10 related to a failure to import Elastix.</p>
<p>SequenceRegistration: <a href="http://slicer.cdash.org/testDetails.php?test=9620798&amp;build=1619449" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=9620798&amp;build=1619449</a><br>
SlicerCochlea: <a href="http://slicer.cdash.org/testDetails.php?test=9662089&amp;build=1619496" rel="nofollow noopener">http://slicer.cdash.org/testDetails.php?test=9662089&amp;build=1619496</a></p>
<pre><code class="lang-auto">test_widgetRepresentation (qSlicerSequenceRegistrationModuleGenericTest.qSlicerSequenceRegistrationModuleGenericTest) ... Traceback (most recent call last):
  File "/Volumes/Dashboards/Stable/S-4102-E-b/SequenceRegistration-build/lib/Slicer-4.10/qt-scripted-modules/SequenceRegistration.py", line 42, in setup
    self.logic = SequenceRegistrationLogic()
  File "/Volumes/Dashboards/Stable/S-4102-E-b/SequenceRegistration-build/lib/Slicer-4.10/qt-scripted-modules/SequenceRegistration.py", line 490, in __init__
    import Elastix
ImportError: No module named Elastix
ok
</code></pre>
<p>The .s4ext files on the 4.10 branch do specify SlicerElastix as a dependency. SequenceRegistration specifies SlicerElastix as a dependency <a href="https://github.com/Slicer/ExtensionsIndex/blob/4.10/SequenceRegistration.s4ext#L15" rel="nofollow noopener">here</a>. Anyone have an idea about why it is failing to import Elastix? Something specific to the build/test process on the nightly builds of extensions?</p>

---

## Post #2 by @lassoan (2019-06-17 15:37 UTC)

<p>If SlicerElastix extension is installed them <code>import Elastix</code> should not throw an error. SlicerElastix is built successfully for Slicer-4.10.x and also for recent Slicer-4.11.x releases. I only see occasional build errors on Linux (dashboard upload fails, so it is not really a build error but some issue on the factory machine).</p>
<p>If an extension uses SlicerElastix and does not list it as a dependency then maybe the expectation is that the user will install it manually? Probably it would be better to list it as a dependency.</p>

---

## Post #3 by @jamesobutler (2019-06-17 15:49 UTC)

<p>I didn’t see any import issues with the extension installed, but it appears the failing test for <code>ImportError: No module named Elastix</code> has been happening since at least 2018.</p>
<p>The extensions are both listing SlicerElastix as a dependency.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Is this some issue with the factory machine?</p>

---

## Post #4 by @jcfr (2019-06-18 07:05 UTC)

<blockquote>
<p>but it appears the failing test for <code>ImportError: No module named Elastix</code></p>
</blockquote>
<p>This should be fixed in  <a href="https://github.com/lassoan/SlicerElastix/pull/18" class="inline-onebox">ENH: Generate SlicerElastixConfig to fix find_package() call by dependent extension by jcfr · Pull Request #18 · lassoan/SlicerElastix · GitHub</a></p>
<p>After integrating this change, the following tests are still failing but this is independent of SlicerElastix:</p>
<pre><code class="lang-plaintext">$ ctest 
Test project /tmp/SlicerCochlea-build
    Start 1: py_nomainwindow_qSlicerCochleaRegModuleGenericTest
1/9 Test #1: py_nomainwindow_qSlicerCochleaRegModuleGenericTest .....   Passed   16.88 sec
    Start 2: py_CochleaReg
2/9 Test #2: py_CochleaReg ..........................................***Failed    3.77 sec
    Start 3: py_CochleaRegModuleTest
3/9 Test #3: py_CochleaRegModuleTest ................................***Failed   82.24 sec
    Start 4: py_nomainwindow_qSlicerCochleaSegModuleGenericTest
4/9 Test #4: py_nomainwindow_qSlicerCochleaSegModuleGenericTest .....   Passed    2.74 sec
    Start 5: py_CochleaSeg
5/9 Test #5: py_CochleaSeg ..........................................***Failed    3.77 sec
    Start 6: py_CochleaSegModuleTest
6/9 Test #6: py_CochleaSegModuleTest ................................***Failed   47.83 sec
    Start 7: py_nomainwindow_qSlicerVisSimCommonModuleGenericTest
7/9 Test #7: py_nomainwindow_qSlicerVisSimCommonModuleGenericTest ...   Passed    2.85 sec
    Start 8: py_VisSimCommon
8/9 Test #8: py_VisSimCommon ........................................   Passed    3.65 sec
    Start 9: py_VisSimCommonModuleTest
9/9 Test #9: py_VisSimCommonModuleTest ..............................   Passed    3.88 sec
</code></pre>
<p>I submitted the following PR to simplify the testing harness and fix the one of the failing tests, the last failing test can be fixed applying similar fixes (cc: <a class="mention" href="/u/brhoom">@brhoom</a>) . See <a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea/pull/17" class="inline-onebox">Fix CochleaReg test by jcfr · Pull Request #17 · MedicalImageAnalysisTutorials/SlicerCochlea · GitHub</a></p>
<pre><code class="lang-plaintext">$ ctest 
Test project /tmp/SlicerCochlea-build
    Start 1: py_nomainwindow_qSlicerCochleaRegModuleGenericTest
1/7 Test #1: py_nomainwindow_qSlicerCochleaRegModuleGenericTest .....   Passed    2.83 sec
    Start 2: py_CochleaReg
2/7 Test #2: py_CochleaReg ..........................................   Passed   22.38 sec
    Start 3: py_nomainwindow_qSlicerCochleaSegModuleGenericTest
3/7 Test #3: py_nomainwindow_qSlicerCochleaSegModuleGenericTest .....   Passed    2.85 sec
    Start 4: py_CochleaSeg
4/7 Test #4: py_CochleaSeg ..........................................***Failed    3.80 sec
    Start 5: py_nomainwindow_qSlicerVisSimCommonModuleGenericTest
5/7 Test #5: py_nomainwindow_qSlicerVisSimCommonModuleGenericTest ...   Passed    2.76 sec
    Start 6: py_VisSimCommon
6/7 Test #6: py_VisSimCommon ........................................   Passed    3.65 sec
    Start 7: py_VisSimCommonModuleTest
7/7 Test #7: py_VisSimCommonModuleTest ..............................   Passed    3.77 sec
</code></pre>

---

## Post #5 by @brhoom (2019-06-18 07:49 UTC)

<blockquote>
<p>This should be fixed in <a href="https://github.com/lassoan/SlicerElastix/pull/18" class="inline-onebox" rel="noopener nofollow ugc">ENH: Generate SlicerElastixConfig to fix find_package() call by dependent extension by jcfr · Pull Request #18 · lassoan/SlicerElastix · GitHub</a></p>
</blockquote>
<p>Thanks for your effort. I got this error, while I am testing your modifications now. I got this error:</p>
<pre><code>                CochleaReg.py", line 398, in testSlicerCochleaRegistration
checksums='SHA256:d7cda4e106294a59591f03e74fbe9ecffa322dd1a9010b4d0590b377acc05eb5')[0]
               TypeError: downloadFromURL() got an unexpected keyword argument 'checksums'
               Reload and Test: Exception!

              downloadFromURL() got an unexpected keyword argument 'checksums'
</code></pre>

---

## Post #6 by @brhoom (2019-06-18 08:02 UTC)

<p>Solved by changing the code to:</p>
<pre><code>  nodeNames='P100001_DV_L_a'
  nodeNames='P100001_DV_L_a'
  fileNames='P100001_DV_L_a.nrrd'
  uris='https://cloud.uni-koblenz-landau.de/s/EwQiQidXqTcGySB/download'
  checksums='SHA256:d7cda4e106294a59591f03e74fbe9ecffa322dd1a9010b4d0590b377acc05eb5'
  if fixedImgPath is None:
      fixedVolumeNode = SampleData.downloadFromURL(uris, fileNames, nodeNames, checksums )[0]</code></pre>

---

## Post #7 by @jamesobutler (2019-06-18 11:26 UTC)

<p><a class="mention" href="/u/brhoom">@brhoom</a> Did you test with a recent Slicer build? Checksum support was added to the SampleData module 6 days ago. See <a href="https://github.com/Slicer/Slicer/commit/aedb7d6702a30b485be952f2c933dfd96f072f02" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/aedb7d6702a30b485be952f2c933dfd96f072f02</a></p>

---

## Post #8 by @jcfr (2019-06-18 13:29 UTC)

<p>As indicated by <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, since the checksum has been introduced recently, make sure to use a recent Slicer version.</p>
<p>Only after all issues have been addressed in the <code>master</code> branch, I suggest you backport changes to the <code>4.10</code></p>

---

## Post #9 by @brhoom (2019-06-18 14:30 UTC)

<p>The error was in 4.11.</p>
<p>I have another issue. By using simpledata , the volume has no storage node anymore. I find a workaround be reloading the volume.</p>

---

## Post #10 by @jcfr (2019-06-18 15:01 UTC)

<blockquote>
<p>I find a workaround be reloading the volume.</p>
</blockquote>
<p>Since the downloaded data are for testing … keeping the storage node would not give the opportunity for the user to save in a location different from the tmp folder.</p>
<p>Updating the <code>CochleaReg</code> module, I noticed you were relaying on the filename associated with the storage node to restore the node name.</p>
<p>Without revisiting the approach, here what i did to make sure the storage node was available:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea/blob/28789608f9fc35deb5ccd8ab4936e7790ff54d84/CochleaReg/CochleaReg.py#L279-L282">
  <header class="source">

      <a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea/blob/28789608f9fc35deb5ccd8ab4936e7790ff54d84/CochleaReg/CochleaReg.py#L279-L282" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea/blob/28789608f9fc35deb5ccd8ab4936e7790ff54d84/CochleaReg/CochleaReg.py#L279-L282" target="_blank" rel="noopener">MedicalImageAnalysisTutorials/SlicerCochlea/blob/28789608f9fc35deb5ccd8ab4936e7790ff54d84/CochleaReg/CochleaReg.py#L279-L282</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="279" style="counter-reset: li-counter 278 ;">
          <li>if movingVolumeNode.GetStorageNode() is None:
</li>
          <li>    movingImgPath = os.path.join(self.vsc.vtVars['vissimPath'], movingVolumeNode.GetName()+".nrrd")
</li>
          <li>    slicer.util.saveNode(movingVolumeNode, movingImgPath)
</li>
          <li>movingPath = movingVolumeNode.GetStorageNode().GetFileName()
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @jcfr (2019-06-18 18:52 UTC)

<p><a class="mention" href="/u/brhoom">@brhoom</a> This commit should fix the remaining test, I will let you cherry-pick what makes sense. See <a href="https://github.com/jcfr/SlicerCochlea/commit/30e61b013582e54fe940a63f2180050420fbe1ec" rel="nofollow noopener">https://github.com/jcfr/SlicerCochlea/commit/30e61b013582e54fe940a63f2180050420fbe1ec</a></p>

---

## Post #12 by @jcfr (2019-06-18 18:55 UTC)

<p>Summary:</p>
<ul>
<li>issue preventing the Elastix module from being available in SlicerCochlea has been fixed in <a href="https://github.com/lassoan/SlicerElastix/pull/18" rel="nofollow noopener">https://github.com/lassoan/SlicerElastix/pull/18</a>
</li>
<li>redundant and unused test script have been removed from SlicerCochlea</li>
<li>failing <code>py_CochleaReg</code> test has been fixed in <a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea/pull/17" rel="nofollow noopener">https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea/pull/17</a>
</li>
<li>failing test <code>py_CochleaSeg</code> has been fixed in <a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCochlea/commit/b50284d1a1cb552a7ee38902ded33fd9e5977c6b" rel="nofollow noopener">SlicerCochlea@b50284d1</a>, with improvements suggested in <a href="https://github.com/jcfr/SlicerCochlea/commit/30e61b013582e54fe940a63f2180050420fbe1ec" rel="nofollow noopener">jcfr/SlicerCochlea@30e61b013</a>
</li>
</ul>

---
