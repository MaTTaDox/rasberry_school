<?php
// web/index.php
require_once __DIR__.'/../vendor/autoload.php';

use Symfony\Component\ClassLoader\ClassLoader;

$loader = new ClassLoader();

// to enable searching the include path (eg. for PEAR packages)
$loader->setUseIncludePath(true);


$loader->addPrefix("App",__DIR__.'/../src');
// ... register namespaces and prefixes here - see below
$loader->register();




$app = new Silex\Application();

$app['debug'] = true;


//Main
$app->get('/', function (\Symfony\Component\HttpFoundation\Request $request) {
    $controller = new App\Controller\DefaultController($request);
    return $controller->base();
});

$app->get("/api/readings", function (\Symfony\Component\HttpFoundation\Request $request) {
    $controller = new App\Controller\DefaultController($request);
    return $controller->listReadingValues();
});

//Summary
$app->get('/summary', function (\Symfony\Component\HttpFoundation\Request $request) {
    $controller = new App\Controller\SummaryController($request);
    return $controller->base();
});

//Summary
$app->get('/api/summary/{locationId}', function (\Symfony\Component\HttpFoundation\Request $request, $locationId) {
    $controller = new App\Controller\SummaryController($request);
    return $controller->summaryByLocation($locationId);
});

//Locations
$app->get('/api/locations', function (\Symfony\Component\HttpFoundation\Request $request) {
    $controller = new App\Controller\LocationController($request);
    return $controller->locations();
});

$app->run();
