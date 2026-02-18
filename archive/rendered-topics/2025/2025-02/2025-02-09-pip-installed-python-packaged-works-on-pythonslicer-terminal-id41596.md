# Pip installed Python packaged works on PythonSlicer terminal but not on Slicer console

**Topic ID**: 41596
**Date**: 2025-02-09
**URL**: https://discourse.slicer.org/t/pip-installed-python-packaged-works-on-pythonslicer-terminal-but-not-on-slicer-console/41596

---

## Post #1 by @modenaxe (2025-02-09 23:40 UTC)

<p>Hello,<br>
I would like to install a python wheel not available form Pypi that was built for Python 3.9.10, which is the same version I see on the Slicer Python console. As suggested in various other posts, I am installing the package using pip:</p>
<pre><code class="lang-auto">PythonSlicer.exe -m pip install package.whl
</code></pre>
<p>After installation I can correctly import the package and use it with the PythonSlicer command line, but if I try to do the same on the Slicer GUI Python Console, Slicer will freeze and crash.<br>
If there anything specific that I could try to debug this issue? As mentioned, the python version of the wheel matches the PythonSlicer one, but I am not sure if I have to check anything else, e.g. other packages compatibility.<br>
Thank you,<br>
Luca</p>

---

## Post #2 by @jamesobutler (2025-02-09 23:47 UTC)

<p>What are the Python package dependencies for your package? Any specific versions of those packages you require?</p>
<p>This is an issue on Windows? Have you tried any debugging on another platform?</p>
<p>Does your package rely on any other special considerations such as OS environment variables?</p>

---

## Post #3 by @modenaxe (2025-02-10 00:03 UTC)

<p>Hi James,<br>
sorry for the lack of details.<br>
I am working on Windows 11, the package is a slightly altered version of <a href="https://github.com/opensim-org/opensim-core" rel="noopener nofollow ugc">opensim</a>, for which I built the libraries and the wheels <a href="https://github.com/modenaxe/testBuildOpenSim/actions/runs/13224443598" rel="noopener nofollow ugc">here</a>. The dependencies are included in the package, which needs to know where the dynamic libraries are, but I have specified that path as an environment variable.<br>
Let me know if there is anything else that could be important to know and thank you for the quick reply!<br>
Luca</p>

---

## Post #4 by @jamesobutler (2025-02-10 03:42 UTC)

<p>Reviewing your whl build output, I suspect something to do with HDF5 which I saw was a dependency in your package.</p>
<p>See the following forum post with a similar issue of crashing within the application, but not when calling PythonSlicer directly:</p>
<aside class="quote quote-modified" data-post="16" data-topic="23408">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicercat-error-with-hdf5/23408/16">SlicerCAT error with hdf5</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    This is only a problem if an application or library brings its own HDF5 as a shared library, without shared library name or symbol mangling. 
ITK and VTK behave well - their HDF5 will not clash with anything (other than potentially another ITK and VTK), unless you force using “system” HDF5. If you force ITK or VTK to use "system HDF5 then it is entirely up to you to manage version conflicts. 
I’ve checked the wheel files of netcdf4 and h5py. 
netcdf4 behaves well - it links HDF5 staticallly, so…
  </blockquote>
</aside>


---

## Post #5 by @modenaxe (2025-02-10 08:23 UTC)

<p>Hi James,<br>
I have built another wheel removing HDF5 and with the minimum amount of dependencies allowed by the main libraries (available <a href="https://github.com/modenaxe/testBuildOpenSim/actions/runs/13234782951" rel="noopener nofollow ugc">here</a>) and the issue persists.<br>
I can smoothly load and use the package using the PythonSlicer console but the Slicer GUI still freezes when I try to do exactly the same using <code>import opensim</code>. I have tried few times and in one occasion the GUI was able to load the package and another time the GUI unfreezed with this error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/927d04e85daae10b34edcb8501f8a0bf46e03638.png" data-download-href="/uploads/short-url/kTTyUgdqikQrsMTCmPs3mTZlSFG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/927d04e85daae10b34edcb8501f8a0bf46e03638.png" alt="image" data-base62-sha1="kTTyUgdqikQrsMTCmPs3mTZlSFG" width="690" height="121" data-dominant-color="FEF4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">936×165 6.76 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.<br>
However, the package dlls are on the system Path variable (and PythonSlicer is finding them), so this is confusing because the outcome from the GUI looks inconsistent.<br>
Is the GUI Python Console handling the module loading in the same way as PythonSlicer?</p>

