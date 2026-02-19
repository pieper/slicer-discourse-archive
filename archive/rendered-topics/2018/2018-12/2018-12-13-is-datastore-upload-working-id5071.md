---
topic_id: 5071
title: "Is Datastore Upload Working"
date: 2018-12-13
url: https://discourse.slicer.org/t/5071
---

# Is dataStore upload working?

**Topic ID**: 5071
**Date**: 2018-12-13
**URL**: https://discourse.slicer.org/t/is-datastore-upload-working/5071

---

## Post #1 by @muratmaga (2018-12-13 17:54 UTC)

<p>I am trying to upload a scene to DataStore. It has a two volumes (one grayscale, one labelmap) and a markups list. I created an account, logged in, described the contents etc. Now the upload is hung, doesn’t seem to progress et all. When saved to disk, MRB file itself is only 11MB. Is that a connection issue (I am behind a proxy)?</p>

---

## Post #2 by @lassoan (2018-12-13 23:20 UTC)

<p>Are you trying to use the upload feature in Slicer or just the Midas web interface in a web browser?</p>
<p>Midas is being replaced by Girder and maybe some features have been disabled already.</p>

---

## Post #3 by @muratmaga (2018-12-14 01:12 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
No, I am using the built-in upload option. See the screenshot.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35df43cb13fca42f8ca154fa5f79f6fb4b21d433.png" data-download-href="/uploads/short-url/7GzEddkWBsjoqeJJLxZYMhTdjoL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35df43cb13fca42f8ca154fa5f79f6fb4b21d433_2_690x377.png" alt="image" data-base62-sha1="7GzEddkWBsjoqeJJLxZYMhTdjoL" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35df43cb13fca42f8ca154fa5f79f6fb4b21d433_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35df43cb13fca42f8ca154fa5f79f6fb4b21d433_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35df43cb13fca42f8ca154fa5f79f6fb4b21d433_2_1380x754.png 2x" data-dominant-color="E0E0E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1511×826 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2018-12-14 03:07 UTC)

<p>You can try uploading scenes by using the web interface in a browser. What data would you like to upload and for what audience and purpose?</p>
<p>When the DataStore module was developed it was hard to find reliable and easily affordable hosting service for research data. However, there are lots of possibilities now (GitHub, Zenodo, low-cost unlimited hosting services, etc.), so DataStore may be reduced to a data index that can point to data stored at various places - similarly how the Extension Manager or Sample Data module work.</p>
<p>You can probably find good free hosting service and you can add links and images to SampleData (as it is done for example in <a href="https://github.com/SlicerRt/Sequences/tree/master/SequenceSampleData" rel="nofollow noopener">SequenceSampleData module</a> in Sequences extension).</p>

---

## Post #5 by @muratmaga (2018-12-14 03:46 UTC)

<p>I don’t need hosting, just a to convenient way to pull existing data into Slicer. This looks it is going to work a like champ. Thanks Andras.</p>

---

## Post #6 by @muratmaga (2018-12-14 05:23 UTC)

<p>Actually one more question: I modified the example script with my url. Data downloads correctly, but fails to get loaded into Slicer. I can open the cached version manually, it is not corrupted or anything. All I changed are these lines:</p>
<blockquote>
<p>sampleName=‘Mouse Head microCT Atlas’,<br>
uris=‘<a href="https://github.com/muratmaga/mouse_CT_atlas/blob/3da1c36c057537384376155f347d08b34817fa5c/data/templates/35_mic_23strain_mus_template_UCHAR.nii.gz?raw=true">https://github.com/muratmaga/mouse_CT_atlas/blob/3da1c36c057537384376155f347d08b34817fa5c/data/templates/35_mic_23strain_mus_template_UCHAR.nii.gz?raw=true</a>’,<br>
fileNames=‘35_mic_23strain_mus_template_UCHAR.nii.gz’,<br>
nodeNames=‘Mus’,</p>
</blockquote>
<p>&lt;b&gt;Requesting download&lt;/b&gt; &lt;i&gt;35_mic_23strain_mus_template_UCHAR.nii.gz&lt;/i&gt; from <a href="https://github.com/muratmaga/mouse_CT_atlas/blob/3da1c36c057537384376155f347d08b34817fa5c/data/templates/35_mic_23strain_mus_template_UCHAR.nii.gz?raw=true">https://github.com/muratmaga/mouse_CT_atlas/blob/3da1c36c057537384376155f347d08b34817fa5c/data/templates/35_mic_23strain_mus_template_UCHAR.nii.gz?raw=true</a>…</p>
<p>&lt;i&gt;Downloaded 960.0 KB (10% of 9.3 MB)…&lt;/i&gt;</p>
<p>&lt;i&gt;Downloaded 1.9 MB (20% of 9.3 MB)…&lt;/i&gt;</p>
<p>&lt;i&gt;Downloaded 2.8 MB (30% of 9.3 MB)…&lt;/i&gt;</p>
<p>&lt;i&gt;Downloaded 3.7 MB (40% of 9.3 MB)…&lt;/i&gt;</p>
<p>&lt;i&gt;Downloaded 4.7 MB (50% of 9.3 MB)…&lt;/i&gt;</p>
<p>&lt;i&gt;Downloaded 5.6 MB (60% of 9.3 MB)…&lt;/i&gt;</p>
<p>&lt;i&gt;Downloaded 6.5 MB (70% of 9.3 MB)…&lt;/i&gt;</p>
<p>&lt;i&gt;Downloaded 7.5 MB (80% of 9.3 MB)…&lt;/i&gt;</p>
<p>&lt;i&gt;Downloaded 8.4 MB (90% of 9.3 MB)…&lt;/i&gt;</p>
<p>&lt;i&gt;Downloaded 9.3 MB (100% of 9.3 MB)…&lt;/i&gt;</p>
<p>&lt;b&gt;Download finished&lt;/b&gt;</p>
<p>&lt;b&gt;Requesting load&lt;/b&gt; &lt;i&gt;35micron_Mouse_Atlas&lt;/i&gt; from C:/Users/Murat/AppData/Local/Temp/Slicer/RemoteIO/35_mic_23strain_mus_template_UCHAR.nii.gz…</p>
<p>&lt;font color="red"&gt;&lt;b&gt; Load failed!&lt;/b&gt;&lt;/font&gt;</p>

