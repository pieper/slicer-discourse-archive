# Sample Data Load Complete, Still Won't Appear

**Topic ID**: 12392
**Date**: 2020-07-06
**URL**: https://discourse.slicer.org/t/sample-data-load-complete-still-wont-appear/12392

---

## Post #1 by @vertebra (2020-07-06 12:36 UTC)

<p>My sample data will download but it will not appear on the slices. I have restarted my slicer and laptop, still doesn’t work. Any tips?</p>

---

## Post #2 by @cpinter (2020-07-06 12:54 UTC)

<p>It is possible that the downloaded file is invalid. Can you try to delete the files in <code>c:\Users\[YourUser]\AppData\Local\Temp\Slicer\RemoteIO</code> and try again?</p>

---

## Post #3 by @vertebrae (2020-07-06 13:31 UTC)

<p>Hello Mr. Pinter,</p>
<p>I deleted the file and it still did not work. Any other ways to solve this issue? I tried to use this code to import the data but it gave an error. This is a part of my final code so do you know how to fix this?</p>
<p>import SampleData<br>
sampleDataLogic = SampleData.SampleDataLogic()<br>
masterVolumeNode = sampleDataLogic.downloadCTACardio()</p>

---

## Post #4 by @vertebra (2020-07-06 13:42 UTC)

<p>Try and delete the files in <code>c:\Users\[YourUser]\AppData\Local\Temp\Slicer\RemoteIO</code> and then run it again? It worked for me</p>

---

## Post #5 by @vertebrae (2020-07-06 14:10 UTC)

<p>Thank you! Does anybody else have any other ideas as to how to solve this problem?</p>

---

## Post #6 by @lassoan (2020-07-06 14:28 UTC)

<p>Please copy here the error messages from the application log.</p>

---

## Post #7 by @vertebrae (2020-07-06 14:34 UTC)

<pre><code class="lang-auto">&lt;b&gt;Requesting download&lt;/b&gt; &lt;i&gt;CTA-cardio.nrrd&lt;/i&gt; from http://slicer.kitware.com/midas3/download/item/292309/CTA-cardio.nrrd...
&lt;i&gt;Downloaded 6.1 MB (10% of 61.1 MB)...&lt;/i&gt;
&lt;i&gt;Downloaded 12.2 MB (20% of 61.1 MB)...&lt;/i&gt;
&lt;i&gt;Downloaded 18.3 MB (30% of 61.1 MB)...&lt;/i&gt;
&lt;i&gt;Downloaded 24.4 MB (40% of 61.1 MB)...&lt;/i&gt;
&lt;i&gt;Downloaded 30.5 MB (50% of 61.1 MB)...&lt;/i&gt;
&lt;i&gt;Downloaded 36.6 MB (60% of 61.1 MB)...&lt;/i&gt;
&lt;i&gt;Downloaded 42.8 MB (70% of 61.1 MB)...&lt;/i&gt;
&lt;i&gt;Downloaded 48.9 MB (80% of 61.1 MB)...&lt;/i&gt;
&lt;i&gt;Downloaded 55.0 MB (90% of 61.1 MB)...&lt;/i&gt;
&lt;i&gt;Downloaded 61.1 MB (100% of 61.1 MB)...&lt;/i&gt;
&lt;b&gt;Download finished&lt;/b&gt;
&lt;b&gt;Requesting load&lt;/b&gt; &lt;i&gt;CTACardio&lt;/i&gt; from C:/Users/nandanlocal/AppData/Local/Temp/Slicer/RemoteIO/CTA-cardio.nrrd...
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:/Program Files/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/SampleData.py", line 596, in downloadCTACardio
    return self.downloadSample('CTACardio')
  File "C:/Program Files/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/SampleData.py", line 574, in downloadSample
    return self.downloadSamples(sampleName)[0]
  File "C:/Program Files/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/SampleData.py", line 582, in downloadSamples
    nodes = self.downloadFromSource(source)
  File "C:/Program Files/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/SampleData.py", line 514, in downloadFromSource
    loadedNode = self.loadNode(filePath, nodeName, loadFileType, source.loadFileProperties)
  File "C:/Program Files/Slicer 4.10.2/bin/../lib/Slicer-4.10/qt-scripted-modules/SampleData.py", line 678, in loadNode
    success = slicer.app.coreIOManager().loadNodes(fileType, fileProperties, loadedNodes)
ValueError: Could not find matching overload for given arguments:
('VolumeFile', {'name': 'CTACardio', 'fileName': 'C:/Users/nandanlocal/AppData/Local/Temp/Slicer/RemoteIO/CTA-cardio.nrrd'}, (vtkCommonCorePython.vtkCollection)00000151368AA9A8)
 The following slots are available:
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, QVariantMap parameters, vtkCollection loadedNodes) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, QVariantMap parameters) -&gt; bool
</code></pre>

---

## Post #8 by @lassoan (2020-07-06 14:34 UTC)

<p>Please try with latest Slicer Preview Release.</p>

---

## Post #10 by @vertebrae (2020-07-06 14:44 UTC)

<p>Hello Andras,</p>
<p>I just did that and it works now! Thank you very much!</p>

---
