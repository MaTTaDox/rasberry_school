<?php

namespace AppBundle\Controller;

use AppBundle\Service\NavService;
use Symfony\Component\HttpFoundation\Request;

class NavigationController extends BaseController
{

    public function mainAction(Request $request)
    {
        /** @var NavService $navService */
        $navService = $this->get(NavService::class);

        // replace this example code with whatever you need
        return $this->render('default/nav.html.twig', [
            'active' => $navService->getActiveTab(),
        ]);
    }

}
