<?php
/**
 * Created by IntelliJ IDEA.
 * User: dmalsch
 * Date: 30.03.17
 * Time: 13:07
 */

namespace App\Controller;


use Symfony\Component\HttpFoundation\Response;

class DefaultController extends BaseController
{

    /**
     * @return Response
     */
    public function base(){

        return $this->render("main.twig",[]);

    }

}