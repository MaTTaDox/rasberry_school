<?php
// src/AppBundle/Repository/UserRepository.php
namespace AppBundle\Repository;

use Symfony\Bridge\Doctrine\Security\User\UserLoaderInterface;
use Doctrine\ORM\EntityRepository;

class UserRepository extends EntityRepository implements UserLoaderInterface
{

    public function loadUserByUsername($username)
    {
        return $this->createQueryBuilder('u')
            ->where('u.username = :username OR u.email = :email')
            ->setParameter('username', $username)
            ->setParameter('email', $username)
            ->getQuery()
            ->getOneOrNullResult();
    }

    public function loadByRFID($rfid)
    {
        return $this->createQueryBuilder('u')
            ->where('u.rfid = :rfid')
            ->setParameter('rfid', $rfid)
            ->getQuery()
            ->getOneOrNullResult();
    }
}