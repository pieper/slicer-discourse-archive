# Error in PyTorch installation

**Topic ID**: 39880
**Date**: 2024-10-27
**URL**: https://discourse.slicer.org/t/error-in-pytorch-installation/39880

---

## Post #1 by @Ben (2024-10-27 11:37 UTC)

<p>I am installing Totalsegmentation in Windows 10, after the installation, I continued to install the PyTorch, and got the error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe5803a076f8d4679ea5d76cad1a89f0c9d2fed0.jpeg" data-download-href="/uploads/short-url/Ai1QvMvhTBB9NhycrzqId6y6b4Y.jpeg?dl=1" title="2024-10-27_151523" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe5803a076f8d4679ea5d76cad1a89f0c9d2fed0.jpeg" alt="2024-10-27_151523" data-base62-sha1="Ai1QvMvhTBB9NhycrzqId6y6b4Y" width="566" height="307"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-10-27_151523</span><span class="informations">566×307 51.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I already uninstall, restart, reinstall, and restart, there is no difference.</p>
<p>My setup is:<br>
<a href="mailto:I7-10700CPU@2.90GHz">I7-10700CPU@2.90GHz</a><br>
64GB RAM<br>
Windows 10 Pro<br>
NIVIDIA GeForce RTX 3060 Ti, Driver version 560.94<br>
NIVIDIA GeForce Experience Version 3.28.0.417<br>
3D Slicer Version 5.6.2</p>
<p>The details of the error are as follows:<br>
Traceback (most recent call last):</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 219, in installTorch</p>
<p>import light_the_torch._patch</p>
<p>ModuleNotFoundError: No module named ‘light_the_torch’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay</p>
<p>yield</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 78, in onInstallTorch</p>
<p>torch = self.logic.installTorch(askConfirmation, None if automaticBackend else backend, torchVersionRequirement, torchvisionVersionRequirement)</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 221, in installTorch</p>
<p>PyTorchUtilsLogic._installLightTheTorch()</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 247, in _installLightTheTorch</p>
<p>slicer.util.pip_install(‘light-the-torch&gt;=0.5’)</p>
<p>File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3887, in pip_install</p>
<p>_executePythonModule(“pip”, args)</p>
<p>File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3848, in _executePythonModule</p>
<p>logProcessOutput(proc)</p>
<p>File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3814, in logProcessOutput</p>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>subprocess.CalledProcessError: Command ‘[‘C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘light-the-torch&gt;=0.5’]’ returned non-zero exit status 1.</p>
<p>Please advise.<br>
Thanks.</p>

---

## Post #2 by @lassoan (2024-10-27 11:41 UTC)

<p>Please check the application log, Python console, or the textbox under the Apply button in the TotalSegmentator module. There should be some more specific information about why light-the-torch installation fails.</p>

---

## Post #3 by @Ben (2024-10-27 15:15 UTC)

