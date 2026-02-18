# How to use command line run slicer's models

**Topic ID**: 18427
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/how-to-use-command-line-run-slicers-models/18427

---

## Post #1 by @lyhsky123 (2021-06-30 12:13 UTC)

<p>When I use Mac command line to run this:</p>
<p>/Applications/Slicer.app/Contents/MacOS/Slicer --launch ResampleScalarVolume -i linear -s 1,1,1 <br>
$CoregPath/Coreg_$MRI.nii.gz <br>
$CoregPath/CoregResamp_$MRI.nii.gz</p>
<p>It always switches to the ‘Welcome’ model automatedly.<br>
Does anyone know how to use the command line, comes into ‘ResampleScalarVolume’ model?</p>

---

## Post #2 by @pieper (2021-06-30 12:37 UTC)

<p>The <code>--launch</code> option is used to run another program in Slicer’s environment (e.g. paths and settings).</p>
<p>You want to use the <code>--python-code</code> option like this to set the module:</p>
<p>./Slicer-4.13.0-2021-06-28-linux-amd64/Slicer --python-code “slicer.util.selectModule(‘SegmentEditor’)”</p>

---

## Post #3 by @lyhsky123 (2021-06-30 13:44 UTC)

<p>Thank you for your help~</p>

---
