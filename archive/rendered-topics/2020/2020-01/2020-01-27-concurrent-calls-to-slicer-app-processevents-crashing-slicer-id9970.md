---
topic_id: 9970
title: "Concurrent Calls To Slicer App Processevents Crashing Slicer"
date: 2020-01-27
url: https://discourse.slicer.org/t/9970
---

# Concurrent calls to slicer app processEvents() crashing slicer

**Topic ID**: 9970
**Date**: 2020-01-27
**URL**: https://discourse.slicer.org/t/concurrent-calls-to-slicer-app-processevents-crashing-slicer/9970

---

## Post #1 by @fbordignon (2020-01-27 15:49 UTC)

<p>Slicer is randomly crashing if I register a callback to the dicom indexer and make my callback call slicer.app.processEvents()</p>
<pre><code>self.indexer = ctk.ctkDICOMIndexer()
self.indexer.connect("progress(int)", updateProgress)
self.indexer.addDirectory( db, inputDir )
</code></pre>
<p>The callback calls processEvents:</p>
<pre><code>def updateProgress():
    ...
    slicer.app.processEvents()
</code></pre>
<p>I suspect that the callback is being called concurrently and crashing slicer by calling processEvents concurrently. If I use a mutex for preventing the call to processEvents by more than one thread, it works.</p>

---

## Post #2 by @pieper (2020-01-27 19:36 UTC)

<p>Makes sense - <code>slicer.app.processEvents()</code> should be used very carefully and only when absolutely needed.</p>

---

## Post #3 by @lassoan (2020-01-27 19:53 UTC)

<p>If you call processEvents() inside an event handler, you may get into infinite recursion (and there might be other issues), so don’t do it.</p>
<p>Since ctkDICOMIndexer can run in non-blocking mode (set <code>indexer.backgroundImportEnabled=True</code>), it is not necessary to call <code>slicer.app.processEvents()</code> at all. If the main thread is not blocked then all events are processed automatically. You can use the application while the import in the background is running; or show a popup window to block the user from wandering away.</p>
<p>You may also use the DICOM module’s indexer, which shows the progress in the DICOM browser and does not block the application at all (as it is done in this <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/RSNAVisTutorial.py#L196-L200">test/example</a>).</p>

---