<p>Thanks for the reply.<br>
I got these:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3fc06c56972cf9c397f3ddeb181d6a4b816f609.jpeg" data-download-href="/uploads/short-url/wwQlHhIkpIxfVT4ztLS3NUsgyXT.jpeg?dl=1" title="2024-10-27_231231" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3fc06c56972cf9c397f3ddeb181d6a4b816f609_2_496x500.jpeg" alt="2024-10-27_231231" data-base62-sha1="wwQlHhIkpIxfVT4ztLS3NUsgyXT" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3fc06c56972cf9c397f3ddeb181d6a4b816f609_2_496x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3fc06c56972cf9c397f3ddeb181d6a4b816f609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3fc06c56972cf9c397f3ddeb181d6a4b816f609.jpeg 2x" data-dominant-color="DBDFE7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-10-27_231231</span><span class="informations">510×514 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90788a1ac877d111c1bb3bc08068a432f8891ca1.jpeg" data-download-href="/uploads/short-url/kC30DRBwmIkz2tizz5lDJvoYFah.jpeg?dl=1" title="2024-10-27_231211" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90788a1ac877d111c1bb3bc08068a432f8891ca1.jpeg" alt="2024-10-27_231211" data-base62-sha1="kC30DRBwmIkz2tizz5lDJvoYFah" width="513" height="401"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-10-27_231211</span><span class="informations">513×401 68.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Ben (2024-10-27 15:21 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/361e2d022da568bbc5a6ee74bfa01059f7692680.jpeg" data-download-href="/uploads/short-url/7IKqXkiKIWQOs30YvVDO9hLnMGY.jpeg?dl=1" title="2024-10-27_232025" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/361e2d022da568bbc5a6ee74bfa01059f7692680_2_422x499.jpeg" alt="2024-10-27_232025" data-base62-sha1="7IKqXkiKIWQOs30YvVDO9hLnMGY" width="422" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/361e2d022da568bbc5a6ee74bfa01059f7692680_2_422x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/361e2d022da568bbc5a6ee74bfa01059f7692680.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/361e2d022da568bbc5a6ee74bfa01059f7692680.jpeg 2x" data-dominant-color="D8DCE4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-10-27_232025</span><span class="informations">490×580 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The text copy is the following:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 219, in installTorch<br>
import light_the_torch._patch<br>
ModuleNotFoundError: No module named ‘light_the_torch’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 78, in onInstallTorch<br>
torch = self.logic.installTorch(askConfirmation, None if automaticBackend else backend, torchVersionRequirement, torchvisionVersionRequirement)<br>
File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 221, in installTorch<br>
PyTorchUtilsLogic._installLightTheTorch()<br>
File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 247, in _installLightTheTorch<br>
slicer.util.pip_install(‘light-the-torch&gt;=0.5’)<br>
File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3887, in pip_install<br>
_executePythonModule(“pip”, args)<br>
File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3848, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3814, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘light-the-torch&gt;=0.5’]’ returned non-zero exit status 1.</p>

---

## Post #5 by @Ben (2024-10-27 15:29 UTC)

