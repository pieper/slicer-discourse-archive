---
topic_id: 7511
title: "Installing Extensions In Binary Distribution Of Slicer"
date: 2019-07-10
url: https://discourse.slicer.org/t/7511
---

# Installing extensions in binary distribution of Slicer

**Topic ID**: 7511
**Date**: 2019-07-10
**URL**: https://discourse.slicer.org/t/installing-extensions-in-binary-distribution-of-slicer/7511

---

## Post #1 by @tbillah (2019-07-10 22:59 UTC)

<p>I need to install a few extensions like <a href="http://dmri.slicer.org/" rel="nofollow noopener">SlicerDMRI</a> and make it available for everyone at my office.</p>
<p>On Partner’s cluster environment, compiling Slicer from source code with desirable <code>.s4ext</code> files, isn’t the best option.</p>
<p>So, I have to resort to <code>ExtensionManager</code> on the Slicer GUI. I installed my desired extensions. The modules are discoverable when I launch Slicer. However, they are not discoverable to other users automatically. Interestingly, when I use a different workstation, they are not discovered either.</p>
<p>I have tried <code>./Slicer --additional-module-paths path1 path2 ...</code>, but I ran into errors that stem from incomplete <code>PYTHONPATH</code> and <code>LD_LIBRARY_PATH</code>.</p>
<p>The question is, what is the most manageable way to install extensions and make it available for all users using that Slicer?</p>

---

## Post #2 by @jcfr (2019-07-11 07:02 UTC)

<p><s>Assuming the user where Slicer and the extensions are installed is called <code>slicer</code>,</s> the idea is to create a script called <code>SlicerWithExtensions.sh</code> along side the Slicer launcher in your shared installation.</p>
<p>The script only need to be updated with the name of the user under which Slicer  is installed on the cluster:</p>
<pre><code class="lang-bash">#!/bin/bash -e

# This is the username associated with the Slicer installation to share between users.
slicer_user=jcfr # TODO: Update this line

script_dir=$(cd $(dirname $0) || exit 1; pwd)
script_name=$(basename $0)

# launcher and launcher settings
launcher=${script_dir}/Slicer
launcher_settings=${script_dir}/bin/SlicerLauncherSettings.ini
echo "Launcher settings ........: ${launcher_settings}"

# sanity checks
if [ ! -f ${launcher} ]; then
  echo "${script_name} is expected to exist along side the Slicer launcher: ${launcher} not found"
  exit 1
fi
if [ ! -f ${launcher_settings} ]; then
  echo "${script_name} is expected to exist along side the Slicer launcher: ${launcher_settings} not found"
  exit 1
fi

# extract revision
revision=$(cat  ${launcher_settings} | grep revision= | cut -d= -f2)
echo "Revision .................: ${revision}"

# revision user settings
slicer_revision_user_settings=/home/${slicer_user}/.config/NA-MIC/Slicer-${revision}.ini
echo "Revision user settings ...: ${launcher_settings}"

# sanity check
if [ ! -f ${slicer_revision_user_settings} ]; then
  echo "Slicer revision user settings not found: ${slicer_revision_user_settings}"
  exit 1
fi

# extract additional module paths
# TODO Handle module path with spaces
additional_module_paths=$(cat  ${slicer_revision_user_settings} | grep AdditionalPaths= | cut -d= -f2 | tr -d ",")
echo "Additional module paths ..: ${additional_module_paths}"

${launcher} --launcher-additional-settings ${slicer_revision_user_settings} --additional-module-paths ${additional_module_paths} "$@"
</code></pre>
<h3>more details</h3>
<p>Generally speaking, extensions are installed in the Slicer setting directory specific to the user and all information are added to a ini file. For example, the ini file associated Slicer 4.10.1 on linux is <code>~/.config/NA-MIC/Slicer-27931.ini</code>.</p>
<p>After installing an extension, you can see settings groups like <code>[LibraryPaths]</code>, <code>[PYTHONPATH]</code>, <code>[Paths]</code> and also <code>[Modules]</code> with the key <code>AdditionalPaths</code>.</p>
<p>To automatically set the environment before starting the real Slicer application, the Slicer launcher is able to infer the path to the user Slicer revision specific file <code>~/.config/NA-MIC/Slicer-27931.ini</code> given information found in the launcher settings.</p>
<p>Here is a snippet of the launcher settings associated with Slicer 4.10.1 (e.g. <code>/path/to/Slicer-4.10.1-linux-amd64/bin/SlicerLauncherSettings.ini</code>)</p>
<pre><code class="lang-auto">[...]

