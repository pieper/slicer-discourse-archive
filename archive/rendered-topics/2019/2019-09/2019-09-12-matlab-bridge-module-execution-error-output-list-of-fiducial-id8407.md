---
topic_id: 8407
title: "Matlab Bridge Module Execution Error Output List Of Fiducial"
date: 2019-09-12
url: https://discourse.slicer.org/t/8407
---

# Matlab Bridge - module execution error - output list of fiducial points

**Topic ID**: 8407
**Date**: 2019-09-12
**URL**: https://discourse.slicer.org/t/matlab-bridge-module-execution-error-output-list-of-fiducial-points/8407

---

## Post #1 by @marlene (2019-09-12 16:33 UTC)

<p>Operating system:Ubuntu 16.04<br>
Slicer version: 4.10<br>
Expected behavior: output fiducial from Matlab Bridge extension<br>
Actual behavior: error</p>
<p>Hello everybody, I am implementing a Matlab Bridge extension which takes as input:</p>
<ol>
<li>two fiducial markers</li>
<li>an input mesh</li>
</ol>
<p>and as output:</p>
<ol>
<li>a long list of fiducial markers ( which are the 3D coordinates of several paths (up to 10 paths))</li>
<li>an output mesh</li>
</ol>
<p>I get an error on the first output, whenever I try to include even just one single RAS coordinates point as output. Would you help me understanding what I am missing please?</p>
<p>Just to clarify …my final goal would be to plot these paths using CurveMaker so that I am not sure whether there is also a easier way to save trajectories from Matlab and pass them to Slicer.</p>
<p>thank you very much for any suggestion</p>
<p>Marlene</p>
<p><strong>This is the Matlab Bridge function:</strong></p>
<pre><code class="lang-auto">function outputParams  = New_AFT_slicer(inputParams)

mesh = cli_geometryread(inputParams.inputmesh);
fiducials=cli_pointvectordecode(inputParams.fiducials);

start=fiducials(:,2);
target=fiducials(:,1);

[mesh,path]=sheep_skull_margin(start',target');

outputParams.Paths=path; 
cli_pointfilewrite(inputParams.Paths_calc, path);
cli_geometrywrite(inputParams.outputmesh, mesh);
</code></pre>
<p>ERROR:</p>
<p>New_AFT_slicer standard error:</p>
<pre><code class="lang-auto">Failed to execute Matlab function: New_AFT_slicer, received the following error message: 
ERROR: Command execution failed. Reference to non-existent field 'Paths_calc'.

Error in New_AFT_slicer (line 37)
cli_pointfilewrite(inputParams.Paths_calc, path);

Error in cli_commandserver (line 91)
                response=evalc(cmd);

Error in run (line 91)
evalin('caller', strcat(script, ';'));
</code></pre>

---

## Post #2 by @marlene (2019-09-12 16:50 UTC)

<p>This is the XML:</p>
<pre><code class="lang-auto">&lt;parameters&gt;
    &lt;label&gt;Inputs&lt;/label&gt;
    &lt;description&gt;&lt;![CDATA[Inputs for the processing]]&gt;&lt;/description&gt;
    &lt;geometry fileExtensions=".ply" &gt;
      &lt;label&gt;Input model&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[Input triangular surface mesh]]&gt;&lt;/description&gt;
      &lt;longflag&gt;inputmesh&lt;/longflag&gt;
      &lt;channel&gt;input&lt;/channel&gt;
    &lt;/geometry&gt;
    
    
&lt;point multiple="true" coordinateSystem="ras"&gt;
      &lt;label&gt;fiducials&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[Input volume to be filtered]]&gt;&lt;/description&gt;
      &lt;longflag&gt;fiducials&lt;/longflag&gt;
      &lt;default&gt;0,0,0&lt;/default&gt;
      &lt;channel&gt;input&lt;/channel&gt;
    &lt;/point&gt;

    &lt;label&gt;Output&lt;/label&gt;    
    &lt;description&gt;&lt;![CDATA[Computed output]]&gt;&lt;/description&gt;
    &lt;geometry fileExtensions=".ply" &gt;
      &lt;label&gt;Output model&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[Transformed triangular surface mesh.]]&gt;&lt;/description&gt;
      &lt;longflag&gt;outputmesh&lt;/longflag&gt;
      &lt;channel&gt;output&lt;/channel&gt;
    &lt;/geometry&gt;

&lt;point multiple="true" coordinateSystem="ras"&gt;
      &lt;label&gt;Paths&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[Paths generated]]&gt;&lt;/description&gt;
      &lt;longflag&gt;Paths_calc&lt;/longflag&gt;
      &lt;default&gt;0,0,0&lt;/default&gt;
      &lt;channel&gt;output&lt;/channel&gt;
    &lt;/point&gt;

  &lt;/parameters&gt;