<p>Python Console:</p>
<p>error: Application does NOT exists [C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/bin/./python-real.exe]</p>
<p>Usage</p>
<p>PythonSlicer [options]</p>
<p>Options</p>
<p>–launcher-help Display help</p>
<p>–launcher-version Show launcher version information</p>
<p>–launcher-verbose Verbose mode</p>
<p>–launch Specify the application to launch</p>
<p>–launcher-detach Launcher will NOT wait for the application to finish</p>
<p>–launcher-no-splash Hide launcher splash</p>
<p>–launcher-timeout Specify the time in second before the launcher kills the application. -1 means no timeout (default: -1)</p>
<p>–launcher-load-environment Specify the saved environment to load.</p>
<p>–launcher-dump-environment Launcher will print environment variables to be set, then exit</p>
<p>–launcher-show-set-environment-commands Launcher will print commands suitable for setting the parent environment (i.e. using ‘eval’ in a POSIX shell), then exit</p>
<p>–launcher-additional-settings Additional settings file to consider</p>
<p>–launcher-additional-settings-exclude-groups Comma separated list of settings groups that should NOT be overwritten by values in User and Additional settings. For example: General,Application,ExtraApplicationToLaunch</p>
<p>–launcher-ignore-user-additional-settings Ignore additional user settings</p>
<p>–launcher-generate-exec-wrapper-script Generate executable wrapper script allowing to set the environment</p>
<p>–launcher-generate-template Generate an example of setting file</p>
<p>[Python] Failed to install PyTorch. Some PyTorch files may be in use or corrupted. Please restart the application, uninstall PyTorch, and try installing again.</p>
<p>[Python] Command ‘[‘C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘light-the-torch&gt;=0.5’]’ returned non-zero exit status 1.</p>
<p>Traceback (most recent call last):</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 219, in installTorch</p>
<p>import light_the_torch._patch</p>
<p>ModuleNotFoundError: No module named ‘light_the_torch’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 78, in onInstallTorch</p>
<p>torch = self.logic.installTorch(askConfirmation, None if automaticBackend else backend, torchVersionRequirement, torchvisionVersionRequirement)</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 221, in installTorch</p>
<p>PyTorchUtilsLogic._installLightTheTorch()</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py”, line 247, in _installLightTheTorch</p>
<p>slicer.util.pip_install(‘light-the-torch&gt;=0.5’)</p>
<p>File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3887, in pip_install</p>
<p>_executePythonModule(“pip”, args)</p>
<p>File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3848, in _executePythonModule</p>
<p>logProcessOutput(proc)</p>
<p>File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3814, in logProcessOutput</p>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>subprocess.CalledProcessError: Command ‘[‘C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘light-the-torch&gt;=0.5’]’ returned non-zero exit status 1.</p>
<p>[Qt] QWindowsWindow::setGeometry: Unable to set geometry 1420x745+0+23 (frame: 1436x784-8-8) on QWidgetWindow/“qSlicerMainWindowWindow” on “\.\DISPLAY1”. Resulting geometry: 1366x745+0+23 (frame: 1382x784-8-8) margins: 8, 31, 8, 8 minimum size: 1420x418 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=1436,457 maxtrack=0,0)</p>
<p>[Qt] QWindowsWindow::setGeometry: Unable to set geometry 1420x745+0+23 (frame: 1436x784-8-8) on QWidgetWindow/“qSlicerMainWindowWindow” on “\.\DISPLAY1”. Resulting geometry: 1366x745+0+23 (frame: 1382x784-8-8) margins: 8, 31, 8, 8 minimum size: 1420x446 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=1436,485 maxtrack=0,0)</p>
<p>[Qt] QWindowsWindow::setGeometry: Unable to set geometry 1444x745+0+23 (frame: 1460x784-8-8) on QWidgetWindow/“qSlicerMainWindowWindow” on “\.\DISPLAY1”. Resulting geometry: 1366x745+0+23 (frame: 1382x784-8-8) margins: 8, 31, 8, 8 minimum size: 1444x418 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=1460,457 maxtrack=0,0)</p>
<p>error: Application does NOT exists [C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/bin/./python-real.exe]</p>
<p>Usage</p>
<p>PythonSlicer [options]</p>
<p>Options</p>
<p>–launcher-help Display help</p>
<p>–launcher-version Show launcher version information</p>
<p>–launcher-verbose Verbose mode</p>

---

## Post #6 by @Ben (2024-10-27 15:32 UTC)

<p>Cont…</p>
<p>–launch Specify the application to launch</p>
<p>–launcher-detach Launcher will NOT wait for the application to finish</p>
<p>–launcher-no-splash Hide launcher splash</p>
<p>–launcher-timeout Specify the time in second before the launcher kills the application. -1 means no timeout (default: -1)</p>
<p>–launcher-load-environment Specify the saved environment to load.</p>
<p>–launcher-dump-environment Launcher will print environment variables to be set, then exit</p>
<p>–launcher-show-set-environment-commands Launcher will print commands suitable for setting the parent environment (i.e. using ‘eval’ in a POSIX shell), then exit</p>
<p>–launcher-additional-settings Additional settings file to consider</p>
<p>–launcher-additional-settings-exclude-groups Comma separated list of settings groups that should NOT be overwritten by values in User and Additional settings. For example: General,Application,ExtraApplicationToLaunch</p>
<p>–launcher-ignore-user-additional-settings Ignore additional user settings</p>
<p>–launcher-generate-exec-wrapper-script Generate executable wrapper script allowing to set the environment</p>
<p>–launcher-generate-template Generate an example of setting file</p>
<p>Traceback (most recent call last):</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 717, in setupPythonRequirements</p>
<p>import pandas</p>
<p>ModuleNotFoundError: No module named ‘pandas’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 274, in onApplyButton</p>
<p>self.logic.setupPythonRequirements()</p>
<p>File “C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 719, in setupPythonRequirements</p>
<p>slicer.util.pip_install(“pandas”)</p>
<p>File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3887, in pip_install</p>
<p>_executePythonModule(“pip”, args)</p>
<p>File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3848, in _executePythonModule</p>
<p>logProcessOutput(proc)</p>
<p>File “C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3814, in logProcessOutput</p>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>subprocess.CalledProcessError: Command ‘[‘C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pandas’]’ returned non-zero exit status 1.</p>
<p>[Python] Failed to install required packages.</p>
<p>[Python] Command ‘[‘C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pandas’]’ returned non-zero exit status 1.</p>
<p>[Qt] Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/32448/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png" rel="noopener nofollow ugc">http://wiki.slicer.org/slicerWiki/images/2/2a/CarreraSliceEffect.png</a>’. This content should also be served over HTTPS.</p>

