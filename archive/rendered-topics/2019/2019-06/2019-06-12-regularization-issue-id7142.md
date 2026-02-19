---
topic_id: 7142
title: "Regularization Issue"
date: 2019-06-12
url: https://discourse.slicer.org/t/7142
---

# Regularization issue

**Topic ID**: 7142
**Date**: 2019-06-12
**URL**: https://discourse.slicer.org/t/regularization-issue/7142

---

## Post #1 by @Jragher (2019-06-12 17:30 UTC)

<p>HI Slice Community,</p>
<p>I have been struggling for certain amount of time regarding what I have understand to be regularization.</p>
<p>I have a MRI of different areas encapsulated in one acquisition.<br>
I just would like to have “blank” slices in the coordinate where there is no acquisition. With regularization activated, there is no distorsion but Slicer make weird stuff between the areas.</p>
<p>I Watch the image information and there were issues with th order. For example n°5 slice beiing in fact n°4 when regarding the coordinate. I changed all names but didn’t make any difference. I guess slice already made the correction.</p>
<p>You will find informations below.</p>
<p>Thanks very much for your help</p>
<p>JR</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5d7bbd4a1f7b26d566b0096e7d0da0325d1b9bd.png" alt="image" data-base62-sha1="wNhxYPfhTg6hSpVYIdrBffC9Bjn" width="197" height="110"></p>
<div class="md-table">
<table>
<thead>
<tr>
<th>M0001</th>
<th>ImagePositionPatient</th>
<th>[3] -150.300, -100.000, 21.000</th>
</tr>
</thead>
<tbody>
<tr>
<td>M0002</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, 18.500</td>
</tr>
<tr>
<td>0003-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, 16.000</td>
</tr>
<tr>
<td>M0004</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, 13.500</td>
</tr>
<tr>
<td>0005-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, 11.000</td>
</tr>
<tr>
<td>0006-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, 8.500</td>
</tr>
<tr>
<td>0007-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, 6.000</td>
</tr>
<tr>
<td>0008-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, 3.500</td>
</tr>
<tr>
<td>M0009</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, 1.000</td>
</tr>
<tr>
<td>M0010</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -1.500</td>
</tr>
<tr>
<td>M0011</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -4.000</td>
</tr>
<tr>
<td>M0012</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -6.500</td>
</tr>
<tr>
<td>0013-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -9.000</td>
</tr>
<tr>
<td>0014-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -11.500</td>
</tr>
<tr>
<td>0015-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -14.000</td>
</tr>
<tr>
<td>M0016</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -16.500</td>
</tr>
<tr>
<td>M0017</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -19.000</td>
</tr>
<tr>
<td>M0018</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -21.500</td>
</tr>
<tr>
<td>M0019</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -24.000</td>
</tr>
<tr>
<td>M0020</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -26.500</td>
</tr>
<tr>
<td>M0021</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -29.000</td>
</tr>
<tr>
<td>M0022</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -31.500</td>
</tr>
<tr>
<td>0023-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -34.000</td>
</tr>
<tr>
<td>0024-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -36.500</td>
</tr>
<tr>
<td>M0025</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -39.000</td>
</tr>
<tr>
<td>M0026</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -41.500</td>
</tr>
<tr>
<td>M0027</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -44.000</td>
</tr>
<tr>
<td>M0028</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -46.500</td>
</tr>
<tr>
<td>M0029</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -49.000</td>
</tr>
<tr>
<td>M0030</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -51.500</td>
</tr>
<tr>
<td>M0031</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -54.000</td>
</tr>
<tr>
<td>0032-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -56.500</td>
</tr>
<tr>
<td>0033-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -59.000</td>
</tr>
<tr>
<td>0034-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -61.500</td>
</tr>
<tr>
<td>0035-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -64.000</td>
</tr>
<tr>
<td>M0036</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -66.500</td>
</tr>
<tr>
<td>M0037</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -69.000</td>
</tr>
<tr>
<td>M0038</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -71.500</td>
</tr>
<tr>
<td>M0039</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -74.000</td>
</tr>
<tr>
<td>M0040</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -76.500</td>
</tr>
<tr>
<td>M0041</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -79.000</td>
</tr>
<tr>
<td>0042-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -81.500</td>
</tr>
<tr>
<td>0043-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -84.000</td>
</tr>
<tr>
<td>0044-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -86.500</td>
</tr>
<tr>
<td>M0045</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -89.000</td>
</tr>
<tr>
<td>M0046</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -91.500</td>
</tr>
<tr>
<td>M0047</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -383.250</td>
</tr>
<tr>
<td>M0048</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -383.875</td>
</tr>
<tr>
<td>M0049</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -384.500</td>
</tr>
<tr>
<td>M0050</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -385.125</td>
</tr>
<tr>
<td>M0051</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -385.750</td>
</tr>
<tr>
<td>0052-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -386.375</td>
</tr>
<tr>
<td>0053-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -387.000</td>
</tr>
<tr>
<td>0054-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -387.625</td>
</tr>
<tr>
<td>M0055</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -388.250</td>
</tr>
<tr>
<td>M0056</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -388.875</td>
</tr>
<tr>
<td>M0057</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -389.500</td>
</tr>
<tr>
<td>M0058</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -390.125</td>
</tr>
<tr>
<td>M0059</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -390.750</td>
</tr>
<tr>
<td>M0060</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -391.375</td>
</tr>
<tr>
<td>0061-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -392.000</td>
</tr>
<tr>
<td>0062-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -392.625</td>
</tr>
<tr>
<td>M0063</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -393.250</td>
</tr>
<tr>
<td>M0064</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -393.875</td>
</tr>
<tr>
<td>M0065</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -394.500</td>
</tr>
<tr>
<td>M0066</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -395.125</td>
</tr>
<tr>
<td>M0067</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -395.750</td>
</tr>
<tr>
<td>M0068</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -396.375</td>
</tr>
<tr>
<td>M0069</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -397.000</td>
</tr>
<tr>
<td>M0070</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -397.625</td>
</tr>
<tr>
<td>0071-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -398.250</td>
</tr>
<tr>
<td>M0072</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -398.875</td>
</tr>
<tr>
<td>0073-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -399.500</td>
</tr>
<tr>
<td>M0074</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -400.125</td>
</tr>
<tr>
<td>M0075</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -400.750</td>
</tr>
<tr>
<td>M0076</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -401.375</td>
</tr>
<tr>
<td>M0077</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -402.000</td>
</tr>
<tr>
<td>M0078</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -402.625</td>
</tr>
<tr>
<td>M0079</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -403.250</td>
</tr>
<tr>
<td>M0080</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -403.875</td>
</tr>
<tr>
<td>0081-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -404.500</td>
</tr>
<tr>
<td>0082-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -405.125</td>
</tr>
<tr>
<td>0083-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -405.750</td>
</tr>
<tr>
<td>0084-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -406.375</td>
</tr>
<tr>
<td>0085-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -407.000</td>
</tr>
<tr>
<td>M0086</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -407.625</td>
</tr>
<tr>
<td>M0087</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -408.250</td>
</tr>
<tr>
<td>M0088</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -408.875</td>
</tr>
<tr>
<td>M0089</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -409.500</td>
</tr>
<tr>
<td>M0090</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -410.125</td>
</tr>
<tr>
<td>0091-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -410.750</td>
</tr>
<tr>
<td>0092-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -411.375</td>
</tr>
<tr>
<td>0093-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -412.000</td>
</tr>
<tr>
<td>0094-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -412.625</td>
</tr>
<tr>
<td>0095-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -413.250</td>
</tr>
<tr>
<td>M0096</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -413.875</td>
</tr>
<tr>
<td>M0097</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -414.500</td>
</tr>
<tr>
<td>M0098</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -415.125</td>
</tr>
<tr>
<td>M0099</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -415.750</td>
</tr>
<tr>
<td>0100-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -416.375</td>
</tr>
<tr>
<td>0101-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -417.000</td>
</tr>
<tr>
<td>M0102</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -417.625</td>
</tr>
<tr>
<td>0103-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -418.250</td>
</tr>
<tr>
<td>M0104</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -418.875</td>
</tr>
<tr>
<td>M0105</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -419.500</td>
</tr>
<tr>
<td>M0106</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -420.125</td>
</tr>
<tr>
<td>M0107</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -420.750</td>
</tr>
<tr>
<td>M0108</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -421.375</td>
</tr>
<tr>
<td>M0109</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -422.000</td>
</tr>
<tr>
<td>0110-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -422.625</td>
</tr>
<tr>
<td>0111-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -423.250</td>
</tr>
<tr>
<td>M0112</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -423.875</td>
</tr>
<tr>
<td>0113-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -424.500</td>
</tr>
<tr>
<td>0114-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -425.125</td>
</tr>
<tr>
<td>M0115</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -425.750</td>
</tr>
<tr>
<td>M0116</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -426.375</td>
</tr>
<tr>
<td>M0117</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -427.000</td>
</tr>
<tr>
<td>M0118</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -427.625</td>
</tr>
<tr>
<td>M0119</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -428.250</td>
</tr>
<tr>
<td>0120-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -428.875</td>
</tr>
<tr>
<td>0121-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -429.500</td>
</tr>
<tr>
<td>M0122</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -430.125</td>
</tr>
<tr>
<td>0123-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -430.750</td>
</tr>
<tr>
<td>M0124</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -431.375</td>
</tr>
<tr>
<td>0125-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -432.000</td>
</tr>
<tr>
<td>M0126</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -432.625</td>
</tr>
<tr>
<td>M0127</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -433.250</td>
</tr>
<tr>
<td>M0128</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -433.875</td>
</tr>
<tr>
<td>M0129</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -434.500</td>
</tr>
<tr>
<td>0130-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -435.125</td>
</tr>
<tr>
<td>0131-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -435.750</td>
</tr>
<tr>
<td>0132-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -436.375</td>
</tr>
<tr>
<td>0133-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -437.000</td>
</tr>
<tr>
<td>0134-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -437.625</td>
</tr>
<tr>
<td>M0135</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -438.250</td>
</tr>
<tr>
<td>M0136</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -438.875</td>
</tr>
<tr>
<td>M0137</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -439.500</td>
</tr>
<tr>
<td>M0138</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -440.125</td>
</tr>
<tr>
<td>M0139</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -440.750</td>
</tr>
<tr>
<td>0140-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -441.375</td>
</tr>
<tr>
<td>0141-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -442.000</td>
</tr>
<tr>
<td>M0142</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -442.625</td>
</tr>
<tr>
<td>M0143</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -443.250</td>
</tr>
<tr>
<td>M0144</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -443.875</td>
</tr>
<tr>
<td>M0145</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -444.500</td>
</tr>
<tr>
<td>M0146</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -445.125</td>
</tr>
<tr>
<td>M0147</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -445.750</td>
</tr>
<tr>
<td>M0148</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -446.375</td>
</tr>
<tr>
<td>M0149</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -447.000</td>
</tr>
<tr>
<td>0150-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -447.625</td>
</tr>
<tr>
<td>0151-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -448.250</td>
</tr>
<tr>
<td>0152-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -448.875</td>
</tr>
<tr>
<td>0153-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -449.500</td>
</tr>
<tr>
<td>0154-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -450.125</td>
</tr>
<tr>
<td>0155-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -450.750</td>
</tr>
<tr>
<td>M0156</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -451.375</td>
</tr>
<tr>
<td>M0157</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -452.000</td>
</tr>
<tr>
<td>M0158</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -452.625</td>
</tr>
<tr>
<td>M0159</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -453.250</td>
</tr>
<tr>
<td>0160-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -453.875</td>
</tr>
<tr>
<td>0161-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -454.500</td>
</tr>
<tr>
<td>0162-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -455.125</td>
</tr>
<tr>
<td>M0163</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -455.750</td>
</tr>
<tr>
<td>M0164</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -456.375</td>
</tr>
<tr>
<td>M0165</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -457.000</td>
</tr>
<tr>
<td>M0166</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -457.625</td>
</tr>
<tr>
<td>M0167</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -458.250</td>
</tr>
<tr>
<td>M0168</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -458.875</td>
</tr>
<tr>
<td>M0169</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -459.500</td>
</tr>
<tr>
<td>M0170</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -460.125</td>
</tr>
<tr>
<td>M0171</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -460.750</td>
</tr>
<tr>
<td>M0172</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -461.375</td>
</tr>
<tr>
<td>M0173</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -462.000</td>
</tr>
<tr>
<td>M0174</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -462.625</td>
</tr>
<tr>
<td>M0175</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -463.250</td>
</tr>
<tr>
<td>M0176</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -463.875</td>
</tr>
<tr>
<td>M0177</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -464.500</td>
</tr>
<tr>
<td>M0178</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -465.125</td>
</tr>
<tr>
<td>M0179</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -465.750</td>
</tr>
<tr>
<td>0180-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -466.375</td>
</tr>
<tr>
<td>0181-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -467.000</td>
</tr>
<tr>
<td>0182-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -467.625</td>
</tr>
<tr>
<td>0183-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -468.250</td>
</tr>
<tr>
<td>0184-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -468.875</td>
</tr>
<tr>
<td>M0185</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -469.500</td>
</tr>
<tr>
<td>M0186</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -470.125</td>
</tr>
<tr>
<td>M0187</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -470.750</td>
</tr>
<tr>
<td>M0188</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -471.375</td>
</tr>
<tr>
<td>M0189</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -472.000</td>
</tr>
<tr>
<td>0190-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -472.625</td>
</tr>
<tr>
<td>M0191</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -473.250</td>
</tr>
<tr>
<td>0192-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -473.875</td>
</tr>
<tr>
<td>0193-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -474.500</td>
</tr>
<tr>
<td>0194-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -475.125</td>
</tr>
<tr>
<td>0195-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -475.750</td>
</tr>
<tr>
<td>M0196</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -476.375</td>
</tr>
<tr>
<td>M0197</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -477.000</td>
</tr>
<tr>
<td>M0198</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -477.625</td>
</tr>
<tr>
<td>M0199</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -478.250</td>
</tr>
<tr>
<td>0200-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -478.875</td>
</tr>
<tr>
<td>0201-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -479.500</td>
</tr>
<tr>
<td>0202-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -480.125</td>
</tr>
<tr>
<td>M0203</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -480.750</td>
</tr>
<tr>
<td>0204-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -481.375</td>
</tr>
<tr>
<td>0205-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -482.000</td>
</tr>
<tr>
<td>M0206</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -482.625</td>
</tr>
<tr>
<td>M0207</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -483.250</td>
</tr>
<tr>
<td>M0208</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -483.875</td>
</tr>
<tr>
<td>M0209</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -484.500</td>
</tr>
<tr>
<td>0210-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -485.125</td>
</tr>
<tr>
<td>0211-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -485.750</td>
</tr>
<tr>
<td>0212-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -486.375</td>
</tr>
<tr>
<td>M0213</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -487.000</td>
</tr>
<tr>
<td>0214-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -487.625</td>
</tr>
<tr>
<td>0215-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -488.250</td>
</tr>
<tr>
<td>M0216</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -488.875</td>
</tr>
<tr>
<td>M0217</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -489.500</td>
</tr>
<tr>
<td>M0218</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -490.125</td>
</tr>
<tr>
<td>M0219</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -490.750</td>
</tr>
<tr>
<td>0220-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -491.375</td>
</tr>
<tr>
<td>0221-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -492.000</td>
</tr>
<tr>
<td>0222-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -492.625</td>
</tr>
<tr>
<td>0223-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -493.250</td>
</tr>
<tr>
<td>M0224</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -493.875</td>
</tr>
<tr>
<td>M0225</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -494.500</td>
</tr>
<tr>
<td>M0226</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -495.125</td>
</tr>
<tr>
<td>M0227</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -495.750</td>
</tr>
<tr>
<td>M0228</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -496.375</td>
</tr>
<tr>
<td>M0229</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -497.000</td>
</tr>
<tr>
<td>0230-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -497.625</td>
</tr>
<tr>
<td>0231-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -498.250</td>
</tr>
<tr>
<td>0232-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -498.875</td>
</tr>
<tr>
<td>0233-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -499.500</td>
</tr>
<tr>
<td>0234-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -500.125</td>
</tr>
<tr>
<td>0235-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -500.750</td>
</tr>
<tr>
<td>M0236</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -501.375</td>
</tr>
<tr>
<td>M0237</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -502.000</td>
</tr>
<tr>
<td>M0238</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -502.625</td>
</tr>
<tr>
<td>M0239</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -503.250</td>
</tr>
<tr>
<td>M0240</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -505.750</td>
</tr>
<tr>
<td>M0241</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -507.000</td>
</tr>
<tr>
<td>M0242</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -503.875</td>
</tr>
<tr>
<td>M0243</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -504.500</td>
</tr>
<tr>
<td>M0244</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -505.125</td>
</tr>
<tr>
<td>M0245</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -506.375</td>
</tr>
<tr>
<td>M0246</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -507.625</td>
</tr>
<tr>
<td>M0247</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -508.250</td>
</tr>
<tr>
<td>M0248</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -508.875</td>
</tr>
<tr>
<td>M0249</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -509.500</td>
</tr>
<tr>
<td>0250-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -510.125</td>
</tr>
<tr>
<td>0251-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -510.750</td>
</tr>
<tr>
<td>0252-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -511.375</td>
</tr>
<tr>
<td>0253-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -512.000</td>
</tr>
<tr>
<td>0254-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -512.625</td>
</tr>
<tr>
<td>0255-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -513.250</td>
</tr>
<tr>
<td>M0256</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -513.875</td>
</tr>
<tr>
<td>M0257</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -514.500</td>
</tr>
<tr>
<td>M0258</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -515.125</td>
</tr>
<tr>
<td>M0259</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -515.750</td>
</tr>
<tr>
<td>0260-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -516.375</td>
</tr>
<tr>
<td>0261-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -517.000</td>
</tr>
<tr>
<td>0262-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -517.625</td>
</tr>
<tr>
<td>0263-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -518.250</td>
</tr>
<tr>
<td>0264-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -518.875</td>
</tr>
<tr>
<td>0265-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -519.500</td>
</tr>
<tr>
<td>M0266</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -520.125</td>
</tr>
<tr>
<td>M0267</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -520.750</td>
</tr>
<tr>
<td>M0268</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -521.375</td>
</tr>
<tr>
<td>M0269</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -522.000</td>
</tr>
<tr>
<td>0270-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -522.625</td>
</tr>
<tr>
<td>0271-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -523.250</td>
</tr>
<tr>
<td>0272-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -523.875</td>
</tr>
<tr>
<td>0273-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -524.500</td>
</tr>
<tr>
<td>0274-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -525.125</td>
</tr>
<tr>
<td>0275-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -525.750</td>
</tr>
<tr>
<td>M0276</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -526.375</td>
</tr>
<tr>
<td>M0277</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -527.000</td>
</tr>
<tr>
<td>M0278</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -527.625</td>
</tr>
<tr>
<td>M0279</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -528.250</td>
</tr>
<tr>
<td>M0280</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -528.875</td>
</tr>
<tr>
<td>M0281</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -529.500</td>
</tr>
<tr>
<td>0282-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -530.125</td>
</tr>
<tr>
<td>0283-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -530.750</td>
</tr>
<tr>
<td>0284-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -531.375</td>
</tr>
<tr>
<td>0285-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -532.000</td>
</tr>
<tr>
<td>M0286</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -532.625</td>
</tr>
<tr>
<td>M0287</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -533.250</td>
</tr>
<tr>
<td>M0288</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -533.875</td>
</tr>
<tr>
<td>M0289</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -534.500</td>
</tr>
<tr>
<td>M0290</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -535.125</td>
</tr>
<tr>
<td>M0291</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -535.750</td>
</tr>
<tr>
<td>M0292</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -536.375</td>
</tr>
<tr>
<td>M0293</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -537.000</td>
</tr>
<tr>
<td>M0294</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -537.625</td>
</tr>
<tr>
<td>M0295</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -538.250</td>
</tr>
<tr>
<td>M0296</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -792.500</td>
</tr>
<tr>
<td>M0297</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -795.000</td>
</tr>
<tr>
<td>M0298</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -797.500</td>
</tr>
<tr>
<td>M0299</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -800.000</td>
</tr>
<tr>
<td>M0300</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -802.500</td>
</tr>
<tr>
<td>M0301</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -805.000</td>
</tr>
<tr>
<td>M0302</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -807.500</td>
</tr>
<tr>
<td>0303-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -810.000</td>
</tr>
<tr>
<td>0304-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -812.500</td>
</tr>
<tr>
<td>0305-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -815.000</td>
</tr>
<tr>
<td>M0306</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -817.500</td>
</tr>
<tr>
<td>M0307</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -820.000</td>
</tr>
<tr>
<td>M0308</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -822.500</td>
</tr>
<tr>
<td>M0309</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -825.000</td>
</tr>
<tr>
<td>M0310</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -827.500</td>
</tr>
<tr>
<td>M0311</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -830.000</td>
</tr>
<tr>
<td>0312-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -832.500</td>
</tr>
<tr>
<td>0313-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -835.000</td>
</tr>
<tr>
<td>M0314</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -837.500</td>
</tr>
<tr>
<td>M0315</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -840.000</td>
</tr>
<tr>
<td>M0316</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -842.500</td>
</tr>
<tr>
<td>M0317</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -845.000</td>
</tr>
<tr>
<td>M0318</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -847.500</td>
</tr>
<tr>
<td>M0319</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -850.000</td>
</tr>
<tr>
<td>M0320</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -852.500</td>
</tr>
<tr>
<td>M0321</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -855.000</td>
</tr>
<tr>
<td>M0322</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -857.500</td>
</tr>
<tr>
<td>M0323</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -860.000</td>
</tr>
<tr>
<td>0324-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -862.500</td>
</tr>
<tr>
<td>0325-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -865.000</td>
</tr>
<tr>
<td>M0326</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -867.500</td>
</tr>
<tr>
<td>M0327</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -870.000</td>
</tr>
<tr>
<td>M0328</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -872.500</td>
</tr>
<tr>
<td>M0329</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -875.000</td>
</tr>
<tr>
<td>0330-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -877.500</td>
</tr>
<tr>
<td>0331-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -880.000</td>
</tr>
<tr>
<td>M0332</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -882.500</td>
</tr>
<tr>
<td>0333-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -885.000</td>
</tr>
<tr>
<td>0334-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -887.500</td>
</tr>
<tr>
<td>0335-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -890.000</td>
</tr>
<tr>
<td>M0336</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -892.500</td>
</tr>
<tr>
<td>M0337</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -895.000</td>
</tr>
<tr>
<td>M0338</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -897.500</td>
</tr>
<tr>
<td>M0339</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -900.000</td>
</tr>
<tr>
<td>M0340</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -902.500</td>
</tr>
<tr>
<td>0341-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -905.000</td>
</tr>
<tr>
<td>0342-</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -907.500</td>
</tr>
<tr>
<td>M0343</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -910.000</td>
</tr>
<tr>
<td>M0344</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -912.500</td>
</tr>
<tr>
<td>M0345</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -915.000</td>
</tr>
<tr>
<td>M0346</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -917.500</td>
</tr>
<tr>
<td>M0347</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -920.000</td>
</tr>
<tr>
<td>M0348</td>
<td>ImagePositionPatient</td>
<td>[3] -150.300, -100.000, -922.500</td>
</tr>
</tbody>
</table>
</div>

