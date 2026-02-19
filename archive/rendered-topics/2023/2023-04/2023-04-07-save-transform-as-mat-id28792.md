---
topic_id: 28792
title: "Save Transform As Mat"
date: 2023-04-07
url: https://discourse.slicer.org/t/28792
---

# Save transform as .mat

**Topic ID**: 28792
**Date**: 2023-04-07
**URL**: https://discourse.slicer.org/t/save-transform-as-mat/28792

---

## Post #1 by @Melanie (2023-04-07 09:16 UTC)

<p>Hi</p>
<p>Could some please help me to save a LinearTransform as .mat file using commandline pls.</p>
<p>I have checked script repository , and tried chat GPT ,<br>
Could find anything.</p>
<p>I generate 50-100 linear transforms (after model registration) with displacement data, that needs saving as .mat files , so I am hoping to do it CLI and loop</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-04-09 01:52 UTC)

<p>I would recommend to save as .txt file. It is human-readable and easy to read and write in both Slicer and Matlab.</p>
<p>Matlab reader and writer are available here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformread.m">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformread.m" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformread.m" target="_blank" rel="noopener">PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformread.m</a></h4>


      <pre><code class="lang-m">function transform = cli_lineartransformread(filename, transformType)
%cli_transformread  Read a single 4x4 linear transformation matrix from an "Insight Transform File V1.0" text file
%
%   By default the output transform is in LPS anatomical coordinate sytem and
%   defined according to ITK ("image processing") convention.
%   If transformType is set to 'slicer' then the output transform is in RAS
%   coordinate system and defined according to Slicer ("computer graphics")
%   convention.
%   See more details at: http://www.slicer.org/slicerWiki/index.php/Documentation/4.2/FAQ#The_registration_transform_file_saved_by_Slicer_does_not_seem_to_match_what_is_shown
%

if nargin &lt; 2
  transformType = 'itk';
end

allTransforms=cli_transformread(filename);

assert(length(allTransforms)==1, 'The transform file should contain exactly one transform');
assert(strcmpi(allTransforms{1}.Transform,'AffineTransform_double_3_3'), 'The transform file should contain an AffineTransform_double_3_3 transform');

</code></pre>



  This file has been truncated. <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformread.m" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformwrite.m">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformwrite.m" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformwrite.m" target="_blank" rel="noopener">PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformwrite.m</a></h4>


      <pre><code class="lang-m">function cli_lineartransformwrite(outputfilename, transformMatrix, transformType)
%cli_transformwrite  Write a single 4x4 linear transformation matrix to an "Insight Transform File V1.0" text file
%
%   By default the output transform is in LPS anatomical coordinate sytem and
%   defined according to ITK ("image processing") convention.
%   If transformType is set to 'slicer' then the output transform is in RAS
%   coordinate system and defined according to Slicer ("computer graphics")
%   convention.
%   See more details at: http://www.slicer.org/slicerWiki/index.php/Documentation/4.2/FAQ#The_registration_transform_file_saved_by_Slicer_does_not_seem_to_match_what_is_shown
%

if nargin &lt; 3
  transformType = 'itk';
end

assert(isequal(size(transformMatrix),[4 4]), 'transformMatrix size must be 4x4');

if (strcmpi(transformType,'itk'))
  transform_lps=transformMatrix;
elseif (strcmpi(transformType, 'slicer'))
</code></pre>



  This file has been truncated. <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_lineartransformwrite.m" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
