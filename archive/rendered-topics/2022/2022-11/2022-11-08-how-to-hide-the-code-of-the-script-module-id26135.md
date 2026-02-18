# How to hide the code of the script module?

**Topic ID**: 26135
**Date**: 2022-11-08
**URL**: https://discourse.slicer.org/t/how-to-hide-the-code-of-the-script-module/26135

---

## Post #1 by @qiqi5210 (2022-11-08 13:20 UTC)

<p>Hello everyone,<br>
I would like to ask how to hide the code of the script module. I am developing the script module recently, and I feel that it is a bit insecure to be able to directly see all the code. Hope to get everyone’s help. thanks!</p>
<p>best wishes,<br>
Mary</p>

---

## Post #2 by @pieper (2022-11-08 13:36 UTC)

<p>You can search the internet for ways to hide your python code.  You may be able to make it harder for people to see the code, but it won’t be possible to hide it completely.</p>

---

## Post #3 by @qiqi5210 (2022-11-09 03:08 UTC)

<p>Thanks Pieper.I will try this method. I learned that python code can be hidden by generating PYD files, and I also saw PYD files in Slicer’s generated project bin file, so when should I generate PYD files?Thanks again.<br>
Mary</p>

---

## Post #4 by @pieper (2022-11-09 13:06 UTC)

<p>You’ll need to do some research on this.  By default Slicer expects python scripts to be available in source form with any optimizations like compiling to byte codes being handled automatically by the python infrastructure.</p>

---

## Post #5 by @MJamal (2024-01-19 14:53 UTC)

<p>Hello <a class="mention" href="/u/qiqi5210">@qiqi5210</a> , continuing this discussion further,</p>
<p>I am interested in knowing if you have found any working methods for this?</p>
<p>Thanks,<br>
Mujassim</p>

---

## Post #6 by @lassoan (2024-01-20 13:25 UTC)

<p>You should be able to replace the original .py source code file by the automatically generated .pyc bytecode files or a .py file that to have run through a Python obfuscator tool.</p>

---

## Post #7 by @jamesobutler (2024-01-20 15:08 UTC)

<p>I suggest others also see the easily available uncompiling tools as well to take obfuscated Python code back to human readable.</p>
<p>See uncompyle6 as an example:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pypi.org/project/uncompyle6/">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.35549fe8.ico" class="site-icon" width="32" height="30">

      <a href="https://pypi.org/project/uncompyle6/" target="_blank" rel="noopener nofollow ugc">PyPI</a>
  </header>

  <article class="onebox-body">
    <img width="300" height="300" src="https://pypi.org/static/images/twitter.abaf4b19.webp" class="thumbnail onebox-avatar">

