# Threading CLI commands

**Topic ID**: 1576
**Date**: 2017-12-01
**URL**: https://discourse.slicer.org/t/threading-cli-commands/1576

---

## Post #1 by @purav70 (2017-12-01 16:40 UTC)

<p>Hi there,</p>
<p>I was wondering if the method slicer.cli.run() acted as a thread, thereby running the command asynchronously, versus the method slicer.cli.runSync().</p>
<p>I need to call on a cli run command several times, and because the dependencies of each command are independent of each other, would using slicer.cli.run parallelize their execution?</p>
<p>Thanks,</p>
<p>Purav</p>

---

## Post #2 by @pieper (2017-12-01 16:55 UTC)

<p>Yes, they can be run in parallel and you can monitor progress and end events.  But also note that a lot of the ITK based CLI implementations already do image-level threading so you may overload your CPU by running them in parallel.  Use top / Task Manager / Activity Monitor as needed.</p>
<p>This test should give you an idea:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/CLIEventTest.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/CLIEventTest.py" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/CLIEventTest.py</a></h4>
<pre><code class="lang-py">import os
import unittest
from __main__ import vtk, qt, ctk, slicer
from slicer.util import VTKObservationMixin
from slicer.ScriptedLoadableModule import *
import time

#
# CLIEventTest
#

class CLIEventTest(ScriptedLoadableModule):
  def __init__(self, parent):
    parent.title = "CLIEventTest" # TODO make this more human readable by adding spaces
    parent.categories = ["Testing.TestCases"]
    parent.dependencies = ["CLI4Test"]
    parent.contributors = ["Johan Andruejol (Kitware)"]
    parent.helpText = """
    This is a self test that tests that CLI send all the event properly.
    """
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/CLIEventTest.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
