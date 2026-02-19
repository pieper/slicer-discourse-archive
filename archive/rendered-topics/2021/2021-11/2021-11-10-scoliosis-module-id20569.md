---
topic_id: 20569
title: "Scoliosis Module"
date: 2021-11-10
url: https://discourse.slicer.org/t/20569
---

# Scoliosis Module

**Topic ID**: 20569
**Date**: 2021-11-10
**URL**: https://discourse.slicer.org/t/scoliosis-module/20569

---

## Post #1 by @stevenagl12 (2021-11-10 17:44 UTC)

<p>I have been going through my downloaded extensions and modifying the scripts that apparently have minor issues, probably from using different systems or different python versions, such as print statements that do not have parentheses around them, and other things, and I found that the Scoliosis module I downloaded through the extension manager has a multitude of TypeError: <strong>init</strong>() takes 1 positional argument but 2 were given issues. I have tried to go through the scripts and identify where these errors are coming from in the scripts, but I must be overlooking them. I have created a gist of the 4 scripts: ToolsViewer.py, VolumesViewer.py, VolumeRenderingViewer.py, and VolumeRenderingPropertiesMenu.py here: <a href="https://gist.github.com/stevenagl12/4be9bcc382a9900182a5b7d5148e3a13" rel="noopener nofollow ugc">Scoliosis_gist</a>. Can anyone help me to identify where these errors are?</p>

---

## Post #2 by @lassoan (2021-11-11 02:58 UTC)

<p>Thank you very much for reviewing modules that have not been kept up-to-date.</p>
<p>Historical background: This extension was developed for a study to compare traditional X-ray based Cobb’s angle measurement with CT and ultrasound based measurements. After this our attention moved on to develop the ultrasound-based scoliosis monitoring system (see a <a href="https://youtu.be/l0BcW8c9CnI?t=420">recent demo video</a>) and not use the extension anymore. <a class="mention" href="/u/ungi">@ungi</a> can provide more details if you were interested.</p>
<p>Would you like to make this extension functional again? If yes, then please submit a pull request to the <a href="https://github.com/SlicerIGT/Scoliosis">Scoliosis repository</a> with all your current fixes and we’ll have a look of what else need to be changed.</p>

---

## Post #3 by @ungi (2021-11-11 13:03 UTC)

<p>As Andras said, we use a different method for spine curve analysis now. Volume reconstruction from AI-segmented images, which produces a single 3D volume. I don’t know of anyone using this extension now, so I’m not sure if it’s worth the effort updating the code. If nobody wants to use it, maybe it’s best to remove it from the extension index.</p>

---
