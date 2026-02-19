---
topic_id: 3159
title: "Extensions Matlabbridge Send Transform 4X4 Matrix From Matla"
date: 2018-06-12
url: https://discourse.slicer.org/t/3159
---

# Extensions/MatlabBridge: Send transform (4x4 matrix) from Matlab to 3D Slicer

**Topic ID**: 3159
**Date**: 2018-06-12
**URL**: https://discourse.slicer.org/t/extensions-matlabbridge-send-transform-4x4-matrix-from-matlab-to-3d-slicer/3159

---

## Post #1 by @katharina_hecker (2018-06-12 19:48 UTC)

<p>Hi,<br>
I’m beginning to work now with Matlab. I’ve looked over descriptions and questions but some questions are not clear for me yet. So I was wondering if somebody could help me out:<br>
I wanted to ask if it is possible to visualize a filtered volume (based on matrices 181x299x305 double - created from image slices) from a Matlab file in 3D Slicer via the MatlabBridge Module Generator? Or whether I need to take the OpenIGTLink where I would need to create libraries (…) first (based on Mex files? Is it possible to see the volume then from the 3 different angles? Can this volume be adjusted with certain modules too?<br>
I’m very thankful for any kind of suggestions!</p>

---

## Post #2 by @lassoan (2018-06-13 00:39 UTC)

<aside class="quote no-group" data-username="katharina_hecker" data-post="1" data-topic="3159">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katharina_hecker/48/3431_2.png" class="avatar"> katharina_hecker:</div>
<blockquote>
<p>wanted to ask if it is possible to visualize a filtered volume (based on matrices 181x299x305 double - created from image slices) from a Matlab file in 3D Slicer via the MatlabBridge Module Generator?</p>
</blockquote>
</aside>
<p>Yes. MatlabBridge Module Generator creates a skeleton that you customize to call the Matlab function you need.</p>
<p>Note that when you use Slicer’s MatlabBridge, Slicer drives the workflow: you load input volumes and other data into Slicer, choose processing inputs and outputs, and initiate processing in Slicer, and then when processing is completed, results automatically transferred to and displayed in Slicer.</p>
<aside class="quote no-group" data-username="katharina_hecker" data-post="1" data-topic="3159">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katharina_hecker/48/3431_2.png" class="avatar"> katharina_hecker:</div>
<blockquote>
<p>Or whether I need to take the OpenIGTLink where I would need to create libraries</p>
</blockquote>
</aside>
<p>Slicer uses OpenIGTLink under the hood to communicate with the Matlab process, but you will not need to worry about these details. There is no need to build any mex files (avoiding mex files was one of the important design requirements of MatlabBridge, as it is a nightmare to maintain them) - MatlabBridge includes an OpenIGTLink server implemented in native Matlab script. But again, it is an internal detail that should not matter for you.</p>
<aside class="quote no-group" data-username="katharina_hecker" data-post="1" data-topic="3159">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katharina_hecker/48/3431_2.png" class="avatar"> katharina_hecker:</div>
<blockquote>
<p>Is it possible to see the volume then from the 3 different angles?</p>
</blockquote>
</aside>
<p>Yes, the full arsenal of Slicer’s visualization tools are available for you. You can view any number of slices, in any orientation, volume renderings, surface renderings, fusing multiple volumes, etc.</p>
<aside class="quote no-group" data-username="katharina_hecker" data-post="1" data-topic="3159">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katharina_hecker/48/3431_2.png" class="avatar"> katharina_hecker:</div>
<blockquote>
<p>Can this volume be adjusted with certain modules too?</p>
</blockquote>
</aside>
<p>Yes. You can implement complete processing workflows as a mixture of Slicer core modules and your Matlab modules.</p>
<p>I can give more specific answers if you describe the clinical problem that you would like to solve and how you plan to approach it.</p>

---

## Post #3 by @katharina_hecker (2018-06-13 06:23 UTC)

<p>Thank you very much for this detailed reply!<br>
I´m trying to display in the 3d slicer a filtered volume, which consists out of 181x299x305 double matrices(=FilteredVolume). The size of the voxels are [0.0500 0.0500 0.0500].<br>
The number of slides from which the volume was created are 181.<br>
So I was trying to write it like this:</p>
<p>img=cli_imageread(double.FilteredVolume);</p>
<p>value=cli_imageread(inputParams.name)</p>
<p>cli_imagewrite(double.FilteredVolume, img);</p>
<p>But then the error appears:</p>
<p>The class double has no Constant property or Static method named ‘FilteredVolume’.</p>
<p>Error in matrixmatlab1 (line 40)<br>
img=cli_imageread(double.FilteredVolume);</p>
<p>I know that I´m missing out something, could you maybe give me a suggestion. I would be really pleased!</p>

---

## Post #4 by @katharina_hecker (2018-06-13 06:37 UTC)

<p>I just realized that I was posting just:<br>
value=cli_imageread(inputParams.name)</p>
<p>instead what I wrote:<br>
value=cli_imageread(double.‘FilteredVolume’)</p>

---

## Post #5 by @katharina_hecker (2018-06-13 08:20 UTC)

<p>Hi again,<br>
I was trying also the way which was described in</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/PlusToolkit/PlusMatlabUtils">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/PlusToolkit/PlusMatlabUtils" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/5d596fa2bc6eeb6b351537abc6072f55f9bc02bea13be3ae1fcd7a83979d6173/PlusToolkit/PlusMatlabUtils" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/PlusToolkit/PlusMatlabUtils" target="_blank" rel="noopener nofollow ugc">GitHub - PlusToolkit/PlusMatlabUtils: Matlab utilities for reading/writing...</a></h3>

  <p>Matlab utilities for reading/writing Plus data structures and communicating with Plus applications - PlusToolkit/PlusMatlabUtils</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and load the following code:</p>
<p>igtlConnection = igtlConnect(‘…’,18944);<br>
transform.name = ‘NeedleToTracker’;</p>
<p>startTime = igtlTimestampNow();</p>
<p>for t=1:1000<br>
t=igtlTimestampNow()-startTime;<br>
transform.matrix = FilteredVolume;<br>
transform.timestamp = igtlTimestampNow();<br>
transform<br>
igtlSendTransform(igtlConnection, transform);<br>
pause(0.1)<br>
end</p>
<p>igtlDisconnect(igtlConnection);</p>
<p>And the Transform was loaded into the Slicer, but not as I expected<br>
the volume is displayed like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22f3fa93ca1d7a8a2a90d55d97bd0a73d5ebd122.png" data-download-href="/uploads/short-url/4ZcXhDvXZIvwerJFLxcDTrx6lBo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22f3fa93ca1d7a8a2a90d55d97bd0a73d5ebd122_2_690x483.png" alt="image" data-base62-sha1="4ZcXhDvXZIvwerJFLxcDTrx6lBo" width="690" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22f3fa93ca1d7a8a2a90d55d97bd0a73d5ebd122_2_690x483.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22f3fa93ca1d7a8a2a90d55d97bd0a73d5ebd122_2_1035x724.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22f3fa93ca1d7a8a2a90d55d97bd0a73d5ebd122.png 2x" data-dominant-color="64596D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1348×944 19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
instead of showing me a structure of vessels…</p>
<p>I am thankful for all help and information!</p>

---

## Post #6 by @lassoan (2018-06-14 04:04 UTC)

<p><a href="https://github.com/PlusToolkit/PlusMatlabUtils/tree/master/MatlabOpenIGTLinkInterface">MatlabOpenIGTLinkInterface</a> in PlusMatlabUtils can only send transformation matrices, not images.</p>
<p>There are two approaches to transfer images from Matlab to Slicer:</p>
<ol>
<li>MatlabBridge (I would recommend this)</li>
</ol>
<p>Slicer drives Matlab, so you must not even start Matlab, but Slicer will, when the user runs your Matlab module in Slicer. You need to create a module using Matlab module generator, customize the XML file to specify user interface for your module, and customize the m file to customize the behavior of your module.</p>
<ol start="2">
<li>Manually transfer through files</li>
</ol>
<p>Save volume to file from Matlab using <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">nrrdwrite.m</a> and load the created .nrrd file into Slicer manually or by running a command like this:</p>
<pre><code>"C:\Program Files\Slicer 4.9.0-2018-06-01\Slicer.exe" --python-code "slicer.util.loadVolume(r'c:\Users\msliv\Documents\Data\MRHead.nrrd')"</code></pre>

---

## Post #7 by @katharina_hecker (2018-06-14 06:26 UTC)

<p>Thank you for your suggestions!</p>
<p>I was creating a new Module in Slicer, which worked (called ‘Matrix1’)<br>
I was saving the needed Matrix in a mat file (‘matrixfilteredvolume.mat’) and I was loadinng it into the .m file from Matrix1 module. Then I was saving the mat file (FilteredVolume matrix) under a new variable called ‘Matrix’. I was changing the XML file like this:</p>
<pre><code>&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;executable&gt;
  &lt;category&gt;Matlab&lt;/category&gt;
  &lt;title&gt;Matrix1&lt;/title&gt;
  &lt;description&gt;&lt;![CDATA[Perform a simple image processing and image statistics computation in Matlab.]]&gt;&lt;/description&gt;
  &lt;version&gt;0.0.0.1&lt;/version&gt;
  &lt;documentation-url&gt;http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/MatlabBridge&lt;/documentation-url&gt;
  &lt;license/&gt;
  &lt;contributor&gt;Andras Lasso (PerkLab)&lt;/contributor&gt;
  &lt;acknowledgements&gt;&lt;![CDATA[SparKit is a project funded by Cancer Care Ontarioand the Ontario Consortium for Adaptive Interventions in Radiation Oncology (OCAIRO) to provide free, open-source toolset for radiotherapy and related image-guided interventions.]]&gt;&lt;/acknowledgements&gt;
  &lt;parameters&gt;
    &lt;label&gt;Processing Parameters&lt;/label&gt;
    &lt;description&gt;&lt;![CDATA[Parameters for the processing]]&gt;&lt;/description&gt;
    &lt;integer&gt;
      &lt;label&gt;Threshold&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[All voxels below this value will be set to zero]]&gt;&lt;/description&gt;
      &lt;longflag&gt;threshold&lt;/longflag&gt;
      &lt;default&gt;50&lt;/default&gt;
      &lt;constraints&gt;
        &lt;minimum&gt;-2000&lt;/minimum&gt;
        &lt;maximum&gt;5000&lt;/maximum&gt;
        &lt;step&gt;5&lt;/step&gt;
      &lt;/constraints&gt;      
    &lt;/integer&gt;
  &lt;/parameters&gt;
  &lt;parameters&gt;
    &lt;label&gt;IO&lt;/label&gt;
    &lt;description&gt;&lt;![CDATA[Input/output parameters]]&gt;&lt;/description&gt;
    &lt;image&gt;
      &lt;label&gt;Matrix&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[Input volume to be filtered]]&gt;&lt;/description&gt;
      &lt;longflag&gt;inputvolume&lt;/longflag&gt;
      &lt;channel&gt;input&lt;/channel&gt;
    &lt;/image&gt;
    &lt;image&gt;
      &lt;label&gt;Matrix&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[Output filtered]]&gt;&lt;/description&gt;
      &lt;longflag&gt;outputvolume&lt;/longflag&gt;
      &lt;channel&gt;output&lt;/channel&gt;
    &lt;/image&gt;
  &lt;/parameters&gt;
  &lt;parameters&gt;
    &lt;label&gt;Output&lt;/label&gt;
    &lt;description&gt;Matlab command output&lt;/description&gt;
    &lt;double&gt;
      &lt;label&gt;Minimum&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[Image mininum]]&gt;&lt;/description&gt;
      &lt;name&gt;min&lt;/name&gt;
      &lt;channel&gt;output&lt;/channel&gt;
      &lt;default&gt;&lt;/default&gt;
    &lt;/double&gt;    
    &lt;double&gt;
      &lt;label&gt;Maximum&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[Image maximum]]&gt;&lt;/description&gt;
      &lt;name&gt;max&lt;/name&gt;
      &lt;channel&gt;output&lt;/channel&gt;
      &lt;default&gt;&lt;/default&gt;
    &lt;/double&gt;    
  &lt;/parameters&gt;
