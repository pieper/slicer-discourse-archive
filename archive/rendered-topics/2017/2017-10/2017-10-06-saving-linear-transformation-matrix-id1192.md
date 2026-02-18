# Saving Linear Transformation Matrix

**Topic ID**: 1192
**Date**: 2017-10-06
**URL**: https://discourse.slicer.org/t/saving-linear-transformation-matrix/1192

---

## Post #1 by @Anna_Morelli (2017-10-06 15:21 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.6.2<br>
Expected behavior: Matrix in ijk coordinates<br>
Actual behavior: Matrix in unknown reference system</p>
<p>Hi guys,<br>
I’m a beginner in Slicer and I’m in trouble saving the transformation matrix. I obtained this matrix with the Fiducial registration module and is expressed w.r.t. RAS reference system, I think. When I save it in other formats, such as .h5 or .txt or .mat, the values are different. I think that automatically the reference frame w.r.t. it is expressed has changed; is it based of IJK or LPS frames?<br>
Thanks</p>

---

## Post #2 by @lassoan (2017-10-07 04:53 UTC)

<p>I think this topic should answer your questions: <a href="https://discourse.slicer.org/t/displayed-transform-vs-tfm-content/270">Displayed transform vs .tfm content</a></p>

---

## Post #3 by @Anna_Morelli (2017-10-07 14:52 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your answer. Yes, the question is the same, but I’m sorry I didn’t understand what I  should do to obtain the transformation matrix in xyz coordinates.</p>

---

## Post #4 by @lassoan (2017-10-07 16:24 UTC)

<p>What anatomical axes your xyz axes correspond to: LPS or RAS?</p>

---

## Post #5 by @lassoan (2017-10-07 16:25 UTC)

<p>Do you process your images in Matlab?</p>

---

## Post #6 by @Anna_Morelli (2017-10-12 13:05 UTC)

<p>Maybe I was not clear in the question, I’m sorry but I was a little bit confused.<br>
I didn’t understand how to deal with the matrix in the txt file, so w.r.t. LPS axes (e.g.I have to do its inverse, to pre or post multiply it for a certain matrix ,…) to obtain the matrix that appears in Slicer. How is it possible?<br>
Then I suppose that applying this matrix to my moving dataset, e.g. I can apply it using Matlab, I can obtain the same results that I obtained applying the tranformation matrix in Slicer and saving the result.<br>
If I’m not clear, please let me know.</p>

---

## Post #7 by @lassoan (2017-10-12 14:32 UTC)

<p>Here is the conversion done by Slicer’s MatlabBridge extension:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/f7d4511ffe9424e827362942beccb29c7007b526/MatlabCommander/commandserver/cli_lineartransformread.m#L25-L30" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/f7d4511ffe9424e827362942beccb29c7007b526/MatlabCommander/commandserver/cli_lineartransformread.m#L25-L30" target="_blank" rel="nofollow noopener">PerkLab/SlicerMatlabBridge/blob/f7d4511ffe9424e827362942beccb29c7007b526/MatlabCommander/commandserver/cli_lineartransformread.m#L25-L30</a></h4>
<pre class="onebox"><code class="lang-m"><ol class="start lines" start="25" style="counter-reset: li-counter 24 ;">
<li>if (strcmpi(transformType,'itk'))</li>
<li>transform=transform_lps;    </li>
<li>elseif (strcmpi(transformType, 'slicer'))</li>
<li>lps2ras=diag([-1 -1 1 1]);</li>
<li>ras2lps=diag([-1 -1 1 1]);</li>
<li>transform=lps2ras*inv(transform_lps)*ras2lps;  </li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If you need the values that are displayed in Slicer, use the computation in the ‘slicer’ branch.</p>
<p>Note that Slicer’s MatlabBridge extension allows you to run Matlab functions directly from the Slicer GUI. So, if you are forced to use Matlab for certain processing, you can still do that, while keeping the GUI and rest of your workflow in Slicer/Python. See more information about the MatlabBridge extension here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge</a></p>

---

## Post #8 by @park (2022-01-12 02:35 UTC)

<p>This is full python code to get the transform matix same in Slicer</p>
<p>The important thing in python<br>
We can not use</p>
<p><code>transfrom_itk = np.reshape(transform_raw, (3,4))</code><br>
or<br>
<code>transfrom_itk = np.reshape(transform_raw, (3,4), order='F')</code></p>
<pre><code class="lang-auto">reader = pd.read_table("Your path\\LinearTransform_3.txt", header=None)
transform_raw = np.array(list(map(float, reader[0][3].split(':')[-1].split(' ')[1:])))

transform_itk  = np.zeros((4,4))
transform_itk[:3,:3] = np.reshape(transform_raw [:9], (3, 3))
transform_itk[:3, 3] = transform_raw [9:12]
transform_itk[3,3] = 1

lps2ras = np.diag([-1, - 1, 1, 1])
ras2lps = np.diag([-1, - 1, 1, 1])
transform_slicer = lps2ras @ np.linalg.inv(transform_itk) @ ras2lps
</code></pre>

---
