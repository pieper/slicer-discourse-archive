# python-real different from python interpreter

**Topic ID**: 2496
**Date**: 2018-04-02
**URL**: https://discourse.slicer.org/t/python-real-different-from-python-interpreter/2496

---

## Post #1 by @David_Burns (2018-04-02 20:17 UTC)

<p>I have discovered that the python in bin/python-real is different from the python interactor compiled into Slicer</p>
<p>Using the pre-combiled binaries on linux (both 4.9.0 and 4.8.1) - I have this problem.</p>
<p>For instance in 4.9.0</p>
<ul>
<li>For the interactor I have: python 2.7.13, which is compiled with ucs2 encoding</li>
<li>For python-real I have: python 2.7.12, compiled with ucs4 encoding</li>
</ul>
<p>For those unaware the ucs encoding can be discovered as follows:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import sys<br>
sys.maxunicode</p>
</blockquote>
</blockquote>
</blockquote>
<p>This difference (the ucs encoding) makes many packages working with python-real not work with the python interactor. It would be really great to have access to the interactor python binary - for making use of virtualenv and the like to install python packages.</p>
<p>Right now my workaround is I compile a python binary with the same version and ucs encoding as the interactor, setup a virtualenv, and use this to install the python packages I desire / need.</p>
<p>My questions are:</p>
<ol>
<li>Where is the actual python binary that the interactor uses?</li>
<li>Can this issue be fixed in the next release?<br>
(I am not familiar enough with the slicer build system to fix this problem myself)</li>
</ol>

---

## Post #2 by @jcfr (2018-04-02 20:45 UTC)

<p>Hi David,</p>
<p>Both <code>bin/python-real</code> and Slicer executable are expected to use the same python shared library.</p>
<p>Here is how you could execute both ensuring they use the expected library:</p>
<ul>
<li>for Slicer</li>
</ul>
<pre><code class="lang-auto">$ ./Slicer-build/Slicer --python-code "import sys; print(sys.maxunicode)" --exit-after-startup --no-main-window --no-splash
65535

# the '-c' option is also supported

$ ./Slicer-build/Slicer -c "import sys; print(sys.maxunicode)" --no-splash
65535
</code></pre>
<ul>
<li>for python interpreter:</li>
</ul>
<pre><code class="lang-auto">./python-install/bin/SlicerPython -c "import sys; print(sys.maxunicode)"
65535
</code></pre>
<p>As you can see, the <code>python-real</code> executable can not be started directly. Otherwise it will resolve its symbols against a python library available somewhere else on your system.</p>
<h3><a name="p-10156-launcher-1" class="anchor" href="#p-10156-launcher-1" aria-label="Heading link"></a>launcher</h3>
<p><code>SlicerPython</code> is a convenience launcher allowing to set the environment. The same one is used to start Slicer.</p>
<pre><code class="lang-plaintext">./python-install/bin/SlicerPython --launcher-help
Usage
  SlicerPython [options]

Options
  --launcher-help                              Display help
  --launcher-version                           Show launcher version information
  --launcher-verbose                           Verbose mode
  --launch                                     Specify the application to launch
  --launcher-detach                            Launcher will NOT wait for the application to finish
  --launcher-no-splash                         Hide launcher splash
  --launcher-timeout                           Specify the time in second before the launcher kills the application. -1 means no timeout (default: -1)
  --launcher-load-environment                  Specify the saved environment to load.
  --launcher-dump-environment                  Launcher will print environment variables to be set, then exit
  --launcher-show-set-environment-commands     Launcher will print commands suitable for setting the parent environment (i.e. using 'eval' in a POSIX shell), then exit
  --launcher-additional-settings               Additional settings file to consider
  --launcher-ignore-user-additional-settings   Ignore additional user settings
  --launcher-generate-exec-wrapper-script      Generate executable wrapper script allowing to set the environment
  --launcher-generate-template                 Generate an example of setting file

</code></pre>
<p>Using <code>--launcher-show-set-environment-commands</code> you could conveniently update the current environment and then start  python-real directly.</p>
<pre><code class="lang-plaintext">eval $(./python-install/bin/SlicerPython --launcher-show-set-environment-commands)
python-real -c "import sys; print(sys.maxunicode)"
</code></pre>
<h3><a name="p-10156-questions-2" class="anchor" href="#p-10156-questions-2" aria-label="Heading link"></a>questions</h3>
<aside class="quote no-group" data-username="David_Burns" data-post="1" data-topic="2496">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/bc79bd/48.png" class="avatar"> David_Burns:</div>
<blockquote>
<p>Where is the actual python binary that the interactor uses?</p>
</blockquote>
</aside>
<p>Both the Slicer python interactor available in the application and <code>bin/python-real</code> are expected to use the same python library.</p>
<aside class="quote no-group" data-username="David_Burns" data-post="1" data-topic="2496">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/bc79bd/48.png" class="avatar"> David_Burns:</div>
<blockquote>
<p>Can this issue be fixed in the next release?</p>
<p>(I am not familiar enough with the slicer build system to fix this problem myself)</p>
</blockquote>
</aside>
<p>Based on the information above, let us know if you are able to work out a solution.</p>
<p>Reading this topic may also be informative: <a href="https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984/2" class="inline-onebox">Slicer-Python Packages Use and Install - #2 by jcfr</a></p>

