# Slicer 5: Disable loading modules from command line

**Topic ID**: 24156
**Date**: 2022-07-02
**URL**: https://discourse.slicer.org/t/slicer-5-disable-loading-modules-from-command-line/24156

---

## Post #1 by @keri (2022-07-02 17:00 UTC)

<p>Hi,</p>
<p>I remember in Slicer 4 it was possible to disable loading modules when launching from command line:</p>
<pre><code class="lang-auto">./Slicer --modules-to-ignore Volumes
</code></pre>
<p>I use SlicerCAT based on Slicer 5 and there no such option anymore.<br>
All I can see when invoking <code>help</code>:</p>
<pre><code class="lang-auto">./Colada --help
Usage
  Colada [options]

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
  --VisualStudio                                  Open Visual Studio with Slicer's DLL paths set up
  --VisualStudioProject                           Open Visual Studio Slicer project with Slicer's DLL paths set up
  --cmd                                           Start cmd
  --designer                                      Start Qt designer using Slicer plugins
error: [C:/C/r/Slicer-build/bin/Release/ColadaApp-real.exe] exit abnormally - Report the problem.
</code></pre>
<p>As you can see I also get error <code>exit abnormally - Report the problem.</code><br>
Is it my customization is to blame or is it Slicer 5?</p>

---

## Post #2 by @keri (2023-04-15 21:39 UTC)

<p>For the future references: as mentioned in the <a href="https://slicer.readthedocs.io/en/5.2/user_guide/settings.html#user-specific-settings" rel="noopener nofollow ugc">docs</a> on Windows the correct command should be:</p>
<pre><code class="lang-auto">./Slicer.exe --help | more
</code></pre>
<p>Didn’t know that…</p>

---
