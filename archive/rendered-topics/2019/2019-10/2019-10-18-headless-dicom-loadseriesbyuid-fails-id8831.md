---
topic_id: 8831
title: "Headless Dicom Loadseriesbyuid Fails"
date: 2019-10-18
url: https://discourse.slicer.org/t/8831
---

# Headless DICOM, loadSeriesByUID fails

**Topic ID**: 8831
**Date**: 2019-10-18
**URL**: https://discourse.slicer.org/t/headless-dicom-loadseriesbyuid-fails/8831

---

## Post #1 by @unnmdnwb3 (2019-10-18 14:02 UTC)

<p>Hi everyone,</p>
<p>I’m trying to load DICOM files to scene (within a headless CI-pipeline) by using <code>DICOMUtils.loadSeriesByUID</code>, as linked  <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py#L120" rel="noopener nofollow ugc">here</a>.</p>
<p>However, <strong>trying to load the scene fails</strong>,  although <strong>no error is thrown</strong>.</p>
<p>Importing the files to the db works, using <code>DICOMUtils.importDicom</code>, as linked <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py#L302" rel="noopener nofollow ugc">here</a>.</p>
<pre><code class="lang-auto">&gt; New patient inserted: 1
&gt; New patient inserted as :  1
&gt; Need to insert new study:  "1.2.826.0.1.3680043.2.146.2.20.3103689.1600244093.0"
&gt; Study Added
&gt; Need to insert new series:  "1.3.12.2.1107.5.6.1.2013.31330116120712460953700001577"
&gt; Series Added
&gt; "DICOM indexer has successfully processed 130 files [0.95s]"
</code></pre>
<p>The series can also be retrieved:</p>
<pre><code class="lang-auto">slicer.dicomDatabase.seriesForStudy(studyList[0])
&gt; ('1.3.12.2.1107.5.6.1.2013.31330116120712460953700001577',)
</code></pre>
<p>To load the series, I use:</p>
<pre><code class="lang-auto">seriesInstanceUID = '1.3.12.2.1107.5.6.1.2013.31330116120712460953700001577'
ok = utils.loadSeriesByUID([seriesInstanceUID])
</code></pre>
<p>The loading does not throw an error, but shows this warning:</p>
<pre><code class="lang-auto">&gt; Warning in DICOM plugin Scalar Volume when examining loadable &lt;SeriesName&gt;: Images are not equally spaced (a difference of 3 vs 3 in spacings was detected).  If loaded image appears distorted, enable 'Acquisition geometry regularization' in Application settings / DICOM / DICOMScalarVolumePlugin. Please use caution.
</code></pre>
<p>The function returns <code>True</code>, although this seems to be the case even if you import a seriesUID with an invalid UID:</p>
<pre><code class="lang-auto">utils.loadSeriesByUID(['1.3.12.2.1107.5.6.1.2013.31330116120712460953700001577'])
&gt; True

utils.loadSeriesByUID(['an invalid seriesUID'])
&gt; True
</code></pre>
<p>Either way, after the loading, there are <strong>no child items</strong> attached to the scene:</p>
<pre><code class="lang-auto">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
sceneID = shNode.GetSceneItemID()
items = vtk.vtkIdList()
shNode.GetItemChildren(sceneID, items)
items.GetNumberOfIds()
&gt; 0
</code></pre>
<p>Is this behaviour linked with the newest <a href="https://discourse.slicer.org/t/new-dicom-browser-is-ready/8819">announcements</a> of decoupling the widget from the logic?<br>
Does anyone have a clue why my approach does not work?</p>
<p>Thanks in advance for any feedback! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @pieper (2019-10-18 14:27 UTC)

<p>Interesting - this sounds like something that should work.  So if you run the same command in the python console with the gui it does load?</p>

---

## Post #3 by @unnmdnwb3 (2019-10-18 14:42 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Yes exactly, this code works perfectly on my local machine (with GUI), but somehow fails in the pipeline.<br>
Btw. the pipeline uses <code>nightly-master:b54b2ea</code>  (<a href="https://github.com/Slicer/Slicer/commit/12a221105b1810a5fc6aaf82679c85afb424e8d2" rel="nofollow noopener">link</a>).</p>
<p>Do you think  this could be the issue?</p>

---

## Post #4 by @lassoan (2019-10-18 15:00 UTC)

