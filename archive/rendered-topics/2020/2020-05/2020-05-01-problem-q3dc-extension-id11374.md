---
topic_id: 11374
title: "Problem Q3Dc Extension"
date: 2020-05-01
url: https://discourse.slicer.org/t/11374
---

# Problem Q3DC extension

**Topic ID**: 11374
**Date**: 2020-05-01
**URL**: https://discourse.slicer.org/t/problem-q3dc-extension/11374

---

## Post #1 by @crisandr (2020-05-01 03:25 UTC)

<p>Hello friends, I installed the Q3DC extension in version 4.10.2 and 4.11.0 In the manage extesions menu if I can see the installed extension. but it does not appear in the Quantification section or when looking for it in modules. Help me please</p>

---

## Post #2 by @lassoan (2020-05-01 16:25 UTC)

<p>Please uninstall and install again. Make sure you wait for the “Restart” button to appear and click that (instead of just closing the window). It may take a few minutes if the extension manager website is under heavy load.</p>

---

## Post #3 by @crisandr (2020-05-03 18:44 UTC)

<p>Thanks for your reply Andras Lasso, but I already tried and I continue with the problem. Any other suggestion please?</p>

---

## Post #4 by @lassoan (2020-05-03 19:52 UTC)

<p>We need to be able to reproduce the problem to help with it. Can you save the scene and share it along with a screenshot that shows which input points you selected in Q3DC?</p>
<p>You can upload to dropbox/onedrive/Google drive and post the link here; use data sets that you are allowed to share, such as any of the data sets in SampleData module.</p>

---

## Post #5 by @jamesobutler (2020-05-03 20:06 UTC)

<p>I wonder if it was a failed install of some python packages that get downloaded from PyPI on startup for this extension. As seen in the code below it will download <code>networkx</code> at startup which also requires getting the dependent <code>decorator</code> module.<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/DCBIA-OrthoLab/Q3DCExtension/blob/master/Q3DC/Q3DC.py#L18-L24" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/DCBIA-OrthoLab/Q3DCExtension/blob/master/Q3DC/Q3DC.py#L18-L24" target="_blank" rel="nofollow noopener">DCBIA-OrthoLab/Q3DCExtension/blob/master/Q3DC/Q3DC.py#L18-L24</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="18" style="counter-reset: li-counter 17 ;">
<li># needed for topological sort. Yes, this is basically just DFS.</li>
<li>try:</li>
<li>    import networkx as nx</li>
<li>except ModuleNotFoundError as e:</li>
<li>    # This requires a network connection!</li>
<li>    slicer.util.pip_install('networkx')</li>
<li>    import networkx as nx</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The extension should probably be updated to get these packages at build time like how SlicerRadiomics gets some python packages during the build process to package with the extension. Described in <a href="https://discourse.slicer.org/t/install-python-library-with-extension/10110/8" class="inline-onebox">Install python library with extension</a> or <a href="https://github.com/Radiomics/SlicerRadiomics/blob/e72c856edf80e740102a068b5466a070130155f9/SuperBuild/External_python-pyradiomics.cmake" rel="nofollow noopener">here</a>. <a class="mention" href="/u/james_hoctor">@James_Hoctor</a> or <a class="mention" href="/u/bpaniagua">@bpaniagua</a> , it looks like you’ve been doing some maintenance on this extension. You might want to implement this change in the build process.</p>
<p><a class="mention" href="/u/crisandr">@crisandr</a> Maybe try using PythonSlicer.exe which is found in your Slicer installation to uninstall/reinstall the packages or clear out any failed downloads in a cached location. Did you install Slicer into a writeable location where the use of <code>slicer.util.pip_install("networkx")</code> would succeed when using the python interactor in Slicer?</p>

---

## Post #6 by @James_Hoctor (2020-05-05 14:43 UTC)

<p>I will make this change to Q3DC. Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a> for making an issue for this on Github, and for the links.</p>
<p>If these lines are at fault, then there should be some sort of error message from <code>slicer.util.pip_install</code> printed in the Python Interactor. Does it make sense to ask <a class="mention" href="/u/crisandr">@crisandr</a> to check the Interactor on Slicer startup to try to verify that this is the issue?</p>

