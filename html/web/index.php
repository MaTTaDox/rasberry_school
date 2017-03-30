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

$app->get('/', function (\Symfony\Component\HttpFoundation\Request $request) {
    $controller = new App\Controller\DefaultController($request);
    return $controller;
});
$app->run();