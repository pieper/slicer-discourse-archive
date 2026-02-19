---
topic_id: 9594
title: "Install Slicer For All Users Option On Windows"
date: 2019-12-23
url: https://discourse.slicer.org/t/9594
---

# Install slicer for all users option on windows

**Topic ID**: 9594
**Date**: 2019-12-23
**URL**: https://discourse.slicer.org/t/install-slicer-for-all-users-option-on-windows/9594

---

## Post #1 by @muratmaga (2019-12-23 18:05 UTC)

<p>While I like that users now can install slicer into their own user space in centrally administered computers, would it be possible to include an option to say ‘install slicer only for this user’ vs ‘install slicer for all users’ and the latter requiring admins rights?</p>
<p>Currently, even if I installed slicer into <strong>C:\Someslicer_directory,</strong> with my own account that has admin rights, the shortcuts for other users don’t get created automatically and we have to add them one by one…</p>

---

## Post #2 by @pieper (2019-12-23 18:42 UTC)

<p>Hi Murat -</p>
<p>I haven’t looked into windows install issues for a long time, but I believe it’s pretty easy to write a script that creates these kinds of shortcuts after the fact.</p>
<p>Or you could have a look at the NSIS install options to see if there’s something easy to allow both kinds of install (I don’t know of any).</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/2b1dd036839df2f94f86e159a54e952963085ca8/CMake/SlicerApplicationOptions.cmake" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/2b1dd036839df2f94f86e159a54e952963085ca8/CMake/SlicerApplicationOptions.cmake" target="_blank">Slicer/Slicer/blob/2b1dd036839df2f94f86e159a54e952963085ca8/CMake/SlicerApplicationOptions.cmake</a></h4>
<pre><code class="lang-cmake">#-----------------------------------------------------------------------------
# Main application
#-----------------------------------------------------------------------------
# Slicer supports more than one application (i.e. an application
# "OtherApp" in addition to "APPLICATION_NAMEApp").
#
# In that specific case, it is required to differentiate the two applications
# and specify which one should be considered as the *Main* one.
#
# This is usually done within the top level CMakeLists.txt file by setting the variable
# Slicer_MAIN_PROJECT.
#
if(NOT DEFINED Slicer_MAIN_PROJECT)
  set(Slicer_MAIN_PROJECT SlicerApp CACHE STRING "Main project name")
endif()
mark_as_superbuild(Slicer_MAIN_PROJECT:STRING)

#-----------------------------------------------------------------------------
# Applications directory
#-----------------------------------------------------------------------------
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/2b1dd036839df2f94f86e159a54e952963085ca8/CMake/SlicerApplicationOptions.cmake" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2019-12-23 19:43 UTC)

<p>Currently, application settings (enabled extensions, various configuration options) are always stored in the user’s profile.</p>
<p>Since Python packages are installed in the application folder, it does not make much sense anymore to install settings or extensions in user profile folder. Instead it would be probably better to make Slicer install fully self-contained: store all .ini files and install extensions in the application folder.</p>

---
