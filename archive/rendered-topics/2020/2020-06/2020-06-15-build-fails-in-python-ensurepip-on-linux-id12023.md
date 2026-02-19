---
topic_id: 12023
title: "Build Fails In Python Ensurepip On Linux"
date: 2020-06-15
url: https://discourse.slicer.org/t/12023
---

# Build fails in python-ensurepip on Linux

**Topic ID**: 12023
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/build-fails-in-python-ensurepip-on-linux/12023

---

## Post #1 by @Zerfox (2020-06-15 00:12 UTC)

<p>Hi!</p>
<p>I am trying to build the nightly version of Slicer on Arch Linux (5.7.2-arch1-1) in debug mode using the developers instructions.</p>
<p>During the install step for ‘python-ensurepip’ I get the following error:</p>
<pre><code>[ 59%] Performing install step for 'python-ensurepip'
-- Looking for 26 include files stdio.h, ..., krb.h - not found
-- Looking for 26 include files stdio.h, ..., libgen.h
-- Looking for 26 include files stdio.h, ..., libgen.h - found
-- Looking for 27 include files stdio.h, ..., libssh2.h
-- Looking for 27 include files stdio.h, ..., libssh2.h - found
-- Looking for 28 include files stdio.h, ..., limits.h
-- Looking for 28 include files stdio.h, ..., limits.h - found
-- Looking for 29 include files stdio.h, ..., locale.h
-- Looking for 29 include files stdio.h, ..., locale.h - found
-- Looking for 30 include files stdio.h, ..., net/if.h
-- Looking for 30 include files stdio.h, ..., net/if.h - found
-- Looking for 31 include files stdio.h, ..., netdb.h
-- Looking for 31 include files stdio.h, ..., netdb.h - found
-- Looking for 32 include files stdio.h, ..., netinet/in.h
-- Looking for 32 include files stdio.h, ..., netinet/in.h - found
-- Looking for 33 include files stdio.h, ..., netinet/tcp.h
-- Looking for 33 include files stdio.h, ..., netinet/tcp.h - found
-- Looking for 34 include files stdio.h, ..., openssl/crypto.h
-- Looking for 34 include files stdio.h, ..., openssl/crypto.h - found
-- Looking for 35 include files stdio.h, ..., openssl/engine.h
-- Looking for 35 include files stdio.h, ..., openssl/engine.h - found
-- Looking for 36 include files stdio.h, ..., openssl/err.h
-- Looking for 36 include files stdio.h, ..., openssl/err.h - found
-- Looking for 37 include files stdio.h, ..., openssl/pem.h
CMake Error at /home/rutger/Desktop/Studie/graduation/slicer/Slicer-SuperBuild-Debug/python-ensurepip-prefix/src/python-ensurepip-stamp/python-ensurepip-install-Debug.cmake:16 (message):
  Command failed: 2

   '/home/rutger/Desktop/Studie/graduation/slicer/Slicer-SuperBuild-Debug/python-install/bin/PythonSlicer' '-m' 'ensurepip' '--default-pip'

  See also

    /home/rutger/Desktop/Studie/graduation/slicer/Slicer-SuperBuild-Debug/python-ensurepip-prefix/src/python-ensurepip-stamp/python-ensurepip-install-*.log


make[2]: *** [CMakeFiles/python-ensurepip.dir/build.make:75: python-ensurepip-prefix/src/python-ensurepip-stamp/python-ensurepip-install] Error 1
make[2]: Leaving directory '/home/rutger/Documents/Studie/tu-eindhoven/Master/year-2019-2020/graduation/slicer/Slicer-SuperBuild-Debug'
make[1]: *** [CMakeFiles/Makefile2:682: CMakeFiles/python-ensurepip.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
</code></pre>
<p>The output log is empty. The error log contains the following:</p>
<pre><code>Exception:
Traceback (most recent call last):
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_internal/basecommand.py", line 228, in main
    status = self.run(options, args)
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_internal/commands/install.py", line 241, in run
    with self._build_session(options) as session:
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_internal/basecommand.py", line 81, in _build_session
    insecure_hosts=options.trusted_hosts,
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_internal/download.py", line 338, in __init__
    self.headers["User-Agent"] = user_agent()
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_internal/download.py", line 101, in user_agent
    zip(["name", "version", "id"], distro.linux_distribution()),
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_vendor/distro.py", line 120, in linux_distribution
    return _distro.linux_distribution(full_distribution_name)
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_vendor/distro.py", line 634, in linux_distribution
    self.version(),
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_vendor/distro.py", line 688, in version
    self.lsb_release_attr('release'),
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_vendor/distro.py", line 836, in lsb_release_attr
    return self._lsb_release_info.get(attribute, '')
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_vendor/distro.py", line 522, in __get__
    ret = obj.__dict__[self._fname] = self._f(obj)
  File "/tmp/tmpsiaxhdyv/pip-10.0.1-py2.py3-none-any.whl/pip/_vendor/distro.py", line 933, in _lsb_release_info
    stdout = subprocess.check_output(cmd, stderr=devnull)
  File "/home/rutger/Desktop/Studie/graduation/slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/subprocess.py", line 336, in check_output
    **kwargs).stdout
  File "/home/rutger/Desktop/Studie/graduation/slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/subprocess.py", line 418, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '('lsb_release', '-a')' returned non-zero exit status 1.
