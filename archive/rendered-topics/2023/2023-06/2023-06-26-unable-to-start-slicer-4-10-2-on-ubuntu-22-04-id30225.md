# Unable to start Slicer 4.10.2 on Ubuntu 22.04

**Topic ID**: 30225
**Date**: 2023-06-26
**URL**: https://discourse.slicer.org/t/unable-to-start-slicer-4-10-2-on-ubuntu-22-04/30225

---

## Post #1 by @jhlegarreta (2023-06-26 02:14 UTC)

<p>Hi,<br>
I have downloaded 3D Slicer 4.10.2 from this data archive:<br>
<a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482</a></p>
<p>(it was the only place I found with legacy releases).</p>
<p>And uncompressed the ZIP file to folder of my choice. When trying to start the application, the splash screen is shown for a few seconds, but then the process terminates with the following error:</p>
<pre><code class="lang-auto">me@machine:/opt/Slicer-4.10.2-linux-amd64$ ./Slicer 
error: [/opt/Slicer-4.10.2-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>Can I expect an old release to work on a more recent OS version? If yes, Is there, is there a location where Slicer keeps a log of the events or an error trace so that I can share it?</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-06-26 13:14 UTC)

<p>In general yes, old releases should still work, but some sometimes the OS changes.  I’ve had very old executables work on windows, so maybe try that instead of linux.</p>

---

## Post #3 by @jhlegarreta (2023-06-26 13:54 UTC)

<p>Unfortunately, trying this on Windows is really not an option in this case/for me.</p>

---

## Post #4 by @RafaelPalomar (2023-06-26 14:48 UTC)

<p><a class="mention" href="/u/jhlegarreta">@jhlegarreta</a>, maybe you should try to build Slicer yourself, but be aware that this will probably require some patching. I don’t think it will compile out-of-the-box</p>

---

## Post #5 by @jhlegarreta (2023-06-26 14:53 UTC)

<p>Sorry Rafael, but I am willing to avoid trying to build it myself, even more so if chances are that I will run into other issues.</p>
<p>But thanks for the suggestion and the support.</p>

---

## Post #6 by @pieper (2023-06-26 17:06 UTC)

<p>If you want to get an idea where the binary failing to start on linux you can start a shell with the environment variables set, something like:<br>
<code>./Slicer --launch xterm</code><br>
and then in the new window try:<br>
<code>sudo strace Slicer</code><br>
If you look at the end of the output you’ll see what happened before it crashes.  If it’s a missing file or similar you may be able to make things work.</p>
<p>Alternatively you might just run an older linux version in a docker container.  You could tunnel the X display to show the old slicer on your newer desktop.  It’s a bit of an ugly workaround but it might get you past whatever issue you are seeing.</p>
<p>As a general rule we only support the current releases to avoid diverting our efforts too much.</p>

---

## Post #7 by @jhlegarreta (2023-06-26 19:23 UTC)