---

## Post #2 by @lassoan (2019-06-12 18:31 UTC)

<p>In DICOM data sets, file names are ignored. Image slices are placed in position and orientation prescribed by “image position patient” and “image orientation patient” fields embedded in the file.</p>
<aside class="quote no-group" data-username="Jragher" data-post="1" data-topic="7142">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/3da27b/48.png" class="avatar"> Jragher:</div>
<blockquote>
<p>I just would like to have “blank” slices in the coordinate where there is no acquisition. With regularization activated, there is no distorsion but Slicer make weird stuff between the areas.</p>
</blockquote>
</aside>
<p>If slices are not spaced equally then you have no other option than enabling regularization. If there are artifacts then most probably the frames contain inconsistent information (image content is not consistent with its position and orientation). You may inspect the files using DICOM browser / Metadata feature to identify offending frames, remove them, clear the database, and re-import the data set without the inconsistent frames.</p>

---

## Post #3 by @Jragher (2019-06-13 06:12 UTC)

<p>Thanks very much. I’ll go through this process then.<br>
appriciate your feedbacks, helps a lot.<br>
JR</p>

---

## Post #4 by @Jragher (2019-06-13 11:56 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, I tried to have a look but didn’t find anything satisfying. However I really don’t understand why Slicer is trying to reconstruct something beetween -91,5 / - 383,250 and -538.250 / -792.5 as there is no slices. may be I misunderstand what he is doing…<br>
Finaly the “harden transform” and and the “segment editor” are impossible to use. Slicer freezes everytime I lunch theses module with this scene. Normaly it works perfectly.</p>
<p>Thanks again for your insights,<br>
Sincerely,</p>
<p>JR</p>

