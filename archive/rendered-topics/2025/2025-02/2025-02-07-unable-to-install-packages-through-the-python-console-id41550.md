---
topic_id: 41550
title: "Unable To Install Packages Through The Python Console"
date: 2025-02-07
url: https://discourse.slicer.org/t/41550
---

# Unable to install packages through the Python Console

**Topic ID**: 41550
**Date**: 2025-02-07
**URL**: https://discourse.slicer.org/t/unable-to-install-packages-through-the-python-console/41550

---

## Post #1 by @dpvaldes (2025-02-07 11:55 UTC)

<p>I’m trying to install the pandas package through the Python console in Slicer. I’m running Slicer 5.8 in macOS Sequoia 15.3</p>
<blockquote>
<blockquote>
<blockquote>
<p>from slicer.util import pip_install<br>
pip_install(‘pandas’)</p>
</blockquote>
</blockquote>
</blockquote>
<p>shows me this output:</p>
<p>error: Application is NOT executable [/Applications/Slicer.app/Contents/bin/./python-real]<br>
Usage<br>
PythonSlicer [options]</p>
<p>Options<br>
–launcher-help                                 Display help<br>
–launcher-version                              Show launcher version information<br>
–launcher-verbose                              Verbose mode<br>
–launch                                        Specify the application to launch<br>
–launcher-detach                               Launcher will NOT wait for the application to finish<br>
–launcher-no-splash                            Hide launcher splash<br>
–launcher-timeout                              Specify the time in second before the launcher kills the application. -1 means no timeout (default: -1)<br>
–launcher-load-environment                     Specify the saved environment to load.<br>
–launcher-dump-environment                     Launcher will print environment variables to be set, then exit<br>
–launcher-show-set-environment-commands        Launcher will print commands suitable for setting the parent environment (i.e. using ‘eval’ in a POSIX shell), then exit<br>
–launcher-additional-settings                  Additional settings file to consider<br>
–launcher-additional-settings-exclude-groups   Comma separated list of settings groups that should NOT be overwritten by values in User and Additional settings. For example: General,Application,ExtraApplicationToLaunch<br>
–launcher-ignore-user-additional-settings      Ignore additional user settings<br>
–launcher-generate-exec-wrapper-script         Generate executable wrapper script allowing to set the environment<br>
–launcher-generate-template                    Generate an example of setting file<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3942, in pip_install<br>
_executePythonModule(“pip”, args)<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3896, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3862, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘-m’, ‘pip’, ‘install’, ‘pandas’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @dpvaldes (2025-02-07 16:30 UTC)

<p>Solved it by changing App Management in the Security settings.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f32f9094d7d99c14a653ddc2901325160ba4c91.png" data-download-href="/uploads/short-url/6JxEhW6Ex0f5lz3DLEcbgiT70xr.png?dl=1" title="Screenshot 2025-02-07 at 11.30.05 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f32f9094d7d99c14a653ddc2901325160ba4c91_2_690x289.png" alt="Screenshot 2025-02-07 at 11.30.05 AM" data-base62-sha1="6JxEhW6Ex0f5lz3DLEcbgiT70xr" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f32f9094d7d99c14a653ddc2901325160ba4c91_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f32f9094d7d99c14a653ddc2901325160ba4c91.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f32f9094d7d99c14a653ddc2901325160ba4c91.png 2x" data-dominant-color="E3E3E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-07 at 11.30.05 AM</span><span class="informations">964×404 24.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
