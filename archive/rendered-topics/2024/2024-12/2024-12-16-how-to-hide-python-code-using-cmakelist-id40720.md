---
topic_id: 40720
title: "How To Hide Python Code Using Cmakelist"
date: 2024-12-16
url: https://discourse.slicer.org/t/40720
---

# How to hide python code using CMakeList

**Topic ID**: 40720
**Date**: 2024-12-16
**URL**: https://discourse.slicer.org/t/how-to-hide-python-code-using-cmakelist/40720

---

## Post #1 by @calvinsuzuki (2024-12-16 20:29 UTC)

<p>Hey everyone,<br>
I’m confused about python code obfuscation.</p>
<p><a href="https://discourse.slicer.org/t/how-to-hide-the-code-of-the-script-module/26135">This matter was already discussed on the community<br>
</a></p>
<p>But I couldn’t see how to do it. Which CMakeList should I configure? And when this should be executed? I’m not familiar with any kind of module installation/build. I’m running Slicer on Ubuntu 20.04</p>
<p>Some interesting links were provided, such as <a href="https://github.com/search?q=repo%3ASlicer%2FSlicer%20.pyc&amp;type=code" rel="noopener nofollow ugc">this one</a> and the following CMakeList code block:</p>
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
<p>Can anyone give me a documentation or a guide to help me generate *.pyc and remove *.py of my module? I tried to simply substitute the files, using *.pyc and *.cpython-39.pyc, but it didn’t worked.</p>

---
