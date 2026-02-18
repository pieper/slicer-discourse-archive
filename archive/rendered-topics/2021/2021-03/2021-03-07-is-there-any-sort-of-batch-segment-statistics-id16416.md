# Is there any sort of "batch" segment statistics?

**Topic ID**: 16416
**Date**: 2021-03-07
**URL**: https://discourse.slicer.org/t/is-there-any-sort-of-batch-segment-statistics/16416

---

## Post #1 by @Maxnach (2021-03-07 17:10 UTC)

<p>Hello everyone,</p>
<p>I performed semi-automated segmentation of muscles on many CT-scan of patients. The data base is organized this way : patients \ slice \ segmentation. For each patients, there is 2 or 3 slice at different time points (its only one slice for the measurements, not a volume). I would like to compute the mean area + mean density in a first step (and eventually apply a pyradiomics pipeline further on). Here is the structure of the data :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/064a87031fbf374274a5f3f4d3a07b35dc545a2d.jpeg" data-download-href="/uploads/short-url/TExq0857kScO4yDTJ6FBf9zPRP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/064a87031fbf374274a5f3f4d3a07b35dc545a2d_2_690x388.jpeg" alt="image" data-base62-sha1="TExq0857kScO4yDTJ6FBf9zPRP" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/064a87031fbf374274a5f3f4d3a07b35dc545a2d_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/064a87031fbf374274a5f3f4d3a07b35dc545a2d_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/064a87031fbf374274a5f3f4d3a07b35dc545a2d_2_1380x776.jpeg 2x" data-dominant-color="F4F6F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">8000×4500 752 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there anyway to compute a batch script (or maybe it already exists?) that would create a single table with patients name and corresponding “segment statistic output” ? I have more &gt;100 and must admit I’m afraid I’ll have to do everything manually…</p>

---

## Post #2 by @pieper (2021-03-08 16:22 UTC)

<p>I haven’t done this myself, but if you are able to do a little bit of python programming this is certainly doable.  Have you gone through the tutorials enough that you are comfortable with doing some scripting?  If so we can give you some specific suggestions for this task.</p>

---

## Post #3 by @Maxnach (2021-03-08 16:28 UTC)

<p>Hello,</p>
<p>Thank you very much for your answer. The problem is I am a complete beginner in programming language…currently starting with R for PhD purposes but never done python or matlab…</p>
<p>I went through the tutorial but did not find any pre-set option/tools to get the segment statistic output in a table with patient’s name (as organized in the DICOM)…</p>

---

## Post #4 by @pieper (2021-03-08 16:34 UTC)

<p>Is there anyone here who has done something similar and is able to step up with some code?</p>
<p>100 cases is on that borderline where you might just be more efficient to do it by hand, although you will benefit much more in the long term by learning the python scripting.</p>
<p>You might start by looking at the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator">Case Iterator</a>.</p>

---

## Post #5 by @Maxnach (2021-03-08 17:40 UTC)

<p>Thank you for your quick feedback.</p>
<p>My main issue is that I already performed all segmentations and it seems that Case Iterator would have required me to start with it beforehand…</p>
<p>I already tried manually but this is a nightmare as I have ± 100 patients with 1 to 3 studies per patients (hence &gt;200) and when I go to segment statistics, the lists of studies are not sorted by patients name but by slice names, which makes almost impossible to match each slice names with each .DICOM files :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e59a82fe70f129e0e395ce127c2c3b2c3f4054ec.png" data-download-href="/uploads/short-url/wLanAGNmDUBlCV86sSBy6sDWF2I.png?dl=1" title="Slicer segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e59a82fe70f129e0e395ce127c2c3b2c3f4054ec_2_690x393.png" alt="Slicer segment" data-base62-sha1="wLanAGNmDUBlCV86sSBy6sDWF2I" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e59a82fe70f129e0e395ce127c2c3b2c3f4054ec_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e59a82fe70f129e0e395ce127c2c3b2c3f4054ec_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e59a82fe70f129e0e395ce127c2c3b2c3f4054ec_2_1380x786.png 2x" data-dominant-color="ADB2B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer segment</span><span class="informations">1524×870 71.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Help^^</p>

---

## Post #6 by @lassoan (2021-03-08 20:01 UTC)

