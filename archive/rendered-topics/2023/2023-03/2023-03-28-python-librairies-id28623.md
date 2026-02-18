# Python librairies

**Topic ID**: 28623
**Date**: 2023-03-28
**URL**: https://discourse.slicer.org/t/python-librairies/28623

---

## Post #1 by @Nicolas_Tempier (2023-03-28 13:22 UTC)

<p>Hello everyone,<br>
I have a little misunderstanding because I managed to install a python library "openslide-python==1.2.0<br>
"on my machine but when I try to install it on another machine on slicer, it returns the following error:<br>
Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “/home/eric.bardinet/Slicer-5.2.2-linux-amd64/bin/Python/slicer/util.py”, line 3578, in pip_install</p>
<pre><code>_executePythonModule('pip', args)
</code></pre>
<p>File “/home/eric.bardinet/Slicer-5.2.2-linux-amd64/bin/Python/slicer/util.py”, line 3540, in _executePythonModule</p>
<pre><code>logProcessOutput(proc)
</code></pre>
<p>File “/home/eric.bardinet/Slicer-5.2.2-linux-amd64/bin/Python/slicer/util.py”, line 3509, in logProcessOutput</p>
<pre><code>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
</code></pre>
<p>subprocess.CalledProcessError: Command ‘[’/home/nicolas.tempier/Slicer-5.2.2-linux-amd64/bin/…/bin/PythonSlicer’, ‘-m’, ‘pip’, ‘install’, ‘openslide-python’]’ returned non-zero exit status 1.</p>
<p>i installed it using pip_install(‘openslide-python’) and it worked before …<br>
I tried pip_install(‘pip install ugrade pip’)<br>
any ideas please ?</p>

---

## Post #2 by @lassoan (2023-03-28 13:56 UTC)

<p>Unfortunately, <code>openslide-python</code> is a poorly implemented package, which <a href="https://openslide.org/api/python/#installing">requires manual installation of additional components</a>.</p>
<p>We implemented automatic installation of openslide binaries on Windows in <a href="https://github.com/gaoyi/SlicerBigImage">BigImage extension</a>. You could make your extension depend on BigImage extension, or - to simplify things - improve and extend BigImage extension to do what you need. For example, it would be nice if you could implement automatic openslide installation for linux and/or macos as well.</p>
<p>Note that <code>pip_install</code> is the officially supported method of Python package installation in Slicer, as we may need to add extra options in the future to customize the behavior of pip in Slicer.</p>

---
