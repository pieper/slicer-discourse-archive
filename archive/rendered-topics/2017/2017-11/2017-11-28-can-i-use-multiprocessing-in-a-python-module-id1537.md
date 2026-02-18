# Can I use multiprocessing in a Python module

**Topic ID**: 1537
**Date**: 2017-11-28
**URL**: https://discourse.slicer.org/t/can-i-use-multiprocessing-in-a-python-module/1537

---

## Post #1 by @langderyos (2017-11-28 07:35 UTC)

<p>Hello，<br>
I am trying to use python multiprocessing in Slicer to deal with a large amount of calculations. I tried ThreadPool but it brings little effect.Then I tried Pool and Process,but they just can’t work. Could you tell me how to use multiprocessing in a Python module.<br>
I am using Slicer4.8.0 in Windows7.</p>
<p>thank you</p>

---

## Post #2 by @jcfr (2017-11-28 14:09 UTC)

<p>Hi <a class="mention" href="/u/langderyos">@langderyos</a>,</p>
<p>Thanks for your report.</p>
<p>Could you share an example of python code allowing to reproduce the problem ?</p>

---

## Post #3 by @cpinter (2017-11-28 14:25 UTC)

<p>I tried various approaches around two years ago, and what I found out is that you cannot use the threads to extend the CPU “allowance” of Slicer. So it will share the resources of the main thread which runs on a single core.<br>
Of course this may have changed, just one thing I thought is good to expect.</p>

---

## Post #4 by @lassoan (2017-11-28 15:02 UTC)

<p>All the underlying libraries (VTK, ITK, numpy, etc) are highly optimized and using multiple threads, some functions may even use GPU. Instead of implementing any low-level processing in Python, I could almost always find a combination of existing methods that do what I need. In the extremely rare case there is some computationally intensive task that I cannot find implemented in any of the libraries, I create a C++ loadable module, and implement the algorithm in a VTK class and put it in the logic component of the module. The class gets Python-wrapping automatically, so I can use it from Python.</p>

---

## Post #5 by @langderyos (2017-11-29 07:17 UTC)

<p>Hi, jcfr</p>
<p>Thanks for your reply!</p>
<p>In fact, I just tried a few lines of code to test if  multiprocessing works in a python module.I am not good at programming so maybe there is something wrong in the code.</p>
<h3>Example 1</h3>
<pre><code class="lang-auto">import os
from multiprocessing.dummy import Pool as ThreadPool
def onepool(x):
  return(x**2)
a=range(100)
pool = ThreadPool(9)
b=pool.map(onepool,a)
pool.close()
pool.join()
</code></pre>
<p>This example works.</p>
<h3>Example 2</h3>
<pre><code class="lang-auto">import os
from multiprocessing import Pool
def onepool(x):
  return(x**2)
a=range(100)
pool = Pool()
b=pool.map(onepool,a)
pool.close()
pool.join()
</code></pre>
<p>This example  doesn’t work. Slicer has no respond.</p>

---

## Post #6 by @langderyos (2017-11-29 07:31 UTC)

<p>Hi, cpinter<br>
Thanks for your reply!</p>

---

## Post #7 by @langderyos (2017-11-29 07:36 UTC)

<p>Hi, lassoan<br>
Thanks for your reply!<br>
Your reply is very help.Maybe I should find an alternate way.</p>

---

## Post #8 by @Alex_Vergara (2019-02-26 15:59 UTC)

<p>I have tried several methods, in particular your example 1 and still have the same <a href="https://stackoverflow.com/questions/26432411/multiprocessing-dummy-in-python-is-not-utilising-100-cpu" rel="nofollow noopener">behaviour</a>, Slicer uses only 1 processor and share all resources and threads in that processor. The rest of processors remain idle. I have tried with several <a href="https://www.programcreek.com/python/example/89008/multiprocessing.pool.ThreadPool" rel="nofollow noopener">examples</a> that releases GIL, joblib with threads, pathos, multiprocessing… Nothing seems to work <a href="https://stackoverflow.com/questions/38217449/python-multiprocessing-slower-than-single-thread?noredirect=1&amp;lq=1" rel="nofollow noopener">properly</a>, sequential codes are still faster than the threaded ones.<br>
Is there a way you can actually launch several threads in python in Slicer??</p>

