---
topic_id: 33390
title: "Slicer Parameters Conflicts When Adding Load File And Python"
date: 2023-12-14
url: https://discourse.slicer.org/t/33390
---

# Slicer parameters conflicts when adding "--load-file" and "--python-script"

**Topic ID**: 33390
**Date**: 2023-12-14
**URL**: https://discourse.slicer.org/t/slicer-parameters-conflicts-when-adding-load-file-and-python-script/33390

---

## Post #1 by @derekcbr (2023-12-14 08:16 UTC)

<p>Slicer.exe, “–python-code”, “print(‘Start Slicer from Blender!’)”, “–python-script”, startup_slice_script_file<br>
When adding both “–load-file” and “–python-script”, “–load-file” will not be executed to load .mrb file, and it only executes “–python-script”. Is there a way of adding both parameters and make it working? Thanks.</p>

---

## Post #2 by @RafaelPalomar (2023-12-15 06:33 UTC)

<p>I don’t think there is any <code>--load-file</code> flag, but i is true that something like</p>
<pre data-code-wrap="bash"><code class="lang-bash">./Slicer --python-code "print('Hello from command-line')" /tmp/scene.mrb
</code></pre>
<p>will both load the file (first) and execute the provided python code (second), while</p>
<pre data-code-wrap="bash"><code class="lang-bash">./Slicer --python-script /tmp/script.py /tmp/scene.mrb
</code></pre>
<p>won’t load the file <code>/tmp/scene.mrb</code>.</p>
<p>It seems that providing python script explicitly prevents the load of files:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/1d77e473abebc3b554d886614e2958adff34e38e/Base/QTCore/qSlicerCoreApplication.cxx#L1145-L1178">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/1d77e473abebc3b554d886614e2958adff34e38e/Base/QTCore/qSlicerCoreApplication.cxx#L1145-L1178" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/1d77e473abebc3b554d886614e2958adff34e38e/Base/QTCore/qSlicerCoreApplication.cxx#L1145-L1178" target="_blank" rel="noopener nofollow ugc">Base/QTCore/qSlicerCoreApplication.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/1d77e473abebc3b554d886614e2958adff34e38e/Base/QTCore/qSlicerCoreApplication.cxx#L1145-L1178" rel="noopener nofollow ugc"><code>1d77e473a</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="1145" style="counter-reset: li-counter 1144 ;">
          <li>QStringList filesToLoad;</li>
          <li>QStringList unparsedArguments = options-&gt;unparsedArguments();</li>
          <li>if (unparsedArguments.length() &gt; 0 &amp;&amp;</li>
          <li>    options-&gt;pythonScript().isEmpty() &amp;&amp;</li>
          <li>    options-&gt;extraPythonScript().isEmpty())</li>
          <li>  {</li>
          <li>  foreach(QString fileName, unparsedArguments)</li>
          <li>    {</li>
          <li>    QUrl url = QUrl(fileName);</li>
          <li>    if (url.scheme().toLower() == this-&gt;applicationName().toLower()) // Scheme is case insensitive</li>
          <li>      {</li>
          <li>      qDebug() &lt;&lt; "URL received via command-line: " &lt;&lt; fileName;</li>
          <li>      emit urlReceived(fileName);</li>
          <li>      continue;</li>
          <li>      }</li>
          <li></li>
          <li>    QFileInfo file(fileName);</li>
          <li>    if (file.exists())</li>
          <li>      {</li>
          <li>      qDebug() &lt;&lt; "Local filepath received via command-line: " &lt;&lt; fileName;</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/1d77e473abebc3b554d886614e2958adff34e38e/Base/QTCore/qSlicerCoreApplication.cxx#L1145-L1178" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<h3><a name="p-104675-moving-forward-1" class="anchor" href="#p-104675-moving-forward-1" aria-label="Heading link"></a>Moving forward</h3>
<ol>
<li>
<p><a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a> , is that an inconsistency that should be fixed?</p>
</li>
<li>
<p><a class="mention" href="/u/derekcbr">@derekcbr</a>, have you tried to load the scene using your python script? or a combination of python script and python code? e.g.,</p>
</li>
</ol>
<pre data-code-wrap="python"><code class="lang-python">./Slicer --python-code "slicer.util.loadScene('/tmp/Scene.mrb')" --python-script /tmp/script.py 
</code></pre>

---

## Post #3 by @pieper (2023-12-15 13:52 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> - right, this is intentional.  The idea is that if you specify a python script then the other command line arguments are made available as <code>sys.argv</code> in python.</p>

---

## Post #4 by @lassoan (2023-12-15 14:50 UTC)

<p>It would be helpful to describe this in the documentation. I had a look in the Slicer documentation but I did not find specification of command-line arguments for the appplication (only <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#run-a-python-script-file-in-the-slicer-environment">examples in the script repository</a> and some <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#what-is-the-python-console">tips in the Python FAQ</a>).</p>
<p>Have I missed something or we should add a new documentation section for describing the frequently used command-line arguments (maybe around <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#qt-built-in-command-line-options">here</a>)?</p>

---

## Post #5 by @pieper (2023-12-15 15:15 UTC)

<p>I agree, I don’t think these are documented beyond the brief message you get with <code>--help</code></p>

---

## Post #6 by @derekcbr (2023-12-16 00:23 UTC)

<p>Thanks, quite helpful!</p>

---
