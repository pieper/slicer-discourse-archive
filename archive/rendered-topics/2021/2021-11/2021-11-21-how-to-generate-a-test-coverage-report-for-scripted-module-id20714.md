# How to generate a test coverage report for scripted module?

**Topic ID**: 20714
**Date**: 2021-11-21
**URL**: https://discourse.slicer.org/t/how-to-generate-a-test-coverage-report-for-scripted-module/20714

---

## Post #1 by @pll_llq (2021-11-21 17:41 UTC)

<p>The title says it all.</p>
<p>Is there a way to generate a test coverage report based on the contents of the <code>ScriptedLoadableModuleTest</code> class contents in a scripted module?</p>

---

## Post #2 by @pieper (2021-11-22 18:13 UTC)

<p>I’m not aware that anyone has tried that, but if I’m not mistaken the scripted module tests are simply pytest invoked from cmake.  So if that’s right you could probably use the pytest coverage tools.  If you come up with a recipe be sure to share it back.</p>

---

## Post #3 by @Alex_Vergara (2021-11-23 09:32 UTC)

<p>I have tried that, it doesn’t work. See <a href="https://gitlab.com/opendose/opendose3d/-/blob/develop/.gitlab-ci.yml" rel="noopener nofollow ugc">https://gitlab.com/opendose/opendose3d/-/blob/develop/.gitlab-ci.yml</a></p>
<p>The relevant pytest lines are commented out because they prevent the module to be built inside CDASH</p>

---

## Post #4 by @pll_llq (2021-11-23 10:05 UTC)

<p>Thanks for the info. I’ll look into what <code>coverage</code> package can provide and if there can be an easy hack to make it work</p>

---

## Post #5 by @pll_llq (2021-11-24 13:27 UTC)

<p>Thanks everyone🖖</p>
<p>Yesterday at the developer call <a class="mention" href="/u/jcfr">@jcfr</a> steered me towards looking into the API of the <code>coverage</code> package and trying to run execution through the Slicer environment.</p>
<p>The <code>coverage</code> package is <em>pip_installable</em> into Slicer and has a pretty simple API.<br>
I came up with this python script that can generate <code>selfTests</code> coverage report for a scriptable module:</p>
<pre><code class="lang-python">import os
from coverage import Coverage

# Setup test execution recording. An sqlite database file will be created here
cov = Coverage(data_file=PATH_TO_COVERAGE_DB)

# Record what lines of code are executed during self test run
cov.start()
slicer.selfTests[MY_MODULE_NAME]()
cov.stop()

# List python files that should be mentioned in the report
extensionPythonFiles = []
for root, dirNames, fileNames in os.walk(PATH_TO_MY_MODULE_FOLDER):
    fileNames = [f for f in fileNames if f.endswith('.py') and not f.startswith('__')]
    for f in fileNames:
        extensionPythonFiles.append(os.path.join(root, f))

# Generate report to a text file
with open(PATH_TO_REPORT_FILE, 'w') as rf:
    cov.report(morfs=extensionPythonFiles, file=rf, show_missing=True)
</code></pre>

---

## Post #6 by @Alex_Vergara (2021-11-26 08:04 UTC)

<p>I think this doesn’t solve the problem. Although it generates the report inside slicer itself, it does not generate the report on build. The build is made using cmake and the tests are done through ctest. This last procedure is not generating reports.</p>

---

## Post #7 by @pll_llq (2021-11-26 08:13 UTC)

<p>I might have not described my use case. At the moment I work only with scriptable modules that I run against the latest slicer so I am not doing builds on the CI. I wanted to have a look at my coverage on the python side and I didn’t look at how to integrate this into the build process.</p>

---

## Post #8 by @Alex_Vergara (2021-11-26 08:15 UTC)

<p>for now I am creating the reports as txt inside slicer, upload them in git pull inside my repo and loading the report after the ctest, UGLY but is the only thing that’s working for me ATM</p>

---
