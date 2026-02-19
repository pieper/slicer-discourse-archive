---
topic_id: 6068
title: "Loading A Deep Learning Model To A Scripted Module"
date: 2019-03-08
url: https://discourse.slicer.org/t/6068
---

# Loading a deep learning model to a scripted module

**Topic ID**: 6068
**Date**: 2019-03-08
**URL**: https://discourse.slicer.org/t/loading-a-deep-learning-model-to-a-scripted-module/6068

---

## Post #1 by @ZiyunLiang (2019-03-08 08:02 UTC)

<p>Hi, I’m working on a project about pelvic floor MRI image recognition. In this project I am trying to  automatic recognize feature points and measure distance on MRI images which will help with pelvic floor disease detection. Right now I have already trained a neural network with Keras and stored the model in a .h5 file. Since Slicer is the perfect open-source platform to implement this idea, I have been working hard to learn, but still a beginner to Slicer. I have finished building the GUI of a scripted module.Now I am trying to put my model into the scripted module I created. And I’m seeking advices and ideas about how to do this.</p>
<p>I’m now using<br>
<em>from pip._internal import main as _main</em><br>
<em>_main([‘install’, ‘pandas’])</em><br>
to load packages to Slicer and<br>
<em>model = load_model(’./models/’ + model_name + ‘.h5’,compile=False)</em><br>
to load my module.<br>
I’m wondering if my idea is ok and is there a better way to do it?</p>
<p>Does anyone have any suggestions?<br>
Thank you!<br>
Andrea</p>

---

## Post #2 by @pieper (2019-03-08 22:08 UTC)

<p>Your approach sounds reasonable to me.  You may see compatibility issues between Slicer’s python and some generally available python packages.  There’s more info <a href="https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984">in this thread</a>.</p>

---

## Post #3 by @ZiyunLiang (2019-03-11 02:35 UTC)

<p>Hi, Steve! Thank you for the advice!</p>
<p>I succeeded in installing the packages, but I’m having a trouble loading the .h5 file. I’m pretty sure it is in the correct directory but when I tried to load the file, it says</p>
<pre><code class="lang-auto">*IOError: Unable to open file (unable to open file: name = './models/best_model_RMSE_RES50.h5', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)*
</code></pre>
<p>Also,  I tried multithreading and used the python on my mac as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_run_Python_script_using_a_non-Slicer_Python_environment" rel="nofollow noopener">here</a>, I launched a python script which worked fine on my mac but when Slicer tried to run that script, it says</p>
<pre><code class="lang-auto">*subprocess.CalledProcessError: Command '['/usr/bin/python', '/Users/andrealiang/Desktop/Pelvicfloor-2019-02-25/lib/slicer-4.11/qt-scripted-modules/nonSlicer_python.py']' returned non-zero exit status 1*
</code></pre>
<p>I’m really confused here. I’m wondering if it is because Slicer has some problem when reading .h5 file.<br>
Is there any solution on how to solve this problem?<br>
Please help!</p>
<p>Thank you!<br>
Andrea</p>

---

## Post #4 by @pieper (2019-03-12 13:08 UTC)

<p>Hi Andrea -</p>
<p>For the first issue, you might try specifying the full path to your .h5 file.  The message is saying that it can’t find the file at the path you specified.  Depending on how you started Slicer it might have a different working directory.</p>
<p>The second one could be the same issue.  The script exits with an error, which could mean it didn’t find the file or could mean something else.  Have a look at the documentation and examples in slicer.</p>
<p><a href="https://docs.python.org/2/library/subprocess.html" class="onebox" target="_blank" rel="nofollow noopener">https://docs.python.org/2/library/subprocess.html</a></p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/4c0b0b15276aedc0e12d77e2227536426979d773/Applications/SlicerApp/Testing/Python/SlicerAppTesting.py#L50-L67" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4c0b0b15276aedc0e12d77e2227536426979d773/Applications/SlicerApp/Testing/Python/SlicerAppTesting.py#L50-L67" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/4c0b0b15276aedc0e12d77e2227536426979d773/Applications/SlicerApp/Testing/Python/SlicerAppTesting.py#L50-L67</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="50" style="counter-reset: li-counter 49 ;">
<li>def run(executable, arguments=[], verbose=True, shell=False, drop_cache=False):</li>
<li>"""Run ``executable`` with provided ``arguments``.</li>
<li>"""</li>
<li>if drop_cache:</li>
<li>  dropcache()</li>
<li>if verbose:</li>
<li>  print("%s %s" % (os.path.basename(executable), " ".join([pipes.quote(arg) for arg in arguments])))</li>
<li>arguments.insert(0, executable)</li>
<li>if shell:</li>
<li>  arguments = " ".join([pipes.quote(arg) for arg in arguments])</li>
<li>p = subprocess.Popen(args=arguments, stdout=subprocess.PIPE,</li>
<li>                     stderr=subprocess.PIPE, shell=shell)</li>
<li>stdout, stderr = p.communicate()</li>
<li>
</li>
<li>if p.returncode != EXIT_SUCCESS:</li>
<li>  print('STDERR: ' + stderr, file=sys.stderr)</li>
<li>
</li>
<li>return (p.returncode, stdout, stderr)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Good luck,<br>
Steve</p>

---

## Post #5 by @ZiyunLiang (2019-03-13 11:24 UTC)

<p>Hi Steve,<br>
Thanks  for the answer. You are right about the working directory and I solved the problem by specifying the full path.</p>
<p>Thanks!<br>
Andrea</p>

---

## Post #6 by @Zhenchen (2022-06-29 08:31 UTC)

<p>Hello Andrea,</p>
<p>I am trying to build a module for segmentation using a pre-trained Unet model. I also used the load_model() function to load my .h5 model file. But when I run it in Slicer, the execution blocks with no error information and the Slicer does not respond. And I have to force quit Slicer. Maybe you have an idea of the reason behind the blockage.</p>
<p>Thanks a lot.<br>
Zhenchen</p>

---