&lt;/executable&gt;
</code></pre>
<hr>
<p>and where running the code of the .m file through the new Slicer module:</p>
<pre><code>function outputParams=Matrix1(inputParams)

load 'matrixfilteredvolume.mat'

Matrix = FilteredVolume

img=cli_imageread(inputParams.'Matrix');

outputParams.min=min(min(min(img.pixelData)));
outputParams.max=max(max(max(img.pixelData)));

img.pixelData=(double(img.pixelData)&gt;inputParams.threshold)*100;

cli_imagewrite(inputParams.'Matrix', img);
</code></pre>
<hr>
<p>The following Error appeared:<br>
Matrix1 standard error:</p>
<blockquote>
<p>Failed to execute Matlab function: Matrix1, received the following error message:<br>
ERROR: Command execution failed. Error: File: Matrix1.m Line: 16 Column: 32<br>
Unexpected MATLAB expression.</p>
<p>Error in cli_commandserver (line 91)<br>
response=evalc(cmd);</p>
<p>Error in run (line 91)<br>
evalin(‘caller’, strcat(script, ‘;’));</p>
</blockquote>
<hr>
<p>Did I load the matrix in a wrong way?</p>

---

## Post #8 by @lassoan (2018-06-15 04:54 UTC)

<p>Have a closer look at the <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabModuleGenerator/Resources/Templates/MatlabModuleTemplate.m">originally generated module skeleton</a>. You refer to parameters by inputParams.variableName (not quoted like ‘variableName’).</p>
<p>Do you want to pass an image or a transformation matrix between Matlab and Slicer?</p>
<p>If you are just learning Matlab then I would recommend to consider using Python instead. While Matlab still has somewhat better IDE and documentation than Python but in most other things are Python is much more capable, it’s free, open-source, has huge community, many libraries, etc., so overall learning it is probably a better long-term investment.</p>

