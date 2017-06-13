<?php
/**
 * Created by IntelliJ IDEA.
 * User: dmalsch
 * Date: 30.03.17
 * Time: 13:07
 */

namespace App\Controller;

use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Response;

class LocationController extends BaseController
{


    public function locations()
    {
        $query = $this->mysql->query("SELECT * FROM `locations`");

        $results = [];
        while ($row = $query->fetch_assoc())
        {
            $results[] = $row;
        }


        return new JsonResponse($results);
    }

}
