---
topic_id: 35964
title: "Is it possible to scroll by dragging the mouse in the current view?"
date: 2024-05-07
url: https://discourse.slicer.org/t/35964
last_bumped: 2026-07-13T11:10:13.279Z
---

# Is it possible to scroll by dragging the mouse in the current view?

**Topic ID**: 35964
**Date**: 2024-05-07
**URL**: https://discourse.slicer.org/t/is-it-possible-to-scroll-by-dragging-the-mouse-in-the-current-view/35964

---

## Post #1 by @ndelgado (2024-05-07 13:37 UTC)

<p>Hello,</p>
<p>I was wondering if there is a way to use a keyboard shortcut and drag the mouse to scroll through the slices in the current selected view. I know that it is possible to use the shift key and then drag mouse to scroll through the corresponding view, but is it also possible to do it in the selected view for ease of performing annotation?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2024-05-07 13:43 UTC)

<p>Do you have. scroll wheel on your mouse?  That’s what we usually use.</p>

---

## Post #3 by @ndelgado (2024-05-07 16:53 UTC)

<p>Thank you! We do use the scroll wheel on our mouse. Our team was just wondering for when we need to move through a lot of slices quickly if there is a method to do so in the current view for 3D slicer.</p>

---

## Post #4 by @pieper (2024-05-07 16:55 UTC)

<p>Would something like a control-shift-mouse-move work for your use case?</p>

---

## Post #5 by @alex_bone (2024-09-19 07:40 UTC)

<p>Dear 3D Slicer team,</p>
<p>Thank you for your amazing work.</p>
<p>I would also be interested in such a feature for very fast slice scrolling controlled by mouse dragging in the current view, for instance with control-shift-mouse-move as proposed by pieper.<br>
In other words, it would be a shortcut replacing the use of the “slider” button usually available at the top of the window.</p>
<p>In typical PACS viewers, radiologists can simply hold a “click left” anywhere in the image and then move the mouse up and down to very quickly scroll across all slices.<br>
In 3D slicer, the left click is already reserved to other actions, and I do not suggest changing that. But this is where this “fast scroll by mouse dragging” feature request is coming from.</p>
<p>Thank you again, best,<br>
Alex</p>

---

## Post #6 by @strider_hunter (2025-08-26 08:54 UTC)

<p>Hi,<br>
Was this functionality implemented? For Ctrl + Mouse-Move = slices scrolled.<br>
Maybe something to add in the “<strong>vtkMRMLCameraWidget.cxx</strong>“ file?</p>

---

## Post #7 by @Y_A (2026-07-11 23:28 UTC)

<p>Hi radiologist here, just wondering if there are any updates on this feature request? It would be really helpful to have a drag and scroll tool like hospital-based PACS systems</p>

---

## Post #8 by @lassoan (2026-07-13 11:10 UTC)

<p>We have a draft implementation for this and discussing some more details here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9284">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9284" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9284" target="_blank" rel="noopener">ENH: Add Scroll mouse mode to browse slices by click-and-drag (#9284)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:add-scroll-mouse-mode</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-07-13" data-time="01:27:59" data-timezone="UTC">01:27AM - 13 Jul 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="2 commits changed 13 files with 180 additions and 54 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9284/files" target="_blank" rel="noopener">
            <span class="added">+180</span>
            <span class="removed">-54</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Add a new "Scroll" mouse interaction mode alongside the existing
Translate/rota<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9284" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">te view, Adjust window/level, and Place modes.

This is consistent with other radiology viewers (Weasis, OsiriX, etc.)
and an older IHE supplement that many viewers adopted
(https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_Suppl_BIR_Rev1.3_TI_2016_09-09.pdf),
and users requested (https://discourse.slicer.org/t/is-it-possible-to-scroll-by-dragging-the-mouse-in-the-current-view/35964/4).

A few additional modes (zoom, pan, crosshair) may be considered,
which can be useful when using single-button mouse or touchscreen.

When this new mode is active, click-and-drag vertically in a slice view scrolls through
slices, with the full view height mapped to the full slice offset slider range.

Implementation:
New mode is added to vtkMRMLInteractionNode.
vtkMRMLSliceIntersectionWidget implements the view interaction.
Added new icon (stack with blue up/down arrow) to the toolbar and shortcut to view context menu.

&lt;img width="614" height="511" alt="image" src="https://github.com/user-attachments/assets/99fb0041-bced-4778-9aed-80660a2770ad" /&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Your inputs would be very welcome.</p>

---
