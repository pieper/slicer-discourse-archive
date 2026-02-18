# How to make module modification take effect without restarting the application?

**Topic ID**: 38420
**Date**: 2024-09-18
**URL**: https://discourse.slicer.org/t/how-to-make-module-modification-take-effect-without-restarting-the-application/38420

---

## Post #1 by @dingdanpeng (2024-09-18 08:09 UTC)

<p>Operating system:Win11<br>
Slicer version:5.7.0<br>
Every time I modify the plug code, I need to restart the software for it to take effect. Pressing reload does not work. This is because only restart Slicer can take effect or there are other issues?</p>
<p>Expected behavior:reload and The modified code will take effect<br>
Actual behavior:only restart slicer can take effect</p>

---

## Post #2 by @muratmaga (2024-09-18 15:02 UTC)

<p>If this is python code, you can enable the developer mode (Edit-&gt;Application Settings), and you can reload the module source code, without having to restart the Slicer application.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be3770ca1f8569a4a6d1bc628ce523d9180988a7.png" data-download-href="/uploads/short-url/r8Jv16TedLBAboZDjoWFp1MZC9F.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3770ca1f8569a4a6d1bc628ce523d9180988a7_2_690x84.png" alt="image" data-base62-sha1="r8Jv16TedLBAboZDjoWFp1MZC9F" width="690" height="84" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3770ca1f8569a4a6d1bc628ce523d9180988a7_2_690x84.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be3770ca1f8569a4a6d1bc628ce523d9180988a7_2_1035x126.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be3770ca1f8569a4a6d1bc628ce523d9180988a7.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1092×134 10.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @cpinter (2024-09-18 15:08 UTC)

<aside class="quote no-group" data-username="dingdanpeng" data-post="1" data-topic="38420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/b77776/48.png" class="avatar"> dingdanpeng:</div>
<blockquote>
<p>Pressing reload does not work.</p>
</blockquote>
</aside>
<p>It does work, so maybe there is something different in your way of using it. A very basic question is whether you have the same folder added to Additional module directories as what you are changing? Because if you built it and you set the <code>qt-scripted-modules</code> folder in the build directory, then it only gets refreshed if you do a build or manually copy the Python file (this is why it would help a lot receiving more details in the report, so that one does not have to guess around). Can you please give details about how you store your module code and what folder did you add to Slicer? Also, can you tell us what appears in the Python window when you press Reload? Thanks!</p>

---

## Post #4 by @dingdanpeng (2024-09-19 01:54 UTC)

<p><strong>I don’t have the qt-scripted-modules folder like the other extensions.</strong><br>
<strong>Here is the extension path I added to 3D slicer.</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce453f4a3d6b08ec7f35e3a0d5c24f6d4031bbc.png" data-download-href="/uploads/short-url/A5bvNIpjBApG2DlrjAq6SvRQgSo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce453f4a3d6b08ec7f35e3a0d5c24f6d4031bbc.png" alt="image" data-base62-sha1="A5bvNIpjBApG2DlrjAq6SvRQgSo" width="690" height="151" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1081×237 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3d4e1e8afd79badeca3145b6be32db095a316a3.png" data-download-href="/uploads/short-url/pERz4OX6fWlRFtfThoM283hNbX5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3d4e1e8afd79badeca3145b6be32db095a316a3.png" alt="image" data-base62-sha1="pERz4OX6fWlRFtfThoM283hNbX5" width="690" height="374" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">760×412 16.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>When i press reload,the Python window appear:</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/472f73e456edf15ffc4492df7a883879b8713888.png" data-download-href="/uploads/short-url/a9JzaTa1zxu6dZdc27okgwV1L16.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/472f73e456edf15ffc4492df7a883879b8713888.png" alt="image" data-base62-sha1="a9JzaTa1zxu6dZdc27okgwV1L16" width="690" height="157" data-dominant-color="FCF7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1111×254 10.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe there’s something wrong with my add path, but how do I set it up correctly ? Thanks!</p>

---

## Post #5 by @dingdanpeng (2024-09-19 01:56 UTC)

<p>I have enabled  the developer mode.This more details:<br>
<strong>I don’t have the qt-scripted-modules folder like the other extensions.</strong><br>
<strong>Here is the extension path I added to 3D slicer.</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce453f4a3d6b08ec7f35e3a0d5c24f6d4031bbc.png" data-download-href="/uploads/short-url/A5bvNIpjBApG2DlrjAq6SvRQgSo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce453f4a3d6b08ec7f35e3a0d5c24f6d4031bbc.png" alt="image" data-base62-sha1="A5bvNIpjBApG2DlrjAq6SvRQgSo" width="690" height="151" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1081×237 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3d4e1e8afd79badeca3145b6be32db095a316a3.png" data-download-href="/uploads/short-url/pERz4OX6fWlRFtfThoM283hNbX5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3d4e1e8afd79badeca3145b6be32db095a316a3.png" alt="image" data-base62-sha1="pERz4OX6fWlRFtfThoM283hNbX5" width="690" height="374" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">760×412 16.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>When i press reload,the Python window appear:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/472f73e456edf15ffc4492df7a883879b8713888.png" data-download-href="/uploads/short-url/a9JzaTa1zxu6dZdc27okgwV1L16.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/472f73e456edf15ffc4492df7a883879b8713888.png" alt="image" data-base62-sha1="a9JzaTa1zxu6dZdc27okgwV1L16" width="690" height="157" data-dominant-color="FCF7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1111×254 10.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe there’s something wrong with my add path, but how do I set it up correctly ? Thanks!</p>

---

## Post #6 by @cpinter (2024-09-19 08:38 UTC)

<p>Thanks for the information! The problem probably will be that you have a lib folder, and the reload function only reloads the module Python file.</p>

---

## Post #7 by @JASON (2024-09-30 21:43 UTC)

<p>So the ‘Reload’ button reloads your Module class, but not the external scripts that your class references.  The way around this is to manually reload in your module’s init method.</p>
<pre><code class="lang-auto">    def __init__(self, parent=None) -&gt; None:
        """Called when the user opens the module the first time and the widget is initialized."""
        ScriptedLoadableModuleWidget.__init__(self, parent)
        VTKObservationMixin.__init__(self)
        
        import importlib
        import lib
        importlib.reload(lib.dataTransfer)
        importlib.reload(lib.segmentExplorer)
</code></pre>

---