<p>You can find example scripts for processing a single case <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Quantifying_segments">script repository</a> and <a href="https://github.com/Slicer/Slicer/blob/9656e088dcf221e5ae60dd950d19593e77c8714b/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L707-L926">module tests</a>). Once you have a code snippet that works for a single file, you can <a href="https://www.google.com/search?q=python+iterate+through+files+in+folder">iterate through all the files in a folder</a>.</p>

---

## Post #7 by @Andinet_Enquobahrie (2021-03-09 20:24 UTC)

<p>Dear <a class="mention" href="/u/maxnach">@Maxnach</a></p>
<p>Can you try something like the following (iterate through all the segmentation MRML modes in your slicer scene and generate the statistics…)? here is a code snippet to demonstrate this for mean intensity</p>
<pre><code>for segmentationNode in slicer.util.getNodesByClass('vtkMRMLSegmentationNode'):
    segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
    segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.mean.enabled", str(True)) 
    segStatLogic.computeStatistics()
    stats = segStatLogic.getStatistics()
    for segmentId in stats['SegmentIDs']:
        mean = np.array(stats[segmentId,"ScalarVolumeSegmentStatisticsPlugin.mean"])
        print(mean)
</code></pre>
<p>Andinet</p>

---

## Post #8 by @Maxnach (2021-03-09 20:51 UTC)

<p>Dear Andinet,</p>
<p>Many thanks for your suggestion, I’m a proper beginner and maybe I did it wrong, but here is the outcome in the python command prompt :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9043d547c5c62ac604c5d8efed676c03a2fdf316.png" data-download-href="/uploads/short-url/kAe5qx4NUDNwbPOIsbRsOwjnrrE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9043d547c5c62ac604c5d8efed676c03a2fdf316.png" alt="image" data-base62-sha1="kAe5qx4NUDNwbPOIsbRsOwjnrrE" width="690" height="430" data-dominant-color="FCF9FC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1102×687 18.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, maybe that could help, I read a bit since your mentionned MRML and it seems indeed that every segmentation has its MRML ref, however the labelling (numbers) does not make any sense to me :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0c8b738c670e3e2a8ddb9a4c5c688efc247fdcb.png" data-download-href="/uploads/short-url/rvrHKUp8te6emI7elsNpY4awaBd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0c8b738c670e3e2a8ddb9a4c5c688efc247fdcb.png" alt="image" data-base62-sha1="rvrHKUp8te6emI7elsNpY4awaBd" width="144" height="500" data-dominant-color="E5E8E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">223×774 18.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The magical solution would be some script that measures the segment.stat from the MRML-ref segmentation/scalar volume and could “match” it with DICOM name/date… which I guess is what you did with this code snippet… but tried everything cannot launch it properly… any ideas where I could have go wrong ?</p>
<p>Many thanks in advance, I feel a solution is not far but my 0 background in coding is probably hiding it <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @Andinet_Enquobahrie (2021-03-09 22:06 UTC)

<p>Here is a little bit of a more complete code snippet</p>
<pre><code class="lang-auto">import SegmentStatistics
import numpy as np

segStatLogic = SegmentStatistics.SegmentStatisticsLogic()

#Scalar Volume MRML Node List ( You will need this to generate image intensity statistics )
scalarVolumeNode = slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode')

#WARNING: Assuming all segmentations were done on the same master volume, in this case the first one
segStatLogic.getParameterNode().SetParameter("ScalarVolume", scalarVolumeNode[0].GetID())
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.mean.enabled", str(True))

for segmentationNode in slicer.util.getNodesByClass('vtkMRMLSegmentationNode'):
    print(segmentationNode.GetID())
    segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
    segStatLogic.computeStatistics()
    stats = segStatLogic.getStatistics()
    for segmentId in stats['SegmentIDs']:
        mean = np.array(stats[segmentId,"ScalarVolumeSegmentStatisticsPlugin.mean"])
        print(mean)

</code></pre>
<p>Andinet</p>

---

## Post #10 by @Maxnach (2021-03-09 22:16 UTC)

