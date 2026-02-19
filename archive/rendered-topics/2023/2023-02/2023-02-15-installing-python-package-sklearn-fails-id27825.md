---
topic_id: 27825
title: "Installing Python Package Sklearn Fails"
date: 2023-02-15
url: https://discourse.slicer.org/t/27825
---

# Installing Python package sklearn fails

**Topic ID**: 27825
**Date**: 2023-02-15
**URL**: https://discourse.slicer.org/t/installing-python-package-sklearn-fails/27825

---

## Post #1 by @cpinter (2023-02-15 12:59 UTC)

<p>I’ve noticed that a module we have in SlicerHeart that uses <code>sklearn</code> always wants to install it. I tried to uninstall it and reinstall it, but import failed. Cleared the pip cache (<code>PythonSlicer.exe -m pip cache remove *</code>) but no improvement.</p>
<p>I tried it with the latest stable 5.2.1 and unfortunately it seems that after fresh-installing it and trying to import does not work:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; pip_install('sklearn')
[Python] Collecting sklearn
[Python] Using cached sklearn-0.0.post1.tar.gz (3.6 kB)
[Python] Preparing metadata (setup.py): started
[Python] Preparing metadata (setup.py): finished with status 'done'
[Python] Building wheels for collected packages: sklearn
[Python] Building wheel for sklearn (setup.py): started
[Python] Building wheel for sklearn (setup.py): finished with status 'done'
[Python] Created wheel for sklearn: filename=sklearn-0.0.post1-py3-none-any.whl size=2936 sha256=168c9171f79b986e006af58f4393c3dc817caf4e274bda64939d7f363f7135d4
[Python] Stored in directory: c:\users\pinte\appdata\local\pip\cache\wheels\03\8b\6f\9f13c705de81a6b351b718b3cf917e41ad7c0933c8630d4dd4
[Python] Successfully built sklearn
[Python] Installing collected packages: sklearn
[Python] Successfully installed sklearn-0.0.post1
[Python] [notice] A new release of pip available: 22.3 -&gt; 23.0
[Python] [notice] To update, run: python-real.exe -m pip install --upgrade pip
&gt;&gt;&gt; import sklearn
Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
ModuleNotFoundError: No module named 'sklearn'
</code></pre>
<p>It’s a bit suspicious that the version number is 0.0, but I’m not familiar with sklearn so not sure if this means nightly or what… Any ideas? Thank you!</p>

---

## Post #2 by @jamesobutler (2023-02-15 17:16 UTC)

<p>You are confusing 2 packages. PyPI name sklearn (<a href="https://pypi.org/project/sklearn/" class="inline-onebox" rel="noopener nofollow ugc">sklearn · PyPI</a>) is not the same as PyPI name scikit-learn (<a href="https://pypi.org/project/scikit-learn/" class="inline-onebox" rel="noopener nofollow ugc">scikit-learn · PyPI</a>). Both use the same <code>import sklearn</code> type though when used.</p>
<p><code>pip_install('scikit-learn')</code> is what you need.</p>

---