[Application]
path=&lt;APPLAUNCHER_DIR&gt;/bin/SlicerApp-real
arguments=
name=Slicer
revision=27931
organizationDomain=www.na-mic.org
organizationName=NA-MIC

[...]
</code></pre>
<p>Within the <code>[Application]</code> group, we can see the key <code>name</code>, <code>revision</code> and <code>organizationName</code>. These information are sufficient to retrieve the revision specific settings file and compose the environment needed to load the additional  modules associated with the <code>AdditionalPaths</code> key.</p>

---

## Post #3 by @tbillah (2019-07-11 22:09 UTC)

<p>You mean called <code>jcfr</code> ?</p>
<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="7511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Assuming the user where Slicer and the extensions are installed is called <code>slicer</code></p>
</blockquote>
</aside>

---

## Post #4 by @jcfr (2019-07-11 22:13 UTC)

<blockquote>
<p>You mean called <code>jcfr</code> ?</p>
<blockquote>
<p>Assuming the user where Slicer and the extensions are installed is called <code>slicer</code></p>
</blockquote>
</blockquote>
<p>Indeed, I edited the post to be more clear. Let us know how it works out.</p>

---

## Post #5 by @tbillah (2019-07-20 03:17 UTC)

<p>For a week, the environment was down. After it came back online, I tried your instruction. It is mostly correct, except another user would not have access to a file in my home directory:</p>
<p>slicer_revision_user_settings=<code>/home/${slicer_user}/.config/NA-MIC/Slicer-${revision}.ini</code></p>
<p>To get around that, I have done the following:</p>
<p>When you install an extension using the Extension Manager, it allows you to specify a path other than the default <code>/home/${slicer_user}/.config/NA-MIC/Slicer-${revision}.ini</code> directory. I have put in a shared path. The Extension got installed, and the above <code>.ini</code> file got written as it should be. Then, I just copied over the <code>.ini</code> file from my home directory to the shared path.</p>
<p>Rest assured, now I have a way to make Extensions available to all other users that I installed.</p>

---