<p>Thank you so much, it seems it loader the segmentation, but there were an error at some point. Of note, each master volume has its own segmentation (actually each master volume = 1 slice of 1 patient at 1 time point)</p>
<p>import SegmentStatistics</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>import numpy as np</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>segStatLogic = SegmentStatistics.SegmentStatisticsLogic()</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p><span class="hashtag-raw">#Scalar</span> Volume MRML Node List ( You will need this to generate image intensity statistics )</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>scalarVolumeNode = slicer.util.getNodesByClass(‘vtkMRMLScalarVolumeNode’)</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p><span class="hashtag-raw">#WARNING:</span> Assuming all segmentations were done on the same master volume, in this case the first one</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>segStatLogic.getParameterNode().SetParameter(“ScalarVolume”, scalarVolumeNode[0].GetID())</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>segStatLogic.getParameterNode().SetParameter(“ScalarVolumeSegmentStatisticsPlugin.mean.enabled”, str(True))</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>for segmentationNode in slicer.util.getNodesByClass(‘vtkMRMLSegmentationNode’):</p>
</blockquote>
</blockquote>
</blockquote>
<p>…</p>
<p>… print(segmentationNode.GetID())</p>
<p>…</p>
<p>vtkMRMLSegmentationNode10</p>
<p>vtkMRMLSegmentationNode11</p>
<p>vtkMRMLSegmentationNode12</p>
<p>vtkMRMLSegmentationNode13</p>
<p>vtkMRMLSegmentationNode14</p>
<p>vtkMRMLSegmentationNode15</p>
<p>vtkMRMLSegmentationNode16</p>
<p>vtkMRMLSegmentationNode17</p>
<p>vtkMRMLSegmentationNode18</p>
<p>vtkMRMLSegmentationNode19</p>
<p>vtkMRMLSegmentationNode20</p>
<p>vtkMRMLSegmentationNode21</p>
<p>vtkMRMLSegmentationNode22</p>
<p>vtkMRMLSegmentationNode23</p>
<p>vtkMRMLSegmentationNode24</p>
<p>vtkMRMLSegmentationNode25</p>
<p>vtkMRMLSegmentationNode26</p>
<p>vtkMRMLSegmentationNode27</p>
<p>vtkMRMLSegmentationNode28</p>
<p>vtkMRMLSegmentationNode29</p>
<p>vtkMRMLSegmentationNode30</p>
<p>vtkMRMLSegmentationNode31</p>
<p>vtkMRMLSegmentationNode32</p>
<p>vtkMRMLSegmentationNode33</p>
<p>vtkMRMLSegmentationNode34</p>
<p>vtkMRMLSegmentationNode35</p>
<p>vtkMRMLSegmentationNode36</p>
<p>vtkMRMLSegmentationNode37</p>
<p>vtkMRMLSegmentationNode38</p>
<p>vtkMRMLSegmentationNode39</p>
<p>vtkMRMLSegmentationNode40</p>
<p>vtkMRMLSegmentationNode41</p>
<p>vtkMRMLSegmentationNode42</p>
<p>vtkMRMLSegmentationNode43</p>
<p>vtkMRMLSegmentationNode44</p>
<p>vtkMRMLSegmentationNode45</p>
<p>vtkMRMLSegmentationNode46</p>
<p>vtkMRMLSegmentationNode47</p>
<p>vtkMRMLSegmentationNode48</p>
<p>vtkMRMLSegmentationNode49</p>
<p>vtkMRMLSegmentationNode50</p>
<p>vtkMRMLSegmentationNode51</p>
<p>vtkMRMLSegmentationNode52</p>
<p>vtkMRMLSegmentationNode53</p>
<p>vtkMRMLSegmentationNode54</p>
<p>vtkMRMLSegmentationNode55</p>
<p>vtkMRMLSegmentationNode56</p>
<p>vtkMRMLSegmentationNode57</p>
<p>vtkMRMLSegmentationNode58</p>
<p>vtkMRMLSegmentationNode59</p>
<p>vtkMRMLSegmentationNode60</p>
<p>vtkMRMLSegmentationNode61</p>
<p>vtkMRMLSegmentationNode62</p>
<p>vtkMRMLSegmentationNode63</p>
<p>vtkMRMLSegmentationNode64</p>
<p>vtkMRMLSegmentationNode65</p>
<p>vtkMRMLSegmentationNode66</p>
<p>vtkMRMLSegmentationNode67</p>
<p>vtkMRMLSegmentationNode68</p>
<p>vtkMRMLSegmentationNode69</p>
<p>vtkMRMLSegmentationNode70</p>
<p>vtkMRMLSegmentationNode71</p>
<p>vtkMRMLSegmentationNode72</p>
<p>vtkMRMLSegmentationNode73</p>
<p>vtkMRMLSegmentationNode74</p>
<p>vtkMRMLSegmentationNode75</p>
<p>vtkMRMLSegmentationNode76</p>
<p>vtkMRMLSegmentationNode77</p>
<p>vtkMRMLSegmentationNode78</p>
<p>vtkMRMLSegmentationNode79</p>
<p>vtkMRMLSegmentationNode80</p>
<p>vtkMRMLSegmentationNode81</p>
<p>vtkMRMLSegmentationNode82</p>
<p>vtkMRMLSegmentationNode83</p>
<p>vtkMRMLSegmentationNode84</p>
<p>vtkMRMLSegmentationNode85</p>
<p>vtkMRMLSegmentationNode86</p>
<p>vtkMRMLSegmentationNode87</p>
<p>vtkMRMLSegmentationNode88</p>
<p>vtkMRMLSegmentationNode89</p>
<p>vtkMRMLSegmentationNode90</p>
<p>vtkMRMLSegmentationNode91</p>
<p>vtkMRMLSegmentationNode92</p>
<p>vtkMRMLSegmentationNode93</p>
<p>vtkMRMLSegmentationNode94</p>
<p>vtkMRMLSegmentationNode95</p>
<p>vtkMRMLSegmentationNode96</p>
<p>vtkMRMLSegmentationNode97</p>
<p>vtkMRMLSegmentationNode98</p>
<p>vtkMRMLSegmentationNode99</p>
<p>vtkMRMLSegmentationNode100</p>
<p>vtkMRMLSegmentationNode101</p>
<p>vtkMRMLSegmentationNode102</p>
<p>vtkMRMLSegmentationNode103</p>
<p>vtkMRMLSegmentationNode104</p>
<p>vtkMRMLSegmentationNode105</p>
<p>vtkMRMLSegmentationNode106</p>
<p>vtkMRMLSegmentationNode107</p>
<p>vtkMRMLSegmentationNode108</p>
<p>vtkMRMLSegmentationNode109</p>
<p>vtkMRMLSegmentationNode110</p>
<p>vtkMRMLSegmentationNode111</p>
<p>vtkMRMLSegmentationNode112</p>
<p>vtkMRMLSegmentationNode113</p>
<p>vtkMRMLSegmentationNode114</p>
<p>vtkMRMLSegmentationNode115</p>
<p>vtkMRMLSegmentationNode116</p>
<p>vtkMRMLSegmentationNode117</p>
<p>vtkMRMLSegmentationNode118</p>
<p>vtkMRMLSegmentationNode119</p>
<p>vtkMRMLSegmentationNode120</p>
<p>vtkMRMLSegmentationNode121</p>
<p>vtkMRMLSegmentationNode122</p>
<p>vtkMRMLSegmentationNode123</p>
<p>vtkMRMLSegmentationNode124</p>
<p>vtkMRMLSegmentationNode125</p>
<p>vtkMRMLSegmentationNode126</p>
<p>vtkMRMLSegmentationNode127</p>
<p>vtkMRMLSegmentationNode128</p>
<p>vtkMRMLSegmentationNode129</p>
<p>vtkMRMLSegmentationNode130</p>
<p>vtkMRMLSegmentationNode131</p>
<p>vtkMRMLSegmentationNode132</p>
<p>vtkMRMLSegmentationNode133</p>
<p>vtkMRMLSegmentationNode134</p>
<p>vtkMRMLSegmentationNode135</p>
<p>vtkMRMLSegmentationNode136</p>
<p>vtkMRMLSegmentationNode137</p>
<p>vtkMRMLSegmentationNode138</p>
<p>vtkMRMLSegmentationNode139</p>
<p>vtkMRMLSegmentationNode140</p>
<p>vtkMRMLSegmentationNode141</p>
<p>vtkMRMLSegmentationNode142</p>
<p>vtkMRMLSegmentationNode143</p>
<p>vtkMRMLSegmentationNode144</p>
<p>vtkMRMLSegmentationNode145</p>
<p>vtkMRMLSegmentationNode146</p>
<p>vtkMRMLSegmentationNode147</p>
<p>vtkMRMLSegmentationNode148</p>
<p>vtkMRMLSegmentationNode149</p>
<p>vtkMRMLSegmentationNode150</p>
<p>vtkMRMLSegmentationNode151</p>
<p>vtkMRMLSegmentationNode152</p>
<p>vtkMRMLSegmentationNode153</p>
<p>vtkMRMLSegmentationNode154</p>
<p>vtkMRMLSegmentationNode155</p>
<p>vtkMRMLSegmentationNode156</p>
<p>vtkMRMLSegmentationNode157</p>
<p>vtkMRMLSegmentationNode158</p>
<p>vtkMRMLSegmentationNode159</p>
<p>vtkMRMLSegmentationNode160</p>
<p>vtkMRMLSegmentationNode161</p>
<p>vtkMRMLSegmentationNode162</p>
<p>vtkMRMLSegmentationNode163</p>
<p>vtkMRMLSegmentationNode164</p>
<p>vtkMRMLSegmentationNode165</p>
<p>vtkMRMLSegmentationNode166</p>
<p>vtkMRMLSegmentationNode167</p>
<p>vtkMRMLSegmentationNode168</p>
<p>vtkMRMLSegmentationNode169</p>
<p>vtkMRMLSegmentationNode170</p>
<p>vtkMRMLSegmentationNode171</p>
<p>vtkMRMLSegmentationNode172</p>
<p>vtkMRMLSegmentationNode173</p>
<p>vtkMRMLSegmentationNode174</p>
<p>vtkMRMLSegmentationNode175</p>
<p>vtkMRMLSegmentationNode176</p>
<p>vtkMRMLSegmentationNode177</p>
<p>vtkMRMLSegmentationNode178</p>
<p>vtkMRMLSegmentationNode179</p>
<p>vtkMRMLSegmentationNode180</p>
<p>vtkMRMLSegmentationNode181</p>
<blockquote>
<blockquote>
<blockquote>
<p>segStatLogic.getParameterNode().SetParameter(“Segmentation”, segmentationNode.GetID())</p>
</blockquote>
</blockquote>
</blockquote>
<p>File “”, line 1</p>
<p>segStatLogic.getParameterNode().SetParameter(“Segmentation”, segmentationNode.GetID())</p>
<p>^</p>
<p>IndentationError: unexpected indent</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>segStatLogic.computeStatistics()</p>
</blockquote>
</blockquote>
</blockquote>
<p>File “”, line 1</p>
<p>segStatLogic.computeStatistics()</p>
<p>^</p>
<p>IndentationError: unexpected indent</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>stats = segStatLogic.getStatistics()</p>
</blockquote>
</blockquote>
</blockquote>
<p>File “”, line 1</p>
<p>stats = segStatLogic.getStatistics()</p>
<p>^</p>
<p>IndentationError: unexpected indent</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>for segmentId in stats[‘SegmentIDs’]:</p>
</blockquote>
</blockquote>
</blockquote>
<p>File “”, line 1</p>
<p>for segmentId in stats[‘SegmentIDs’]:</p>
<p>^</p>
<p>IndentationError: unexpected indent</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>mean = np.array(stats[segmentId,“ScalarVolumeSegmentStatisticsPlugin.mean”])</p>
</blockquote>
</blockquote>
</blockquote>
<p>File “”, line 1</p>
<p>mean = np.array(stats[segmentId,“ScalarVolumeSegmentStatisticsPlugin.mean”])</p>
<p>^</p>
<p>IndentationError: unexpected indent</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>print(mean)</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #11 by @lassoan (2021-04-06 13:27 UTC)

