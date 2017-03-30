<?php
/**
 * Created by IntelliJ IDEA.
 * User: dmalsch
 * Date: 30.03.17
 * Time: 13:20
 */

namespace App\Lib;


class Path
{

    public static function getRootDir()
    {
        return dirname(__DIR__)."../";
    }

}