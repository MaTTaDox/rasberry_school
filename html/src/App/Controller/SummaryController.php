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

class SummaryController extends BaseController
{

    /**
     * @return Response
     */
    public function base(){

        return $this->render("summary.twig",[]);

    }

    public function summaryByLocation($locationId)
    {
        $query = $this->mysql->query("SELECT MAX(`value`) as max, MIN(`value`) as min, AVG(`value`) as avg, unit FROM `values` WHERE location_id = ".(int)$locationId." GROUP BY unit");

        $results = [];

        while($row = $query->fetch_assoc()){
            $results[$row['unit']] = $row;
        }

        $query = $this->mysql->query("SELECT `value`, unit FROM `values` WHERE location_id =  ".(int)$locationId);

        while($row = $query->fetch_assoc()){
            $results[$row['unit']]['values'][] = $row['value'];
        }

        return new JsonResponse($results);
    }

}