<p>Python is very sensitive to indentation.</p>
<p>Indentation error is most likely due to how you copy-paste the code into the console (extra line breaks may interfere with the parser). Copy-pasting the code in smaller chunks or putting the code into a Python scripted module should fix the issue.</p>

---

## Post #12 by @Maxnach (2021-05-01 19:00 UTC)

<p>Thank you for that input, I’ve been trying for weeks to make it work without success, I’m on the edge to give up… Basically when I enter the script, here is the output :</p>
<pre><code>vtkMRMLSegmentationNode10

vtkMRMLSegmentationNode11

vtkMRMLSegmentationNode12

-496.58272879464283

vtkMRMLSegmentationNode13

-74.15475789615462

vtkMRMLSegmentationNode14

vtkMRMLSegmentationNode15

vtkMRMLSegmentationNode16

vtkMRMLSegmentationNode17

vtkMRMLSegmentationNode18

vtkMRMLSegmentationNode19

vtkMRMLSegmentationNode20

-1024.0

vtkMRMLSegmentationNode21

vtkMRMLSegmentationNode22

vtkMRMLSegmentationNode23

vtkMRMLSegmentationNode24

vtkMRMLSegmentationNode25

-462.4361410918192

vtkMRMLSegmentationNode26

-256.5129649980126