---

## Post #3 by @David_Burns (2018-04-03 02:02 UTC)

<p>Hi Jean,</p>
<p>I really appreciate your informative and prompt reply.</p>
<p>Based on your suggestion I used <code>SlicerPython --launcher-show-set-environment-commands</code> to update the shell environment variables and run <code>python-real</code> directly</p>
<p>This did bring up the same python version and ucs encoding as the interpreter with <code>python-real</code>. Unfortunately, within the shell environment, <code>virtualenv</code> wouldn’t work anymore failing with the error:</p>
<pre><code class="lang-auto">Fatal Python error: Py_Initialize: Unable to get the locale encoding
ImportError: No module named 'encodings'

Current thread 0x00007fd9b9a95700 (most recent call first):
Aborted
</code></pre>
<p>I haven’t done a lot of digging into what is causing this, but will post again if I figure it out. In any case, using virtualenv with the workaround I described above seems a useful / flexible way to install python packages and import them into slicer (including the pre-compiled binary). Maybe that will be helpful to some, as with it I can bring in sklearn, numba, pycuda, scipy, etc…</p>
<p>For now, I haven’t been able to setup a virtualenv with the Slicer’s own python and am stuck having to compile a compatible version from source for the the virtualenv. It is not a terrible solution…</p>

---

## Post #4 by @jcfr (2018-04-03 03:34 UTC)

<p>Would you mind sharing the output of <code>SlicerPython --launcher-show-set-environment-commands</code>, I suspect a system path is prepended to either <code>PATH</code> or <code>LD_LIBRARY_PATH</code> causing your system library to be picked up instead of the one buitd by Slicer.</p>
<p>Also, did you build against Qt5 or Qt4 ?</p>
<p>This used to happen when building against a system Qt4, but we added logic to account for this. I suspect we need to add a similar logic for <code>Qt5_DIR</code>.</p>
<p><a href="https://github.com/Slicer/Slicer/blob/cc723d67c620c17de2d3dd877c52f67f1bbd5ab6/CMakeLists.txt#L606-L629" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/cc723d67c620c17de2d3dd877c52f67f1bbd5ab6/CMakeLists.txt#L606-L629</a></p>
<blockquote>
<p>the workaround I described above seems a useful / flexible way to install python packages and import them into slicer<br>
I haven’t been able to setup a virtualenv with the Slicer’s own python</p>
</blockquote>
<p>Consider Slicer python is itself an isolated environment and installing python package (on Linux) is already possible, we haven’t done much testing using virtualenv in this context.</p>
<p>To support virtualenv, we need to make sure that the PYTHONPATH used when starting Slicer is also updated when switching virtual env.</p>

---

## Post #5 by @David_Burns (2018-04-03 14:25 UTC)

