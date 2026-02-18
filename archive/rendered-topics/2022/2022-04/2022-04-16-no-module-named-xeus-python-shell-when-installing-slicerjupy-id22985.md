# No module named 'xeus_python_shell' when installing SlicerJupyter on SlicerCAT

**Topic ID**: 22985
**Date**: 2022-04-16
**URL**: https://discourse.slicer.org/t/no-module-named-xeus-python-shell-when-installing-slicerjupyter-on-slicercat/22985

---

## Post #1 by @keri (2022-04-16 18:20 UTC)

<p>Hi,</p>
<p>To build SlicerJupyter I use the hints from the <a href="https://discourse.slicer.org/t/failures-due-to-build-order-of-slicer-cat-with-superbuild-remote-modules/21841/11">link</a></p>
<p>After building SlicerCAT with SlicerJupyter I click on <code>Start Jupyter Server</code> button and after a while the Jupyter runs.</p>
<p>After new instances of SlicerCAT are launched by Jupyter I get an error:<br>
<code>ModuleNotFoundError: No module named 'xeus_python_shell'</code></p>
<p>and an error within Jupyter:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77921b7e8a754ceb641445d27c965ec9db52b978.png" alt="image" data-base62-sha1="h3LQRyNsxm997MFDuUfuxRIj4Q8" width="517" height="191"></p>
<p>After manually <code>pip install xeus_python_shell</code> it seems I can run SlicerJupyter but an error appear:</p>
<pre><code class="lang-auto">Failed to create history session in /home/kerim/.ipython/profile_default/history.sqlite. History will not be saved.
Traceback (most recent call last):
  File "/home/kerim/Documents/Colada/r/python-install/lib/python3.9/site-packages/IPython/core/history.py", line 546, in __init__
    self.new_session()
  File "/home/kerim/Documents/Colada/r/python-install/lib/python3.9/site-packages/decorator.py", line 232, in fun
    return caller(func, *(extras + args), **kw)
  File "/home/kerim/Documents/Colada/r/python-install/lib/python3.9/site-packages/IPython/core/history.py", line 60, in only_when_enabled
    return f(self, *a, **kw)
  File "/home/kerim/Documents/Colada/r/python-install/lib/python3.9/site-packages/IPython/core/history.py", line 571, in new_session
    cur = conn.execute("""INSERT INTO sessions VALUES (NULL, ?, NULL,
sqlite3.OperationalError: no such column: 
</code></pre>
<p>and for example <code>getNode('Some Node')</code> doesn’t work from Jupyter:<br>
<code>NameError: name 'getNode' is not defined</code></p>

---

## Post #2 by @lassoan (2022-04-17 03:34 UTC)

<p>It seems you connect to a stock Python kernel. Choose the Slicer kernel instead.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c59156e703e901841034b80d0656fe6aa46168ff.png" data-download-href="/uploads/short-url/sbLrTXjVWgxcEmPLBtpbHXZHo19.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c59156e703e901841034b80d0656fe6aa46168ff_2_657x500.png" alt="image" data-base62-sha1="sbLrTXjVWgxcEmPLBtpbHXZHo19" width="657" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c59156e703e901841034b80d0656fe6aa46168ff_2_657x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c59156e703e901841034b80d0656fe6aa46168ff_2_985x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c59156e703e901841034b80d0656fe6aa46168ff_2_1314x1000.png 2x" data-dominant-color="BFC0C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1337×1016 92.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @keri (2022-04-17 17:49 UTC)

<p>Thank you for response,</p>
<p>No I connect to the Slicer’s kernel:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a731053aec2e50733a90fc99acabbd27e49663dd.png" data-download-href="/uploads/short-url/nR2LkkiJA4HDgk2MGcuE8h6jfNr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a731053aec2e50733a90fc99acabbd27e49663dd_2_690x134.png" alt="image" data-base62-sha1="nR2LkkiJA4HDgk2MGcuE8h6jfNr" width="690" height="134" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a731053aec2e50733a90fc99acabbd27e49663dd_2_690x134.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a731053aec2e50733a90fc99acabbd27e49663dd_2_1035x201.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a731053aec2e50733a90fc99acabbd27e49663dd.png 2x" data-dominant-color="ECEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1232×241 45.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I just noticed that <code>getNode()</code> is not recognized but <code>a = slicer.util.getNode('F')</code> works fine. So I think that is ok.</p>
<p>But the above error <code>Failed to create history session</code> still exist.<br>
I should mention that I use <code>sqlite</code> built as a shared library…</p>
<p>Though the more important thing is the following:<br>
after installing SlicerCAT (using <code>cpack</code>) with SlicerJupyter I’m unable to run SlicerJupyter. After clicking on <code>Start Jupyter server</code> I get an error:</p>
<pre><code class="lang-auto">Switch to module:  "JupyterKernel"
QIODevice::read (QFile, "/home/kerim/.local/share/Trash/files/Colada-0.2.1.0-2022-04-17-linux-amd64/bin/../share/Colada-4.13/qt-loadable-modules/JupyterKernel/Colada-4.13/kernel-template.json"): device not open
QIODevice::read (QFile, "/home/kerim/.local/share/Trash/files/Colada-0.2.1.0-2022-04-17-linux-amd64/bin/../share/Colada-4.13/qt-loadable-modules/JupyterKernel/Colada-4.13/kernel-template.json"): device not open
Removing existing kernelspec in /home/kerim/.local/share/jupyter/kernels/colada-4.13
Installed kernelspec colada-4.13 in /home/kerim/.local/share/jupyter/kernels/colada-4.13
usage: jupyter.py [-h] [--version] [--config-dir] [--data-dir] [--runtime-dir]
                  [--paths] [--json] [--debug]
                  [subcommand]

Jupyter: Interactive Computing

positional arguments:
  subcommand     the subcommand to launch

optional arguments:
  -h, --help     show this help message and exit
  --version      show the versions of core jupyter packages and exit
  --config-dir   show Jupyter config dir
  --data-dir     show Jupyter data dir
  --runtime-dir  show Jupyter runtime dir
  --paths        show all Jupyter paths. Add --json for machine-readable
                 format.
  --json         output paths as machine-readable json
  --debug        output debug information about paths

Available subcommands: kernel kernelspec migrate run troubleshoot trust

Jupyter command `jupyter-lab` not found.
</code></pre>
<p>The file <code>/home/kerim/.local/share/Trash/files/Colada-0.2.1.0-2022-04-17-linux-amd64/bin/../share/Colada-4.13/qt-loadable-modules/JupyterKernel/Colada-4.13/kernel-template.json</code> exists and its content (opened with <code>gedit &lt;path&gt;</code>):</p>
<pre><code class="lang-auto">{
    "display_name": "{slicer_application_name} {slicer_version_major}.{slicer_version_minor}",
    "language" : "python",
    "argv": [
        "{slicer_launcher_executable}",
        "--no-splash",
        "--python-code",
        "connection_file=r'{connection_file}';print('JupyterConnectionFile:['+connection_file+']');slicer.modules.jupyterkernel.startKernel(connection_file);slicer.util.mainWindow().showMinimized()"
    ]
}
</code></pre>
<p>The content of the folder:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4849f4d0fdcb9d8747c9077e9ffabcb26a05be48.png" data-download-href="/uploads/short-url/ajuPmVhHXQOQMqLRiSzx8qeJiOI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4849f4d0fdcb9d8747c9077e9ffabcb26a05be48_2_690x263.png" alt="image" data-base62-sha1="ajuPmVhHXQOQMqLRiSzx8qeJiOI" width="690" height="263" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4849f4d0fdcb9d8747c9077e9ffabcb26a05be48_2_690x263.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4849f4d0fdcb9d8747c9077e9ffabcb26a05be48.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4849f4d0fdcb9d8747c9077e9ffabcb26a05be48.png 2x" data-dominant-color="3B3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">801×306 78.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And the permissions of <code>kernel-template.json</code>:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a86e0e10df75405427de979e0020b52b1f1935a.png" alt="image" data-base62-sha1="3MFoaWyc256Uvt3MGXWmJ9UixMC" width="479" height="432"></p>
<p>Ubuntu 20.04</p>

---

## Post #4 by @lassoan (2022-04-17 18:15 UTC)

<p>The kernel installation looks good (<code>Installed kernel spec... </code>). You can confirm this by seeing the Slicer kernel showing up in the list of kernels.</p>
<p>Maybe jupyter notebook server is not installed. Or maybe you just need to restart Slicer after installing it before it can be found. Restart the application and then try again. If does not help then pip_install jupyterlab:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerJupyter/blob/6a0ef21752c1d212478fd6e4e760780cb5da4149/JupyterNotebooks/JupyterNotebooks.py#L51">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerJupyter/blob/6a0ef21752c1d212478fd6e4e760780cb5da4149/JupyterNotebooks/JupyterNotebooks.py#L51" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerJupyter/blob/6a0ef21752c1d212478fd6e4e760780cb5da4149/JupyterNotebooks/JupyterNotebooks.py#L51" target="_blank" rel="noopener">Slicer/SlicerJupyter/blob/6a0ef21752c1d212478fd6e4e760780cb5da4149/JupyterNotebooks/JupyterNotebooks.py#L51</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="41" style="counter-reset: li-counter 40 ;">
            <li>      except:</li>
            <li>        needToInstall = True</li>
            <li>
            <li>    if needToInstall:</li>
            <li>      # Install required packages</li>
            <li>      import os</li>
            <li>      if os.name != 'nt':</li>
            <li>        # PIL may be corrupted on linux, reinstall from pillow</li>
            <li>        slicer.util.pip_install('--upgrade pillow --force-reinstall')</li>
            <li>
            <li class="selected">      slicer.util.pip_install("jupyter jupyterlab ipywidgets pandas ipyevents ipycanvas --no-warn-script-location")</li>
            <li>
            <li>    # Install Slicer Jupyter kernel</li>
            <li>    # Create Slicer kernel</li>
            <li>    slicer.modules.jupyterkernel.updateKernelSpec()</li>
            <li>    # Install Slicer kernel</li>
            <li>    import jupyter_client</li>
            <li>    jupyter_client.kernelspec.KernelSpecManager().install_kernel_spec(slicer.modules.jupyterkernel.kernelSpecPath(), user=True, replace=True)</li>
            <li>
            <li>class JupyterNotebooksTest(ScriptedLoadableModuleTest):</li>
            <li>  """</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @keri (2022-04-17 18:40 UTC)

<p>Didn’t help…</p>
<p>When I do <code>pip_install jupyterlab</code> I can see that the requirements already satisfied.<br>
After that I tried to <code> slicer.util.pip_install("jupyter jupyterlab ipywidgets pandas ipyevents ipycanvas --no-warn-script-location")</code><br>
And once again I got <code>requirements already satisfied</code>.</p>
<p>The same error I get:</p>
<pre><code class="lang-auto">QTextCursor::setPosition: Position '-2358' out of range
QTextCursor::setPosition: Position '-2358' out of range
QTextCursor::setPosition: Position '-2358' out of range
QIODevice::read (QFile, "/home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/bin/../share/Colada-4.13/qt-loadable-modules/JupyterKernel/Colada-4.13/kernel-template.json"): device not open
Removing existing kernelspec in /home/kerim/.local/share/jupyter/kernels/colada-4.13
Installed kernelspec colada-4.13 in /home/kerim/.local/share/jupyter/kernels/colada-4.13
usage: jupyter.py [-h] [--version] [--config-dir] [--data-dir] [--runtime-dir]
                  [--paths] [--json] [--debug]
                  [subcommand]

Jupyter: Interactive Computing

positional arguments:
  subcommand     the subcommand to launch

optional arguments:
  -h, --help     show this help message and exit
  --version      show the versions of core jupyter packages and exit
  --config-dir   show Jupyter config dir
  --data-dir     show Jupyter data dir
  --runtime-dir  show Jupyter runtime dir
  --paths        show all Jupyter paths. Add --json for machine-readable
                 format.
  --json         output paths as machine-readable json
  --debug        output debug information about paths

Available subcommands: kernel kernelspec migrate run troubleshoot trust

Jupyter command `jupyter-lab` not found.
</code></pre>
<p>Then I tried to launch app with <code>sudo</code> but still no progress</p>

---

## Post #6 by @keri (2022-04-17 18:48 UTC)

<p>Maybe some <code>...Settings.ini</code> is incorrect?</p>
<p>ColadaLauncherSettings.ini:</p>
<pre><code class="lang-auto">[General]
launcherNoSplashScreen=false
launcherSplashImagePath=&lt;APPLAUNCHER_DIR&gt;/bin/SplashScreen.png
launcherSplashScreenHideDelayMs=3000
additionalLauncherHelpShortArgument=-h
additionalLauncherHelpLongArgument=--help
additionalLauncherNoSplashArguments=--no-splash,--help,--version,--home,--program-path,--no-main-window,--settings-path,--temporary-path





[Application]
path=&lt;APPLAUNCHER_DIR&gt;/bin/ColadaApp-real
arguments=
name=Colada
revision=30783
organizationDomain=kitware.com
organizationName=Kitware, Inc.

[ExtraApplicationToLaunch]

designer/shortArgument=
designer/help=Start Qt designer using Slicer plugins
designer/path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../bin/designer-real
designer/arguments=


[Environment]
additionalPathVariables=QT_PLUGIN_PATH,PYTHONPATH,LibraryPaths

[LibraryPaths]
1\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../bin
2\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Colada-4.13
3\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Colada-4.13/cli-modules
4\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Colada-4.13/qt-loadable-modules
5\path=../lib/Colada-4.13/qt-loadable-modules
6\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Python/lib
7\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib
8\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Teem-1.12.0
9\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/PythonQt
10\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Python/lib/python3.9/site-packages/numpy/core
11\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Python/lib/python3.9/site-packages/numpy/lib
size=11

[Paths]
1\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../bin
2\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Colada-4.13/cli-modules
3\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Colada-4.13/qt-loadable-modules
size=3

[EnvironmentVariables]
SLICER_HOME=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/..
ITK_AUTOLOAD_PATH=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Colada-4.13/ITKFactories
PIP_REQUIRE_VIRTUALENV=0
SSL_CERT_FILE=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../share/Colada-4.13/Slicer.crt
HDF5_USE_FILE_LOCKING=FALSE
PYTHONHOME=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Python
PYTHONNOUSERSITE=1
PROJ_LIB=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../share/proj
GDAL_DATA=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../share/gdal



[QT_PLUGIN_PATH]
1\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/QtPlugins
size=1

[PYTHONPATH]
1\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Colada-4.13
2\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Colada-4.13/qt-scripted-modules
3\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Colada-4.13/qt-loadable-modules
4\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/vtkTeem
5\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../bin/Python
6\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Colada-4.13/qt-loadable-modules/Python
7\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Python/lib/python3.9
8\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Python/lib/python3.9/lib-dynload
9\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Python/lib/python3.9/site-packages
10\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/python3.9/site-packages
size=10
</code></pre>

---

## Post #7 by @lassoan (2022-04-17 19:10 UTC)

<p>There are two completely independent components, the jupyter server and the kernel.</p>
<p>The jupyter kernel is just Slicer started with a special command-line argument (that contains the connection file). The jupyter server knows about the Slicer kernel if the kernelspec file is registered into it. This part seems to work well.</p>
<p>The jupyter server can be any Python environment, requires pip installing and running jupyterlab (and a few extras if you want to have widgets). It is convenient if you don’t need to install another Python environment, that’s they the JupyterKernel Slicer modules uses Slicer’s Python environment for this. It seems that installation of JupyterLab fails or it is not found or not started correctly.</p>
<p>Maybe you could start everything from scratch, and then don’t try to automatically set up Jupyter using JupyterKernel Slicer module but instead install manually using <code>slicer.util.pip_install("jupyter jupyterlab ipywidgets pandas ipyevents ipycanvas --no-warn-script-location")</code> and see it you get any errors.</p>

---

## Post #8 by @keri (2022-04-17 23:38 UTC)

<p>Thank you for clarification,</p>
<p>I think I have found something:</p>
<p>I ran the command <code>./PythonSlicer -m jupyter --paths</code> from build tree (from build tree I can launch jupyter) and from install tree (after using cpack).</p>
<p>In build tree I get:</p>
<pre><code class="lang-auto">config:
    /home/kerim/.jupyter
    /home/kerim/Documents/Colada/r/python-install/etc/jupyter
    /usr/local/etc/jupyter
    /etc/jupyter
data:
    /home/kerim/.local/share/jupyter
    /home/kerim/Documents/Colada/r/python-install/share/jupyter
    /usr/local/share/jupyter
    /usr/share/jupyter
runtime:
    /home/kerim/.local/share/jupyter/runtime
</code></pre>
<p>All the paths from build tree exist.</p>
<p>And from install tree i get:</p>
<pre><code class="lang-auto">config:
    /home/kerim/.jupyter
    /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/bin/../lib/Python/etc/jupyter    # 'etc' doesn't exist
    /usr/local/etc/jupyter
    /etc/jupyter
data:
    /home/kerim/.local/share/jupyter
    /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/bin/../lib/Python/share/jupyter    # 'share' doesn't exist
    /usr/local/share/jupyter
    /usr/share/jupyter
runtime:
    /home/kerim/.local/share/jupyter/runtime
</code></pre>
<p>In build tree <code>etc</code> and <code>share</code> folders don’t exist. I think that may be the reason.</p>
<p>If you know how to control these path please let me know.<br>
For now I have a lack of knowledge of how the Jupyter staff is managed. I look in source code but have no luck yet.</p>

---

## Post #9 by @keri (2022-04-17 23:39 UTC)

<p>Also the command <code>./PythonSlicer -m jupyter --help</code> from build tree shows:</p>
<pre><code class="lang-auto">Available subcommands: bundlerextension console dejavu execute kernel kernelspec lab labextension labhub migrate nbclassic nbconvert nbextension notebook qtconsole run
server serverextension troubleshoot trust
</code></pre>
<p>and from install tree:</p>
<pre><code class="lang-auto">Available subcommands: kernel kernelspec migrate run troubleshoot trust
</code></pre>

---

## Post #10 by @keri (2022-04-18 00:00 UTC)

<p>I just uninstalled these packages using the command<code>./PythonSlicer -m pip uninstall jupyter jupyterlab ipywidgets pandas ipyevents ipycanvas -y</code><br>
andafter that I installed them back <code>./PythonSlicer -m pip install jupyter jupyterlab ipywidgets pandas ipyevents ipycanvas</code></p>
<p>After that I’m able to run JupyterSlicer.<br>
Here is the output of that command and it seems there is no any errors:</p>
<pre><code class="lang-auto">./PythonSlicer -m pip install jupyter jupyterlab ipywidgets pandas ipyevents ipycanvas
Collecting jupyter
  Using cached jupyter-1.0.0-py2.py3-none-any.whl (2.7 kB)
Collecting jupyterlab
  Using cached jupyterlab-3.3.4-py3-none-any.whl (8.7 MB)
Collecting ipywidgets
  Using cached ipywidgets-7.7.0-py2.py3-none-any.whl (123 kB)
Collecting pandas
  Using cached pandas-1.4.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7 MB)
