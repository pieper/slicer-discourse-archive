# Problem installing radiology app of MonaiLabel in conda environment

**Topic ID**: 42567
**Date**: 2025-04-15
**URL**: https://discourse.slicer.org/t/problem-installing-radiology-app-of-monailabel-in-conda-environment/42567

---

## Post #1 by @chz31 (2025-04-15 06:13 UTC)

<p>Hi,</p>
<p>I tried to reinstall monailabel in a fresh conda environment in Windows 11. Previously, I successfully installed monai and radiology app in a conda envrionment and ran in Slicer with no issue, but it suddenly could not locate the radiology app anymore.</p>
<p>pip install monailabel had no issue. However, installing the radiology app<code> monailabel apps --name radiology --download --output .</code> returned error below:</p>
<pre><code class="lang-auto">Using PYTHONPATH=C:\Users\chi.zhang\AppData\Local\anaconda3\envs;C:\Users\chi.zhang\SOFA\v24.06.00\plugins\SofaPython3\lib\python3\site-packages;C:\Users\chi.zhang\SOFA\external_plugins\STLIB\build\lib\python3\site-packages;
""
Traceback (most recent call last):
  File "C:\Users\chi.zhang\AppData\Local\anaconda3\envs\monai_py39\lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Users\chi.zhang\AppData\Local\anaconda3\envs\monai_py39\lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\Users\chi.zhang\AppData\Local\anaconda3\envs\monai_py39\lib\site-packages\monailabel\main.py", line 24, in &lt;module&gt;
    from monailabel.config import settings
  File "C:\Users\chi.zhang\AppData\Local\anaconda3\envs\monai_py39\lib\site-packages\monailabel\config.py", line 23, in &lt;module&gt;
    class Settings(BaseSettings):
  File "C:\Users\chi.zhang\AppData\Local\anaconda3\envs\monai_py39\lib\site-packages\monailabel\config.py", line 109, in Settings
    if is_package_installed("SAM-2")
  File "C:\Users\chi.zhang\AppData\Local\anaconda3\envs\monai_py39\lib\site-packages\monailabel\config.py", line 20, in is_package_installed
    return name in sorted(x.name for x in distributions())
  File "C:\Users\chi.zhang\AppData\Local\anaconda3\envs\monai_py39\lib\site-packages\monailabel\config.py", line 20, in &lt;genexpr&gt;
    return name in sorted(x.name for x in distributions())
AttributeError: 'PathDistribution' object has no attribute 'name'
</code></pre>
<p>Can someone give me some suggestions?</p>

---

## Post #2 by @chz31 (2025-04-15 06:33 UTC)

<p>I found this commit <a href="https://github.com/Project-MONAI/MONAILabel/commit/30e97b49ce02efd0e897c55f874b5c80bf27c7aa" rel="noopener nofollow ugc">30e97b4</a> and updated line 20 of monailbel/config.py. It appeared everything worked now!</p>

---