vtkMRMLSegmentationNode27

-227.99324965434977

vtkMRMLSegmentationNode28

vtkMRMLSegmentationNode29

vtkMRMLSegmentationNode30

vtkMRMLSegmentationNode31

-316.79681233215916

vtkMRMLSegmentationNode32

-137.02753698998654

vtkMRMLSegmentationNode33

vtkMRMLSegmentationNode34

vtkMRMLSegmentationNode35

vtkMRMLSegmentationNode36

-215.98637721279232

vtkMRMLSegmentationNode37

vtkMRMLSegmentationNode38

vtkMRMLSegmentationNode39

vtkMRMLSegmentationNode40

vtkMRMLSegmentationNode41

-254.12470667113644

vtkMRMLSegmentationNode42

vtkMRMLSegmentationNode43

vtkMRMLSegmentationNode44

vtkMRMLSegmentationNode45

30.2841052299937

vtkMRMLSegmentationNode46

vtkMRMLSegmentationNode47

vtkMRMLSegmentationNode48

vtkMRMLSegmentationNode49

vtkMRMLSegmentationNode50

vtkMRMLSegmentationNode51

vtkMRMLSegmentationNode52

vtkMRMLSegmentationNode53

-1024.0

vtkMRMLSegmentationNode54

vtkMRMLSegmentationNode55