Collecting ipyevents
  Using cached ipyevents-2.0.1-py2.py3-none-any.whl (130 kB)
Collecting ipycanvas
  Using cached ipycanvas-0.11.0-py2.py3-none-any.whl (255 kB)
Requirement already satisfied: nbconvert in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter) (6.5.0)
Requirement already satisfied: notebook in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter) (6.4.10)
Requirement already satisfied: ipykernel in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter) (6.13.0)
Requirement already satisfied: qtconsole in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter) (5.3.0)
Requirement already satisfied: jupyter-console in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter) (6.4.3)
Requirement already satisfied: nbclassic~=0.2 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab) (0.3.7)
Requirement already satisfied: jinja2&gt;=2.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab) (3.1.1)
Requirement already satisfied: tornado&gt;=6.1.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab) (6.1)
Requirement already satisfied: ipython in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab) (8.2.0)
Requirement already satisfied: jupyter-core in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab) (4.9.2)
Requirement already satisfied: packaging in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab) (21.3)
Requirement already satisfied: jupyter-server~=1.4 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab) (1.16.0)
Requirement already satisfied: jupyterlab-server~=2.10 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab) (2.12.0)
Requirement already satisfied: nbformat&gt;=4.2.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipywidgets) (5.3.0)
Requirement already satisfied: jupyterlab-widgets&gt;=1.0.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipywidgets) (1.1.0)
Requirement already satisfied: traitlets&gt;=4.3.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipywidgets) (5.1.1)
Requirement already satisfied: widgetsnbextension~=3.6.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipywidgets) (3.6.0)
Requirement already satisfied: ipython-genutils~=0.2.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipywidgets) (0.2.0)
Requirement already satisfied: pytz&gt;=2020.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from pandas) (2022.1)
Requirement already satisfied: numpy&gt;=1.18.5 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from pandas) (1.22.1)
Requirement already satisfied: python-dateutil&gt;=2.8.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from pandas) (2.8.2)
Requirement already satisfied: pillow&gt;=6.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipycanvas) (9.0.1)
Requirement already satisfied: jupyter-client&gt;=6.1.12 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipykernel-&gt;jupyter) (7.2.2)
Requirement already satisfied: matplotlib-inline&gt;=0.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipykernel-&gt;jupyter) (0.1.3)
Requirement already satisfied: psutil in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipykernel-&gt;jupyter) (5.9.0)
Requirement already satisfied: debugpy&gt;=1.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipykernel-&gt;jupyter) (1.6.0)
Requirement already satisfied: nest-asyncio in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipykernel-&gt;jupyter) (1.5.5)
Requirement already satisfied: backcall in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipython-&gt;jupyterlab) (0.2.0)
Requirement already satisfied: pickleshare in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipython-&gt;jupyterlab) (0.7.5)
Requirement already satisfied: decorator in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipython-&gt;jupyterlab) (5.1.1)
Requirement already satisfied: setuptools&gt;=18.5 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipython-&gt;jupyterlab) (60.9.3)
Requirement already satisfied: jedi&gt;=0.16 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipython-&gt;jupyterlab) (0.18.1)
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipython-&gt;jupyterlab) (3.0.29)
Requirement already satisfied: stack-data in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipython-&gt;jupyterlab) (0.2.0)
Requirement already satisfied: pexpect&gt;4.3 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipython-&gt;jupyterlab) (4.8.0)
Requirement already satisfied: pygments&gt;=2.4.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from ipython-&gt;jupyterlab) (2.11.2)
Requirement already satisfied: MarkupSafe&gt;=2.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jinja2&gt;=2.1-&gt;jupyterlab) (2.1.1)
Requirement already satisfied: terminado&gt;=0.8.3 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter-server~=1.4-&gt;jupyterlab) (0.13.3)
Requirement already satisfied: Send2Trash in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter-server~=1.4-&gt;jupyterlab) (1.8.0)
Requirement already satisfied: pyzmq&gt;=17 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter-server~=1.4-&gt;jupyterlab) (22.3.0)
Requirement already satisfied: argon2-cffi in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/python3.9/site-packages (from jupyter-server~=1.4-&gt;jupyterlab) (20.1.0)
Requirement already satisfied: anyio&gt;=3.1.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter-server~=1.4-&gt;jupyterlab) (3.5.0)
Requirement already satisfied: websocket-client in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter-server~=1.4-&gt;jupyterlab) (1.3.2)
Requirement already satisfied: prometheus-client in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyter-server~=1.4-&gt;jupyterlab) (0.14.1)
Requirement already satisfied: requests in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab) (2.27.1)
Requirement already satisfied: jsonschema&gt;=3.0.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab) (4.4.0)
Requirement already satisfied: entrypoints&gt;=0.2.2 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab) (0.4)
Requirement already satisfied: babel in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab) (2.9.1)
Requirement already satisfied: json5 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jupyterlab-server~=2.10-&gt;jupyterlab) (0.9.6)
Requirement already satisfied: notebook-shim&gt;=0.1.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from nbclassic~=0.2-&gt;jupyterlab) (0.1.0)
Requirement already satisfied: jupyterlab-pygments in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from nbconvert-&gt;jupyter) (0.2.2)
Requirement already satisfied: beautifulsoup4 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from nbconvert-&gt;jupyter) (4.11.1)
Requirement already satisfied: nbclient&gt;=0.5.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from nbconvert-&gt;jupyter) (0.6.0)
Requirement already satisfied: bleach in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from nbconvert-&gt;jupyter) (5.0.0)
Requirement already satisfied: mistune&lt;2,&gt;=0.8.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from nbconvert-&gt;jupyter) (0.8.4)
Requirement already satisfied: defusedxml in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from nbconvert-&gt;jupyter) (0.7.1)
Requirement already satisfied: tinycss2 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from nbconvert-&gt;jupyter) (1.1.1)
Requirement already satisfied: pandocfilters&gt;=1.4.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from nbconvert-&gt;jupyter) (1.5.0)
Requirement already satisfied: fastjsonschema in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from nbformat&gt;=4.2.0-&gt;ipywidgets) (2.15.3)
Requirement already satisfied: six&gt;=1.5 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from python-dateutil&gt;=2.8.1-&gt;pandas) (1.16.0)
Requirement already satisfied: pyparsing!=3.0.5,&gt;=2.0.2 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from packaging-&gt;jupyterlab) (3.0.7)
Requirement already satisfied: qtpy&gt;=2.0.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from qtconsole-&gt;jupyter) (2.0.1)
Requirement already satisfied: sniffio&gt;=1.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from anyio&gt;=3.1.0-&gt;jupyter-server~=1.4-&gt;jupyterlab) (1.2.0)
Requirement already satisfied: idna&gt;=2.8 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from anyio&gt;=3.1.0-&gt;jupyter-server~=1.4-&gt;jupyterlab) (3.3)
Requirement already satisfied: parso&lt;0.9.0,&gt;=0.8.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jedi&gt;=0.16-&gt;ipython-&gt;jupyterlab) (0.8.3)
Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,&gt;=0.14.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server~=2.10-&gt;jupyterlab) (0.18.1)
Requirement already satisfied: attrs&gt;=17.4.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from jsonschema&gt;=3.0.1-&gt;jupyterlab-server~=2.10-&gt;jupyterlab) (21.4.0)
Requirement already satisfied: ptyprocess&gt;=0.5 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from pexpect&gt;4.3-&gt;ipython-&gt;jupyterlab) (0.7.0)
Requirement already satisfied: wcwidth in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,&lt;3.1.0,&gt;=2.0.0-&gt;ipython-&gt;jupyterlab) (0.2.5)
Requirement already satisfied: cffi&gt;=1.0.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from argon2-cffi-&gt;jupyter-server~=1.4-&gt;jupyterlab) (1.15.0)
Requirement already satisfied: soupsieve&gt;1.2 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from beautifulsoup4-&gt;nbconvert-&gt;jupyter) (2.3.2.post1)
Requirement already satisfied: webencodings in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from bleach-&gt;nbconvert-&gt;jupyter) (0.5.1)
Requirement already satisfied: certifi&gt;=2017.4.17 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from requests-&gt;jupyterlab-server~=2.10-&gt;jupyterlab) (2021.10.8)
Requirement already satisfied: charset-normalizer~=2.0.0 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from requests-&gt;jupyterlab-server~=2.10-&gt;jupyterlab) (2.0.12)
Requirement already satisfied: urllib3&lt;1.27,&gt;=1.21.1 in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from requests-&gt;jupyterlab-server~=2.10-&gt;jupyterlab) (1.26.8)
Requirement already satisfied: asttokens in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from stack-data-&gt;ipython-&gt;jupyterlab) (2.0.5)
Requirement already satisfied: pure-eval in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from stack-data-&gt;ipython-&gt;jupyterlab) (0.2.2)
Requirement already satisfied: executing in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from stack-data-&gt;ipython-&gt;jupyterlab) (0.8.3)
Requirement already satisfied: pycparser in /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/lib/python3.9/site-packages (from cffi&gt;=1.0.0-&gt;argon2-cffi-&gt;jupyter-server~=1.4-&gt;jupyterlab) (2.21)
Installing collected packages: pandas, ipywidgets, jupyterlab, jupyter, ipyevents, ipycanvas
  WARNING: The scripts jlpm, jupyter-lab, jupyter-labextension and jupyter-labhub are installed in '/home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/lib/Python/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed ipycanvas-0.11.0 ipyevents-2.0.1 ipywidgets-7.7.0 jupyter-1.0.0 jupyterlab-3.3.4 pandas-1.4.2