<h3><a href="https://pypi.org/project/uncompyle6/" target="_blank" rel="noopener nofollow ugc">uncompyle6</a></h3>

  <p>Python cross-version byte-code decompiler</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/rocky/python-uncompyle6/">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">

      <a href="https://github.com/rocky/python-uncompyle6/" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/dae360e9eca46972b43b1a31d5d84849f32400ec7bc895ed78b21779900f1e37/rocky/python-uncompyle6" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/rocky/python-uncompyle6/" target="_blank" rel="noopener nofollow ugc">GitHub - rocky/python-uncompyle6: A cross-version Python bytecode decompiler</a></h3>

  <p>A cross-version Python bytecode decompiler. Contribute to rocky/python-uncompyle6 development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @MJamal (2024-01-22 07:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, thank you for your inputs.</p>
<p>Is there any way to have Slicer load scripted modules from <code>.pyd</code> files instead of <code>.py</code> files? Why does Slicer specifically look for <code>module_name.py</code> files in <code>qt-scripted-modules</code> directory?</p>

---

## Post #9 by @lassoan (2024-01-22 16:11 UTC)

<aside class="quote no-group" data-username="MJamal" data-post="8" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>Is there any way to have Slicer load scripted modules from <code>.pyd</code> files instead of <code>.py</code> files? Why does Slicer specifically look for <code>module_name.py</code> files in <code>qt-scripted-modules</code> directory?</p>
</blockquote>
</aside>
<p>.pyd files are not relevant if you develop your code in Python because .pyd files are created by compiling C/C++ code. The module factory is looking for .py (source) and .pyc (byte code) files in scripted module folders.</p>
<p>Probably the simplest solution for hiding your source code is to replace .py files by .pyc files. If you use obfuscation tools then you can keep using .py files but you need to be careful about keeping some publicly used symbols unchanged (e.g., the Slicer module and widget class names must not be obfuscated).</p>

---

## Post #10 by @MJamal (2024-01-23 04:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>.pyd files are not relevant if you develop your code in Python because .pyd files are created by compiling C/C++ code.</p>
</blockquote>
</aside>
<p>Indeed, I generated those .pyd files using the Cython build process.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The module factory is looking for .py (source) and .pyc (byte code) files in scripted module folders.</p>
</blockquote>
</aside>
<p>Does this imply that the module factory utilizes these .py or .pyc files as a package (e.g., importing from .py) to be registered in the factory manager? If that’s the case, then .py files could potentially be replaced with .pyd files, as they are also usable as packages.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably the simplest solution for hiding your source code is to replace .py files by .pyc files. If you use obfuscation tools then you can keep using .py files but you need to be careful about keeping some publicly used symbols unchanged (e.g., the Slicer module and widget class names must not be obfuscated).</p>
</blockquote>
</aside>
<p>However, there’s a challenge. As suggested by <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and confirmed through my own experiments on obfuscated scripts (or .pyc files), I discovered that these can be translated back into a human-readable form. Therefore, using .pyc files or obfuscation tools to conceal the source code might not be a secure approach. This is why I am exploring a way to use .pyd (or .so, .dylib) files in place of .py or .pyc files. There should be a solution!</p>

---

## Post #11 by @lassoan (2024-01-23 05:00 UTC)

<aside class="quote no-group" data-username="MJamal" data-post="10" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>Indeed, I generated those .pyd files using the Cython build process.</p>
</blockquote>
</aside>
<p>If you write your code in C++ then you can create a C++ loadable module, as most of the Slicer core modules. There is no need to use Python then.</p>
<aside class="quote no-group" data-username="MJamal" data-post="10" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>Does this imply that the module factory utilizes these .py or .pyc files as a package (e.g., importing from .py) to be registered in the factory manager?</p>
</blockquote>
</aside>
<p>The .py/.pyc file is imported and then the module and widget classes are instantiated.</p>
<aside class="quote no-group" data-username="MJamal" data-post="10" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>I discovered that these can be translated back into a human-readable form</p>
</blockquote>
</aside>
<p>Yes, you can disassemble any code (including .pyd files) back to human-readable form. You can try to make it harder with some extra work, but you cannot prevent it completely.</p>
<p>Your extra measures would incur extra costs and there many ways around all of them anyway. Even if you run your software as a service on a server, your competitors can still hire your employees, hack into your system, deduce how you do things by observing what your software does, etc.</p>
<p>It would be also irresponsible to try to protect your key technologies just by attempting to keep them secret. Trade secrets are not protected, so any other company can come up with the same product (by taking ideas from you or inventing it independently) and sell it and you may not be able to do anything about it. The other company might even block you from using the technology that you (also) invented if they patent it first. If you patent the idea then it can ensure that only you can use it (and may significantly increase the value of your company), but it can be quite expensive. If you want to avoid patenting cost but want to ensure that you can use your ideas then you may consider publicly disclosing them (e.g., instead of trying to obfuscate the code, you could decide to make the source code publicly available or describe the idea in a research paper).</p>
<p>Overall, if you want to make it harder for people to see how your modules work, distributing .pyc files instead of .py files may be a resonable tradeoff between maixmum protection and minimizing extra costs and complexities.</p>

---

## Post #12 by @MJamal (2024-01-23 16:21 UTC)

<p>Thanks a lot andras! I completely agree with your insights and suggestions.</p>
<p>By the way, I am working on my university end-semester research project, focusing on optimizing and securing Python source code. I came across Slicer and found it to be a good starting point, especially with the demonstration on scripted modules.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you write your code in C++ then you can create a C++ loadable module, as most of the Slicer core modules. There is no need to use Python then.</p>
</blockquote>
</aside>
<p>Yes, I have already created my own Python module, so I’m not planning to rewrite it in C++.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The .py/.pyc file is imported and then the module and widget classes are instantiated.</p>
</blockquote>
</aside>
<p>Could you please guide me to the file(s) where this happens? Your explanation would be quite helpful.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>if you want to make it harder for people to see how your modules work, distributing .pyc files instead of .py files may be a resonable tradeoff</p>
</blockquote>
</aside>
<p>It seems like I don’t have many choices but .pyc. Anyways, instead of manually distributing the .pyc files, how can i automate this in the Slicer build process to generate and utilize .pyc files in the qt-scripted-module directory and completely eliminate the .py files?</p>

---

## Post #13 by @lassoan (2024-01-23 21:31 UTC)

<aside class="quote no-group" data-username="MJamal" data-post="12" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>Could you please guide me to the file(s) where this happens?</p>
</blockquote>
</aside>
<p>You can search for “.pyc” in the slice source tree.</p>
<aside class="quote no-group" data-username="MJamal" data-post="12" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>It seems like I don’t have many choices but .pyc. Anyways, instead of manually distributing the .pyc files, how can i automate this in the Slicer build process to generate and utilize .pyc files in the qt-scripted-module directory and completely eliminate the .py files?</p>
</blockquote>
</aside>
<p>The simplest is probably to write a short Python script that compiles your .py files and then replaces the .py files by the .pyc files.</p>
<p>This script could added as a custom build or installation step in your extension build CMake files. If you are not sure how to do it, you can ask advice on the CMake forum or contract a CMake expert at Kitware.</p>

---

## Post #14 by @MJamal (2024-01-27 16:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The simplest is probably to write a short Python script that compiles your .py files and then replaces the .py files by the .pyc files.</p>
</blockquote>
</aside>
<p>I found that <code>.pyc</code> files were already generated in <code>__pycache__</code> folder of scripted modules after the build process. Can I use those .pyc files directly instead of recompiling .py files?</p>
<p>Furthermore, is there any Slicer-specific CMake flag to determine the directory path of Qt scripted modules?</p>

---

## Post #15 by @lassoan (2024-01-27 16:21 UTC)

<p>Yes, those are cached automatically compiled files. You can certainly use them.</p>
<p>Slicer application looks for scripted module files in <code>lib\Slicer-5.6\qt-scripted-modules</code> folder and folders in the “additional module paths” (stored in application settings).</p>

---

## Post #16 by @jcfr (2024-01-27 21:27 UTC)

<p><strong>Background:</strong> Support for discovering and loading scripted modules from <code>.pyc</code> files has already been implemented for all scripted plugins and modules. You can find the related changes in the <a href="https://github.com/search?q=repo%3ASlicer%2FSlicer%20.pyc&amp;type=code">Slicer GitHub repository</a>.</p>
<p>However, it’s crucial to note that, starting with Python 3.2, the default behavior of <a href="https://docs.python.org/3/library/py_compile.html#py_compile.compile">py_compile.compile</a>, which is utilized in <a href="https://github.com/commontk/CTK/blob/master/CMake/ctk_compile_python_scripts.cmake.in">ctk_compile_python_scripts.cmake.in</a>, is to generate files like <code>__pycache__/scriptname.cpython-XY.pyc</code>, following the specifications in <a href="https://peps.python.org/pep-3147/">PEP-3147</a>. This explains why we may not have <code>*.pyc</code> files compiled after building the <code>CompileSlicerPythonFiles</code> target.</p>
<hr>
<p><strong>Update</strong>: To address this, a pull request has been submitted to the CTK repository. This pull request, available at <a href="https://github.com/commontk/CTK/pull/1188">https://github.com/commontk/CTK/pull/1188</a>, aims to ensure that Slicer scripts are consistently compiled as legacy <code>.pyc</code> files.</p>
<p>After you have a chance to test and review, we will look into integrating the corresponding changes into Slicer.</p>

---

## Post #17 by @MJamal (2024-01-28 13:49 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>, I have reviewed the pull request. Thanks for bringing it up!</p>

---

## Post #18 by @MJamal (2024-02-01 05:01 UTC)

<p>Hello <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>I have written the following script in <code>slicersources-src\CMake\LastConfigureStep\CMakeLists.txt</code> to replace .py with .pyc files during last configuration step. I didn’t encounter any errors during the build process; however, it appears that the script is not functioning as expected. Could you please help me troubleshoot this issue?</p>
<pre><code class="lang-auto">function(replace_py_with_pyc ${SCRIPTED_MODULE_PYCACHE_DIR_PATH})
  if (EXISTS ${SCRIPTED_MODULE_PYCACHE_DIR_PATH}/__pycache__ AND IS_DIRECTORY ${SCRIPTED_MODULE_PYCACHE_DIR_PATH}/__pycache__)
    message("--- Attempting to copy .pyc files...")
    file(GLOB PYC_FILES ${SCRIPTED_MODULE_PYCACHE_DIR_PATH}/__pycache__/*.pyc)
    file(COPY ${PYC_FILES} DESTINATION ${SCRIPTED_MODULE_PYCACHE_DIR_PATH}/)

    message("--- Attempting to remove .py files...")
    file(GLOB PY_FILES ${SCRIPTED_MODULE_PYCACHE_DIR_PATH}/*.py)
    file(REMOVE ${PY_FILES})
  endif()

  file(GLOB SUBDIRS LIST_DIRECTORIES True ${SCRIPTED_MODULE_PYCACHE_DIR_PATH}/*)
  foreach(subdir ${SUBDIRS})
    replace_py_with_pyc(${subdir})
  endforeach()

  message("--- Done copying .pyc files.")
endfunction()

replace_py_with_pyc(${Slicer_INSTALL_QTSCRIPTEDMODULES_LIB_DIR})
</code></pre>

---

## Post #19 by @MJamal (2024-02-01 12:05 UTC)

<p>Never mind, the script is working now. However, I noticed that the build process is still copying Python script files again to the scripted modules.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71759326181b7bc2b42785d70d744a16ebef2e32.png" alt="image" data-base62-sha1="gbHR8l0wkhzENFv9CDfUxH43g3M" width="498" height="205"></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, how can I execute the script on slicer’s post build?</p>

---

## Post #20 by @jcfr (2024-02-02 04:33 UTC)

<p>Technically, the <code>.py</code> files are not replaced, there are removed.</p>
<p>The target <code>CompileSlicerPythonFiles</code> depends on the <code>CopySlicerPythonScriptFiles</code> one, these are defined using the <code>ctkFunctionAddCompilePythonScriptTargets</code> CMake function.<br>
See  <a href="https://github.com/Slicer/Slicer/blob/4efda831815917174b421fb710d1a76e7a9e68f2/CMakeLists.txt#L1280-L1309">Slicer/CMakeLists.txt#L1280-L1309</a></p>
<p>To properly support “compiling” source file exclusively to <code>.pyc</code>, the CMake function <code>ctkFunctionAddCompilePythonScriptTargets</code> should be improved to accept an new parameter option (e.g <code>SKIP_SCRIPT_COPY</code>).<br>
See <a href="https://github.com/commontk/CTK/blob/4aba4e20341c7111f5637337952a089464dc15db/CMake/ctkMacroCompilePythonScript.cmake#L101">CTK/CMake/ctkMacroCompilePythonScript.cmake</a></p>
<p>The  <code>ctkMacroCompilePythonScript.cmake</code> CMake module could also be updated to define an option for controlling the behavior globally  (e.g <code>CTK_COMPILE_PYTHON_SCRIPT_SKIP_SCRIPT_COPY</code>).</p>
<p>This new option should be added to <code>SlicerConfig.cmake.in</code>, that way extension build against Slicer would also leverage it.</p>
<p>This should provide you with enough hints to move forward and create a pull request at <a href="https://github.com/commontk/CTK">https://github.com/commontk/CTK</a></p>
<p>We will address corner cases during the review process.</p>

---

## Post #21 by @MJamal (2024-02-10 11:59 UTC)

<p>Hello <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>I appreciate your suggested hints.</p>
<p>I’m wondering if your solution will work when generating the installer. Specifically, after creating the installer from Visual Studio and when a user installs slicer.exe, I want the installer directory to contain only .pyc files in the qt-scripted-directory.</p>
<p>I aim to automate this process to ensure that, in the end, the user only sees bytecode files. Is this achievable?</p>

---

## Post #22 by @lassoan (2024-02-10 16:55 UTC)

<p>Yes, this solution will work when generating the installer: qt-scripted-modules folders will not contain any .py files.</p>

---

## Post #23 by @MJamal (2024-02-11 04:36 UTC)

<p>Great.</p>
<p>So, <a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/lassoan">@lassoan</a>, since this is my first time contributing to open source, like ctk, I will need your guidance throughout the process of making these changes.</p>
<p>Following <a class="mention" href="/u/jcfr">@jcfr</a>’s suggested hints, here’s what I did:</p>
<p>Firstly, I’ve used <a href="https://github.com/commontk/CTK/blob/master/CMake/ctk_compile_python_scripts.cmake.in" rel="noopener nofollow ugc">this</a> version of <code>ctk_compile_python_scripts.cmake.in</code>. I’ve also defined an option at the top of the file <code>ctkMacroCompilePythonScript.cmake</code>:</p>
<aside class="quote no-group" data-username="jcfr" data-post="20" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>The <code>ctkMacroCompilePythonScript.cmake</code> CMake module could also be updated to define an option for controlling the behavior globally (e.g <code>CTK_COMPILE_PYTHON_SCRIPT_SKIP_SCRIPT_COPY</code>).</p>
</blockquote>
</aside>
<pre><code class="lang-auto"># For default behavior
set(CTK_COMPILE_PYTHON_SCRIPT_SKIP_SCRIPT_COPY FALSE)
</code></pre>
<br>
<p>Then,</p>
<aside class="quote no-group" data-username="jcfr" data-post="20" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>To properly support “compiling” source file exclusively to <code>.pyc</code>, the CMake function <code>ctkFunctionAddCompilePythonScriptTargets</code> should be improved to accept an new parameter option (e.g <code>SKIP_SCRIPT_COPY</code>).</p>
</blockquote>
</aside>
<p>In <code>ctkFunctionAddCompilePythonScriptTargets</code> function , I’ve made the following changes:</p>
<pre><code class="lang-auto">if(NOT MY_GLOBAL_TARGET)
    ctkFunctionAddCompilePythonScriptTargets(${target} ${CTK_COMPILE_PYTHON_SCRIPT_SKIP_SCRIPT_COPY})
  endif()
</code></pre>
<pre><code class="lang-auto">function(ctkFunctionAddCompilePythonScriptTargets target SKIP_SCRIPT_COPY)
  if (NOT ${SKIP_SCRIPT_COPY})
    _ctk_add_copy_python_files_target(${target} Script ${ARGN})
  endif()
  _ctk_add_copy_python_files_target(${target} Resource ${ARGN})
  _ctk_add_compile_python_directories_target(${target})
endfunction()
</code></pre>
<p>and in Slicer/CmakeLists.txt:</p>
<pre><code class="lang-auto"># Create targets CopySlicerPython{Resource, Script}Files, CompileSlicerPythonFiles
if(Slicer_USE_PYTHONQT)
  slicerFunctionAddPythonQtResourcesTargets(SlicerPythonResources)
  ctkFunctionAddCompilePythonScriptTargets(
    ${CTK_COMPILE_PYTHON_SCRIPTS_GLOBAL_TARGET_NAME}
    ${CTK_COMPILE_PYTHON_SCRIPT_SKIP_SCRIPT_COPY}
    DEPENDS SlicerPythonResources
    )
....
</code></pre>
<br>
Finally,
<aside class="quote no-group" data-username="jcfr" data-post="20" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>This new option should be added to <code>SlicerConfig.cmake.in</code>, that way extension build against Slicer would also leverage it.</p>
</blockquote>
</aside>
<p>In <code>SlicerConfig.cmake.in</code> , I’m setting up the flag of <code>CTK_COMPILE_PYTHON_SCRIPT_SKIP_SCRIPT_COPY</code> to be <code>TRUE</code> :</p>
<pre><code class="lang-auto">set(CTK_COMPILE_PYTHON_SCRIPT_SKIP_SCRIPT_COPY TRUE)
</code></pre>
<br>
If I understood correctly, when the `SKIP_SCRIPT_COPY` argument is set to TRUE, I don't think the compilation step will work, since `CompileSlicerPythonFiles` depends on `CopySlicerPythonScriptFiles` target. Is this correct, or did I make a mistake in the changes?

---

## Post #24 by @MJamal (2024-02-13 06:18 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="16" data-topic="26135">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>aims to ensure that Slicer scripts are consistently compiled as legacy <code>.pyc</code> files.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, I’d like to provide an update on this. I’ve observed that all scripts are compiled as <code>.pyc</code> files except for the <code>SegmentEditorEffects/__init__.py</code> script.</p>

---

## Post #25 by @MJamal (2024-03-14 04:07 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/cpinter">@cpinter</a>, What I have found is that the CMake file:</p>
<p><code>slicersources-src\Modules\Loadable\Segmentations\EditorEffects\Python\CMakeLists.txt</code></p>
<p>does not include an entry for the <code>SegmentEditorEffects/__init__.py</code> file when setting <code>SegmentEditorEffects_PYTHON_SCRIPTS</code>, but instead uses the template <code>SegmentEditorEffects.__init__.py.in</code> for configuration.</p>
<p>As per my understanding, we have two ways to handle the compilation for the <code>__init__.py</code> file:</p>
<ol>
<li>We can configure <code>SegmentEditorEffects.__init__.py.in</code> to be in the same directory <code>slicersources-src\Modules\Loadable\Segmentations\EditorEffects\Python\</code> instead of the scripted modules directory and add an entry for it.</li>
<li>Or we can completely replace the template file with the <code>__init__.py</code> file and add the entry directly, as I see there is nothing to be configurable in the template file.</li>
</ol>
<p>What are your thoughts on this?</p>
<p><br><br><br>
Also, following up the PR: <a href="https://github.com/commontk/CTK/pull/1192" rel="noopener nofollow ugc">https://github.com/commontk/CTK/pull/1192</a>.</p>
<p>To completely support ‘.pyc’ for the scripted module <code>SubjectHierarchy</code>,<br>
the file <code>slicersources-src\Modules\Loadable\SubjectHierarchy\Widgets\Python\__init__.py</code> should also be updated to check the file extention:</p>
<p>From:<br>
<code>if fileExtension == '.py' and fileNameNoExtension != '__init__'</code><br>
To:<br>
<code>if fileExtension in ('.py', '.pyc') and fileNameNoExtension != '__init__'</code></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, Do we have any update for the PR?</p>

---

## Post #26 by @jcfr (2024-03-20 18:54 UTC)

<p>Corresponding approach was revisited by instead introduce the option <code>CTK_COMPILE_PYTHON_SCRIPT_KEEP_ONLY_PYC</code> to support removing <code>*.py</code> script once the corresponding <code>*.pyc</code> file has been generated in the destination directory.</p>
<p>See <a href="https://github.com/commontk/CTK/pull/1192">https://github.com/commontk/CTK/pull/1192</a></p>
<p><a class="mention" href="/u/mjamal">@MJamal</a> At your convenience, consider reviewing and testing the proposed changes <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---