<p>Thanks for the effort Steve.</p>
<p>I am attaching two files for the sake of completeness:</p>
<ul>
<li>First one (could only get a screenshot, sorry) corresponds to the terminal messages I get when running <code>./Slicer --launch xterm</code>. Of course, on my Ubuntu 22.04 I do not have Python 2.7, but I assume Slicer bundles its own interpreter (even if 2.7 seems old for a 2019 4.2.10 release). Installing 2.7 is not an option if that is the main issue.</li>
<li>Second one (dropbox link; current discourse instance does not allow uploading text files) corresponds to the messages I get when running <code>sudo strace Slicer</code>. Not sure what the <code> BadShmSeg (invalid shared segment parameter)</code> message means, but it does not look straightforward to debug. There are other errors in the trace that seem equally hard to me to guess what they mean/how to fix them. All seem related to X11 windowing system.</li>
</ul>
<blockquote>
<p>Alternatively you might just run an older linux version in a docker container</p>
</blockquote>
<p>If this involves building the docker image myself, I do not think this is doable given some constraints I have.</p>
<blockquote>
<p>As a general rule we only support the current releases to avoid diverting our efforts too much.</p>
</blockquote>
<p>I completely understand, so if things do not seem they can be fixed easily, I would understand not continuing to put time on this on your side.</p>
<p>Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47ffa8db6f59b53a70e0a413b804b172561254e2.png" data-download-href="/uploads/short-url/agVEd5dvZCnKkiX9jzfbYSliCfE.png?dl=1" title="slicer_xtem_launch" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47ffa8db6f59b53a70e0a413b804b172561254e2_2_345x170.png" alt="slicer_xtem_launch" data-base62-sha1="agVEd5dvZCnKkiX9jzfbYSliCfE" width="345" height="170" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47ffa8db6f59b53a70e0a413b804b172561254e2_2_345x170.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47ffa8db6f59b53a70e0a413b804b172561254e2_2_517x255.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47ffa8db6f59b53a70e0a413b804b172561254e2_2_690x340.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_xtem_launch</span><span class="informations">1852×914 19.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/v5kspchfw8ics58/slicer_xterm_log.txt?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/v5kspchfw8ics58/slicer_xterm_log.txt?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img width="160" height="160" src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-file-text-landscape.png" class="thumbnail onebox-avatar">

<h3><a href="https://www.dropbox.com/s/v5kspchfw8ics58/slicer_xterm_log.txt?dl=0" target="_blank" rel="noopener nofollow ugc">slicer_xterm_log.txt</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @jamesobutler (2023-06-26 19:34 UTC)