---

## Post #9 by @lassoan (2019-03-13 14:16 UTC)

<p>I’m not sure if you can run several threads but you can certainly run several processes.</p>
<p>You can use Slicer’s CLI module interface to synchronize execution and pass data between the main process and the parallel processes. <a href="https://discourse.slicer.org/t/how-to-run-python-based-cli-modules/4627">CLI modules can be implemented in Python</a> or C++.</p>
<p>We plan to have native Python3 support and ability to install any Python packages within a few weeks. This will allow you to use any of the native Python multi-processing methods. It won’t make things faster or simpler, the only difference is that you can use pure Python mechanisms instead of Slicer-specific ones.</p>

---

## Post #10 by @Alex_Vergara (2019-03-13 14:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="1537">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We plan to have native Python3 support and ability to install any Python packages within a few weeks.</p>
</blockquote>
</aside>
<p>Really good news!!! Thanks! This will be a major jump in Slicer. Is there anyway I can help??</p>

---

## Post #11 by @evan (2019-11-29 21:17 UTC)

<p>Hi all,</p>
<p>I am new to the Slicer CLI world as well and was looking for any insight on the following:</p>
<p>Currently, I am processing some extensive vtkModifiedBSPTree line intersections (iterating over about 6000) in a python slicer module and am currently iterating through them in the Logic portion of my module. As pointed out this can be quite slow as only one cpu core is being used. As far as I know, I should move these calculations to a python-based CLI module and interface with it to speed up this process. My question is; is this correct? Will this speed up this process (perhaps if I use multiprocessing within the cli module)? Or will this only allow this process to be run asynchronously and thus allow the user to interact with slicer will it is being done.</p>
<p>Many thanks,<br>
Evan</p>

---

## Post #12 by @lassoan (2019-11-29 21:56 UTC)

<p>CLI modules run asynchronously, without blocking the main thread. So, moving the computationally intensive part of your module to a CLI would allow you to keep the application responsive.</p>

---

## Post #13 by @DanceWithFeathers (2024-12-12 08:07 UTC)

<p>So in Slicer version 5.6.2, can i use the the native Python multi-processing methods? I test a sample code in the slicer python console ,and i find multi_thread method words very well, but multi_process method will crash the slicer.</p>
<pre><code class="lang-auto">import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 测试的大素数列表
PRIMES = [112272535095293] * 10  # 重复多次以延长计算时间

# 判断一个数是否为素数
def is_prime(n):
    if n &lt; 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

# 单线程运行
def single_thread():
    for number in PRIMES:
        is_prime(number)

# 多线程运行
def multi_thread():
    with ThreadPoolExecutor() as executor:
        executor.map(is_prime, PRIMES)

# 多进程运行
def multi_process():
    with ProcessPoolExecutor() as executor:
        executor.map(is_prime, PRIMES)

# 测试三种方法的运行时间
if __name__ == "__main__":
    for method, func in [("Single Thread", single_thread), 
                         ("Multi Thread", multi_thread), 
                         ("Multi Process", multi_process)]:
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{method} cost: {end_time - start_time:.2f} seconds")
</code></pre>
<p>In fact, I want to speed up the processing of extracting multimodal radiomics features. Currently, I am primarily using the following approach to call the CLI module:</p>
<pre><code class="lang-auto">self.cliNode = slicer.cli.run(slicer.modules.slicerradiomicscli, self.cliNode, cliParams,wait_for_completion=self.runSync)

</code></pre>
<p>As a result, I hope to call multiple CLI modules simultaneously. However, testing with Python’s <code>multiprocessing</code> seems not to work. Therefore, I would like to ask two questions:</p>
<ol>
<li>Can Python’s native <code>multiprocessing</code> be used in this scenario?</li>
<li>Is it possible to call CLI modules in parallel?"</li>
</ol>

