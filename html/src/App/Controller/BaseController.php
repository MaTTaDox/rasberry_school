<?php

namespace App\Controller;


use App\Lib\Path;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

abstract class BaseController
{
    protected $mysql;

    protected $request;

    public function __construct(Request $request)
    {
        $this->request = $request;
        $this->mysql = new \MySQLi("localhost", "root", "abcD123", "readings");
    }

    public function render($path, array $params)
    {

        $loader = new \Twig_Loader_Filesystem(Path::getRootDir()."/resources/twig");
        $twig = new \Twig_Environment($loader, array(
           # 'cache' => '/path/to/compilation_cache',
        ));

        $template = $twig->load($path);


        return new Response($template->render($params));
    }
}