# Issue with DebuggingTools Module on 3D Slicer (v5.6.2 r32448) on Ubuntu 22.04

**Topic ID**: 40339
**Date**: 2024-11-23
**URL**: https://discourse.slicer.org/t/issue-with-debuggingtools-module-on-3d-slicer-v5-6-2-r32448-on-ubuntu-22-04/40339

---

## Post #1 by @shahrokh (2024-11-23 07:14 UTC)

<p><strong>Hello Dear Developers and Users,</strong></p>
<p>Excuse me for asking a question that might be obvious to many:</p>
<p>I have installed the <strong>DebuggingTools</strong> module on 3DSlicer <strong>version 5.6.2 r32448</strong> on <strong>Ubuntu 22.04</strong> .<br>
I also installed <strong>PyCharm 2024.2.4 (Professional Edition)</strong> , with its executable located in the following path:<br>
<code>/home/sn/pycharm-2024.2.4/bin/pycharm.sh</code></p>
<p>Additionally, its <strong>egg file</strong> is located here:<br>
<code>/home/sn/pycharm-2024.2.4/debug-eggs/pydevd-pycharm.egg</code></p>
<p>I have tried to follow the setup instructions from the <strong>SlicerDebuggingTools</strong> page on GitHub:</p>
<p><strong>Title</strong> : GitHub - SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing various tools for module development and debugging<br>
<strong>Address</strong> : <a href="https://github.com/SlicerRt/SlicerDebuggingTools" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing various tools for module development and debugging</a></p>
<p>I checked that the installed PyCharm also includes the <strong>remote debug server</strong> .<br>
As shown in the image below, I cannot select the path to the <strong>pydevd-pycharm.egg</strong> file in the DebuggingTools module (I don’t have the Browse option in the <strong>Debugger</strong> section of this module.), and 3DSlicer also fails to automatically detect the location of this file.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cae4efb6b6821208a3b886abe95415ae18adfe3.png" data-download-href="/uploads/short-url/6ngsHJqqrqprOMqWM9v1tvXoZSb.png?dl=1" title="Screenshot from 2024-11-23 09-51-42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cae4efb6b6821208a3b886abe95415ae18adfe3.png" alt="Screenshot from 2024-11-23 09-51-42" data-base62-sha1="6ngsHJqqrqprOMqWM9v1tvXoZSb" width="425" height="307"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-11-23 09-51-42</span><span class="informations">425×307 22.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To solve this problem, I have tried the following steps, but none of them worked and my issue remains unresolved.<br>
<strong>Step 1</strong> : Added the path of this file to the <strong>PATH</strong> variable and included it in the <strong>~/.bashrc</strong> file.<br>
<code>export PATH=$PATH:/home/sn/pycharm-2024.2.4/debug-eggs/</code></p>
<p><strong>Step 2</strong> : Added the path of this file to the <strong>PYTHONPATH</strong> variable.<br>
<code>export PYTHONPATH=/home/sn/pycharm-2024.2.4/debug-eggs</code></p>
<p>Additionally, as shown in the image below…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43819efaf5f70b5ff6a6ce1e0b4bbf0257c939e3.png" data-download-href="/uploads/short-url/9DbHxw6CRFxzEB989xJO57skGfp.png?dl=1" title="Screenshot from 2024-11-23 10-41-04" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43819efaf5f70b5ff6a6ce1e0b4bbf0257c939e3_2_690x388.png" alt="Screenshot from 2024-11-23 10-41-04" data-base62-sha1="9DbHxw6CRFxzEB989xJO57skGfp" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43819efaf5f70b5ff6a6ce1e0b4bbf0257c939e3_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43819efaf5f70b5ff6a6ce1e0b4bbf0257c939e3_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43819efaf5f70b5ff6a6ce1e0b4bbf0257c939e3_2_1380x776.png 2x" data-dominant-color="303136"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-11-23 10-41-04</span><span class="informations">1920×1080 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The following command was also executed:<br>
<code>pip install pydevd-pycharm~=242.23726.102</code></p>
<p>I also did not see any option called <strong>Debugger</strong> or similar in the <strong>Application Settings</strong> section of 3DSlicer.<br>
Please guide me on what I should do so that 3DSlicer can recognize the location of the <strong>pydevd-pycharm.egg</strong> file, allowing me to use PyCharm’s debugging features for module development.</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #2 by @shahrokh (2024-11-23 11:44 UTC)

