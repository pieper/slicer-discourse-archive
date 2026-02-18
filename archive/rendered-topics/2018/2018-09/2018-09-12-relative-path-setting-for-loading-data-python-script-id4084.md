# Relative path setting for loading data python script

**Topic ID**: 4084
**Date**: 2018-09-12
**URL**: https://discourse.slicer.org/t/relative-path-setting-for-loading-data-python-script/4084

---

## Post #1 by @Saima (2018-09-12 15:19 UTC)

<p>How to set relative path for loading Data using scripts in python slicer?</p>

---

## Post #2 by @cpinter (2018-09-12 15:31 UTC)

<p>Relative to what? Please be more specific.</p>
<p>There are paths in the object slicer.app, such as</p>
<pre><code>slicer.app.slicerHome
</code></pre>
<p>You can concatenate the relative path to one of these.</p>

---

## Post #4 by @lassoan (2018-12-17 14:16 UTC)

<p><em>(See below a response that a user posted a few hours ago. Unfortunately, the response was flagged as spam - probably due to reviving a stale discussion and posting a short answer with a suspicious link - and I’ve made a mistake of confirming that this was a spam.)</em></p>
<hr>
<p>PYTHONPATH is used by the python interpreter to determine which modules to load.</p>
<p><a href="http://net-informations.com/python/intro/path.htm" rel="nofollow noopener">PATH</a> is used by the shell to determine which executables to run.</p>

---
