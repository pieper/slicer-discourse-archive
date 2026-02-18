# ROI to IJK coordinates with MATLAB bridge

**Topic ID**: 14764
**Date**: 2020-11-25
**URL**: https://discourse.slicer.org/t/roi-to-ijk-coordinates-with-matlab-bridge/14764

---

## Post #1 by @OscarD (2020-11-25 10:50 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.0<br>
Expected behavior: Find IJK coordinates of ROI<br>
Actual behavior: I get negative or bigger than dimensions IJK coordinates</p>
<p>Dear slicers,</p>
<p>I am trying to get iMin, iMax, jMin, jMax, kMin, kMax from some Annotation ROI using a MATLAB bridge module such that<br>
ROI = Volume[iMin:iMax,jMin:jMax,kMin:kMax] and then I will perform some analysis on the ROI on MATLAB.</p>
<p>I have created a MATLAB module thanks to MATLAB bridge to <strong>get IJK coordinates of an ROI.</strong><br>
<strong>Inputs of module</strong></p>
<ul>
<li>ROI</li>
<li>Volume (to get ijkToLpsTransform…)</li>
</ul>
<p><strong>Outputs</strong></p>
<ul>
<li>IJK coordinates so ROI = Volume(iMin:iMax,jMin:jMax,kMin:kMax)</li>
</ul>
<p>I based my code on 2 MATLAB bridge module examples :</p>
<ul>
<li>FillAroundSeeds : <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/Examples/FillAroundSeeds" rel="noopener nofollow ugc">https://github.com/PerkLab/SlicerMatlabBridge/tree/master/Examples/FillAroundSeeds</a>
</li>
<li>MatlabBridgeParameterPassingTest : <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/Examples/MatlabBridgeParameterPassingTest" rel="noopener nofollow ugc">https://github.com/PerkLab/SlicerMatlabBridge/tree/master/Examples/MatlabBridgeParameterPassingTest</a>
</li>
</ul>
<p>Here is my code</p>
<pre><code class="lang-auto">function outputParams=ijkROI(inputParams)
% returns ijk coordinates of Annotation ROI
% Parameters:
%   inputParams.region: ROI
%   inputParams.inputvolume: input volume
%   outputParams.stringCoordinates: coordinates of ROI as string 'iMin:iMax,jMin:jMax,kMin:kMax'

imageValue = cli_imageread(inputParams.inputImage);
regionValue = cli_pointvectordecode(inputParams.region);
[~, regionCount] = size(regionValue);

% only one ROI
assert(regionCount==1)
regionIndex = 1;

% get center of ROI and radius
radius_LPS = [regionValue(4:6,regionIndex); 0];
% radius_IJK = abs(round(imageValue.ijkToLpsTransform\radius_LPS));
radius_IJK = ceil(abs(imageValue.ijkToLpsTransform\radius_LPS));

center_LPS = [regionValue(1:3,regionIndex); 1];
center_IJK = round(imageValue.ijkToLpsTransform\center_LPS);

% get coordinates of ROI
ROIijk = [center_IJK(1)-radius_IJK(1),...
    center_IJK(1)+radius_IJK(1),...
    center_IJK(2)-radius_IJK(2),...
    center_IJK(2)+radius_IJK(2),...
    center_IJK(3)-radius_IJK(3),...
    center_IJK(3)+radius_IJK(3)];

% assert coordinates are not outside input volume
volumeSize = size(imageValue.pixelData);
% assert((ROIijk(1) &gt; 1) &amp; (ROIijk(3) &gt; 1) &amp; (ROIijk(5) &gt; 1))
% assert((ROIijk(2) &lt; volumeSize(1)) &amp; (ROIijk(4) &lt; volumeSize(2)) &amp; (ROIijk(6) &lt; volumeSize(3)))

% Write outputs
outputParams.stringCoordinates = sprintf('%d:%d,%d:%d,%d:%d',ROIijk(1),ROIijk(2),ROIijk(3),ROIijk(4),ROIijk(5),ROIijk(6));
</code></pre>
<p>I have tried it with a random Annotation ROI inside MRHead volume.<br>
The center given by regionValue = cli_pointvectordecode(inputParams.region) is consistent with coordinates of center in Red, Green and Yellow slices in user’s interface.<br>
Yet radius is bigger than expected and I get negative coordinates or coordinates bigger than dimension.</p>
<p>Any idea why the ijkToLpsTransform gives results outside the ROI ?</p>
<p>Thank you very much</p>

---

## Post #2 by @OscarD (2020-12-04 09:06 UTC)

<p>Eventually I have found the problem.<br>
I need to convert first RAS coordinates to LPS coordinates. With this piece of code everything works smoothly.</p>
<pre><code class="lang-auto">% get center of ROI
center_RAS = [regionValue(1:3,regionIndex); 1];
% Point coordinates are provided by Slicer in RAS coordinate system
% Multiply the first two components by -1 to obtain points in LPS coordinate system
center_LPS = [-1*center_RAS(1:2,:); center_RAS(3:end,:)];
center_IJK = round(imageValue.ijkToLpsTransform\center_LPS);

% get radius of ROI
radius_RAS = [regionValue(4:6,regionIndex); 0];
radius_LPS = [-1*radius_RAS(1:2,:); radius_RAS(3:end,:)];
radius_IJK = round(imageValue.ijkToLpsTransform\radius_LPS);
</code></pre>

---
