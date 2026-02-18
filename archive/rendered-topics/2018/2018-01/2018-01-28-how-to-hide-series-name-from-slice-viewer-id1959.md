# How to hide series name from slice viewer?

**Topic ID**: 1959
**Date**: 2018-01-28
**URL**: https://discourse.slicer.org/t/how-to-hide-series-name-from-slice-viewer/1959

---

## Post #1 by @Justin_Cramer (2018-01-28 01:35 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.9.0</p>
<p>When I load a series, the series name is displayed in the lower-left corner of any display window. Example: “B: head_ct”. How do I hide this display? Have combed through keyboard shortcuts, preferences, and extensions and cannot find a way to hide it.</p>
<p>This is an issue when taking screenshots as the label is present in the screen capture also.</p>

---

## Post #2 by @lassoan (2018-01-28 05:59 UTC)

<p>You can configure slice view annotations in <code>DataProbe</code> module.</p>
<p>It is difficult to find, so we’ll probably find a better place for it in Slicer5.</p>

---

## Post #3 by @Justin_Cramer (2018-01-28 12:41 UTC)

<p>Great - I’ll look there. Thanks again.</p>

---

## Post #4 by @Fernando (2018-01-29 16:29 UTC)

<p>Hi Andras,</p>
<p>Is there a simple way to do this programmatically?</p>

---

## Post #5 by @lassoan (2018-01-29 17:16 UTC)

<p>You can disable slice view annotations as shown in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Hide_slice_view_annotations_.28DataProbe.29">example in script repository</a>.</p>

---

## Post #6 by @wyli (2023-06-30 09:44 UTC)

<p>It took me some time to find it in the GUI… in case anyone is also searching for this option, please see attached a screenshot of Slicer 5.3 about the option (Quantification-&gt;DataProbe and there are checkboxes in the Corner Text Annotation section) :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60d70dffe7eb882dc4a6f550787ce4a3637f8b45.jpeg" data-download-href="/uploads/short-url/dOGAyOKblaAjQ6dYPiUW4Am3g57.jpeg?dl=1" title="Screenshot 2023-06-30 at 10.40.35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60d70dffe7eb882dc4a6f550787ce4a3637f8b45_2_521x500.jpeg" alt="Screenshot 2023-06-30 at 10.40.35" data-base62-sha1="dOGAyOKblaAjQ6dYPiUW4Am3g57" width="521" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60d70dffe7eb882dc4a6f550787ce4a3637f8b45_2_521x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60d70dffe7eb882dc4a6f550787ce4a3637f8b45_2_781x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60d70dffe7eb882dc4a6f550787ce4a3637f8b45_2_1042x1000.jpeg 2x" data-dominant-color="E8E9EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-30 at 10.40.35</span><span class="informations">1646×1578 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
