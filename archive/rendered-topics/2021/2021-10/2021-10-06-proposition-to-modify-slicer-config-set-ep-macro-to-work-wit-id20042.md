---
topic_id: 20042
title: "Proposition To Modify Slicer Config Set Ep Macro To Work Wit"
date: 2021-10-06
url: https://discourse.slicer.org/t/20042
---

# Proposition to modify `slicer_config_set_ep` macro to work with `LIST` vars

**Topic ID**: 20042
**Date**: 2021-10-06
**URL**: https://discourse.slicer.org/t/proposition-to-modify-slicer-config-set-ep-macro-to-work-with-list-vars/20042

---

## Post #1 by @keri (2021-10-06 23:43 UTC)

<p>Hi,</p>
<p>In <code>SlicerConfig.cmake.in</code> there is a macro called <code>slicer_config_set_ep</code>.<br>
Current implementation assumes that the variable is represented as a <code>STRING</code>.<br>
And if the variable is a <code>LIST</code> then cmake configure may fail. For example in my case I have some libs that I link as I dependencies:</p>
<pre><code class="lang-auto">slicer_config_set_ep(
  SOME_LIB_DEPS
  "/home/lib_0.so;/home/lib_1.so;/home/lib_2.so"
  CACHE STRING "Path to project build directory or file" FORCE)
</code></pre>
<p>Then when I try to configure and build some external module I need to <code>find_package(Slicer REQUIRED)</code>.<br>
Configuring my module for the first time works fine, but when I try to reconfigure then I get error yelding that unknown property… In brief cmake tries to retrieve <code>REALPATH</code> property from that <code>"/home/lib_0.so;/home/lib_1.so;/home/lib_2.so"</code></p>
<p>To avoid that I propose to modify this macro in the following manner:</p>
<pre><code class="lang-auto">macro(slicer_config_set_ep var values)
  if(NOT "${values}" STREQUAL "")
    if(DEFINED ${var})
      get_filename_component(var_realpath "${${var}}" REALPATH)
	  foreach(value ${values})
		get_filename_component(val_realpath ${value} REALPATH)
		if (NOT ${val_realpath} IN_LIST var_realpath)
			message(FATAL_ERROR "Variable ${var} defined prior calling 'find_package(Slicer)' does NOT "
					"match value used to configure Slicer. It probably means that a different "
					"${var} has been used to configure this project and Slicer.\n"
					"${var}=${${var}}\n"
					"Slicer_${var}=${value}")
		endif()
	  endforeach()
    endif()
    set(${var} "${values}" ${ARGN})
  endif()
endmacro()
</code></pre>
<p>Thus I assume that the variable is a <code>LIST</code> and I check if list contains some each path.</p>
<p>How do you think?<br>
I tested this modified version and for me it works</p>

---

## Post #2 by @lassoan (2021-10-07 05:51 UTC)

<p>I could not really follow what your problem and solution was, but <a href="https://cmake.org/cmake/help/latest/command/set.html#command:set">CMake does not have a <code>LIST</code> type</a> for cache entries, so we use a the <code>EP_LIST_SEPARATOR</code> (this special string: <code>^^</code>) to separate list items in a string.</p>

---

## Post #3 by @keri (2021-10-07 13:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20042">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="https://cmake.org/cmake/help/latest/command/set.html#command:set" rel="noopener nofollow ugc">CMake does not have a <code>LIST</code> type</a> for cache entries</p>
</blockquote>
</aside>
<p>I think that is the truth but we can consider <code>STRING</code> with semicolon delimited values as a <code>LIST</code> I think.<br>
<code>EP_LIST_SEPARATOR</code> I didn’t tested it but from <code>ExternalProjectDependency.cmake</code> I can see that it works only with <code>_COMMAND</code> options:</p>
<pre data-code-wrap="bash"><code class="lang-bash">#.rst:
# .. cmake:variable:: EP_LIST_SEPARATOR
#
# This variable is used to separate list items when passed in various external project
# ``..._COMMAND`` options.
#
# If defaults to ``^^``.
if(NOT DEFINED EP_LIST_SEPARATOR)
  set(EP_LIST_SEPARATOR "^^")
endif()
</code></pre>
<p>I’ve recorded a small video where I’m trying to explain the problem and uploaded it on <a href="https://drive.google.com/file/d/1IVME8_qk06iwrBKNw3o5o2flIEOvAmv1/view?usp=sharing" rel="noopener nofollow ugc">google drive</a>. Please take a look</p>

---

## Post #4 by @lassoan (2021-10-07 13:15 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> what do you think?</p>

---
