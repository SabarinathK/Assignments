text = '''
<html>

<body>
<h3><span>VM created</span></h3>
<table border="1" cellpadding="0" width="100%" style="width: 100.0%; border:dotted black
1.0pt">
<tbody>
<tr>
<td style="border:none; background:#27AE60; padding:.75pt .75pt .75pt 3.75pt">
<p><b><span style="font-size:11.Opt; color:white;
text-transform:uppercase">Details</span></b></p>
</td>
</tr>
<tr>
<td style="border:none; padding:.75pt .75pt .75pt .75pt">
<h4><span>VM Name: {{hostName}}</span></h4>
<ul type="disc">
<li><span>Type: {{provider}}</span></li>
<li><span>Region: {{region}}</span></li>
</ul>
</td>
</tr>
</tbody>
</table>
</body>

</html>
'''

file = open("index.html","w")
file.write(text)
file.close()