</code></pre>
<p>Now <code>./PythonSlicer -m jupyter --help</code> tells me that <code>Available subcommands: kernel kernelspec lab labextension labhub migrate run troubleshoot trust</code>.<br>
The list is still smaller that that gives me from build tree but I can run <code>lab</code></p>
<p>The <code>./PythonSlicer -m jupyter --paths</code> now show me correct path and all of them exist:</p>
<pre><code class="lang-auto">config:
    /home/kerim/.jupyter
    /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/bin/../lib/Python/etc/jupyter
    /usr/local/etc/jupyter
    /etc/jupyter
data:
    /home/kerim/.local/share/jupyter
    /home/kerim/Documents/Colada/Colada-0.1.0-2022-04-17-linux-amd64/bin/../lib/Python/share/jupyter
    /usr/local/share/jupyter
    /usr/share/jupyter
runtime:
    /home/kerim/.local/share/jupyter/runtime
</code></pre>

---

## Post #11 by @lassoan (2022-04-18 00:32 UTC)

<p>If you want to distribute the Jupyter server (jupyterlab) then you can install jupyterlab along with all other Python packages here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerJupyter/blob/6a0ef21752c1d212478fd6e4e760780cb5da4149/SuperBuild/External_python-packages.cmake#L63">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerJupyter/blob/6a0ef21752c1d212478fd6e4e760780cb5da4149/SuperBuild/External_python-packages.cmake#L63" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerJupyter/blob/6a0ef21752c1d212478fd6e4e760780cb5da4149/SuperBuild/External_python-packages.cmake#L63" target="_blank" rel="noopener">Slicer/SlicerJupyter/blob/6a0ef21752c1d212478fd6e4e760780cb5da4149/SuperBuild/External_python-packages.cmake#L63</a></h4>



    <pre class="onebox">      <code class="lang-cmake">
        <ol class="start lines" start="53" style="counter-reset: li-counter 52 ;">
            <li># note: --force-reinstall ensures the python dependency is installed within</li>
            <li>#       this library's prefix for packaging.</li>
            <li>set(_install_jedi COMMAND ${CMAKE_COMMAND}</li>
            <li>    -E env</li>
            <li>      PYTHONNOUSERSITE=1</li>
            <li>      CC=${CMAKE_C_COMPILER}</li>
            <li>      PYTHONPATH=${python_sitepackages_DIR}</li>
            <li>      ${wrapper_script} ${PYTHON_EXECUTABLE} -m pip install</li>
            <li>        jedi==${${CMAKE_PROJECT_NAME}_jedi_VERSION}</li>
            <li>        argon2-cffi==${${CMAKE_PROJECT_NAME}_argon2_cffi_VERSION}</li>
            <li class="selected">        xeus-python-shell==${${CMAKE_PROJECT_NAME}_xeus_python_shell_VERSION}</li>
            <li>        ${_no_binary}</li>
            <li>        --prefix ${python_packages_DIR_NATIVE_DIR}</li>
            <li>        --force-reinstall</li>
            <li>        --no-warn-script-location</li>
            <li>  )</li>
            <li>
            <li>ExternalProject_Add(${proj}</li>
            <li>  ${${proj}_EP_ARGS}</li>
            <li>  SOURCE_DIR ${proj}</li>
            <li>  BUILD_IN_SOURCE 1</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The problem is that Jupyter server is very large (1GB?) so if you don’t always use it then it may not worth it.</p>
<p>If you plan to install Jupyter server on demand then you may need to ask help from <a class="mention" href="/u/jcfr">@jcfr</a>.</p>

---

## Post #12 by @keri (2022-04-18 00:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="22985">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you plan to install Jupyter server on demand</p>
</blockquote>
</aside>
<p>Could you please explain a little bit. Does it involves installing SlicerJupyter from <code>Extension Manager</code>?</p>
<p>Also I’m curious how to setup <code>Extension Manager</code> for SlicerCAT. Is there too much of work to make first “dirty” steps? If so I would postpone it but If it is pretty easy I would try it soon with SlicerJupyter.<br>
For now <code>Extension Manager</code> shows nothing</p>

---

## Post #13 by @lassoan (2022-04-18 01:03 UTC)

<p>The extensions infrastructure has been designed to allow private extensions servers. I remember seeing the instructions for setting up your own girder server with the required add-on to have your own private extension server (probably <a class="mention" href="/u/jcfr">@jcfr</a> wrote it, so if you cannot find it then you may ask him).</p>
<p>Once you have the server set up, you can configure your extension builds to upload packages to that server, and you can set the address of that server as default extension server in your custom application.</p>

---

## Post #14 by @keri (2022-04-18 01:06 UTC)

<p>Thank you very much!</p>
<p>I will try to find information on that<br>
That is important</p>

---
