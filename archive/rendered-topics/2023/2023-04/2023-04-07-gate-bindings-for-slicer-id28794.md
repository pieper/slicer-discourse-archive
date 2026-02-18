# Gate bindings for Slicer

**Topic ID**: 28794
**Date**: 2023-04-07
**URL**: https://discourse.slicer.org/t/gate-bindings-for-slicer/28794

---

## Post #1 by @Alex_Vergara (2023-04-07 10:26 UTC)

<p>I’m trying to use <a href="https://github.com/OpenGATE/opengate" rel="noopener nofollow ugc">Gate</a> inside Slicer within my module <a href="https://gitlab.com/opendose/opendose3d" rel="noopener nofollow ugc">OpenDose3D</a>.</p>
<p>However, it’s being a bit difficult to install gate as a pip package.</p>
<pre><code class="lang-auto">slicer.util.pip_install("opengate")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\alex.vergara.F-P-PHYS-02\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3571, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\alex.vergara.F-P-PHYS-02\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3533, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\alex.vergara.F-P-PHYS-02\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3502, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/alex.vergara.F-P-PHYS-02/AppData/Local/NA-MIC/Slicer 5.2.1/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'opengate']' returned non-zero exit status 1.`
</code></pre>
<p>May someone guide me as why it does not install? I could maybe try to guide the Gate developers to build some wheel, but I don’t know if that will be enough.</p>
<p>EDIT: I have reported this issue in <a href="https://github.com/OpenGATE/opengate/issues/146" rel="noopener nofollow ugc">gate page</a></p>

---

## Post #2 by @Alex_Vergara (2023-04-07 20:02 UTC)

<p>In Linux opengate installs but when started it gave this error:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import opengate as gate
opengate_core is not detected. Be sure to execute these lines before to run python:
export LD_LIBRARY_PATH=/home/alex/Programas/Slicer-5.3.0-2023-03-16-linux-amd64/bin/../lib/Python/lib/python3.9/site-packages/opengate_core.libs:${LD_LIBRARY_PATH}
export LD_PRELOAD=/home/alex/Programas/Slicer-5.3.0-2023-03-16-linux-amd64/bin/../lib/Python/lib/python3.9/site-packages/opengate_core.libs/libG4processes-9232ba54.so:/home/alex/Programas/Slicer-5.3.0-2023-03-16-linux-amd64/bin/../lib/Python/lib/python3.9/site-packages/opengate_core.libs/libG4geometry-fbd76286.so:${LD_PRELOAD}
</code></pre>
<p>Is there any way to set up these variables for Slicer?</p>

---

## Post #3 by @lassoan (2023-04-08 20:39 UTC)

<p>Fixing the packaging of Gate is not really a feature request for Slicer but a bug report/feature request for Gate maintainers. I’ll change the category of the post accordingly (we can change it again if the discussion leads to the conclusion that there is some missing feature in Slicer).</p>
<p>Use Slicer-5.2.2 and try again, it may print more information about the error that occurred. You can also run <code>PythonSlicer -m pip install... </code> to see more details.</p>

---
