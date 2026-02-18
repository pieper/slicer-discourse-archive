# Unable to find all referenced series in DICOM Browser

**Topic ID**: 43022
**Date**: 2025-05-21
**URL**: https://discourse.slicer.org/t/unable-to-find-all-referenced-series-in-dicom-browser/43022

---

## Post #1 by @DeepaKrishnaswamy (2025-05-21 15:10 UTC)

<p>Hi,</p>
<p>I am working on improving the loading of DICOM Structured Reports into Slicer using the QuantitativeReporting plugin. Some SRs could have multiple series that are referenced. However, when I choose to load the SR in the DICOM Browser, as an example, only 2 out of the 3 valid series are actually listed to be selected in the pop-up window. Additionally, sometimes they are listed as a scalar volume or as an image sequence. The series that are displayed in this pop-up window, and if they are a scalar volume or image sequence, change every time I open Slicer.</p>
<p>I know that these series could be a scalar volume or an image sequence, especially if they’re old, from <a href="https://discourse.slicer.org/t/loading-dicom-seg-imports-referenced-scalar-volume-and-first-slice-of-referenced-series/22692">this post</a>.</p>
<p>Additionally, from my understanding, as seen in the <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/DICOMBrowser.py" rel="noopener nofollow ugc">DICOMBrowser loadCheckedLoadables function</a>, I need to have a list of <code>loadable.referencedInstanceUIDs</code>. In my changes to QuantitativeReporting, I have also confirmed that the <code>loadable.referencedInstanceUIDs</code> contains all of the referenced SOPInstanceUIDs from the valid referenced series.</p>
<p>Therefore, I think that in an ideal case, the pop-up window should have the 3 series listed as scalar volumes, and then additionally listed as image sequences, for a total of 6 check boxes.</p>
<p>Am I missing something when creating the <code>loadable.referencedInstanceUIDs</code> list?</p>
<p>Thank you!</p>
<p>Deepa</p>

---

## Post #2 by @fedorov (2025-05-21 18:46 UTC)

<p>Deepa, it might be helpful if you provided a script and instructions to reproduce the problem.</p>

---

## Post #3 by @DeepaKrishnaswamy (2025-05-21 19:26 UTC)

<p>Absolutely. To reproduce, please:</p>
<ol>
<li>Clone the master branch from this fork: <a href="https://github.com/deepakri201/QuantitativeReporting" class="inline-onebox" rel="noopener nofollow ugc">GitHub - deepakri201/QuantitativeReporting: Segmentation-based measurements with DICOM import and export of the results.</a></li>
<li>Add this github repo to the additional modules paths.</li>
<li>Import DICOM files <a href="https://www.dropbox.com/scl/fi/nas9ylf6ygnop6qu6t2sd/Slicer_discourse_SR_loading_references_05_21_25.zip?rlkey=hqv9743zlnt984ilypxo2r3re&amp;st=aklbrx89&amp;dl=0" rel="noopener nofollow ugc">from here</a> into the DICOM database. This contains the SR, and 3 referenced series.</li>
<li>Select the Structured Report, and click Examine, and then click Load. The popup box with only some of the referenced series should appear.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39bbc2c4415ab99b0a7c9eb6a5862339dbf5c4c5.png" data-download-href="/uploads/short-url/8eJuthJ2AaD8qt0RgLt56Mbdr0h.png?dl=1" title="Screenshot 2025-05-21 at 3.25.32 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39bbc2c4415ab99b0a7c9eb6a5862339dbf5c4c5.png" alt="Screenshot 2025-05-21 at 3.25.32 PM" data-base62-sha1="8eJuthJ2AaD8qt0RgLt56Mbdr0h" width="499" height="350"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-05-21 at 3.25.32 PM</span><span class="informations">499×350 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2025-05-23 21:01 UTC)

