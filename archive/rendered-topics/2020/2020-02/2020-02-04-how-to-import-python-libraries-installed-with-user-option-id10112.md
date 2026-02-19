---
topic_id: 10112
title: "How To Import Python Libraries Installed With User Option"
date: 2020-02-04
url: https://discourse.slicer.org/t/10112
---

# How to import python libraries installed with --user option

**Topic ID**: 10112
**Date**: 2020-02-04
**URL**: https://discourse.slicer.org/t/how-to-import-python-libraries-installed-with-user-option/10112

---

## Post #1 by @muratmaga (2020-02-04 21:16 UTC)

<p>on a shared linux system,  if I install pip_install a python package I get this error</p>
<blockquote>
<pre><code>&gt;&gt;&gt; pip_install('scipy')
Collecting scipy
  Using cached https://files.pythonhosted.org/packages/dc/29/162476fd44203116e7980cfbd9352eef9db37c49445d1fec35509022f6aa/scipy-1.4.1-cp36-cp36m-manylinux1_x86_64.whl
Requirement already satisfied: numpy&gt;=1.13.3 in /data/home/apps/Slicer-4.11.0-2020-01-30-linux-amd64/lib/Python/lib/python3.6/site-packages (from scipy) (1.17.3)
Installing collected packages: scipy
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/home/apps/Slicer-4.11.0-2020-01-30-linux-amd64/lib/Python/lib/python3.6/site-packages/scipy'
Consider using the `--user` option or check the permissions.
</code></pre>
</blockquote>
<p>When I use the --user option, scipy is installed under <strong>~/.local/lib/python3.6/site-packages</strong>, but I can’t import it into Slicer.</p>
<blockquote>
<p>import scipy<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
ModuleNotFoundError: No module named ‘scipy’</p>
</blockquote>
<p>Is the only solution to install slicer into a user-writable folder?</p>

---

## Post #2 by @pieper (2020-02-04 22:21 UTC)

<p>Yes, if you want to install a package in the application tree you need to be able to write there.</p>
<p>Or you could try <a href="https://stackoverflow.com/questions/3108285/in-python-script-how-do-i-set-pythonpath">appending to <code>sys.path</code></a> before importing.</p>

---

## Post #3 by @jamesobutler (2020-02-04 23:47 UTC)

<p>If specifically about <code>scipy</code> I have a Slicer <a href="https://github.com/Slicer/Slicer/pull/1254#" rel="nofollow noopener">PR #1254</a> to include Scipy in the standard build. It is a WIP as I stopped working on it after having some issues with it quietly failing due to some likely parallel build problem.  Updates to this PR would be welcomed.</p>

---
