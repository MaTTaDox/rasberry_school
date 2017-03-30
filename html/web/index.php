<?php
// web/index.php
require_once __DIR__.'/../vendor/autoload.php';

$app = new Silex\Application();

$app->get('/', function (\Symfony\Component\HttpFoundation\Request $request) {
    $controller = new \Controller\DefaultController($request);
    return $controller;
});
$app->run();