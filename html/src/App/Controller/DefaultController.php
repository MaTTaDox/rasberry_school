<?php
/**
 * Created by IntelliJ IDEA.
 * User: dmalsch
 * Date: 30.03.17
 * Time: 13:07
 */

namespace App\Controller;


use App\Lib\Path;
use App\Lib\Python;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;

class DefaultController extends BaseController
{

    /**
     * @return Response
     */
    public function base(){

        return $this->render("main.twig",[]);

    }

    public function display(){
            $message = $this->request->get("m");

            if (strlen($message))
            {

                $x = Path::getRootDir() . "/../python/display_string.py \"" . $message . "\"";
                Python::run($x);

            }

        return new JsonResponse(["success" => true]);
    }

}
