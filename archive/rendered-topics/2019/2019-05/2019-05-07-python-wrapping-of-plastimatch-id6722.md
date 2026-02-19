---
topic_id: 6722
title: "Python Wrapping Of Plastimatch"
date: 2019-05-07
url: https://discourse.slicer.org/t/6722
---

# Python wrapping of plastimatch

**Topic ID**: 6722
**Date**: 2019-05-07
**URL**: https://discourse.slicer.org/t/python-wrapping-of-plastimatch/6722

---

## Post #1 by @gcsharp (2019-05-07 15:17 UTC)

<p>This morning I have been investigating python wrapping for plastimatch.  It looks feasible to use the ITK wrapping method.  Would this be a reasonable approach for eventually allowing python interaction within 3D Slicer?  I’m a bit concerned because looking at the Slicer’s build it seems ITK itself is not wrapped and not available in Slicer python.</p>

---

## Post #2 by @jcfr (2019-05-07 15:41 UTC)

<blockquote>
<p>investigating python wrapping for plastimatch</p>
</blockquote>
<p>This is good to hear. Are you thinking about creating a dedicated “pythonic” API or a one-to-one mapping with the C++ one ?</p>
<blockquote>
<p>It looks feasible to use the ITK wrapping method</p>
</blockquote>
<p>This is suitable for projects providing ITK filters and/or classes (or having functionality that could be wrapped in such a way).</p>
<p>If that makes sense, you could look at using the <a href="https://github.com/InsightSoftwareConsortium/ITKModuleTemplate" class="inline-onebox">GitHub - InsightSoftwareConsortium/ITKModuleTemplate: A template to start an ITK Module</a> as a starting point. See also <a href="https://blog.kitware.com/python-packages-for-itk-modules/">https://blog.kitware.com/python-packages-for-itk-modules/</a></p>
<blockquote>
<p>Would this be a reasonable approach for eventually allowing python interaction within 3D Slicer?</p>
</blockquote>
<p>Since python packages distributed on <a href="http://pypi.org/">http://pypi.org/</a> can now be installed on Linux, macOS and windows. This would work.</p>
<blockquote>
<p>Slicer’s build it seems ITK itself is not wrapped</p>
</blockquote>
<p>This is correct, while there is an option called <code>Slicer_BUILD_ITKPython</code>, it not enabled by default.</p>
<blockquote>
<p>ITK itself […] not available in Slicer python</p>
</blockquote>
<p>following the recent transition of Slicer to python 3.6, running <code>pip install itk</code> would allow you to use it.</p>
<h3><a name="p-23843-suggestions-1" class="anchor" href="#p-23843-suggestions-1" aria-label="Heading link"></a>suggestions</h3>
<p>You may want to look at using <a href="https://github.com/pybind/pybind11#readme" class="inline-onebox">GitHub - pybind/pybind11: Seamless operability between C++11 and Python</a> along <a href="https://scikit-build.readthedocs.io">https://scikit-build.readthedocs.io</a></p>

---

## Post #3 by @gcsharp (2019-05-07 18:57 UTC)

<p>Thank you for the great feedback!  This is quite new area for me, and I’m still considering the best plan.</p>
<p>Both pybind or scikit-build look good.  Do you have any idea which would be better?   I note that SimpleITK seems to use scikit-build.</p>

---

## Post #4 by @jcfr (2019-05-07 19:25 UTC)

