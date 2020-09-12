<!DOCTYPE html>
<html>
<head>
	<title>JobLister</title>
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<link rel="stylesheet" href="css/styles.css">
</head>
<body>
	<div class="container">
      <div class="header clearfix">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
					<div class="collapse navbar-collapse" id="navbarColor02">
    				<ul class="navbar-nav mr-auto">
      				<li class="nav-item">
        				<a class="nav-link" href="index.php">Home <span class="sr-only">(current)</span></a>
      				</li>
							<li class="nav-item">
        				<a class="nav-link" href="create.php">Create Listing</a>
      				</li>
						</ul>	
					</div>
        </nav>
        <h3 class="text-muted"><?php echo SITE_TITLE; ?></h3>
      </div>
      <?php displayMessage(); ?>
