<?php
/**
 * Created by IntelliJ IDEA.
 * User: dmalsch
 * Date: 30.03.17
 * Time: 13:07
 */

namespace App\Controller;


use App\Lib\Path;
use Symfony\Component\HttpFoundation\Response;

class DefaultController extends BaseController
{

    /**
     * @return Response
     */
    public function base(){

        $message = $this->request->get("m");

        if(strlen($message)){

            $exec = "python ".Path::getRootDir()."/../python/display_string.py \"".$message."\"";
            var_dump(exec($exec));
            
        }


        return $this->render("main.twig",[]);

    }

}