<p>Hi Jean,</p>
<p>Thanks again. Here is the output from  <code>SlicerPython --launcher-show-set-environment-commands</code></p>
<p>This was generated using the pre-compiled binary for Linux v 4.9.0 from here: <a href="https://download.slicer.org/" rel="nofollow noopener">https://download.slicer.org/</a></p>
<p>I am running Linux Mint 18.3 (based on Ubuntu 16.04).</p>
<pre><code class="lang-auto">declare -x "APPLAUNCHER_0_CINNAMON_VERSION=3.6.6";
declare -x "APPLAUNCHER_0_DBUS_SESSION_BUS_ADDRESS=unix:abstract=/tmp/dbus-29uAFN9nm1,guid=fa699cb1fdc1e9c4aa89dbea5ac383d6";
declare -x "APPLAUNCHER_0_DEFAULTS_PATH=/usr/share/gconf/cinnamon.default.path";
declare -x "APPLAUNCHER_0_DESKTOP_SESSION=cinnamon";
declare -x "APPLAUNCHER_0_DISPLAY=:0";
declare -x "APPLAUNCHER_0_GDMSESSION=cinnamon";
declare -x "APPLAUNCHER_0_GDM_LANG=en_CA";
declare -x "APPLAUNCHER_0_GJS_DEBUG_OUTPUT=stderr";
declare -x "APPLAUNCHER_0_GJS_DEBUG_TOPICS=JS ERROR;JS LOG";
declare -x "APPLAUNCHER_0_GNOME_DESKTOP_SESSION_ID=this-is-deprecated";
declare -x "APPLAUNCHER_0_GTK_MODULES=gail:atk-bridge";
declare -x "APPLAUNCHER_0_GTK_OVERLAY_SCROLLING=1";
declare -x "APPLAUNCHER_0_HOME=/home/david";
declare -x "APPLAUNCHER_0_INSIDE_NEMO_PYTHON=";
declare -x "APPLAUNCHER_0_LANG=en_CA.UTF-8";
declare -x "APPLAUNCHER_0_LANGUAGE=en_CA:en";
declare -x "APPLAUNCHER_0_LESSCLOSE=/usr/bin/lesspipe %s %s";
declare -x "APPLAUNCHER_0_LESSOPEN=| /usr/bin/lesspipe %s";
declare -x "APPLAUNCHER_0_LOGNAME=david";
declare -x "APPLAUNCHER_0_LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:";
declare -x "APPLAUNCHER_0_MANDATORY_PATH=/usr/share/gconf/cinnamon.mandatory.path";
declare -x "APPLAUNCHER_0_OLDPWD=/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin";
declare -x "APPLAUNCHER_0_PATH=/home/david/bin:/home/david/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games";
declare -x "APPLAUNCHER_0_PWD=/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64";
declare -x "APPLAUNCHER_0_QT_ACCESSIBILITY=1";
declare -x "APPLAUNCHER_0_QT_LINUX_ACCESSIBILITY_ALWAYS_ON=1";
declare -x "APPLAUNCHER_0_QT_QPA_PLATFORMTHEME=qgnomeplatform";
declare -x "APPLAUNCHER_0_QT_STYLE_OVERRIDE=gtk";
declare -x "APPLAUNCHER_0_SESSION_MANAGER=local/gunstar1:@/tmp/.ICE-unix/1735,unix/gunstar1:/tmp/.ICE-unix/1735";
declare -x "APPLAUNCHER_0_SHELL=/bin/bash";
declare -x "APPLAUNCHER_0_SHLVL=1";
declare -x "APPLAUNCHER_0_SSH_AGENT_PID=1790";
declare -x "APPLAUNCHER_0_SSH_AUTH_SOCK=/run/user/1000/keyring/ssh";
declare -x "APPLAUNCHER_0_TERM=xterm-256color";
declare -x "APPLAUNCHER_0_USER=david";
declare -x "APPLAUNCHER_0_VTE_VERSION=4205";
declare -x "APPLAUNCHER_0_WINDOWID=104857687";
declare -x "APPLAUNCHER_0_XAUTHORITY=/home/david/.Xauthority";
declare -x "APPLAUNCHER_0_XDG_CONFIG_DIRS=/etc/xdg/xdg-cinnamon:/etc/xdg";
declare -x "APPLAUNCHER_0_XDG_CURRENT_DESKTOP=X-Cinnamon";
declare -x "APPLAUNCHER_0_XDG_DATA_DIRS=/usr/share/cinnamon:/usr/share/gnome:/home/david/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share:/usr/share";
declare -x "APPLAUNCHER_0_XDG_GREETER_DATA_DIR=/var/lib/lightdm-data/david";
declare -x "APPLAUNCHER_0_XDG_RUNTIME_DIR=/run/user/1000";
declare -x "APPLAUNCHER_0_XDG_SEAT=seat0";
declare -x "APPLAUNCHER_0_XDG_SEAT_PATH=/org/freedesktop/DisplayManager/Seat0";
declare -x "APPLAUNCHER_0_XDG_SESSION_DESKTOP=cinnamon";
declare -x "APPLAUNCHER_0_XDG_SESSION_ID=c2";
declare -x "APPLAUNCHER_0_XDG_SESSION_PATH=/org/freedesktop/DisplayManager/Session0";
declare -x "APPLAUNCHER_0_XDG_SESSION_TYPE=x11";
declare -x "APPLAUNCHER_0_XDG_VTNR=7";
declare -x "APPLAUNCHER_0__=bin/SlicerPython";
declare -x "APPLAUNCHER_LEVEL=1";
declare -x "LD_LIBRARY_PATH=/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin/../bin:/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin/../lib/Slicer-4.9:/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin/../lib/Python/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}";
declare -x "PATH=/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin${PATH:+:$PATH}";
declare -x "PYTHONHOME=/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin/../lib/Python";
declare -x "PYTHONNOUSERSITE=1";
declare -x "PYTHONPATH=/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin/../lib/Python/lib/Python/lib/python2.7:/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin/../lib/Python/lib/Python/lib/python2.7/lib-dynload:/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin/../lib/Python/lib/Python/lib/python2.7/site-packages:/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin/../bin/Python${PYTHONPATH:+:$PYTHONPATH}";
declare -x "SSL_CERT_FILE=/home/david/Programs/Slicer-4.9.0-2018-04-01-linux-amd64/bin/../share/Slicer-4.9/Slicer.crt";
</code></pre>
<p>I have been able to install many python packages to slicer from the python interpreter using eg <code>pip.main(['install','scipy'])</code>. However, having a virtualenv allowed me to compile / install packages from source and import packages (numba, pycuda for instance) that weren’t available or didn’t work from me when installing with pip from the interpreter. Bringing in the packages to slicer with <code>sys.path.append</code> to the virtualenv package directory means that the slicer build is never harmed when things are going badly…</p>
<p>I am not sure if others are having the same limitations I am using pip from the interpreter, or if a better solution exists. Anyhow, hopefully that explains my rationale for wanting to use a virtualenv.</p>
<p>Thanks again for looking at this.</p>
<p>David</p>

---
