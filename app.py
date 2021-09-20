<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Top Greek gods</title>

    <!-- Bootstrap and Bootswatch CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/minty/bootstrap.min.css">

    <!-- Javascript -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js" integrity="sha384-LtrjvnR4Twt/qOuYxE721u19sVFLVSA4hf/rRt6PrZTmiPltdZcI7q7PXQBYTKyf" crossorigin="anonymous"></script>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="data.js"></script>
    <script src="plots.js"></script>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container-fluid">
            <a class="navbar-brand" href="index.html">HOME</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-bs-target="#navbarColor03" aria-controls="navbarColor03" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
        </div>
    </nav>

    <div class="container-fluid d-flex justify-content-center">
        <div class="row">
            <div class="col-md-12">
                <h1>My Greek/Roman God Dashboard</h1>
            </div>
        </div>
    </div>
    <div class="container-fluid d-flex justify-content-center">
        <div class="row">
            <div class="col-md-12">
                <div class="card border-primary mb-3">
                    <div class="card-header">Filters</div>
                    <div class="card-body">
                        <div id="filters">
                            <div class="container-fluid">
                                <div class="row">
                                    <div class="col-md-6 form-group">
                                        <label class="col-form-label col-form-label-lg mt-4" for="minSearches">Min Searches</label>
                                        <input class="form-control form-control-lg" type="number" placeholder="" id="minSearches">
                                    </div>
                                    <div class="col-md-6 form-group">
                                        <label class="col-form-label col-form-label-lg mt-4" for="maxResults">Max Results</label>
                                        <input class="form-control form-control-lg" type="number" placeholder="" id="maxResults">
                                    </div>
                                </div>
                            </div>
                            <button type="button" class="btn btn-primary" id="filter_btn">Filter!</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12">
                <div id="plot"></div>
            </div>
        </div>
    </div>
</body>

</html>