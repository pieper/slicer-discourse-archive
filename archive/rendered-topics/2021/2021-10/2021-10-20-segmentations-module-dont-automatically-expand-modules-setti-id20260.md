# Segmentations module: don't automatically expand module's settings pane for long file/folder paths

**Topic ID**: 20260
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/segmentations-module-dont-automatically-expand-modules-settings-pane-for-long-file-folder-paths/20260

---

## Post #1 by @DIV (2021-10-20 11:02 UTC)

<p>I have noticed that when I select the <strong>Segmentations</strong> module the greyish pane at left of screen where all of the settings for that module are entered will expand if the path to the <strong>Destination folder</strong> under <em>Export to files</em> is rather lengthy.  (I imagine that there is no limit imposed on the expansion.)<br>
While it’s nice to be able to see the entire path at a glance, the serious disadvantage is that the viewing area is encroached upon.  While the vertical separator between the two ‘halves’ of the screen can be moved, it cannot be dragged further left.</p>
<p>A possible solution would be to:</p>
<ul>
<li>
<em>not</em> automatically expand the module’s pane (thereby <em>preserving</em> space for the viewing port);</li>
<li>display the path name in ellipted (abbreviated) form, such as “C:\users\DIV\…\subsubsubdir” (this style of presentation is already implemented elsewhere in Slicer, such as in the full path to the *.mrml file shown next to <em>Data Probe</em> in several modules);</li>
<li>display the full path name in a tooltip (tooltips are already implemented elsewhere throughout Slicer).</li>
</ul>
<p>Analogous behaviour to this proposed solution is seen in other (Windows) applications.</p>
<p>—DIV</p>

---

## Post #2 by @DIV (2021-12-01 05:29 UTC)

<p>Is anybody else bothered by this?<br>
Does anyone have a suggestion to fix it?<br>
Maybe the code relating to <code>ctkDirectoryButton</code> (<em>e.g.</em> in <code>qMRMLSegmentationFileExportWidget.ui</code> and <code>qSlicerCLIModuleUIHelper.cxx</code>) could be relevant?  Perhaps something to do with <code>setSizePolicy</code>?<br>
—DIV</p>

---

## Post #3 by @lassoan (2021-12-22 15:19 UTC)

<p>I’ve pushed a fix for this today. Long paths are now elided (middle is replaced by <code>...</code>) in directory buttons instead of requiring a lot of space for displaying the full path.</p>

---

## Post #4 by @DIV (2022-03-31 03:26 UTC)

<p>Something similar occurs in both the <strong>Segmentations</strong> module and the <strong>Segment Editor</strong> module for the <em>name</em> of the <code>Segmentation</code> (and <code>Segment</code>?).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75224dc8ff850f3716f94b309e60637a0c16d544.png" data-download-href="/uploads/short-url/gIdmiGcS0hYg2jrEYLbdE0q3rjS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75224dc8ff850f3716f94b309e60637a0c16d544_2_690x159.png" alt="image" data-base62-sha1="gIdmiGcS0hYg2jrEYLbdE0q3rjS" width="690" height="159" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75224dc8ff850f3716f94b309e60637a0c16d544_2_690x159.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75224dc8ff850f3716f94b309e60637a0c16d544_2_1035x238.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75224dc8ff850f3716f94b309e60637a0c16d544.png 2x" data-dominant-color="97B49A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×316 43.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe this is not typical of all users, but I had output an STL file with a rather long filename to try to keep track of the process used to generate it.  (As I’ve said elsewhere, I may want to <a href="https://discourse.slicer.org/t/simple-color-vs-terminology-color-usage/20271/13">compare different attempted segmentations of the same anatomy</a>.)  I then reloaded it with the <code>Data</code> button as a segmentation, and with the existing name the panel at the left takes up a minimum of half my screen (note that the application is maximised in the above screenshot).<br>
Interestingly, even if I switch to make a different <code>Segmentation</code> “active”, I still cannot shrink the pane.</p>
<p>Whereas for a file path it’s usual to put ellipsis at the start or in the middle (and then display the full path in a tooltip), for an object name I think it’s more usual to put the ellipsis at the end (and then display the full name in a tooltip).<br>
—DIV</p>

---

## Post #5 by @lassoan (2022-06-19 04:11 UTC)

<aside class="quote no-group" data-username="DIV" data-post="4" data-topic="20260">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Interestingly, even if I switch to make a different <code>Segmentation</code> “active”, I still cannot shrink the pane.</p>
</blockquote>
</aside>
<p>I’ve implemented a small <a href="https://github.com/Slicer/Slicer/commit/5ecfcc37a51703bbd5638ecd6508541d35661e74">fix</a> to prevent a long segmentation or master node name making the Segment Editor widget very wide.</p>

---

## Post #6 by @lassoan (2023-03-21 02:04 UTC)



---