---

## Post #9 by @katharina_hecker (2018-06-15 04:55 UTC)

<p>I want to pass a matrix</p>

---

## Post #10 by @lassoan (2018-06-15 04:56 UTC)

<p>Do you mean a 4x4 homogeneous transformation matrix?</p>

---

## Post #11 by @katharina_hecker (2018-06-15 04:56 UTC)

<p>it consists of the following parameters: 181x299x305 double</p>

---

## Post #12 by @katharina_hecker (2018-06-15 04:58 UTC)

<p>i= 181 are the slices from which it was created and the SizeVoxel are [0.050000000000000 0.050000000000000 0.050000000000000]</p>

---

## Post #13 by @lassoan (2018-06-15 04:58 UTC)

<p>So, you want to pass an image volume. Then the default generated skeleton code should work as is. First don’t modify anything in it and see if it computes thresholded image. If everything is OK then modify the script step-by-step to see what changes cause errors.</p>

---

## Post #14 by @katharina_hecker (2018-06-15 04:59 UTC)

<p>i´m kind of stuck in the modifying part</p>

---

## Post #15 by @katharina_hecker (2018-06-15 05:00 UTC)

<p>I´m not sure wheter I should use this:</p>
<p>%<br>
load ‘matrixfilteredvolume.mat’</p>
<p>Matrix = FilteredVolume</p>
<p>img=cli_imageread(Matrix);</p>
<p>outputParams.min=min(min(min(img.pixelData)));<br>
outputParams.max=max(max(max(img.pixelData)));</p>
<p>img.pixelData=(double(img.pixelData)&gt;inputParams.threshold)*100;</p>
<p>cli_imagewrite(Matrix, img);</p>

