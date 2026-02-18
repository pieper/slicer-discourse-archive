# I'm getting not a useful error when I try to start Slicer Jupyter kernel, how to debug?

**Topic ID**: 13530
**Date**: 2020-09-17
**URL**: https://discourse.slicer.org/t/im-getting-not-a-useful-error-when-i-try-to-start-slicer-jupyter-kernel-how-to-debug/13530

---

## Post #1 by @myousefi2016 (2020-09-17 16:04 UTC)

<p>I’m using Slicer 4.10 on our cluster that has Centos8. It’s a headless server and I’m able successfully to run Slicer and even its graphical interface by using Xvfb. The problem is that I want to use Slicer in Jupyter notebook. I installed the extension and installed the kernel. This is my <code>kernel.json</code> file:</p>
<pre><code class="lang-auto">{
    "display_name": "Slicer 4.10",
    "language" : "python",
    "argv": [
	"xvfb-run",
	"-a",
        "/home/yousefi/Slicer-4.10.2-linux-amd64/bin/../Slicer",
        "--no-splash",
        "--python-code",
        "connection_file=r'{connection_file}'; print('Jupyter connection file: ['+connection_file+']'); slicer.modules.jupyterkernel.startKernel(connection_file);slicer.util.mainWindow().showMinimized()"
    ]
}
</code></pre>
<p>When I’m trying to check the kernel by using:</p>
<pre><code class="lang-auto">jupyter-kernel --kernel=slicer-4.10
</code></pre>
<p>I’m seeing this error which is not helpful at all:</p>
<pre><code class="lang-auto">[KernelApp] Starting kernel 'slicer-4.10'
[KernelApp] Connection file: /home/yousefi/.local/share/jupyter/runtime/kernel-562c7160-c8ee-47a3-a89c-92bba771b660.json
[KernelApp] To connect a client: --existing kernel-562c7160-c8ee-47a3-a89c-92bba771b660.json
/home/yousefi/Slicer-4.10.2-linux-amd64/bin/../Slicer: /software/spackages/linux-centos8-x86_64/gcc-8.3.1/anaconda3-2020.07-4obfocw3kpymwz7obsjukroelfwutobz/lib/libuuid.so.1: no version information available (required by /lib64/libSM.so.6)
/home/yousefi/Slicer-4.10.2-linux-amd64/bin/SlicerApp-real: /software/spackages/linux-centos8-x86_64/gcc-8.3.1/anaconda3-2020.07-4obfocw3kpymwz7obsjukroelfwutobz/lib/libuuid.so.1: no version information available (required by /lib64/libSM.so.6)
/home/yousefi/Slicer-4.10.2-linux-amd64/bin/SlicerApp-real: /software/spackages/linux-centos8-x86_64/gcc-8.3.1/anaconda3-2020.07-4obfocw3kpymwz7obsjukroelfwutobz/lib/libuuid.so.1: no version information available (required by /lib64/libblkid.so.1)
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/local_scratch/pbs.440991.pbs02/runtime-yousefi'
"Failed to create temporary directory" "/local_scratch/pbs.435439.pbs02/Slicer-yousefi"
"Failed to create temporary directory" "/local_scratch/pbs.435439.pbs02/Slicer-yousefi"
"Failed to create temporary directory" "/local_scratch/pbs.435439.pbs02/Slicer-yousefi"
"Failed to create temporary directory" "/local_scratch/pbs.435439.pbs02/Slicer-yousefi"
Switch to module:  "Welcome"
Jupyter connection file: [/home/yousefi/.local/share/jupyter/runtime/kernel-562c7160-c8ee-47a3-a89c-92bba771b660.json]
error: [/home/yousefi/Slicer-4.10.2-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>The error at the end just says <code>SlicerApp-real</code> exit abnormally. Note that Slicer works perfectly fine and I’m even able to run my Python code. The only problem is that Slicer Jupyter kernel does not start. Any idea how to fix it? Thanks!</p>

---

## Post #2 by @lassoan (2020-09-17 16:06 UTC)

<p>Could you try if it works with latest Slicer Preview Release? (it is recommended anyway, as it has huge Jupyter support improvements)</p>

---

## Post #3 by @myousefi2016 (2020-09-17 16:42 UTC)

<p>I tried the latest preview release version 4.11 and get the same error. Any idea what’s wrong here?</p>

---

## Post #4 by @myousefi2016 (2020-09-17 17:09 UTC)

<p>I’m not sure if it helps or not but this command also fails with the same error:</p>
<pre><code class="lang-auto">xvfb-run -a /home/yousefi/Slicer-4.11.0-2020-09-16-linux-amd64/bin/PythonSlicer -m pip install --upgrade pillow --force-reinstall
</code></pre>

---

## Post #5 by @myousefi2016 (2020-09-17 17:42 UTC)

<p>Finally, I think I found something. When I run <code>PythonSlicer</code> like this:</p>
<pre><code class="lang-auto">xvfb-run -a /home/yousefi/Slicer-4.11.0-2020-09-16-linux-amd64/bin/PythonSlicer
</code></pre>
<p>and then in the console, I try these Python commands:</p>
<pre><code class="lang-auto">Python 3.6.7 (default, Sep 17 2020, 03:03:22) 
[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import os
&gt;&gt;&gt; os.system('pip install --upgrade pillow --force-reinstall')
</code></pre>
<p>I got this error:</p>
<pre><code class="lang-auto">Fatal Python error: init_import_size: Failed to import the site module
Python runtime state: initialized
Traceback (most recent call last):
  File "/home/yousefi/Slicer-4.11.0-2020-09-16-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 553, in &lt;module&gt;
    main()
  File "/home/yousefi/Slicer-4.11.0-2020-09-16-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 539, in main
    known_paths = addusersitepackages(known_paths)
  File "/home/yousefi/Slicer-4.11.0-2020-09-16-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 282, in addusersitepackages
    user_site = getusersitepackages()
  File "/home/yousefi/Slicer-4.11.0-2020-09-16-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 258, in getusersitepackages
    user_base = getuserbase() # this will also set USER_BASE
  File "/home/yousefi/Slicer-4.11.0-2020-09-16-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 248, in getuserbase
    USER_BASE = get_config_var('userbase')
  File "/home/yousefi/Slicer-4.11.0-2020-09-16-linux-amd64/lib/Python/lib/python3.6/sysconfig.py", line 601, in get_config_var
    return get_config_vars().get(name)
  File "/home/yousefi/Slicer-4.11.0-2020-09-16-linux-amd64/lib/Python/lib/python3.6/sysconfig.py", line 550, in get_config_vars
    _init_posix(_CONFIG_VARS)
  File "/home/yousefi/Slicer-4.11.0-2020-09-16-linux-amd64/lib/Python/lib/python3.6/sysconfig.py", line 421, in _init_posix
    _temp = __import__(name, globals(), locals(), ['build_time_vars'], 0)
ModuleNotFoundError: No module named '_sysconfigdata__linux_x86_64-linux-gnu'
256
</code></pre>
<p>Any idea what’s missing here that says no module named <code>'_sysconfigdata__linux_x86_64-linux-gnu' 256'</code>?</p>

---

## Post #6 by @lassoan (2020-09-17 18:27 UTC)

<p>This is probably due to mixup of different Python environments.</p>
<p>We have encountered this problem when we simply wanted to run a terminal in Slicer’s Python environment:</p><aside class="quote quote-modified" data-post="8" data-topic="13265">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/crash-when-initializing-app-built-and-run-from-ubuntu-20-04/13265/8">Crash when initializing app built and run from Ubuntu 20.04</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Knowing that the crash occurred in libc is not very useful. Can you get a stack trace? This may help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Analyze_a_segmentation_fault">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Analyze_a_segmentation_fault</a> 
I’ve tried to start Slicer in gdb on Linux by following <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#GDB_debug_with_launch_arguments">these instructions</a>, I get the error below. When I try to debug using VS Code, I get the same error. 
osboxes@osboxes:~/D/Slicer-SuperBuild-Release/Slicer-build$ ./Slicer --launch /usr/bin/gnome-terminal
Fatal Python error:…
  </blockquote>
</aside>

<p><a class="mention" href="/u/jcfr">@jcfr</a> can you help us here? This user site packages/sysconfigdata issues has come up again. Should we add <code>Py_NoSiteFlag=1</code> in Slicer as suggested <a href="https://stackoverflow.com/questions/49921336/sysconfigdata-error-when-trying-to-freeze-a-python-3-6-5-application">here</a> and <a href="https://github.com/conda-forge/python-feedstock/issues/220">here</a>? (although I’m not sure how that could fix launching of a terminal or gdb)</p>

---

## Post #7 by @myousefi2016 (2020-09-18 01:52 UTC)

<p>Do you think if I build Slicer from scratch in our cluster with our system installed Python this error will go away?</p>

---

## Post #8 by @lassoan (2020-09-18 14:29 UTC)

<p>I’ve found a much better solution! Run jupyter notebook server from Slicer’s Python environment to resolve the Python site package conflict issue. We need to get <a href="https://github.com/Slicer/Slicer/pull/5190">this change</a> integrated first and then you can start jupyter notebook server from Slicer’s Python environment using <code>PythonSlicer.exe -m notebook</code>.</p>

---

## Post #9 by @myousefi2016 (2020-09-20 06:17 UTC)

<p>I tried the latest preview release built on 09/19/2020 revision 29380 and still have the same problem. Pretty much nothing is changed. I tried <code>PythonSlicer -m notebook</code> but it says <code>No module named notebook</code> despite the fact I already installed SlicerJupyter extension.</p>

---

## Post #10 by @lassoan (2020-09-20 14:12 UTC)

<p>SlicerJupyter extension does not install the jupyter package in Slicer’s Python environment (you might not want to use it and it is a huge package). If you want to run the jupyter notebook server in Slicer’s Python environment then run the following commands after installing SlicerJupyter:</p>
<pre><code class="lang-python"># Install jupyter
pip_install('jupyter --no-warn-script-location')
# Create Slicer kernel
slicer.modules.jupyterkernel.updateKernelSpec()
# Install kernel
import jupyter_client
jupyter_client.kernelspec.KernelSpecManager().install_kernel_spec(slicer.modules.jupyterkernel.resourceFolderPath(), user=True, replace=True)
</code></pre>
<p>After that, you can start the notebook server by running this command in a terminal:</p>
<pre><code>PythonSlicer -m notebook</code></pre>

---

## Post #11 by @myousefi2016 (2020-09-20 17:02 UTC)

<p>I run <code>pip_install('jupyter --no-warn-script-location')</code> and I received this error:</p>
<pre><code class="lang-auto">[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux2
&gt;&gt;&gt; pip_install('jupyter --no-warn-script-location')
/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/bin/../bin/PythonSlicer: /software/spackages/linux-centos8-x86_64/gcc-8.3.1/anaconda3-2020.07-4obfocw3kpymwz7obsjukroelfwutobz/lib/libuuid.so.1: no version information available (required by /lib64/libSM.so.6)
error: [/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/bin/./python-real] exit abnormally - Report the problem.
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/bin/Python/slicer/util.py", line 2569, in pip_install
    _executePythonModule('pip', args)
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/bin/Python/slicer/util.py", line 2545, in _executePythonModule
    logProcessOutput(proc)
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/bin/Python/slicer/util.py", line 2517, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'jupyter', '--no-warn-script-location']' returned non-zero exit status 1.
</code></pre>

---

## Post #12 by @lassoan (2020-09-20 17:22 UTC)

<blockquote>
<p>/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/bin/…/bin/PythonSlicer: /software/spackages/linux-centos8-x86_64/gcc-8.3.1/anaconda3-2020.07-4obfocw3kpymwz7obsjukroelfwutobz/lib/libuuid.so.1: no version information available (required by /lib64/libSM.so.6)</p>
</blockquote>
<p>I don’t know how or why anaconda’s libuuid is found instead of the system libuuid. Can you check if your environment has some conda variables? Was this Slicer started from some virtual Python environment?</p>
<p>Does <code>./PythonSlicer -m jupyter --no-warn-script-location</code> work from a terminal?</p>

---

## Post #13 by @myousefi2016 (2020-09-20 17:33 UTC)

<p>Yes that happened because I had an anaconda module loaded in my environment. I just unload that anaconda module and your above script worked fine. Now, I’m running <code>PythonSlicer -m notebook</code> and I’m getting this error, which I think is on our cluster’s fault that has a firewall:</p>
<pre><code class="lang-auto">[yousefi@node1266 bin]$ xvfb-run -a ./PythonSlicer -m notebook
Traceback (most recent call last):
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/site-packages/notebook/__main__.py", line 5, in &lt;module&gt;
    app.launch_new_instance()
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/site-packages/jupyter_core/application.py", line 270, in launch_instance
    return super(JupyterApp, cls).launch_instance(argv=argv, **kwargs)
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/site-packages/traitlets/config/application.py", line 663, in launch_instance
    app.initialize(argv)
  File "&lt;decorator-gen-7&gt;", line 2, in initialize
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/site-packages/traitlets/config/application.py", line 87, in catch_config_error
    return method(app, *args, **kwargs)
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/site-packages/notebook/notebookapp.py", line 2037, in initialize
    self.init_webapp()
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/site-packages/notebook/notebookapp.py", line 1711, in init_webapp
    success = self._bind_http_server()
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/site-packages/notebook/notebookapp.py", line 1718, in _bind_http_server
    return self._bind_http_server_unix() if self.sock else self._bind_http_server_tcp()
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/site-packages/notebook/notebookapp.py", line 1744, in _bind_http_server_tcp
    self.http_server.listen(port, self.ip)
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/site-packages/tornado/tcpserver.py", line 151, in listen
    sockets = bind_sockets(port, address=address)
  File "/home/yousefi/Slicer-4.11.0-2020-09-19-linux-amd64/lib/Python/lib/python3.6/site-packages/tornado/netutil.py", line 174, in bind_sockets
    sock.bind(sockaddr)
OSError: [Errno 99] Cannot assign requested address
</code></pre>
<p>Is there any way to start notebook and workaround the firewall?</p>

---

## Post #14 by @myousefi2016 (2020-09-20 17:36 UTC)

<p>Never mind. I solved that problem and it works fine! I just run this:</p>
<pre><code class="lang-auto">PythonSlicer -m notebook --ip=127.0.0.1 --port=8888
</code></pre>
<p>Yay!!!</p>

---
