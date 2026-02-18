# How to get the normalized image (file)?

**Topic ID**: 25709
**Date**: 2022-10-14
**URL**: https://discourse.slicer.org/t/how-to-get-the-normalized-image-file/25709

---

## Post #1 by @Josefa_Garcia (2022-10-14 17:47 UTC)

<p>Hi, is there an option to get the image normalized?, because after run the feature extraction I checked the histogram of the image from which I extracted the features and it didn’t change. (I have normalize enabled in the script)</p>

---

## Post #2 by @lassoan (2022-10-19 05:51 UTC)

<p>You can set the same window/level settings by either right-clicking on the volume in a slice view and selecting the same “Window/level preset”; or in Volumes module’s Display section make sure you have the same <code>W</code> and <code>L</code> (window and level) values for your volumes.</p>

---

## Post #3 by @Josefa_Garcia (2022-10-19 12:51 UTC)

<p>Hi Andras, I’ve checked the histogram from the volume information and then plotted the histogram, so I think that is not the problem. I’ve attached the parameters I’m using, I’ve also tried running the extraction with the manual customization. Do I need to add anything else? thank you, appreciate your help!</p>
<p>imageType:<br>
Original: {}</p>
<p>featureClass:<br>
shape:<br>
firstorder:<br>
glcm:<br>
- ‘Autocorrelation’<br>
- ‘JointAverage’<br>
- ‘ClusterProminence’<br>
- ‘ClusterShade’<br>
- ‘ClusterTendency’<br>
glrlm:<br>
glszm:<br>
gldm:</p>
<p>setting:<br>
normalize: true<br>
normalizeScale: 100  # This allows you to use more or less the same bin width.</p>
<p>binWidth: 64<br>
voxelArrayShift: 300<br>
label: 1</p>
<p><span class="hashtag">#Resegmentation:</span> remove outliers<br>
resegmentRange: [-3, 3]<br>
resegmentMode: sigma</p>

---

## Post #4 by @lassoan (2022-10-19 13:45 UTC)

<p>I’m not experienced with how to configure SlicerRadiomics. Maybe <a class="mention" href="/u/joostjm">@JoostJM</a> or other radiomics experts can help.</p>

---
