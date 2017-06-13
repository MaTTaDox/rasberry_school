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

        $page = $this->request->get('page', 1);
        $itemsPerPage = $this->request->get('itemsPerPage', 50);

        $offset = ($page * $itemsPerPage) - $itemsPerPage;

        $mysql = new \MySQLi("localhost", "root", "abcD123", "readings");
        $query = $mysql->query("SELECT SQL_CALC_FOUND_ROWS * FROM `values` as v INNER JOIN locations as l 
                                  WHERE l.id = v.location_id LIMIT " . $itemsPerPage . " OFFSET " . $offset);

        $total = $mysql->query("SELECT FOUND_ROWS() as foundRows")->fetch_assoc()['foundRows'];


        $results = [];
        while ($row = $query->fetch_assoc())
        {
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
