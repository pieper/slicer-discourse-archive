---
topic_id: 46579
title: "Adaptibility AutoScoper source code"
date: 2026-03-26
url: https://discourse.slicer.org/t/46579
last_bumped: 2026-04-17T15:36:16.294Z
---

# Adaptibility AutoScoper source code

**Topic ID**: 46579
**Date**: 2026-03-26
**URL**: https://discourse.slicer.org/t/adaptibility-autoscoper-source-code/46579

---

## Post #1 by @Sebastiaan (2026-03-26 16:31 UTC)

<p>Hi all,</p>
<p>I am currently working on a MSc Thesis project with mono-planar fluoroscopy images. A current struggle for me is accurate registration of the 3D bone models from MRI or CT to fluoroscopy images. To further optimize the tracking software and obtain high accuracy, I am considering tuning Autoscoper’s source code e.g. by adapting the optimization criteria of the registration. I’m wondering if anyone has experience with this?</p>
<ul>
<li>Is it feasible for ‘outsiders’ to make (minor) adjustments to the code and implement them into Autoscoper/3D Slicer environment in the timeline of a MSc thesis (3-4 months)?</li>
<li>The Gitlab code seems to consist mainly of C++ code, but also some Matlab and Python. Can the tracking software be optimzied through the latter two, or only via the C++ files?</li>
<li>And for someone who is only familiar with Matlab and Python programming: Would it take advanced knowledge of the C++ language to make ‘minor’ changes to the tracking process?</li>
</ul>
<p>In advance thanks for the help!</p>

---

## Post #2 by @John_Holtgrewe (2026-04-03 19:11 UTC)

<p>Hi Sebastiaan,</p>
<p>Thank you for reaching out. Could you provide additional details about your project? Specifically: How are you calibrating your mono-planar setup? Have you tried to use SAM as is, and if so what problems have you encountered?</p>
<p>Thank you,</p>
<p>John</p>

---

## Post #3 by @Sebastiaan (2026-04-09 14:01 UTC)

<p>Hi John,</p>
<p>Thank you for your response! Could you elaborate on what you mean by the calibration of the monoplanar setup?</p>
<p>So far, we have mainly used SAM with available, biplanar datasets. We are still in the early phases of testing with our own data. So, we haven’t really found big problems yet, but will definitely reach out if we do. At this point we are just trying to figure out if it feasible to make changes to the registration process to hopefully imrpove registration accuracy. E.g. would we have to dig into the Autoscoper C++ code (tracking files to change optimization for example)? Or could we make a python-based extension similar to Hierarchical3DRegistration? Do you have any experience with this or advice how to approach this?</p>
<p>Sebastiaan</p>

---

## Post #4 by @John_Holtgrewe (2026-04-17 15:36 UTC)

<p>One of the input requirements for SAM is a calibration file (which is included in the configuration file used to load a trial). Specifics about the formatting of the calibration file can be found <a href="https://autoscoper.readthedocs.io/en/latest/file-specifications/camera-calibration.html" rel="noopener nofollow ugc">here</a>. This file is necessary to relate 2D image coordinates to the 3D world space. Utilizing SAM with mono-planar data would require some sort of calibration method that results in a calibration file that conforms to the formats described in the above link. The calibration process we used has been described in these publications: <a href="https://pubmed.ncbi.nlm.nih.gov/20095029/" rel="noopener nofollow ugc">Brainerd, EL, et al. J Exp Zool A Ecol Genet Physiol, 2010</a>, and <a href="https://pubmed.ncbi.nlm.nih.gov/27655556/" rel="noopener nofollow ugc">Knorlein, BJ, et al. J Exp Biol, 2016</a>.</p>
<p>Could you provide additional details into what changes you are wanting to make to the registration process?</p>
<p>Unfortunately, I do not have any experience with what you are hoping to do, but my understanding is that you should be able to pull the source code and make changes to the code and run it from source.</p>

---
