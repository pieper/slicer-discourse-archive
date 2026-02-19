---
topic_id: 1906
title: "Slicer Main Ui Freezes During Python Scripted Module Executi"
date: 2018-01-23
url: https://discourse.slicer.org/t/1906
---

# Slicer main UI freezes during python scripted module execution

**Topic ID**: 1906
**Date**: 2018-01-23
**URL**: https://discourse.slicer.org/t/slicer-main-ui-freezes-during-python-scripted-module-execution/1906

---

## Post #1 by @Milogav (2018-01-23 12:46 UTC)

<p>Hi Slicer developers,</p>
<p>I’m currently developing a python module that performs quite heavy computation over image volumes.</p>
<p>The module computations work as expected giving correct results. However, the main slicer window freezes during execution. When execution finishes, the main UI returns to normal. I would like to retain the UI functionality during execution in order to add a stop button that can halt the exection at user request, and maybe include a progress bar.</p>
<p>I am quite new at slicer developing and I don’t know how to handle this issue. I have already tried to execute the run function of the module logic in a separate thread using the threading library but I couldn get it working and I have read it is not a good approach in Slicer. I have also read that creating a separate cli module is a solution for this, but unfortunately, I very little experience on C++ language apart from some Qt basic knowledge.</p>
<p>Any clues on solving this issue?? or some python code examples I can read???</p>
<p>Thanks in advance for the help!</p>
<p>Miguel</p>

---

## Post #2 by @Davide_Punzo (2018-01-23 13:08 UTC)

