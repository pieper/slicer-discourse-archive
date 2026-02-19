---
topic_id: 12331
title: "Load A Scene From Mnc File"
date: 2020-07-01
url: https://discourse.slicer.org/t/12331
---

# Load a scene from .mnc file

**Topic ID**: 12331
**Date**: 2020-07-01
**URL**: https://discourse.slicer.org/t/load-a-scene-from-mnc-file/12331

---

## Post #1 by @Eloi_gbrt (2020-07-01 23:12 UTC)

<p>Hello,<br>
In the module i develop in python, i need to load a scene. This scene i need to load is a .mnc file.</p>
<p>Does someone know how to load this type of file with python or if i have to convert it and if so the tools i have to use ?</p>
<p>Thank you!<br>
Eloi</p>

---

## Post #2 by @koeglfryderyk (2022-10-17 16:36 UTC)

<p>Slicer doesn’t support .mnc files.</p>
<p>You have to convert them to a different format first, e.g. .nii.</p>
<p>To do that, you can install the <a href="https://bic-mni.github.io" rel="noopener nofollow ugc">MINC Toolkit</a> or <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki" rel="noopener nofollow ugc">Freesurfer</a> and then use the command line tool <code>mnc2nii</code> to convert the file. For example:<br>
<code>mnc2nii Desktop/01_preop_mri.mnc -nii</code></p>

---
