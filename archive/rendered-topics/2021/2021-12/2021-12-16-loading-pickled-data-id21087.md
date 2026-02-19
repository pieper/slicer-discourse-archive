---
topic_id: 21087
title: "Loading Pickled Data"
date: 2021-12-16
url: https://discourse.slicer.org/t/21087
---

# Loading pickled data

**Topic ID**: 21087
**Date**: 2021-12-16
**URL**: https://discourse.slicer.org/t/loading-pickled-data/21087

---

## Post #1 by @koeglfryderyk (2021-12-16 10:21 UTC)

<p>I want to load pickled data from the GUI in my custom extension.</p>
<p>When using the ‘Add data’ dialog to try to load such data, Slicer throws an error (Error - load failed).</p>
<p>As a workaround, I thought I could use the ‘Add data’ dialog to get the path to the required file and then load it in my scripted module.</p>
<p>However, I could not find out how to access this path. I only managed to open the dialog with <code>slicer.util.openAddVolumeDialog()</code>.</p>
<p>How can I access this path?</p>

---

## Post #2 by @lassoan (2021-12-16 17:32 UTC)

<p>You can add a custom reader for any file format using a short Python script. See example here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/8381ef3e6d73afc9f15ac0db5ddb7de753c90641/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/8381ef3e6d73afc9f15ac0db5ddb7de753c90641/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/8381ef3e6d73afc9f15ac0db5ddb7de753c90641/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py" target="_blank" rel="noopener">Slicer/Slicer/blob/8381ef3e6d73afc9f15ac0db5ddb7de753c90641/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py</a></h4>


    <pre><code class="lang-py">import logging
import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *

class SlicerScriptedFileReaderWriterTest(ScriptedLoadableModule):
  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    parent.title = 'SlicerScriptedFileReaderWriterTest'
    parent.categories = ['Testing.TestCases']
    parent.dependencies = []
    parent.contributors = ["Andras Lasso (PerkLab, Queen's)"]
    parent.helpText = '''
    This module is used to test qSlicerScriptedFileReader and qSlicerScriptedFileWriter classes.
    '''
    parent.acknowledgementText = '''
    This file was originally developed by Andras Lasso, PerkLab.
    '''
    self.parent = parent
</code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/8381ef3e6d73afc9f15ac0db5ddb7de753c90641/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>That said, pickling is intended for temporary storage, not for archival or sharing. So, loading pickled data via “Add data” does not sound like a good idea. Using any of the standard file formats, and maybe using a simple human-readable container file format, such as json for custom metadata would be more appropriate.</p>
<p>Can you tell a bit more about your use case? What generates the pickled data? What kind of data you pickle? Have you considered using a standard file format instead (nrrd for images, ply for meshes, etc)?</p>

---

## Post #3 by @koeglfryderyk (2021-12-17 15:38 UTC)

<p>Thank you!</p>
<p>Just a follow-up regarding the custom reader - do I add this class to the same file where all my custom extension code is?</p>
<p>A colleague of mine creates landmarks in US and MR images in his custom software, and from there he saves the landmarks. The landmarks are stored in a numpy array which he then pickles.</p>
<p>I understand that pickles are not created for such a use case, but I’m not sure I’ll be able to change his mind to adapt his workflow.</p>

---

## Post #4 by @lassoan (2021-12-17 16:02 UTC)

<p>Saving the data in json should be almost as simple as pickling and would have many advantages (I don’t even want to get started on that). You could even use Slicer’s <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-json-file-format-mrk-json">markup json file format</a> and then you would not need an importer at all, you could just drag-and-drop the files into Slicer to load them and could directly save them from Slicer.</p>
<aside class="quote no-group" data-username="koeglfryderyk" data-post="3" data-topic="21087">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>do I add this class to the same file where all my custom extension code is?</p>
</blockquote>
</aside>
<p>Yes, you put the <code>MyModuleFileReader</code> and <code>MyModuleFileWriter</code> classes into any scripted module in your extension and Slicer automatically discovers them when the module is loaded. <code>MyModule</code> is the name of the main module class.</p>

---