<p>Dear all,</p>
<p>I wanted to share an update regarding the issue I raised earlier about setting up PyCharm debugging with 3D Slicer.</p>
<p>I noticed that in the version of <strong>5.0.2 r30822 / a4420c3</strong>, the option to specify the <strong>PyCharm debug egg path</strong> is available under the <strong>Settings</strong> section of the <strong>Python debugger</strong> module, as shown in the screenshot below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91d703e128440447a9463d28b33a25db8cef088a.png" data-download-href="/uploads/short-url/kO9TRFxqqZHjTjKRf98ygG7L3w6.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91d703e128440447a9463d28b33a25db8cef088a_2_690x393.png" alt="1" data-base62-sha1="kO9TRFxqqZHjTjKRf98ygG7L3w6" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91d703e128440447a9463d28b33a25db8cef088a_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91d703e128440447a9463d28b33a25db8cef088a_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91d703e128440447a9463d28b33a25db8cef088a_2_1380x786.png 2x" data-dominant-color="727279"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1851×1056 69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
As mentioned on the website here:</p>
<ul>
<li><strong>Title</strong> : GitHub - SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing various tools for module development and debugging</li>
<li><strong>Address</strong> : <a href="https://github.com/SlicerRt/SlicerDebuggingTools" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing various tools for module development and debugging</a></li>
</ul>
<p>To start debugging, I need to first <strong>Run</strong> <em>Slicer remote debugger</em> option from the <strong>Run</strong> menu in PyCharm.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99b56d8320fc68665e3644f35968d7883744328f.png" data-download-href="/uploads/short-url/lVLL8f8t9WrMoRJKsorHzDYd7Eb.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99b56d8320fc68665e3644f35968d7883744328f_2_690x58.png" alt="2" data-base62-sha1="lVLL8f8t9WrMoRJKsorHzDYd7Eb" width="690" height="58" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99b56d8320fc68665e3644f35968d7883744328f_2_690x58.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99b56d8320fc68665e3644f35968d7883744328f_2_1035x87.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99b56d8320fc68665e3644f35968d7883744328f_2_1380x116.png 2x" data-dominant-color="2E2F34"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1850×158 51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After that, in 3D Slicer, open the <em>Python debugger</em> module and click <em>Connect to debug server</em> .<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b197b95d09248ecb8fb211fb448c0652457c139a.png" data-download-href="/uploads/short-url/pl3zVZA3DfUzu8sZxYmLGJCnXM6.png?dl=1" title="Screenshot 2024-11-23 14:47:51" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b197b95d09248ecb8fb211fb448c0652457c139a_2_690x392.png" alt="Screenshot 2024-11-23 14:47:51" data-base62-sha1="pl3zVZA3DfUzu8sZxYmLGJCnXM6" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b197b95d09248ecb8fb211fb448c0652457c139a_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b197b95d09248ecb8fb211fb448c0652457c139a_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b197b95d09248ecb8fb211fb448c0652457c139a_2_1380x784.png 2x" data-dominant-color="6A6B72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-11-23 14:47:51</span><span class="informations">1855×1056 81.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, as I mentioned in my previous issue, the <strong>PyCharm debug egg path</strong> option is not available in the new version of 3DSlicer <strong>5.6.2 r32448 / f10cd8c</strong>.</p>
<p>Best regards.<br>
Shahrokh</p>

---