---

## Post #7 by @lassoan (2024-10-27 16:59 UTC)

<aside class="quote no-group" data-username="Ben" data-post="5" data-topic="39880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ben/48/78311_2.png" class="avatar"> Ben:</div>
<blockquote>
<p>error: Application does NOT exists [C:/Users/User/AppData/Local/slicer.org/Slicer 5.6.2/bin/./python-real.exe]</p>
</blockquote>
</aside>
<p>This is an important message.</p>
<p><strong>Does this file exist on your computer?</strong></p>
<pre><code>C:\Users\User\AppData\Local\slicer.org\Slicer 5.6.2\bin\python-real.exe
</code></pre>
<p>(I guess you need to replace <code>User</code> by your actual username)</p>
<p><strong>Does your username contain special (non-ASCII) characters?</strong></p>

---

## Post #8 by @jamesobutler (2024-10-27 17:00 UTC)

<p>Or has Windows Defender or other antivirus incorrectly quarantined python-real.exe making it no longer exist at that location?</p>

---

## Post #9 by @Ben (2024-10-27 23:26 UTC)

<p>Yes, thanks. I have Norton, it probably blocked some actions in the installation.<br>
I can find the file in the folder.</p>
<p>I reinstalled Slicer 5.6.2, and PyTorch, giving it an exception for Norton’s blocking action<br>
Can install PyTorch version 1.81<br>
Uninstalled 1.81 and reinstall with “&gt;1.12” in the version requirement<br>
Again give an exception for Norton’s blocking action<br>
Then I received the following error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4746d9d8ec240927700cc68346a9ac02c7f68934.jpeg" data-download-href="/uploads/short-url/aaxHgInAHj7ymbWuPlfqgVcyKNe.jpeg?dl=1" title="2024-10-28_071534" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4746d9d8ec240927700cc68346a9ac02c7f68934_2_690x235.jpeg" alt="2024-10-28_071534" data-base62-sha1="aaxHgInAHj7ymbWuPlfqgVcyKNe" width="690" height="235" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4746d9d8ec240927700cc68346a9ac02c7f68934_2_690x235.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4746d9d8ec240927700cc68346a9ac02c7f68934.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4746d9d8ec240927700cc68346a9ac02c7f68934.jpeg 2x" data-dominant-color="D7D7D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-10-28_071534</span><span class="informations">941×321 61.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1110f2b999ce32b1daf7c2f976df19fe2b029e3.jpeg" data-download-href="/uploads/short-url/tPul7kKB9pxvYxANqADakjfuYGD.jpeg?dl=1" title="2024-10-28_071601" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1110f2b999ce32b1daf7c2f976df19fe2b029e3_2_690x254.jpeg" alt="2024-10-28_071601" data-base62-sha1="tPul7kKB9pxvYxANqADakjfuYGD" width="690" height="254" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1110f2b999ce32b1daf7c2f976df19fe2b029e3_2_690x254.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1110f2b999ce32b1daf7c2f976df19fe2b029e3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1110f2b999ce32b1daf7c2f976df19fe2b029e3.jpeg 2x" data-dominant-color="D0D0D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2024-10-28_071601</span><span class="informations">953×351 64.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @jamesobutler (2024-12-18 15:47 UTC)

<p><a class="mention" href="/u/ben">@Ben</a>, in the screenshots that you provided you are putting the version requirement in the field specifically for <code>torchvision</code>, but if you are wanting to install the <code>torch</code> package, please place the “&gt;=1.12” into the “Torch version requirement” field and try again.</p>

---
