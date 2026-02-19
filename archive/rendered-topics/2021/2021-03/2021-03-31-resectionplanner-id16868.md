---
topic_id: 16868
title: "Resectionplanner"
date: 2021-03-31
url: https://discourse.slicer.org/t/16868
---

# ResectionPlanner

**Topic ID**: 16868
**Date**: 2021-03-31
**URL**: https://discourse.slicer.org/t/resectionplanner/16868

---

## Post #1 by @Saima (2021-03-31 07:55 UTC)

<p>Hi,<br>
I am unable to download the extension inside 3d slicer ResectionPlanner.<br>
Could you please help.</p>
<p>Regards,<br>
Saima Safdar</p>
<p>[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux2</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/saima/Downloads/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “/home/saima/.config/NA-MIC/Extensions-29402/ResectionPlanner/lib/Slicer-4.11/qt-scripted-modules/ResectionVolume.py”, line 229<br>
except Exception, e:<br>
^<br>
SyntaxError: invalid syntax</p>

---

## Post #2 by @lassoan (2021-04-03 02:06 UTC)

<p>The resection planner modules has not yet been updated to Python3 syntax. If you can, please fix the syntax errors and send a pull request with the proposed changes. If you google for the syntax error then usually you can find the instructions how to fix it but if you get stuck with any particular change then let us know.</p>

---

## Post #3 by @J.vd.Zee (2021-09-01 14:31 UTC)

<p>Hi, is this problem fixed yet? Since, I installed the Resection Planner Extension, it won’t show up in my  available modules. Looking forward to hearing from you!</p>

---

## Post #4 by @Saima (2021-09-03 06:00 UTC)

<p>Hi,<br>
I just went to page</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/ResectionPlanner/blob/master/ResectionVolume/ResectionVolume.py">
  <header class="source">

      <a href="https://github.com/SlicerIGT/ResectionPlanner/blob/master/ResectionVolume/ResectionVolume.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/ResectionPlanner/blob/master/ResectionVolume/ResectionVolume.py" target="_blank" rel="noopener nofollow ugc">SlicerIGT/ResectionPlanner/blob/master/ResectionVolume/ResectionVolume.py</a></h4>


    <pre><code class="lang-py">import os
import unittest
from __main__ import vtk, qt, ctk, slicer

#
# ResectionVolume
#

class ResectionVolume:
  def __init__(self, parent):
    self.parent = parent
    self.moduleName = self.__class__.__name__
    parent.title = "ResectionVolume"
    parent.categories = ["IGT"]
    parent.dependencies = []
    parent.contributors = ["Matt Lougheed (Queen's University)"]
    parent.helpText = """
    This module uses fiducial points to generate a 3D shape. The shape can be adjusted by dragging or adding new fiducials and is used to recolor a label map.
    """
    parent.acknowledgementText = """
</code></pre>


  This file has been truncated. <a href="https://github.com/SlicerIGT/ResectionPlanner/blob/master/ResectionVolume/ResectionVolume.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I used the logic implemented.</p>
<p>Regards,<br>
Saima Safdar</p>

---
