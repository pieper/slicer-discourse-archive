---
topic_id: 4952
title: "Plus Using The Transform Embedded In Openigtlink Image Messa"
date: 2018-12-04
url: https://discourse.slicer.org/t/4952
---

# Plus : using the transform embedded in OpenIGTLink "IMAGE" messages

**Topic ID**: 4952
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/plus-using-the-transform-embedded-in-openigtlink-image-messages/4952

---

## Post #1 by @Tiffas (2018-12-04 13:19 UTC)

<p>Hi,</p>
<p>I am trying to use the transform embedded in OpenIGTLink “IMAGE” messages. In the Plus documentation about OpenIGTLink devices, it is specified about the <strong>ImageMessageEmbeddedTransformName</strong> attribute that :<br>
<em><strong>ImageMessageEmbeddedTransformName</strong> If IMAGE message is received and this attribute is defined then the transform embedded in the message will be recorded as a transform, with the specified name (e.g., “ImageToReference”).</em></p>
<p>So I tried the following xml file:</p>

<pre><code>&lt;DataCollection StartupDelaySec="1.0" &gt;

	&lt;DeviceSet 
		Name="PlusServer: Verasonics image sending"
		Description="Broadcasting acquired ultrasound video acquired on the Verasonics system through OpenIGTLink" /&gt;

		&lt;Device
			Id="Verasonics"
			Type="OpenIGTLinkVideo"        
			MessageType="IMAGE"
			ServerAddress="172.31.1.2"
			ServerPort="18944"
			IgtlMessageCrcCheckEnabled="false"
			ReconnectOnReceiveTimeout="false"
			UseReceivedTimestamps="false"
			AcquisitionRate="40"
			ReceiveTimeoutSec="30"
			SendTimeoutSec="30"
			ImageMessageEmbeddedTransformName="ImageToReference"&gt;
			&lt;DataSources&gt;
				&lt;DataSource Type="Video" Id="Video" PortUsImageOrientation="MF"  /&gt;
			&lt;/DataSources&gt;
			&lt;OutputChannels&gt;
				&lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video" /&gt;
			&lt;/OutputChannels&gt;
		&lt;/Device&gt; 

&lt;/DataCollection&gt;

&lt;PlusOpenIGTLinkServer 
	MaxNumberOfIgtlMessagesToSend="1" 
	MaxTimeSpentWithProcessingMs="50" 
	ListeningPort="18944" 
	SendValidTransformsOnly="true" 
	OutputChannelId="VideoStream" &gt; 
	&lt;DefaultClientInfo&gt; 
		&lt;MessageTypes&gt; 
			&lt;Message Type="IMAGE" /&gt;
		&lt;/MessageTypes&gt;
		&lt;ImageNames&gt;
			&lt;Image Name="Image" EmbeddedTransformToFrame="Reference" /&gt;
		&lt;/ImageNames&gt;
	&lt;/DefaultClientInfo&gt;
&lt;/PlusOpenIGTLinkServer&gt;
</code></pre>

<p>With this setup file I have the following error :</p>
<p>|ERROR|075.812595| Unable to get custom transform status from name: ImageToReferenceTransformStatus| in /home/ldaunizeau/Devel/PlusServer/PlusBuild/PlusLib/src/PlusCommon/PlusTrackedFrame.cxx(488)</p>
<p>I don’t know what transform status are and I found no clue in the Plus documentation.<br>
Thanks for your help !</p>

---

## Post #2 by @lassoan (2018-12-04 13:47 UTC)

<p>Please submit this question to the <a href="https://github.com/PlusToolkit/PlusLib/issues/new" rel="nofollow noopener">Plus issue tracker</a>. Attach the complete error log, because the root cause of the error might be shown in the few lines preceding the final error message that you included.</p>

---

## Post #3 by @Tiffas (2019-02-25 18:04 UTC)

<p>Hi, I have no news from Github, can you help ? Thanks a lot !</p>

---

## Post #4 by @Tiffas (2019-03-08 13:20 UTC)

<p>Related to: <a href="https://github.com/PlusToolkit/PlusLib/issues/504" rel="nofollow noopener">https://github.com/PlusToolkit/PlusLib/issues/504</a> and <a href="https://github.com/PlusToolkit/PlusLib/issues/459" rel="nofollow noopener">https://github.com/PlusToolkit/PlusLib/issues/459</a>. Plus perform some checks on the “transformStatus” field which appeared with OpenIGTLink version 3 and does not exist in previous version of OpenIGTLink.</p>

---