---

## Post #5 by @Jragher (2019-06-27 12:50 UTC)

<p>Hi Slice community,</p>
<p>If anyone has some advice or things I could try…<br>
The fact is that we have an MRI with different slices height and gaps between each body part ie: Ankle with slices height 1 --&gt; blank --&gt; knee with slices height 2 --&gt; blank --&gt; hip with slices height 3. I tried to check if there were inconsistencies as <a class="mention" href="/u/lassoan">@lassoan</a> suggested but everything seems ok except that Slicer is trying to “make” slices in the gaps which causes problems I think. Is there a way in the regularization process to indicate not to “fill” the gaps?<br>
Regards,</p>
<p>JR</p>

---

## Post #6 by @lassoan (2019-06-27 13:54 UTC)

<aside class="quote no-group" data-username="Jragher" data-post="4" data-topic="7142">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/3da27b/48.png" class="avatar"> Jragher:</div>
<blockquote>
<p>Finaly the “harden transform” and and the “segment editor” are impossible to use. Slicer freezes everytime I lunch theses module with this scene. Normaly it works perfectly.</p>
</blockquote>
</aside>
<p>Depending on how large the image is and how much memory you have, you may need to wait a very long time.</p>
<aside class="quote no-group" data-username="Jragher" data-post="4" data-topic="7142">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/3da27b/48.png" class="avatar"> Jragher:</div>
<blockquote>
<p>why Slicer is trying to reconstruct something beetween -91,5 / - 383,250 and -538.250 / -792.5 as there is no slices</p>
</blockquote>
</aside>
<p>One image series is always loaded as one contiguous block of image. If you want to load them separately then they should have saved as separate image series. You might be able to load subvolumes by series time, if you enable menu: Edit / Application settings / DICOM / “Allow loading subseries by time” and enable Advanced mode in DICOM module. You may also split the volume manually by moving selected image slices into separate subfolders and loading them using “Add data” (instead of DICOM module), because “Add data” only looks into the current folder.</p>

---
