# No module named 'clr' error

**Topic ID**: 22028
**Date**: 2022-02-17
**URL**: https://discourse.slicer.org/t/no-module-named-clr-error/22028

---

## Post #1 by @siaeleni (2022-02-17 18:44 UTC)

<p>Hello,<br>
I use a module and I get the following error when they try to import clr:<br>
“No module named ‘clr’ error”<br>
I tried to import pythonnet by using: pip_install(‘pythonnet’).<br>
But when I restart 3DSlicer I get the following pop up and<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a787b0048be2b79967523f1205663a131967694.png" alt="image" data-base62-sha1="1uCTYQVDnria1Ev13gncjDVzYSU" width="254" height="143"></p>
<p>Any idea that can be helful?<br>
Thank you</p>

---

## Post #2 by @jamesobutler (2022-02-17 20:20 UTC)

<p>Does installing <code>pythonnet</code> in a system python (not Python integrated into Slicer) such as Python 3.9.10 work for you? Do you have the same import error?</p>
<p>Slicer uses an integrated Python 3.9.10, but pypi says there is not an available whl for this python package for Python 3.9 (<a href="https://pypi.org/project/pythonnet/2.5.2/#files" class="inline-onebox" rel="noopener nofollow ugc">pythonnet · PyPI</a>) so it’s likely trying to build from source which can open you up to many errors if you don’t have all the required build tools.</p>

---

## Post #3 by @lassoan (2022-02-18 01:24 UTC)

<p>See the answer to this question in the pythonnet issue tracker:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/pythonnet/pythonnet/issues/1647#issuecomment-1001495228">
  <header class="source">

      <a href="https://github.com/pythonnet/pythonnet/issues/1647#issuecomment-1001495228" target="_blank" rel="noopener">github.com/pythonnet/pythonnet</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/pythonnet/pythonnet/issues/1647#issuecomment-1001495228" target="_blank" rel="noopener">Unable to pip3 install pythonnet</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-12-27" data-time="01:37:17" data-timezone="UTC">01:37AM - 27 Dec 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-12-27" data-time="02:17:02" data-timezone="UTC">02:17AM - 27 Dec 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/amrit-poudel" target="_blank" rel="noopener">
          <img alt="amrit-poudel" src="https://avatars.githubusercontent.com/u/12847183?v=4" class="onebox-avatar-inline" width="20" height="20">
          amrit-poudel
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">### Environment

-   Pythonnet version: 2.5.2
-   Python version: 3.9
-   Op<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">erating System: macosx 11.6
-   .NET Runtime:

### Details

-   pip3 install pythonnet==2.5.2 crashes with error. I see the 2.5.2 does support python 3.9, was wondering why it crashes on pip3 install. 

    _TODO_

