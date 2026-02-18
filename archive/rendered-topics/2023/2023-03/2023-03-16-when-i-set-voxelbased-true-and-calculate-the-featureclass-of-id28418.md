# When I set voxelBased=True and calculate the featureclass of glcm,I meet some problems

**Topic ID**: 28418
**Date**: 2023-03-16
**URL**: https://discourse.slicer.org/t/when-i-set-voxelbased-true-and-calculate-the-featureclass-of-glcm-i-meet-some-problems/28418

---

## Post #1 by @duckfen (2023-03-16 13:28 UTC)

<pre><code class="lang-auto">code:
extractor = featureextractor.RadiomicsFeatureExtractor('.yaml')
result = extractor.execute(image, mask, voxelBased=True)
for key, val in six.iteritems(result):
    if isinstance(val, sitk.Image):
        shape = (sitk.GetArrayFromImage(val)).shape
        print('feature_map shape is ', shape)
        sitk.WriteImage(val,r'C:\Users\feature'+'/'+key+'.nrrd', True)
yaml:
imageType:
    Wavelet: { } }
featureClass:
     glcm: ['ClusterProminence']
setting:
    binWidth: 40
</code></pre>
<p>I am currently working on radiomic feature extraction using voxel-based analysis with the parameter voxel-base=True. When I attempt to calculate features such as gldm and firstorder, everything runs smoothly. However, when I try to calculate the glcm feature, I encounter an error.</p>
<p>When I set the binWidth to a larger value, the program doesn’t output anything, and PyCharm displays the message “Process finished with exit code -1073741819 (0xC0000005).” Conversely, when I set the binWidth to a smaller value, I receive a MemoryError.</p>
<p>I’m wondering if this issue might be due to my computer’s limited memory (16GB). The size of my original image is 170<em>88</em>170, and the size of the tumor mask is 42<em>40</em>45.</p>
<p>Can anyone help me troubleshoot this problem and suggest a potential solution? Thank you in advance for your assistance!</p>

---