<p>Hi <a class="mention" href="/u/deepakrishnaswamy">@DeepaKrishnaswamy</a> - did you try adding some prints to debug this code?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/756d101a60889c68ae299741d8c0b6726d1da8b9/Modules/Scripted/DICOMLib/DICOMBrowser.py#L698-L709">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/756d101a60889c68ae299741d8c0b6726d1da8b9/Modules/Scripted/DICOMLib/DICOMBrowser.py#L698-L709" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/756d101a60889c68ae299741d8c0b6726d1da8b9/Modules/Scripted/DICOMLib/DICOMBrowser.py#L698-L709" target="_blank" rel="noopener">Modules/Scripted/DICOMLib/DICOMBrowser.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/756d101a60889c68ae299741d8c0b6726d1da8b9/Modules/Scripted/DICOMLib/DICOMBrowser.py#L698-L709" rel="noopener"><code>756d101a6</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="698" style="counter-reset: li-counter 697 ;">
          <li>def _addLoadableCheckboxes(self):</li>
          <li>    self.checkBoxGroupBox = qt.QGroupBox(_("References"))</li>
          <li>    self.checkBoxGroupBox.setLayout(qt.QFormLayout())</li>
          <li>    for plugin in self.loadables:</li>
          <li>        for loadable in [loadable_item for loadable_item in self.loadables[plugin] if loadable_item.selected]:</li>
          <li>            checkBoxText = loadable.name + " (" + plugin.loadType + ") "</li>
          <li>            cb = qt.QCheckBox(checkBoxText, self)</li>
          <li>            cb.checked = True</li>
          <li>            cb.setSizePolicy(qt.QSizePolicy(qt.QSizePolicy.Expanding, qt.QSizePolicy.Preferred))</li>
          <li>            self.checkboxes[loadable] = cb</li>
          <li>            self.checkBoxGroupBox.layout().addWidget(cb)</li>
          <li>    self.layout().addWidget(self.checkBoxGroupBox, 1, 0, 1, 3)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @DeepaKrishnaswamy (2025-05-27 21:55 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Yes, I did try to put some print statements in DICOMBrowser.py. In the <code>loadCheckedLoadables</code> I added statements to print the 1) <code>referencedFileLists</code>, and the 2) <code>self.referencedLoadables</code> from <code>self.getLoadablesFromFileLists(referencedFileLists)</code>.</p>
<p>Here was my thought process:</p>
<ol>
<li>From the <code>referencedFileLists</code>, I first checked that it contained the three unique SeriesInstanceUIDs, which it does.</li>
<li>I then checked that the number of SOPInstanceUIDs for each of the SeriesInstanceUIDs matches what I see in Slicer, which it does. (file_counts: [19, 19, 15])</li>
<li>I then checked the <code>self.referencedLoadables</code> to make sure the right plugins were being used for each loadable. This is where I can see a potential issue. The DICOMImageSequencePlugin has a list of 1 loadables, and DICOMScalarVolumePlugin has a list of 7 loadables. Shouldn’t <code>self.referencedLoadables</code> only contain 3 loadables?</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e156a4a1164a4d47fbdd704101a0d797b906c8a4.png" data-download-href="/uploads/short-url/w9r3Tp3elS1TG9DKENi60ewecni.png?dl=1" title="Screenshot 2025-05-27 at 5.43.51 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e156a4a1164a4d47fbdd704101a0d797b906c8a4_2_689x354.png" alt="Screenshot 2025-05-27 at 5.43.51 PM" data-base62-sha1="w9r3Tp3elS1TG9DKENi60ewecni" width="689" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e156a4a1164a4d47fbdd704101a0d797b906c8a4_2_689x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e156a4a1164a4d47fbdd704101a0d797b906c8a4_2_1033x531.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e156a4a1164a4d47fbdd704101a0d797b906c8a4.png 2x" data-dominant-color="E9E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-05-27 at 5.43.51 PM</span><span class="informations">1181×607 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks!</p>

---

## Post #6 by @pieper (2025-05-27 22:08 UTC)

<p>A series can map to multiple loadables.  You can confirm this by selecting just the series and clicking Examine to see what is detected and what is checked by default.</p>
<p>I’m thinking that in the loop referenced above at line 702 some of the loadables are not selected.</p>

---

## Post #7 by @DeepaKrishnaswamy (2025-05-27 22:56 UTC)

<p>Yes you’re right, that some of the loadables are not selected. From the original list of 7 for DICOMScalarVolumePlugin, only 1 has <code>loadable.selected=True</code>.</p>

---

## Post #8 by @fedorov (2025-05-27 23:00 UTC)

<p><a class="mention" href="/u/deepakrishnaswamy">@DeepaKrishnaswamy</a>, first, I think we do not want all of the loadables to show up checked in that popup - only high confidence. Second, since this depends on your updates to QuantitativeReporting, I am not sure your updates correctly initialize the list of referenced instances - there may be duplicates, and I do not know how this is handled downstream, see comment here: <a href="https://github.com/QIICR/QuantitativeReporting/pull/287#discussion_r2107236883" class="inline-onebox">Added code to import and display points, lines and bounding boxes by deepakri201 · Pull Request #287 · QIICR/QuantitativeReporting · GitHub</a>. I think it makes sense to first make sure your implementation is correct. If you suspect Slicer has a bug, I recommend creating an example where you have a standalone script that can reproduce the issue outside that large PR above.</p>

---

## Post #9 by @DeepaKrishnaswamy (2025-07-29 18:33 UTC)

<p>As an update to this issue, I have recently submitted a PR to DICOMBrowser.py: <a href="https://github.com/Slicer/Slicer/pull/8605" class="inline-onebox" rel="noopener nofollow ugc">BUG: Show all referenced series as checkboxes in DICOM popup by deepakri201 · Pull Request #8605 · Slicer/Slicer · GitHub</a></p>

---
