---
topic_id: 919
title: "Subprocess Call In Python Interpreter Results In Memory Corr"
date: 2017-08-22
url: https://discourse.slicer.org/t/919
---

# Subprocess call in Python interpreter results in memory corruption

**Topic ID**: 919
**Date**: 2017-08-22
**URL**: https://discourse.slicer.org/t/subprocess-call-in-python-interpreter-results-in-memory-corruption/919

---

## Post #1 by @Zoe_Goey (2017-08-22 13:03 UTC)

<p>I have a C++ program that I can call from my system-installed Python using the subprocess module without causing any problems.</p>
<p>However, if I do so from within Slicer it results in a memory corruption error.  The problem occurs when the program reaches this line of code:</p>
<pre><code class="lang-auto">itk::Statistics::MersenneTwisterRandomVariateGenerator::Pointer rndgen = \
  itk::Statistics::MersenneTwisterRandomVariateGenerator::New();
</code></pre>
<p>In fact, the problem can be reproduced by calling a program that consists of that one, single line.</p>
<p>Can anyone explain why this is happening and how it can be circumvented?</p>

---

## Post #2 by @jcfr (2017-08-22 13:05 UTC)

<aside class="quote no-group" data-username="Zoe_Goey" data-post="1" data-topic="919">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/898d66/48.png" class="avatar"> Zoe_Goey:</div>
<blockquote>
<p>Can anyone explain why this is happening and how it can be circumvented?</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/zoe_goey">@Zoe_Goey</a>,</p>
<p>Could you that the program you are calling is linked against its own version of ITK ?</p>

---

## Post #4 by @Zoe_Goey (2017-08-22 15:45 UTC)

<p>Yes, the program is linked against its own version of ITK.</p>

---

## Post #5 by @jcfr (2017-08-22 18:38 UTC)

<p>Great. If you can wait few days, I have to implement a solution to allow calling a subprocess with a “clean” environment  (aka without Slicer paths) for a different project.</p>
<p>Once done, you should have an easy way to achieve this.</p>

---

## Post #6 by @Zoe_Goey (2017-08-23 16:47 UTC)

<p>OK, thanks. It would be great to get this working without replacing the random number generator. Please keep me posted about your solution.</p>

---

## Post #7 by @Zoe_Goey (2017-09-03 23:05 UTC)

<p>Any news on this yet? I am now using docker to achieve what I need. I would still be interested in a more elegant solution, though.</p>

---

## Post #8 by @lassoan (2017-09-03 23:36 UTC)

<p>Probably you can simply launch your process using custom environment. We do this when we launch Elastix. Example:</p>
<ol>
<li><a href="https://github.com/lassoan/SlicerElastix/blob/777c5259eaa5eb45d46b97ce83c67f865096ec55/Elastix/Elastix.py#L423-L434">Create custom environment</a></li>
<li><a href="https://github.com/lassoan/SlicerElastix/blob/777c5259eaa5eb45d46b97ce83c67f865096ec55/Elastix/Elastix.py#L460-L466">Launch process using subprocess.Popen</a></li>
</ol>
<p>Note that in case of Elastix, we added more directories to the path/LD path. In your case you probably want to either add your external program’s paths to the beginning of relevant environment variables; or remove all Slicer-specific paths from environment variables.</p>

---

## Post #10 by @Zoe_Goey (2017-09-04 09:39 UTC)

<p>Yes, you are right. I did not know that subprocess offered options to configure the environment. Thank you!</p>

---

## Post #11 by @jcfr (2017-09-04 21:08 UTC)

<p>Then, as soon as we are done implementing a more general solution, you would be able to do:</p>
<pre><code class="lang-python">from  subprocess import check_output
check_output(
    ["/path/to/program", "arg1", ...],
    env=slicer.util.startupEnvironment())
</code></pre>
<p>similarly, it will be possible to start CLI excluding the slicer environment. (edit: This last part is  <strong>NOT</strong> yet implemented.)</p>

---

## Post #12 by @lassoan (2017-09-04 22:34 UTC)