vtkMRMLSegmentationNode56

vtkMRMLSegmentationNode57

vtkMRMLSegmentationNode58

-1024.0

vtkMRMLSegmentationNode59

vtkMRMLSegmentationNode60

-1024.0

vtkMRMLSegmentationNode61

vtkMRMLSegmentationNode62

14.96579391891892

vtkMRMLSegmentationNode63

vtkMRMLSegmentationNode64

vtkMRMLSegmentationNode65

vtkMRMLSegmentationNode66

vtkMRMLSegmentationNode67

vtkMRMLSegmentationNode68

vtkMRMLSegmentationNode69

vtkMRMLSegmentationNode70

vtkMRMLSegmentationNode71

vtkMRMLSegmentationNode72

vtkMRMLSegmentationNode73

vtkMRMLSegmentationNode74

vtkMRMLSegmentationNode75

-128.97017045454547

vtkMRMLSegmentationNode76

vtkMRMLSegmentationNode77

vtkMRMLSegmentationNode78

vtkMRMLSegmentationNode79

vtkMRMLSegmentationNode80

vtkMRMLSegmentationNode81

vtkMRMLSegmentationNode82

vtkMRMLSegmentationNode83

vtkMRMLSegmentationNode84

vtkMRMLSegmentationNode85

vtkMRMLSegmentationNode86

vtkMRMLSegmentationNode87

vtkMRMLSegmentationNode88

vtkMRMLSegmentationNode89

vtkMRMLSegmentationNode90

vtkMRMLSegmentationNode91

vtkMRMLSegmentationNode92

vtkMRMLSegmentationNode93

vtkMRMLSegmentationNode94

vtkMRMLSegmentationNode95

vtkMRMLSegmentationNode96

vtkMRMLSegmentationNode97

vtkMRMLSegmentationNode98

vtkMRMLSegmentationNode99

vtkMRMLSegmentationNode100

vtkMRMLSegmentationNode101

vtkMRMLSegmentationNode102

vtkMRMLSegmentationNode103

vtkMRMLSegmentationNode104

vtkMRMLSegmentationNode105

vtkMRMLSegmentationNode106

vtkMRMLSegmentationNode107

vtkMRMLSegmentationNode108

vtkMRMLSegmentationNode109

vtkMRMLSegmentationNode110

vtkMRMLSegmentationNode111

vtkMRMLSegmentationNode112

vtkMRMLSegmentationNode113

vtkMRMLSegmentationNode114

vtkMRMLSegmentationNode115

-1024.0

vtkMRMLSegmentationNode116

vtkMRMLSegmentationNode117

vtkMRMLSegmentationNode118

vtkMRMLSegmentationNode119

vtkMRMLSegmentationNode120

vtkMRMLSegmentationNode121

vtkMRMLSegmentationNode122

vtkMRMLSegmentationNode123

vtkMRMLSegmentationNode124

vtkMRMLSegmentationNode125

vtkMRMLSegmentationNode126

vtkMRMLSegmentationNode127

vtkMRMLSegmentationNode128

vtkMRMLSegmentationNode129

vtkMRMLSegmentationNode130

vtkMRMLSegmentationNode131

