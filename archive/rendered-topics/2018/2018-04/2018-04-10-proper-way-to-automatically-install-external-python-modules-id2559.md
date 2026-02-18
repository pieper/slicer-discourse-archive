# Proper way to automatically install external Python modules

**Topic ID**: 2559
**Date**: 2018-04-10
**URL**: https://discourse.slicer.org/t/proper-way-to-automatically-install-external-python-modules/2559

---

## Post #1 by @patrickcox3 (2018-04-10 17:02 UTC)

<p>I am developing a Scripted Loadable Module that utilizes several external Python modules, specifically scipy, sklearn, and PyWavelets.</p>
<p>Currently, the module has the below script written along with its import statements:</p>
<pre><code class="lang-auto">pip_modules = ['scipy', 'sklearn', 'PyWavelets']
for module_ in pip_modules:
    try:
        module_obj = __import__(module_)
    except ImportError:
        logging.info("{0} was not found.\n Attempting to install {0} . . ."
                     .format(module_))
        pip_main(['install', module_])
</code></pre>
<p>However, I feel this is an ugly and perhaps unacceptable way to do this.<br>
Is there a proper or preferred “Slicery” way for me to check if these modules exist and install them if they do not?</p>
<p>The main approach I have been looking at was using the cmake files, but I have not had any success in that area.</p>

---

## Post #2 by @lassoan (2018-04-10 18:08 UTC)

<p>This solution is appropriate for the current level of support for custom Python dependencies.</p>
<p>Once pip install works for all Python packages on all platforms (currently, binary packages are not available on Windows), we can add some Slicer infrastructure to manage package dependency in a nice, abstract way. Slicer needs to switch to Python3 first, so it will take at least 6-12 months from now.</p>

---
