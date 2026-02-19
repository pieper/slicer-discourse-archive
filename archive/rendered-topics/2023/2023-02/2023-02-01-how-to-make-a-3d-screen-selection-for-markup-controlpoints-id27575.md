---
topic_id: 27575
title: "How To Make A 3D Screen Selection For Markup Controlpoints"
date: 2023-02-01
url: https://discourse.slicer.org/t/27575
---

# How to make a 3D screen selection for Markup ControlPoints?

**Topic ID**: 27575
**Date**: 2023-02-01
**URL**: https://discourse.slicer.org/t/how-to-make-a-3d-screen-selection-for-markup-controlpoints/27575

---

## Post #1 by @sunshine (2023-02-01 02:36 UTC)

<p>Hello everyone,</p>
<p>I am working on my Python Scripted extension, trying to implement a rectangle (drawn by mouse) selection on the screen (3D Widget / Window) to select all the ControlPoints covered by the rectangle.</p>
<p>Could anyone share some ideas on what functions I should call, or what existing modules I can use to achieve this?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @muratmaga (2023-02-01 04:24 UTC)

<p>We have a tool, <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MarkupsEditor">MarkupEditor</a>,  that does something similar (by drawing closed curve Markup) as part of the SlicerMorph extension. I linked the tutorial.</p>
<p>The selection process (add/remove) can be improved. If you don’t want to rebuild from scratch, feel free to contribute to it…</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/MarkupEditor/MarkupEditor.py">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/MarkupEditor/MarkupEditor.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/MarkupEditor/MarkupEditor.py" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/master/MarkupEditor/MarkupEditor.py</a></h4>


      <pre><code class="lang-py">import logging
import math
import numpy
import os
import unittest

import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

from SubjectHierarchyPlugins import AbstractScriptedSubjectHierarchyPlugin

#
# MarkupEditor
#

class MarkupEditor(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/MarkupEditor/MarkupEditor.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @smrolfe (2023-02-01 11:51 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="27575">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>We have a tool, <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MarkupsEditor" rel="noopener nofollow ugc">MarkupEditor</a>, that does something similar (by drawing closed curve Markup) as part of the SlicerMorph extension. I linked the tutorial.</p>
</blockquote>
</aside>
<p>The <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MarkupsEditor" rel="noopener nofollow ugc">MarkupEditor</a> was just updated today with a bug fix, so I recommend downloading from the Github repository directly or installing from the extension manager after the next build (likely tomorrow).</p>

---
