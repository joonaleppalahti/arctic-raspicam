 <!DOCTYPE html>
<html>
<head>
 <meta http-equiv="X-UA-Compatible" content="IE=Edge,">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <meta charset="UTF-8">
 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
 <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
 <link rel="stylesheet" type="text/css" href="style.css">
<title>Arctic Raspicam Videos</title>
</head>
<body>
<nav class="navbar navbar-inverse">
  <div class="container-fluid">
	<a id="brand" class="navbar-brand" href="/index.html">Arctic</a>
	 <ul class="nav navbar-nav">
        	<li><a href="/ArcticWeb/img/old/">Archive</a></li>
      	</ul>
 </div>
</nav>
	<?php
		$doc_dir = '/var/www/html/ArcticWeb/img/';
		foreach(glob("img/*.mp4") as $file) {
  		echo "<ul><video controls><source src='$file' type='video/mp4'></video>
		</ul>", PHP_EOL;
		}
	?>
</body>
</html>
