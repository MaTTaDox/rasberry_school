<?php

namespace AppBundle\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Component\HttpFoundation\Request;

class UserController extends BaseController
{
    /**
     * @Route("/users/add", name="addUser")
     */
    public function addAction(Request $request)
    {

        return $this->render('default/main.html.twig', []);
    }

    public static function activeNavTab()
    {
        return "home";
    }
}
