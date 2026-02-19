---
topic_id: 21868
title: "Access Dicom Metadata Dialog"
date: 2022-02-09
url: https://discourse.slicer.org/t/21868
---

# Access Dicom metadata dialog

**Topic ID**: 21868
**Date**: 2022-02-09
**URL**: https://discourse.slicer.org/t/access-dicom-metadata-dialog/21868

---

## Post #1 by @Shahnawaz_Vora (2022-02-09 12:12 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 4.13</p>
<p>I am looking to access DICOM tag(metadata) display dialog by using button.<br>
Currently we are the same operation by right click on database.<br>
How can I access ctkBrowserWidget function and achieve this using Python.<br>
I got one script on slicer script repository<br>
dicomBrowser = slicer.modules.DICOMWidget.browserWidget.dicomBrowser<br>
But doesn’t helped me much</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a800d95543546e166d3f2f58bbe2db0a5d45b81.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a800d95543546e166d3f2f58bbe2db0a5d45b81.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a800d95543546e166d3f2f58bbe2db0a5d45b81.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @Dwij_Mistry (2022-02-09 16:36 UTC)

<p>I tried the following code in python interactor</p>
<pre><code class="lang-auto">slicer.modules.DICOMWidget.browserWidget.dicomBrowser.children()
</code></pre>
<p>it is having all components but not having access of Metadata<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fddad2dcc90f16996ffdad619c1b3e068cc63203.png" data-download-href="/uploads/short-url/AdHCUuniU4bzvCz15Lkic2oKt35.png?dl=1" title="Screenshot (89)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fddad2dcc90f16996ffdad619c1b3e068cc63203_2_690x388.png" alt="Screenshot (89)" data-base62-sha1="AdHCUuniU4bzvCz15Lkic2oKt35" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fddad2dcc90f16996ffdad619c1b3e068cc63203_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fddad2dcc90f16996ffdad619c1b3e068cc63203_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fddad2dcc90f16996ffdad619c1b3e068cc63203_2_1380x776.png 2x" data-dominant-color="32302F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (89)</span><span class="informations">1920×1080 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Does we are having any other way to access DICOM metadata popup?</p>

---

## Post #3 by @lassoan (2022-02-10 19:35 UTC)

<p>Using Qt introspection (accessing widgets using <code>children()</code>) is the very last resort if all else fail. Instead, public API of classes should be used.</p>
<pre><code class="lang-python"># Get the currently selected series ID
seriesInstanceUIDs = dicomBrowser.dicomTableManager().seriesTable().currentSelection
seriesInstanceUID = seriesInstanceUIDs[0]  # just use the first series in this example
# Get the DICOM file paths for this series
files = slicer.dicomDatabase.filesForSeries(seriesInstanceUID)
# Show metadata viewer
metadataViewer = ctk.ctkDICOMObjectListWidget()
metadataViewer.setFileList(files)
metadataViewer.show()
</code></pre>

---

## Post #4 by @Dwij_Mistry (2022-02-11 05:12 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for the valuable replay.<br>
It worked flawlessly.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="21868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Using Qt introspection (accessing widgets using <code>children()</code> ) is the very last resort if all else fail. Instead, public API of classes should be used.</p>
</blockquote>
</aside>
<p>Sure, first I will look for  public API then other things.</p>

---
