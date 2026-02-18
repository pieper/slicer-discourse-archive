# Elastix extension error in Nightly version of Slicer

**Topic ID**: 1396
**Date**: 2017-11-07
**URL**: https://discourse.slicer.org/t/elastix-extension-error-in-nightly-version-of-slicer/1396

---

## Post #1 by @roger_sela (2017-11-07 19:27 UTC)

<p>Hi all,</p>
<p>I am trying to run the Elastix module in the Nightly version of Slicer. I have installed the Elastix bundle through Slicer’s Extension Manager. However, I receive an error message (below) each time I try registration with Elastix. Any advice is appreciated. Thanks!</p>
<p>Volume registration is started in working directory: /var/folders/83/cwh_fnrj2t35ldgzvlk6_srh0000gp/T/Slicer/Elastix/20171107_140201_188<br>
Register volumes…<br>
Error: Elastix not found</p>

---

## Post #2 by @lassoan (2017-11-07 19:56 UTC)

<p>Thanks for reporting this, we’ll investigate this. Until then, you can download and install Elastix package separately and set Slicer to use it (see details here: <a href="https://github.com/lassoan/SlicerElastix/issues/2">https://github.com/lassoan/SlicerElastix/issues/2</a>).</p>

---
