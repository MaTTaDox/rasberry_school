<?php

namespace AppBundle\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Request;

class DefaultController extends Controller
{
    /**
     * @Route("/", name="homepage")
     */
    public function indexAction(Request $request)
    {
        if(!$this->isGranted('IS_AUTHENTICATED_REMEMBERED') ) {
            return $this->render('default/login.html.twig', []);
        }

        return $this->render('default/main.html.twig', []);
    }
}