vtkMRMLSegmentationNode132

vtkMRMLSegmentationNode133

vtkMRMLSegmentationNode134

vtkMRMLSegmentationNode135

vtkMRMLSegmentationNode136

vtkMRMLSegmentationNode137

vtkMRMLSegmentationNode138

vtkMRMLSegmentationNode139

vtkMRMLSegmentationNode140

-505.8226897069872

vtkMRMLSegmentationNode141

vtkMRMLSegmentationNode142

vtkMRMLSegmentationNode143

vtkMRMLSegmentationNode144

vtkMRMLSegmentationNode145

vtkMRMLSegmentationNode146

vtkMRMLSegmentationNode147

45.87743054397492

vtkMRMLSegmentationNode148

vtkMRMLSegmentationNode149

vtkMRMLSegmentationNode150

vtkMRMLSegmentationNode151

vtkMRMLSegmentationNode152

vtkMRMLSegmentationNode153

vtkMRMLSegmentationNode154

vtkMRMLSegmentationNode155

vtkMRMLSegmentationNode156

vtkMRMLSegmentationNode157

vtkMRMLSegmentationNode158

vtkMRMLSegmentationNode159

vtkMRMLSegmentationNode160

vtkMRMLSegmentationNode161

vtkMRMLSegmentationNode162

vtkMRMLSegmentationNode163

vtkMRMLSegmentationNode164

vtkMRMLSegmentationNode165

vtkMRMLSegmentationNode166

vtkMRMLSegmentationNode167

vtkMRMLSegmentationNode168

vtkMRMLSegmentationNode169

vtkMRMLSegmentationNode170

vtkMRMLSegmentationNode171

vtkMRMLSegmentationNode172

vtkMRMLSegmentationNode173

vtkMRMLSegmentationNode174

-305.12905001376066

vtkMRMLSegmentationNode175

vtkMRMLSegmentationNode176

vtkMRMLSegmentationNode177

vtkMRMLSegmentationNode178

vtkMRMLSegmentationNode179

vtkMRMLSegmentationNode180

vtkMRMLSegmentationNode181
</code></pre>
<p>No results anywhere except some random number in between some lines.</p>
<p>I am just getting crazy. I have around 70 patients, each one has 2 to 3 slice (DICOM format), corresponding to different timepoints.</p>
<p>My problems are the following :</p>
<ul>
<li>
<p>The DICOM file is named ideally for me (in the directory folder) e.g. “Patientsname-T0” (with either T0, T1 or T2 to denote the timepoint). However, when I performed measurements, patients are well recognized (name ect. from the dicom), but the slice on 3Dslicer is not named like I did : it is name with acquisition parameters (like “Abdomen i_dose”) which are generic names. Hence, seen the number of patients, slice are names completely randomly (Abdomen i_dose, Abdomen i_dose(1), Abdomen i_dose(2), etc;).</p>
</li>
<li>
<p>The segmentation nodes are also names completely randomly, even though I can manually see which segmentation node is connected with which image :</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0c8b738c670e3e2a8ddb9a4c5c688efc247fdcb.png" data-download-href="/uploads/short-url/rvrHKUp8te6emI7elsNpY4awaBd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0c8b738c670e3e2a8ddb9a4c5c688efc247fdcb.png" alt="image" data-base62-sha1="rvrHKUp8te6emI7elsNpY4awaBd" width="144" height="500" data-dominant-color="E5E8E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">223×774 18.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(The name of the patients is on the left of that column)</p>
<p>Therefore, it’s a nightmare for me as I don’t have any idea of where are the radiomics features corresponding to those segmentation nodes. And even if I did, I’d still have to cross-link manually every segmentation nodes to every patients images (i.e. abdomne i_dose (1) ect.) and finally link those random names to the actual dicom file name.</p>
<p>I have no clue what to do… would anyone help?</p>
<p>Edit: to make it more complicated, I’m actually trying to apply the pyradiomic pipleline on those images…</p>

---

## Post #13 by @jamesobutler (2021-05-01 20:46 UTC)

<p>HI <a class="mention" href="/u/maxnach">@Maxnach</a>, have you tried using the Slicer GUI to load in a single patient volume and segmentation and use the SegmentStatistics module to generate the statistics you are looking for?</p>
<p>It is helpful to think about the individual case in GUI to help guide the python scripting. Once you have successfully completed what you want for one individual case, then you can begin thinking about how you would do this in a repeated manner.</p>

---
