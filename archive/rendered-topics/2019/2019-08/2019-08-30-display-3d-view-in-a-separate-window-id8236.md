---
topic_id: 8236
title: "Display 3D View In A Separate Window"
date: 2019-08-30
url: https://discourse.slicer.org/t/8236
---

# Display 3d view in a separate window

**Topic ID**: 8236
**Date**: 2019-08-30
**URL**: https://discourse.slicer.org/t/display-3d-view-in-a-separate-window/8236

---

## Post #1 by @rprueckl (2019-08-30 07:52 UTC)

<p>Hi - I remember to read about this subject somewhere, but I am unable to find now where it was. I want to display a 3D view in a dialog (e.g. to preview an STL file to be loaded).</p>
<p>Is there an integrated way to create a view and connecting it to the scene without having it in a layout description? Is <code>app-&gt;mrmlScene()-&gt;CreateNodeByClass("vtkMRMLViewNode");</code> enough to do that? I could then use the widget and re-parent it into my dialog. I assume that I could use the ViewNodeID property of the ModelNode to display the STL only in my view then, while hiding all other ModelNodes.</p>
<p>Is there also a possibility that could be considered to manage a temporary scene for the dialog to display my preview? Is this even possible without side-effects or a lot of overhead?</p>
<p>I would appreciate someone pointing me into the right direction regarding the approach to be used for this.</p>

---

## Post #2 by @pieper (2019-08-30 13:00 UTC)

<p>Did you find this example? I think it’s what you are looking for:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_3D_view_outside_the_view_layout" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_3D_view_outside_the_view_layout</a></p>

---

## Post #3 by @slicer365 (2021-06-10 12:09 UTC)

<p>Is there any way to separate the four views from the main program？</p>
<p>When I use two monitors,  I want one monitor to display the view separately,  the toolbar and input panel are on the other monitor.</p>
<p>Shown as the picture.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f064228e1da5622828030946f3401aba92702676.jpeg" data-download-href="/uploads/short-url/yiB880pCWo6TgchaUq5eyNM8yQS.jpeg?dl=1" title="捕获.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f064228e1da5622828030946f3401aba92702676_2_517x246.jpeg" alt="捕获.PNG" data-base62-sha1="yiB880pCWo6TgchaUq5eyNM8yQS" width="517" height="246" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f064228e1da5622828030946f3401aba92702676_2_517x246.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f064228e1da5622828030946f3401aba92702676_2_775x369.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f064228e1da5622828030946f3401aba92702676_2_1034x492.jpeg 2x" data-dominant-color="B6B1B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获.PNG</span><span class="informations">1295×619 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-06-10 14:55 UTC)

<p>Yes, you can click-and-drag the module panel, toolbars, etc. to move it to your other monitor.</p>

---

## Post #5 by @slicer365 (2021-06-10 15:14 UTC)

<p>Thank you,professor!<br>
I know this .<br>
I mean to move the 3D view and Red,Yellow,Green.</p>
<p>I want to separate the four views from the  Slicer.</p>

---