---

## Post #7 by @pieper (2018-12-14 18:54 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> here’s a working sample for that data.</p>
<pre><code class="lang-auto">import SampleData

dataSource = SampleData.SampleDataSource(
  sampleName= 'Mouse Head microCT Atlas', 
  uris= 'https://github.com/muratmaga/mouse_CT_atlas/blob/3da1c36c057537384376155f347d08b34817fa5c/data/templates/35_mic_23strain_mus_template_UCHAR.nii.gz?raw=true',
  fileNames= '35_mic_23strain_mus_template_UCHAR.nii.gz', 
  nodeNames= 'Mus'
  )

SampleData.SampleDataLogic().downloadFromSource(dataSource)


</code></pre>

---

## Post #8 by @muratmaga (2018-12-14 19:03 UTC)

<p>Thanks Steve, it works if I copy/paste to the python console.</p>
<p>But I actually want to add a new Category to the SampleData module as the Sequences module have done. I have been trying to modify the following to make it work with this particular data (as well as few other different kinds).</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/Sequences/blob/master/SequenceSampleData/SequenceSampleData.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/Sequences/blob/master/SequenceSampleData/SequenceSampleData.py" target="_blank" rel="nofollow noopener">SlicerRt/Sequences/blob/master/SequenceSampleData/SequenceSampleData.py</a></h4>
<pre><code class="lang-py">import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# SequenceSampleData
#

class SequenceSampleData(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Sequence Sample Data"
    self.parent.categories = ["Sequences"]
    self.parent.dependencies = ["SampleData"]
</code></pre>

  This file has been truncated. <a href="https://github.com/SlicerRt/Sequences/blob/master/SequenceSampleData/SequenceSampleData.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2018-12-14 19:21 UTC)

<p>This works for me:</p>
<pre><code class="lang-auto">    SampleData.SampleDataLogic.registerCustomSampleDataSource(
      sampleName='Mouse Head microCT Atlas',
      uris='https://github.com/muratmaga/mouse_CT_atlas/blob/3da1c36c057537384376155f347d08b34817fa5c/data/templates/35_mic_23strain_mus_template_UCHAR.nii.gz?raw=true',
      fileNames='35_mic_23strain_mus_template_UCHAR.nii.gz',
      nodeNames='Mus',
      )
</code></pre>

---

## Post #10 by @smrolfe (2018-12-14 19:47 UTC)

<p>This works for me too, thanks <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---

## Post #11 by @muratmaga (2018-12-14 20:11 UTC)

<p>Works for me too  as it is.<br>
So,  loadFileType=‘Volume Sequence’ tag is not necessary, then?</p>

---

## Post #12 by @lassoan (2018-12-14 20:13 UTC)

<p>You need to define “Volume Sequence” if you want the data set to be loaded as a volume sequence (4D volume).</p>

---

## Post #13 by @muratmaga (2018-12-14 20:17 UTC)

<p>Is there some documentation for the tags that I have to use and what they can be set as ? I am trying with a mrb scene now, and I had the same issue as before, ie., downloads but doesn’t load into Slicer.</p>

---

## Post #14 by @lassoan (2018-12-14 20:30 UTC)

<p>You can use standard Python <code>help</code> method to get documentation of any method or class.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import SampleData
&gt;&gt;&gt; help(SampleData.SampleDataLogic.registerCustomSampleDataSource)

Help on function registerCustomSampleDataSource in module SampleData:

registerCustomSampleDataSource(category='Custom', sampleName=None, uris=None, fileNames=None, nodeNames=None, customDownloader=None, thumbnailFileName=None, loadFileType='VolumeFile', loadFileProperties={})
    Adds custom data sets to SampleData.
    :param category: Section title of data set in SampleData module GUI.
    :param sampleName: Displayed name of data set in SampleData module GUI.
    :param thumbnailFileName: Displayed thumbnail of data set in SampleData module GUI,
    :param uris: Download URL(s).
    :param fileNames: File name(s) that will be loaded.
    :param nodeNames: Node name in the scene.
    :param customDownloader: Custom function for downloading.
    :param loadFileType: file format name ('VolumeFile' by default).
    :param loadFileProperties: custom properties passed to the IO plugin.
</code></pre>
<p>File reader plugin name (loadFileType) is defined in each reader plugin. New plugins can be specified in any module in any extension, so there is no “list”. You can find most of them mentioned in <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py</a> - search for <code>filetype</code>.</p>

---

## Post #15 by @muratmaga (2018-12-14 20:44 UTC)

<p>Thanks Andras. This is very useful.</p>

---

## Post #16 by @smrolfe (2018-12-19 23:21 UTC)

<p>The issue with loading an MRB file when registering a custom data source is documented <a href="https://issues.slicer.org/view.php?id=4668" rel="nofollow noopener">here</a> and fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27666" rel="nofollow noopener">r27666</a>. Thanks for your advice <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---
