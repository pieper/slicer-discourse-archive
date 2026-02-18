# Error when installing scikit-image via Python Interactor

**Topic ID**: 2884
**Date**: 2018-05-22
**URL**: https://discourse.slicer.org/t/error-when-installing-scikit-image-via-python-interactor/2884

---

## Post #1 by @codymorris (2018-05-22 17:55 UTC)

<p>Hello all,</p>
<p>I am trying to install scikit-image into slicer so that I can use some of its histogram equalization and contrast stretching tools.  When I go to install it (after updating pip to 10.0.1) I get errors (as seen below) for scikit-image in particular and may other python packages as well.  Any suggestions would be appreciated.  Thanks.  As a side note, I have tried also installing from wheels and from zipped files but neither of those methods worked either.</p>
<p>Operating system: win10<br>
Slicer version: Nightly 4.9.0-2018-05-20<br>
Expected behavior: install scikit-image (and many other python packages)<br>
Actual behavior:<br>
pip.main([‘install’, ‘scikit-image’])<br>
Collecting scikit-image<br>
Could not fetch URL <a href="https://pypi.python.org/simple/scikit-image/:" rel="nofollow noopener">https://pypi.python.org/simple/scikit-image/:</a> There was a problem confirming the ssl certificate: [Errno 2] No such file or directory - skipping<br>
Could not find a version that satisfies the requirement scikit-image (from versions: )<br>
No matching distribution found for scikit-image<br>
1</p>

---

## Post #2 by @lassoan (2018-05-22 18:29 UTC)

<p>See this topic for explanation: <a href="https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984/9">Slicer-Python Packages Use and Install</a></p>

---

## Post #3 by @codymorris (2018-05-22 18:40 UTC)

<p>After trying the exact steps you mention I still get the same errors. Do you know what might be causing the inability to fetch the files/directories?</p>
<blockquote>
<blockquote>
<blockquote>
<p>pip.main([‘install’, ‘requests’])<br>
Collecting requests<br>
Could not fetch URL <a href="https://pypi.python.org/simple/requests/:" rel="noopener nofollow ugc">https://pypi.python.org/simple/requests/:</a> There was a problem confirming the ssl certificate: [Errno 2] No such file or directory - skipping<br>
Could not find a version that satisfies the requirement requests (from versions: )<br>
No matching distribution found for requests<br>
1</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #4 by @lassoan (2018-05-22 19:13 UTC)

<p>This works for me with the latest nightly build (starting Slicer as an admin):</p>
<pre><code>import pip
pip.main(['install', 'requests'])
</code></pre>
<p>“There was a problem confirming the ssl certificate” is a generic pip error, not related to Slicer. You may be able to fix it by <a href="https://stackoverflow.com/questions/16370583/pip-issue-installing-almost-any-library">installing some additional security certificates</a>, updating pip, or <a href="https://stackoverflow.com/questions/21468550/pip-not-working-behind-firewall">configuring pip to work correctly behind a proxy server/firewall</a>.</p>

---