---

## Post #16 by @katharina_hecker (2018-06-15 05:01 UTC)

<p>or if I have to add infos about the slices and spaces too</p>

---

## Post #17 by @lassoan (2018-06-15 05:05 UTC)

<p>Right now, your code has two issues:</p>
<ol>
<li>There is no such variable as Matrix. You’ve only set the label to Matrix in the XML file, but the variable name is generated from the <code>longflag</code> parameter.</li>
<li>You added single-quotes around variable name. That’s invalid syntax, just remove the quotes.</li>
</ol>
<p>Image origin, spacing, and axis directions are stored in <code>img.ijkToLpsTransform</code>. This matrix is a homogeneous transform, which transforms voxel (IJK) coordinates to physical (LPS) coordinates. Top-left 3x3 submatrix is axis direction and spacing. Top-right 3-element column vector is the image origin.</p>

---

## Post #18 by @katharina_hecker (2018-06-15 05:07 UTC)

<p>yes I was going over this function already but I don´t understand this part:</p>
<pre><code>% Define origin, spacing, axis directions by a homogeneous transformation matrix:
img.ijkToLpsTransform = [ 1.2 0 0 10; 0 1.2 0 12; 0 0 3.0 -22; 0 0 0 1];
</code></pre>
<p>I was applying the following parameters:</p>
<pre><code>load 'matrixfilteredvolume.mat'

Matrix = FilteredVolume

L = max(Matrix)

[X,Y,Z]=meshgrid(1:size(L,1), 1:size(L,2), 1:size(L,3))

img.pixelData = x/3+y/4+z/2;
 