&lt;/executable&gt;
</code></pre>

---

## Post #3 by @lassoan (2019-09-12 17:54 UTC)

<p><code>point</code> element is uses the command-line to pass point coordinates to the module, therefore cannot be used for output parameter. You have to use <code>pointfile</code> element for output point lists instead.</p>

---

## Post #4 by @roozbehshams (2019-09-13 15:12 UTC)

<p>Another way is to use Matlab engine for python, which basically gives you access to your current Matlab session in Slicer. I’ve found it to be easier especially when there’s a lot of back and forth between Matlab and Slicer. You can read more here: <a href="https://www.mathworks.com/help/matlab/matlab-engine-for-python.html" rel="nofollow noopener">https://www.mathworks.com/help/matlab/matlab-engine-for-python.html</a></p>

---

## Post #5 by @lassoan (2019-09-13 15:25 UTC)

<p>Thanks for the suggestion. Slicer’s MatlabBridge was developed many years before Matlab’s Python engine was created - maybe we should promote this new integration approach instead.</p>
<p>How do you pass MRML node content between your Matlab functions and Slicer? Using <a href="https://github.com/lassoan/SlicerPythonCLIExample" rel="nofollow noopener">Python CLI</a> or by implementing a Python scripted module?</p>

---

## Post #6 by @roozbehshams (2019-09-13 16:15 UTC)

<p>By implementing a Python scripted module. From Mathworks: " The  <code>matlab</code>  Python package provides array classes to represent arrays of MATLAB numeric types as Python variables so that MATLAB arrays can be passed between Python and MATLAB.". Like so:</p>
<pre><code>import matlab.engine
A = matlab.double([[1,2,3,4,5], [6,7,8,9,10]])
print(A)
[[1.0,2.0,3.0,4.0,5.0],[6.0,7.0,8.0,9.0,10.0]]
</code></pre>
<p>I haven’t extensively played with passing arrays back and forth since that wasn’t needed in my case, but it looks straight forward. I can put together a simple example if it helps.</p>

---

## Post #7 by @wpgao (2020-12-09 06:49 UTC)

<p>Hi Roozbeh,</p>
<p>I had installed Matlab engine for python successfully. However, I can not import it in  my module script because the python in Slicer is different from that in the system. So how can use it in my module script?<br>
Thanks!</p>

---

## Post #8 by @lassoan (2020-12-09 14:54 UTC)

<p>You need to install Python packages in Slicer’s Python environment (e.g., by running <code>pip_install</code> command in Slicer’s Python console). You can also use MatlabBridge extension to run Matlab functions from Slicer.</p>
<p>What are those Matlab features that you need that are not available in Python packages?</p>

---

## Post #9 by @wpgao (2020-12-09 15:40 UTC)

<p>Hi Andras,</p>
<p>Thanks! I followed the instruction (<a href="https://www.mathworks.com/help/matlab/matlab-engine-for-python.html" rel="noopener nofollow ugc">https://www.mathworks.com/help/matlab/matlab-engine-for-python.html</a>) mentioned by <a class="mention" href="/u/roozbehshams">@roozbehshams</a>, instead, I run "PythonSlicer setup.py install ". It works finally after I upgraded a lib.</p>
<p>There are some powerful Matlab packages in Lead-DBS and SPM which are not available in Python packages, and I plan to add these packages into my module.</p>

---

## Post #10 by @lassoan (2020-12-09 16:21 UTC)

<aside class="quote no-group" data-username="wpgao" data-post="9" data-topic="8407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/8e8cbc/48.png" class="avatar"> wpgao:</div>
<blockquote>
<p>It works finally after I upgraded a lib.</p>
</blockquote>
</aside>
<p>What exactly you had to upgrade? (just to help others who want to follow this approach)</p>
<aside class="quote no-group" data-username="wpgao" data-post="9" data-topic="8407">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/8e8cbc/48.png" class="avatar"> wpgao:</div>
<blockquote>
<p>There are some powerful Matlab packages in Lead-DBS and SPM which are not available in Python packages, and I plan to add these packages into my module.</p>
</blockquote>
</aside>
<p>I see. It is very unfortunate that these packages are built on top of closed-source proprietary software. Hopefully they will consider porting their invaluable work to open platforms, until then there is indeed not much else you can do than interface with Matlab.</p>

---

## Post #11 by @wpgao (2020-12-10 01:10 UTC)

<p>The error is “/usr/lib/x86_64-linux-gnu/libstdc++.so.6: version ‘GLIBCXX_3.4.22’ not found!</p>
<p>“In my computer there is only GLIBCXX_3.4.20, so I download libstdc++.so.6.0.22 and install it!</p>

---
