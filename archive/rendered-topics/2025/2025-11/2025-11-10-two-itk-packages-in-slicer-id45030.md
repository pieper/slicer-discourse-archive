# Two ITK packages in Slicer

**Topic ID**: 45030
**Date**: 2025-11-10
**URL**: https://discourse.slicer.org/t/two-itk-packages-in-slicer/45030

---

## Post #1 by @muratmaga (2025-11-10 23:40 UTC)

<p>When I try to register two volumes using our ANTsPy extension, I get this error on Linux. Things workout perfectly fine on Windows and Mac:</p>
<pre><code class="lang-auto">Switch to module:  "ANTsRegistration"
WARNING: In /project/itksource/Modules/Core/Common/src/itkObjectFactoryBase.cxx, line 543
Possible incompatible factory load:
Running itk version :
itk version 5.4.3
Loaded factory version:
itk version 5.4.4
Loading factory:
/home/maga/Downloads/Slicer-5.10.0-linux-amd64/bin/../lib/Slicer-5.10/ITKFactories/libMRMLIDIOPlugin.so
</code></pre>
<p>But when I look at the packages ANTsRegistration is loading, I am not seeing an ITK-5.4.3 being brought in:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 10.11.2025 15:23:05 [] (unknown:0) - Switch to module:  "ANTsRegistration"
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Collecting antspyx
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) -   Using cached antspyx-0.6.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.1 kB)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Collecting pandas (from antspyx)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) -   Using cached pandas-2.3.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (91 kB)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Collecting pyyaml (from antspyx)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) -   Using cached pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Requirement already satisfied: numpy in ./lib/Python/lib/python3.12/site-packages (from antspyx) (2.0.2)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Collecting statsmodels (from antspyx)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) -   Using cached statsmodels-0.14.5-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Collecting webcolors (from antspyx)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) -   Using cached webcolors-25.10.0-py3-none-any.whl.metadata (2.2 kB)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Collecting matplotlib (from antspyx)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) -   Using cached matplotlib-3.10.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (11 kB)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Requirement already satisfied: Pillow in ./lib/Python/lib/python3.12/site-packages (from antspyx) (11.2.1)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Requirement already satisfied: requests in ./lib/Python/lib/python3.12/site-packages (from antspyx) (2.32.3)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Collecting scikit-learn (from antspyx)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) -   Using cached scikit_learn-1.7.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (11 kB)
[INFO][Stream] 10.11.2025 15:23:06 [] (unknown:0) - Requirement already satisfied: scipy&lt;1.16 in ./lib/Python/lib/python3.12/site-packages (from antspyx) (1.13.1)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Collecting contourpy&gt;=1.0.1 (from matplotlib-&gt;antspyx)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) -   Using cached contourpy-1.3.3-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.5 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Collecting cycler&gt;=0.10 (from matplotlib-&gt;antspyx)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) -   Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Collecting fonttools&gt;=4.22.0 (from matplotlib-&gt;antspyx)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) -   Using cached fonttools-4.60.1-cp312-cp312-manylinux1_x86_64.manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_5_x86_64.whl.metadata (112 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Collecting kiwisolver&gt;=1.3.1 (from matplotlib-&gt;antspyx)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) -   Using cached kiwisolver-1.4.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (6.3 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Requirement already satisfied: packaging&gt;=20.0 in ./lib/Python/lib/python3.12/site-packages (from matplotlib-&gt;antspyx) (25.0)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Requirement already satisfied: pyparsing&gt;=3 in ./lib/Python/lib/python3.12/site-packages (from matplotlib-&gt;antspyx) (3.2.3)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Requirement already satisfied: python-dateutil&gt;=2.7 in ./lib/Python/lib/python3.12/site-packages (from matplotlib-&gt;antspyx) (2.9.0.post0)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Requirement already satisfied: six&gt;=1.5 in ./lib/Python/lib/python3.12/site-packages (from python-dateutil&gt;=2.7-&gt;matplotlib-&gt;antspyx) (1.17.0)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Collecting pytz&gt;=2020.1 (from pandas-&gt;antspyx)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) -   Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Collecting tzdata&gt;=2022.7 (from pandas-&gt;antspyx)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) -   Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Requirement already satisfied: charset-normalizer&lt;4,&gt;=2 in ./lib/Python/lib/python3.12/site-packages (from requests-&gt;antspyx) (3.4.2)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Requirement already satisfied: idna&lt;4,&gt;=2.5 in ./lib/Python/lib/python3.12/site-packages (from requests-&gt;antspyx) (3.10)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in ./lib/Python/lib/python3.12/site-packages (from requests-&gt;antspyx) (2.4.0)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Requirement already satisfied: certifi&gt;=2017.4.17 in ./lib/Python/lib/python3.12/site-packages (from requests-&gt;antspyx) (2025.4.26)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Collecting joblib&gt;=1.2.0 (from scikit-learn-&gt;antspyx)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) -   Using cached joblib-1.5.2-py3-none-any.whl.metadata (5.6 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Collecting threadpoolctl&gt;=3.1.0 (from scikit-learn-&gt;antspyx)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) -   Using cached threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Collecting patsy&gt;=0.5.6 (from statsmodels-&gt;antspyx)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) -   Using cached patsy-1.0.2-py2.py3-none-any.whl.metadata (3.6 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached antspyx-0.6.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (22.4 MB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached matplotlib-3.10.7-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (8.7 MB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached contourpy-1.3.3-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (362 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached fonttools-4.60.1-cp312-cp312-manylinux1_x86_64.manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_5_x86_64.whl (4.9 MB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached kiwisolver-1.4.9-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (1.5 MB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached pandas-2.3.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (12.4 MB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached scikit_learn-1.7.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (9.5 MB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached joblib-1.5.2-py3-none-any.whl (308 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached statsmodels-0.14.5-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (10.4 MB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached patsy-1.0.2-py2.py3-none-any.whl (233 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Using cached webcolors-25.10.0-py3-none-any.whl (14 kB)
[INFO][Stream] 10.11.2025 15:23:07 [] (unknown:0) - Installing collected packages: pytz, webcolors, tzdata, threadpoolctl, pyyaml, patsy, kiwisolver, joblib, fonttools, cycler, contourpy, scikit-learn, pandas, matplotlib, statsmodels, antspyx
[INFO][Stream] 10.11.2025 15:23:21 [] (unknown:0) -
[INFO][Stream] 10.11.2025 15:23:21 [] (unknown:0) - Successfully installed antspyx-0.6.1 contourpy-1.3.3 cycler-0.12.1 fonttools-4.60.1 joblib-1.5.2 kiwisolver-1.4.9 matplotlib-3.10.7 pandas-2.3.3 patsy-1.0.2 pytz-2025.2 pyyaml-6.0.3 scikit-learn-1.7.2 statsmodels-0.14.5 threadpoolctl-3.6.0 tzdata-2025.2 webcolors-25.10.0
</code></pre>
<p>When I try to run <code>pip_uninstall("itk==5.4.3")</code> I get skipping, not installed message.  when I check for itk version I get 5.4.4</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import itk
&gt;&gt;&gt; itk.__version__
'5.4.4'
</code></pre>
<p>It is not clear to me or <a class="mention" href="/u/dzenanz">@dzenanz</a> where this itk-5.4.3 is coming from.  Again this is specific to the Linux and is reproducible all recent previews, and today’s stable. Any suggestion is much appreciated.</p>

---

## Post #2 by @jamesobutler (2025-11-11 02:01 UTC)

<p>It appears that AntsPy does not use ITK’s Python package but instead builds ITK C++ from source and uses that along with wrapping it using a package called nanobind.</p>
<p>I observe similar warnings about possible incompatible factory load when I connect an OpenIGTLink connection using PlusToolkit’s PlusServer that uses a slightly different ITK version than the one used by Slicer core and corresponding SlicerOpenIGTLink extension. I observe the warning, but generally don’t face any issues because the versions are similar enough.</p>
<p>Here is the C++ ITK build that uses ITK 5.4.3.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/ANTsX/ANTsPy/blob/50bdb2445051841613cef0bbb899e4c6a3cc4c4a/scripts/configure_ITK.bat#L6-L8">
  <header class="source">

      <a href="https://github.com/ANTsX/ANTsPy/blob/50bdb2445051841613cef0bbb899e4c6a3cc4c4a/scripts/configure_ITK.bat#L6-L8" target="_blank" rel="noopener nofollow ugc">github.com/ANTsX/ANTsPy</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/ANTsX/ANTsPy/blob/50bdb2445051841613cef0bbb899e4c6a3cc4c4a/scripts/configure_ITK.bat#L6-L8" target="_blank" rel="noopener nofollow ugc">scripts/configure_ITK.bat</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/ANTsX/ANTsPy/blob/50bdb2445051841613cef0bbb899e4c6a3cc4c4a/scripts/configure_ITK.bat#L6-L8" rel="noopener nofollow ugc"><code>50bdb2445</code></a>
</div>



    <pre class="onebox"><code class="lang-bat">
      <ol class="start lines" start="6" style="counter-reset: li-counter 5 ;">
          <li>SET itkgit=https://github.com/InsightSoftwareConsortium/ITK.git</li>
          <li>:: 5.4.3</li>
          <li>SET itktag=0913f2a962d28eb5725a50a17304c4652ca6cfdc</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2025-11-11 05:29 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>I will try to build a custom wheel using 5.4.4.post1, but don’t know how to get that ITK tag.</p>
<p>Do you know where I can find that information?</p>
<p>Found it: f98d5fac5e1d5ef694f3010f12bbbc2c792994c6</p>

---

## Post #4 by @muratmaga (2025-11-11 06:28 UTC)

<p>Looks like the custom antspyx wheel with itk-5.4.4 seems to solve the crash. I will make changes in SlicerANTsPy to use this custom wheel on Linux. Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>

---