<p>Thanks, this will be useful. Please consider giving a more descriptive name and only use positive statements in names (try to describe what it <em>is</em>, instead of what it <em>is not</em>). For example, <code>systemEnv()</code>, <code>defaultEnv()</code>, <code>externalEnv()</code>, or <code>startupEnv()</code> names would be better.</p>

---

## Post #13 by @jcfr (2017-09-05 04:28 UTC)

<p>Good point. Thanks for the suggestions <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:">  . I will <s>most likely</s> go with <s> <code>systemEnv</code></s> <code>startupEnvironment</code>.</p>

---

## Post #14 by @jcfr (2017-09-05 15:37 UTC)

<p>Here is a work-in-progress topic</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/787" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/787" target="_blank">Extensions cannot be --launch'ed</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:59" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:59" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #15 by @jcfr (2017-09-05 20:37 UTC)

<p>With the upcoming feature, it will be possible to easily invoke processes by excluding the Slicer environment.:</p>
<ul>
<li>from c++ (using <code>app-&gt;startupEnvironment()</code>), or;</li>
<li>from python (using <code>slicer.util.startupEnvironment()</code>
</li>
</ul>
<p>Here are two examples:</p>
<p>Without using the <code>startup</code> environment, this first example fails (as expected):</p>
<pre><code class="lang-auto">&gt;&gt;&gt; from subprocess import check_output
&gt;&gt;&gt; check_call(["/usr/bin/python3", "-c", "print('hola')"])
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/jcfr/Projects/Slicer-2-build/python-install/lib/python2.7/subprocess.py", line 186, in check_call
    raise CalledProcessError(retcode, cmd)
CalledProcessError: Command '['/usr/bin/python3', '-c', "print('hola')"]' returned non-zero exit status -6
</code></pre>
<p>Now, using the sanitized environment, this one succeeds:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; from subprocess import check_output
&gt;&gt;&gt; check_output(
  ["/usr/bin/python3", "-c", "print('hola')"], 
  env=slicer.util.startupEnvironment())
'hola\n'
</code></pre>

---

## Post #16 by @jcfr (2017-09-05 22:20 UTC)

<p>The topic is now read for final review</p>
<pre><code class="lang-auto">601: Test timeout computed to be: 1800
601: Number of registered modules: 1 
601: Number of instantiated modules: 1 
601: Number of loaded modules: 1 
601: -------------------------------------------
601: path: ['/home/jcfr/Projects/Slicer-2-build/Slicer-build/Applications/SlicerApp/Testing/Python', '/home/jcfr/Projects/Slicer-2/Base/Python/slicer/tests']
601: testname: test_slicer_environment
601: -------------------------------------------
601: test_slicer_app_environment (test_slicer_environment.SlicerEnvironmentTests) ... ok
601: test_slicer_app_startupEnvironment (test_slicer_environment.SlicerEnvironmentTests) ... ok
601: test_slicer_util_startupEnvironment (test_slicer_environment.SlicerEnvironmentTests) ... ok
601: 
601: ----------------------------------------------------------------------
601: Ran 3 tests in 0.002s
601: 
601: OK
601: vtkDebugLeaks has found no leaks.
1/1 Test #601: py_nomainwindow_test_slicer_environment ...   Passed    1.23 sec

</code></pre>

---

## Post #17 by @jcfr (2017-09-06 03:23 UTC)

<p>Starting with <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26351">r26351</a>, a new public API allowing to get the startup environment is available.</p>
<ul>
<li>In c++: <code>qSlicerCoreApplication::startupEnvironment()</code>
</li>
<li>In python: <code>slicer.util.startupEnvironment()</code>
</li>
</ul>
<p>We are still <a href="https://github.com/Slicer/Slicer/pull/787#issuecomment-327361381">discussing</a> some of the internals but that will not affect the public API.</p>

---

## Post #18 by @jcfr (2017-09-07 20:14 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> You can now start a process with the original environment using something like this:</p>
<pre><code class="lang-auto">from subprocess import check_output
check_output(
  ["/usr/bin/python3", "-c", "print('hola')"], 
  env=slicer.util.startupEnvironment())
'hola\n'
</code></pre>

---
