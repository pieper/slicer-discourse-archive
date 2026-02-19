---
topic_id: 8660
title: "Synchronizing Zoom Factor Between Views"
date: 2019-10-03
url: https://discourse.slicer.org/t/8660
---

# Synchronizing zoom factor between views

**Topic ID**: 8660
**Date**: 2019-10-03
**URL**: https://discourse.slicer.org/t/synchronizing-zoom-factor-between-views/8660

---

## Post #1 by @lassoan (2019-10-03 15:21 UTC)

<p>Currently, when slice views are linked, zoom factor is only synchronized between views that have the same orientation. It means that when you zoom in on an axial view, you still need to go to sagittal and coronal views if you want to have a close-up view there, too. This can be quite inconvenient when you need to zoom in/out many times.</p>
<p><strong>Proposal: change view link behavior so that zoom factor (field of view) is synchronized between slice views, regardless of their orientation.</strong></p>
<p>Demo of the proposed new behavior:</p>
<div class="lazyYT" data-youtube-id="esP1K917BIY" data-youtube-title="Preview of linking zoom factor between all slice views in the same view group" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>This is the behavior of slice views in ITK-Snap, too.</p>
<p>You can still have different zoom factors in views by not enabling view linking or setting different view group IDs. There should be no performance issues, as on slow computers hot-linking can be disabled (so synchronization only happens when the mouse button is released).</p>
<p>This is a very small, easy modification in the code.</p>
<p><strong>Are there any objections to making this change?</strong></p>

---

## Post #2 by @cpinter (2019-10-03 18:40 UTC)

<p>When I zoom into a slice view, I automatically zoom in the other views, almost 100% of the time. This change would save me those clicks.</p>
<p>My only concern would be about showing different datasets at a time or wanting to show certain views differently on purpose (like an overview for example), but the view groups can handle these cases.</p>
<p>My vote goes for making this change.</p>

---

## Post #3 by @lassoan (2019-10-08 00:32 UTC)

<p>Thank you for the feedback, the change is committed in r28536.</p>

---
