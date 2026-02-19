---
topic_id: 34265
title: "Unable To Open Vff File"
date: 2024-02-12
url: https://discourse.slicer.org/t/34265
---

# Unable to open vff file

**Topic ID**: 34265
**Date**: 2024-02-12
**URL**: https://discourse.slicer.org/t/unable-to-open-vff-file/34265

---

## Post #1 by @sieunmiin96 (2024-02-12 19:36 UTC)

<p>I have Slicer 5.6.1, but I’m unable to open the vff file despite having the SlicerRT extension installed. The following is the error log:</p>
<p>LoadVffFile: The values for the origin must each be greater than or equal to 0.<br>
LoadVffFile: Incorrect parameters or required parameters that were not set, vff file failed to load. The required parameters are: rank, type, format, bits, bands, size, spacing, origin, rawsize, data scale, data offset, and title.<br>
Warning: In vtkSlicerVffFileReaderLogic.cxx, line 109<br>
vtkSlicerVffFileReaderLogic (0000016588499780): ReadVffFileHeader: Nothing follows the equal sign in header item: ‘batch’<br>
Warning: In vtkSlicerVffFileReaderLogic.cxx, line 109<br>
vtkSlicerVffFileReaderLogic (0000016588499780): ReadVffFileHeader: Nothing follows the equal sign in header item: ‘gel’<br>
Warning: In vtkSlicerVffFileReaderLogic.cxx, line 109<br>
vtkSlicerVffFileReaderLogic (0000016588499780): ReadVffFileHeader: Nothing follows the equal sign in header item: ‘modification_history’</p>
<p>The vff files that I’m trying to open are optical CT images, which were reconstructed using a software called VistaScan.</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2024-02-14 10:41 UTC)

<p>Thanks for including the log!</p>
<p>It is possible that the VFF files written by the latest scanners have changed. It will be needed to update the reader class.</p>
<p>For example, it is possible that the restriction for the origin to be positive is not needed, see</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/VffFileReader/Logic/vtkSlicerVffFileReaderLogic.cxx#L368">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/VffFileReader/Logic/vtkSlicerVffFileReaderLogic.cxx#L368" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/VffFileReader/Logic/vtkSlicerVffFileReaderLogic.cxx#L368" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/master/VffFileReader/Logic/vtkSlicerVffFileReaderLogic.cxx#L368</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="358" style="counter-reset: li-counter 357 ;">
          <li>if (numbersFromParsedStringOrigin.empty())
</li>
          <li>{
</li>
          <li>  vtkErrorMacro("LoadVffFile: 3 doubles were not entered for the origin.");
</li>
          <li>  parameterMissing = true;
</li>
          <li>}
</li>
          <li>else
</li>
          <li>{
</li>
          <li>  origin[0] = numbersFromParsedStringOrigin[0];
</li>
          <li>  origin[1] = numbersFromParsedStringOrigin[1];
</li>
          <li>  origin[2] = numbersFromParsedStringOrigin[2];
</li>
          <li class="selected">  if (origin[0] &lt; 0 || origin[1] &lt;0 || origin[2] &lt; 0)
</li>
          <li>  {
</li>
          <li>    vtkErrorMacro("LoadVffFile: The values for the origin must each be greater than or equal to 0.");
</li>
          <li>    parameterInvalidValue = true;
</li>
          <li>  }
</li>
          <li>}          
</li>
          <li>
</li>
          <li>std::vector&lt;int&gt; numberFromParsedStringRawsize = this-&gt;ParseNumberOfNumbersFromString&lt;int&gt;(parameterList["rawsize"], 1);
</li>
          <li>if (numberFromParsedStringRawsize.empty()) 
</li>
          <li>{
</li>
          <li>  vtkErrorMacro("LoadVffFile: An integer was not entered for the rawsize.");
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you have the capacity to build SlicerRT and try simply commenting out this check, then it would be great.</p>

---

## Post #3 by @sieunmiin96 (2024-02-15 20:55 UTC)

<p>Can you elaborate on what you mean by “building SlicerRT”? All I could find was vtkSlicerVffFileReaderLogic.so and not a cxx file.</p>
<p>I also tried downloading the vtkSlicerVffFileReaderLogic.cxx file from github, commented out the line, and added it to the folder qt-loadable modules. However, I’m still getting the same error message.</p>
<p>File path: Slicer &gt; Show Package Contents &gt; Contents &gt; Extensions-32438 &gt; SlicerRT &gt; lib &gt; Slicer-5.6 &gt; qt-loadable-modules</p>

---

## Post #4 by @cpinter (2024-02-16 11:39 UTC)

<aside class="quote no-group" data-username="sieunmiin96" data-post="3" data-topic="34265">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sieunmiin96/48/67738_2.png" class="avatar"> sieunmiin96:</div>
<blockquote>
<p>Can you elaborate on what you mean by “building SlicerRT”?</p>
</blockquote>
</aside>
<p>So the answer is no. No worries. Let me remove this condition for you then.</p>

---

## Post #5 by @cpinter (2024-02-16 11:44 UTC)

<p>I created an issue for this: <a href="https://github.com/SlicerRt/SlicerRT/issues/241" class="inline-onebox">Fix Vff file loading with latest scanners · Issue #241 · SlicerRt/SlicerRT · GitHub</a></p>
<p>I removed the condition for positive origin coordinates. The change will be reflected in the preview version tomorrow. This means that if you download the latest Slicer preview tomorrow, and install SlicerRT from there, the change will be in effect. Let’s see if there are more errors with your file. Please note that it takes time for all the extensions to be built by the factory, so it may only be available in the afternoon (also depending on your time zone).</p>

---

## Post #7 by @sieunmiin96 (2024-02-20 16:33 UTC)

<p>Thank you so much!<br>
I was able to open the vff file.<br>
I realized I forgot to install the extensions before opening the vff file in my previous reply.</p>

---

## Post #8 by @cpinter (2024-02-21 12:44 UTC)

<p>Excellent, thank you for the confirmation. I’m then closing the issue in SlicerRT.</p>

---