<p>Hi Miguel,</p>
<p>the issue is that Slicer GUI is on the same thread that you will run the computation.<br>
CLI modules work because they use another thread.<br>
I don’t know if there is a simple solution in Python.</p>
<p>But,  in the case you feel to experiment with a pure C++ (loadable) module<br>
(or I guess you can convert the code to python),<br>
you may have a look here:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/Punzo/SlicerAstro/tree/master/AstroModeling">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Punzo/SlicerAstro/tree/master/AstroModeling" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Punzo/SlicerAstro/tree/master/AstroModeling" target="_blank" rel="noopener nofollow ugc">SlicerAstro/AstroModeling at master · Punzo/SlicerAstro</a></h3>

  <p><a href="https://github.com/Punzo/SlicerAstro/tree/master/AstroModeling" target="_blank" rel="noopener nofollow ugc">master/AstroModeling</a></p>

  <p><span class="label1">Astronomy (HI) extension for 3DSlicer (https://www.slicer.org/)</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>essentially I have a worker class that run the computation on a separate QThread.<br>
The module needs still some cleaning and the widget has many methods for others things,<br>
therefore it can be hard to go through it. However, the methods that you may be interested are (in the widget class):<br>
onApply<br>
onWorkFinished<br>
onMRMLAstroModelingParametersNodeModified<br>
and the init() to check how to setup the worker and the thread.</p>

---

## Post #3 by @Davide_Punzo (2018-01-23 13:12 UTC)

<p>P.S.: building a CLI module should be easier (and safer) than building your own infrastructure like I did in the link (unless you need more flexibility, like I needed).</p>
<p>You may have a look at the many CLI module in Slicer and check if they satisfy your requirement and start from there. The idea of the CLI module is exactly to give developer an easy way to run heavy computation.</p>

---

## Post #4 by @pieper (2018-01-23 13:46 UTC)

<p>Another option is to use Slicer’s CLI infrastructure to run python code in a separate process.  The CLI python process communicates with Slicer through files, like a C++ CLI would do, so it cannot call the running Slicer python API, but this can be okay for many use cases.  We’ve been looking at adapting SlicerRadiomics to use this approach.</p>

---

## Post #5 by @Milogav (2018-01-23 14:40 UTC)

<p>I guess I will start looking into CLI module developing, as it seems the best solution and I will need it sooner or later.<br>
Thank you very much for your answers, Davide and Steve!</p>

---

## Post #6 by @Milogav (2018-01-25 14:37 UTC)

<p>I have tried to write a preliminary CLI python module. The GUI loads just fine on Slicer but when clicking the apply button I get some import errors:</p>
<p><em>BiasCorrection2 standard error:</em></p>
<p><em>Traceback (most recent call last):</em><br>
_  File “/home/miguel/Documentos/Extensiones_3DSlicer/Prueba/PythonScript”, line 6, in _<br>
_    import numpy as np_<br>
_  File “/home/miguel/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/numpy/<strong>init</strong>.py”, line 142, in _<br>
_    from . import add_newdocs_<br>
_  File “/home/miguel/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/numpy/add_newdocs.py”, line 13, in _<br>
_    from numpy.lib import add_newdoc_<br>
_  File “/home/miguel/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/numpy/lib/<strong>init</strong>.py”, line 8, in _<br>
_    from .type_check import *_<br>
_  File “/home/miguel/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/numpy/lib/type_check.py”, line 11, in _<br>
_    import numpy.core.numeric as <em>nx</em><br>
_  File “/home/miguel/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/numpy/core/<strong>init</strong>.py”, line 26, in _<br>
_    raise ImportError(msg)_<br>
_ImportError: _<br>
<em>Importing the multiarray numpy extension module failed.  Most</em><br>
<em>likely you are trying to import a failed build of numpy.</em><br>
<em>If you’re working with a numpy git repo, try <code>git clean -xdf</code> (removes all</em><br>
<em>files not under version control).  Otherwise reinstall numpy.</em></p>
<p><em>Original error was: /home/miguel/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/numpy/core/multiarray.so: undefined symbol: PyUnicodeUCS2_FromObject</em></p>
<p>The above error is from trying to import numpy.<br>
I would also like to import some slicer functionality via:</p>
<p><em>import slicer</em></p>
<p>But the code seems to break at this line while the GUI says “completed with errors”. Is this what you mean by “it cannot call the running Slicer python API”, <a class="mention" href="/u/pieper">@pieper</a> ??.</p>
<p>Importing os and sys works just fine.</p>
<p>Links to the code here:<br>
<a href="https://github.com/Milogav/BiasCorrection" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/Milogav/BiasCorrection</a></p>
<p>PS: I have not found much information about python cli modules and I don’t know if I require more than creating the .xml file, the program file and add the folder to slicer module path settings. Am I missing something else??</p>

---

## Post #7 by @pieper (2018-01-25 19:05 UTC)

<p>Hi <a class="mention" href="/u/milogav">@Milogav</a> -</p>
<p>You can have a look at what we did for SlicerRadiomicsCLI - there are some subtleties about setting things up to use the right interpreter and to install correctly cross platform, but you should be able to follow pretty much the same recipe (literally just worked out yesterday):</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics/pull/37">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics/pull/37" target="_blank" rel="noopener">github.com/AIM-Harvard/SlicerRadiomics</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/AIM-Harvard/SlicerRadiomics/pull/37" target="_blank" rel="noopener">Add SlicerRadiomicsCLI</a>
      </h4>

    <div class="branches">
      <code>AIM-Harvard:master</code> ← <code>AIM-Harvard:add-cli</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2018-01-24" data-time="17:02:37" data-timezone="UTC">05:02PM - 24 Jan 18 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/JoostJM" target="_blank" rel="noopener">
            <img alt="JoostJM" src="https://avatars.githubusercontent.com/u/18026947?v=4" class="onebox-avatar-inline" width="20" height="20">
            JoostJM
          </a>
        </div>

        <div class="lines" title="4 commits changed 7 files with 197 additions and 0 deletions">
          <a href="https://github.com/AIM-Harvard/SlicerRadiomics/pull/37/files" target="_blank" rel="noopener">
            <span class="added">+197</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Add a SlicerExecutionModel CLI for PyRadiomics. This will run the PyRadiomics ex<span class="show-more-container"><a href="https://github.com/AIM-Harvard/SlicerRadiomics/pull/37" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">traction in a separate process and return the results.
This will allow to perform large extractions without freezing the main UI thread and also allow for progress reporting.

TODO:
- [x] Integrate with SlicerRadiomics module
- [ ] Add progress reporting
- [ ] Intercept logging messages?
- [ ] Make CLI module hidden for users?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>By “it cannot call the running Slicer python API” I meant that Slicer itself will have a python interpreter instance that is populated with data and hooks to the running application instances.  Running a python CLI can import the same packages as slicer but in an independent process so data is only shared by files (or by stdio and exit codes).</p>
<p>-Steve</p>

---
