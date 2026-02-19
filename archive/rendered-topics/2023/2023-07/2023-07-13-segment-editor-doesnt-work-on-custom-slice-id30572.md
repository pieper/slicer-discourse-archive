---
topic_id: 30572
title: "Segment Editor Doesnt Work On Custom Slice"
date: 2023-07-13
url: https://discourse.slicer.org/t/30572
---

# Segment Editor doesn't work on custom slice

**Topic ID**: 30572
**Date**: 2023-07-13
**URL**: https://discourse.slicer.org/t/segment-editor-doesnt-work-on-custom-slice/30572

---

## Post #1 by @nnzzll (2023-07-13 01:53 UTC)

<p>I added a custom slice outside the view layout using this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">script</a> and tried to use segment editor paint on it. But it doesn’t work</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d423d7018be11edb5e7f10c35c7e8e616777f8b5.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d423d7018be11edb5e7f10c35c7e8e616777f8b5.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d423d7018be11edb5e7f10c35c7e8e616777f8b5.mp4</a>
    </video>
  </div><p></p>
<p>How can I get the Segment Editor work on slice that outside the view layout?</p>

---

## Post #2 by @lassoan (2023-07-13 02:02 UTC)

<p>Segment Editor gets the list of views from the layout manager, so all the views must be described in the view layout. The good news is that in recent Slicer versions, the <a href="https://discourse.slicer.org/t/new-feature-dual-monitor-and-picture-in-picture-view-layout/27218">layout manager can display views outside the main viewport</a> in a dockable widget that you can make float over other views, displayed in a second monitor, placed right below your module panel, etc.</p>

---