---

## Post #14 by @DanceWithFeathers (2024-12-12 09:40 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> and I learn your great job in project <a href="https://github.com/pieper/SlicerParallelProcessing" rel="noopener nofollow ugc">SlicerParallelProcessing</a> which used Qprocess that can start some <code>PythonSlicer</code> environment to run <code>.py</code> files. I think a lot of task used   <code>multiprocessing</code> now can be solved by using your method.</p>
<p>But since my processing involves not directly using Python’s internal packages but rather using <code>Slicer.cli.run</code> (because I want to reuse high-quality code that others have already written), this approach might encounter some issues.</p>
<p>Or, can I parallelize the calling of slicer modules using this method?</p>

---

## Post #15 by @DanceWithFeathers (2024-12-12 09:47 UTC)

<p>Currently, the only solution I can think of is to directly call the <code>pyradiomics</code> package from Python and write my own feature extraction pipeline. <a href="https://github.com/pieper/SlicerParallelProcessing" rel="noopener nofollow ugc">SlicerParallelProcessing</a></p>
<p>However, if I also have to wrap a large amount of MRI preprocessing, etc., myself, I feel like I wouldn’t be fully utilizing the work done by others in the Slicer module, and it doesn’t seem like the most suitable path.</p>

---

## Post #16 by @pieper (2024-12-12 20:41 UTC)

<p><a class="mention" href="/u/dancewithfeathers">@DanceWithFeathers</a> yes, there are some constraints and tradeoffs due to limitations of some of the packages we rely on, but many different options are avalable and you just need to figure out what’s cleanest and most suitable for your work.  Running cli modules from Slicer is an easy way to leverage parallelism, and as you mentioned SlicerParallelProcessing gives you another way to offload tasks.  Depending on your overall needs you may want to mix and match options.</p>
<p>Maybe if you give a specific use case people can give you more specific suggestions.</p>

---

## Post #17 by @DanceWithFeathers (2024-12-13 03:16 UTC)

<p>Thank you so much for reply. The way I use radiomics module for processing MRI is very simple：</p>
<pre><code class="lang-auto">cliParams = {
    # 'Image': inputVolume.GetID(),
    # 'Mask': inputSegmentation.GetID(),
    'Image': imageNode.GetID(),
    'Mask': labelNode.GetID(),
    'param': self._parameterFile,
    'out': self._cli_output.GetID(),
    'label': label_idx
}
# run the radiomics module
self.cliNode = slicer.cli.run(slicer.modules.slicerradiomicscli, self.cliNode, cliParams,
                              wait_for_completion=self.runSync)
</code></pre>
<p>and I have to use <code>slicer.cli.run</code> many times for different modalities and ROIs. The overall process has been placed into different functions, but in practice, it is similar to running the CLI sequentially：</p>
<pre><code class="lang-auto">#for modality1 and  ROI1
cliParams11={XXX}#include inputVolume1 and inputSegmentation1
self.cliNode11 = slicer.cli.run(slicer.modules.slicerradiomicscli, self.cliNode11, cliParams11)

#for modality1 and  ROI2
cliParams12={XXX}#include inputVolume1 and inputSegmentation2
self.cliNode12 = slicer.cli.run(slicer.modules.slicerradiomicscli, self.cliNode12, cliParams12)

#for modality2 and  ROI1
cliParams21={XXX}#include inputVolume2 and inputSegmentation1
self.cliNode21 = slicer.cli.run(slicer.modules.slicerradiomicscli, self.cliNode21, cliParams21)


#for modalityN and one ROIM, which means I call slicer.cli.run N*M times in one patient case
cliParamsNM={XXX}#include inputVolumeN and inputSegmentationM
self.cliNodeNM = slicer.cli.run(slicer.modules.slicerradiomicscli, self.cliNodeNM, cliParamsNM)
</code></pre>
<p>So, is it possible to call CLI modules in parallel? or another way that I can use <code>slicerradiomicscli</code> in parallel?</p>

---
