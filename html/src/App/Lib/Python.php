<?php
/**
 * Created by IntelliJ IDEA.
 * User: dmalsch
 * Date: 30.03.17
 * Time: 13:20
 */

namespace App\Lib;


class Python
{

    public static function run($command){

        $exec = "ssh pi@localhost \"/usr/bin/python ".addslashes($command)." \" 2>&1 ";
        return shell_exec($exec);
    }

}