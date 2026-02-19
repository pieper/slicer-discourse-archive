---
topic_id: 8359
title: "Returning A Vector From Cli Module"
date: 2019-09-10
url: https://discourse.slicer.org/t/8359
---

# Returning a vector from CLI module

**Topic ID**: 8359
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/returning-a-vector-from-cli-module/8359

---

## Post #1 by @fpsiddiqui91 (2019-09-10 09:01 UTC)

<p>Hello Developers.</p>
<p>I am developing a CLI module and calling it from my scripted module using  “slicer.cli.run” . I can parse the arguments from my scripted module to CLI module but I failed to get the returning arguments from my CLI module.</p>
<p>I am trying to copy fudicial registration module but unfortunately I wasn’t able to get the returning argument in my scripted module. I am missing simething, it might be very basic, but I have wasted alot of time in it.</p>
<p>My XML is:</p>
<pre><code>&lt;?xml version="1.0" encoding="utf-8"?&gt;
</code></pre>

  Examples
  CLI_test
  
  0.0.1
  http://www.example.com/Slicer/Modules/CLI_test
  Slicer
  FirstName LastName (Institution), FirstName LastName (Institution)
  This work was partially funded by NIH grant NXNNXXNNNNNN-NNXN
   
    IO
    
    
      sigmas
      sigmas
      s
      output
<pre><code>  &lt;label&gt;Sigmas&lt;/label&gt;
  &lt;description&gt;&lt;![CDATA[A double value (in units of mm) passed to the algorithm]]&gt;&lt;/description&gt;
     &lt;/float-vector&gt;

&lt;double&gt;
  &lt;name&gt;rms&lt;/name&gt;
  &lt;longflag&gt;rms&lt;/longflag&gt;
  &lt;description&gt;&lt;![CDATA[Display RMS Error.]]&gt;&lt;/description&gt;
  &lt;flag&gt;R&lt;/flag&gt;
  &lt;label&gt;RMS Error&lt;/label&gt;
  &lt;channel&gt;output&lt;/channel&gt;
  &lt;default&gt;0.1&lt;/default&gt;
&lt;/double&gt;
</code></pre>
<p>The part of updating rms value in my CLI .cpp code is:</p>
<p>rms=42.0 ;<br>
std::ofstream rts;<br>
rts.open(returnParameterFile.c_str() );<br>
rts &lt;&lt; “rms=” &lt;&lt; rms &lt;&lt; std::endl;<br>
rts.close();</p>
<p>I dont know how to get this “rms” value in my scripted module (python code). Thank you in advance</p>

---

## Post #2 by @fpsiddiqui91 (2019-09-10 11:44 UTC)

<p>Just to be clear, If I run my CLI module as standalone program it does generate an output text file, my question is, how can I get the output if I call my CLI from scripted module with slicer.cli.run command.</p>
<p>Thank you.</p>

---

## Post #3 by @lassoan (2019-09-10 12:59 UTC)

<p>Return values are stored in the parameter node and you can retrieve it using <code>GetParameterAsString()</code> method. For example:</p>
<pre><code class="lang-python">parameterNode = slicer.util.getNode('Execution Model Tour')
returnedRmsValue = float(parameterNode.GetParameterAsString('rms'))
</code></pre>

---

## Post #4 by @fpsiddiqui91 (2019-09-10 13:16 UTC)

<p>Thank you for you reply Andras, I have tried this command, the problem is my ‘rms’ variable doesn’t get updated. its just returning the same initial value.</p>
<p>Ideally, inital rms value should go into my CLI module , it should get updated, and I should get the updated variable.</p>
<p>this is the python code from where I am calling my CLI</p>
<pre><code>module = slicer.modules.cli_test

rms=5.0
a=(np.random.randint(0, 100, size=(30, 10, 2)) ).tolist()

cliParams = {
  'sigmas' : a,
  'rms' : rms,


}

cliNode = slicer.cli.run(module, None, cliParams, wait_for_completion=True)

returnedRmsValue = float(cliNode.GetParameterAsString('rms'))
print(returnedRmsValue)
</code></pre>
<p>The returned RMS value should be 49, but it is still giving 5.<br>
Am I missing something?</p>

---

## Post #5 by @lassoan (2019-09-10 13:26 UTC)

<p>A parameter can be either input or output, defined by the <code>channel</code> element. For example, <code>&lt;channel&gt;output&lt;/channel&gt;</code> means an output parameter.</p>

---

## Post #6 by @fpsiddiqui91 (2019-09-10 13:28 UTC)

<p>yes, I have defined the parameter as output. (xml attached in my first post). Even then it is not updating.</p>

---

## Post #7 by @lassoan (2019-09-10 13:33 UTC)

<p>It works for me with the ExecutionModelTour test module. See how to correctly write output parameters here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/e091a2b016eef4a621fce1dfecc6faa7f6433b51/Modules/CLI/ExecutionModelTour/ExecutionModelTour.cxx#L188-L198" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/e091a2b016eef4a621fce1dfecc6faa7f6433b51/Modules/CLI/ExecutionModelTour/ExecutionModelTour.cxx#L188-L198" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/e091a2b016eef4a621fce1dfecc6faa7f6433b51/Modules/CLI/ExecutionModelTour/ExecutionModelTour.cxx#L188-L198</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="188" style="counter-reset: li-counter 187 ;">
<li>// Write out the return parameters in "name = value" form</li>
<li>std::ofstream rts;</li>
<li>rts.open(returnParameterFile.c_str() );</li>
<li>rts &lt;&lt; "anintegerreturn =  10" &lt;&lt; std::endl;</li>
<li>rts &lt;&lt; "abooleanreturn = true" &lt;&lt; std::endl;</li>
<li>rts &lt;&lt; "afloatreturn = 34.2" &lt;&lt; std::endl;</li>
<li>rts &lt;&lt; "adoublereturn = 102.7" &lt;&lt; std::endl;</li>
<li>rts &lt;&lt; "astringreturn = Good-bye" &lt;&lt; std::endl;</li>
<li>rts &lt;&lt; "anintegervectorreturn = 4,5,6,7" &lt;&lt; std::endl;</li>
<li>rts &lt;&lt; "astringchoicereturn = Ron" &lt;&lt; std::endl;</li>
<li>rts.close();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>There are no whitespaces in your code above, maybe that breaks the output file parsing.</p>

---

## Post #8 by @fpsiddiqui91 (2019-09-10 13:45 UTC)

<p>Thank you fro your response Andras, I have tried the exact same thing. Even hardcoded the text, it is still returning the same value.</p>
<p>Am I making any mistake in calling a CLI?</p>
<pre><code>cliNode = slicer.cli.run(module, None, cliParams, wait_for_completion=True)
</code></pre>
<p>parameters being:</p>
<pre><code>rms=5.0
a=(np.random.randint(0, 100, size=(30, 10, 2)) ).tolist()
sigmaout=23.0
cliParams = {
  'sigmas' : a,
  'rms' : rms,
  'sigmaout' : sigmaout

}</code></pre>

---

## Post #9 by @fpsiddiqui91 (2019-09-10 14:33 UTC)

<p>Thank you Andras, it worked. there were some other problems. Thank you for your help</p>

---
