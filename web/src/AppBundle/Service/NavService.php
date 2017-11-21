<?php
/**
 * Created by IntelliJ IDEA.
 * User: dmalsch
 * Date: 03.08.17
 * Time: 16:09
 */

namespace AppBundle\Service;


use AppBundle\Controller\BaseController;
use Symfony\Component\DependencyInjection\ContainerInterface;
use Symfony\Component\HttpFoundation\RequestStack;

class NavService
{
    protected $container;

    protected $stack;


    function __construct(ContainerInterface $container, RequestStack $stack)
    {
        $this->container = $container;
        $this->stack = $stack;
    }

    public function getActiveTab()
    {
        $request = $this->stack->getMasterRequest();
        list($controller,$method) = explode("::",$request->get("_controller"));

        $controllerObj = new $controller;
        if(!$controllerObj instanceof BaseController){
            return null;
        }

        $active = $controllerObj::activeNavTab();

        if(is_array($active)){
            if(!isset($active[$method]))
            {
                return null;
            }
            return $active[$method];
        }

        return $active;
    }



}