% Define origin, spacing, axis directions by a homogeneous transformation matrix:
img.ijkToLpsTransform = [ 0.05 0 0 181; 0 0.05 0 299; 0 0 0.05 305; 0 0 0 1];
 
% Enable compression

img.metaData.encoding='gzip';

nrrdwrite('testOutput.nrrd', img);

% Open file for writing
fid=fopen(outputFilename, 'w');
if(fid&lt;=0)</code></pre>

---

## Post #19 by @katharina_hecker (2018-06-15 05:11 UTC)

<blockquote>
<p>There is no such variable as Matrix. You’ve only set the label to Matrix in the XML file, but the variable name is generated from the longflag parameter.</p>
</blockquote>
<p>so I have to change the location of ‘Matrix’ in the XML file to here:</p>
<pre><code>&lt;label&gt;Threshold&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[All voxels below this value will be set to zero]]&gt;&lt;/description&gt;
      &lt;longflag&gt;Matrix&lt;/longflag&gt;
</code></pre>
<blockquote>
<p>You added single-quotes around variable name. That’s invalid syntax, just remove the quotes.</p>
</blockquote>
<p>where exactly do you mean?</p>

---

## Post #20 by @katharina_hecker (2018-06-15 05:13 UTC)

<p>sorry this part was lost in the reply:<br>
so I have to change the location of ‘Matrix’ in the XML file to here:<br>
Threshold</p>
<pre><code>&lt;label&gt;Threshold&lt;/label&gt;
      &lt;description&gt;&lt;![CDATA[All voxels below this value will be set to zero]]&gt;&lt;/description&gt;
      &lt;longflag&gt;Matrix&lt;/longflag&gt;</code></pre>

---

## Post #21 by @lassoan (2018-06-15 05:29 UTC)

<p>Probably the simplest is to revert all your changes in the .xml and .m file and just modify these lines in your .m file:</p>
<pre><code>img.pixelData = some3DArray;
img.ijkToLpsTransform = [ 0.05 0 0 0; 0 0.05 0 0; 0 0 0.05 0; 0 0 0 1];</code></pre>

---

## Post #22 by @katharina_hecker (2018-06-15 05:33 UTC)

<p>thank you very much.<br>
so just to understand it correctly: I use not theis part anymore:</p>
<pre><code>img=cli_imageread(inputParams.inputvolume);

outputParams.min=min(min(min(img.pixelData)));
outputParams.max=max(max(max(img.pixelData)));

img.pixelData=(double(img.pixelData)&gt;inputParams.threshold)*100;

cli_imagewrite(inputParams.outputvolume, img);
</code></pre>
<p>instead I just add:</p>
<pre><code>img.pixelData = some3DArray;
img.ijkToLpsTransform = [ 0.05 0 0 0; 0 0.05 0 0; 0 0 0.05 0; 0 0 0 1];
</code></pre>
<p>and leave the XML file like it is.</p>
<p>I really appreciate your effort. it is so important for me</p>

---

## Post #23 by @lassoan (2018-06-15 05:37 UTC)

<p><code>cli_imageread</code> reads data from Slicer. If your image is taken from a different source then this part is not needed.</p>
<p><code>cli_imagewrite</code> writes the volume so that Slicer can read it, so that is still needed.</p>
<p>You have to take care of replacing <code>some3DArray</code> with actual data that you get from somewhere.</p>

---

## Post #24 by @katharina_hecker (2018-06-15 05:38 UTC)

<p>ok thanks I will try it out.<br>
The xml-file i dont change at all?</p>

---

## Post #25 by @katharina_hecker (2018-06-15 06:13 UTC)

<p>Dear Mr. Lasso,<br>
I was running the following code:</p>
<p>load ‘matrixfilteredvolume.mat’</p>
<p>Matrix = FilteredVolume</p>
<p>cli_imagewrite(inputParams.Matrix)</p>
<p>img.pixelData = Matrix;<br>
img.ijkToLpsTransform = [ 0.05 0 0 0; 0 0.05 0 0; 0 0 0.05 0; 0 0 0 1];</p>
<p>cli_imagewrite(onputParams.Matrix, img)</p>
<p>and I´m getting the error:<br>
Not enough input arguments<br>
error in: cli_imagewrite(inputParams.Matrix)</p>
<p>Which kind of inputParams I should change or which parameters are actually missing?</p>
<p>Thank you so much for your help!</p>

---

## Post #26 by @katharina_hecker (2018-06-15 08:26 UTC)

