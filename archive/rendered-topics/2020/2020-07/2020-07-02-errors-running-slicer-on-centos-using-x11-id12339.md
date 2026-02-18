# Errors Running Slicer on CentOS using X11

**Topic ID**: 12339
**Date**: 2020-07-02
**URL**: https://discourse.slicer.org/t/errors-running-slicer-on-centos-using-x11/12339

---

## Post #1 by @lennymartinez (2020-07-02 15:49 UTC)

<p>Got Slicer 4.11 installed on a CentOS remote machine mainly to be used for processing. It was working fine the first week, but something seems to have happened in between, or we didn’t notice what was up then.</p>
<p>Ideally we’ll be running Slicer with the --no-main-window and --no-splash flag and using a --python-script to do our processing, <strong>but</strong> when I try running Slicer by itself I get the following errors:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef6e9db29d5f52cb9ade2754b471005ccfa05558.png" data-download-href="/uploads/short-url/ya76LwNyUzxfnq3orqj0ROoiEME.png?dl=1" title="Screenshot 2020-07-02 11.21.16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef6e9db29d5f52cb9ade2754b471005ccfa05558.png" alt="Screenshot 2020-07-02 11.21.16" data-base62-sha1="ya76LwNyUzxfnq3orqj0ROoiEME" width="689" height="139" data-dominant-color="152535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-07-02 11.21.16</span><span class="informations">1292×262 19.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The splash window does pop up, and modules are loaded, and then it tries to show the welcome module, but all I get is this on the command line<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0eee6b7bc16f644026be8cfc766ff2fddb07f28b.png" data-download-href="/uploads/short-url/285uNBe3GLaunmPqBhCERMFYPQT.png?dl=1" title="Screenshot 2020-07-02 11.22.36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0eee6b7bc16f644026be8cfc766ff2fddb07f28b.png" alt="Screenshot 2020-07-02 11.22.36" data-base62-sha1="285uNBe3GLaunmPqBhCERMFYPQT" width="690" height="353" data-dominant-color="152535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-07-02 11.22.36</span><span class="informations">1108×568 40.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After a while of this, Slicer GUI screen container pops up, but it’s empty and the command line repeats the same error over and over:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a053692c6a950ce97146a558370567934953574.png" data-download-href="/uploads/short-url/f7TMqlCOwTQaFqdoC7xr4Cy9QFu.png?dl=1" title="Screenshot 2020-07-01 11.26.20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a053692c6a950ce97146a558370567934953574_2_690x492.png" alt="Screenshot 2020-07-01 11.26.20" data-base62-sha1="f7TMqlCOwTQaFqdoC7xr4Cy9QFu" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a053692c6a950ce97146a558370567934953574_2_690x492.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a053692c6a950ce97146a558370567934953574_2_1035x738.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a053692c6a950ce97146a558370567934953574_2_1380x984.png 2x" data-dominant-color="FBFCFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-07-01 11.26.20</span><span class="informations">1690×1206 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a5803d11cfdb0b4e22436dc6251394fa512fbfd.jpeg" data-download-href="/uploads/short-url/8k8gocpLSSHYXfielioYwwgQVIh.jpeg?dl=1" title="Screenshot 2020-07-01 11.25.08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a5803d11cfdb0b4e22436dc6251394fa512fbfd_2_358x499.jpeg" alt="Screenshot 2020-07-01 11.25.08" data-base62-sha1="8k8gocpLSSHYXfielioYwwgQVIh" width="358" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a5803d11cfdb0b4e22436dc6251394fa512fbfd_2_358x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a5803d11cfdb0b4e22436dc6251394fa512fbfd_2_537x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a5803d11cfdb0b4e22436dc6251394fa512fbfd_2_716x998.jpeg 2x" data-dominant-color="223140"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-07-01 11.25.08</span><span class="informations">948×1322 470 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried looking into the initial libGL errors, and I can find swrast on the machine. I can’t find the fbConfigs or visuals the command line is talking about. I tried finding the OpenGL version but have been unlucky.<br>
And I have no idea what happened next or how to fix it.</p>
<p>Do anyone have tips on how I can install and run Slicer on a CentOs machine? Everything in the processing pipeline with the extension works and this is the last step where things are going wrong.</p>

---

## Post #2 by @lassoan (2020-07-02 16:15 UTC)

<p>Does other OpenGL applications, such as the standard <code>glxgears</code> demo work on your computer?</p>

---

## Post #3 by @lennymartinez (2020-07-02 16:38 UTC)

<p>It does not. I get the following errors<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d61e826e3148cd9fd7b5fe5d1a6c2e3b07e190c8.png" data-download-href="/uploads/short-url/uybxMQuHbx4ucNHySLiQjDtPYQE.png?dl=1" title="Screenshot 2020-07-02 12.37.23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d61e826e3148cd9fd7b5fe5d1a6c2e3b07e190c8_2_690x160.png" alt="Screenshot 2020-07-02 12.37.23" data-base62-sha1="uybxMQuHbx4ucNHySLiQjDtPYQE" width="690" height="160" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d61e826e3148cd9fd7b5fe5d1a6c2e3b07e190c8_2_690x160.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d61e826e3148cd9fd7b5fe5d1a6c2e3b07e190c8_2_1035x240.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d61e826e3148cd9fd7b5fe5d1a6c2e3b07e190c8_2_1380x320.png 2x" data-dominant-color="112231"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-07-02 12.37.23</span><span class="informations">2028×472 74.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2020-07-02 16:40 UTC)

<p>If you are running no-main-window anyway you can use <a href="https://xpra.org/trac/wiki/Xdummy">Xdummy</a> or <a href="https://en.wikipedia.org/wiki/Xvfb">xvfb</a> to fake the connection.</p>

---

## Post #5 by @muratmaga (2020-07-02 16:51 UTC)

<p>You are using a X11 server that doesn’t support GLX extension that is required to run openGL libraries on X11 clients.</p>
<p>If you don’t need the GUI, <a class="mention" href="/u/pieper">@pieper</a>’s suggestions should work. If you eventually need the GUI, VirtualGL (<a href="https://virtualGL.org" rel="nofollow noopener">https://virtualGL.org</a>) works really well on centos 7 (I haven’t tested 8 yet).</p>

---

## Post #6 by @lennymartinez (2020-07-02 16:52 UTC)

<p>Don’t need a GUI in the end, so I’ll check out Xdummy and xvfb! Thanks for the recommendations.</p>

---