</code></pre>
<p>I could not find any related issues on GitHub nor any topics here on Discourse. Would anyone be so kind to point me in the right direction as to what I am doing wrong? I assume it has something to do with my Python version (3.8), but I did not see any specific requirements in the developers build instructions regarding Python versions.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2020-06-15 00:30 UTC)

<p>It should not matter what Python distributions you have installed on your system. Do you see something that would indicate that your system Python interferes with the build process?</p>
<p>Was the release-mode build successful?</p>

---

## Post #3 by @Zerfox (2020-06-15 20:09 UTC)

<p>Hi Andras,</p>
<p>Honestly I don’t see any indicators why my system python would interfere with the build process.<br>
Calling <code>lsb_release -a</code> directly on the command-line worked fine so I am not sure what is going wrong.</p>
<p>In the end I decided to temporarily remove <code>/usr/bin/lsb_release</code>, which circumvented the error. I based this on <a href="https://github.com/pypa/pip/issues/4924" rel="nofollow noopener">https://github.com/pypa/pip/issues/4924</a>. Not sure why this worked exactly, I’m not that familiar with Python.</p>
<p>Thanks again and keep up the good work.</p>

---

## Post #4 by @jcfr (2020-06-15 20:44 UTC)

<p>Older distributions have an implementation of <code>lsb_release</code> in python that do not specify flag  <code>-Es</code> in the shebang.  Without these flags, the script was <code>lsb_release</code> incorrectly using the Slicer python environment instead of the one on the system.</p>
<p>This is why in Slicer build system we work around the issue generating a launcher emulating the role of <code>-Es</code>.</p>
<p>If you are curious, you could look at  <a href="https://bugs.launchpad.net/ubuntu/+source/lsb/+bug/938869/comments/28">https://bugs.launchpad.net/ubuntu/+source/lsb/+bug/938869/comments/28</a> and  what is done in the Slicer build system:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/9b7aef985f045fd6727c2f5e90a649faea4eed9a/SuperBuild/External_python.cmake#L216-L227" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/9b7aef985f045fd6727c2f5e90a649faea4eed9a/SuperBuild/External_python.cmake#L216-L227" target="_blank">Slicer/Slicer/blob/9b7aef985f045fd6727c2f5e90a649faea4eed9a/SuperBuild/External_python.cmake#L216-L227</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="216" style="counter-reset: li-counter 215 ;">
<li>find_program(LSB_RELEASE_EXECUTABLE NAMES lsb_release)</li>
<li>set(_configure_lsb_release_wrapper FALSE)</li>
<li>if(LSB_RELEASE_EXECUTABLE)</li>
<li>  file(STRINGS ${LSB_RELEASE_EXECUTABLE} _content LIMIT_INPUT 80)</li>
<li>  list(GET _content 0 _first_line)</li>
<li>  # Generate lsb_release wrapper only if the executable is a script that</li>
<li>  # (1) has a "shebang" and (2) does NOT contain "-Es" option.</li>
<li>  # See https://bugs.launchpad.net/ubuntu/+source/lsb/+bug/938869/comments/28</li>
<li>  if(${_first_line} MATCHES "^#!" AND NOT ${_first_line} MATCHES "-Es")</li>
<li>    set(_configure_lsb_release_wrapper TRUE)</li>
<li>  endif()</li>
<li>endif()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