---

## Post #7 by @crisandr (2020-05-08 01:13 UTC)

<p>Thanks for your responses, I used ashampoo uninstaller to clear all installation logs, reinstall the program and extension, then restart Slicer3d and the antivirus detected a threat but check as an exception.</p>
<p>I don’t know if that has anything to do with it but it already works</p>
<p>                    <a href="https://dl.dropboxusercontent.com/s/1jkep39q6yhi42w/slicer3d%20excepci%C3%B3n.jpg?dl=0" target="_blank" rel="nofollow noopener" class="onebox">
            <img src="https://dl.dropboxusercontent.com/s/1jkep39q6yhi42w/slicer3d%20excepci%C3%B3n.jpg?dl=0" width="682" height="211">
          </a>

</p>

---

## Post #8 by @jcfr (2020-05-21 05:20 UTC)

<aside class="quote no-group" data-username="crisandr" data-post="1" data-topic="11374">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/crisandr/48/6738_2.png" class="avatar"> crisandr:</div>
<blockquote>
<p>it does not appear in the Quantification section</p>
</blockquote>
</aside>
<p>It is available when typing <code>Q3DC</code> in the search box on the top right or when going to the “Shape Analysis” category</p>
<aside class="quote no-group quote-modified" data-username="crisandr" data-post="1" data-topic="11374">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/crisandr/48/6738_2.png" class="avatar"> crisandr:</div>
<blockquote>
<p>it does not appear […] when looking for it in modules. Help me please</p>
</blockquote>
</aside>
<p>Module will be available in the Modules menu only after the corresponding extension has been installed.</p>
<aside class="quote no-group" data-username="crisandr" data-post="7" data-topic="11374">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/crisandr/48/6738_2.png" class="avatar"> crisandr:</div>
<blockquote>
<p>I used ashampoo uninstaller to clear all installation logs, reinstall the program and extension</p>
</blockquote>
</aside>
<p>I am not familiar with <code>ashampoo</code>, uninstalling Slicer is possible from windows “Settings → App &amp; Feature”</p>
<p>After installing Slicer and configuring your antivirus adding the relevant exceptions, which error message to you get when you try to install and then Restart Slicer ?</p>
<p>Consider the extension is <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2020-05-20&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Q3DC">build and packaged</a> on Linux, macOS and Windows, it should be available in the extension manager.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="11374">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The extension should probably be updated to get these packages at build time like how SlicerRadiomics gets some python packages during the build process to package with the extension. Described in <a href="https://discourse.slicer.org/t/install-python-library-with-extension/10110/8">Install python library with extension </a> or <a href="https://github.com/Radiomics/SlicerRadiomics/blob/e72c856edf80e740102a068b5466a070130155f9/SuperBuild/External_python-pyradiomics.cmake">here </a>. <a class="mention" href="/u/james_hoctor">@James_Hoctor</a> or <a class="mention" href="/u/bpaniagua">@bpaniagua</a> , it looks like you’ve been doing some maintenance on this extension. You might want to implement this change in the build process.</p>
</blockquote>
</aside>
<p>This is now tracked in <a href="https://github.com/DCBIA-OrthoLab/Q3DCExtension/issues/24" class="inline-onebox">Revisit integration of networkx package · Issue #24 · DCBIA-OrthoLab/Q3DCExtension · GitHub</a> we will increase the complexity of the extension build system after we have a better understand of the problem <a class="mention" href="/u/crisandr">@crisandr</a> is experiencing.</p>
<p>Since both <code>networkx</code> and its dependency <code>decorator</code> have wheels (see <a href="https://pypi.org/project/networkx/#files">here</a> and <a href="https://pypi.org/project/decorator/#files">here</a>), I would prefer not changing the build system of the extension yet.</p>
<p>Finally, as it was suggested in <a href="https://github.com/DCBIA-OrthoLab/Q3DCExtension/issues/22">Q3DCExtension#22</a> by <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, install of <code>scipy</code> with <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.pip_install">slicer.util.pip_install</a> has been removed in <a href="https://github.com/DCBIA-OrthoLab/Q3DCExtension/pull/25">PR Q3DCExtension#25</a></p>

---
