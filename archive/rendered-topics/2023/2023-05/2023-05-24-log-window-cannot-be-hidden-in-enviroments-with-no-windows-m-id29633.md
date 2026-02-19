---
topic_id: 29633
title: "Log Window Cannot Be Hidden In Enviroments With No Windows M"
date: 2023-05-24
url: https://discourse.slicer.org/t/29633
---

# Log window cannot be hidden in enviroments with no windows manager

**Topic ID**: 29633
**Date**: 2023-05-24
**URL**: https://discourse.slicer.org/t/log-window-cannot-be-hidden-in-enviroments-with-no-windows-manager/29633

---

## Post #1 by @Davide_Punzo (2023-05-24 16:29 UTC)

<p>Hi all,</p>
<p>the log messages widget is a separate window respect the main one of 3DSlicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/0198d01ce766d2ec5c9cc331bbfda9b97ea7cf1b.png" data-download-href="/uploads/short-url/e7SpPj9pvL65tDODcRs9YBmhXJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0198d01ce766d2ec5c9cc331bbfda9b97ea7cf1b_2_345x201.png" alt="image" data-base62-sha1="e7SpPj9pvL65tDODcRs9YBmhXJ" width="345" height="201" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0198d01ce766d2ec5c9cc331bbfda9b97ea7cf1b_2_345x201.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0198d01ce766d2ec5c9cc331bbfda9b97ea7cf1b_2_517x301.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0198d01ce766d2ec5c9cc331bbfda9b97ea7cf1b_2_690x402.png 2x" data-dominant-color="E1E1E1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">848×495 45.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is not optimal when Slicer is in an enviroment with no windows manager (e.g. Slicer running in a docker with vnc). For example, once the “show log” button in the bottom-right corner is clicked, it is not possible to hide the application log window anymore. Also it can’t be moved etc…</p>
<p>It would be great if this can be changed in Slicer core.</p>
<p>The idea would be to make the logging window a dockable widget (and make the show button toggle) - exactly the same way as the Python console.</p>
<p>Before doing it and opening a PR, I would like to hear your feedback.</p>
<p>Davide.</p>

---

## Post #2 by @pieper (2023-05-24 17:10 UTC)

<p>Sounds reasonable to me.</p>

---

## Post #3 by @jamesobutler (2023-05-24 17:38 UTC)

<p>In general, the issue affects non-modal windows like the application log window, but not other modal windows like the Add Data Dialog?</p>

---

## Post #4 by @Davide_Punzo (2023-05-25 08:05 UTC)

<p>While the issue is present for every separate window/dialog, the most incovenient is just the application log window. Dialogs have always a “close” button inside the window (ok, load, etc…) and generally the user does not need to move the dialog window, since it is a prompt to the user for an immediate action to do.</p>

---