---

## Post #6 by @jamesobutler (2025-02-10 12:43 UTC)

<p>Are you able to build without the ezc3d package? Or if needed are you able to get ezc3d working on its own in Slicer? Last I remember ezc3d’s Python package was only Python 3.10+ compatible and Slicer is using Python 3.9.</p>
<p>One thing to do to get latest help would be to switch from Slicer 5.6.0 to latest Slicer stable 5.8.0.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> may have other thoughts but I would think there is some issues with this package and the app launcher that sets up the paths for things like the Python libraries to load.</p>

---

## Post #7 by @modenaxe (2025-02-11 05:14 UTC)

<p>Hi James, I have now tried with a wheel without ezc3d in Slicer 5.8.0…Again same outcome for both PythonSlicer (smooth loading the module) and Slicer GUI (frozen).<br>
The new wheel is available <a href="https://github.com/modenaxe/testBuildOpenSim/actions/runs/13254251967" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #8 by @modenaxe (2025-02-11 08:21 UTC)

<p>After a bit more testing I can confirm that when used through PythonSlicer.exe the loaded package works perfectly, which I assume it means that it is installed correctly and there are no incompatibilities. So my hypothesis is that the issue is due to a difference in how the GUI loads the packages compared to PythonSlicer. Is there a way to enforce the same loading behaviour?</p>

---

## Post #9 by @jcfr (2025-02-11 14:37 UTC)

<blockquote>
<p>So my hypothesis is that the issue is due to a difference in how the GUI loads the packages compared to PythonSlicer.</p>
</blockquote>
<p>When importing a package from the <em>Python Console</em> <sup class="footnote-ref"><a href="#footnote-122413-1" id="footnote-ref-122413-1">[1]</a></sup> within the application, the Python interpreter is embedded in the overall Qt application, inheriting all Qt, VTK, ITK, and other symbols. As <a class="mention" href="/u/jamesobutler">@jamesobutler</a> originally suggested, an ABI mismatch is likely causing DLL loading failures.</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-122413-1" class="footnote-item"><p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#what-is-the-python-console">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#what-is-the-python-console</a> <a href="#footnote-ref-122413-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #10 by @modenaxe (2025-02-12 00:10 UTC)

<p>Thank you Jean. This is not a familiar topic for me, I assume ABI is application binary incompatibility. Can this issue be overcome with some workaround? Building Slicer and the package on the same platform for example?</p>

---

## Post #11 by @aagatti (2025-02-17 16:12 UTC)

<p>Luca - I was here to try and debug an extension Im working on… I couldnt help but notice your name, and then that the libraray is opensim! Im keen to see what you’re working on.</p>

---

## Post #13 by @modenaxe (2025-03-21 00:02 UTC)

<p>Hi Anthony, I am just learning how to use Slicer and its Python capabilities (and seeing how much I could push it!), the extension system is very clever! Is your extension related to your neural shape model?</p>

---

## Post #14 by @aagatti (2025-03-24 05:08 UTC)

<p>Yes, the extensions are awesome - and they are always getting better! I wrote my first extension for T2 mapping way back (<a href="https://github.com/gattia/Slicer-T2mapping" class="inline-onebox" rel="noopener nofollow ugc">GitHub - gattia/Slicer-T2mapping</a>)… at that point I think you could only use the already installed python libraries, which were pretty basic. Its awesome how it has grown. For this one… I just downloaded the template library, copied by current script into the repository, and told Cursor what I wanted - it handled most of the hard work :D.</p>
<p>The goal of the extension is to deploy our whole pipeline for knee MRI segmentation, quantitative analysis (cartilage thickness, T2), and apply the NSM: <a href="https://www.medrxiv.org/content/10.1101/2025.02.21.25322094v1.full.pdf" rel="noopener nofollow ugc">https://www.medrxiv.org/content/10.1101/2025.02.21.25322094v1.full.pdf</a></p>
<p>But… that might be ambitious. We’ll see how far I can get <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=14" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20">.</p>
<p>I dont think we’ve met in person. Hopefully we’ll get a chance to connect at ISB - I’ll be co-hosting a shape modeling workshop, and we should touch on neural shape models there too.</p>

---

## Post #15 by @modenaxe (2025-03-27 23:13 UTC)

<p>I was planning to attend the workshop…and looking forward to testing your new extension!</p>

---