<p>Dear Mr. Lasso,<br>
I was thinking over my code again and came to the following conclusion, which I took from your poster:</p>
<p><a href="http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Lasso2014b-poster.pdf" rel="noopener nofollow ugc">http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Lasso2014b-poster.pdf</a></p>
<p>I tried to adjust all the parameter and tried to run this code:</p>
<p>load(‘matrixfilteredvolume.mat’)</p>
<p>Volume = (FilteredVolume)</p>
<p>Matrixin=cli_imagewrite(inputParams.Volume);</p>
<p>img.pixelData = Matrixin;<br>
img.ijkToLpsTransform = [ 0.05 0 0 0; 0 0.05 0 0; 0 0 0.05 0; 0 0 0 1];</p>
<p>outputvol = Matrixin</p>
<p>cli_imagewrite(inputParams.outputvolume, outputvol);</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91558df0d74f1d93e4c565aa54b490eb790b53bb.png" alt="image" data-base62-sha1="kJGx23hDtnxKAsjlpN8CLl3L4wj" width="270" height="74"></p>
<p>I would be very pleased about any suggestions!</p>

---

## Post #27 by @katharina_hecker (2018-06-15 08:33 UTC)

<p>PS: Error Not enough input arguments in line:</p>
<p>Matrixin=cli_imagewrite(inputParams.Volume);</p>

---

## Post #28 by @katharina_hecker (2018-06-16 08:30 UTC)

<p>after looking over the whole discussion, I’m coming to this conclusion:</p>
<p>matlab code:</p>
<p>load(‘matrixfilteredvolume.mat’);</p>
<p>img.ijkToLpsTransform = [ 0.05 0 0 0; 0 0.05 0 0; 0 0 0.05 0; 0 0 0 1];</p>
<p>img.pixelData=FilteredVolume</p>
<p>cli_imagewrite(img.ijkToLpsTransform.FilteredVolume, img);</p>
<hr>
<p>it seems to be the right path but I still got one error to solve:</p>
<p>img =</p>
<p>struct with fields:</p>
<pre><code>ijkToLpsTransform: [4×4 double]
        pixelData: [181×299×305 double]
</code></pre>
<p>Struct contents reference from a non-struct array object.</p>
<p>Error in afterMoritz (line 19)<br>
cli_imagewrite(img.ijkToLpsTransform.FilteredVolume, img);</p>
<p>I am thankful for all kind of suggestions!</p>

---

## Post #29 by @lassoan (2018-06-16 14:31 UTC)

<p>There is no such thing as img.ijkToLpsTransform.FilteredVolume. Follow the working example more closely. Something like this should work:</p>
<p>cli_imagewrite(inputParams.outputvolume, img);</p>

---

## Post #30 by @katharina_hecker (2018-06-16 16:06 UTC)

<p>Thanks a lot Sir for your reply! I did now everything which you said:</p>
<p>load(‘matrixfilteredvolume.mat’); <a class="hashtag" href="https://discourse.slicer.org/tags/loading">#<span>loading</span></a> of  matrix</p>
<p>img.pixelData = FilteredVolume <span class="hashtag">#using</span> the codes you suggested</p>
<p>outputParams.min=min(min(min(img.pixelData))); <span class="hashtag">#following</span> the working example more closely<br>
outputParams.max=max(max(max(img.pixelData)));</p>
<p>img.ijkToLpsTransform = [ 0.05 0 0 0; 0 0.05 0 0; 0 0 0.05 0; 0 0 0 1];</p>
<p>cli_imagewrite(inputParams.outputvolume, img); <span class="hashtag">#use</span> the cli_imagewrite code to import the data like you said in the last post</p>
<p>Still I seem to miss something out, since the error appears:</p>
<p>Not enough input arguments.</p>
<p>Error in matrixvolumeto3dslicer (line 23)<br>
cli_imagewrite(inputParams.outputvolume, img);</p>
<p>I really appreciate your effort and am very thankful for your suggestions.</p>

---

## Post #31 by @lassoan (2018-06-16 16:41 UTC)

<p>Modifying an example script to use your data instead of similar sample data should be a site straightforward Matlab programming task. You should be able to find a solution by reflecting on the error message, experimenting, Google searching, or asking someone in your group to sit down with you and go through your code.</p>
<p>If you are just starting to learn Matlab, then I would recommend to consider learning Python instead, as most likely you’ll benefit from that more in the long term.</p>

---
