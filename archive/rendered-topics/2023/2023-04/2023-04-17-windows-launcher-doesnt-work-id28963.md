# Windows launcher doesn't work

**Topic ID**: 28963
**Date**: 2023-04-17
**URL**: https://discourse.slicer.org/t/windows-launcher-doesnt-work/28963

---

## Post #1 by @Kening_Zhang (2023-04-17 13:19 UTC)

<p>I was trying for calling a module from cli but doesn’t work.<br>
I tried two ways, one was directly calling the module exe, but it shown many dll files missing.<br>
Then I tried to use launcher but it doesn’t give any output.<br>
“C:\Users\13956\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerDMRI\lib\Slicer-5.2\cli-modules\FiberTractMeasurements.exe”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc2cc4b15c74b1c134871a6525f5e885ea57cecd.png" alt=")CJVBOEIAD1H1LJTU5_UY(C" data-base62-sha1="qQFGavf8xRWzAivONYy13nsla4R" width="536" height="217"><br>
Sorry about the content of message not in English but it says cannot find vtkDMRI.dll.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b76f4a1807fe9ea4177293a572c77d1940f7626b.png" data-download-href="/uploads/short-url/qaJOrsmuluVCN99Qem4icoH96Nd.png?dl=1" title="OCMZ4T$RKX@(Z9`4JH_VPUN" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b76f4a1807fe9ea4177293a572c77d1940f7626b.png" alt="OCMZ4T$RKX@(Z9`4JH_VPUN" data-base62-sha1="qaJOrsmuluVCN99Qem4icoH96Nd" width="690" height="48" data-dominant-color="131313"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">OCMZ4T$RKX@(Z9`4JH_VPUN</span><span class="informations">1182×83 4.27 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thank you for your help.<br>
Regards,<br>
Kening Zhang</p>

---

## Post #2 by @lassoan (2023-04-17 14:02 UTC)

<p>On Windows, by default the application launcher is built as a Windows GUI application (as opposed to a console application) to avoid opening a console window when starting the application. Therefore, you won’t see any console appearing or any console output when you launch a command with it. See more information <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/tips.html#console-output-on-windows">here</a>.</p>
<h2><a name="p-93655-method-1-1" class="anchor" href="#p-93655-method-1-1" aria-label="Heading link"></a>Method 1</h2>
<p>You can run the CLI using a single command using the <code>--launch</code> argument. If you want to see the output, you can use the <code>| more</code> utility like this (hit arrow key or space to navigate the process output):</p>
<pre><code>"%localappdata%\NA-MIC\Slicer 5.2.2\Slicer.exe" --launch "%localappdata%\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerDMRI\lib\Slicer-5.2\cli-modules\FiberTractMeasurements.exe" --help | more
</code></pre>
<h2><a name="p-93655-method-2-2" class="anchor" href="#p-93655-method-2-2" aria-label="Heading link"></a>Method 2</h2>
<p>Use Slicer launcher to start a console that can display process output:</p>
<pre><code>"%localappdata%\NA-MIC\Slicer 5.2.2\Slicer.exe" --launch %comspec% /c start
</code></pre>
<p>In this console, you can simply run a CLI module by typing its name. For example:</p>
<pre><code>FiberTractMeasurements.exe --help
</code></pre>

---