<p>With the DICOM browser rework, GUI classes are no more needed for indexing and loading DICOM files, so it should be easier to do DICOM operations on a headless node (you should not need to set up X server, etc). However, not all possible use cases are checked by automated testing so maybe there are some regressions.</p>
<p>Do you run the same script exactly the same way?<br>
Do you launch Slicer using --no-main-window?<br>
Could you provide a minimal example of a complete script that reproduces the issue?</p>

---

## Post #5 by @unnmdnwb3 (2019-10-21 06:40 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<ol>
<li>Yes, the locally run code is also used for our pipeline - and is therefore exactly the same.</li>
<li>We don’t specifically run Slicer, we use <code>ctest</code> to run the tests for our extension within our <code>gitlab-ci</code>.</li>
<li>Sure, the example code below is used for loading the scene:</li>
</ol>
<pre><code class="lang-python">1.  import DICOMLib.DICOMUtils as utils
2.
3.  databaseFilePath = 'path/to/slicer/database'
4.  slicer.dicomDatabase.openDatabase(databaseFilePath)
5.  if not slicer.dicomDatabase.isOpen:
6.     self.logger.error('Unable to connect to database')
7.        
8.  seriesInstanceUID = '1.3.12.2.1107.5.6.1.2013.31330116120712460953700001577'
9.  ok = utils.loadSeriesByUID([seriesInstanceUID])
10. if not ok:
11.    self.logger.error('Could not load files from database.')
12.
13. shNode = vtkmrmlutils.getSubjectHierarchyNode()
14. studyID = vtkmrmlutils.getStudyIDs()[0]
15. itemID = vtkmrmlutils.getAllFolderChildren(studyID)[0]
16. 
17. return itemID
</code></pre>
<p>Previous to this function, files already have been successfully written to the database.</p>
<p>The error-logs for testing the database connection and the loading are both not written. As already mentioned, only the following warning is shown:</p>
<pre><code class="lang-auto">Warning in DICOM plugin Scalar Volume when examining loadable 3: CT LU177  3.0  I31s STD: Images are not equally spaced (a difference of 3 vs 3 in spacings was detected).  If loaded image appears distorted, enable 'Acquisition geometry regularization' in Application settings / DICOM / DICOMScalarVolumePlugin. Please use caution.
</code></pre>
<p>But there is an <strong>error thrown at line 14</strong>:</p>
<pre><code class="lang-auto">subjectID = vtkmrmlutils.getSubjectIDs()[0]
&gt; IndexError: list index out of range
</code></pre>
<p>As an info, our <code>vtkmrmlutils</code> basically wraps all functionality dealing with <code>vtkmrml</code> elements. <code>vtkmrmlutils.getStudyIDs()</code> returns all nodes with <code>Level:Study</code> for the first subject found as a child element of the scene.</p>
<pre><code class="lang-auto">shNode = vtkmrmlutils.getSubjectHierarchyNode()
sceneID = shNode.GetSceneItemID()
try:
    subjectID = vtkmrmlutils.getSubjectIDs()[0]
except:
    raise
</code></pre>
<p>When trying to find any subjects after loading (<em>with no apparent error thrown by <strong>DICOMUtils</strong></em>), there is no subject to be found in the scene. This means, the files are not correctly loaded, otherwise we would find <code>1 Subject -&gt; 1 Study -&gt; 1 Series</code>:</p>
<p>Does this help?</p>

---

## Post #6 by @lassoan (2019-10-22 12:49 UTC)

<p>How do you determine <code>databaseFilePath</code>? When you launch Slicer in testing mode the database is set to a temporary location (see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L121-L125" rel="nofollow noopener">here</a>).</p>
<p>The database is attempted to be opened on application startup (see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L69" rel="nofollow noopener">here</a>). Maybe the database is switched to the temporary one after you open yours? You can print the database folder and  filesForSeries from the database after your failed attempts to retrieve subject hierarchy items.</p>
<p>But all these are really just guessing. The best would be if you could give complete example of your test and CMake file that runs it.</p>

---

## Post #7 by @unnmdnwb3 (2019-10-22 13:02 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thanks for your input! We didn’t change anything, but updated the version of <code>nightly-master</code> that we use to commit <a href="https://github.com/Slicer/Slicer/commit/80338611790baf572bca02c4e3f90d4aeb3f92de" rel="nofollow noopener">b485c8b</a> and this fixed the issue that we had!</p>

---
