---
topic_id: 972
title: "Exporting Dicom Programatically"
date: 2017-08-30
url: https://discourse.slicer.org/t/972
---

# Exporting Dicom programatically

**Topic ID**: 972
**Date**: 2017-08-30
**URL**: https://discourse.slicer.org/t/exporting-dicom-programatically/972

---

## Post #1 by @mmtg (2017-08-30 21:53 UTC)

<p>Hello everyone,</p>
<p>This is a question I asked a while ago and it was resolved. However, that was with a much older version and my script no longer works with the newer versions of slicer that have a different subjecthierarchy organization.</p>
<p>I decided to try and remake it for newer versions. However I am having issues understanding how it works, especially since I am not a strong programmer and very unfamiliar with how the SubjectHierarchy works on the backend.</p>
<p>I started off looking here:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L516" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L516" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L516</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="506" style="counter-reset: li-counter 505 ;">
<li>    if units is not None:</li>
<li>      volumeNode.SetVoxelValueUnits(units)</li>
<li>
</li>
<li>def loadWithMultipleLoaders(self,loadable):</li>
<li>  """Load using multiple paths (for testing)</li>
<li>  """</li>
<li>  volumeNode = self.loadFilesWithArchetype(loadable.files, loadable.name+"-archetype")</li>
<li>  self.setVolumeNodeProperties(volumeNode, loadable)</li>
<li>  volumeNode = self.loadFilesWithSeriesReader("GDCM", loadable.files, loadable.name+"-gdcm")</li>
<li>  self.setVolumeNodeProperties(volumeNode, loadable)</li>
<li class="selected">  volumeNode = self.loadFilesWithSeriesReader("DCMTK", loadable.files, loadable.name+"-dcmtk")</li>
<li>  self.setVolumeNodeProperties(volumeNode, loadable)</li>
<li>
</li>
<li>  return volumeNode</li>
<li>
</li>
<li>def load(self,loadable,readerApproach=None):</li>
<li>  """Load the select as a scalar volume using desired approach</li>
<li>  """</li>
<li>  # first, determine which reader approach the user prefers</li>
<li>  if not readerApproach:</li>
<li>    readerIndex = slicer.util.settingsValue('DICOM/ScalarVolume/ReaderApproach', 0, converter=int)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>specifically the line:<br>
volumeNode = shNode.GetItemDataNode(exportable.subjectHierarchyItemID)</p>
<p>So the volumeNode it gets is the same as if I were to do</p>
<p>volumeNode = getNode(‘<em>Some_name</em>’)</p>
<p>what I don’t understand is how to get the item ID’s quickly. The first step is</p>
<p>shn = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)</p>
<p>and when I look at that I see that there are ID’s. But I don’t see/ know how to get the ID for a volume node. From what I can tell, it seems that all the methods associated with shn need you to know the itemID ahead of time. I am assuming there is some other method to get the ID for a volumeNode but I don’t know where to look.</p>
<p>I am sure it’s right in front of me but spent some time and couldn’t see where. I appreciate any help</p>

---

## Post #2 by @lassoan (2017-08-30 22:06 UTC)

<p>The method you are looking for is <a href="http://apidocs.slicer.org/master/classvtkMRMLSubjectHierarchyNode.html#a05a31b3a075a4bc08abf3997bcc8f562">GetItemByDataNode</a>.</p>
<p>Subject hierarchy usage examples:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy</a></li>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/SubjectHierarchyGenericSelfTest.py">https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/SubjectHierarchyGenericSelfTest.py</a></li>
</ul>
<p>In general, use the <a href="http://apidocs.slicer.org/master/">API documentation</a> and examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a> and in <a href="https://github.com/Slicer/Slicer/tree/master/">Slicer core self-tests and Python scripted modules</a>.</p>

---