-   What commands did you run to trigger this issue? If you can provide a
    [Minimal, Complete, and Verifiable example](http://stackoverflow.com/help/mcve)
    this will help us understand the issue.

```python
    print('TODO')
```

-  Collecting pythonnet==2.5.2
  Downloading pythonnet-2.5.2.tar.gz (1.9 MB)
     |████████████████████████████████| 1.9 MB 851 kB/s            
  Preparing metadata (setup.py) ... done
Collecting pycparser
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
     |████████████████████████████████| 118 kB 148 kB/s            
Building wheels for collected packages: pythonnet
  Building wheel for pythonnet (setup.py) ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/apoudel/Desktop/hpc_lib/homebrew/opt/python@3.9/bin/python3.9 -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/setup.py'"'"'; __file__='"'"'/private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-wheel-2wbatvmt
       cwd: /private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/
  Complete output (43 lines):
  running bdist_wheel
  running build
  running build_ext
  /bin/sh: mono: command not found
  Traceback (most recent call last):
    File "&lt;string&gt;", line 1, in &lt;module&gt;
    File "/private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/setup.py", line 630, in &lt;module&gt;
      setup(
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/lib/python3.9/site-packages/setuptools/__init__.py", line 159, in setup
      return distutils.core.setup(**attrs)
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/core.py", line 148, in setup
      dist.run_commands()
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/dist.py", line 966, in run_commands
      self.run_command(cmd)
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/dist.py", line 985, in run_command
      cmd_obj.run()
    File "/private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/setup.py", line 612, in run
      return bdist_wheel.bdist_wheel.run(self)
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/lib/python3.9/site-packages/wheel/bdist_wheel.py", line 299, in run
      self.run_command('build')
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/cmd.py", line 313, in run_command
      self.distribution.run_command(command)
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/dist.py", line 985, in run_command
      cmd_obj.run()
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/command/build.py", line 135, in run
      self.run_command(cmd_name)
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/cmd.py", line 313, in run_command
      self.distribution.run_command(command)
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/dist.py", line 985, in run_command
      cmd_obj.run()
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/command/build_ext.py", line 340, in run
      self.build_extensions()
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/command/build_ext.py", line 449, in build_extensions
      self._build_extensions_serial()
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/distutils/command/build_ext.py", line 474, in _build_extensions_serial
      self.build_extension(ext)
    File "/private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/setup.py", line 249, in build_extension
      self._install_packages()
    File "/private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/setup.py", line 438, in _install_packages
      subprocess.check_call(cmd, shell=use_shell)
    File "/Users/apoudel/Desktop/hpc_lib/homebrew/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/subprocess.py", line 373, in check_call
      raise CalledProcessError(retcode, cmd)
  subprocess.CalledProcessError: Command 'mono tools/nuget/nuget.exe update -self' returned non-zero exit status 127.
  ----------------------------------------
  ERROR: Failed building wheel for pythonnet
  Running setup.py clean for pythonnet
Failed to build pythonnet
Installing collected packages: pycparser, pythonnet
  DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621
    Running setup.py install for pythonnet ... error
    ERROR: Command errored out with exit status 1:
     command: /Users/apoudel/Desktop/hpc_lib/homebrew/opt/python@3.9/bin/python3.9 -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/setup.py'"'"'; __file__='"'"'/private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-record-rytd6lqg/install-record.txt --single-version-externally-managed --compile --install-headers /Users/apoudel/Desktop/hpc_lib/homebrew/include/python3.9/pythonnet
         cwd: /private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/
    Complete output (6 lines):
    usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
       or: setup.py --help [cmd1 cmd2 ...]
       or: setup.py --help-commands
       or: setup.py cmd --help
    
    error: option --single-version-externally-managed not recognized
    ----------------------------------------
ERROR: Command errored out with exit status 1: /Users/apoudel/Desktop/hpc_lib/homebrew/opt/python@3.9/bin/python3.9 -u -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/setup.py'"'"'; __file__='"'"'/private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-install-sj3whon9/pythonnet_99c95ae1c8dc44df9dc8586a2f7ee189/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/95/c_bn57x5613fwcs5n60rckzw0000gp/T/pip-record-rytd6lqg/install-record.txt --single-version-externally-managed --compile --install-headers /Users/apoudel/Desktop/hpc_lib/homebrew/include/python3.9/pythonnet Check the logs for full command output.

```python
    print('TODO')
```
I would really appreciate if someone could help me resolve this error. Thanks!</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @siaeleni (2022-02-18 03:27 UTC)

<p>Thanks for the answer.<br>
I installed the --pre pythonnet in Slicer 4.13, but seems that I get the same error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68661a2c151df7b7954f090203358de167360cd6.png" alt="image" data-base62-sha1="eTyppS8Nr4caE2u4kJb8CgnrsGy" width="410" height="274"></p>
<p>Also, I checked the PYTHONPATH and I get the following:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/088d5fd0f3664176baa2f2aaaacd0842f7c693ac.png" alt="image" data-base62-sha1="1dEIbS6p8KfxWxca3U2IV8mvozG" width="670" height="89"></p>
<p>Thanks for your help,<br>
Eleni</p>

---

## Post #5 by @lassoan (2022-02-18 04:02 UTC)

<p>I’ve tested pythonnet with latest Slicer Preview Release on Windows, installed using</p>
<pre><code class="lang-python">pip_install('--pre pythonnet')
</code></pre>
<p>Everything seems to work well. Your problem most likely is not related to pythonnet.</p>
<p>A software component overwriting PYTHONPATH would be completely unacceptable, and announcing this in a popup called “Delete Files” makes things even more bizarre. I would recommend to contact the developers of the code that displays this message to sort this out. If they cannot make their software compatible without such a huge hack then I would recommend not to try to integrate it directly with Slicer, but instead send data to Slicer via OpenIGTLink, using <a href="https://pypi.org/project/pyigtl/">pyigtl</a>.</p>

---

## Post #6 by @siaeleni (2022-02-21 04:02 UTC)

<p>Yes, you are right, the problem is coming from that package that I was using.<br>
I could reproduce it on their side as well. Thanks for your help</p>

---
