# How to install python packages using jupyterlab?

**Topic ID**: 21343
**Date**: 2022-01-06
**URL**: https://discourse.slicer.org/t/how-to-install-python-packages-using-jupyterlab/21343

---

## Post #1 by @user4 (2022-01-06 09:16 UTC)

<p>Hi all,I am using the Slicer 4.11 and I am stucked with installing packages.<br>
Here is the thing in detail:</p>
<p>I was trying to install some packages,say matplotlib in Slicer:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4ca52986a6e64b0c1f8a7fe837cba7c2b8831d3.png" alt="image" data-base62-sha1="umqHh4acjUIrCnIaWISxXJauBF1" width="653" height="50"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/485be21e163e3cff9561489cb74a892dedfb3009.png" data-download-href="/uploads/short-url/ak7eGxEYN2qLxOpsYqnHfc0IuKd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/485be21e163e3cff9561489cb74a892dedfb3009.png" alt="image" data-base62-sha1="ak7eGxEYN2qLxOpsYqnHfc0IuKd" width="690" height="181" data-dominant-color="F6DDDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">834×219 7.33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also,I tried to install the package in Python Interactor:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e360b88c40c95f46c36fe44612c736f63b2104d.png" data-download-href="/uploads/short-url/mzBele5mUHiClinuX9era5ZT8zX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e360b88c40c95f46c36fe44612c736f63b2104d.png" alt="image" data-base62-sha1="mzBele5mUHiClinuX9era5ZT8zX" width="690" height="64" data-dominant-color="FCEEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1023×95 5.28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42dbadc74bba38df824bc9d3ba6042f9ee51362a.png" data-download-href="/uploads/short-url/9xsaI4vUO0DGaG1tkbXfUXspw6u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42dbadc74bba38df824bc9d3ba6042f9ee51362a.png" alt="image" data-base62-sha1="9xsaI4vUO0DGaG1tkbXfUXspw6u" width="690" height="30" data-dominant-color="FEEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1288×57 3.92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to manage the package installation quickly and easily?<br>
By the way I was using Anaconda to launch the jupyter and select the Slicer as a kernel.<br>
Thank you for any possible advice in advance.</p>

---

## Post #2 by @Alex_Vergara (2022-01-06 09:19 UTC)

<p>Normal install in jupyterlab</p>
<pre><code class="lang-auto">import sys
import subprocess

def installPackage(package):
    p = subprocess.run([sys.executable, "-m", "pip", "install", "-U", package], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p.stdout.decode())

requirements = ["numpy", "scipy", "matplotlib", "chart_studio", "scikit-learn", "psutil", "openpyxl", "pandas", "pydicom","lmfit","numericalunits", "sqlalchemy"]
for requirement in requirements:
    installPackage(requirement)
</code></pre>
<p>Using Slicer kernel</p>
<pre><code class="lang-auto">from slicer.util import pip_install as installPackage

requirements = ["numpy", "scipy", "matplotlib", "chart_studio", "scikit-learn", "psutil", "openpyxl", "pandas", "pydicom","lmfit","numericalunits", "sqlalchemy"]
for requirement in requirements:
    installPackage(requirement)
</code></pre>

---

## Post #3 by @user4 (2022-01-07 03:21 UTC)

<p>Thank you Alex,<br>
This really works,so if I want to install other packages just add the package name in the requirements right?</p>

---

## Post #4 by @Alex_Vergara (2022-01-07 07:54 UTC)

<p>Normally yes, but you may also try <code>installPackage(requirement, "-U")</code> if something fails</p>

---

## Post #5 by @user4 (2022-01-07 08:31 UTC)

<p>Okay,thank you Alex.</p>

---
