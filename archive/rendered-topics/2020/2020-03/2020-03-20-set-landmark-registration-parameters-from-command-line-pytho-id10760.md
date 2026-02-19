---
topic_id: 10760
title: "Set Landmark Registration Parameters From Command Line Pytho"
date: 2020-03-20
url: https://discourse.slicer.org/t/10760
---

# Set landmark registration parameters from command line python

**Topic ID**: 10760
**Date**: 2020-03-20
**URL**: https://discourse.slicer.org/t/set-landmark-registration-parameters-from-command-line-python/10760

---

## Post #1 by @Tokai (2020-03-20 11:01 UTC)

<p>Hi,<br>
I want to set the landmark registration module’s parameters from command line and then later select the landmarks interactively.<br>
For example  instead of using below dialog box to choose fixed and moved one and clicking apply<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71c07a2ab26040ccc7c73fb102aa4ed77ee02f4c.png" alt="Unbenannt" data-base62-sha1="geikKxXR1UZtg7jqzWuVFtmKWGE" width="394" height="208"></p>
<p>I want to set them from command line, so  that I have to do only the land mark selection.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-03-20 16:09 UTC)

<p>Landmark registration module is not prepared to be used from Python. I would recommend to use “Fiducial registration” module instead (it is a CLI module, can be used from Python as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">here</a>).</p>
<p>If you need more advanced features (such as automatic pairing of points, warping registration, real-time update of transformation), you can use “Fiducial registration wizard” module (in SlicerIGT extension).</p>

---
