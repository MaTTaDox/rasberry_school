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

class DefaultController extends BaseController
{

    /**
     * @return Response
     */
    public function base(){

        return $this->render("main.twig",[]);

    }

    public function listReadingValues(){

            $page = $this->request->get('page',1);
            $itemsPerPage = $this->request->get('itemsPerPage',50);

            $offset = ($page * $itemsPerPage) - $itemsPerPage;

            $mysql = new \mysqli("localhost","root","abcD123","readings");

            $query = $mysql->prepare("SELECT SQL_CALC_FOUND_ROWS * FROM `values` as v INNER JOIN locations as l 
                                  WHERE l.id = v.location_id LIMIT ? OFFSET ?");
            $query->bind_param("ii", $itemsPerPage, $offset);

            $query->execute();

            $total = $query->num_rows;

            $results = [];
            $result = $query->get_result();
            while($row = $result->fetch_assoc()){
                $results[] = $row;
            }


        return new JsonResponse([
            "page" => $page,
            "itemsPerPage" => $itemsPerPage,
            "total" => $total,
            "results" => $results
        ]);
    }

}