<p>I assume using Slicer 4.10.2 is because it had DTI extensions available and latest Slicer does not have this extensions (re <a href="https://discourse.slicer.org/t/previously-available-extensions-no-longer-available-on-5-2-2/30226/2" class="inline-onebox">Previously available extensions no longer available on 5.2.2 - #2 by jamesobutler</a>) . It would be great if you can try getting those DTI extensions working with latest Slicer.</p>

---

## Post #9 by @jhlegarreta (2023-06-26 19:47 UTC)

<blockquote>
<p>I assume using Slicer 4.10.2 is because it had DTI extensions available and latest Slicer does not have this extensions (re <a href="https://discourse.slicer.org/t/previously-available-extensions-no-longer-available-on-5-2-2/30226/2">Previously available extensions no longer available on 5.2.2 - #2 by jamesobutler</a>) .</p>
</blockquote>
<p>Using Slicer 4.10.2 was probably just due to the fact that at the time it was the version they had working on their systems, for sure before Ubuntu 22.04 was available, and probably on a different OS (most likely macOS).</p>
<blockquote>
<p>It would be great if you can try getting those DTI extensions working with latest Slicer.</p>
</blockquote>
<p>I ignore the effort that this requires, and if I need to do this in my spare time, then I simply may not have the bandwidth; I am already a contributor/maintainer on a number of other open-source projects that also require time.</p>

---

## Post #10 by @jcfr (2023-06-26 21:40 UTC)

<p>To avoid issue related to virtual env wrapper, you may introduce a variable called <code>VIRTUALENV_DISABLED</code>.</p>
<p>For example, see</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/jcfr/dotfiles/blob/088697a0a16b0ce4cc785aab0b7f09665d55260d/.exports#L8-L19">
  <header class="source">

      <a href="https://github.com/jcfr/dotfiles/blob/088697a0a16b0ce4cc785aab0b7f09665d55260d/.exports#L8-L19" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/jcfr/dotfiles/blob/088697a0a16b0ce4cc785aab0b7f09665d55260d/.exports#L8-L19" target="_blank" rel="noopener">jcfr/dotfiles/blob/088697a0a16b0ce4cc785aab0b7f09665d55260d/.exports#L8-L19</a></h4>



    <pre class="onebox"><code class="lang-exports">
      <ol class="start lines" start="8" style="counter-reset: li-counter 7 ;">
          <li># virtualenvwrapper</li>
          <li>if [[ $VIRTUALENV_DISABLED ]];</li>
          <li>then</li>
          <li>  echo "Skipping VirtualEnv initialization"</li>
          <li>else</li>
          <li>  export WORKON_HOME=$HOME/.virtualenvs</li>
          <li>  export PROJECT_HOME=$HOME/Projects</li>
          <li>  # shellcheck disable=SC2034</li>
          <li>  VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3</li>
          <li>  # shellcheck source=/dev/null</li>
          <li>  source /usr/local/bin/virtualenvwrapper.sh</li>
          <li>fi</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bad9b7c14aea2bf2ffca96d452a6547aca8aa5d.png" data-download-href="/uploads/short-url/jVEjROgkLcJVPXyvuQkRzXeRQ1T.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bad9b7c14aea2bf2ffca96d452a6547aca8aa5d_2_690x407.png" alt="image" data-base62-sha1="jVEjROgkLcJVPXyvuQkRzXeRQ1T" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bad9b7c14aea2bf2ffca96d452a6547aca8aa5d_2_690x407.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bad9b7c14aea2bf2ffca96d452a6547aca8aa5d_2_1035x610.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bad9b7c14aea2bf2ffca96d452a6547aca8aa5d.png 2x" data-dominant-color="E1DFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1211×715 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @jhlegarreta (2023-06-27 15:13 UTC)

<p>Thanks for the tip JC. Although that indeed fixes the xterm launch error, the second command (<code>sudo strace Slicer</code>) still produces the same error as in the earlier post.</p>

---

## Post #12 by @pieper (2023-06-27 22:37 UTC)

<p>Sorry, that was a typo on my part.  After launch in the new shell try <code>sudo strace SlicerApp-real</code></p>

---

## Post #13 by @jhlegarreta (2023-06-28 14:58 UTC)

<p>Thanks for the effort Steve.</p>
<p>It looks like Slicer is unable to find some shared libraries/expect them to be somewhere where they are not. Not sure how this can be approached.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e7e421b27690346f148d2fe0e899aba010595a0.png" data-download-href="/uploads/short-url/i30FqRQ0vHLC0CvH6NmHTdGWa8o.png?dl=1" title="slicer_4-10-2_ubuntu_22-04_start_issue_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e7e421b27690346f148d2fe0e899aba010595a0.png" alt="slicer_4-10-2_ubuntu_22-04_start_issue_1" data-base62-sha1="i30FqRQ0vHLC0CvH6NmHTdGWa8o" width="690" height="392" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_4-10-2_ubuntu_22-04_start_issue_1</span><span class="informations">1856×1055 32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08034b567c0859a8f539ee5eeefa423d66432040.png" data-download-href="/uploads/short-url/18SSq2XjD8Goo9XkHCWeINJafHW.png?dl=1" title="slicer_4-10-2_ubuntu_22-04_start_issue_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08034b567c0859a8f539ee5eeefa423d66432040.png" alt="slicer_4-10-2_ubuntu_22-04_start_issue_2" data-base62-sha1="18SSq2XjD8Goo9XkHCWeINJafHW" width="690" height="392" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_4-10-2_ubuntu_22-04_start_issue_2</span><span class="informations">1856×1055 31.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @pieper (2023-06-28 19:58 UTC)

<p>Did you do this part:</p>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="30225">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><code>./Slicer --launch xterm</code><br>
and then in the <strong>new window</strong> try:</p>
</blockquote>
</aside>
<p>(corrected)</p>
<pre><code class="lang-auto">strace SlicerApp-real
</code></pre>

---

## Post #15 by @jhlegarreta (2023-06-28 20:04 UTC)

<blockquote>
<p>Did you do this part:</p>
</blockquote>
<p>Sorry Steve, yes.</p>

---
