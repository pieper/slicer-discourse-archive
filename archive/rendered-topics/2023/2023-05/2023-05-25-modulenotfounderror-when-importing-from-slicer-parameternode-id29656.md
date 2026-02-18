# ModuleNotFoundError when importing from slicer.parameterNodeWrapper

**Topic ID**: 29656
**Date**: 2023-05-25
**URL**: https://discourse.slicer.org/t/modulenotfounderror-when-importing-from-slicer-parameternodewrapper/29656

---

## Post #1 by @asyeda (2023-05-25 21:16 UTC)

<p>I am developing a scripted module in Slicer 5.2.2 and one key issue is that when I save/load the scene I want to preserve the class attributes in addition to the views and segmentations so I can fully restore the UI to its previous state. As suggested by this thread:</p><aside class="quote quote-modified" data-post="2" data-topic="9830">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-save-slicer-scene-with-both-slicer-data-and-with-self-variables-within-custom-widget/9830/2">How to save slicer scene with both slicer data and with "self.variables" within custom widget</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    You raise a very important point. It is easy to write a scripted module that “works” and it is very tempting to stop there - and not spend time with implementing automatic tests, saving of module state to the scene, etc. 
Developers are supposed to save all information that is necessary to recreate the current state of the module in nodes in the MRML scene. You can find some useful general information about this in the first part of <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="noopener nofollow ugc">PerkLab Scripted Module Development tutorial</a>. This practice is …
  </blockquote>
</aside>
<p>
I have modified my widget class similar to the <code>VectorToScalarVolume</code> class. However, the main issue is that I get a <code>ModuleNotFound</code> error on starting up Slicer.</p>
<p>The error is coming from the line:</p>
<p><code>from slicer.parameterNodeWrapper import parameterNodeWrapper</code></p>
<p>The full traceback looks like this:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/Users/{myname}/Desktop/{modulename} project/Code/{modulename}-main/{modulename}/{modulename}.py", line 32, in &lt;module&gt;
    from slicer.parameterNodeWrapper import parameterNodeWrapper
ModuleNotFoundError: No module named 'slicer.parameterNodeWrapper'
[Qt] loadSourceAsModule - Failed to load file "/Users/{myname}/Desktop/{modulename} project/Code/{modulename}-main/{modulename}/{modulename}.py"  as module "{modulename}" !
[Qt] Fail to instantiate module {modulename}
[Qt] The following modules failed to be instantiated:
[Qt]    {modulename}
</code></pre>
<p>It’s a confusing error, since this line seems to work just fine in <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py" rel="noopener nofollow ugc">VectorToScalarVolume</a> and the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/parameter_nodes/overview.html" rel="noopener nofollow ugc">official documentation</a>. I’m working with Slicer 5.2.2 and haven’t had issues importing from <code>slicer.util</code> or elsewhere. I also checked the <a href="https://discourse.slicer.org/t/slicer-5-2-summary-highlights-and-changelog/26916/2">changelog for v5.2</a> but no luck.</p>
<p>What could be causing this issue?</p>

---

## Post #2 by @jamesobutler (2023-05-25 21:26 UTC)

<aside class="quote no-group" data-username="asyeda" data-post="1" data-topic="29656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3da27b/48.png" class="avatar"> asyeda:</div>
<blockquote>
<p>I am developing a scripted module in Slicer 5.2.2</p>
</blockquote>
</aside>
<p><code>slicer.parameterNodeWrapper</code> is not available in Slicer 5.2.2. It is currently only available in latest Slicer Preview. That is why it is not working for you when using Slicer 5.2.2.</p>
<p>VectorToScalarVolume code for Slicer 5.2.2</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/v5.2.2/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/v5.2.2/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/v5.2.2/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/v5.2.2/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py</a></h4>


      <pre><code class="lang-py">from contextlib import contextmanager
import logging
import qt
import vtk

import slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin


@contextmanager
def MyScopedQtPropertySetter(qobject, properties):
    """ Context manager to set/reset properties"""
    # TODO: Move it to slicer.utils and delete it here.
    previousValues = {}
    for propertyName, propertyValue in properties.items():
        previousValues[propertyName] = getattr(qobject, propertyName)
        setattr(qobject, propertyName, propertyValue)
    yield
    for propertyName in properties.keys():
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/v5.2.2/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
versus VectorToScalarVolume code for latest Slicer Preview (aka <code>main</code> branch)</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/main/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py</a></h4>


      <pre><code class="lang-py">from contextlib import contextmanager
import logging
from typing import Optional
import qt
import vtk
import enum

import slicer
from slicer.i18n import tr as _
from slicer.i18n import translate
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin
from slicer.parameterNodeWrapper import parameterNodeWrapper


@contextmanager
def MyScopedQtPropertySetter(qobject, properties):
    """Context manager to set/reset properties"""
    # TODO: Move it to slicer.utils and delete it here.
    previousValues = {}
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @asyeda (2023-05-25 21:32 UTC)

<p>I see - does <code>VectorToScalarVolume</code> in 5.2 implement this functionality too? (saving class attributes when saving mrml scene)</p>

---
