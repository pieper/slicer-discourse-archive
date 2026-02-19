---
topic_id: 43461
title: "Problems With Alpaca"
date: 2025-06-23
url: https://discourse.slicer.org/t/43461
---

# Problems with alpaca 

**Topic ID**: 43461
**Date**: 2025-06-23
**URL**: https://discourse.slicer.org/t/problems-with-alpaca/43461

---

## Post #1 by @aventador17 (2025-06-23 17:13 UTC)

<p>Hello, this is my first time using 3d slicer. I write to community 'cause I have had some problem with ALPACA, it does  not run . The phyton console showes this:</p>
<p>In the future <code>np.bool</code> will be defined as the corresponding NumPy scalar.<br>
Traceback (most recent call last):<br>
File “C:/Users/USUARIO/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/ALPACA.py”, line 105, in setup<br>
from itk import Fpfh<br>
File “C:\Users\USUARIO\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\itk_<em>init</em>_.py”, line 59, in <br>
from itk.support.extras import *<br>
File “C:\Users\USUARIO\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\itk\support\extras.py”, line 37, in <br>
import itk.support.types as itkt<br>
File “C:\Users\USUARIO\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\itk\support\types.py”, line 178, in <br>
) = itkCType.initialize_c_types_once()<br>
File “C:\Users\USUARIO\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\itk\support\types.py”, line 143, in initialize_c_types_once<br>
<em>B: “itkCType” = itkCType(“bool”, “B”, np.dtype(np.bool))<br>
File "C:\Users\USUARIO\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Lib\site-packages\numpy_<em>init</em></em>.py", line 353, in <strong>getattr</strong><br>
raise AttributeError(<strong>former_attrs</strong>[attr])<br>
AttributeError: module ‘numpy’ has no attribute ‘bool’.<br>
<code>np.bool</code> was a deprecated alias for the builtin <code>bool</code>. To avoid this error in existing code, use <code>bool</code> by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use <code>np.bool_</code> here.<br>
The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:<br>
<a href="https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations" class="inline-onebox" rel="noopener nofollow ugc">NumPy 1.20.0 Release Notes — NumPy v2.4.dev0 Manual</a></p>
<p>I hope someone could help me, I would be very grateful</p>

---

## Post #2 by @muratmaga (2025-06-23 17:15 UTC)

<p>please see the workaround in this thread:</p><aside class="quote" data-post="3" data-topic="43415">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/opening-alpaca-for-the-first-time-and-stuck-on-installing-alpaca-python-packages/43415/3">Opening ALPACA for the first time and stuck on "Installing ALPACA Python Packages...."</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/jsguerra">@jsguerra</a> If you are tracking the github issue, until the fix is integrated, the workaround is to manually install the numpy. These steps worked for me: 

