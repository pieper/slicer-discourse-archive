# Volume doesn't after I modify the voxel value

**Topic ID**: 4037
**Date**: 2018-09-09
**URL**: https://discourse.slicer.org/t/volume-doesnt-after-i-modify-the-voxel-value/4037

---

## Post #1 by @Tien_Qiao (2018-09-09 19:26 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: latest from github<br>
Expected behavior: volume color should be changed if I modified its voxel value.<br>
Actual behavior: The volume appearance doesn’t change. I wonder how to trigger updating action?</p>

---

## Post #2 by @lassoan (2018-09-09 20:42 UTC)

<p>You can call <code>slicer.util.arrayFromVolumeModified(myvolumenode)</code>. See documentation and related functions here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py" target="_blank">Slicer/Slicer/blob/master/Base/Python/slicer/util.py</a></h4>
<pre><code class="lang-py">
from __future__ import print_function

#
# General
#

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def quit():
  exit(EXIT_SUCCESS)

def exit(status=EXIT_SUCCESS):
  """Exits the application with the specified exit code.
  The method does not stops the process immediately but lets
  pending events to be processed.
  If exit() is called again while processing pending events,
  the error code will be overwritten.

</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
