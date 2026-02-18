# Loading matrix data structure

**Topic ID**: 9859
**Date**: 2020-01-17
**URL**: https://discourse.slicer.org/t/loading-matrix-data-structure/9859

---

## Post #1 by @wieke.prummel (2020-01-17 22:07 UTC)

<p>Hello slicer community,</p>
<p>I would like to load a matrix data structure (json and csv file) into Slicer.</p>
<p>Is it possible to define our own slicer node type?</p>
<p>Thank you,<br>
Wieke</p>

---

## Post #2 by @pieper (2020-01-17 23:14 UTC)

<p>Yes, you can make custom node types in C++, but maybe you want to use a Table Node?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Tables" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Tables</a></p>
<p>If that’s not what you need please provide more details on your use case.</p>

---

## Post #3 by @wieke.prummel (2020-01-22 16:24 UTC)

<p>Thank you for your answer.</p>
<p>I can work with the table Node to represent connections, but in order to associate rows with metadata (such as: names, location in atlas and hierarchy) I would like to load this through a json file.</p>
<p>I looked at the Terminology Module, but this didn’t seem to work.<br>
Is it possible to customize the terminology Node?</p>

---

## Post #4 by @lassoan (2020-01-22 16:56 UTC)

<p>You can create custom terminologies. You can start from the <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Terminologies/Resources">current terminology files</a> and create yours and add it in the terminology selector widget:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a733cf4479c1b7783b5fb6afad8b4f377a407cc.png" data-download-href="/uploads/short-url/3LZjgr2LCUKECh284sP5r2WRGBS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a733cf4479c1b7783b5fb6afad8b4f377a407cc_2_690x374.png" alt="image" data-base62-sha1="3LZjgr2LCUKECh284sP5r2WRGBS" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a733cf4479c1b7783b5fb6afad8b4f377a407cc_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a733cf4479c1b7783b5fb6afad8b4f377a407cc_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a733cf4479c1b7783b5fb6afad8b4f377a407cc_2_1380x748.png 2x" data-dominant-color="D9E6ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1526×829 51.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Are you aware of <a href="https://www.openanatomy.org/">Open Anatomy</a> effort? Atlas import/export/authoring tools are being developed in Slicer (see <a href="https://github.com/PerkLab/SlicerOpenAnatomy">extension</a> and <a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/">this week’s Open Anatomy discussions</a>).</p>

---