in Python console type `pip_install(“numpy==2.00”)’
Restart Slicer
Switch to ALPACA

It should continue installing remaining packages (pandas) and then ALPACA should be working.
  </blockquote>
</aside>


---

## Post #3 by @aventador17 (2025-06-24 02:09 UTC)

<p>Thenks a lot for your answer. I have installed numpy as you said, but a new error has appeared, it says: “AttributeError: <code>np.Inf</code> was removed in the NumPy 2.0 release. Use <code>np.inf</code> instead.”</p>

---

## Post #4 by @jamesobutler (2025-06-24 08:26 UTC)

<p>FYI <a class="mention" href="/u/smrolfe">@smrolfe</a></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/4b3234c5cd36e235cdd906835faa202626d3f413/ALPACA/ALPACA.py#L2500">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/4b3234c5cd36e235cdd906835faa202626d3f413/ALPACA/ALPACA.py#L2500" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/4b3234c5cd36e235cdd906835faa202626d3f413/ALPACA/ALPACA.py#L2500" target="_blank" rel="noopener nofollow ugc">ALPACA/ALPACA.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/SlicerMorph/blob/4b3234c5cd36e235cdd906835faa202626d3f413/ALPACA/ALPACA.py#L2500" rel="noopener nofollow ugc"><code>4b3234c5c</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="2490" style="counter-reset: li-counter 2489 ;">
          <li>    transform.SetIdentity()</li>
          <li>    return [transform, transform]</li>
          <li></li>
          <li>import time</li>
          <li></li>
          <li>bransac = time.time()</li>
          <li></li>
          <li>maxAttempts = 1</li>
          <li>attempt = 0</li>
          <li>best_fitness = -1</li>
          <li class="selected">best_rmse = np.Inf</li>
          <li>while attempt &lt; maxAttempts:</li>
          <li>    # Perform Initial alignment using Ransac parallel iterations with no scaling</li>
          <li>    transform_matrix, fitness, rmse = self.ransac_using_package(</li>
          <li>        movingMeshPoints=sourcePoints,</li>
          <li>        fixedMeshPoints=targetPoints,</li>
          <li>        movingMeshFeaturePoints=moving_corr.T,</li>
          <li>        fixedMeshFeaturePoints=fixed_corr.T,</li>
          <li>        number_of_iterations=parameters["maxRANSAC"],</li>
          <li>        number_of_ransac_points=3,</li>
          <li>        inlier_value=float(parameters["distanceThreshold"]) * voxelSize,</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I would suggest adding the ruff hook to SlicerMorph’s pre-commit-config like in Slicer as ruff includes a numpy 2 deprecation rule that can auto apply fixes ( <a href="https://docs.astral.sh/ruff/rules/numpy2-deprecation/" class="inline-onebox" rel="noopener nofollow ugc">numpy2-deprecation (NPY201) | Ruff</a>).</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/406beac7a2583eed3cc91513f7aaa314d6668cc9/.pre-commit-config.yaml#L20">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/406beac7a2583eed3cc91513f7aaa314d6668cc9/.pre-commit-config.yaml#L20" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/406beac7a2583eed3cc91513f7aaa314d6668cc9/.pre-commit-config.yaml#L20" target="_blank" rel="noopener nofollow ugc">.pre-commit-config.yaml</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/406beac7a2583eed3cc91513f7aaa314d6668cc9/.pre-commit-config.yaml#L20" rel="noopener nofollow ugc"><code>406beac7a</code></a>
</div>



    <pre class="onebox"><code class="lang-yaml">
      <ol class="start lines" start="10" style="counter-reset: li-counter 9 ;">
          <li>    - id: check-yaml</li>
          <li>    - id: debug-statements</li>
          <li>      exclude: "Base/QTGUI/Testing/Data/Input/qSlicerScriptedLoadableModuleSyntaxErrorTestWidget.py|Base/QTGUI/Testing/Data/Input/qSlicerScriptedLoadableModuleSyntaxErrorTest.py"</li>
          <li>    - id: end-of-file-fixer</li>
          <li>      exclude: "\\.(md5|svg|vtk|vtp)$|^Resources\\/[^\\/]+\\.h$|\\/ColorFiles\\/.+\\.txt$|Data\\/Input\\/.+$"</li>
          <li>    - id: mixed-line-ending</li>
          <li>      exclude: "\\.(svg|vtk|vtp)$"</li>
          <li>    - id: trailing-whitespace</li>
          <li>      exclude: "\\.(svg|vtk|vtp)$"</li>
          <li></li>
          <li class="selected">- repo: https://github.com/astral-sh/ruff-pre-commit</li>
          <li>  rev: v0.12.0</li>
          <li>  hooks:</li>
          <li>    - id: ruff</li>
          <li>      args: ["--fix", "--show-fixes"]</li>
          <li></li>
          <li>- repo: https://github.com/asottile/pyupgrade</li>
          <li>  rev: v3.20.0</li>
          <li>  hooks:</li>
          <li>    - id: pyupgrade</li>
          <li>      args: [--py312-plus]</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @muratmaga (2025-06-24 16:57 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>When is Slicer going to officially transition to numpy 2?</p>

---

## Post #6 by @jamesobutler (2025-06-24 18:04 UTC)

<p>Slicer preview already comes with numpy 2 bundled. This was updated as part of the transition to Python 3.12. Most latest Python packages have numpy binary compatibility with numpy 1 and 2.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/6afc5bc94decd35561717583fde1c3f63d6fb5d8/SuperBuild/External_python-numpy.cmake#L43">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/6afc5bc94decd35561717583fde1c3f63d6fb5d8/SuperBuild/External_python-numpy.cmake#L43" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/6afc5bc94decd35561717583fde1c3f63d6fb5d8/SuperBuild/External_python-numpy.cmake#L43" target="_blank" rel="noopener nofollow ugc">SuperBuild/External_python-numpy.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/6afc5bc94decd35561717583fde1c3f63d6fb5d8/SuperBuild/External_python-numpy.cmake#L43" rel="noopener nofollow ugc"><code>6afc5bc94</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="33" style="counter-reset: li-counter 32 ;">
          <li># Hashes correspond to the following packages:</li>
          <li>#  - numpy-2.0.2-cp312-cp312-macosx_10_9_x86_64.whl</li>
          <li>#  - numpy-2.0.2-cp312-cp312-macosx_11_0_arm64.whl</li>
          <li>#  - numpy-2.0.2-cp312-cp312-macosx_14_0_arm64.whl</li>
          <li>#  - numpy-2.0.2-cp312-cp312-macosx_14_0_x86_64.whl</li>
          <li>#  - numpy-2.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl</li>
          <li>#  - numpy-2.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl</li>
          <li>#  - numpy-2.0.2-cp312-cp312-musllinux_1_1_x86_64.whl</li>
          <li>#  - numpy-2.0.2-cp312-cp312-musllinux_1_2_aarch64.whl</li>
          <li>#  - numpy-2.0.2-cp312-cp312-win_amd64.whl</li>
          <li class="selected">numpy==2.0.2 --hash=sha256:df55d490dea7934f330006d0f81e8551ba6010a5bf035a249ef61a94f21c500b \</li>
          <li>             --hash=sha256:8df823f570d9adf0978347d1f926b2a867d5608f434a7cff7f7908c6570dcf5e \</li>
          <li>             --hash=sha256:9a92ae5c14811e390f3767053ff54eaee3bf84576d99a2456391401323f4ec2c \</li>
          <li>             --hash=sha256:a842d573724391493a97a62ebbb8e731f8a5dcc5d285dfc99141ca15a3302d0c \</li>
          <li>             --hash=sha256:c05e238064fc0610c840d1cf6a13bf63d7e391717d247f1bf0318172e759e692 \</li>
          <li>             --hash=sha256:0123ffdaa88fa4ab64835dcbde75dcdf89c453c922f18dced6e27c90d1d0ec5a \</li>
          <li>             --hash=sha256:96a55f64139912d61de9137f11bf39a55ec8faec288c75a54f93dfd39f7eb40c \</li>
          <li>             --hash=sha256:ec9852fb39354b5a45a80bdab5ac02dd02b15f44b3804e9f00c556bf24b4bded \</li>
          <li>             --hash=sha256:cfd41e13fdc257aa5778496b8caa5e856dc4896d4ccf01841daee1d96465467a</li>
          <li># [/numpy]</li>
          <li>]===])</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @aventador17 (2025-06-25 01:35 UTC)

<p>Muchas gracias por tu repsuesta, el problema fue solucionado. Ten un maravilloso día. <img src="https://emoji.discourse-cdn.com/twitter/raising_hands.png?v=14" title=":raising_hands:" class="emoji" alt=":raising_hands:" loading="lazy" width="20" height="20"></p>

---
