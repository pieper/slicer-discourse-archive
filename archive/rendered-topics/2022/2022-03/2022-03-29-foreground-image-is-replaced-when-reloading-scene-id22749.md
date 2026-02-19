---
topic_id: 22749
title: "Foreground Image Is Replaced When Reloading Scene"
date: 2022-03-29
url: https://discourse.slicer.org/t/22749
---

# Foreground image is replaced when reloading scene

**Topic ID**: 22749
**Date**: 2022-03-29
**URL**: https://discourse.slicer.org/t/foreground-image-is-replaced-when-reloading-scene/22749

---

## Post #1 by @rphellan2210 (2022-03-29 14:11 UTC)

<p>I displayed MRHead_1 (foreground) and MRHead (background) on the red view of Slicer. Then, I saved the scene and reloaded it, and MRHead_1 was switched to MRHead. See image attached. Could this be a bug on Slicer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5595219a2a7213950d9c82a2fff08d24a75b3095.jpeg" data-download-href="/uploads/short-url/cd661M70SFEpPj8iIfXKaz6KvoV.jpeg?dl=1" title="BugOnReload" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5595219a2a7213950d9c82a2fff08d24a75b3095_2_690x312.jpeg" alt="BugOnReload" data-base62-sha1="cd661M70SFEpPj8iIfXKaz6KvoV" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5595219a2a7213950d9c82a2fff08d24a75b3095_2_690x312.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5595219a2a7213950d9c82a2fff08d24a75b3095_2_1035x468.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5595219a2a7213950d9c82a2fff08d24a75b3095_2_1380x624.jpeg 2x" data-dominant-color="84896D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BugOnReload</span><span class="informations">1814×821 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2022-03-29 14:29 UTC)

<p>I just tested the very same thing using the latest preview version and for me it works well.</p>
<ul>
<li>What Slicer version do you use?</li>
<li>What is the layout in the saved scene?</li>
<li>Are the slice views linked?</li>
</ul>

---

## Post #3 by @rphellan2210 (2022-03-29 14:43 UTC)

<p>I used Slicer 4.13.0-2022-03-26 for Windows. The layout is “Red slice only”. The views are not linked. I clicked on “Create a Medical Record Bundle containing the scene” before saving it.</p>
<p>I checked with the latest version and I got the same problem.</p>

---

## Post #4 by @cpinter (2022-03-29 14:47 UTC)

<p>Using these settings I could reproduce the issue you reported with the latest version.</p>
<p>Can you please check if the layout or the linked slices is the setting that matters in this case?</p>

---

## Post #5 by @rphellan2210 (2022-03-29 15:06 UTC)

<p>I selected different layouts, with linked and unlinked slice views, but the problem still appears.</p>
<p>I just noticed this warning on Slicer, while saving the scene: class QList&lt;class qSlicerFileWriter *&gt; __cdecl qSlicerCoreIOManagerPrivate::writers(const class QString &amp;,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLScene *) const warning: Unable to find node with ID “” in the given scene.</p>

---

## Post #6 by @cpinter (2022-03-29 15:13 UTC)

<p>Strange because as I said when saving the scene with Four-Up layout and linked slices it loaded OK for me…</p>
<p>The error seems unrelated since it is definitely not because of a missing file as the error may suggest (that writing a file failed).</p>

---

## Post #7 by @rphellan2210 (2022-03-29 15:33 UTC)

<p>If I click the link views button before doing any changes and then set the volumes and their opacity, the scene is reloaded correctly after saving. This happens independently of the type of layout.</p>
<p>If I turn link views off, and then modify the opacity of one of the views, the scene is reloaded with the wrong settings.</p>
<p>It seems as if, in general, I need to activate the linked views before saving to keep the right settings.</p>

---

## Post #8 by @cpinter (2022-03-29 17:58 UTC)

<p>This is useful. Can you please add an Issue on <a href="https://github.com/Slicer/Slicer/issues" class="inline-onebox">Issues · Slicer/Slicer · GitHub</a> including these findings?</p>

---
