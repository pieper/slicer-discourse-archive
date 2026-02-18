# Monai auto3dsegmenta - error from python package information

**Topic ID**: 35693
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/monai-auto3dsegmenta-error-from-python-package-information/35693

---

## Post #1 by @eNable_Polska (2024-04-23 18:56 UTC)

<p>I cannot run the Monai Auto3dseg module. Python package information gives me the following information:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:\Users\krzys\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py", line 3255, in tryWithErrorDisplay
    yield
  File "C:/Users/krzys/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules/MONAIAuto3DSeg.py", line 588, in onPackageInfoUpdate
    self.ui.packageInfoTextBrowser.plainText = self.logic.installedMONAIPythonPackageInfo().rstrip()
  File "C:/Users/krzys/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/MONAIAuto3DSeg/lib/Slicer-5.6/qt-scripted-modules/MONAIAuto3DSeg.py", line 1031, in installedMONAIPythonPackageInfo
    versionInfo = subprocess.check_output([shutil.which("PythonSlicer"), "-m", "pip", "show", "MONAI"]).decode()
  File "C:\Users\krzys\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\subprocess.py", line 424, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "C:\Users\krzys\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\subprocess.py", line 528, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['C:/Users/krzys/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'show', 'MONAI']' returned non-zero exit status 1.</code></pre>
<p>Windows 10 system, nvidia graphics card, current drivers, AMD processor, 64 Gb RAM<br>
What could cause such an error?</p>

---

## Post #2 by @lassoan (2024-04-24 01:13 UTC)

<p>The MONAIAuto3DSeg extension is only supported for the very latest Slicer Preview Release (revision 32818 and later).</p>

---
