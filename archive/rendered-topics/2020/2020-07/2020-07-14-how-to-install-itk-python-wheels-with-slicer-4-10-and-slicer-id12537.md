# How to install ITK python wheels with Slicer 4.10 and Slicer 4.11?

**Topic ID**: 12537
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/how-to-install-itk-python-wheels-with-slicer-4-10-and-slicer-4-11/12537

---

## Post #1 by @siaeleni (2020-07-14 16:44 UTC)

<p>Hello,</p>
<p>I have two questions related to itk installation:</p>
<ol>
<li>I want to install itk at 4.10 Slicer version but gives me error:<br>
Command “python setup.py egg_info” failed with error code 1 in c:\users\siael\appdata\local\temp\pip-install-law80k\itk\</li>
</ol>
<blockquote>
<p>from pip._internal import main as pipmain<br>
pipmain([“install”, “itk”])</p>
</blockquote>
<ol start="2">
<li>Is it possible to install a 4.XX version of itk for 4.11 version of Slicer?</li>
</ol>
<p>Thanks</p>

---

## Post #2 by @jcfr (2020-07-14 18:48 UTC)

<aside class="quote no-group" data-username="siaeleni" data-post="1" data-topic="12537">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>I want to install itk at 4.10 Slicer version</p>
</blockquote>
</aside>
<p>Since Slicer 4.10.2 is built against python 2.7, and there no ITK wheels for python 2.7 for latest version of ITK you would have to do this:</p>
<pre data-code-wrap="python"><code class="lang-python">from pip._internal import main as pipmain
pipmain(["install", "--no-cache-dir", "itk==4.13.2"])
</code></pre>
<aside class="quote no-group" data-username="siaeleni" data-post="1" data-topic="12537">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>Is it possible to install a 4.XX version of itk for 4.11 version of Slicer?</p>
</blockquote>
</aside>
<p>You could try approach described above.</p>
<p>Out of curiosity, is there something that should be fixed in ITK 5.x ? What motivate the use of an older ITK version ?</p>

---

## Post #3 by @siaeleni (2020-07-14 19:17 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>,<br>
Thanks for the information.</p>
<p>No, there is nothing wrong that I have noticed so far.<br>
I was wondering if I have a .exe file that I want to execute it through Slicer with different targeting vtk version (8.1.0 instead of 8.2.0), would that be an issue or the versions (itk/vtk) should much always?</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2020-07-14 19:37 UTC)

<p>That should be no problem at all. On Windows, you just need to make sure that if that exe uses VTK or ITK DLLs then those DLLs are in the same folder as the exe file and that the folder is <em>not</em> added to Slicer’s module paths. Rules might be slightly different on Linux and Mac.</p>

---

## Post #5 by @siaeleni (2020-07-14 21:28 UTC)

<p>If by term Slicer’s module path you mean the “Additional module path” under Application Settings, then no. Thanks Andras!</p>

---

## Post #6 by @lassoan (2020-07-14 21:43 UTC)

<p>Yes, I meant standard module paths (within Slicer install folder) and any additional module paths that you specify in application settings.</p>

---

## Post #7 by @siaeleni (2020-07-16 02:30 UTC)

<p>Hello again,</p>
<p>I am trying to install itk 4.13.0 version on Slicer 4.11 (2020-06-24) but I get the following error:</p>
<blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>from pip.<em>internal import main as pipmain<br>
pipmain([“install”, “–no-cache-dir”, “itk==4.13.0”])<br>
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.<br>
Please see <a href="https://github.com/pypa/pip/issues/5599" class="inline-onebox" rel="noopener nofollow ugc">ImportError in system pip wrappers after an upgrade · Issue #5599 · pypa/pip · GitHub</a> for advice on fixing the underlying issue.<br>
To avoid this problem you can invoke Python with ‘-m pip’ instead of running pip directly.<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File "C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal_<em>init</em></em>.py", line 17, in main<br>
return <em>wrapper(args)<br>
File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\utils\entrypoints.py”, line 31, in <em>wrapper<br>
return main(args)<br>
File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\cli\main.py”, line 73, in main<br>
command = create_command(cmd_name, isolated=(“–isolated” in cmd_args))<br>
File "C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\commands_<em>init</em></em>.py", line 104, in create_command<br>
module = importlib.import_module(module_path)<br>
File "C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\importlib_<em>init</em></em>.py", line 126, in import_module<br>
return _bootstrap._gcd_import(name[level:], package, level)<br>
File “”, line 994, in _gcd_import<br>
File “”, line 971, in _find_and_load<br>
File “”, line 955, in _find_and_load_unlocked<br>
File “”, line 665, in _load_unlocked<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\commands\install.py”, line 24, in <br>
from pip._internal.cli.req_command import RequirementCommand, with_cleanup<br>
File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\cli\req_command.py”, line 16, in <br>
from pip._internal.index.package_finder import PackageFinder<br>
File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\index\package_finder.py”, line 21, in <br>
from pip._internal.index.collector import parse_links<br>
File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\index\collector.py”, line 25, in <br>
from pip.<em>internal.vcs import is_url, vcs<br>
File "C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\vcs_<em>init</em></em>.py", line 9, in <br>
import pip._internal.vcs.subversion  # noqa: F401<br>
File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\vcs\subversion.py”, line 334, in <br>
vcs.register(Subversion)<br>
File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\vcs\versioncontrol.py”, line 221, in register<br>
self._registry[cls.name] = cls()<br>
File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\vcs\subversion.py”, line 192, in <strong>init</strong><br>
use_interactive = is_console_interactive()<br>
File “C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-24\lib\Python\Lib\site-packages\pip_internal\utils\misc.py”, line 875, in is_console_interactive<br>
return sys.stdin is not None and sys.stdin.isatty()<br>
AttributeError: ‘PythonQtStdInRedirect’ object has no attribute ‘isatty’</p>
</blockquote>
</blockquote>
</blockquote>
</blockquote>
<p>Do you have any idea?</p>
<p>Thanks</p>

---

## Post #8 by @lassoan (2020-07-16 03:08 UTC)

<p>I don’t know how exactly ITK Python package is created, but since ITK is already bundled with Slicer, if you install a different version in side Slicer’s environment then there could be version conflicts. You have several options:</p>
<ul>
<li>don’t use old ITK, simply use current version: <code>pip_install('itk')</code>
</li>
<li>install old ITK in a different Python virtual environment, not in Slicer’s</li>
<li>use SimpleITK bundled with Slicer</li>
</ul>

---