<blockquote>
<p>Do you have any idea which would be better?</p>
</blockquote>
<h3><a name="p-23851-itkmoduletemplate-1" class="anchor" href="#p-23851-itkmoduletemplate-1" aria-label="Heading link"></a>ITKModuleTemplate</h3>
<p>If you are already familiar with ITK and crafting a Plastimatch API built around ITK data structure is relevant, this would be a sensible approach.</p>
<p>You also be able to leverage the input of the community and wealth of knowledge shared on the ITK forum (<a href="https://discourse.itk.org/">https://discourse.itk.org/</a>)</p>
<p>The template would also give you CI and infrastructure for package distributions with no effort. <a class="mention" href="/u/phcerdan">@phcerdan</a>  works on a similar project to wrap the <code>proxTV</code> project and make it available as <a href="https://github.com/InsightSoftwareConsortium/ITKTotalVariation" class="inline-onebox">GitHub - InsightSoftwareConsortium/ITKTotalVariation: External Module for Total Variation Algorithms, providing wrap for https://github.com/albarji/proxTV</a> module</p>
<p>Cc: <a class="mention" href="/u/thewtex">@thewtex</a></p>
<h3><a name="p-23851-pybind11-2" class="anchor" href="#p-23851-pybind11-2" aria-label="Heading link"></a>pybind11</h3>
<p>While this removes the need for tools like <code>swig</code>, you are still required to maintain the wrapping code. Note that I don’t have a lot of experience with it.</p>
<h3><a name="p-23851-suggested-next-steps-3" class="anchor" href="#p-23851-suggested-next-steps-3" aria-label="Heading link"></a>suggested next steps</h3>
<p>It may be sensible to craft a document listing the functionality and API you would like to expose to Python.</p>
<p>It would also be nice to listing the data structure that should not be deep-copied and are expected to be shared between VTK/ITK/etc …  (if any)</p>
<h3><a name="p-23851-scikit-build-4" class="anchor" href="#p-23851-scikit-build-4" aria-label="Heading link"></a>scikit-build.</h3>
<p>This project streamlines the creation of python package (called wheel) for project using CMake. It is not responsible for any wrapping in itself and will be relevant for all approaches involving compilation of python modules.</p>

---

## Post #5 by @thewtex (2019-05-07 21:27 UTC)

<p>Hi <a class="mention" href="/u/gcsharp">@gcsharp</a>,</p>
<p>As <a class="mention" href="/u/jcfr">@jcfr</a> notes, the <em>ITKModuleTemplate</em> may be the fastest way to get started. This avoids:</p>
<ul>
<li>Manually maintaining binding code (we analyize the headers with CastXML to generate the required SWIG interface files).</li>
<li>The CI infrastructure to generate Windows, Linux, and macOS packages.</li>
<li>The configuration to build the wheel with scikit-build and the post-processing steps to make distributable wheels.</li>
</ul>
<p>The <a href="https://itk.org/ItkSoftwareGuide.pdf" rel="nofollow noopener">ITK Software Guide</a> has a section on writing the wrap interface files, but we would be happy to answer questions.</p>

---

## Post #6 by @gcsharp (2019-05-07 22:13 UTC)

<p>Got it.  Thank you!  I will do a pilot study.</p>
<p>I think for Slicer users interface with sitk might be more important than itk.</p>

---

## Post #7 by @fedorov (2021-09-16 15:46 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> do you have any updates on this topic?</p>
<p>We are using Plastimatch for developing use cases in <a href="https://imaging.datacommons.cancer.gov/">IDC</a>, and lacking such wrapper, Dennis Bontempi put together this as a workaround: <a href="https://github.com/AIM-Harvard/pyplastimatch" class="inline-onebox">GitHub - AIM-Harvard/pyplastimatch: Dummy python plastimatch wrapper.</a>.</p>

---

## Post #8 by @gcsharp (2021-09-20 19:24 UTC)

<p>Regrettably, I have no progress.  Would the method used in your/Paolo’s approach be good?</p>

---

## Post #9 by @fedorov (2021-09-21 01:23 UTC)

<p>I will let Dennis and <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a> respond with their thoughts. I think what would be ideal is to be able to install those wrappers with <code>pip</code>. Meanwhile, maybe Plastimatch documentation can include pointers to the existing wrappers, to save effort for the next developer?</p>

---

## Post #10 by @denbonte (2021-09-21 08:12 UTC)

<p>Thanks <a class="mention" href="/u/fedorov">@fedorov</a> for the mention! (I actually remember looking at this thread while deciding what to do for the dummy wrapper - so hopefully this will be able to help someone else!)</p>
<p><a class="mention" href="/u/gcsharp">@gcsharp</a> what I’ve implemented on the fly (the plan is to expand it a bit, to make sure at least all the “common” operations can be launched from python scripts) is really simple and quite close to what Paolo did back in the days. The only reason I decided to implement “my own” is that I feared Paolo’s version could be outdated (with respect to Plastimatch). I also wanted to make sure a couple of features useful for the use cases were there, and forking Paolo’s implementation to then customise it didn’t look as fun <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
<p>Basically, it’s as simple as calling Plastimatch from python exploiting <code>subprocess</code> (any library for process management will do), and adding some other handy functionalities in the meantime (e.g., logging all the operations, and a few other scripts for visualisation etc.). This not only allows to run Plastimatch functions directly from your python scripts (of course, abstracting the OS - although I must report I have tested this exclusively on Linux), but also make use of other python functionalities that can help you process a great amount of data in less time. For instance, I have used the Plastimatch wrapper to run DICOM to NRRD conversion of hundreds/thousands of patients in parallel (with the performance/time requirements scaling almost linearly with the number of cores). In some cases, I’ve done so and then applied some pre-processing on the fly (for a total of a dozen lines of code), processing in a few minutes a dataset that would have required hours otherwise (e.g., DICOM to NRRD conversion scripting everything from bash, one subject at a time, then read the NRRD files, preprocess them exploiting python, and save them back).</p>
<p>The multiprocessing code I’m referring to here will be made available super soon (a matter of a couple of weeks if not less, I hope!) as part of the development of the use cases Andrey mentioned. In case you don’t want to wait though, here is an idea how you could script it using the <a href="https://github.com/AIM-Harvard/pyplastimatch" rel="noopener nofollow ugc">dummy PyPlastimatch wrapper</a>:</p>
<pre><code class="lang-auto">import os
import tqdm
import multiprocessing
import utils.pyplastimatch as pypla

# pat_config is a dictionary storing basic I/O and config info for the conversion 
def run_core(pat_config):

  # patient subfolder where all the preprocessed data will be stored
  if not os.path.exists(PAT_DIR): os.mkdir(PAT_DIR)
   
  verbose = pat_config["verbose"]
  
  # logfile for the plastimatch conversion
  LOGFILE = os.path.join(PAT_DIR, pat + '_pypla.log')
    
  # DICOM CT to NRRD conversion
  if not os.path.exists(CT_NRRD_PATH):
    convert_args_ct = {"input" : PATH_TO_DICOM_DIR,
                       "output-img" : PATH_TO_NRRD_CT}
    
    # clean old log file if it exist
    if os.path.exists(log_file_path_nrrd): os.remove(LOGFILE)
    
    pypla.convert(verbose = verbose, path_to_log_file = LOGFILE, **convert_args_ct)
</code></pre>
<pre><code class="lang-auto">def main(config):

  cpu_cores = config["cpu_cores"]

  if use_multiprocessing:
    pool = multiprocessing.Pool(processes = cpu_cores)

  """
  write here the code to populate "pat_config_list", a list of dictionaries storing
  the information used by the "run_core" function for the processing (e.g., paths, verbosity, etc.)
  """

  for _ in tqdm.tqdm(pool.imap_unordered(run_core, pat_config_list), total = len(pat_dict_list_mp)):
    pass
</code></pre>
<pre><code class="lang-auto">if __name__ == '__main__':

  """
  Parse the config file for the "main" function here!
  """
</code></pre>
<p>(sorry if this is not a MWE - if you want to test-run your own code based on this and have problems, do reach out! As I said, such scripts and all the details will be made available as part of the on-going effort at IDC!)</p>
<p>P.S.</p>
<aside class="quote no-group" data-username="fedorov" data-post="9" data-topic="6722">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I think what would be ideal is to be able to install those wrappers with <code>pip</code> . Meanwhile, maybe Plastimatch documentation can include pointers to the existing wrappers, to save effort for the next developer?</p>
</blockquote>
</aside>
<p>That is the plan indeed (to have it documented and available through pip)!</p>

---

## Post #11 by @PaoloZaffino (2021-09-21 09:21 UTC)

<p>Hi all,<br>
glad to hear my code “inspired” someone <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
I agree with <a class="mention" href="/u/denbonte">@denbonte</a> , the idea is to run the executable via the python os module.<br>
It’s not strictly a wrapper, rather an additional layer.</p>
<p>My version was written for plastimatch at that time, now some commands have changed and it’s possible to have some errors (I didn’t update it).</p>
<p>In SlicerRT we implemented a direct bridge between the  plastimatch registration algorithm and the Slicer environment. That is not an addition layer, but a real connection (Slicer infrastructure helped a lot to achieve this). After that, I think other commands have been exposed in slicer (eg DRR).</p>
<p>Great to hear it can be installed via pip!<br>
Let me know if I can help, it’s always a pleasure working on plastimatch!</p>
<p>Best,<br>
Paolo</p>

---
