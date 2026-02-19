---
topic_id: 21290
title: "Raise Only Add Files Gui"
date: 2021-12-31
url: https://discourse.slicer.org/t/21290
---

# Raise only Add Files GUI

**Topic ID**: 21290
**Date**: 2021-12-31
**URL**: https://discourse.slicer.org/t/raise-only-add-files-gui/21290

---

## Post #1 by @Srijeet_Chatterjee (2021-12-31 10:54 UTC)

<p>Hello Everyone,</p>
<p>I want to create a simple button in a scripted (python) module,such that on clicked ideally that should raise the “Add Data” widget. Ideally I want it be preselected as the file loader only i.e the “Choose File(s) to Add” option. I research, but could not find a suitable solution for the Load. Would it be possible to do this using python?</p>
<p>Currently I could use the hot key combination as a work around, but “Choose File(s) to Add” option directly was not possible with that. Could anyone please suggest a better way to get this done?</p>
<p>Thanks a lot,<br>
Best regards,<br>
Srijeet</p>

---

## Post #2 by @lassoan (2022-01-02 02:11 UTC)

<p>Can you tell a bit more about your workflow? What kind of files do your users load? How many at a time? Do they use drag-and-drop to load files? Do you want to entirely skip the “Add data” dialog (always want to load files with the default options)?</p>

---

## Post #3 by @Srijeet_Chatterjee (2022-01-02 03:51 UTC)

<p>Thank you, the workflow mainly involves replay recorded video. The users would upload .mkv (description: IGISO) format video or sequences. Ideally one/two files to replay the recorded videos. Keeping the default options and removing the “Add Data” dialog option would be great.</p>
<p>Best Regards,<br>
Srijeet</p>

---

## Post #4 by @lassoan (2022-01-02 20:29 UTC)

<p>You can use <code>openDialog</code> method to show a file selector dialog and directly load the chosen file. See examples in the <a href="https://github.com/Slicer/Slicer/blob/c57dd676fdcccacc8d40727c65e85eb118701ee7/Base/Python/slicer/util.py#L899">script repository</a>.</p>
<p>For direct loading by drag-and-drop, you can register a drag-and-drop handler that can detect this specific file format and load the file directly (without opening the Add data window). See the DICOM module as an example, which does this for DICOM files.</p>

---

## Post #6 by @Srijeet_Chatterjee (2022-01-03 14:48 UTC)

<p>Thanks a lot, the <code>openDialog</code> method to show a file selector dialog works great. It’s even better because it restricts the user to only view supported file formats. However the file format as I mentioned are .mkv and those didn’t get loaded finally even after selecting and opening them (I tried both ‘SequenceFile’ and ‘VolumeFile’ as filetype).</p>

---

## Post #7 by @lassoan (2022-01-03 15:42 UTC)

<p>The file type is “IGSIO Sequence” - see here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/IGSIO/SlicerIGSIO/blob/master/SequenceIO/qSlicerSequenceIOReader.cxx#L85">
  <header class="source">

      <a href="https://github.com/IGSIO/SlicerIGSIO/blob/master/SequenceIO/qSlicerSequenceIOReader.cxx#L85" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/IGSIO/SlicerIGSIO/blob/master/SequenceIO/qSlicerSequenceIOReader.cxx#L85" target="_blank" rel="noopener">IGSIO/SlicerIGSIO/blob/master/SequenceIO/qSlicerSequenceIOReader.cxx#L85</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="75" style="counter-reset: li-counter 74 ;">
          <li>
          </li>
<li>//-----------------------------------------------------------------------------</li>
          <li>QString qSlicerSequenceIOReader::description() const</li>
          <li>{</li>
          <li>  return "IGSIO Sequence";</li>
          <li>}</li>
          <li>
          </li>
<li>//-----------------------------------------------------------------------------</li>
          <li>qSlicerIO::IOFileType qSlicerSequenceIOReader::fileType() const</li>
          <li>{</li>
          <li class="selected">  return "IGSIO Sequence";</li>
          <li>}</li>
          <li>
          </li>
<li>//-----------------------------------------------------------------------------</li>
          <li>QStringList qSlicerSequenceIOReader::extensions() const</li>
          <li>{</li>
          <li>  QStringList supportedExtensions = QStringList();</li>
          <li>#ifdef IGSIO_SEQUENCEIO_ENABLE_MKV</li>
          <li>  supportedExtensions &lt;&lt; "IGSIO sequence Matroska (*.mkv)";</li>
          <li>  supportedExtensions &lt;&lt; "IGSIO sequence WebM (*.webm)";</li>
          <li>#endif</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @Srijeet_Chatterjee (2022-01-03 23:06 UTC)

<p>That’s great, thank you so much! Now it works perfectly</p>

---