## Post #6 by @tbillah (2019-07-24 15:29 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<blockquote>
<p>${launcher} --launcher-additional-settings ${slicer_revision_user_settings} --additional-module-paths ${additional_module_paths} “$@”</p>
</blockquote>
<p>The “$@” is failing here. For example, I have tried the following command with additional arguments, but it fails:</p>
<blockquote>
<p>Slicer-4.10.2-linux-amd64/SlicerWithExtensions.sh --launch python-real SlicerDiffusionQC/Test/run_test.py</p>
</blockquote>
<p>Error message:</p>
<pre><code class="lang-auto">Unknown option: --
usage: /rfanfs/pnl-zorro/software/pnlpipe3/Slicer-4.10.2-linux-amd64/bin/../bin/./python-real [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `python -h' for more information.
</code></pre>
<p>I understand you are trying to get any additional argument passed to the script.</p>

---

## Post #7 by @tbillah (2019-09-05 20:06 UTC)

<p>Upon installing an Extension from ExtensionManager, it appears that <code>~/.config/NA-MIC/Slicer-{revision}.ini</code> file gets updated with new <code>[LibraryPaths]</code>, <code>AdditionalPaths</code>, <code>[PYTHONPATH]</code>, <code>[PATH]</code> even though I specify a different directory for <code>Extensions installation path</code>. Is there a way to compartmentalize where <code>Slicer-{revision}.ini</code> file will be written?</p>
<p>The use case is, I have my own Extensions at <code>~/.config/NA-MIC</code> while there is a shared Extension path at <code>~/where/ever/it/is</code>. Extensions installed at the latter directory are not found by a different user unless a <code>Slicer-{revision}.ini</code> exists in a shared directory.</p>

---

## Post #8 by @pieper (2019-09-05 20:23 UTC)

<p>I think in this case the easiest solution is to make a shell script that uses the --additional-module-paths command line argument to specify all the extensions.</p>

---

## Post #9 by @tbillah (2019-09-05 20:26 UTC)

<p>Okay, but then someone would have to type in all the extensions, right? In <a class="mention" href="/u/jcfr">@jcfr</a>’s suggestion, it was more or less automatically discovered.</p>

---

## Post #10 by @lassoan (2019-09-05 20:39 UTC)

<p>To compartmentalize settings, you can rename the Slicer executable file (bin/SlicerApp-real). This will create custom .ini files completely independent from Slicer installations. You also need to update Application/path value in bin/SlicerLauncherSettings.ini file accordingly.</p>
<p>To have completely isolated, custom-branded applications, you can build Slicer from source using <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="nofollow noopener">this template</a>.</p>

---

## Post #11 by @pieper (2019-09-05 20:42 UTC)

<aside class="quote no-group" data-username="tbillah" data-post="9" data-topic="7511" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tbillah/48/4139_2.png" class="avatar"> tbillah:</div>
<blockquote>
<p>Okay, but then someone would have to type in all the extensions, right? In <a class="mention" href="/u/jcfr">@jcfr</a>’s suggestion, it was more or less automatically discovered.</p>
</blockquote>
</aside>
<p>It’s a matter of taste, but there’s a tradeoff here between simplicity and automation.  Personally, I think a script that has a lot of identical lines adding paths to the command line is easier to understand and maintain (especially if it’s nicely formatted with backslashes and indentation).  There’s only so much that needs to be in such a script.</p>

---

## Post #12 by @tbillah (2019-09-05 20:50 UTC)

<blockquote>
<p>There’s only so much that needs to be in such a script.</p>
</blockquote>
<p>I like your thought. Question on that: see the following excerpt from <code>Slicer-28257.ini</code> file:</p>
<pre><code class="lang-auto">[LibraryPaths]
1\path=/rfanfs/pnl-zorro/software/pnlpipe3/Slicer-4.10.2-linux-amd64/.config/NA-MIC/Extensions-28257/DiffusionQC/bin
10\path=/rfanfs/pnl-zorro/software/pnlpipe3/Slicer-4.10.2-linux-amd64/.config/NA-MIC/Extensions-28257/UKFTractography/lib/Slicer-4.10/cli-modules
11\path=/rfanfs/pnl-zorro/software/pnlpipe3/Slicer-4.10.2-linux-amd64/.config/NA-MIC/Extensions-28257/UKFTractography/lib/Slicer-4.10/qt-loadable-modules
</code></pre>
<p>In the rest of the file, those paths appear multiple times in <code>[LibraryPaths]</code> section. Similar multiplicity exists in other sections i.e <code>[PYTHONPATH]</code> and <code>[Paths]</code>. So, when writing the shell script, can I omit multiplicity of paths? <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #13 by @tbillah (2019-09-05 20:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="7511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To have completely isolated, custom-branded applications, you can build Slicer from source using <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">this template</a>.</p>
</blockquote>
</aside>
<p>Built many times so far, but not the sweetest option on a shared cluster without administrative privileges.</p>
<p>I shall try the first part of your suggestion.</p>

---

## Post #14 by @lassoan (2019-09-05 20:59 UTC)

<p>If you want to have a shared Slicer with extensions installed, you can also just copy all the extensions in lib\Slicer-4.11 folder. No need to modify any settings or paths.</p>

---

## Post #15 by @pieper (2019-09-05 21:04 UTC)

<p>If you don’t want to copy the files, you can just list the modules folders in the command line to start slicer.<br>
I often have a small shell script to start up slicer with extensions under development and just point to their build directories.</p>
<p>I don’t have one handy, but something like:</p>
<pre><code class="lang-auto">Slicer --additional-module-paths \
  ${extdir}/cli-modules \
  ${extdir}/qt-loadable-modules \
  ${extdir}/qt-scripted-modules \
</code></pre>
<p>all the extensions will follow the same pattern.</p>

---

## Post #16 by @tbillah (2019-10-11 16:37 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, sorry I might be a little late to check on this. I tried the following:</p>
<pre><code class="lang-auto">./Slicer --additional-module-paths .config/NA-MIC/Extensions-28257/DiffusionQC/lib/Slicer-4.10/cli-modules/ .config/NA-MIC/Extensions-28257/DiffusionQC/lib/Slicer-4.10/qt-scripted-modules/ --launch bin/python-real .config/NA-MIC/Extensions-28257/DiffusionQC/lib/Slicer-4.10/cli-modules/diffusionQC.py -h
</code></pre>
<p>But ran into the error:</p>
<pre><code class="lang-auto">Usage
  Slicer [options]

Options
  --launcher-help                                 Display help
  --launcher-version                              Show launcher version information
  --launcher-verbose                              Verbose mode
  --launch                                        Specify the application to launch
  --launcher-detach                               Launcher will NOT wait for the application to finish
  --launcher-no-splash                            Hide launcher splash
  --launcher-timeout                              Specify the time in second before the launcher kills the application. -1 means no timeout (default: -1)
  --launcher-load-environment                     Specify the saved environment to load.
  --launcher-dump-environment                     Launcher will print environment variables to be set, then exit
  --launcher-show-set-environment-commands        Launcher will print commands suitable for setting the parent environment (i.e. using 'eval' in a POSIX shell), then exit
  --launcher-additional-settings                  Additional settings file to consider
  --launcher-additional-settings-exclude-groups   Comma separated list of settings groups that should NOT be overwritten by values in User and Additional settings. For example: General,Application,ExtraApplicationToLaunch
  --launcher-ignore-user-additional-settings      Ignore additional user settings
  --launcher-generate-exec-wrapper-script         Generate executable wrapper script allowing to set the environment
  --launcher-generate-template                    Generate an example of setting file
  --designer                                      Start Qt designer using Slicer plugins
Unknown option: --
usage: bin/python-real [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `python -h' for more information.
</code></pre>
<p>So, am I not using it the right way?</p>

---

## Post #17 by @pieper (2019-10-11 17:32 UTC)

<p>Ah, right - the problem here is that  <code>--additional-module-paths</code> is an argument of the application, not the launcher.  But I see here you are wanting to launch <code>bin/python-real</code> .</p>
<p>Probably you want something more like this, where you use the app as a python environment to it has the extensions loaded.</p>
<pre><code class="lang-auto">EXT_DIR=.config/NA-MIC/Extensions-28257/DiffusionQC/lib/Slicer-4.10

./Slicer-build/Slicer \
  --no-main-window \
  --python-script ${EXT_DIR}/cli-modules/diffusionQC.py \
  --additional-module-paths \
      ${EXT_DIR}/cli-modules/ \
      ${EXT_DIR}/qt-scripted-modules/
</code></pre>

---

## Post #18 by @tbillah (2019-10-11 18:56 UTC)

<p>The suggestion ran into following error (I am connected via SSH though):</p>
<pre><code class="lang-auto">qt.qpa.screen: QXcbConnection: Could not connect to display
Could not connect to any X display.
</code></pre>
<p>The point of trying to run a script like above is to omit Slicer GUI.</p>
<p>I also tried the following (<code>--additional-module-paths</code> as an argument for the application now), but failed with the same error:</p>
<pre><code class="lang-auto">./Slicer --additional-module-paths ${EXT_DIR}/cli-modules/ ${EXT_DIR}/qt-scripted-modules/ --launch python-real ${EXT_DIR}/cli-modules/diffusionQC.py -h

</code></pre>
<pre><code class="lang-auto">Unknown option: --
usage: /rfanfs/pnl-zorro/software/pnlpipe3/Slicer-4.10.2-linux-amd64/bin/../bin/./python-real [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `python -h' for more information.
</code></pre>

---

## Post #19 by @pieper (2019-10-11 19:14 UTC)

<p>Probably easiest just to install and run <a href="https://xpra.org/trac/wiki/Xdummy" rel="nofollow noopener">Xdummy</a>.  You shouldn’t need any of the GLX options if you just want to run the script.</p>

---

## Post #20 by @tbillah (2019-10-11 20:01 UTC)

<p>Okay, solved the X error. Now, how would I provide argument to the python-script I want to run?</p>
<blockquote>
<p>./Slicer --additional-module-paths ${EXT_DIR}/cli-modules/ ${EXT_DIR}/qt-scripted-modules/ --no-main-window --python-script ${EXT_DIR}/cli-modules/diffusionQC.py -h</p>
</blockquote>
<p>The above prints Slicer’s help message, not the one from the python-script.</p>

---

## Post #21 by @pieper (2019-10-11 20:30 UTC)

<p>Ah, yes, I recall there’s a bug with -h getting grabbed by the launcher, but other args should work.</p>
<p>Maybe you can add suggestions for your use case to this issue:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/commontk/AppLauncher/issues/111" target="_blank" rel="nofollow noopener">github.com/commontk/AppLauncher</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/AppLauncher/issues/111" target="_blank" rel="nofollow noopener">`--ignore-rest` does not work correctly</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2018-10-17" data-time="14:56:50" data-timezone="UTC">02:56PM - 17 Oct 18 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/ihnorton" target="_blank" rel="nofollow noopener">
          <img alt="ihnorton" src="https://avatars1.githubusercontent.com/u/327706?v=4" class="onebox-avatar-inline" width="20" height="20">
          ihnorton
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">As far as I understand, it should allow to pass further arguments only to the launched binary, but:
```
sliceruser@8192a65779e5:~/Slicer-4.9.0-2018-10-14-linux-amd64$ ./Slicer --launch ./bin/python-real...</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #22 by @lassoan (2019-10-12 00:55 UTC)

<p>This post may answer your question:</p>
<aside class="quote" data-post="2" data-topic="8217">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-should-i-pass-arguments-when-running-slicer-in-batch-mode/8217/2">How should I pass arguments when running Slicer in batch mode?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Everything after --python-script until the next recognizable flag is passed into the python interpreter: 
Run: 
./Slicer.exe --no-main-window --python-script test.py param1 param2 param3 
Where test.py is: 
print(sys.argv) 
You will get this output on the console: 
['test.py', 'param1', 'param2', 'param3']
  </blockquote>
</aside>

<p>Also not that if you don’t need to run the application (e.g., just run Python CLI modules) then you may be able to run Python scripts using <code>PythonSlicer</code> executable.</p>

---

## Post #23 by @tbillah (2020-11-30 22:48 UTC)

<aside class="quote no-group" data-username="pieper" data-post="17" data-topic="7511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Ah, right - the problem here is that <code>--additional-module-paths</code> is an argument of the application, not the launcher.</p>
</blockquote>
</aside>
<p>Hi all,</p>
<p>I would like to share a solution to the above problem I figured–in <a class="mention" href="/u/jcfr">@jcfr</a>’s suggestion, if I change the last line to:</p>
<pre data-code-wrap="bash"><code class="lang-bash">AdditionalPaths=${additional_module_paths} ${launcher} --launcher-additional-settings ${slicer_revision_user_settings}
</code></pre>
<p>it goes away. As you can see, the trick is to move the additional paths from end to front.</p>
<p>For what it’s worth, I am no longer in <code>python-real</code>. I needed to launch a module from SlicerDMRI:</p>
<pre data-code-wrap="bash"><code class="lang-bash">AdditionalPaths=${additional_module_paths} ${launcher} --launcher-additional-settings ${slicer_revision_user_settings} --launch .config/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/cli-modules/FiberTractMeasurements --help
</code></pre>
<p>Lastly, to echo Andras’ suggestion, I think I am better off building an independent Slicer in future.</p>

---

## Post #24 by @fuentesdt (2021-03-05 14:00 UTC)

<p>Hi,</p>
<p>I have a similar question to this post. I want to make a minor modification to a Slicer Extension for another lab member to use. Is the best approach to build everything in a docker and package the extension modification? something like:</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/Slicer/SlicerBuildEnvironment#configure-build-and-package-a-slicer-extension-for-linux" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars.githubusercontent.com/u/324362?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/Slicer/SlicerBuildEnvironment#configure-build-and-package-a-slicer-extension-for-linux" target="_blank" rel="noopener nofollow ugc">Slicer/SlicerBuildEnvironment - Configure, build and package a Slicer extension for Linux</a></h3>


  <p><span class="label1">A repository of scripts to set up a Slicer build environment. </span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>as long as the group all have a similar linux environment on a local machine should be ok?</p>

---

## Post #25 by @lassoan (2021-03-05 14:08 UTC)

<p>I would recommend to send a pull request to the extension’s repository. Then not only that lab member but all other users can benefit from the change.</p>
<p>In general, “similar” build environment is not sufficient for achieving binary compatibility, but you can try and it may or may not work. To ensure binary compatibility, you need to have the exact same build environment, which is the easiest to achieve if you build on the same computer (physical or virtual machine or container).</p>

---

## Post #26 by @fuentesdt (2021-03-05 14:18 UTC)

<p>thank you. i’ll try both. the modification is very much a hack that breaks other functionality a user might want. I need to give it some thought how to not break existing the calculation.</p>

---
