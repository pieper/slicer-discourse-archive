---
topic_id: 48946
title: "Save failed for transforms sequence"
date: 2026-11-17
url: https://discourse.slicer.org/t/48946
last_bumped: 2026-11-18T09:39:15.120Z
---

# Save failed for transforms sequence

**Topic ID**: 48946
**Date**: 2026-11-17
**URL**: https://discourse.slicer.org/t/save-failed-for-transforms-sequence/48946

---

## Post #1 by @mhouse (2026-11-17 19:53 UTC)

<p>So far I haven’t found a related thread with the same issue.</p>
<p>After <code>Sequence Registration</code> the output transforms sequence cannot be saved, because there is no valid (grid) transform for the first (fixed) frame. Slicer version 5.13.0-2026-11-09 (revision 35466 / b5d5d9e).</p>
<p>Sometimes the <code>seq</code> in the filename extension is missing. But also with <code>seq</code> it’s the same error.</p>
<pre><code class="lang-auto">[ERROR][VTK] 17.11.2026 18:45:55 [vtkMRMLFileIOManager (0x5bf8ef1d2e00)] (vtkMRMLFileIOManager.cxx:1468) - SaveNodes error: Saving failed with all writers found for file .../3DSlicer/scenes/seg-dl/Reg/OutputTransforms.nrrd of type SequenceFile
[CRITICAL][Qt] 17.11.2026 18:45:55 
 (unknown:0) - void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save error: "- Error: First frame in the sequence needs to contain a valid grid transform.\n- Error: Cannot write data file: .../3DSlicer/scenes/seg-dl/Reg/OutputTransforms.nrrd.\n"


</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b1722850a9560299bbd1f23c25058902b242c25.png" data-download-href="/uploads/short-url/fhmEDMijONUdwdvaBeKvH8sA6ln.png?dl=1" title="Screenshot Save" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b1722850a9560299bbd1f23c25058902b242c25_2_690x226.png" alt="Screenshot Save" data-base62-sha1="fhmEDMijONUdwdvaBeKvH8sA6ln" width="690" height="226" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b1722850a9560299bbd1f23c25058902b242c25_2_690x226.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b1722850a9560299bbd1f23c25058902b242c25_2_1035x339.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b1722850a9560299bbd1f23c25058902b242c25_2_1380x452.png 2x" data-dominant-color="353435"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot Save</span><span class="informations">2048×672 299 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mhouse (2026-11-18 09:39 UTC)

<p>If the fixed frame is not the first frame then the saving works without an error. But sometimes it’s needed to have the fixed frame as the first frame.</p>

---
