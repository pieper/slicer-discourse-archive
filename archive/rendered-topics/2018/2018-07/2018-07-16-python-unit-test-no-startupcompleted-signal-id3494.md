---
topic_id: 3494
title: "Python Unit Test No Startupcompleted Signal"
date: 2018-07-16
url: https://discourse.slicer.org/t/3494
---

# Python unit test: no startupCompleted signal

**Topic ID**: 3494
**Date**: 2018-07-16
**URL**: https://discourse.slicer.org/t/python-unit-test-no-startupcompleted-signal/3494

---

## Post #1 by @Nicole_Aucoin (2018-07-16 14:58 UTC)

<p>I’m updating my python extension from Slicer 4.6 to the master and already fixed it to only use the DICOM database after slicer.app has sent the startupCompleted signal (Modules/Scripted/DICOM/DICOM.py initializes slicer.dicomDatabase after it gets this signal). But my python unit tests that check the DICOM functionality are all failing because that signal is not being sent/caught and the slicer.dicomDatabase isn’t initialized before my test starts running. My extension module also doesn’t finish set up before the test starts running.</p>
<p>I tried setting up my test to wait for the signal, but it’s not getting it either. I looked through the Slicer application tests and didn’t find a test that accesses slicer.dicomDatabase in a similar way. The DICOMReaders.py is a ScriptedLoadableModule rather than a unitTest.TestCase and does throw up some errors when I run it locally but still reports as passing (the Preview dashboard for the windows nightly package only says “no leaks”).</p>
<pre><code>618: Could not load  "C:/Users/Nicole Aucoin/AppData/Local/Temp/Slicer-tmp/tempDICOMDatabase/dicom/1.3.6.1.4.1.9590.100.1.2.217975813113576534408907137883645586330/1.3.6.1.4.1.9590.100.1.2.366426457713813178933224342280246227461/1.3.6.1.4.1.9590.100.1.2.311244454913801066106129755371102910260"
618: DCMTK says:  No such file or directory
618: Mouse-MR-example-where-GDCM_fails Test caused exception!
618: std::logic_error: Calling methods on uninitialized ctkDICOMItem
</code></pre>
<p>The tests that are derived just from unittest.TestCase (like RSNAVisTutorialTest) create their own temporary DICOM database rather than using the default slicer.dicomDatabase.</p>
<p>Has anyone else encountered and fixed this problem yet?</p>
<p>Nicole</p>

---

## Post #2 by @Nicole_Aucoin (2018-07-16 15:48 UTC)

<p>Working with it some more, it looks like slicer.dicomDatabase was set up but any signal was sent after I connected to it during the test in either my module or my unit test.</p>

---

## Post #3 by @lassoan (2018-07-17 04:36 UTC)

<p>Do you mean that the database is initialized, but too late (because your module is notified about startupCompleted earlier than the database is initialized)?</p>
<p>Maybe instead of processing startupCompleted events in random order, we should add a method to the module interface similar to qSlicerAbstractCoreModule::initialize, which would be called in the same order as initialize (respecting module dependencies), after application startup is completed.</p>

---

## Post #4 by @pieper (2018-07-17 11:37 UTC)

<p>Yes, providing a way to define module dependencies for startupCompleted tasks makes sense.</p>

---

## Post #5 by @lassoan (2018-07-18 01:30 UTC)

<p>I’ve added <a href="https://issues.slicer.org/view.php?id=4582">https://issues.slicer.org/view.php?id=4582</a> issue to track this.</p>

---

## Post #6 by @Nicole_Aucoin (2018-07-18 13:53 UTC)

<p>Apologies, I wrote that incorrectly. When I run my test, the database is initialized but neither my module nor my test script get notified via the startup complete signal. The startup complete signal is either not sent due to the way the test is starting Slicer, or it’s sent before my module or my test script connect to listen for the signal.<br>
If I modify my module to check if slicer.dicomDatabase is set right before I need it, on regular start up, it’s set and I’ve received the startup complete signal, but when I run the test, the database is set but I’ve not received the start up completed signal. But if I try to use the database at that point, I’m getting the warnings about an uninitialized ctkDICOMItem.</p>
<p>My module definitely needs to do it’s start up completed tasks after the DICOM module has finished processing on start up complete, but it’s still odd that I’m not getting the start up completed signal at all when I run my test.</p>
<p>Nicole</p>

---

## Post #7 by @pieper (2018-07-18 15:56 UTC)

<p><a class="mention" href="/u/nicole_aucoin">@Nicole_Aucoin</a> would it be possible for you to write a small example test/module to replicate the issue?</p>

---

## Post #8 by @Nicole_Aucoin (2018-07-19 16:18 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Here you go:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/nicoleaucoin/DICOMStartupExample">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/nicoleaucoin/DICOMStartupExample" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/1eb52a86b23ee60b9884992864f90093146994a7c0ff5e2c921b323d916978ed/nicoleaucoin/DICOMStartupExample" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/nicoleaucoin/DICOMStartupExample" target="_blank" rel="noopener nofollow ugc">GitHub - nicoleaucoin/DICOMStartupExample: An example Slicer module testing...</a></h3>

  <p>An example Slicer module testing the start up complete signal and DICOM database initialization. - GitHub - nicoleaucoin/DICOMStartupExample: An example Slicer module testing the start up complete ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Notes:<br>
When I run slicer and go to my example module:<br>
The connected slot that I set up on my scripted loadable module in <strong>init</strong> is triggered (and slicer.dicomDatabase is set), but not the one that I set up in the widget representation setup.</p>
<p>When I run the test:</p>
<pre><code>ctest -C Release -R CheckDB -VV
</code></pre>
<p>The slot on my module is triggered, but slicer.dicomDatabase is None at that point. The slots on my widget and on my test that are connected to the start up signal are not triggered. At the start of my test function, slicer.dicomDatabase is still None.</p>
<p>Nicole</p>

---

## Post #9 by @pieper (2018-07-20 13:50 UTC)

<p>As a workaround, you could try adding this call to your test function:</p>
<pre><code class="lang-auto">slicer.modules.DICOMInstance.performPostModuleDiscoveryTasks()
</code></pre>

---
